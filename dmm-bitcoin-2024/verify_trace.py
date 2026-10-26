#!/usr/bin/env python3
"""Check the saved DMM explorer snapshot offline; Python standard library only.

Validates capture integrity, agreement on transaction fields, exact UTXO
continuity, satoshi conservation, and the published destination set. This does
not validate Bitcoin consensus/signatures or establish real-world ownership.
"""

import hashlib
import json
from pathlib import Path

SEED = "975ec405ac9dc9fa5ab8009d94d6a1fe31dff8a8127ea90d023104e52754e4d7"
RECIPIENT = "1B6rJRfjTXwEy36SCs5zofGMmdv2kdZw7P"
PUBLISHED_DESTINATIONS = {
    "bc1qx6jpnnfjrfcx9ehhdmj7qqyzpyd8pek00trrq7",
    "bc1qrtltlc7zjzj3knde2tqjt7tl2p5l2keh4l2uka",
    "bc1qr4vnu4f4tl3gwfxt6a5hgt6vuusgsd0j2cnz74",
    "bc1qgcv2j80009apvjekph40wagwutfu6l3gcm2fw0",
    "bc1qegcazuxnp5wxxxamdqvjv345fpve6656vpjln4",
    "bc1q7p3atj3v95k4pd7qxnnqlhjwu843ty2hqn9gy0",
    "bc1q3ur23g02rq5w0x6y8vek3xradjgs080nzksfje",
    "bc1q2u9m2eqy8glvrjeqr5sceqngpad6dnxrtyxlf3",
    "bc1q2tu4dxyvnaquar96mj99yqjanfzgg3fv4gzytd",
    "bc1q7pdecv2raf3x84unxlv9ghtpjfpwlam6dx27xd",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def comparable(tx):
    return {
        "txid": tx["txid"],
        "version": tx["version"],
        "locktime": tx["locktime"],
        "inputs": [
            (i["txid"], i["vout"], i["prevout"]["value"],
             i["prevout"]["scriptpubkey"], i["prevout"].get("scriptpubkey_address"))
            for i in tx["vin"]
        ],
        "outputs": [
            (o["value"], o["scriptpubkey"], o.get("scriptpubkey_address"))
            for o in tx["vout"]
        ],
        "fee": tx["fee"],
        "status": tx["status"],
    }


def verify():
    path = Path(__file__).parent / "evidence" / "snapshot.json"
    snapshot = json.loads(path.read_text(encoding="utf-8"))
    captures = {}
    for record in snapshot["captures"]:
        raw = record["raw_json"].encode("utf-8")
        require(hashlib.sha256(raw).hexdigest() == record["sha256"],
                "Capture hash mismatch: " + record["file"])
        require(record["file"] not in captures, "Duplicate capture name")
        captures[record["file"]] = json.loads(raw)

    trace = []
    for item in snapshot["trace"]:
        label = item["label"]
        a = captures[label + "-mempool.json"]
        b = captures[label + "-blockstream.json"]
        require(a["txid"] == item["txid"], "Trace identifier mismatch")
        require(comparable(a) == comparable(b), "Explorer disagreement: " + label)
        values = [i["prevout"]["value"] for i in a["vin"]]
        outputs = [o["value"] for o in a["vout"]]
        require(all(type(v) is int and v >= 0 for v in values + outputs + [a["fee"]]),
                "Invalid satoshi amount: " + label)
        require(sum(values) == sum(outputs) + a["fee"], "Value mismatch: " + label)
        require(a["status"]["confirmed"], "Unconfirmed transaction: " + label)
        require(a["status"]["block_height"] == 845859, "Unexpected block: " + label)
        trace.append(a)

    require(len(trace) == 11 and trace[0]["txid"] == SEED, "Unexpected trace scope")
    seed = trace[0]
    require(len(seed["vin"]) == 9 and len(seed["vout"]) == 1, "Seed shape mismatch")
    require(seed["vout"][0]["scriptpubkey_address"] == RECIPIENT, "Seed recipient mismatch")
    require(seed["vout"][0]["value"] == 450290000000, "Seed amount mismatch")

    previous = seed
    terminal_outputs = []
    fees = 0
    seen_outpoints = set()
    for tx in trace[1:]:
        require(len(tx["vin"]) == 1, "Unexpected additional input")
        entry = tx["vin"][0]
        outpoint = (entry["txid"], entry["vout"])
        require(outpoint not in seen_outpoints, "Duplicate spent outpoint")
        seen_outpoints.add(outpoint)
        require(entry["txid"] == previous["txid"], "Broken transaction continuity")
        previous_output = previous["vout"][entry["vout"]]
        require(previous_output["scriptpubkey_address"] == RECIPIENT,
                "Trace left the initial recipient's remainder path")
        require(previous_output["value"] == entry["prevout"]["value"], "Prevout value mismatch")
        for index, output in enumerate(tx["vout"]):
            if output["scriptpubkey_address"] != RECIPIENT:
                terminal_outputs.append({"txid": tx["txid"], "vout": index,
                                         "address": output["scriptpubkey_address"],
                                         "sats": output["value"]})
        fees += tx["fee"]
        previous = tx

    require(all(o["scriptpubkey_address"] != RECIPIENT for o in previous["vout"]),
            "Unfinished remainder path")
    require(len(terminal_outputs) == 10, "Unexpected terminal output count")
    require({o["address"] for o in terminal_outputs} == PUBLISHED_DESTINATIONS,
            "Mismatch with published Beosin destination set")
    total = sum(o["sats"] for o in terminal_outputs)
    require(total + fees == seed["vout"][0]["value"], "Trace-wide accounting mismatch")
    return {"result": "PASS", "captured_responses": len(captures),
            "transactions_cross_checked": len(trace), "destination_outputs": len(terminal_outputs),
            "seed_output_sats": seed["vout"][0]["value"], "distribution_fee_sats": fees,
            "terminal_output_sats": total, "outputs": terminal_outputs}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
