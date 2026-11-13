# Runtime participant configuration

Optional CLI flag: `--allocation-config /absolute/path/confirmed-participants.json`.
The agent prepares this temporary JSON only from the current inputs and explicit user confirmations where identity is ambiguous. It is not another mandatory source export. Omitted PM/Estimator people remain eligible for source-driven discovery. Explicit mappings replace inferred vehicles for that person only, and support any number of vehicles. Vehicle strings are exact current QuickBooks Name values. A person must exist in the corresponding current DASH role. Unknown fields, duplicate people, duplicate vehicles in one mapping and absent vehicles are errors.

```json
{
  "pm": [
    {"foreman": "Example New PM", "vehicles": ["Exact current QB vehicle Name", "Another exact QB vehicle Name"]}
  ],
  "estimator": [
    {"estimator": "Example New Estimator", "vehicles": ["Exact current QB Name"], "displayAlias": "Optional label"}
  ]
}
```

Construction Class eligibility, report-month rules, estimate-weighted PM allocation, equal-weight Estimator allocation, raw-gas toll denominator, cent rounding, held pools and ownership-conflict behavior are unchanged. Explicit confirmation does not override an ownership conflict or Class eligibility. Shared PM/Estimator pools are held, not allocated twice. Reports still reconcile exactly; a workbook with held money can retain FAIL under the existing accounting policy. Generation success does not mean accounting PASS.

## Employee-hours mappings

Optional `employeeHoursMappings` replaces the complete default employee-hours role configuration; omission retains the existing special role rules, while `[]` disables those configured roles. It does not affect PM or Estimator discovery. Use confirmed roles rather than assigning a new person to another person's business policy by guesswork.

Each mapping has:

- `id`: stable unique identifier.
- `employeeMatch`: `{ "mode": "full_name", "value": "Confirmed Full Name" }` or `first_name` mode.
- `classificationExemptServiceItems`: array of explicitly eligible service items.
- `hoursSelection`: `{ "mode": "service_items", "serviceItems": ["Construction"] }` or `{ "mode": "non_excluded_jobs" }`.
- `vehicleOrName`: exact current QuickBooks Name.
- `poolClaim`: `{ "mode": "classes", "quickBooksClasses": ["Construction"] }` or `{ "mode": "all_classes" }`.
- `displayLabel`: readable label. Optional `ownershipLabel`.
- `presentation`: `{ "kind": "con_mit", "optional": true }` or `{ "kind": "worksheet", "worksheetLabel": "Confirmed label" }`, optionally with a unique `summaryKey`.

The runner validates these through its existing employee-hours policy validator. Preserve service/Class restrictions and ordinary exclusions unless the user explicitly changes that business rule.

## Established allocation roles

Prior profile PM/Estimator roles are retained with identity aliases as compatibility defaults, independently of incidental appearances in the other DASH role. Established exclusive PM identities remain PMs. Current explicit mappings override defaults; two conflicting explicit mappings are still held. New people and current replacement/multiple vehicles remain source-discovered without a closed roster. Unknown dual-role ownership still requires resolution; there is no blanket PM precedence.
