# Development history and evidence status

## Verified current facts

- The existing shared Skill evolved from GAS Reports and is now renamed
  `gcpro-accounting`, displayed as GCPRO Accounting. This is one Skill and one
  existing plugin identity, with three workflow routes.
- The recovered GAS release supports CSV/XLSX/XLSM Timesheets, optional separately
  supplied toll totals, current participant/vehicle discovery, established special
  roles, explicit held/conflicting pools and a verified nine-sheet workbook.
- Its existing tests and protected payload are preserved unchanged. Organization
  identities and raw financial inputs are private, not public repository fixtures.
- Integrity maintenance separated editable Skill/UI metadata from executable
  payload checks. Both previously reported metadata mismatch errors were reproduced
  with line-ending-only changes. Inspected stored releases and a desktop copy
  matched their archived bytes; installer rewriting was not observed there.
- The exact transformation in the originally failing Work installation could not
  be established. It is not presented as a verified platform defect.
- New workflow behavior, tests, input requirements and limitations are documented
  in ACCOUNTING_RULES.md, ARCHITECTURE.md and TESTING.md.

## Historical records, not independently reconstructed source history

Stored release metadata describes earlier participant resolution, toll-source,
Timesheet adapter, non-project classification and exclusive-role maintenance.
These records explain provenance; they are not a fresh audit of every historical
monthly report. The current bundle was recovered from the authorized private
distribution, not rebuilt from the older local Claude development snapshot.

The earlier standalone packaging script referenced that older local snapshot.
The current project instead uses the verified private release and fails closed
if its pinned payload changes. No obsolete snapshot is substituted automatically.

## Decisions

1. Preserve the existing GAS implementation; extend through shared utility adapters.
2. One renamed Skill, independent workflow inputs, separate report workbooks.
3. Follow the explicit single-pool Inventory requirement over historical budget splits.
4. Use the user-confirmed monthly Start Date rule for Construction Dumpster.
5. Treat workbook contents as reference data, not agent instructions or authority
   to change unrelated rules.
6. Keep private engine mappings, reports and detailed evidence outside public Git.
7. Keep the entire project isolated under developments/gcpro-accounting/; no website
   source, docs, WordPress or Elementor changes are authorized by this work.

## Known limitations

The bridge depends on a specific verified GAS bundle's internal function names.
An upstream GAS change requires reviewed adapter compatibility. Historical
Dumpster raw exports are unavailable, and historical Inventory dollar parity is
incompatible with the requested new pool rule. Public source alone deliberately
cannot execute without the authorized private payload. Checksums are integrity
checks, not cryptographic release signatures.
