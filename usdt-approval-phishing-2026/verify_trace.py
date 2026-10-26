#!/usr/bin/env python3
"""Verify the saved, bounded USDT trace offline using Python's standard library."""
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

USDT = '0xdac17f958d2ee523a2206206994597c13d831ec7'
VICTIM = '0x8c949361b49320c48a51f4b1c6f9f83862530f89'
SPENDER = '0x1178a87db6dc5c010e39a325af1f73bec6470502'
EXECUTOR = '0x6d8c070338ec3d297f1d0eceea296bd7e13a32b9'
A = '0xf84c62572eeafc90c0bce3fb6c85bcb573e68d93'
B = '0xc508a8c01bc3835be67e0e5554b7d91a1bb70da1'
TRANSFER = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
APPROVAL = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def address(value):
    return value['hash'].lower()


def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def word(data, offset):
    require(offset >= 0 and offset + 32 <= len(data), 'ABI word outside payload')
    return int.from_bytes(data[offset:offset + 32], 'big')


def abi_address(data, offset):
    value = word(data, offset)
    require(value < 2**160, 'Invalid ABI address padding')
    return '0x' + value.to_bytes(20, 'big').hex()


def transfer_from(raw):
    data = bytes.fromhex(raw.removeprefix('0x'))
    require(data[:4].hex() == '23b872dd' and len(data) == 100, 'Unexpected transferFrom ABI')
    return abi_address(data, 4), abi_address(data, 36), word(data, 68)


def multicall(raw):
    data = bytes.fromhex(raw.removeprefix('0x'))
    require(data[:4].hex() == 'caa5c23f', 'Unexpected multicall selector')
    data = data[4:]
    array = word(data, 0)
    count = word(data, array)
    require(count == 2, 'Expected two calls in this case')
    base = array + 32
    calls = []
    for i in range(count):
        start = base + word(data, base + i * 32)
        target = abi_address(data, start)
        payload = start + word(data, start + 32)
        length = word(data, payload)
        require(payload + 32 + length <= len(data), 'Truncated nested call')
        inner = '0x' + data[payload + 32:payload + 32 + length].hex()
        calls.append((target, *transfer_from(inner)))
    return calls


def raw_event(log):
    require(len(log['data']) == 66, 'Unexpected event data width')
    for topic in log['topics'][1:3]:
        require(topic[:26] == '0x' + '0' * 24, 'Invalid indexed address')
    return (address(log['address']), log['topics'][0],
            '0x' + log['topics'][1][-40:], '0x' + log['topics'][2][-40:],
            int(log['data'], 16), log['index'])


def verified_transfers(tx):
    return [(address(t['from']), address(t['to']), int(t['total']['value']), t['log_index'])
            for t in tx['token_transfers']
            if t['token']['address_hash'].lower() == USDT]


def run(snapshot):
    require(snapshot['chain_id'] == 1, 'Wrong chain')
    captures = snapshot['captures']
    data = {}
    for key, capture in captures.items():
        require(hashlib.sha256(capture['body'].encode()).hexdigest() == capture['sha256'],
                'Capture integrity mismatch: ' + key)
        data[key] = json.loads(capture['body'])

    # Etherscan facts were independently extracted from saved HTML, not copied from Blockscout.
    pairs = [('approval-tx', 'approval-etherscan', 'approval-logs'),
             ('first-drain-tx', 'first-drain-etherscan', 'first-drain-logs'),
             ('blockscout-tx', 'etherscan', 'drain-logs'),
             ('side-transfer-tx', 'side-transfer-etherscan', None)]
    for key, other, logs_key in pairs:
        tx, eth = data[key], data[other]
        require(tx['status'] == 'ok' and eth['status'] == 'Success', 'Transaction status mismatch')
        require(not tx['token_transfers_overflow'], 'Incomplete transfer summary')
        require((tx['hash'], tx['block_number'], tx['position'], timestamp(tx['timestamp']),
                 address(tx['from']), address(tx['to'])) ==
                (eth['hash'], eth['block_number'], eth['position'], timestamp(eth['timestamp']),
                 eth['sender'], eth['target']), 'Explorer transaction disagreement: ' + key)
        if logs_key:
            logs = data[logs_key]
            require(logs['next_page_params'] is None, 'Unfetched event page')
            require(all(log['transaction_hash'] == tx['hash'] for log in logs['items']), 'Wrong log transaction')
            observed = sorted(raw_event(log) for log in logs['items'])
            extracted = sorted((e['contract'], e['topic0'], e['first_address'], e['second_address'],
                                int(e['value_units']), e['index']) for e in eth['events'])
            require(observed == extracted, 'Explorer event disagreement: ' + key)
            transfers = [(f, t, value, index) for contract, topic, f, t, value, index in observed
                         if contract == USDT and topic == TRANSFER]
            require(sorted(transfers) == sorted(verified_transfers(tx)), 'Summary disagrees with raw logs')
        else:
            e = eth['events'][0]
            require(e['contract'] == USDT and e['topic0'] == TRANSFER, 'Wrong side-transfer asset')
            require(verified_transfers(tx) == [(e['first_address'], e['second_address'],
                                              int(e['value_units']), e['index'])], 'Side transfer disagreement')

    approval = data['approval-tx']
    require(address(approval['from']) == VICTIM and address(approval['to']) == USDT, 'Wrong approval parties')
    raw = bytes.fromhex(approval['raw_input'][2:])
    require(raw[:4].hex() == '095ea7b3' and len(raw) == 68, 'Wrong approval calldata')
    require(abi_address(raw, 4) == SPENDER and word(raw, 36) == 2**256 - 1, 'Wrong allowance')
    event = raw_event(data['approval-logs']['items'][0])
    require(event[:5] == (USDT, APPROVAL, VICTIM, SPENDER, 2**256 - 1), 'Approval log mismatch')
    require(not verified_transfers(approval), 'Approval incorrectly counted as a transfer')

    first, second = data['first-drain-tx'], data['blockscout-tx']
    expected_first = [(USDT, VICTIM, A, 200000000000), (USDT, VICTIM, B, 800000000000)]
    expected_second = [(USDT, VICTIM, A, 159999873783), (USDT, VICTIM, B, 639999495132)]
    require(multicall(first['raw_input']) == expected_first, 'First multicall mismatch')
    require(multicall(second['raw_input']) == expected_second, 'Second multicall mismatch')
    for tx in [first, second]:
        require(address(tx['from']) == EXECUTOR and address(tx['to']) == SPENDER, 'Wrong executor/spender')
        require(int(tx['gas_used']) * int(tx['gas_price']) == int(tx['fee']['value']), 'Gas accounting mismatch')
        require(int(tx['value']) == 0, 'Unexpected ETH value')

    # A successful outer transaction can contain a failed internal call.
    trace = data['first-raw-trace']
    outer = next(t for t in trace if t['traceAddress'] == [])
    require(not outer.get('error') and outer['action']['input'] == first['raw_input'], 'Wrong outer trace')
    calls = [t for t in trace if t['action'].get('to', '').lower() == USDT]
    require(len(calls) == 2, 'Unexpected internal calls')
    require([transfer_from(t['action']['input']) for t in calls] == [x[1:] for x in expected_first], 'Trace calldata mismatch')
    require(not calls[0].get('error') and calls[1].get('error') == 'invalid opcode: INVALID', 'Internal failure not established')
    require(data['first-drain-etherscan']['internal_error_present'], 'Internal error not corroborated')
    require(verified_transfers(first) == [(VICTIM, A, 200000000000, 4)], 'Failed call counted as completed')
    require(sorted(verified_transfers(second)) == sorted([(VICTIM, A, 159999873783, 168),
                                                        (VICTIM, B, 639999495132, 169)]), 'Second drain logs mismatch')

    totals = Counter()
    transfers = verified_transfers(first) + verified_transfers(second)
    for sender, receiver, units, _ in transfers:
        require(sender == VICTIM, 'Wrong loss origin')
        totals[receiver] += units
    require(dict(totals) == {A: 359999873783, B: 639999495132}, 'Recipient total mismatch')
    require(sum(totals.values()) == 999999368915 and len(transfers) == 3, 'Loss total/count mismatch')
    require(len({first['hash'], second['hash']}) == 2, 'Transaction count mismatch')
    require((timestamp(second['timestamp']) - timestamp(approval['timestamp'])).total_seconds() == 48, 'Timing mismatch')
    side = data['side-transfer-tx']
    require(verified_transfers(side) == [(VICTIM, '0xe3478b0bb1a5084567c319096437924948be1964', 631085, 43)], 'Side transfer mismatch')
    require((approval['block_number'], approval['position']) < (side['block_number'], side['position'])
            < (first['block_number'], first['position']) < (second['block_number'], second['position']), 'Sequence mismatch')

    spoof = data['spoof-tx']
    example = [t for t in spoof['token_transfers'] if address(t['from']) == VICTIM]
    require(len(example) == 1, 'Missing excluded-token example')
    require(example[0]['token']['symbol'] == 'USDT' and
            example[0]['token']['address_hash'].lower() == '0x4607094744786ec873ed9f8264d40433deaad755', 'Wrong look-alike token')
    require(int(example[0]['total']['value']) == 200000000000, 'Look-alike amount mismatch')
    require(not verified_transfers(spoof), 'Noncanonical token admitted to USDT trace')
    print('PASS: 13 capture hashes; 4 explorer transaction cross-checks; approval and raw-event decoding.')
    print('PASS: failed internal call excluded; look-alike token excluded; gas checked separately.')
    print('PASS: 2 drain transactions / 3 Transfer events / 2 recipients = 999,999.368915 USDT.')


if __name__ == '__main__':
    run(json.loads((Path(__file__).parent / 'evidence/snapshot.json').read_text()))
