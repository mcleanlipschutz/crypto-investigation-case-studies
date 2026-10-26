# Wallets and transactions

[Case overview](README.md) · [Triage workflow](triage-and-handoff.md) · [Sources](sources.md)

## Scope and verification

This is the seed plus the initial distribution, reconstructed from saved mempool.space and Blockstream API responses on October 26, 2026. The two providers agree on the compared transaction fields. Bitcoin transaction structure and value movement are verified through those explorers; case linkage and ownership attribution are separate questions. The study does not use a locally validating Bitcoin node.

## Seed transaction

[`975ec405ac9dc9fa5ab8009d94d6a1fe31dff8a8127ea90d023104e52754e4d7`](https://mempool.space/tx/975ec405ac9dc9fa5ab8009d94d6a1fe31dff8a8127ea90d023104e52754e4d7)

| Field | Value |
|---|---|
| Network / asset | Bitcoin mainnet / BTC |
| Input address | `3P8MfdM4pULv7ozdQvfwAqNF29zAjmnUYD` |
| Inputs | Nine UTXOs: one 503 BTC input and eight 500 BTC inputs |
| Gross input total | 4,503.00000000 BTC |
| Recipient, output index 0 | `1B6rJRfjTXwEy36SCs5zofGMmdv2kdZw7P` |
| Recipient output | 4,502.90000000 BTC |
| Transaction fee | 0.10000000 BTC |
| Block | 845859 |
| Block timestamp | 2024-05-31 04:12:49 UTC |

Whale Alert supplied the transaction candidate [S7](sources.md#s7). Beosin identifies the recipient in its incident analysis [S3](sources.md#s3). The exact amounts and outpoint linkage come from the explorer responses [S5](sources.md#s5), [S6](sources.md#s6). An explorer record alone does not label a transfer unauthorized or establish who controlled an address.

## Initial destination outputs

Each row is a distinct output reached by following the remainder at the initial recipient address. The transaction link and output index identify the outpoint. These are historical allocation amounts, not current balances or independent additional losses. Full transaction identifiers are listed below and retained in the snapshot.

| Step / transaction | Output index | Destination address | BTC |
|---|---:|---|---:|
| [D01](https://mempool.space/tx/f5e1f024f1b9c6e28395beb70e418a51dd15f566b2458cf001f82e3c521faadf) | 0 | `bc1q3ur23g02rq5w0x6y8vek3xradjgs080nzksfje` | 500.00000000 |
| [D02](https://mempool.space/tx/f4aa3f933aceade58a8b6c9392889f6b3db3a1a7db0f960126a4cb472e541c6e) | 0 | `bc1q2u9m2eqy8glvrjeqr5sceqngpad6dnxrtyxlf3` | 500.00000000 |
| [D03](https://mempool.space/tx/0886f137887dc79bdceafb60fa74d7f70bf08b03cbd836420b3eee7b50289973) | 0 | `bc1qegcazuxnp5wxxxamdqvjv345fpve6656vpjln4` | 500.00000000 |
| [D04](https://mempool.space/tx/af39be7c0ebb79e790c6de73b7946037ff45ae0c6172175ded569a3350a14857) | 0 | `bc1q7p3atj3v95k4pd7qxnnqlhjwu843ty2hqn9gy0` | 500.00000000 |
| [D05](https://mempool.space/tx/cfff68af782824bc9531488dd6f15a4fb913bab423685cb065581e7b0b8ec656) | 0 | `bc1qgcv2j80009apvjekph40wagwutfu6l3gcm2fw0` | 500.00000000 |
| [D06](https://mempool.space/tx/fc6cf5612f789869efae96e1673bb88182e938bf867552020664c631c6b2db72) | 0 | `bc1qr4vnu4f4tl3gwfxt6a5hgt6vuusgsd0j2cnz74` | 500.00000000 |
| [D07](https://mempool.space/tx/cb4c7fc266bbe640281483a2d1bea59474fc52c50a6008da535b212a7d590140) | 0 | `bc1qx6jpnnfjrfcx9ehhdmj7qqyzpyd8pek00trrq7` | 500.00000000 |
| [D08](https://mempool.space/tx/810b5a983845b05160432b2c6a203e9bd4f21c74287543fece62a062659f7ebf) | 0 | `bc1q2tu4dxyvnaquar96mj99yqjanfzgg3fv4gzytd` | 500.00000000 |
| [D09](https://mempool.space/tx/9402a584c1fd9a64b646f60b74db4a7a7288b226764aa1fc5554a24d09c59e85) | 1 | `bc1qrtltlc7zjzj3knde2tqjt7tl2p5l2keh4l2uka` | 500.00000000 |
| [D10](https://mempool.space/tx/61e556358bbd9450e6c2e4671bcdc1af3bb591ffb97cdc800d2610f626fcc92e) | 0 | `bc1q7pdecv2raf3x84unxlv9ghtpjfpwlam6dx27xd` | 2.89245200 |

The address set matches all ten addresses published by Beosin. That corroboration supports linkage to the incident; it does not make the addresses ten people, ten exchange accounts, or ten separately recoverable balances.

## Distribution transaction identifiers

- D01: `f5e1f024f1b9c6e28395beb70e418a51dd15f566b2458cf001f82e3c521faadf`
- D02: `f4aa3f933aceade58a8b6c9392889f6b3db3a1a7db0f960126a4cb472e541c6e`
- D03: `0886f137887dc79bdceafb60fa74d7f70bf08b03cbd836420b3eee7b50289973`
- D04: `af39be7c0ebb79e790c6de73b7946037ff45ae0c6172175ded569a3350a14857`
- D05: `cfff68af782824bc9531488dd6f15a4fb913bab423685cb065581e7b0b8ec656`
- D06: `fc6cf5612f789869efae96e1673bb88182e938bf867552020664c631c6b2db72`
- D07: `cb4c7fc266bbe640281483a2d1bea59474fc52c50a6008da535b212a7d590140`
- D08: `810b5a983845b05160432b2c6a203e9bd4f21c74287543fece62a062659f7ebf`
- D09: `9402a584c1fd9a64b646f60b74db4a7a7288b226764aa1fc5554a24d09c59e85`
- D10: `61e556358bbd9450e6c2e4671bcdc1af3bb591ffb97cdc800d2610f626fcc92e`

Each distribution transaction has one input. D01 spends seed output 0. D02–D09 spend the remainder output 1 of their immediate predecessor. D10 spends D09 output 0: the output order changes at D09. The verifier follows explicit input outpoints rather than assuming the last output is always change.

## Satoshi reconciliation

| Accounting item | Satoshis | BTC |
|---|---:|---:|
| Seed output / trace starting value | 450,290,000,000 | 4,502.90000000 |
| Nine 500 BTC allocations | 450,000,000,000 | 4,500.00000000 |
| Final allocation | 289,245,200 | 2.89245200 |
| Total initial destination allocations | 450,289,245,200 | 4,502.89245200 |
| Distribution fees: nine at 76,500 sats plus one at 66,300 sats | 754,800 | 0.00754800 |

The ten destination outputs plus distribution fees equal the seed output exactly. Including the seed fee, the entire bounded chain reconciles to 4,503 BTC of gross inputs. Summing every intermediate transfer as another loss would repeatedly count the same value.

No unrelated input is added along this captured distribution path. A FIFO, LIFO, or proportional allocation rule is therefore unnecessary within this boundary. If later transactions combine this value with other funds, the attribution method and its assumptions must be stated before extending case-value totals.

## Time and trace boundaries

All 11 captured transactions appear in block 845859 with block timestamp 2024-05-31 04:12:49 UTC. A shared block timestamp is not a precise broadcast time for each transaction and cannot establish a seconds-level response window. Input dependencies provide the order of the distribution.

The last outputs in this study may have been spent later. They are terminal only relative to the chosen trace boundary. No claim is made about present balances, all downstream recipients, mixer withdrawal matches, cross-chain continuity, service control, or recovery.

## Reproduce the checks

Run from the repository root:

```bash
python3 dmm-bitcoin-2024/verify_trace.py
```

The [snapshot](evidence/snapshot.json) preserves raw response text, SHA-256 hashes, source URLs, and UTC retrieval times. The [verifier](verify_trace.py) checks all capture hashes, compares the transaction fields across both providers, validates every spent-output link, reconciles amounts in integer satoshis, and compares the resulting destination set with the published address list. Hashes detect changes to the captured bytes; they are not certificates of source truth or evidence of ownership.
