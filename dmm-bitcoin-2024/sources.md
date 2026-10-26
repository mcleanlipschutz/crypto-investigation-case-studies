# Sources and evidence limits

[Case overview](README.md) · [Transaction evidence](wallets-and-transactions.md) · [Triage workflow](triage-and-handoff.md)

Sources were reviewed on October 26, 2026. This is a bounded historical reconstruction, not a comprehensive update on all subsequent DMM-related developments. Narrative sources are linked rather than reproduced. Explorer response retrieval times are preserved in the [evidence snapshot](evidence/snapshot.json).

## S1

**FBI / DC3 / Japan NPA — December 23, 2024**  
[Joint public attribution statement](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom)

Supports the reported 4,502.9 BTC loss, approximately $308 million at the time, and official attribution to North Korean TraderTraitor activity. It describes recruitment-themed compromise at Ginco, session-cookie misuse, and likely manipulation of a DMM transaction request. The word “likely” matters: the statement does not publish a complete forensic proof or transaction-by-transaction graph. It is later attribution, not contemporaneous May intelligence.

## S2

**Elliptic Research — May 31, 2024**  
[DMM Bitcoin loses $308 million in “unauthorized leak”](https://www.elliptic.co/insights/dmm-bitcoin-loses-308-million-in-unauthorized-leak/)

Contemporaneous researcher account of DMM's announced loss and early dispersal. The published graph is described as current at 15:00 UTC. It provides context, not a substitute for checking individual transaction outputs. This study does not claim access to Elliptic's proprietary dataset.

## S3

**Beosin — June 4, 2024**  
[Analysis of the 4,502.9 BTC outflow](https://beosin.com/resources/more-than-300-million-in-losses-analysis-of-45029-btc-abnormal-outflow-on-dmm-bitcoin-exchange)

Publishes the initial recipient and ten distribution addresses used for comparison with the explorer trace. Its early root-cause explanations are explicitly possibilities. They are not promoted to established facts in this study.

## S4

**Merkle Science — December 19, 2024**  
[Hack Track: DMM Flow of Funds Analysis](https://www.merklescience.com/blog/hack-track-dmm-flow-of-funds-analysis)

Discusses peeling and potential obfuscation. A bullet dates the theft to May 5, conflicting with contemporaneous reporting and the seed transaction's May 31 block date. This study rejects that date for its chronology. Its suggested mixer examples and downstream activity are not treated as independently verified hops. The source is retained to make the discrepancy reviewable, not to supply a confirmed recovery path.

## S5

**mempool.space — public Bitcoin explorer and Esplora-compatible API**  
[Seed transaction](https://mempool.space/tx/975ec405ac9dc9fa5ab8009d94d6a1fe31dff8a8127ea90d023104e52754e4d7)

Transaction and outspend endpoints supplied the first-pass trace. Each retrieved response is preserved with URL, UTC retrieval time, and SHA-256 in the snapshot. Transaction values are stored as integer satoshis. Outspend responses identify follow-up candidates; full transaction inputs confirm the links.

## S6

**Blockstream Explorer — second public Bitcoin explorer**  
[Seed transaction](https://blockstream.info/tx/975ec405ac9dc9fa5ab8009d94d6a1fe31dff8a8127ea90d023104e52754e4d7)

Used to cross-check every captured transaction's inputs, outputs, fees, and block metadata against S5. Agreement between explorer providers supports reproducibility but is not independent Bitcoin-node validation, a transaction-signature audit, or proof of beneficial ownership.

## S7

**Whale Alert — May 31, 2024 transaction record**  
[Public transaction alert](https://whale-alert.io/transaction/bitcoin/975ec405ac9dc9fa5ab8009d94d6a1fe31dff8a8127ea90d023104e52754e4d7)

Provided the seed transaction candidate. Its displayed BTC values are rounded and its counterparties are labeled unknown. Exact values come from S5/S6; case linkage comes from corroboration with S3. Dollar estimates in this alert are not substituted for S1's historical loss estimate.

## Evidence classification

| Classification | Meaning in this case |
|---|---|
| VERIFIED ON-CHAIN | Transaction fields checked against two public explorers, with output continuity and arithmetic validated locally. No ownership claim is implied. |
| OFFICIAL ATTRIBUTION | The government's published incident-level conclusion, attributed to S1 and dated. |
| SUPPORTED ATTRIBUTION | Researcher identification of the DMM-related address set in S3, corroborated by the bounded transaction trace. |
| ANALYTICAL LINK | A proposed interpretation or next step that lacks sufficient evidence to become a confirmed transaction or ownership relationship. |

Do not use evidence strength as a substitute for temporal relevance. A historic address label does not establish a current account holder, present asset balance, or immediate freeze opportunity.
