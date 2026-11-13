# Existing GAS accounting behavior

This is sanitized operator guidance. The unchanged private accounting payload is
authoritative for company-specific mappings and exceptions. Do not publish its
employee identities, vehicle assignments or exact private override values.

## Inputs

The GAS workflow accepts Timesheet CSV/XLSX/XLSM, QuickBooks gas/tolls XLSX/XLSM,
and explicitly assigned PM Start, PM Major and Estimator Inspect exports. The
three DASH roles have the same structure and are not inferred from filenames.
Period validation and read-only formula-cache handling remain those of the
existing runtime. A separately confirmed toll amount is supported only through
the normal complete workbook writer, never a simplified report.

## Preserved calculations

- Toll shares by Name/Class use the original full raw-gas denominator.
- Class-wide Contents/Mitigation pools use eligible job hours.
- PM pools use eligible job Total Estimates.
- Estimator pools use equal eligible-job weights within resolved exact pools.
- Special employee-hours roles retain their distinct configured hours rules.
- Money uses the original Decimal largest-remainder cent allocation and stable
  tie behavior. Zero-weight nonzero pools remain unallocated/held, not fabricated.

Canonical job identity is Job Code 2; Job Code 1 is display text. Internal and
non-project exclusions, invalid-hour handling, supported service eligibility,
Construction employee exceptions and malformed-job review retain existing policy.
There is no new employee or customer allowlist in this extension.

## Ownership and participants

Current source people and vehicles are resolved by the original participant
resolver. Existing exclusive roles, identity aliases and confidential exact-match
historical overrides remain intact. A matching person name alone does not bypass
Class eligibility. Conflicting exact Name/Class pools are held once; unrelated
valid pools continue allocating. No blanket PM-over-Estimator precedence is
introduced for unknown identities. Confirm ambiguous mappings using supported
runtime input configuration; do not modify packaged policy to force PASS.

## Reconciliation and outputs

The GAS report keeps its existing nine-sheet default workbook: CON&MIT, PM,
Estimator, Review Required, Reconciliation, Pivot Gas, Pivot Tolls, the configured
employee sheet and QB Gas by Department. Existing formatting is unchanged.

Displayed reconciliation remains expected minus allocated minus held/remaining
equals difference. Money must not disappear or be allocated twice. Generation
success and accounting status are separate: FAIL or REVIEW REQUIRED must remain
visible when source issues or held money remain. Return the original verified
workbook, not an independently authored summary.
