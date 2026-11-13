# Testing

Run `node tools/project.mjs test` from this directory with the authorized private
GAS payload installed. No packages are installed. Detailed logs are written only
under ignored `test-results/`.

## Automated coverage

Verified maintenance result on 2026-11-13: **44 tests passed, zero failures**.
This comprises the 23 preserved GAS/integrity tests and 21 extension tests.
The original GAS baseline comparison found zero populated-cell differences across
all nine worksheets. Both renamed ZIPs passed extraction, integrity and actual
sanitized installed-CLI execution checks.

The current suite includes the unchanged GAS integrity, participant and end-to-end
tests, plus synthetic extension tests. Coverage includes single-pool Inventory,
three isolated Dumpster budgets, monthly Construction eligibility, estimate
weighting, exact cent rounding, deterministic ties, empty data, zero expenses,
held amounts, missing jobs/dates, invalid inputs, non-project exclusions, Excel
Timesheet parity, duplicate-expense detection and reopened-workbook tampering.

The existing GAS runtime suite can compare against the unchanged private baseline
with `--baseline ABSOLUTE_PRIOR_RUNNER`. Local baseline evidence verifies zero
populated-cell differences across the original nine sheets. Original tests stay
unchanged in the private payload because they include organization-specific
identity fixtures; do not force-add them to public Git.

## Historical validation performed

- Inspected every monthly Inventory worksheet, formulas, cached results and
  expense inputs without running macros or modifying the reference workbook.
- Selected a historical month with an original Timesheet. Independently generated
  the new report from that Timesheet and the historical input expense budgets
  combined into the requested single pool. Canonical job population and job-level
  eligible hours match the historical worksheet. An independent Decimal calculation
  agrees with every new whole-cent allocation and the monthly total.
- Historical dollar outputs do not match the requested single-pool policy, because
  the historical workbook uses separate department budgets. An observed shared
  formula also points to an individual job's hours instead of the monthly total,
  causing historical over-allocation. No historical output values were copied into
  the new calculations, and the source workbook was not repaired.
- For historical Dumpster weighting, independently recalculated Construction,
  Contents and Mitigation from the reference's job-hours/estimate inputs. New final
  cents differ from the reference's unrounded calculations by less than one cent
  per job, with exact department reconciliation.
- Original raw exports for that historical Dumpster month were unavailable.
  This validates its fixed-population weighting, not historical date eligibility
  or a fresh raw-source reconstruction. The new date rule comes from explicit
  user confirmation.
- The delivered Dumpster workbook uses available original Timesheet/PM Start data
  and clearly labeled illustrative budgets, not a claim of actual expenses for
  that month. Existing Timesheet review items stay visible in both samples.
- Rendered every sheet of both new outputs, checked formulas/errors and corrected
  new-report presentation issues. Detailed workbooks, comparisons and previews
  remain under ignored `private-validation/` and are not published to GitHub.

## Packaging/install validation

`node tools/project.mjs package` runs tests before producing ignored deployment
archives. Each ZIP is CRC-checked, extracted, verified against full-package and
runtime manifests, checked for the renamed Skill identity, then used for an actual
sanitized Inventory CLI run. The old portable Skill path must be absent. Private
financial source files and credentials are excluded. Existing GAS code is pinned,
not rebuilt.

Public checkout limitation: it intentionally excludes the private GAS payload.
Tests and report execution require authorized private installation. This is a
documented privacy boundary, not a substitute simplified accounting engine.

Before a public commit, stage only this project directory and run
`node tools/privacy-check.mjs`. Review the diff as well: the automated gate checks
scope, private/generated paths, source-data extensions, email/credential patterns
and unexpected embedded payload sizes; it does not replace contextual review.
