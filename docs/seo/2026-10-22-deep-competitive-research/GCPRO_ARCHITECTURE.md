# GCPRO architecture: preserve the build, clarify ownership

## Verified current structure and reuse

Repository architecture is Elementor Atomic V4 on ROBYLO Starter. Current browser reads confirm Home 154 `/`, Residential 484 `/residential-services/` and Commercial 499 `/commercial-services/` and their H1s. Header113/Footer114, Why1149, Process1152→timeline582, Areas1140, CTA80, service card62, image/text77, FAQ83 and heading71 already provide reusable building blocks. Use native object links and existing classes/variables. Shared code590/847/903 already exists; this analysis adds none.

The two audience hubs have completed nine-section builds. Child IDs are an existing inventory, not permission to publish or proof that their content is complete. Homepage and hub projects are a starting source of real proof; a gallery photograph alone is not a documented case study.

| Intent / audience | Current exact route and ID | Recommended owner / next action | Reason and constraint |
|---|---|---|---|
| Company/general/emergency | `/` 154 | Keep company intent; improve specialist summaries and contextual links | SERPs show company homepages serving multiple broad service queries; no separate generic “restoration company Chicago” clone |
| Homeowner selection | `/residential-services/` 484 | Preserve hub and six child routes; improve decisions/proof | Navigation/conversion role is useful independently of a measurable exact keyword |
| Business selection | `/commercial-services/` 499 | Preserve hub; distinct access, contacts, documentation, continuity content | ATI/Paul commercial examples; local exact volume is limited |
| Generic water / homeowner workflow | `/residential-services/water-damage/` 514 | Preferred first-phase generic water owner on existing route, pending approval | Complete task and link from both relevant hubs; nested path is not a reason to duplicate |
| Commercial water | `/commercial-services/water-damage/` 515 | Separate business workflow; scope to premises/tenant coordination and documented process | ServiceMaster commercial-water performance and Paul business page; no copied generic body |
| Generic fire/smoke | `/residential-services/fire-smoke/` 517 | First-phase fire/smoke owner | Romexterra fire cleanup / ATI service evidence; include odor/contents/rebuild handoffs |
| Commercial fire | `/commercial-services/fire-smoke/` 520 | Hold extensive SEO build until unique operational content and demand joins | Existing route preserved; summary hub links can remain without six duplicated briefs |
| Generic mold | `/residential-services/mold-removal/` 516 | First-phase mold-remediation owner; explain inspection/remediation scope accurately | Romexterra and specialist results; keyword differs from existing slug without requiring URL change |
| Commercial mold | `/commercial-services/mold-removal/` 519 | Build only with facility containment/access/verification facts | BluSky/EHC/Enviro commercial-oriented evidence; health/safety claims require review |
| Reconstruction | Residential 518, Commercial 524 | 518 loss-reconstruction owner; 524 B2B conditional | “Reconstruction services” SERP is mixed with remodeling/foundation; exclude medical intent and unrelated repairs |
| Storm | `/residential-services/storm-damage/` 523 | Improve existing storm owner after core water/fire/mold | Distinguish weather stabilization/repair from roofing-only promises |
| Contents | Residential 521; Commercial 525 | 521 candidate shared contents owner; 525 needs differentiated business/document workflow or stays support | Packout/storage process must be real. No merge/redirect inferred |
| General contracting | Commercial 522 | Retain separate business scope if actually offered | Do not make it a duplicate generic reconstruction keyword owner |
| Extraction / drying | `/water-extraction/` 487; `/dehumidification/` 491 | Extraction task page links to full water owner; drying initially a section/supporting page | Different immediate task, no new pages for every equipment synonym |
| Stabilization / odor / diagnostics | `/board-up/` 488; `/odor-removal/` 489; `/moisture-mapping/` 490 | Retain distinct tasks; scope, cross-link, proof | Restore emergency board-up; CWF moisture article demonstrate adjacent demand, not automatic new URLs |
| Local coverage | `/service-area/` 495 and 51 city objects | Pilot one existing Glenview object after exact URL/ID inventory check; consider Lombard next | Existing real Glenview water project and genuine Lombard establishment; no invented Glenview office |
| Evidence | `/before-and-after/` 493; `/portfolio/` 1132 | Gallery→documented project entries; avoid parallel duplicate gallery structures | Two complete cases first, using actual records and consent |
| Contact/conversion | `/service-request/` 492 and existing contact route | Define functional request workflow before sending new traffic | Current structural page is not a verified working lead form |

## Recommended relationships, without URL migration

Home → Residential/Commercial selection hubs and primary Water/Fire/Mold/Storm/Reconstruction/Contents owners. Each hub → relevant existing service object. Generic owner → audience-specific workflow where one exists, relevant diagnostic/stabilization page, documented project, coverage hub and request page. Case → the service actually performed and the genuine city page. City → broad relevant services and local case, not all six cloned city×service children. Helpful article → one appropriate service and the immediate next step.

Use existing Atomic components for consistent visual sections, but write page-specific evidence and task content. A reused FAQ layout does not justify identical FAQs on every service/city page. Keep a link register of source object→target object to prevent hardcoded staging URLs and migration drift.

## Changes needing separate evidence or approval

Six new root service paths, moving existing children, merging Residential/Commercial siblings, deleting city pages, redirects, canonicals, indexability and production schema remain unapproved. Before a migration: export exact URL inventory; query-specific GSC joins; page backlinks; current status/canonical/indexing; planned equivalent content; redirect map; internal-link updates; rollback and post-launch tracking. The first 30 days intentionally do not depend on that migration.

No new plugin, JavaScript framework, SEO widget pack, custom CSS system or duplicated component library is needed for the recommended content work. FAQ structured data eligibility is not guaranteed by adding questions; native SEO output must be checked against actual page content after implementation approval.
