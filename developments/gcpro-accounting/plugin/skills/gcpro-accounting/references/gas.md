# GCPRO Gas Report

## Required execution contract

For every Gas Report request, read this workflow and execute its bundled Node runner. The agent is an operator of the accounting engine, not an author of a replacement allocation algorithm. Read-only inspection of inputs is allowed; constructing a report outside the runner is not.

Before any report is delivered, require all of the following evidence from this run:

- All five sources are assigned and passed to the runner, including PM Start, PM Major and Estimator Inspect. Never ignore DASH inputs because their jobs have no same-day employee timesheet match.
- The generation JSON reports `success: true`, `runnerVersion`, `outputPath`, `outputSha256`, and `verification.success: true`. Accounting status may still be FAIL or REVIEW REQUIRED and must be reported honestly.
- The delivered file is exactly that `outputPath`, unmodified after verification, with the returned SHA-256. Do not rename it into a preliminary summary or replace it with an independently built file.
- Its sheets include CON&MIT, PM, Estimator, Review Required, Reconciliation, Pivot Gas, Pivot Tolls, QB Gas by Department and configured employee sheets. Return the complete workbook even when review items remain.

Never use openpyxl, pandas, xlsxwriter, a generic spreadsheet authoring workflow, or custom JS/Python to calculate or write the report. Never substitute a report containing Summary / Gas Transactions / Job Allocations / Needs Review / Methodology. Never invent an allocation rule based on card-holder surname plus transaction date, subtract credits as a new policy, omit tolls, or call a partial allocation a Gas Report. PM weighting remains Total Estimates; Estimator weighting remains equal eligible jobs; class-wide Contents/Mitigation allocation remains the existing monthly eligible-hours policy.

If execution or packaged files are unavailable, report that exact capability failure and do not generate a replacement. If an input is missing, ask only for that input and resume the same runner. This is a skills-only execution workflow: the file format alone is not evidence that the runner was used.


This Work workflow uses only five files manually supplied by the user. Never connect to DASH, QuickBooks, or any external service; never request login credentials. Use the deterministic accounting engine included in this skill. PMs, estimators, and their vehicles are discovered from the current inputs, not a fixed roster. Do not recreate calculations in a spreadsheet or modify rules to force PASS.

## Inputs

Locate supplied files in the current chat or user-authorized locations. Do not reuse another chat's inputs. Inspect files read-only and identify the Timesheet and QuickBooks by structure, not filename:

- Timesheet CSV/XLSX/XLSM: Service Item, Job Code 2, and Hours (Total Hours / Worked Hours aliases supported). Job Code 1 is display text only.
- QuickBooks XLSX/XLSM: Date, Name, Class, Debit (recognized aliases supported), with a monthly toll total or toll transaction area when available. A missing toll total is not a missing QuickBooks file; the user can supply the total separately. Headerless input is accepted only if the engine can establish one unique mapping.
- Three DASH XLSX/XLSM files with Job Number and supported fields such as Foreman, Estimator, Total Estimates, Start Date, Date of Majority Completion, Date Inspected, and Status.

An Excel timesheet is a supported source. Pass its original `.xlsx` or `.xlsm` path directly as `--timesheet`; do not ask the user to export CSV and do not manually rebuild or edit it. The runner reads the structurally detected worksheet and normalizes cell values in memory into the unchanged hours/allocation engine. Preserve typed dates, hours, employee fields, job codes and source row order. Saved formula results can be read; macros and formulas are never executed. If a formula lacks a saved result, report the specific cell and request a recalculated saved workbook rather than inventing its value.

The three DASH files share one structure. Get explicit user assignment to PM Start, PM Major, and Estimator Inspect. A user statement or attachment description assigning roles is sufficient; a filename or date-column presence alone is not. If roles are ambiguous, ask one concise question assigning all three. Ask for missing files together. Never invent inputs or infer roles by elimination.

The engine validates the same single report month in Timesheet and QuickBooks and applicable toll dates. Use actual source dates, not filenames or the current month. If periods disagree, report the error and request corrected sources; do not edit source dates. Read [accounting behavior](references/behavior.md) when interpreting allocations, eligibility, held pools, or review items.

## Toll total: file, separate amount, or one reminder

1. Prefer the readable monthly toll total or validated toll transactions in the current QuickBooks workbook. A numeric cached result of a labeled toll-total formula is readable; do not execute Excel formulas or macros.
2. If the workbook does not establish a toll total, use an amount the user explicitly supplied for this report month in the current conversation. Add `--total-tolls <CONFIRMED_AMOUNT>` to the SAME generation command. Normalize a clear currency entry to a nonnegative decimal string with at most two decimal places, for example `125.50`. Zero is a valid explicit amount. Never assume zero when no amount was supplied.
3. If neither source exists, ask once: “Яка загальна сума tolls за цей місяць? У файлі не вдалося її прочитати. Якщо tolls не було, вкажіть 0.” Preserve all five file assignments and resume the same runner once the user answers. The runner returns `code: toll_total_required` and `requiredInput: totalTolls` for this expected input request. Do not ask the user to edit the workbook, upload it again, or provide another export merely to supply the toll total.

If both sources exist, the readable workbook amount takes priority. Report any runner notice that the separately supplied amount differs. Conflicting readable totals or malformed toll transactions remain source errors; a separate amount must not conceal them.

A separately entered toll amount MUST use the normal complete accounting writer. Never substitute a simplified workbook, hand-built spreadsheet, partial summary, CSV, or a different calculation path. Keep every department and all normal output sheets, including `QB Gas by Department`, `Pivot Gas`, `Pivot Tolls`, PM, Estimator, CON&MIT and configured employee sheets. Run `--verify-workbook` on the actual output before delivery; it now checks departmental and Name/Class breakdown totals as well as reconciliation. Missing toll input is an input reminder, not a reason to abandon the workflow.


## Structural Timesheet categories

Identify projects by the canonical number in Job Code 2, never by a person's name, parent label, or an allowlist of customers. A nonblank text-only Job Code 2 with no numeric characters is a non-project category and is excluded before allocation. This covers new staff/category labels without code updates. Preserve the existing internal-code and Construction employee rules. Blank codes, malformed codes containing numeric characters, and invalid hours remain review items; never repair or infer their job numbers from Job Code 1. The runner returns excluded source rows, labels, service items, hours and reasons in `timesheetExclusions`; exclusion is explicit, not an allocation to another job.

## New people and vehicles

Preserve established allocation roles automatically: the runtime retains prior PM and Estimator role assignments as compatibility defaults. Established exclusive PM identities retain their PM allocation even if present in an Estimator field. Do not ask the user to reconfirm these established assignments. Current explicit runtime mappings override defaults; new people and vehicles remain supported through source discovery. Never apply a blanket PM-over-Estimator precedence to unknown people.

Never refuse a report because a PM, estimator, or vehicle is new. There is no fixed PM/estimator allowlist and no five-PM limit. The runner discovers people from the supplied DASH Foreman and Estimator fields and matches current exact QuickBooks Name/Class pools. One person may have multiple vehicles; those pools share that person's existing job-weight denominator.

Automatic identity matching ignores case, accents, and extra whitespace. It accepts a full-name suffix or a unique first-name / first-name-plus-last-initial suffix across current PMs and estimators. Previously established profile aliases (for example Mike L, Kris and Alex) remain supported automatically on current source vehicles. These are identity aliases, not a fixed vehicle assignment or participation whitelist. Do not infer new nicknames, guess between duplicate names, assume an old vehicle is still assigned, or allocate the same pool twice.

Inspect `participantResolution`, held pools and review items. If a relationship is unresolved and money is held, ask one concise question naming the people and exact QuickBooks Names requiring confirmation. A user statement in this conversation confirming the relationship is enough. Do not ask for code changes, a new plugin release, credentials or a sixth accounting export.

When needed, write a temporary UTF-8 JSON allocation config from confirmed user statements, then add `--allocation-config <CONFIG_JSON>` to the normal generation command. This is run data, not a code edit. Each `vehicles` entry must match an exact current QuickBooks Name. Multiple vehicles are supported. An explicit empty list suppresses automatic matching for that person. Do not manufacture confirmations. See [participant configuration](references/participants.md).

The existing special employee-hours business rules remain separate from PM/estimator discovery. If their assignments change, the same optional run config accepts the complete `employeeHoursMappings` list using the documented mapping schema. These are role-specific allocation rules, not a whitelist for other employees or new PMs.

## Execute and verify

Use an available execution environment with Node.js 20 or newer and access to both this skill and the five files. Resolve this skill directory from its loaded location; never use a creator-specific absolute path. If Node or file execution is unavailable, clearly report that limitation instead of claiming a report was produced. No npm packages, package installation, network access, API keys, or server are needed.

Run these commands separately, proceeding only on success, with absolute paths substituted for placeholders:

```text
node <SKILL_DIR>/engine/scripts/dist/run-gas-report.mjs --verify-distribution
node <SKILL_DIR>/engine/scripts/dist/run-gas-report.mjs --timesheet <TIMESHEET_CSV_OR_XLSX_OR_XLSM> --quickbooks <QB_XLSX> --pm-start <PM_START_XLSX> --pm-major <PM_MAJOR_XLSX> --estimator <ESTIMATOR_XLSX> --output <NEW_WRITABLE_OUTPUT_DIRECTORY>
node <SKILL_DIR>/engine/scripts/dist/run-gas-report.mjs --verify-workbook <ACTUAL_RETURNED_WORKBOOK_PATH>
```

Quote each path using the active shell's safe quoting. Choose a fresh output directory in the task's writable artifact location, outside the installed plugin. The engine refuses to overwrite an existing workbook. Keep inputs read-only. Do not execute Excel macros.

The engine/ directory contains the versioned, integrity-checked accounting runtime and its participant resolver. Follow THIS skill's manual five-input workflow. Do not export DASH, follow creator-specific paths or install dependencies. Runtime integrity covers executable code, allocation policy JSON and immutable supporting files; host-facing SKILL.md and agents/openai.yaml are release-package metadata, not runtime hash dependencies. Do not repair a mismatch by editing files or regenerating hashes. On hash mismatch or runtime/verification failure stop and show the actual error; do not refresh hashes, rebuild, simplify formulas, or substitute a different engine during report generation. A confirmed participant mapping or separately supplied toll total is an ordinary supported runtime input and does not change engine integrity. Handle `toll_total_required` using the reminder above, then rerun the same engine; do not improvise another workbook.

## Deliver

Return the verified Monthly_Accounting_YYYY-MM.xlsx as a downloadable artifact. Report the month, source/allocated/held gas and toll totals, differences, Review Required count, section statuses, and overall accounting status. Generation success is separate from accounting status: a verified workbook can still show FAIL or REVIEW REQUIRED. Explain material held amounts or review issues without changing policy. If verification fails, do not label the workbook final or verified.

Default workbook sheets: CON&MIT, PM, Estimator, Review Required, Reconciliation, Pivot Gas, Pivot Tolls, the configured employee sheet, QB Gas by Department.
