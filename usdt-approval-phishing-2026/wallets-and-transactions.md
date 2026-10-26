# Wallets and transaction evidence

Network: **Ethereum mainnet, chain ID 1**. Asset: USDT, six decimals. Addresses identify transaction roles; they do not identify people. The loss window ends with D2 on July 8, 2026. [Source register](sources.md)

## Address register

| Role | Full address | Evidence and limit |
|---|---|---|
| Canonical USDT contract | `0xdAC17F958D2ee523a2206206994597C13D831ec7` | Listed by Tether; emitter of the counted events. [S6](sources.md#s6) |
| Reported victim / token owner | `0x8C949361B49320C48a51F4B1C6f9f83862530F89` | Sends A1; source address in D1/D2 Transfer logs. Victim characterization is externally reported. |
| Approved spender / multicall contract | `0x1178a87DB6dc5C010E39A325AF1F73BEc6470502` | A1 approval recipient; D1/D2 transaction destination; caller of USDT in D1's trace. |
| D1/D2 transaction sender | `0x6D8c070338eC3d297f1D0ECEEA296bd7E13a32b9` | Initiates the multicalls and pays their ETH gas fees. |
| Recipient A | `0xf84c62572eEaFC90C0BCE3Fb6c85bCB573E68d93` | Receives 359,999.873783 USDT across D1/D2. |
| Recipient B | `0xc508a8C01bc3835BE67e0e5554B7D91A1bb70Da1` | Receives 639,999.495132 USDT in D2. |
| Separate A2 recipient | `0xe3478b0BB1A5084567C319096437924948Be1964` | Receives 0.631085 USDT by direct transfer. Purpose and relationship are not established here. |

## Transaction register

Times are UTC on July 8, 2026. Positions are zero-based transaction indices as returned by the explorers. Links open Etherscan; matching Blockscout responses are preserved in the [snapshot](evidence/snapshot.json).

| ID | Full transaction hash | Block / position | Time | Result |
|---|---|---|---|---|
| A1 | [0x295549f3dabb8c02ed1910386bee51b6bcc6f2074887dba43d54806320b4bde2](https://etherscan.io/tx/0x295549f3dabb8c02ed1910386bee51b6bcc6f2074887dba43d54806320b4bde2) | 25489459 / 23 | 17:51:47 | Successful approval; log 42 |
| A2 | [0x21aaa9d9295d289d8e4dca7433112f151e157dc1022f4b3687a87948df1d8fe9](https://etherscan.io/tx/0x21aaa9d9295d289d8e4dca7433112f151e157dc1022f4b3687a87948df1d8fe9) | 25489459 / 24 | 17:51:47 | Successful direct transfer; log 43 |
| D1 | [0x19ddd4f515f71da24859992496c9b1424bb26a6a9d02075f76b7eb258270f37c](https://etherscan.io/tx/0x19ddd4f515f71da24859992496c9b1424bb26a6a9d02075f76b7eb258270f37c) | 25489460 / 1 | 17:51:59 | Outer success; one internal call fails |
| D2 | [0x6e882fd802e96c51521869e9f433fec00aac5403d39356820d14e8a3f2e6ffb9](https://etherscan.io/tx/0x6e882fd802e96c51521869e9f433fec00aac5403d39356820d14e8a3f2e6ffb9) | 25489463 / 39 | 17:52:35 | Outer success; two completed transfers |
| X1 | [0x7046fbb549067529c4df3cab2da926cd38135c0dcfad0a10ea55804fd0bc3d87](https://etherscan.io/tx/0x7046fbb549067529c4df3cab2da926cd38135c0dcfad0a10ea55804fd0bc3d87) | 25489463 / 204 | 17:52:35 | Noncanonical token example; excluded |

## Approval and execution

A1 calls `approve(address,uint256)` on USDT with selector `0x095ea7b3`. Its Approval log records the owner and spender listed above and this allowance:

```text
115792089237316195423570985008687907853269984665640564039457584007913129639935
```

That is `2^256 − 1` raw token units, conventionally described as unlimited approval. The approval itself moves no USDT. It is historical evidence, not a current allowance query.

D1 and D2 call `multicall((address,bytes)[])`, selector `0xcaa5c23f`. Their nested USDT calls use `transferFrom(address,address,uint256)`, selector `0x23b872dd`. In D1, the captured trace shows a successful 200,000 USDT call and a failed 800,000 USDT call with `invalid opcode: INVALID`. Etherscan also flags an internal execution error while marking the outer transaction successful. The error alone does not prove its root cause; this study does not claim a verified historical balance check or a specific automated script implementation.

## Exact initial loss accounting

Each included record must have the canonical USDT emitter, the Transfer event signature, the victim as indexed sender, and a successful parent transaction. Amounts are decoded from raw log data as integers, then divided by 1,000,000.

| Transaction / log index | Token sender | Recipient | Raw units | USDT |
|---|---|---|---:|---:|
| D1 / 4 | Victim | A | 200000000000 | 200,000.000000 |
| D2 / 168 | Victim | A | 159999873783 | 159,999.873783 |
| D2 / 169 | Victim | B | 639999495132 | 639,999.495132 |
| **Total** | | | **999999368915** | **999,999.368915** |

Recipient A's directly attributable initial receipts total **359,999.873783 USDT**; B's total **639,999.495132 USDT**. These are receipt totals and starting amounts for follow-up, not present balances. Any downstream allocation requires its own treatment of intervening funds and commingling.

The failed 800,000 attempt contributes zero to completed loss. A2's 0.631085 USDT is a separate direct transfer and is excluded from this defined drain. This exclusion does not resolve whether A2 was authorized by the person controlling the wallet.

ETH gas is accounted for separately. For example, D2 used 165,494 gas at 552,371,608 wei per gas: **91,414,186,894,352 wei**, or **0.000091414186894352 ETH**, paid by the transaction sender. It is not additional USDT removed from the victim.

## Look-alike token exclusion

X1 contains an apparent 200,000-token movement from the victim to `0xf84e291A05c5E8724be54C4a8292EdA763E68D93`. Blockscout identifies that token's symbol as `USDT`, but its contract is **`0x4607094744786EC873eD9f8264D40433deaaD755`**, not Tether's Ethereum USDT contract. It contributes **zero canonical USDT** to this trace.

The look-alike recipient also resembles A in its leading and trailing characters. Compare full addresses and contract identifiers before linking the record. The resemblance supports an address-poisoning hypothesis; it does not prove a shared controller or make the unrelated token event a transfer of genuine USDT. X1's detailed response is saved as an exclusion example, not as another drain transaction.

[Case overview](README.md) · [Triage and handoff](triage-and-handoff.md)
