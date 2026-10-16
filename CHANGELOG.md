# GCPRO changelog

Record verified delivered changes with date, scope, evidence, validation, and remaining limitations. Do not turn a plan or an uncorroborated chat statement into completed development history. Evidence definitions are in [PROJECT_CONTEXT](PROJECT_CONTEXT.md#evidence-register).

## 2026-10-16 — Homepage CTA conversion hierarchy

- Published owner-authorized CTA refinements on Homepage 154: Hero and Final use orange Call first, white-outline Request Service second. Reused existing Component 53/103 and Homepage Component 80 instance overrides in the native visual editor.
- Verified exactly eight text/link leaf changes, with no structure/style changes; Header 113 and Footer 114 match their before reads. All three Homepage call buttons and Footer telephone link use `tel:+18476563322`.
- Preserved researcher paths, Emergency call priority, Header Request Service, city links and disabled ZIP prototype. No new classes, variables, components, custom code, plugins or dependencies.
- QA at 1440×900 / 1200×800 / 900×900 / 390×844: correct order/variants, no wrapping/overflow, 52.5px controls, visible keyboard focus and preserved document/section dimensions. Request Service remains `#` because no destination page exists. Fixed orange text contrast remains an approval item.
- Added [milestone](docs/milestones/2026-10-16-homepage-cta-strategy.md), sanitized evidence and post-change screenshots; updated context, map and decision register. No production or unrelated layout change.

## 2026-10-16 — Homepage vertical layout and scroll audit

- Completed read-only audit of all nine Homepage sections at the four exact requested viewport sizes. Authenticated document heights: 6167 / 6167 / 7307 / 10413px; measured Header/Footer, section positions/heights, padding/gaps, CTA/Core visibility and viewport-length counts.
- Saved [audit](docs/audits/2026-10-16-homepage-vertical-layout.md), sanitized measurements and actual pre-CTA full-page desktop/mobile screenshots with section crops. Distinguished measured geometry from estimated savings and authenticated assets from untested public performance.
- Recorded selective boundary/card/Final-frame recommendations, Emergency desktop/tablet gutter defect and pending proof/destination issues. Reviewed actual tree, class CSS and dependencies without deleting or modifying anything.
- Owner subsequently authorized the separate CTA change above. Other audit proposals remain pending approval; no spacing/media/global-style recommendations were implemented.

## 2026-10-16 — Permanent implementation reporting standard

- Updated AGENTS and WORKFLOWS for all future GCPRO agents: exact final headings Implementation Summary, Technical Changes, Complexity Audit, Verification, GitHub and Outstanding Items.
- Required individual inventories of every new class, variable, Component, custom code file, plugin and external dependency, with purpose, demonstrated gap, reuse scope and edit location; explicit no-additions statements when applicable.
- Added a native-first addition gate and a mandatory review/removal of unjustified task-introduced complexity before completion. Speculative abstractions and undocumented styling are prohibited.
- Preserved required commit/push/remote verification and added documentation-only applicability so the reporting template never authorizes website changes or invented runtime QA.
- Updated PROJECT_CONTEXT to make the permanent standard discoverable. Verification covers requirement consistency, document links, diff/whitespace, intended files and actual Git delivery. No WordPress, Elementor, production, application code or shared ROBYLO changes.

## 2026-10-16 — ZIP prototype and owner-requested Homepage refinements

- Refined the existing Service Areas section of Homepage 154 into information/city links plus a native ZIP Checker panel, with a visible future-feature notice and a real disabled submit button. No ZIP validation, results, API or custom backend was added.
- Preserved all eight city links and the directory destination. Added seven reusable native form classes; removed converter-generated custom CSS rather than keeping a styling workaround.
- Applied the owner's follow-up: smaller Montserrat step numbers in Component 65 (24px desktop/tablet, 22px mobile), preserving the existing number/icon visibility rule and four numbered instances. Added process-step-number with priority above card-icon.
- Applied the audience-card reference to the two existing Residential/Commercial wrappers: 16:9 placeholders, bordered rounded white cards, native heading/description and circular navy actions with SVG 464. Added four shared card classes. Six core Component 62 instances are unchanged.
- Final H1–H6 defaults match the initial state: uppercase only H1/H2, capitalize H3/H4, none H5/H6. Header 113, Footer 114, other Homepage section trees, production and shared ROBYLO remain unchanged.
- QA: actual 1440/1200/900/390px rendering, no horizontal overflow, native edit controls, associated label/input, disabled button, Enter without ZIP submission/results, real arrow SVGs and process numbers without visible checkmarks. No new CSS/PHP/JavaScript, plugin or theme code remains.
- Limitations: Atomic Input requires Form and hidden native status slots. Clearing all form actions reverts to default Email after reopen; keep the button disabled. Built-in WebMCP form exposure is native, not a lookup API. Full backup/restore, physical touch and production migration were not tested. Detailed evidence and rollback: [milestone](docs/milestones/2026-10-16-zip-and-homepage-refinements.md).

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
