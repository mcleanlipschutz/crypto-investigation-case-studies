# DMM Bitcoin 2024
## Bitcoin trace and triage case study

**Public-source reconstruction · Prepared October 26, 2026 · McLean Lipschutz**

This case study reconstructs the initial Bitcoin distribution following the DMM incident and explains how those findings would support triage and investigative handoff. It combines public reporting with transaction data checked against two Bitcoin explorers. It does not claim participation in the original investigation, identification of account holders, or recovery of stolen funds. Research, drafting, and data validation were assisted by AI; the sources, captured responses, and verification code are available for review.

## Executive finding

The seed transaction created a **4,502.9 BTC** output at the address identified by Beosin as the DMM attacker recipient. Ten subsequent transactions distributed that output into **nine 500 BTC outputs and one 2.892452 BTC output**, with **0.007548 BTC** paid in distribution fees. The ten destination addresses match Beosin's published set. This establishes a bounded transaction path; it does not prove the identity of whoever controlled the addresses. [S3](sources.md#s3), [S5](sources.md#s5), [S6](sources.md#s6)

The proposed triage disposition is **escalate for specialist tracing and incident coordination**. The trace offers concrete starting outpoints for follow-up, but no verified custodial endpoint or currently recoverable balance is established here.

## Incident context and chronology

DMM's reported loss was 4,502.9 BTC. In December 2024, the FBI, DC3, and Japan's NPA attributed the incident to North Korean TraderTraitor activity, estimating the loss at approximately $308 million at the time. That statement describes a compromise at wallet provider Ginco and a likely manipulation of a DMM transaction request. This is government attribution, not a conclusion derived from the transaction graph alone. [S1](sources.md#s1)

| Date | Evidence available | Interpretation |
|---|---|---|
| May 31, 2024 | Seed and initial distribution are recorded in block 845859; Elliptic publishes contemporaneous loss and dispersal reporting. | Establish the reported incident and the transaction trail; do not assume a known actor at intake. [S2](sources.md#s2), [S5](sources.md#s5), [S6](sources.md#s6) |
| June 4, 2024 | Beosin publishes the recipient and ten destination addresses, alongside possible explanations of the compromise. | Use the addresses as research leads; keep its root-cause hypotheses provisional. [S3](sources.md#s3) |
| December 19, 2024 | Merkle Science publishes later laundering analysis with a conflicting May 5 incident date. | Record the discrepancy; use the May 31 transaction block date for this trace. Do not import unverified downstream paths. [S4](sources.md#s4) |
| December 23, 2024 | Joint government attribution is published. | Update retrospective actor attribution while preserving the original knowledge boundary. [S1](sources.md#s1) |

Historical dollar estimates are not present-day valuations and are not used in the Bitcoin accounting.

## What was verified

| Check | Result |
|---|---|
| Transactions cross-checked | 11: the seed and ten distribution transactions |
| Explorer providers | mempool.space and Blockstream |
| Initial destination outputs | 10, matching the Beosin address set |
| Exact flow accounting | 4,502.90000000 BTC = 4,502.89245200 BTC allocated + 0.00754800 BTC distribution fees |
| Data preserved | 32 API responses with URLs, UTC retrieval times, and SHA-256 hashes |
| Verification | Offline script checks captured-data integrity, explorer agreement, outpoint continuity, and integer-satoshi conservation |

The seed additionally spends 4,503 BTC in inputs and pays 0.1 BTC in its own fee. Counting gross input value as the recipient's stolen output would overstate this trace's starting amount. See [transaction evidence](wallets-and-transactions.md).

## Investigative judgment

The repeated transfers are a peeling pattern: each transaction spends the previous remainder, sends a fixed amount to a new destination, and returns the residual to the initial recipient until the last transfer. This pattern is observable; an actor identity or cash-out service is not encoded in it.

The reconstruction stops at the first ten destination outputs. Later mixer exposure, cross-chain transfers, exchange deposits, account ownership, current balances, and recovered value would require additional evidence. “Terminal output” means the end of this bounded trace, not an unspent output today.

The [triage and handoff](triage-and-handoff.md) translates the evidence into proposed priorities, provider-record needs, AI-output review checks, and an explicit handoff. Its first-hour schedule is an exercise target, not a claim about work performed during the incident.

## Review the work

| File | Purpose |
|---|---|
| [wallets-and-transactions.md](wallets-and-transactions.md) | Exact seed, destination outputs, transaction identifiers, fee reconciliation, and timestamp limits |
| [triage-and-handoff.md](triage-and-handoff.md) | Proposed disposition, escalation criteria, quality checks, and next-investigator handoff |
| [sources.md](sources.md) | Source register, attribution levels, and conflicting-source treatment |
| [evidence/snapshot.json](evidence/snapshot.json) | Captured explorer responses and provenance |
| [verify_trace.py](verify_trace.py) | Offline validation using the Python standard library |

From the repository root, run:

```bash
python3 dmm-bitcoin-2024/verify_trace.py
```

The script reads the saved snapshot and prints `PASS` plus counts and exact satoshi totals when the checks succeed. It performs no network calls or account actions. Explorer agreement and file hashes do not replace Bitcoin-node validation or prove real-world ownership.

[Back to portfolio](../README.md)
