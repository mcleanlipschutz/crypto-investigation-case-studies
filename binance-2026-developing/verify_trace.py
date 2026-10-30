"""Offline validation of the selected Binance incident trace. No network calls."""
from pathlib import Path
import csv,hashlib,json
from decimal import Decimal,localcontext
from datetime import datetime

P=Path(__file__).parent
TRANSFER='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
ASSETS={'ETH':('native',18),'USDT':('0xdac17f958d2ee523a2206206994597c13d831ec7',6),
        'USDC':('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',6),
        'RLUSD':('0x8292bb45bf1ee4d140127049757c2e0ff06317ed',18)}
def check(ok,message):
    if not ok:raise ValueError(message)
def run(snapshot):
    data={}
    for name,c in snapshot['captures'].items():
        check(hashlib.sha256(c['body'].encode()).hexdigest()==c['body_sha256'],'Changed capture: '+name)
        data[name]=json.loads(c['body'])
    for name in ['sweep','usdc','binance16','onward']:
        a,b=data[name],data[name+'-etherscan']
        check(a['status']=='ok' and b['status']=='Success','Unsuccessful transaction')
        for key in ['hash','block_number','from','to']:check(a[key]==b[key],'Explorer mismatch: '+key)
        check(datetime.fromisoformat(a['timestamp'].replace('Z','+00:00'))==datetime.fromisoformat(b['timestamp']),'Timestamp mismatch')
        check(int(a['gas_used'])*int(a['gas_price'])==int(a['fee']['value']),'Gas mismatch')
    check(data['sweep-logs']['next_page_params'] is not None,'Expected pagination')
    check(data['sweep-logs-2']['next_page_params'] is None,'Unfetched sweep log page')
    check(data['usdc-logs']['next_page_params'] is None,'Unfetched USDC log page')
    logs=data['sweep-logs']['items']+data['sweep-logs-2']['items']+data['usdc-logs']['items']
    keys=set()
    for e in snapshot['edges']:
        check((e['contract'],e['decimals'])==ASSETS[e['asset']],'Wrong asset identity')
        tx=data[e['capture_id']]; other=data[e['capture_id']+'-etherscan']
        check(e['tx_hash']==tx['hash'] and e['block_number']==tx['block_number'],'Wrong edge transaction')
        key=(1,e['tx_hash'],e['event_key'],e['contract']);check(key not in keys,'Duplicate movement');keys.add(key)
        with localcontext() as ctx:
            ctx.prec=80
            check(Decimal(e['raw_units'])/Decimal(10)**e['decimals']==Decimal(e['amount_exact']),'Decimal conversion mismatch')
        if e['event_key'].startswith('log:'):
            index=int(e['event_key'].split(':')[1])
            candidates=[l for l in logs if l['transaction_hash']==e['tx_hash'] and l['index']==index]
            check(len(candidates)==1,'Missing/duplicate log')
            l=candidates[0]
            check(l['topics'][0]==TRANSFER and l['contract']==e['contract'],'Wrong emitter/event')
            check('0x'+l['topics'][1][-40:]==e['source'] and '0x'+l['topics'][2][-40:]==e['target'],'Wrong log endpoints')
            check(int(l['data'],16)==int(e['raw_units']),'Raw log amount mismatch')
            ev=next(x for x in other['events'] if x['index']==index)
            check((ev['contract'],ev['from'],ev['to'],ev['units'])==(e['contract'],e['source'],e['target'],e['raw_units']),'Etherscan event mismatch')
        elif e['event_key']=='trace:0':
            tr=next(x for x in data['sweep-trace'] if x['traceAddress']==[0])
            check(not tr.get('error') and tr['result'] is not None,'Failed native transfer')
            check((tr['action']['from'],tr['action']['to'])==(e['source'],e['target']),'Native endpoints mismatch')
            check(int(tr['action']['value'],16)==int(e['raw_units']),'Native trace amount mismatch')
            check(Decimal(other['native_amount_exact'])==Decimal(e['amount_exact']),'Etherscan native amount mismatch')
        else:
            check((tx['from'],tx['to'],tx['value'])==(e['source'],e['target'],e['raw_units']),'Direct native movement mismatch')
            check(Decimal(other['native_amount_exact'])==Decimal(e['amount_exact']),'Etherscan native amount mismatch')
    auth=data['delegation']['authorization_list']
    check(len(auth)==50 and sum(x['status']=='ok' for x in auth)==1,'Authorization interpretation changed')
    check(sum(x['status']=='invalid_nonce' for x in auth)==49,'Nonce status mismatch')
    check(len(keys)==6,'Expected six starter movements')
    check(data['sweep']['token_transfers_overflow'],'Expected truncated sweep summary; do not infer complete token scope')
    check(next(e for e in snapshot['edges'] if e['asset']=='USDC')['source']!=data['usdc']['to'],'Token sender conflated with transaction target')
    return data
if __name__=='__main__':
    snapshot=json.loads((P/'evidence/snapshot.json').read_text());run(snapshot)
    rows=list(csv.DictReader((P/'edges.csv').open()))
    check(len(rows)==6,'CSV row count')
    for row,e in zip(rows,snapshot['edges']):
        check((row['Id'],row['Source'],row['Target'],row['AmountExact'],row['TxHash'])==
              (e['id'],'ethereum:'+e['source'],'ethereum:'+e['target'],e['amount_exact'],e['tx_hash']),'CSV disagrees with evidence')
    nodes=list(csv.DictReader((P/'nodes.csv').open()));ids={n['Id'] for n in nodes}
    check(all(r['Source'] in ids and r['Target'] in ids for r in rows),'Missing graph node')
    print('PASS: 13 extracted-body hashes; four explorer comparisons; six exact fund-flow edges; graph references.')
    print('PASS: token emitters, raw log amounts, native trace, gas, pagination, and delegation-status checks.')
    print('Scope: selected Ethereum transfers, not total incident loss, full downstream trace, or recovered funds.')
