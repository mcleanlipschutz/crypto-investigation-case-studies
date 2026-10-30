# Working with the tracing workbook

Open [Binance_2026_Tracing_Workbook.xlsx](Binance_2026_Tracing_Workbook.xlsx) in Excel. It contains six seeded movement rows and space through row 105 for additions. The visible diagram is a **static initial snapshot**; the summary and Graph Edges sheet are formula-linked to the Transfers sheet.

## Extend the trace

1. Add a stable, unique Edge ID to an unused Transfers row. Record UTC time, network context, transaction hash, block, full source and destination addresses, asset contract, decimals, raw integer units, and exact decimal quantity. This version is Ethereum-specific; do not reuse its `ethereum:` node prefix for other chains.
2. Use one row per completed token Transfer log or native movement. Distinguish `log:<index>`, `trace:<path>`, and `tx:value`. A transaction can contain many movements. Use chain ID + transaction hash + event key + asset contract to avoid duplicates.
3. Record the actual token/log or native-transfer endpoints in Source/Target. Transaction sender and transaction target have separate fields. A contract invocation does not necessarily transfer money to that contract.
4. Mark Flow role as Initial receipt, Onward transfer, or Other. Preserve gross observed movement separately from any later victim-fund allocation. No allocation model is implemented here.
5. Add evidence URLs and notes; set Review status to Pending review until validated. Use Verified only after checking the amount, contract, endpoints, transaction outcome, and event/trace. Set Evidence status consistently; the Graph Edges sheet carries that value. Excluded or pending records must be filtered out before drawing a verified-funds graph.
6. Add new wallets to Wallets. Node IDs must match the chain-qualified addresses used in Graph Edges, for example `ethereum:0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c`. Use lowercase full addresses as IDs; short labels are display-only.

The prefilled display-quantity formulas, graph formulas, and summary ranges cover Transfers rows 6–105. Beyond row 105, extend all three ranges and table boundaries. Do not overwrite formula columns when pasting new data. Add new wallet rows to the Wallets table as needed.

## Preserve exact amounts

Excel numeric values retain about 15 significant decimal digits. Ethereum raw amounts commonly exceed that limit. **Raw units and Exact quantity are stored as text** and must remain text when pasted, imported, or exported. Display quantity is calculated numerically for sorting and summaries and is approximate. It is not the forensic amount of record.

The evidence snapshot and CSV preserve exact decimal strings. When importing CSV into Excel, explicitly set RawUnits, AmountExact, transaction hashes, and addresses to Text. Double-clicking a CSV can let Excel infer numeric types and round amounts. An amount of zero differs from a missing amount. Do not fill unknown quantities with zero.

## Produce a visual trace

The repository contains starter [nodes.csv](nodes.csv) and [edges.csv](edges.csv). These are static exports of the initial six movements. To export updates, save the Wallets and Graph Edges sheets as separate CSV copies, excluding blank IDs and unverified records. Keep the original `.xlsx` intact.

For a graph tool accepting node and edge tables:

| Field | Use |
|---|---|
| Nodes `Id` | Unique wallet identity; join on this exact field |
| Nodes `Label` | Readable node name; retain attribution qualifier |
| Edges `Source` and `Target` | Directed endpoints referencing node IDs |
| Edges `Id` | Unique movement ID; retain parallel edges between the same wallets |
| Edges `Label` | Exact amount and asset shown on the edge |
| Edges `TxHash` / workbook Transaction hash | Underlying evidence reference |
| Edges `Asset` | Color or filter category |
| Edges `FlowRole` | Distinguish initial receipts from later movement |

Import nodes first, then directed edges. Preserve multiple edges between the same pair, because ETH, USDT, and RLUSD are different assets. The CSV has no universal Weight column: 1 ETH and 1 USDT are not comparable weights. Use uniform widths or filter to one asset before sizing edges. Add USD-based weights only with an explicit price source and timestamp.

Keep approvals, delegation relationships, freezes, and speculative attribution separate from fund-flow edges. They can be drawn as distinct annotations later, with their evidence status visible. Do not draw a freeze as a payment to Tether or Circle.

## Scope and checks

The summary totals only rows marked Verified and separates initial receipts from onward transfers. It is not an incident-wide loss estimate or a wallet balance. The saved offline verifier validates the original packaged evidence and CSV files; it does not automatically validate your later workbook edits. Export and review new records before publishing an expanded case study.

Formula recalculation, a new-record extension, graph-link updates, and formula-error scans were checked with the authoring engine. Desktop Microsoft Excel itself was not run. The static SVG and embedded picture must be regenerated when the trace changes.
