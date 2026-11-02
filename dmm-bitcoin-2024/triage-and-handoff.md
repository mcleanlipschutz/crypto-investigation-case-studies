# Investigative assessment and follow-up

[Case overview](README.md) · [Transaction evidence](wallets-and-transactions.md) · [Sources](sources.md)

My assessment connects the verified initial Bitcoin distribution to the next investigative questions: where the outputs moved, whether a service can be identified, and what additional evidence would establish control of an endpoint. The findings below document completed transaction analysis; follow-up recommendations identify the remaining work.

## Disposition

**Continue tracing the ten destination outputs and evaluate downstream service exposure.** My initial analysis establishes the distribution and reconciles the transaction amounts and fees. A request to preserve records or restrict assets additionally requires a verified recipient service, relevant transaction identifiers, an authorized requesting party, and the applicable process. The initial distribution alone does not identify an exchange account or establish present recoverability.

Two time frames must stay separate:

- **Historical intake:** use information available at the relevant time in May 2024. The later FBI attribution cannot be inserted into an initial complaint as if it were already known.
- **Retrospective review:** apply the December 2024 attribution with its publication date, then reassess hypotheses and source conflicts. A historic lead still requires a fresh balance and service check before any present-day action.

## Evidence review and follow-up sequence

| Stage | Research task | Decision or output |
|---|---|---|
| Establish the incident | Compare contemporaneous loss reporting, the seed transaction, and later attribution. Record publication dates and resolve conflicts. | A chronology that separates transaction evidence from subsequent intelligence. |
| Validate the initial movement | Check the seed transaction, input/output amounts, fees, and confirmed status. Preserve the retrieved data and retrieval time. | The reported loss distinguished from the transaction's gross input value. |
| Extend individual branches | Follow specific spent outputs and check available service attribution. Document the basis for each new connection. | Prioritized leads with full identifiers, evidence, uncertainty, and next action. |
| Prepare further investigation | Record the trace boundary, outstanding questions, and evidence needed for each proposed service or records inquiry. | A reviewer can continue from a full transaction ID and output index. |

Urgency comes from the asset exposure and evidence, not the number of times a complaint appears. Separate exchange-level loss from individual customer claims to avoid counting the same stolen assets twice.

## Lead priorities

| Lead | What this study establishes | Proposed next step |
|---|---|---|
| Initial Bitcoin distribution | Exact transactions and output allocations in the bounded trace | Follow terminal outpoints and document each subsequent spend. Current balances are outside this snapshot's conclusions. |
| Potential custodial endpoint | None independently identified in this bounded trace | If a service match emerges, validate the attribution and deposit reference before preparing targeted outreach. A label alone is insufficient. |
| Compromised business workflow | Later government reporting describes a likely transaction-request manipulation path [S1](sources.md#s1) | In an authorized investigation, seek relevant approval records, communications, access logs, and transaction instructions from the affected organizations. |
| Possible mixer or cross-chain activity | Later analyst reporting exists; this study does not verify those paths [S4](sources.md#s4) | Require the actual deposit, withdrawal, service evidence, and explanation of linkage before extending the confirmed trace. |

For a verified custodial lead, a proposed records package would identify the incident, authority and contact, network, asset, full deposit transaction and output, relevant time window, attributable amount, and attribution basis. Potential records include account identifiers, KYC, deposit/withdrawal history, and relevant login/device records. Preservation, account restriction, and disclosure are separate outcomes; none should be described as completed without a response establishing it.

## Analytical quality checks

These checks keep the conclusions aligned with the transaction records and the chronology of the reporting.

| Candidate assertion | Review decision |
|---|---|
| “The loss transaction sent 4,503 BTC to the recipient.” | Correct it: 4,503 BTC is the input total; the recipient output is 4,502.9 BTC and the miner fee is 0.1 BTC. |
| “Every transaction with this block time happened simultaneously.” | Reject it: the timestamp belongs to the block. Spent-output dependencies establish ordering, not exact elapsed time. |
| “The FBI had attributed the case at intake in May.” | Reject the timing: the cited public attribution was released December 23, 2024. |
| “The ten destination addresses are ten exchange accounts.” | Reject it: addresses and accounts are different objects, and this dataset supplies no custodial-account mapping. |
| “A similar laundering pattern proves the same actor.” | Retain only as an analytical lead unless supported by additional evidence; keep official attribution separately sourced. |

## Handoff record

**Status:** Initial Bitcoin distribution analyzed and reconciled against preserved public explorer responses.

**Verified boundary:** Seed transaction through the initial terminal output set listed in [wallets-and-transactions.md](wallets-and-transactions.md). “Terminal” identifies where the published trace stops; current spend status requires a fresh check.

**Attribution:** Public researcher linkage to the DMM incident; later government attribution recorded separately. Address ownership is not proved by a transaction record.

**Next research priorities:** Continue from each listed outpoint and evaluate any service exposure. A verified service connection can support a targeted records inquiry through the appropriate authorized process.

**Open questions:** Which downstream transfers are directly connected? Which services, if any, control an identifiable endpoint? What can provider records establish about account control? What value is still available now?

**Review criteria:** Complete transaction identifiers, reproducible output continuity, reconciled amounts and fees, dated attribution, and clearly stated evidence requirements for each unresolved lead.
