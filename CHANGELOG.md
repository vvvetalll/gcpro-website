# GCPRO changelog

Record verified delivered changes with date, scope, evidence, validation, and remaining limitations. Do not turn a plan or an uncorroborated chat statement into completed development history. Evidence definitions are in [PROJECT_CONTEXT](PROJECT_CONTEXT.md#evidence-register).

## 2026-10-16 — Repository workflow integration and Homepage V2 reconciliation

- Read the repository instructions and all existing reference documents; verified the target is `vvvetalll/gcpro-website`, with main initially at `701e70cbc6b831ff929d296048e79dc89e655454` and a clean dedicated checkout.
- GitHub authenticated as `vvvetalll`; repository metadata returned admin/push permissions and the collaborator check returned admin. These checks establish reported permission only; delivery also requires a successful real commit/push and a matching remote head.
- Compared fresh read-only Elementor content for 154/62/65/68/80/86/286/113/114 with the implementation's final-state artifact: all nine matched. Confirmed eight Service Card instances, individual saved SVG/content/link overrides, absence of `43e3093`, the non-link DIV root of 286, two Style Guide cards, and no returned local-style entries in these nine documents (E6).
- Added the detailed [Homepage V2 milestone](docs/milestones/2026-10-16-homepage-v2.md) and sanitized [reconciliation evidence](docs/evidence/2026-10-16-homepage-v2-reconciliation.json). Recorded historical responsive/SVG/editor checks and performance limits separately from current reads (E7).
- Documented current H1-H6 HTML Defaults, the 17 V2 class roles, exact eight-card mapping, final Header/eyebrow/city refinements, missing destinations and outstanding visual approval.
- Made documentation update, commit, push and remote verification mandatory after every completed development milestone. Kept shared ROBYLO separate.
- Validation: documentation diff, links, evidence consistency, whitespace checks and remote commit verification. No website writes or new frontend/editor QA. No application/custom code, theme or production changes. The containing commit and delivery receipt identify the actual Git write test; no separate dummy permission-test file is needed.

## 2026-10-16 — Documentation foundation

- Created AGENTS.md, PROJECT_CONTEXT.md, CHANGELOG.md, docs/ARCHITECTURE.md, docs/DESIGN_SYSTEM.md, docs/ELEMENTOR_MAP.md, docs/WORKFLOWS.md, and docs/DECISIONS.md.
- Established permanent staging-only/native-editing rules, mandatory ChatGPT Work milestone documentation, backup and handoff procedures, and a clear boundary with shared ROBYLO.
- Inspected the initial GCPRO history and shared ROBYLO source; recorded read-only staging page/component/template inventories, exposed overrides, variables and class labels (E1–E3).
- Preserved reported implementation and unresolved dependencies separately from current verification (E4/E5).
- Validation scope: documentation content, relative links, expected file set, Git diff and remote commit checks. No WordPress implementation or runtime QA was performed by this milestone. Commit/push receipt is reported with delivery; the containing commit identifies this entry.
- WordPress, production, and the shared ROBYLO repository were not modified.

## 2026-10-16 — Initial repository record

Verified [commit 61624508705fe9d7947d145e3cc9ef973421fb3d](https://github.com/vvvetalll/gcpro-website/commit/61624508705fe9d7947d145e3cc9ef973421fb3d), titled "Update README with project details and links", is the root commit returned by the repository history. It contains the initial README identifying GCPRO Restoration, staging, the shared theme, WordPress, and Elementor Atomic V4 (E1).

## Earlier implementation provenance

E4 reports Homepage V2 delivery on 2026-10-16 and E5 describes an earlier component foundation. The integration entry above adds E6/E7 corroboration and the detailed milestone record. It does not replay implementation or runtime tests. The website changes were made in WordPress, not deployed from this documentation repository; do not assign them a fabricated implementation Git commit or production deployment date.

For a future entry, include: date; environment; actual change and affected IDs/files; source/commit or evidence reference; checks and outcomes; custom-code exceptions; unresolved work. Keep future plans in PROJECT_CONTEXT.
