# Triage decision and investigative handoff

[Case overview](README.md) · [Transaction evidence](wallets-and-transactions.md) · [Sources](sources.md)

This is a proposed response workflow for a historical public case. No provider requests, freezes, seizures, victim notifications, or official investigative actions were performed for this portfolio. The time targets below are an exercise design, not measured response times.

## Disposition

**Escalate for specialist tracing and incident coordination.** A large reported exchange loss and corroborated initial Bitcoin movement justify urgent review. A request to preserve records or restrict assets would additionally need a verified recipient service, relevant transaction identifiers, an authorized requesting party, and the applicable process. The initial distribution alone does not identify an exchange account or establish present recoverability.

Two time frames must stay separate:

- **Historical intake:** use information available at the relevant time in May 2024. The later FBI attribution cannot be inserted into an initial complaint as if it were already known.
- **Retrospective review:** apply the December 2024 attribution with its publication date, then reassess hypotheses and source conflicts. A historic lead still requires a fresh balance and service check before any present-day action.

## Proposed first-hour workflow

| Target | Work | Decision or output |
|---|---|---|
| 0–10 minutes | Authenticate the reporting party through an independently established channel; establish network, asset, transaction identifier, loss basis, and incident reference. Check for duplicate reports. | One incident record; identity and missing evidence clearly marked. |
| 10–25 minutes | Validate the seed transaction, input/output amounts, fees, and confirmed status. Preserve the retrieved data and retrieval time. | Separate the reported loss from the transaction's gross input value. |
| 25–45 minutes | Follow specific spent outputs, record the initial branches, and check available service attribution. Escalate a verified actionable custodial exposure as soon as found. | Prioritized leads with evidence, owner, uncertainty, and next action. |
| 45–60 minutes | Package the trace boundary and outstanding questions for the next investigator; record the next review time and acknowledge the handoff. | A reviewer can continue from a full transaction ID and output index without reconstructing prior work. |

Urgency comes from the asset exposure and evidence, not the number of times a complaint appears. Separate exchange-level loss from individual customer claims to avoid counting the same stolen assets twice.

## Lead priorities

| Lead | What this study establishes | Proposed next step |
|---|---|---|
| Initial Bitcoin distribution | Exact transactions and output allocations in the bounded trace | Follow terminal outpoints and document each subsequent spend. Current balances are outside this snapshot's conclusions. |
| Potential custodial endpoint | None independently identified in this bounded trace | If a service match emerges, validate the attribution and deposit reference before preparing targeted outreach. A label alone is insufficient. |
| Compromised business workflow | Later government reporting describes a likely transaction-request manipulation path [S1](sources.md#s1) | In an authorized investigation, seek relevant approval records, communications, access logs, and transaction instructions from the affected organizations. |
| Possible mixer or cross-chain activity | Later analyst reporting exists; this study does not verify those paths [S4](sources.md#s4) | Require the actual deposit, withdrawal, service evidence, and explanation of linkage before extending the confirmed trace. |

For a verified custodial lead, a proposed records package would identify the incident, authority and contact, network, asset, full deposit transaction and output, relevant time window, attributable amount, and attribution basis. Potential records include account identifiers, KYC, deposit/withdrawal history, and relevant login/device records. Preservation, account restriction, and disclosure are separate outcomes; none should be described as completed without a response establishing it.

## AI-output review examples

These are illustrative quality-control checks, not results from a deployed model or a completed benchmark.

| Candidate assertion | Review decision |
|---|---|
| “The loss transaction sent 4,503 BTC to the recipient.” | Correct it: 4,503 BTC is the input total; the recipient output is 4,502.9 BTC and the miner fee is 0.1 BTC. |
| “Every transaction with this block time happened simultaneously.” | Reject it: the timestamp belongs to the block. Spent-output dependencies establish ordering, not exact elapsed time. |
| “The FBI had attributed the case at intake in May.” | Reject the timing: the cited public attribution was released December 23, 2024. |
| “The ten destination addresses are ten exchange accounts.” | Reject it: addresses and accounts are different objects, and this dataset supplies no custodial-account mapping. |
| “A similar laundering pattern proves the same actor.” | Retain only as an analytical lead unless supported by additional evidence; keep official attribution separately sourced. |

## Handoff record

**Status:** Initial Bitcoin distribution reconstructed from public explorer responses. Historical case; no live response underway.

**Verified boundary:** Seed transaction through the initial terminal output set listed in [wallets-and-transactions.md](wallets-and-transactions.md). “Terminal” means the stopping point of this reconstruction, not that an output remains unspent.

**Attribution:** Public researcher linkage to the DMM incident; later government attribution recorded separately. Address ownership is not proved by a transaction record.

**Next owner/action:** Specialist tracer to continue from each listed outpoint and evaluate any service exposure. An incident lead should coordinate business-record requests if operating with authorization.

**Open questions:** Which downstream transfers are directly connected? Which services, if any, control an identifiable endpoint? What can provider records establish about account control? What value is still available now?

**Success measures for a real operation:** Time to validated disposition, proportion of leads with complete identifiers, reviewer reversal rate, and time to acknowledged handoff. No throughput, recovery, or business-impact metrics are claimed for this exercise.
