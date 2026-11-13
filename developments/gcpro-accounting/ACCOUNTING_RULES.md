# Accounting rules

## Preserved GAS behavior

The original Gas & Tolls runner remains authoritative for all PM, Estimator,
Contents, Mitigation, special employee, ownership-conflict and period rules. Its
Decimal cent allocation, nine-sheet structure, workbook formatting and regression
tests are unchanged. Confidential default mappings stay in the private payload.
See the sanitized [GAS operator instructions](plugin/skills/gcpro-accounting/references/gas.md).

## Shared Timesheet policy

The new workflows use the original read-only CSV/XLSX/XLSM adapter, existing GAS
classifier, canonical Job Code 2 and job-hours aggregation. Job Code 1 is display
text, not a replacement identifier. Existing internal categories and nonparticipating
rows remain excluded, with reasons. Missing/malformed job information or invalid
hours remain explicit review items. No new customer or employee exclusions are added.
Every source row must reconcile into included, excluded or review hours.

## Inventory

One supplied monthly Inventory amount is allocated across canonical jobs by
eligible job hours divided by total eligible hours. Combine the same canonical
job across eligible service groups once. Do not use estimates, equal shares,
vehicle mappings or separate expense pools. Use the existing largest-remainder
cent allocator with stable canonical job ordering.

The historical workbook uses separate department budgets. The user's explicit
single-pool instruction takes precedence. Historical dollar parity is therefore
not a success criterion; independent hours and the requested formula are.

## Dumpster

There are three explicit department budgets: Construction, Contents and Mitigation.
Do not combine them. Contents/Mitigation invoke the exact existing GAS class-hours
allocator using department expense pools through its pool input interface.

The user confirmed Construction eligibility: **Construction jobs whose Start Date
falls in the report month**. Recognize Construction job types with the existing
job parser. Allocate the Construction budget by Total Estimates across that
whole monthly population. Do not split the pool by foreman or require a vehicle,
Timesheet match, PM Major date, fixed PM list or an invented threshold.
Missing Start Dates are review items; do not invent them. Ambiguous source fields,
missing/negative estimate weights and invalid amounts are input errors.

## Money controls

Inputs must be explicit nonnegative whole-cent decimal amounts. A missing amount
is not zero. Reject negative, nonfinite and fractional-cent input amounts. No
expense is allocated twice. A nonzero budget with no eligible weights remains
held and accounting status FAIL. Source = allocated + held; the difference must
be exactly zero. Generation/verification success is distinct from accounting status.
