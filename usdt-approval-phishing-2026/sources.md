# Sources, provenance, and limitations

Prepared October 26, 2026. URLs and UTC collection times for transaction captures are preserved in [evidence/snapshot.json](evidence/snapshot.json). Incident reporting supplies context; the asset accounting comes from transaction records.

## S1

**Scam Sniffer — original public alert.** [Post](https://x.com/realScamSniffer/status/2075007064154452200)

The alert identifies the reported victim address and describes a roughly 999,999 USDT approval-phishing loss. This is external incident attribution, not a firsthand victim statement. Direct retrieval of X was unavailable; indexed text and the linked contemporaneous article were available. The exact post-publication time was not independently established and is not used to date the transactions.

## S2

**Etherscan — transaction summaries and receipt events.** Primary transaction-record access through an explorer.

- [A1 approval](https://etherscan.io/tx/0x295549f3dabb8c02ed1910386bee51b6bcc6f2074887dba43d54806320b4bde2)
- [A2 separate direct transfer](https://etherscan.io/tx/0x21aaa9d9295d289d8e4dca7433112f151e157dc1022f4b3687a87948df1d8fe9)
- [D1 first multicall](https://etherscan.io/tx/0x19ddd4f515f71da24859992496c9b1424bb26a6a9d02075f76b7eb258270f37c)
- [D2 second multicall](https://etherscan.io/tx/0x6e882fd802e96c51521869e9f433fec00aac5403d39356820d14e8a3f2e6ffb9)
- [X1 look-alike token example](https://etherscan.io/tx/0x7046fbb549067529c4df3cab2da926cd38135c0dcfad0a10ea55804fd0bc3d87)

Four factual extracts cover A1, A2, D1, and D2: full hash, status, block, transaction position, timestamp, transaction sender/destination, receipt-event addresses and values, and presence of an internal error. They were parsed from retrieved HTML independently of Blockscout. The snapshot preserves both a digest of each extracted body and the source HTML digest. Full HTML is not bundled; its digest cannot be recomputed from the extract alone. X1's Etherscan page was reviewed but is not one of these four packaged extracts.

Explorer phishing labels are external annotations. They may change and do not establish ownership, government attribution, or a common controller. Present-day price displays are not used as incident-date valuations.

## S3

**Blockscout Ethereum — transaction details, raw logs, and execution trace.** Primary transaction-record access through a second explorer.

The snapshot contains nine exact JSON response bodies:

| Capture ID | Endpoint / purpose |
|---|---|
| `approval-tx` | A1 transaction details and calldata |
| `approval-logs` | A1 raw Approval event |
| `first-drain-tx` | D1 transaction details and transfer summary |
| `first-drain-logs` | D1 raw Transfer event |
| `first-raw-trace` | D1 internal-call outcomes and calldata |
| `blockscout-tx` | D2 transaction details and transfer summary |
| `drain-logs` | D2 raw Transfer events |
| `side-transfer-tx` | A2 direct-transfer details |
| `spoof-tx` | X1 transaction details and noncanonical token identity |

For example, [D1 raw trace](https://eth.blockscout.com/api/v2/transactions/0x19ddd4f515f71da24859992496c9b1424bb26a6a9d02075f76b7eb258270f37c/raw-trace) distinguishes its completed call from its failed internal call. [D2 raw logs](https://eth.blockscout.com/api/v2/transactions/0x6e882fd802e96c51521869e9f433fec00aac5403d39356820d14e8a3f2e6ffb9/logs) provide the canonical emitter, indexed addresses, amounts, and log indices.

All three bundled log responses have no next page; the transaction summaries report no transfer overflow. The scope is selected transactions, not a complete account-history export. Unused provider metadata in the raw bodies, including tags and prices, is not adopted as an investigative conclusion.

## S4

**Ethereum EIP-20 — ERC-20 Token Standard.** [Official specification](https://eips.ethereum.org/EIPS/eip-20)

Reference for approval, allowance, transferFrom, Transfer events, and Approval events. It explains the permission and event model. Individual token implementations can differ; the trace relies on the actual contract's observed execution and logs, not an assumption that every attempted call succeeds.

## S5

**Cointelegraph — contemporary incident coverage, published July 9, 2026.** [Article](https://cointelegraph.com/news/trader-loses-1m-after-signing-phishing-token-approval)

Used for reporting context and the link to Scam Sniffer. The article's image caption counts three transactions, while the verified initial loss has two transaction hashes and three Transfer events. Its failed-attempt description also needs qualification: D1 completed a 200,000 USDT transfer despite an internal error. The chain records control these technical findings. The article's description of automated recalculation is not treated as proof of the operator's code or intent.

## S6

**Tether — Supported Protocols and Integration Guidelines.** [Official issuer page](https://tether.to/en/supported-protocols/)

Lists `0xdac17f958d2ee523a2206206994597c13d831ec7` as Ethereum USD₮. This is the asset-identity reference used to reject tokens that merely share its name or symbol.

## Reproducibility limits

The [verification script](verify_trace.py) checks SHA-256 over each saved UTF-8 body, explorer field agreement, ABI-decoded approval and multicall inputs, raw-event amounts, recipient totals, internal-call failure, gas arithmetic, and exclusion of the look-alike token. Etherscan extracts are factual subsets, not raw page archives. Hashes detect changes relative to the saved evidence; they do not authenticate a provider, establish collection-time notarization, or prove blockchain consensus.

A separate Ethereum RPC receipt lookup returned null and supplies no corroboration. No node was independently synchronized or used to replay execution. The two-explorer comparison supports the bounded reconstruction without eliminating shared indexing or interpretation risks. The study establishes no current balance, complete downstream trace, victim identity, private-key compromise, law-enforcement attribution, or recovery.

[Case overview](README.md)
