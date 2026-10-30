# Sources and evidence register

The incident is dated October 29, 2026. Individual UTC collection timestamps and source URLs are recorded in [evidence/snapshot.json](evidence/snapshot.json). This starter package is a point-in-time reconstruction, not continuous monitoring.

## Transaction register

| Capture | Transaction | Scope |
|---|---|---|
| sweep | [0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3](https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3) | E01 internal ETH, E02 USDT log 519, E03 RLUSD log 520 |
| binance16 | [0x51f263fa50966df6bbd7f8c6e6e99e3791c94444f7c4343b2fef1ee2d62fd39f](https://etherscan.io/tx/0x51f263fa50966df6bbd7f8c6e6e99e3791c94444f7c4343b2fef1ee2d62fd39f) | E04 direct ETH |
| onward | [0x551d7961652e6d9835b11988908adf86ebe480badb4ce2d7d52193b2b1b02c76](https://etherscan.io/tx/0x551d7961652e6d9835b11988908adf86ebe480badb4ce2d7d52193b2b1b02c76) | E05 direct ETH onward |
| usdc | [0xdc102dd89dded5a83f1008906883ffb7c81ff3b7d7965d8c7277d170b5e17481](https://etherscan.io/tx/0xdc102dd89dded5a83f1008906883ffb7c81ff3b7d7965d8c7277d170b5e17481) | E06 USDC log 685 |
| delegation | [0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b](https://eth.blockscout.com/tx/0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b) | Authorization metadata only; not a fund-flow edge |

## Transaction evidence

**Blockscout Ethereum** provides five transaction-detail captures, two pages of sweep logs, one page of USDC logs, and the sweep's execution trace. Each bundled body is a factual extract of the response, excluding unrelated labels, prices, and navigation metadata. The sweep log pagination ends on page two. The sweep summary's transfer-overflow flag is retained and prevents treating that summary as a complete token inventory.

**Etherscan** provides four independently extracted transaction summaries. Relevant USDT, RLUSD, and USDC events are decoded from the page's receipt-event section. Native quantities are extracted from its internal-transfer or transaction-value display. The comparisons cover hash, success, block, UTC time, transaction sender/target, and selected movement amounts/endpoints. Explorer labels provide wallet names; label provenance is separate from the verified movement itself.

There are **13 capture bodies**. `body_sha256` hashes the exact bundled UTF-8 body. `source_response_sha256` hashes the original response from which the subset was extracted; original HTML and unabridged API responses are not bundled, so their hashes cannot be recomputed from the subset. Raw log topics/data and the full sweep execution trace remain available inside the extracts. Hashes detect changes relative to these stored values; they do not notarize collection or replace independent node validation.

## Issuer and protocol references

| Asset / protocol | Primary reference | Use |
|---|---|---|
| Ethereum USDT | [Tether supported protocols](https://tether.to/en/supported-protocols/) | Canonical token `0xdac17f958d2ee523a2206206994597c13d831ec7` |
| Ethereum USDC | [Circle supported blockchains](https://help.circle.com/support/en/usdc-supported-blockchains-minting-redemption-faqs?id=kb_article_view&sysparm_article=KB0010590) | Native token `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` |
| Ethereum RLUSD | [Ripple token addresses](https://docs.ripple.com/products/stablecoin/overview/token-addresses) | Proxy `0x8292bb45bf1ee4d140127049757c2e0ff06317ed` |
| EIP-7702 | [Official specification](https://eips.ethereum.org/EIPS/eip-7702) | Authorization tuple validation and persistent delegation semantics |

## Reporting and unresolved claims

- [Reuters, October 29](https://www.reuters.com/legal/transactional/tether-circle-freeze-238-billion-after-binance-reports-security-incident-2026-10-29/): reporting context for Binance's investigation and reported aggregate frozen assets. It is not the source of individual ledger amounts.
- [CryptoTicker incident report](https://cryptoticker.io/en/binance-hack-hot-wallet-drained/): lead for reported Tornado Cash funding. Its interpretation is not substituted for a verified withdrawal transaction or deposit linkage.
- User-supplied screenshot, reviewed October 29: intake source for the initial wallet identifiers and reported USDT/USDC freeze amounts. The author, original post timestamp, and claimed Chainalysis tracing are not authenticated. The screenshot is not republished.

No freeze events, current frozen balances, complete cross-chain path, named actor, DPRK attribution, original attack root cause, or recovered value are independently established here. The USDC token sender's explorer label does not prove its legal ownership. Public transaction data is used without confidential case records or paid blockchain-intelligence exports.
