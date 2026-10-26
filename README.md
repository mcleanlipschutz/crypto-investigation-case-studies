# Cryptocurrency Investigation Case Studies

A public portfolio of cryptocurrency tracing, blockchain investigation methodology, cross-chain analysis, incident triage, attribution handling, and investigative documentation.

## Purpose

My law-enforcement cryptocurrency investigations can involve victim information, non-public wallet intelligence, preservation requests, subpoenas, account records, investigative leads, and other information that should not be published.

Because of that, the case studies in this repository use public blockchain data, government reporting, public incident reports, and published blockchain-intelligence research. The goal is to demonstrate how I approach a crypto investigation without disclosing protected or non-public case information.

I am not claiming credit for the original investigations documented here. These are independent reconstructions used to demonstrate tracing methodology, evidence handling, wallet organization, asset attribution, cross-chain analysis, and investigative decision-making.

## Featured Case Studies

### [Bybit / Lazarus Group 2025 — Cross-Chain Crypto Tracing Case Study](bybit-lazarus-2025/README.md)

The February 2025 Bybit theft is a useful tracing case because the laundering activity moved well beyond a simple wallet-to-wallet path. Public reporting documents:

- approximately $1.46 billion in stolen cryptoassets
- rapid Ethereum wallet fan-out
- conversion of ERC-20 assets
- decentralized exchange activity
- chain peeling and repeated use of intermediary wallets
- cross-chain movement from Ethereum into Bitcoin
- extensive THORChain activity
- mixer, CoinJoin, and high-risk service exposure
- later movement into additional chains and stablecoins
- potential VASP and OTC investigative leads
- official FBI attribution to North Korean TraderTraitor activity

The case study separates direct on-chain evidence from government attribution, blockchain-intelligence attribution, and analytical links. A connection is not treated as proven simply because it appears in a public cluster or tracing platform.

### [DMM Bitcoin 2024 — Bitcoin Trace and Triage Case Study](dmm-bitcoin-2024/README.md)

A public-source reconstruction of the initial distribution following the DMM Bitcoin theft, with 11 transactions cross-checked against two public Bitcoin explorers. It includes exact output and fee accounting, ten destination outputs, a saved evidence snapshot, and an offline verification script.

The accompanying triage workflow shows how to prioritize leads, review AI-generated assertions, handle conflicting sources, and prepare a clear investigative handoff. It separates verified transaction fields from public attribution and proposed actions. No participation in the original investigation or asset recovery is claimed.

### [USDT Approval Phishing 2026 — Ethereum Scam Trace and Triage](usdt-approval-phishing-2026/README.md)

A reconstruction of the July 8, 2026 Ethereum approval-phishing incident covered in the news on July 9. It verifies an initial loss of 999,999.368915 USDT across two transactions and three Transfer events, with exact token-unit accounting and four transaction cross-checks between Etherscan and Blockscout.

The study examines an unlimited token approval, a successful multicall containing a failed internal transfer, and a look-alike USDT token excluded from the loss. It includes captured evidence, an offline verification script, source discrepancies, and a proposed investigative handoff. It does not claim participation in the original case or recovery of funds.

## Investigative Approach

For each material hop, I want enough information that another investigator can understand why it belongs in the trace:

- full sending wallet
- full receiving wallet
- transaction hash
- blockchain
- asset
- transaction amount
- maximum potentially attributable case funds
- date and time
- service or entity attribution
- evidence level
- attribution source
- investigator note explaining why the hop matters

The graph is only one part of the investigation. The underlying transaction evidence, attribution source, asset accounting, and investigative lead are more important than the number of nodes on the screen.

## Evidence Levels

I use four basic evidence levels throughout these public reconstructions:

| Level | Meaning |
|---|---|
| **VERIFIED ON-CHAIN** | Independently observable transaction, address, amount, contract interaction, or blockchain event |
| **OFFICIAL ATTRIBUTION** | Publicly identified by a government agency, victim organization, or similarly authoritative source |
| **SUPPORTED ATTRIBUTION** | Service, wallet cluster, or laundering path identified by established blockchain-intelligence research and supported by observable activity |
| **ANALYTICAL LINK** | Reasoned connection supported by timing, amount, service behavior, or other indicators but not represented as a direct proven transaction unless the evidence establishes it |

## Repository Structure

| Case folder | Contents |
|---|---|
| [bybit-lazarus-2025](bybit-lazarus-2025/README.md) | Overview, wallets and transactions, methodology, sources |
| [dmm-bitcoin-2024](dmm-bitcoin-2024/README.md) | Overview, verified initial Bitcoin distribution, triage and handoff, sources, evidence snapshot, validation script |
| [usdt-approval-phishing-2026](usdt-approval-phishing-2026/README.md) | Overview, approval and transfer evidence, token exclusions, triage and handoff, sources, evidence snapshot, validation script |

Additional public or synthetic case studies can be added as separate folders while keeping the same evidence standard.

## Scope

This repository is for investigative training and professional portfolio use. It does not contain confidential law-enforcement case files, victim identifiers, subpoena returns, private exchange records, or proprietary blockchain-intelligence data.

Public attribution is preserved with its source. Analytical conclusions are labeled as analysis rather than presented as established fact.

## Author

McLean Lipschutz
