# Architecture

## One renamed Skill

`plugin/skills/gcpro-accounting/` is the only portable Skill directory. Its
frontmatter identifier is `gcpro-accounting`; UI name is `GCPRO Accounting`.
The existing plugin backend identity is retained during distribution, even though
its original package slug predates the Skill rename. Updating it removes the old
`skills/gcpro-gas-report/` files rather than adding a second Skill.

## Boundaries

- `scripts/run-accounting.mjs`: report routing, scoped input validation and errors.
- `scripts/shared-runtime.mjs`: immutable-payload checks and read-only adapter to
  the existing GAS utility functions. No npm or accounting rebuild.
- `scripts/workflows.mjs`: Inventory and Dumpster orchestration, department pools,
  existing eligibility utilities and the user-confirmed Construction date rule.
- `scripts/report-workbook.mjs`: new workflow Excel reports, existing GAS ExcelJS
  and table styling helpers, exact job/pool verification after reopening.
- `engine/`: private, unchanged GAS release, excluded from public Git. It contains
  parsers, Decimal allocation, class-hours policies, workbook logic and original tests.
- `tests/accounting.test.mjs`: synthetic extension tests; no real records.
- `tools/project.mjs`, `tools/package.py`: maintenance-only preparation, test and
  archive gates. The runtime never regenerates hashes.

GAS calls its original runner directly. Its bundle, resolver, policy, existing
tests and reports are byte-for-byte preserved. There is no new GAS calculation path.

The bundle has no exported utility API. The adapter uses the same controlled
export technique as its existing tests: verify the exact bundle SHA-256, resolve
its existing relative resolver import, disable its CLI footer in a disposable
module copy, and expose the original functions. It never rewrites the installed
bundle or reimplements its calculations. A changed adapter boundary fails closed.
This coupling is explicit; a future GAS upgrade needs a reviewed compatibility
update, not an automatic hash refresh.

## Integrity and reproducibility

The GAS runtime verifies its original immutable payload. The extension has a
separate exact-membership manifest protecting its executable workflow files and
accounting reference. Both are checked before reports run. Host-facing Skill/UI
metadata remains outside runtime hashes to avoid the earlier metadata false
positives. Full ZIP manifests verify metadata and all serialized release bytes.
Private payload fingerprints are pinned in the public adapter; policy values
themselves are never copied into public code.

Package archives have deterministic entry ordering and timestamps. Every archive
is extracted, checked and exercised through its renamed CLI. No source workbook,
report, credential, dependency directory or session state is included. The private
GAS configuration is included only in the ignored private deployment artifact.

Checksums detect corruption and mixed releases. They are not digital signatures
against an actor able to replace both the executable verifier and trusted manifests.
