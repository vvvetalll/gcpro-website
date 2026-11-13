# Change history

## 1.2.0 — 2026-11-13

- Renamed the existing Skill to GCPRO Accounting (`gcpro-accounting`), preserving
  the existing plugin identity and unchanged GAS payload/tests.
- Added Dumpster department expense allocation and common-pool Inventory allocation.
- Added user-confirmed monthly Start Date eligibility for Construction Dumpster.
- Added scoped inputs, exact reconciliation, explicit held/review amounts,
  reopened-workbook checks and sanitized regression coverage.
- Added isolated test/package tooling with extracted-ZIP execution and preserved
  metadata/executable integrity boundaries.
- Established public/private source separation inside the existing accounting
  development directory; excluded private mappings, raw records and built archives.

## 1.1.6 — prior maintenance, verified preserved baseline

- Repaired metadata-dependent distribution verification without rebuilding or
  changing accounting formulas. Executable and allocation-policy hashes remain
  strict; editable host metadata is checked at release packaging instead.
- Original GAS regression suites and workbook comparison passed. Earlier release
  provenance and observed/unverified claims are separated in HISTORY.md.
