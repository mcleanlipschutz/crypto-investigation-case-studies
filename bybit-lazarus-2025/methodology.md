# Tracing Methodology

## Purpose

The point of this reconstruction is not to reproduce a vendor graph. I want to be able to explain why each material wallet, transaction, service, and cross-chain connection is in the trace.

If I cannot explain why two nodes are connected, the line should not be presented as a confirmed path.

---

## 1. Start With the Loss Event

Before expanding the graph, establish the event that created the loss.

For the Bybit case that means documenting:

- victim wallet
- malicious contract activity
- drain transaction hashes
- assets taken
- amounts taken
- time of theft
- first attacker-controlled activity

This gives the trace a fixed starting point.

---

## 2. Build Forward From Known Case Funds

I trace forward from confirmed stolen assets instead of starting with a large attributed wallet cluster and assuming everything in the cluster belongs to the case.

For every hop I want the full address and transaction hash.

Shortened addresses can be used on a visual graph, but the underlying case notes should preserve the full identifier.

---

## 3. Track the Asset, Not Just the Wallet

A wallet can contain unrelated funds.

For each material hop I record:

- total transaction amount
- asset being transferred
- amount of known or potentially attributable stolen funds
- remaining attributable balance after the transfer

When funds commingle, I do not treat the entire wallet balance as stolen simply because stolen funds entered the wallet.

For this public reconstruction, the conservative default is to record the **maximum potential stolen amount** that could be associated with the outbound transaction unless public evidence supports a more specific allocation.

If a formal FIFO, LIFO, pro-rata, or other allocation method is used, it should be stated in the case notes and applied consistently.

---

## 4. Treat Swaps as Asset-Conversion Events

A DEX swap changes the asset but does not automatically break the trace.

The case record should identify:

- input asset
- input amount
- transaction hash
- DEX/router or liquidity protocol
- output asset
- output amount
- destination wallet

The trace should make it clear that ETH became another asset rather than making it appear that the same asset simply moved to another address.

---

## 5. Treat Cross-Chain Movement as Two Legs

A bridge or cross-chain swap should not be drawn as if Ethereum sent a native transaction directly to Bitcoin.

I document:

### Source-chain leg

`wallet -> cross-chain service`

and then:

### Destination-chain leg

`cross-chain service -> destination wallet`

The bridge/service becomes an investigative node between the two blockchains.

Evidence used to associate the two legs can include:

- protocol transaction records
- service attribution
- matching or near-matching value
- timing
- swap identifiers
- public intelligence
- proprietary tracing results when lawfully available

If the exact cross-chain continuity cannot be independently established from public evidence, the connection should be labeled as a supported or analytical link rather than a direct on-chain transaction.

---

## 6. Separate Attribution From Transaction Evidence

An address can be factually involved in a transaction without the owner being known.

Likewise, an intelligence provider may attribute a wallet to a service or threat actor without that attribution being visible directly on-chain.

I separate these concepts:

- **transaction fact** — what happened on the blockchain
- **entity attribution** — who or what is believed to control the address
- **case attribution** — why the address is connected to this specific theft

The FBI TraderTraitor list is treated as official attribution. TRM, Elliptic, Arkham, Chainalysis and other published intelligence can support service or laundering-path attribution, but I still preserve the source of the conclusion.

---

## 7. Handle Mixers and CoinJoin Carefully

Mixer exposure is not the same as a normal wallet-to-wallet transfer path.

For services such as Tornado Cash, Cryptomixer, or Wasabi Wallet, I document:

- confirmed deposit into the service or privacy tool
- amount and time
- known withdrawal or output intelligence if available
- evidence supporting any claimed post-service connection
- confidence level

I do not draw a deterministic line through a privacy service unless the evidence supports that conclusion.

If the trace becomes probabilistic, the graph should say so.

---

## 8. Identify Investigative Choke Points

The best investigative lead is not always the wallet holding the most funds.

I flag services that may hold records capable of identifying the actor or establishing continuity, including:

- centralized exchanges
- hosted swap services
- custodial wallets
- OTC services
- payment processors
- bridge operators where records exist

Potential records can include:

- KYC
- account identifiers
- deposit addresses
- withdrawal addresses
- IP/login history
- device information
- transaction records
- linked accounts
- fiat funding or withdrawal information

The availability of those records depends on the service, jurisdiction, and legal process.

---

## 9. Do Not Let the Graph Become the Investigation

A graph with hundreds of nodes can be technically correct and still be difficult to understand.

I organize large traces into separate views:

1. theft
2. first fan-out
3. Ethereum layering
4. cross-chain transition
5. Bitcoin laundering
6. mixer/service exposure
7. re-emergence and off-ramp

The master view should show the laundering strategy. Branch views should hold the transaction-level detail.

---

## 10. Preserve the Reason for Every Important Conclusion

For every major node or branch I want a note answering:

- Why is this wallet in the case?
- What transaction brought the case funds here?
- How much case value could be present?
- What happened next?
- Is the next hop verified, attributed, or analytical?
- What source supports the attribution?
- Is there a preservation, subpoena, freeze, or intelligence lead associated with the service?

That makes the trace reviewable by someone who did not build it.

---

## Evidence Labels Used in This Case Study

| Label | Meaning |
|---|---|
| VERIFIED ON-CHAIN | Independently observable blockchain transaction or contract activity |
| OFFICIAL ATTRIBUTION | Publicly identified by the FBI, Bybit, or another authoritative official source |
| SUPPORTED ATTRIBUTION | Published blockchain-intelligence attribution supported by observable activity |
| ANALYTICAL LINK | Reasoned connection that should not be represented as a direct proven transaction |

---

## Final Standard

The final trace should allow another investigator to answer three questions without relying on me to explain the graph:

1. Where did the stolen assets go?
2. What evidence supports each major part of that conclusion?
3. Where are the best investigative or recovery opportunities?
