# Triage and investigative handoff

This is a proposed workflow for a comparable intake, informed by the July 2026 reconstruction. It is not a record of actions taken for the original victim. No outreach, freeze request, wallet action, or recovery was performed as part of this portfolio exercise.

## Disposition and priorities

**Escalate for specialist tracing and incident coordination.** The evidence supports a large spender-executed USDT drain after approval. Prioritize prevention of additional loss, preservation of the phishing evidence, and identification of any actionable downstream service.

| Priority | Proposed action | Evidence needed / completion condition |
|---|---|---|
| Confirm the incident | Obtain the complainant's account, wallet address, transaction links, and chronology; distinguish observed transfers from their explanation of events. | A1/D1/D2 matched to the correct network, token, owner, and complaint. |
| Assess continuing exposure | Query the current USDT allowance for this owner/spender and assess other suspicious approvals. Coordinate a trusted revocation process with the wallet owner if exposure remains. | Current state recorded with block number; a successful revocation verified where appropriate. Revocation does not reverse earlier transfers. |
| Preserve off-chain evidence | Preserve the URL, message or advertisement, browser history, screenshots, approval prompt, and relevant timestamps through the applicable evidence process. | Original files and metadata retained; hashes and collection notes recorded. Never request the user's seed phrase or private key. |
| Extend the trace | Follow canonical USDT receipts at A and B, validating each outgoing transaction, contract, amount, and destination. | A bounded path with commingling limits, endpoint evidence, and unresolved branches. |
| Assess service action | If a custodial endpoint or issuer intervention becomes supportable, identify the correct recipient and prepare an evidence-backed escalation through the appropriate channel. | Verified service attribution, transaction identifiers, relevant amounts, current status, and applicable authority; no promised freeze or recovery. |

At live intake, a continuing allowance would be an urgent exposure. In this retrospective study, its current state is unknown. Historical labels and receipts are not a substitute for a current query.

## Handoff brief

| Field | Handoff content |
|---|---|
| Classification | Publicly reported approval phishing; observed unlimited USDT approval followed by spender-executed transfers. |
| Incident window | July 8, 2026, 17:51:47–17:52:35 UTC, blocks 25489459–25489463. |
| Measured initial loss | 999,999.368915 USDT across D1/D2, three canonical Transfer logs. |
| Starting follow-up amounts | A: 359,999.873783 USDT; B: 639,999.495132 USDT. These are historical receipts. |
| Core evidence | [Transaction register](wallets-and-transactions.md), [snapshot](evidence/snapshot.json), and [offline verifier](verify_trace.py). |
| Attribution | Scam Sniffer's incident report and explorer labels; no verified actor or custodial-service identity. |
| Main gaps | Victim interview, phishing infrastructure, current allowance, downstream movements, account ownership, and recoverability. |
| Next investigator's task | Validate present exposure, preserve the lure, and trace onward canonical USDT movements before asserting an endpoint. |

## Review of AI-assisted assertions

These are concrete failure modes checked against the evidence before publication:

| Possible assertion | Review decision |
|---|---|
| “The loss happened July 9.” | Use July 8 for the transaction date; July 9 is the news publication date. |
| “Three transactions stole the funds.” | Count unique transaction hashes separately from Transfer events: two transactions, three events. |
| “The first attempt failed completely.” | D1's outer transaction succeeded and 200,000 USDT moved; only one internal call failed. |
| “Every token labeled USDT is part of the loss.” | Filter by the issuer-listed contract; exclude X1. |
| “The approval exposed every asset or the seed phrase.” | State only the demonstrated token allowance. |
| “These addresses belong to named criminals or an exchange.” | Require sourced attribution beyond timing, visual similarity, or explorer labels. |
| “The funds can still be frozen or recovered.” | Require current balances, an actionable endpoint, and the relevant provider's response. |

The successful checks support a reproducible initial trace. They do not fill missing evidence with plausible narrative.

[Case overview](README.md) · [Sources and limitations](sources.md)
