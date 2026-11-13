# GCPRO accounting workflows

One Skill supports gas, dumpster and inventory. Ask which report when unspecified.
Use the supplied files read-only. No external services, dependencies or macros.

## GAS

Use the unchanged `engine/scripts/dist/run-gas-report.mjs`, or route through
`scripts/run-accounting.mjs --workflow gas` followed by the same existing flags.
All GAS eligibility, ownership, special cases, formulas, formatting and nine-sheet
output are unchanged. The engine SHA-256 is pinned to the verified 1.1.6 release.
Read `gas.md` for the complete existing GAS instructions.

## Inventory

Required: one Timesheet CSV/XLSX/XLSM, report month and a single nonnegative
whole-cent monthly expense. No QuickBooks, DASH, PM Major or Estimator export.

```text
node scripts/run-accounting.mjs --workflow inventory --timesheet ABSOLUTE_FILE --month YYYY-MM --total AMOUNT --output NEW_DIRECTORY
```

The verified GAS CSV/XLSX adapter, classifier, canonical job normalization and
hours aggregation determine eligible project hours. Excluded rows and review
rows retain their existing GAS treatment and are shown in the output. Eligible
hours are combined by canonical Job Number across service items, with no duplicate
expense for a job. No new person/customer exclusions are introduced. Unknown
or malformed job information stays in Review Required, not an invented project.

One common pool is allocated by eligible job hours divided by total eligible
hours. Reuse the GAS Decimal largest-remainder cent allocator in stable Job Number
order. Do not use estimates, equal shares, vehicle ownership or departmental
expense budgets for Inventory. A nonzero pool with no eligible weights remains
held, with accounting status FAIL; never call it a fully allocated report.

Historical reference `Inventory 2026.xlsm` has separate Mitigation/Contents pools.
The user's explicitly requested single-pool policy supersedes that historical
budget split. Therefore historical dollar outputs are not a parity baseline for
the new single-pool workflow. An original Timesheet is available for an inspected historical month.
Its canonical job-level hours match the reference. Private amounts and source
records are retained only in local, ignored validation evidence. Validate job hours and the
new formula independently. Historical October D110:D163 uses the incorrect
denominator B161 for that shared-formula block, including D163. Do not copy its
over-allocation or silently repair the historical source.

## Dumpster

Required: month and three explicit expense amounts for Construction, Contents,
Mitigation. Zero must be explicit, not assumed. Timesheet is needed if either
hours-based department has expense. PM Start is needed if Construction has
expense. Do not request QB, PM Major or Estimator files.

```text
node scripts/run-accounting.mjs --workflow dumpster --timesheet ABSOLUTE_FILE --month YYYY-MM --construction AMOUNT --contents AMOUNT --mitigation AMOUNT --pm-start ABSOLUTE_FILE --output NEW_DIRECTORY
```

Contents/Mitigation invoke the unchanged GAS `buildConMitAllocationDataset` with
department expense pools in place of its vehicle expense pool input. It uses the
existing class-wide hours policies and rounding. Budgets remain separate; no
Construction or employee-specific GAS vehicle budget is introduced here.

Construction historical evidence: `9 Sept 2026.xlsm`, PM E2:E58 uses
`Total Estimates / SUM(C2:C58) * Construction total` across one selected population,
not separate foreman pools or equal shares. It contains a selected CIP/CND/CNI population and one Construction
expense pool. Actual amounts and customer records are not stored in this public
source tree. Selection
criteria cannot be inferred from this output-only list. There is no source PM
Start export or original September Timesheet in the supplied historical workbook.

The user subsequently confirmed the eligibility rule: Construction jobs whose
Start Date falls in the report month. The runtime uses existing canonical job
types CIP/CND/CNI and `isInReportMonth` to select that population automatically.
Weight it by Total Estimates across one shared monthly Construction pool.
Other-month/non-Construction jobs do not qualify. No PM vehicle, foreman allowlist,
Timesheet match, PM Major date, minimum estimate or extra selection file is needed.
Missing dates are shown for review, not inferred. Missing/negative estimates or
conflicting source fields are errors. Identical duplicate source jobs are merged
by the existing DASH normalizer and cannot receive the pool twice.

The September reference lacks its original PM Start export and daily Timesheet,
so its historical selection cannot independently prove the newly confirmed date
rule. Its job hours and estimate inputs can still validate the weighting formula;
label that reconstruction as a historical-input check, not an original-source audit.

## Outputs and verification

Inventory: Inventory, Reconciliation, Review Required, Excluded Hours.
Dumpster: CON&MIT, Construction, Reconciliation, Review Required, Excluded Hours.
Job-level source-row references are retained. Reconciliation shows each source
pool, allocated, held, difference and status plus a source-hours classification
tie-out. Verify every written job, source budget and reconciled total after
reopening the actual workbook. Return the exact output and SHA-256 from this run.
Execution success is separate from accounting status PASS/REVIEW REQUIRED/FAIL.

No expense can be allocated beyond the supplied pool. Nonzero pools with no
eligible weights are explicitly held and FAIL. Invalid/negative/sub-cent amounts,
ambiguous input structures and missing/out-of-period dates fail before writing.
No source data or historical amount is used to fabricate missing inputs.

Integrity: `scripts/run-accounting.mjs --verify-distribution` verifies both the
unchanged GAS payload and the new immutable workflow files. Host-editable Skill
and UI metadata remain outside runtime hash dependencies, while release archive
manifests cover their final serialized bytes. Never refresh hashes during a run.
