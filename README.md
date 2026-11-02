# Cryptocurrency Investigations

**McLean Lipschutz | Cryptocurrency Investigator**

I investigate cryptocurrency theft, fraud, and the movement of illicit funds. My work combines blockchain tracing, transaction analysis, public-source research, and investigative judgment to establish what happened, account for the assets involved, and identify leads for further investigation.

This repository documents my independent research into major exchange thefts and cryptocurrency scams. Each case presents the investigative questions, supporting evidence, analytical findings, and follow-up priorities. The documentation makes the reasoning behind each conclusion available for review.

## Investigative Research

### [Binance October 2026 — Ethereum Fund-Flow Investigation](binance-2026-developing/README.md)

My Binance research examines selected Ethereum fund movements, EIP-7702 authorization metadata, token identity, and asset-freeze reporting. The published trace covers **six movements across four transactions**, cross-checked against Etherscan and Blockscout. It includes an Excel tracing workbook, a visual fund-flow diagram, wallet and transaction registers, preserved evidence, and an offline verification script.

The findings distinguish internal ETH transfers from transaction-envelope values, token senders from transaction targets, and initial receipts from onward movement. Freeze verification and additional asset branches remain documented follow-up priorities.

### [USDT Approval Phishing 2026 — Ethereum Transaction Investigation](usdt-approval-phishing-2026/README.md)

My analysis of the July 8, 2026 approval-phishing incident examines the spender allowance, contract execution, completed transfers, and exact initial loss. The evidence accounts for **999,999.368915 USDT across two transactions and three Transfer events**, with four transaction cross-checks between Etherscan and Blockscout.

The findings distinguish a failed internal call from a successful outer transaction and exclude a look-alike token from the loss calculation. The case includes captured evidence, reproducible verification, source discrepancies, and investigative follow-up priorities.

### [DMM Bitcoin 2024 — Bitcoin Distribution Investigation](dmm-bitcoin-2024/README.md)

My DMM research follows the initial Bitcoin distribution through **11 transactions**, checked against mempool.space and Blockstream. The trace reconciles the **4,502.9 BTC** starting output to ten destination outputs and the exact distribution fees.

The case documents outpoint continuity, integer-satoshi accounting, source conflicts, and the distinction between historical receipts and current balances. A preserved evidence snapshot and offline verifier support review of the findings and continued tracing from each destination.

### [Bybit / Lazarus Group 2025 — Cross-Chain Investigation](bybit-lazarus-2025/README.md)

My Bybit research examines the reported theft and laundering sequence, including Ethereum wallet fan-out, token conversion, intermediary wallets, THORChain exposure, movement into Bitcoin, and potential service endpoints. The case organizes published addresses and transaction identifiers into an investigative framework with explicit evidence requirements for each phase.

Government attribution, published blockchain-intelligence findings, observable transaction activity, and analytical links are recorded separately. Reported downstream routes remain attributed to their sources until transaction-level continuity is established.

## Research Methodology

I organize cryptocurrency investigations around five questions:

1. **What establishes the loss?** Identify the relevant transactions, assets, amounts, and execution outcomes.
2. **Where did the value move?** Follow full addresses and transaction identifiers, accounting for fees, conversions, and commingled funds.
3. **What supports each connection?** Examine transaction records, contract events, service records, and attribution sources.
4. **What can the evidence establish?** Separate verified observations from analytical conclusions and unresolved questions.
5. **What merits follow-up?** Prioritize branches, service exposure, and records that could establish continuity or account control.

Each material trace entry records the network, asset, full source and destination addresses, transaction hash, amount, timestamp, evidence source, and investigative significance. Where an allocation is supported, case-attributable value is distinguished from the total movement. Cross-chain and privacy-service links require their own supporting evidence.

## Evidence Standards

| Classification | Meaning |
|---|---|
| **VERIFIED ON-CHAIN** | Transaction fields, amounts, contract activity, or events corroborated by the documented blockchain records and checks |
| **OFFICIAL ATTRIBUTION** | Attribution published by a government agency, victim organization, or other authoritative source |
| **SUPPORTED ATTRIBUTION** | Published blockchain-intelligence attribution supported by observable activity |
| **ANALYTICAL LINK** | A reasoned connection whose supporting indicators and remaining uncertainty are stated explicitly |

My findings retain their source, observation date, and verification scope. A transaction link establishes movement; identifying the person or service controlling an address requires additional evidence.

## Published Materials

The case folders contain research narratives, source registers, transaction records, and analytical notes. The DMM, USDT, and Binance cases also include preserved evidence and executable verification scripts. The Binance case includes an editable workbook and graph exports.

This public research uses blockchain records, government releases, incident reporting, and published technical analysis. Confidential law-enforcement records, victim identifiers, and non-public account information are excluded. Completed analytical findings and recommended investigative actions are identified separately throughout the case records.

## Investigator

**McLean Lipschutz**

Cryptocurrency investigations, blockchain tracing, financial-crime research, and investigative documentation.
