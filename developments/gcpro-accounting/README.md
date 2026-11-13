# GCPRO Accounting

This directory is reserved for the **GCPRO Accounting** Skill and its independent development history. It is **not part of the GCPRO website**, WordPress, Elementor, or the website deployment process.

## Scope

- Existing Gas & Tolls report, retained inside the renamed `gcpro-accounting` Skill
- Dumpster allocation report
- Inventory allocation report
- Skill packaging, tests, reconciliation, and development documentation

## Boundaries

- Keep accounting source and documentation inside `developments/gcpro-accounting/`.
- Do not modify the website's source, documentation, or deployment configuration as part of accounting development.
- This repository is **public**. Do **not** commit real Timesheets, QuickBooks exports, accounting workbooks, employee or customer records, confidential business data, credentials, or private financial calculations and amounts. Use sanitized fixtures only.
- Preserve the existing Gas Report logic until changes are independently verified.

## Status

The existing Skill is renamed **GCPRO Accounting** (`gcpro-accounting`) and extended
with `gas`, `dumpster`, and `inventory` workflows. The extension code, sanitized
tests, packaging tools and documentation live only in this directory. The existing
GAS accounting payload is unchanged and is **not committed to this public repository**:
it contains private organization-specific employee/vehicle configuration. Install
that authorized payload privately to run the complete Skill. Nothing here deploys
or modifies the website.

## Project files

- [Skill entry point](plugin/skills/gcpro-accounting/SKILL.md)
- [Workflow source](plugin/skills/gcpro-accounting/scripts/)
- [Sanitized accounting tests](plugin/skills/gcpro-accounting/tests/accounting.test.mjs)
- [Accounting rules](ACCOUNTING_RULES.md)
- [Architecture and private-payload boundary](ARCHITECTURE.md)
- [Testing and historical-validation limits](TESTING.md)
- [Work record](WORK.md), [change history](CHANGELOG.md), [development history](HISTORY.md)
- [Project test/build command](tools/project.mjs)

## Local execution

Node.js 20+ is required. Packaging additionally uses Python 3's standard library.
No npm packages or application server are added.

Obtain the existing authorized GAS engine directory through the private workspace
distribution. It must match the pinned release; the installer refuses substitutes.
Keep it outside Git or in the ignored destination:

```text
node tools/project.mjs check --engine ABSOLUTE_PRIVATE_ENGINE_DIRECTORY
node tools/project.mjs test
node tools/project.mjs package
```

Run these from `developments/gcpro-accounting/`. The first command copies a
missing private engine into `plugin/skills/gcpro-accounting/engine/`; it will not
overwrite an existing payload. Subsequent checks need no `--engine` flag.
Without that private payload, this public checkout deliberately reports a missing
capability rather than generating a replacement accounting report.

The private installable Skill ZIP is generated as `dist/gcpro-accounting.zip`.
The same existing workspace plugin is updated using `dist/gcpro-accounting-plugin.zip`.
Both archives are ignored by Git because they contain the private GAS payload.
Packaging tests ZIP extraction, manifests and an actual sanitized Inventory run
from each installed archive. It does not rebuild the GAS engine.

## Reports

- **Gas & Tolls:** original five-input workflow, allocation rules and nine-sheet output.
- **Dumpster:** separate department expense pools. Contents/Mitigation reuse the
  GAS class-hours allocator. Construction uses Construction jobs whose Start Date
  is in the report month, weighted by Total Estimates across that population.
- **Inventory:** one common monthly expense pool, weighted by GAS-eligible job hours.

If no report type is specified, the Skill asks which one. It requests only that
workflow's required input files and amounts. No DASH login or external service
connection is used.

## Data handling

Real reports, historical workbooks, employee mappings, source exports, previews
and detailed comparisons remain in ignored private storage. Public tests create
their own synthetic inputs. Do not force-add ignored files or publish built ZIPs
from this repository. SHA-256 fingerprints and generic accounting algorithms are
not source financial records.
