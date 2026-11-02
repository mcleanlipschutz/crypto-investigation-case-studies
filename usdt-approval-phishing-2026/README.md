# USDT Approval Phishing — July 2026

**McLean Lipschutz · Cryptocurrency Investigator · Research prepared October 26, 2026**

My investigation examines the approval, contract execution, and initial loss in an Ethereum phishing incident reported by Scam Sniffer and covered by Cointelegraph on July 9, 2026. The transactions occurred on **July 8, 2026 UTC**. My analysis focuses on canonical token identification, spender permissions, successful and failed internal calls, exact loss accounting, and source discrepancies. Captured evidence and verification code support review of each finding. [S1](sources.md#s1), [S5](sources.md#s5)

## Executive finding

After the reported victim address approved a spender for the maximum `uint256` allowance, that spender was used to transfer **999,999.368915 USDT** to two addresses. The initial drain consists of **two successful Ethereum transactions containing three completed USDT Transfer events**. It occurred within 48 seconds of the approval, measured using block timestamps. [S2–S3](sources.md#s2)

The first multicall requested 200,000 USDT and 800,000 USDT. The 200,000 transfer completed; the 800,000 internal call failed with an invalid-opcode error. The outer transaction nevertheless succeeded. The second multicall transferred another 799,999.368915 USDT. Counting attempted calldata as completed movement would materially overstate the loss.

**Investigative priority:** extend the trace from the initial recipients and assess continuing allowance exposure. Custodial-service attribution, current balances, actor identity, and recoverability remain open questions.

## Verified chronology

All times below are July 8, 2026 UTC. Full identifiers and source links are in [wallets and transactions](wallets-and-transactions.md).

| Time | Record | Observed result |
|---|---|---|
| 17:51:47 | A1: approval | Victim approves the spender for `2^256 − 1` units of canonical Ethereum USDT; no USDT transfer occurs in A1. |
| 17:51:47 | A2: nearby direct transfer | Victim sends 0.631085 USDT separately. Its purpose is not established here; it is excluded from the spender-executed drain. |
| 17:51:59 | D1: first multicall | 200,000 USDT reaches recipient A. The attempted 800,000 transfer to B fails internally. |
| 17:52:35 | D2: second multicall | 159,999.873783 USDT reaches A; 639,999.495132 reaches B. |
| 17:52:35 | X1: excluded token | Another contract emits a 200,000-unit-denominated look-alike token transfer. It is not canonical USDT and is excluded. |

Transaction position orders A1 before A2 within the same block. Block timestamps establish chain ordering and elapsed block time, not the exact time a person saw a prompt or submitted a transaction.

## Investigative Findings

| Investigative question | Evidence-based answer |
|---|---|
| What asset moved? | Ethereum USDT at the contract listed by Tether, using six decimals. Token names and symbols alone were insufficient. [S6](sources.md#s6) |
| What permission was granted? | An allowance for one spender to move this token from this owner. It does not establish disclosure of a seed phrase or unrestricted control over every asset. [S4](sources.md#s4) |
| How much moved in the initial drain? | 999,999,368,915 integer token units, or 999,999.368915 USDT. No assumed dollar exchange rate is needed. |
| What succeeded? | Three canonical Transfer events across D1 and D2. One attempted internal transfer failed even though D1's outer status was successful. |
| Who is responsible? | The transaction roles are observable. The phishing classification comes from public reporting; address labels do not establish a natural person or organization. |
| What remains unknown? | The phishing page and lure, victim intent, exact cause of the internal failure, operator identity, complete downstream path, current allowance, and recoverable funds. |

## Evidence and scope

The evidence package contains **nine raw Blockscout JSON responses and four factual extracts from Etherscan transaction pages**, each with a source URL, UTC retrieval time, and SHA-256 digest. The script checks agreement on four transactions and their relevant events, decodes approval and multicall inputs, reconciles integer-unit totals, checks the internal failure, and rejects the look-alike token example.

The bounded trace ends at recipients A and B in the initial drain. This is not a claim that they retained the funds, that they are separate people, or that the wallet had no subsequent activity. Later dust, onward transfers, other tokens, and lifetime losses are outside the measured total. Explorer agreement is useful corroboration; it is not independent Ethereum-node execution. An attempted RPC receipt lookup returned null and was not counted as confirmation.

## Review the work

| File | Purpose |
|---|---|
| [wallets-and-transactions.md](wallets-and-transactions.md) | Full addresses, transaction identifiers, log indices, exclusions, and exact accounting |
| [triage-and-handoff.md](triage-and-handoff.md) | Investigative priorities, evidence gaps, analytical quality checks, and follow-up |
| [sources.md](sources.md) | Source register, attribution limits, and reporting discrepancies |
| [evidence/snapshot.json](evidence/snapshot.json) | Captured responses, extracted facts, and provenance |
| [verify_trace.py](verify_trace.py) | Offline checks using Python's standard library |

From the repository root:

```bash
python3 usdt-approval-phishing-2026/verify_trace.py
```

The script performs no network calls or wallet actions. `PASS` confirms the packaged checks, not real-world ownership or recovery.

[Back to portfolio](../README.md)
