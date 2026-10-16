# GCPRO project context

Last reviewed: 2026-10-16 (America/Chicago). Current milestone: Service Areas ZIP UI, process-number refinement and reference-based audience cards on staging Homepage 154. See the current implementation record below; earlier baseline observations remain dated history.

## Current implementation — E8

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
| Next | Replace missing navigation/service/request/project/city destinations and audit all links | E4 reports many `#` destinations; live inventory has no Contact or Service Request page |
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
