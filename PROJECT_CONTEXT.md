# GCPRO project context

Last reviewed: 2026-10-16 (America/Chicago). Current milestone: SEO URL architecture and partial Draft page skeleton (E12). Earlier implementation records below remain dated history.

## Current architecture and partial skeleton — E12

[SEO_STRUCTURE](docs/SEO_STRUCTURE.md) and the single canonical [URL inventory](docs/SEO_URL_INVENTORY.csv) reconcile the authoritative audit/build plan with current public production objects/HTML and native staging reads. There are 207 URL rows: 200 audited, two unapproved proposals and five current-only review items. Original actions remain unchanged; UPDATE is normalized to KEEP only in the additional migration-decision column. No new search metrics or revised SEO decisions were invented.

Created **15 blank root Draft Pages**, verified exact slugs/parent 0 after native Quick Edit save and reload: Residential 484, Commercial 499, Apply 486, Water extraction 487, Board Up 488, Odor Removal 489, Moisture mapping 490, Dehumidification 491, Service Request 492, Before And After 493, Copyright 494, Service Area 495, Contact 496, About 497, Testimonials 498. Reused Homepage 154 and existing Privacy Policy 3; its generic body is not migrated content. Total staging Pages: **21 (3 published, 18 Draft)**. No new visual templates or content were built.

**Incomplete:** 64 retained nested Pages are not created. WordPress Quick Edit and Gutenberg Parent selectors exclude Draft parents, while the exposed create-page MCP lacks native slug/parent fields. Need a supported authenticated native Page create/update capability exposing `slug` and `parent`; do not publish parents or create flat substitutes. CSV records real hub IDs and intended parent paths, with blank child IDs. First planned template: Residential Water Damage; unblocked alternative: Water Extraction 487.

Mapped 30 retained archives/taxonomies (12 tags, 16 dates, Blog and Portfolio), 29 posts and 13 portfolio CPT items without manufacturing Pages. Staging exposes no portfolio CPT, no tags and only Uncategorized 1. Blog/Portfolio production routes are actual archives despite public REST Page records. `/team/` is a retained audit URL but currently 404/no Page; five current-only sources and two proposals require review. Zero detected new slug collisions; eight source/approval holds are distinct from the 64 technical parent holds. All nine layout families remain mapped, not built.

No link implementation occurred; it belongs to the separate linking task. **Service Request 492 and Contact 496 now exist only as Drafts**; previous missing-page reports below are historical. Existing `#` dependencies must stay explicit until destinations become public. The shared menu still has 32 Custom Link placeholders; the Header logo retains its existing Internal URL reference to 154. The canonical CSV contains destination dependencies and source internal-link/media relationships.

Before/after Reading Settings: search-engine discouragement checked, Homepage 154, posts-page 0. Anonymous staging root has `noindex, nofollow`; robots.txt is not a site-wide crawl block. Homepage 154/Header 113/Footer 114 full saved trees match before/after. All new Draft element arrays are empty; production received public GET requests only. No layout/style/navigation/permalink change, new classes, Variables, Components, custom code, plugins or dependencies. No responsive test replay is claimed for unchanged layouts. Local scoped snapshots exist; full database/files backup/restore remains unverified. Detailed counts, IDs, blocker evidence, source hash, migration checklist and recovery boundaries are in SEO_STRUCTURE.

Permanent workflow update, 2026-10-16: every AI agent must automatically use the six-section final reporting standard in [AGENTS](AGENTS.md#mandatory-implementation-reporting-standard) and [WORKFLOWS](docs/WORKFLOWS.md#mandatory-final-implementation-report). Every new technical element needs an individual purpose/gap/reuse/edit-location inventory; a pre-completion complexity audit is mandatory. Minor reports stay concise without omitting additions or custom code. This update changes documentation only; no WordPress/Elementor or shared ROBYLO modification is authorized or performed.

## Current implementation and audit — E9 / E10

Permanent linking rule added 2026-10-16: use native WordPress objects / Elementor Internal URL or equivalent selectors, preserve independent Component destination overrides, and record missing/manual exceptions plus migration checks. See [AGENTS](AGENTS.md#mandatory-native-internal-linking-and-url-integrity) and [verified method/limits](docs/WORKFLOWS.md#atomic-v4-method-verified-on-this-installation--e11). E11 confirms schema support; dynamic object-bound instance save/render independence and migration remapping remain untested. This documentation update changes no website links.

Homepage 154 Hero and Final CTA use orange Call first (`tel:+18476563322`) and white-outline Request Service second (`#`). Existing Components 53/103 and the instance overrides of 80 were reused; only eight text/link leaf values changed in E10. Header 113, Footer 114, shared definitions, styling, layout and other sections were unchanged. At E10 Request Service did not exist in the then-six-page inventory; E12 created Draft 492, but the public destination and existing orange/white contrast issue remain unresolved. No new classes, variables, components, code or dependencies. See [CTA milestone](docs/milestones/2026-10-16-homepage-cta-strategy.md) for actual four-width, keyboard and saved-state verification.

The preceding [vertical-layout audit](docs/audits/2026-10-16-homepage-vertical-layout.md) measures all nine sections at 1440×900, 1200×800, 900×900 and 390×844. Document heights are 6167 / 6167 / 7307 / 10413px in the authenticated session; CTA-only edits preserve these values. Selective spacing, Emergency gutter and proof-content recommendations remain **unimplemented**, pending approval. Do not interpret CTA implementation authorization as approval for those layout changes. Audit screenshots show the pre-CTA baseline; CTA milestone screenshots show the updated buttons.

## Previous implementation — E8

Homepage 154 now has a native ZIP input and disabled Check Area button within the existing Service Areas section. City links and their destinations are preserved, with information on the left and a minimal panel on the right. This is an inactive visual prototype: no coverage lookup, validation, API or custom backend was implemented.

During the same work the owner requested smaller Montserrat process numbers and a new Residential/Commercial card treatment. Component 65 numbers use 24px desktop/tablet and 22px mobile; existing number/icon visibility behavior is preserved. The two audience cards retain their original wrappers, 16:9 placeholders and destinations, with native editable copy and real SVG arrows. Six core-service instances still use Component 62; the former two audience instances were replaced only in this authorized section. Header 113 and Footer 114 remain unchanged.

Final heading policy: H1–H2 uppercase, H3–H4 capitalize, H5–H6 none. All six defaults match the pre-task values; the temporary all-uppercase change was reversed following owner correction. No heading text or other typography values were changed.

There are now 83 Global Classes (71 previous + 12 role-based additions) and the same 36 variables. See [milestone](docs/milestones/2026-10-16-zip-and-homepage-refinements.md), [design system](docs/DESIGN_SYSTEM.md#zip-ui-and-homepage-refinements--e8) and [map](docs/ELEMENTOR_MAP.md#zip-ui-and-audience-card-locators--e8).

Actual frontend QA covered 1440/1200/900/390px, native input editing and disabled submission behavior. Visual owner approval remains pending. Atomic Input requires an Atomic Form ancestor; its default Email action reappears after saving an empty action list. Keep the submit button disabled. No recipient, lookup or external service was configured. The native form also advertises its built-in WebMCP submission tool; it was not invoked. Do not treat this prototype as a form/backend integration or enable it before the next functional implementation review.

E8 sources: current staging MCP schemas and before/after structure/default reads, actual Elementor editor controls and screenshots, browser DOM/computed styles and a network-observed Enter test on 2026-10-16. Sanitized findings: [evidence](docs/evidence/2026-10-16-zip-and-homepage-refinements.json). Local snapshots complement recovery; a full database/files restore remains unverified. Production and shared ROBYLO were not changed.

## Start and ownership

GCPRO Restoration uses WordPress and Elementor Atomic V4 according to the initial README. [GCPRO repository](https://github.com/vvvetalll/gcpro-website) holds client-specific documentation; [ROBYLO](https://github.com/vvvetalll/robylo-website-starter) supplies the shared theme foundation. Staging: https://vitaliiv1.sg-host.com. Production is outside the permitted editing scope.

Read [AGENTS.md](AGENTS.md) for permanent rules and [WORKFLOWS.md](docs/WORKFLOWS.md) for editing, backups, documentation, and handoff.

## Current verified baseline

- Before this milestone, GCPRO main contained only README.md at commit [6162450](https://github.com/vvvetalll/gcpro-website/commit/61624508705fe9d7947d145e3cc9ef973421fb3d). No application source, build configuration, deployment pipeline, or WordPress backup was present in that tree (E1).
- Read-only staging page inventory returned six pages. Homepage 154 is published and resolves to the staging root; the validation page 50 and page 7 are drafts (E3). See [ELEMENTOR_MAP](docs/ELEMENTOR_MAP.md) for the complete inventory.
- Fifteen reusable Components were returned. Header 113 and Footer 114 were returned as published and active with site-wide conditions. Four other Theme Builder templates are published with conditions but returned inactive (E3); this is not a failed-template diagnosis.
- The active kit resource returned 36 variables and 71 class labels, captured in [DESIGN_SYSTEM](docs/DESIGN_SYSTEM.md). Class CSS and tag defaults were not comprehensively audited.
- Live Homepage structure includes Hero, two audience paths, six core service cards, emergency response, four process steps, three project wireframes, benefits/testimonials, eight city links, and final CTA (E3).
- Documentation initialization added the eight handoff documents at [701e70c](https://github.com/vvvetalll/gcpro-website/commit/701e70cbc6b831ff929d296048e79dc89e655454). The integration milestone now reconciles the [Homepage V2 record](docs/milestones/2026-10-16-homepage-v2.md) against fresh saved-state reads (E6) and inspected historical QA artifacts (E7). Neither documentation milestone modifies WordPress, production or shared ROBYLO.
- Fresh full reads of Homepage 154, Components 62/65/68/80/86/286, Header 113 and Footer 114 match the prior final-state artifact for all nine documents. Eight Component 62 instances and their individual saved SVG/content/link values are present; the extra `43e3093` is absent. These are saved-configuration checks, not a new frontend/editor test.
- Every completed GCPRO development milestone now requires relevant documentation changes plus a commit, push and remote verification. Read [WORKFLOWS](docs/WORKFLOWS.md); if write access fails, report the exact restriction and leave documentation synchronization pending.

## Reported implementation and open issues

The earlier Homepage V2 completion report (E4) states that Service Card 62 was restored with independent SVG overrides; Homepage 154, Header 113, and shared components were refined; responsive checks at 1440/1200/900/390 px and actual Elementor controls were checked; Footer and production were unchanged; and no new custom CSS/PHP/JavaScript was added in that milestone. These are attributed historical outcomes, not tests repeated in this task.

E4 also reports existing legacy navigation rules, so do not generalize its no-new-code statement to a site-wide absence of custom code. The older component JSON (E5) has outdated names/structures and limitations; current live inventory wins for identity, while implementation behavior still needs testing.

The reconciliation inspected the actual E7 test records: all four recorded viewports have one H1, eight service cards and no horizontal overflow; the controlled SVG test changes only Water Damage; the latest recorded eyebrow has 12/11px text, an 8px gap and no underline. Fresh E6 reads corroborate the stored component/page definitions, including the informational DIV root of Component 286. Historical visual/editor outcomes remain dated to their implementation run. Owner visual approval is still pending, and no new runtime QA was run in this documentation task.

| Priority | Outstanding work | Evidence/status |
| --- | --- | --- |
| Next | Review Homepage V2 visually with the owner | Earlier report stopped for visual approval; approval not established here |
| Next | Complete native object architecture, then connect published destinations in the separate linking task | E12 created Contact 496/Service Request 492 as Drafts only; 64 nested Pages await parent capability; see SEO_STRUCTURE |
| Next | Resolve orange CTA text contrast | E4 reports white on #F05A29 at about 3.39:1; retest actual text/states before selecting an editable fix |
| Next | Supply approved photographs, attributable reviews, credentials, and final copy | E4 reports placeholders; do not publish invented business claims |
| Before further implementation | Record installed WordPress/PHP/Hello/ROBYLO/Elementor/Pro/connector versions, active theme and license/Atomic settings | Not established by repository source or inventory |
| Before further implementation | Verify recoverable database + files backup and restore process | No backup or restore test confirmed |
| Before transfer | Validate Elementor export/import and ID remapping on an isolated target | No portable package or tested transfer process established |
| Before completion of affected work | Recheck editor controls, override independence, frontend, keyboard and responsive behavior; audit existing customizations | Earlier checks do not establish future/current behavior |

No production migration, SEO redirects, launch, or deployment is authorized by this documentation milestone.

## Evidence register

Use these labels throughout the documentation. Observed facts are limited to the specified read; sources can become stale.

| Ref | Source and date | What it establishes / limits |
| --- | --- | --- |
| E12 | Authoritative workbook/build register read; dated public production REST/HTML; native WordPress Pages/Quick Edit/Parent/Reading/menu UI and staging public types/taxonomies; MCP create/re-read and full 154/113/114 before/after reads, 2026-10-16 | [207-row inventory](docs/SEO_URL_INVENTORY.csv), [architecture and exact outcomes](docs/SEO_STRUCTURE.md): 15 new root Drafts, 2 reused objects, 64 children blocked by Draft-parent controls; preserved layouts/noindex. No production writes, publishing, redirect execution, link implementation, visual templates, responsive replay or full backup/restore verification. |
| E11 | Read-only staging host/Widget/Component discovery, `elementor://dynamic-tags`, e-button and 53/62/80/103 schemas, plus Hero Actions saved read on 2026-10-16 | Internal URL/object-selector link contract and exposed Component destinations; current Hero static tel/# values. No dynamic binding writes, two-instance dynamic runtime test, site-wide conversion or migrated-site test |
| E9 | Read-only IAB frontend/editor, saved Homepage structure and global inventories on 2026-10-16; [audit](docs/audits/2026-10-16-homepage-vertical-layout.md), [measurements](docs/evidence/2026-10-16-homepage-vertical-layout.json) | Actual four-size vertical layout, pre-CTA screenshots, scoped architecture findings and clearly estimated proposals; authenticated session, not anonymous performance or approval to implement spacing changes |
| E10 | Owner-authorized native CTA edits, fresh MCP before/after comparison and IAB frontend/keyboard QA on 2026-10-16; [milestone](docs/milestones/2026-10-16-homepage-cta-strategy.md), [evidence](docs/evidence/2026-10-16-homepage-cta-strategy.json) | Eight Hero/Final instance text/link changes, published staging output, unchanged Header/Footer and geometry; no real Request Service route, actual call, touch/screen-reader or performance test |
| E1 | GCPRO main tree, initial README and commit history read on 2026-10-16; pinned [README](https://github.com/vvvetalll/gcpro-website/blob/61624508705fe9d7947d145e3cc9ef973421fb3d/README.md) | Repository baseline and declared stack; not runtime installation |
| E2 | ROBYLO source reviewed read-only at [8e1397a](https://github.com/vvvetalll/robylo-website-starter/tree/8e1397aab99ab5965c10a251cf144ea3ba3a0372): README, AI-CONTEXT, AGENTS, docs/setup, docs/elementor, theme PHP/CSS | Shared source architecture; not proof of deployment to GCPRO |
| E3 | Read-only Elementor MCP on 2026-10-16: list-posts (page, 25; total 6, returned URLs match staging), list-components, schemas for 62/80/286, list-site-parts, get-page-structure(154), discovered global-variables/global-classes resources | Saved inventories, exposed override keys, token values and structural labels; no writes, frontend/editor QA or version audit |
| E4 | Prior chat **Audit GCPRO SEO migration**, ID `01a140c7-2f6a-79e2-a465-bcab1d96262c`, turn `01a14519-52af-7a32-af57-5bf01b8f7328`; local `outputs/homepage-v2-implementation-2026-10-16/completion-report.html`, `final-state.json`, `final-responsive-qa.json` reviewed | Historical implementation report and local artifacts; not a newly reproduced runtime test |
| E5 | Prior workspace `robylo-atomic-components.json`, read 2026-10-16; declares the same staging host | Older reported component IDs/validation; several names and schemas superseded by E3 |
| E6 | Read-only staging MCP during repository integration, 2026-10-16: Homepage lookup, full content reads of 154/62/65/68/80/86/286/113/114, Style Guide library root, global resources and H1-H6 defaults | Nine document trees match the prior final snapshot; eight saved service-card overrides, absence of the extra card, two Style Guide cards, zero returned local-style entries, 36 variables, 71 classes and current HTML defaults. No frontend/editor/interaction test or full class-CSS audit was repeated. Sanitized results: [evidence](docs/evidence/2026-10-16-homepage-v2-reconciliation.json) |
| E7 | Historical local `final-state.json`, `final-responsive-qa.json`, `svg-override-test.json`, `final-performance.json` and implementation report inspected during integration | Dated QA/performance evidence, not current replay. Source-file SHA-256 hashes and limitations are recorded in the [milestone](docs/milestones/2026-10-16-homepage-v2.md); raw snapshots, network traces and private backups are not published |
| E8 | Authorized staging implementation on 2026-10-16: MCP schemas/snapshots/defaults, native editor controls, SVG import, four-width frontend screenshots and Enter/network test | ZIP prototype, process-number and audience-card changes; actual results and native Form limitations in the [milestone](docs/milestones/2026-10-16-zip-and-homepage-refinements.md) and sanitized [evidence](docs/evidence/2026-10-16-zip-and-homepage-refinements.json). No production or lookup/backend activation. |

E4/E5 artifacts reside in the earlier chat workspace, not in this repository; relative artifact paths above identify their original location and are not repository links. The relevant findings are summarized here. Review and sanitize any future evidence exports before committing them. No credentials or full site/database export is included.

The public staging URL could not be retrieved by the web reader in this task. Read-only MCP succeeded; this is not evidence of a staging outage.

## Next handoff

1. Read this context, the map and design system; reconfirm target and versions.
2. Resolve owner review and the authorized next scope.
3. Verify backup and affected current state before any writes.
4. Implement through native Elementor controls, test affected consumers and editor controls.
5. Update all affected documentation, commit, push and verify the remote branch before handing off completion. Report the canonical commit URL. If access is missing, explicitly keep documentation synchronization pending.

The containing Git commit is the documentation milestone reference. Use Git history and the verified remote head for its SHA; do not substitute a guessed commit URL.
