# Bybit / Lazarus Group 2025
## Cross-Chain Crypto Tracing Case Study

## Why I Used a Public Case

Most of the cryptocurrency investigations I work on involve law-enforcement records, victim information, investigative leads, preservation requests, subpoenas, and other material that I cannot post publicly.

This case study is different. Everything used here comes from public blockchain data, government reporting, public incident reports, and published blockchain-intelligence research. The purpose is to show how I approach a large crypto investigation without disclosing information from an actual case.

This is not an attempt to claim credit for the original Bybit investigation. It is a reconstruction of a public case used to demonstrate tracing methodology, evidence handling, wallet organization, cross-chain analysis, and investigative decision-making.

---

## Incident Summary

On February 21, 2025, Bybit suffered a compromise of one of its Ethereum cold wallets. Approximately $1.46 billion in cryptoassets were removed, including approximately:

- 401,347 ETH
- 90,375 stETH
- 15,000 cmETH
- 8,000 mETH

Bybit reported that the stolen assets were initially split across 39 addresses. On February 26, 2025, the FBI publicly attributed the theft to North Korea and identified the activity as **TraderTraitor**. The FBI reported that stolen assets had been converted into Bitcoin and other virtual assets and dispersed across thousands of addresses on multiple blockchains.

The laundering that followed is what makes this case useful for tracing practice. Public reporting documents:

- rapid wallet fan-out
- token swaps through decentralized exchanges
- chain-peeling and intermediary wallets
- cross-chain movement from Ethereum into Bitcoin
- heavy use of THORChain
- exposure to eXch
- mixing and privacy-enhancing services
- later movement into additional chains, including TRON
- eventual conversion toward stablecoins and suspected OTC cash-out activity

This is not a one-chain wallet trace. It is a large laundering network where the investigator has to separate direct blockchain evidence from service attribution and analytical conclusions.

---

## Primary Investigative Questions

I approached the case with the same questions I would use when starting a crypto fraud or theft investigation:

1. What transaction establishes the original loss?
2. What wallet or contract was compromised?
3. Which addresses first received or controlled the stolen assets?
4. How quickly were the assets dispersed?
5. Where did the assets change form through swaps or wrapping/unwrapping?
6. Where did the trace cross from one blockchain to another?
7. Which services created an investigative or evidentiary break in the public chain?
8. Which wallets are directly verified and which are only attributed through public intelligence?
9. Which services could potentially hold KYC, account, IP, or transaction records?
10. Where can the transparent blockchain trace resume after a swap, bridge, mixer, or exchange interaction?

---

## Starting Point

### Bybit Cold Wallet 1

`0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4`

This is the compromised Ethereum multisig cold wallet identified in public incident reporting.

### Initial attack operator address

`0x0fa09C3A328792253f8dee7116848723b72a6d2e`

Public technical reporting identifies this address as the address that executed the initial malicious transaction.

### Malicious implementation contract

`0xbDd077f651EBe7f7b3cE16fe5F2b025BE2969516`

### Delegate-call attack contract

`0x96221423681A6d52E184D440a8eFCEbB105C7242`

The exploit and loss transactions are listed in [wallets-and-transactions.md](wallets-and-transactions.md).

---

## Trace Structure

I separated the case into phases instead of trying to place the entire laundering network on one graph.

### Phase 0 — Compromise and Theft

Establish the victim wallet, malicious contract change, loss transactions, assets, amounts, and first attacker-controlled activity.

### Phase 1 — Initial Fan-Out

Follow the stolen ETH and converted ERC-20 assets into the first generation of intermediary wallets. Bybit reported that the assets were split across 39 addresses shortly after the theft.

At this stage the main concern is maintaining transaction-level continuity. A wallet appearing in the same cluster is not enough by itself. I want the transaction hash, sending address, receiving address, asset, amount, and timestamp.

### Phase 2 — Layering and Asset Conversion

The stolen assets were moved through large numbers of intermediary addresses and decentralized services. Public blockchain-intelligence reporting describes chain-peeling and repeated movement through fresh wallets.

The tracing problem changes here. The investigator is no longer following one balance. The funds are being fragmented, recombined, swapped, and moved through services designed to make the path difficult to follow.

### Phase 3 — Cross-Chain Movement

TRM Labs reported that the vast majority of the stolen Ethereum was bridged into Bitcoin, mostly through services using **THORChain**. Arkham later reported that approximately 72% of the proceeds were bridged through THORChain.

This is an important investigative point. An Ethereum address and a Bitcoin address do not have a normal on-chain transaction edge between them. The continuity has to be documented through the cross-chain service, asset amounts, timing, service intelligence, and other available evidence.

I treat the bridge event as its own investigative node instead of drawing a line that makes the transaction appear native to both chains.

### Phase 4 — Mixers, CoinJoin and High-Risk Services

Published reporting identifies exposure to services including:

- eXch
- Tornado Cash
- Cryptomixer
- Wasabi Wallet

Elliptic reported that more than $200 million in Bybit proceeds moved through eXch after passing through hundreds of intermediary wallets.

A mixer or privacy-enhancing service does not mean the investigation ends. It means the confidence and evidence supporting the next hop must be clearly stated.

### Phase 5 — Re-Emergence and Off-Ramp

Later public reporting identified Bybit-linked funds moving across additional blockchains and into TRON, where stolen value was converted into USDT and linked to suspected OTC cash-out activity.

At that point the investigation becomes more than blockchain tracing. Potential next steps can include preservation, account records, KYC, IP/login history, deposit and withdrawal records, counterparties, and other records held by a VASP or service provider.

---

## Evidence Standard

One of the biggest problems with a large tracing graph is that every line can start to look equally reliable. It is not.

I use four evidence levels in this case study:

### VERIFIED ON-CHAIN
A transaction, address, asset, amount, or contract interaction that can be independently confirmed on the blockchain.

### OFFICIAL ATTRIBUTION
An address or activity publicly identified by a government agency, victim exchange, or similarly authoritative source.

### SUPPORTED ATTRIBUTION
A service, wallet cluster, or laundering path identified by established blockchain-intelligence research and supported by observable blockchain activity.

### ANALYTICAL LINK
A connection used during reconstruction that is supported by timing, amounts, service behavior, or other indicators but should not be presented as a proven transaction unless the underlying evidence establishes it.

If a link cannot be supported, it does not belong in the final trace as a confirmed hop.

---

## What I Would Capture for Every Hop

For each material transaction I want:

| Field | Purpose |
|---|---|
| Sending wallet | Establish source |
| Receiving wallet | Establish destination |
| Transaction hash | Independent verification |
| Blockchain | Identify network |
| Asset | Track asset changes |
| Total transaction amount | Establish actual movement |
| Attributable stolen amount | Separate case funds from unrelated funds |
| Date/time | Build chronology and bridge correlation |
| Service/entity | Identify VASP, DEX, bridge, mixer, or protocol |
| Evidence level | Distinguish fact from attribution or analysis |
| Source | Preserve how the conclusion was reached |
| Investigator note | Explain why the hop matters |

---

## Investigative Value of the Case

This case is useful because it forces the trace through several different problems at once:

- Ethereum account-based tracing
- ERC-20 asset conversion
- wallet fan-out
- large-scale layering
- DEX interaction
- chain peeling
- cross-chain tracing
- ETH-to-BTC conversion
- THORChain activity
- mixer/CoinJoin exposure
- service attribution
- stablecoin conversion
- VASP and OTC investigative leads
- government attribution
- confidence labeling
- evidence preservation

The goal is not to draw the biggest graph possible. The goal is to make the movement understandable and defensible.

---

## How I Would Present the Final Graph

I would not show hundreds or thousands of nodes in one view.

The main graph should show the major stages:

`Bybit Cold Wallet -> Exploit -> Initial Fan-Out -> DEX / Layering -> THORChain -> Bitcoin -> Mixer / Service Exposure -> Re-Emergence -> Off-Ramp`

Separate branch views can then show transaction-level detail for each phase.

This keeps the high-level laundering methodology visible while still allowing a reviewer to drill into the actual wallet and transaction evidence.

---

## Files in This Case Study

- [wallets-and-transactions.md](wallets-and-transactions.md) — public seed addresses, FBI TraderTraitor addresses, and exploit transaction hashes
- [methodology.md](methodology.md) — tracing workflow and analytical rules used for the reconstruction
- [sources.md](sources.md) — government, victim, blockchain-intelligence, and technical sources

---

## Scope and Limitations

This case study uses public information only. I do not have Bybit's internal records, exchange account records, law-enforcement returns, proprietary TRM/Elliptic/Chainalysis/Arkham datasets, or non-public investigative evidence from the original case.

Because of that, this reconstruction should not be represented as the complete official investigative trace.

The case study is intended to demonstrate how I organize and analyze a complex cryptocurrency investigation using information that can be shared publicly.

## Author

McLean Lipschutz
