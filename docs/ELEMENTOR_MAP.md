# GCPRO Elementor map

## Homepage process timeline — E15, 2026-10-16

Homepage154 section `4681b8f5` / container `4a8f9eb5` / heading71 instance `5494e63e` preserved. Retained Process Steps `5a7e87b2` now uses existing layout-reset and one instance `79a67ca3` of new **ROBYLO / Process Timeline582** (UID `component-05873ba5-60ba-44ec-9fed-ffb25ced3f75`, root `16ae2220`). Twelve supported overrides are grouped Step1–4: `step_N_number`, `step_N_title`, `step_N_description`. Use instance Content controls without detaching; shared layout uses four documented native Global Classes.

Only the four previous Feature65 process instances were replaced. Shared Feature65, Why GCPRO usages, Header113/Footer114 and eight other Homepage sections compare exactly equal on fresh saved reads. Titles Contact/Assessment/Restoration/Review and descriptions unchanged. [Implementation/editing/verification/recovery](milestones/2026-10-16-process-timeline.md); whole-step hover now uses the approved scoped external exception and existing native transition. Direct [component editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=582&action=elementor); verified in-context Edit Component path from Homepage154. No service-page instances, SEO object or URL changes.

Environment: https://vitaliiv1.sg-host.com. Last read: 2026-10-16. IDs are installation-specific and must be rechecked before writes. Sources E3–E5 are defined in [PROJECT_CONTEXT](../PROJECT_CONTEXT.md#evidence-register).

**Verified** below means returned by the indicated read-only MCP inventory/schema/structure in this task. It does not mean the document is visually approved, every instance was tested, or frontend/editor behavior was verified. **Reported** means an earlier chat/artifact claim not fully repeated here.

## Current completed native Page skeleton — E14

2026-10-16 native REST and browser reads confirm **85 Pages: 3 published, 82 Draft**, after creating **64 child Drafts, IDs 514–577**. All 81 verified retained Page destinations now have actual object IDs: 79 new Drafts across E12/E14 plus existing Homepage154 and Privacy3. See the single [canonical inventory](SEO_URL_INVENTORY.csv) for every exact path/ID; [SEO_STRUCTURE](SEO_STRUCTURE.md#completed-hierarchical-drafts--e14) provides grouped mappings and validation limits.

| Parent | New child count | Representative children |
| --- | ---: | --- |
| Residential484 | 6 | Water Damage514; Fire & Smoke517 |
| Commercial499 | 6 | Water Damage515; Fire & Smoke520 |
| Service Area495 | 51 | Lombard526; Downers Grove527 |
| About497 | 1 | Careers534 |

Native authenticated WordPress REST, using existing same-host configured Basic authorization, accepted Draft parents with exact slug/status. No native Page existed for these 64 paths in the initial 21-object read; independent post-save and final reads verified all64 exact paths, Draft status, empty content and no duplicates. Native editor514 displayed its correct Draft/slug/Parent and standard Edit with Elementor entry. No Elementor layout was created for these native shells. Future design uses normal Elementor editing; no custom framework or metadata injection is required.

**Distinct objects:** Water Extraction487 → `/water-extraction/`, parent0, Supporting service; Residential Water Damage514 → `/residential-services/water-damage/`, parent484; Commercial Water Damage515 → `/commercial-services/water-damage/`, parent499. Recommended first internal layout is 514, not487. All remain Draft and are not working public navigation destinations.

All21 existing native Page fields/settings, full saved154/113/114 trees, Classes/Variables resources and Component registry are unchanged. No new Component/class/Variable/code/plugin or link edit. Eight unresolved URL decisions remain uncreated. Preserve E13 archive observations below and commit `6b53d20`: no duplicate Blog/Portfolio Page, no production template/condition changes and no historical PHP reproduction. Blog query type, title hooks and active-state/conditions/source locations remain future archive-phase work. [E14 evidence](evidence/2026-10-16-completed-page-skeleton.json).

## Historical initial Draft skeleton — E12

The following 21-object baseline and parent-interface blocker are superseded by E14; the earlier 15 root IDs remain valid.

At E12 on 2026-10-16 native WordPress/MCP reads returned **21 Pages: 3 published and 18 Draft**. The original six remained; 15 new blank root Drafts were added. [SEO_STRUCTURE](SEO_STRUCTURE.md#created-root-drafts-and-verified-paths) lists every actual root ID/path/family; [SEO_URL_INVENTORY.csv](SEO_URL_INVENTORY.csv) is the authoritative per-URL register. All 15 root IDs were re-read after saving exact native slugs and parent 0; MCP returned empty Elementor arrays. Native page template was Default; no family layout was built or assigned.

Actual IDs: Residential 484, Commercial 499, Apply 486, Water extraction 487, Board Up 488, Odor Removal 489, Moisture mapping 490, Dehumidification 491, Service Request 492, Before And After 493, Copyright 494, Service Area 495, Contact 496, About 497, Testimonials 498. Existing Privacy Policy 3 retains `privacy-policy`, parent 0 and Draft. These are future paths, not public navigation destinations. Homepage 154 stays published/front page; full saved Homepage/Header113/Footer114 trees match pre-task reads.

At E12, 64 nested retained Pages were uncreated because of the exposed parent controls; E14 has now created them through authenticated native REST and recorded real IDs. Posts29, Portfolio CPT13 and archive/index/taxonomy30 remain separately mapped, not fabricated Pages. Staging public types do not expose Portfolio. No Component, class, Variable or template change occurred in either skeleton milestone.

## Production archive observations — E13, read only

These are **production IDs**, verified in served HTML and the actual IAB DOM on 2026-10-16, not staging documents to edit or copy:

| Production route / sample | Rendered template/object | Meaning / limitation |
| --- | --- | --- |
| `/blog/` | Elementor Archive **6858**, public Page **2187** | Current `blog` body class and Page-based menu item 2905 support a posts-index interpretation; January category routing is owner-reported history, not current proof. Native Reading/query configuration is unverified. |
| `/portfolio/` | Elementor Archive **8412**, CPT `portfolio`, `has_archive=true` | Actual CPT archive confirmed, despite a separate public REST Page 8929; no duplicate staging Page. |
| Article `/signs-of-hidden-water-damage-in-your-home/` | Post **21140**, Single Post template **5897** | One sampled post, not all article-template coverage. |
| Project `/portfolio/reconstruction-after-water-damage-on-montana-street-chicago/` | Portfolio item **10625**, template **7996** | Body `single-portfolio`; rendered template type says `single-post`, so do not infer stored display conditions from its label. |
| Shared rendered shell on those routes | Header **21168**, Footer **21217** | Production IDs, unrelated to staging 113/114. |

Production admin redirects to login; settings REST and the targeted template-library read both return 401. Exact Theme Builder Display Conditions, Reading Settings, production PHP paths and active hook source were **not available**. Assets identify only theme directory `wp-content/themes/custom-dev-theme-elementor-master/`; this is not proof of any `functions.php` implementation. Owner reports historical `is_category('blog')` title/meta logic and `nav_menu_css_class`; do not copy these blindly or claim their current code location is known.

Current Header active markers are present on the Blog archive/Showcase parent on Portfolio, but absent on the sampled single post/project. Footer single views show extra current-item LI classes without corresponding active anchor classes/aria-current. Reproduce the intended parent navigation behavior natively and test archive/pagination/singles in the later archive phase; do not assume current custom behavior is consistently correct.

See [historical/current comparison and required migration behavior](SEO_STRUCTURE.md#blogportfolio-historical-php-and-current-routing-follow-up--e13), [sanitized public evidence](evidence/2026-10-16-archive-routing.json) and the two updated rows in the existing canonical CSV. No website, object, PHP or display condition was changed in E13.

## Historical six-page inventory — E3

Source: `list-posts`, page type, 25 per page, total six returned; their URLs match the designated staging host. Status is WordPress's returned state. Titles are preserved, even when the report uses a newer milestone name.

| Post ID | Returned title | Status | Location |
| --- | --- | --- | --- |
| 50 | ROBYLO — Atomic Foundation Validation (Temporary Draft) | draft | [Edit 50](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=50&action=elementor) |
| 154 | GCPRO Homepage — Phase 1 Atomic Wireframe | publish | [Edit 154](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=154&action=elementor) |
| 7 | Elementor #7 | draft | [Edit 7](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=7&action=elementor) |
| 12 | GCPRO — Coming Soon | publish | [Edit 12](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=12&action=elementor) |
| 3 | Privacy Policy | draft | [Edit 3](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=3&action=elementor) |
| 2 | Sample Page | publish | [Edit 2](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=2&action=elementor) |

Homepage 154 returned the staging root as its URL. The other published non-root pages are Coming Soon 12 and Sample Page 2. A published state is not launch approval. Page 50 is historically used for validation/Style Guide work, but its returned title and draft status above are authoritative for this inventory.

## Verified reusable Component identities

Source: `list-components` discovery; fifteen returned non-archived entries. Current capabilities returned `can_create=true`, `can_edit=true`, `can_add_to_page=true`. These are capability flags, not authorization or proof a write succeeds. UID is included to disambiguate identity; neither numeric IDs nor UIDs are proven portable.

| Component ID | Returned name | UID |
| --- | --- | --- |
| 286 | ROBYLO / Emergency Service Mark | `component-dfdb0e08-1a53-43c1-bde9-fa31f0beeb55` |
| 103 | ROBYLO / Button / Outline White | `component-9e3d299e-89f8-4484-9760-f482541d98b1` |
| 100 | ROBYLO / Button / Outline Orange | `component-ed18ed61-03d5-404d-9a97-561404cb1f6b` |
| 86 | ROBYLO / Testimonial Card | `component-f5ecac7b-b6be-427f-b1b9-448885252dab` |
| 83 | ROBYLO / FAQ Group | `component-48fec5e6-0cc8-454c-a7ab-406a2b516bec` |
| 77 | ROBYLO / Image + Text Section | `component-b66e71a0-22c6-43dc-9f1b-9c5c73df7abc` |
| 80 | ROBYLO / CTA Section | `component-02310d3c-933a-484b-9978-d9ad96274eca` |
| 74 | ROBYLO / Hero | `component-de6a4e56-5ca8-43ff-aa72-ef03aafc2c81` |
| 68 | ROBYLO / Interactive Card | `component-4da4b304-cf49-4cb4-85f0-ae8a96f5fb43` |
| 71 | ROBYLO / Section Heading | `component-9bb099ec-804d-4618-a599-5b7e321d2e9d` |
| 65 | ROBYLO / Feature Card | `component-d84d7370-a5fc-477a-9e2d-78ac1238dc13` |
| 62 | ROBYLO / Service Card | `component-ef3a2a49-e07b-44bb-8d5c-e4335142d946` |
| 56 | ROBYLO / Button / Secondary Blue | `component-95811d48-98e9-481d-b56d-2ff397eaa583` |
| 59 | ROBYLO / Button / Outline Blue | `component-2ae9e4bb-f521-425d-a612-2d23e67a42a2` |
| 53 | ROBYLO / Button / Primary CTA | `component-a16fd4f6-ec5f-4a1c-b43e-c5a2f7cb18cc` |

Open a component via the staging editor with its numeric post ID. Key entries: [Edit 62](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=62&action=elementor) (Service Card), [Edit 80](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=80&action=elementor) (CTA), [Edit 286](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=286&action=elementor) (Emergency Service Mark).

### Verified exposed override keys

Source: schema reads for 62, 80 and 286 only. All three returned `is_archived=false`. Values must match the current returned schema; do not infer new override keys from a label.

| Component | Override keys (current labels) |
| --- | --- |
| 62 | `icon` (SVG Icon); `title` (Title); `description` (Description); `cta_text` (Link Label); `cta_link` (Link Destination) |
| 80 | `title` (Title); `description` (Description); `cta_text` (Primary Label); `cta_link` (Primary Link); `secondary_text` (Secondary Label); `secondary_link` (Secondary Link) |
| 286 | `label` (Eyebrow Text) |

Existence of these fields is verified. Independent SVG behavior and actual visual editor usability remain attributed to the prior E4 report.

## Verified Theme Builder inventory

Source: `list-site-parts`. All six returned `has_conditions=true`. Conditions are transcribed exactly. Active is the API's returned flag at the time of this read; inactive does not establish that a template will fail in its matching request context.

| Post ID | Returned title / type | Post status | Active flag | Conditions |
| --- | --- | --- | --- | --- |
| 126 | ROBYLO / Search Results / search-results | publish | false | `include/archive/search` |
| 125 | ROBYLO / 404 / error-404 | publish | false | `include/singular/not_found404` |
| 124 | ROBYLO / Archive / archive | publish | false | `include/archive`, `exclude/archive/search` |
| 123 | ROBYLO / Single Post / single-post | publish | false | `include/singular/post` |
| 114 | ROBYLO / Universal Footer / footer | publish | true | `include/general` |
| 113 | ROBYLO / Universal Header / header | publish | true | `include/general` |

Header 113 and Footer 114 are separate documents with site-wide `include/general` conditions. Do not edit the Homepage expecting to change their definitions.

## Verified Homepage structural locators

Source: `get-page-structure(154)`. These are saved element identities and Navigator titles. The lean tree does not establish all settings or which Component definition each instance uses.

| Element ID | Returned title / purpose |
| --- | --- |
| `46c3aad4` | GCPRO Homepage Main |
| `a62cdd3` | 01 Hero |
| `7b416658` | 02 Residential and Commercial Services |
| `38ed6da4` | 03 Core Restoration Services |
| `6cde656f` | 05 Emergency Response |
| `4681b8f5` | 06 How We Work |
| `4221ba60` | 07 Projects and Before After |
| `5b2c6d3c` | 04 Why Choose GCPRO |
| `7d8c17ad` | 09 Service Areas |
| `37feb023` | 10 Final CTA |
| `5a3d7f5d` | Core Service Cards (six named instances) |
| `5fa5a818` | Residential Service Path |
| `4e0d3e66` | Commercial Service Path |
| `4af4b551` | Emergency Eyebrow — Editable Label |

Titles retain their existing numbering even when the order differs. The tree also contains four process instances, three project wireframes, two testimonial placeholders and eight city links: Lombard, Downers Grove, Highland Park, Elmhurst, Elk Grove Village, Bridgeview, Naperville and Glenview. Their presence is not evidence of approved copy, completed media or working destinations.

## Reported history and superseded information

| Reported ID / claim | Source | Current evidence / verification still needed |
| --- | --- | --- |
| Homepage 154 received V2 composition; eight Service Card instances restored | E4 completion report | Page and section/instance structure verified E3; complete settings/rendering not retested |
| Service Card 62 supports independent SVG changes without detaching | E4 | Identity and current override schema verified E3; repeat independent-instance/editor check before relying on it |
| CTA 80 and Emergency Service Mark 286 refined; 65/68/86 layouts updated | E4 | Identities and selected schemas verified E3; implementation diff and rendering not reproduced |
| Header 113 refined; Footer 114 unchanged during V2 | E4 | Current identities/status/conditions verified E3; historical unchanged claim not re-proven |
| Validation/Style Guide 50 used for component tests | E4/E5 | Page 50 exists as a draft; coverage/persistence not retested |
| Button 53 called Primary; 56 Accent; 59 Outline in old register | E5 | Current names in verified inventory supersede these old labels |
| Old Service Card 62 had text-symbol icon and different nested structure | E5 | Current schema exposes SVG Icon; never replay the old definition as current |
| Page 7 reported preserved by earlier validation | E5 | Current page inventory confirms a draft only; no unchanged-state comparison performed here |

No additional unverified numeric page/component ID is invented. If a future handoff reports another ID, add it to this reported section with its source/date until a read verifies host, type, name and status. Do not create absent pages or alter IDs as part of maintaining this map.

## Homepage V2 saved-state reconciliation — E6

Fresh full reads on 2026-10-16 match the prior final snapshot for 154, 62, 65, 68, 80, 86, 286, 113 and 114. This corroborates saved configuration, not a new visual/editor or independent-override test. Details and historical QA: [milestone](milestones/2026-10-16-homepage-v2.md).

| Homepage instance | Role | Saved SVG attachment |
| --- | --- | --- |
| `5fa5a818` | Residential | 204 |
| `4e0d3e66` | Commercial | 205 |
| `28d9f7c` | Water Damage | 192 |
| `7ce1a666` | Fire & Smoke Damage | 193 |
| `4ac87e43` | Mold Remediation | 206 |
| `95336d4` | Reconstruction | 207 |
| `318ea723` | Storm Damage | 208 |
| `22d372d7` | Personal Property Restoration | 209 |

All eight reference existing Component 62 and retain the five exposed fields. Their service destinations are `#`, not completed service routes. The confirmed extra `43e3093` is absent. Style Guide 50 has `edbef13` (Service A, SVG 192) and `2049f456` (Service B, SVG 193); its validation anchors remain `#robylo-content`.

Component 62 has a native SVG, H3, description and text link. Component 80 has an inset CTA panel with primary/secondary actions and six exposed fields. Component 286 is an informational native `div`, not a telephone anchor; `label` exposes Eyebrow Text. Its Homepage instance is `4af4b551`. Phone actions remain separate CTAs. No new Component ID was created for V2.

Header 113 uses the existing WordPress Menu widget `7983af36`. The V2 implementation enabled the native Full Width control through the editor (the working stored value was `stretch`; do not infer it from a connector enum). Header CTA instance `cd66895` and Homepage Request Service actions remain `#` pending a real destination. Hero Call instance `a7bcc76` uses `tel:+18476563322`. Footer 114 matched the prior final snapshot; the earlier milestone also recorded its equality with the pre-V2 snapshot.

## ZIP UI and audience card locators — E8

Current on staging Homepage 154; fresh-read before future writes.

| Element | ID / relationship |
| --- | --- |
| Existing Service Areas section / two-column container | 7d8c17ad / 585624a1 |
| Left introduction | 3dc285eb; existing city parent d6dbbe2 moved here before directory action |
| ZIP panel / H3 / description | 49f026c9 / 1c84aa78 / 264a3beb |
| Native Form / label / controls row | 376376c8 / 10dd9f53 / 4a71aa98 |
| Native input / disabled submit button | 351e2f2 / 5350691e |
| Input ID / associated label for | gcpro-area-zip |
| Future-feature notice | 244c26e6 |
| Native required hidden status slots | 42bd3375 / 2cbaaa52; not coverage results |
| Component 65 Step Number | 77fda46a; class process-step-number plus retained card-icon/hide-empty |
| Existing Residential / Commercial wrappers | 4c8810dc / 2066a26; now linked cards, destination # |
| Residential body / heading / description / SVG | 6b95719 / 7f49d2f5 / 1a430710 / 658b1119 |
| Commercial body / heading / description / SVG | 687ff42f / 51809f70 / 6eb72b87 / 6773a91b |
| Shared decorative arrow asset | attachment 464, robylo-arrow-right.svg, 24 by 24 |

The former audience instances 5fa5a818 and 4e0d3e66 were removed only from this section to implement the owner's new card reference. This supersedes the eight-instance Homepage mapping above: the six core service instances remain Component 62. No shared Component 62 definition was changed; no new Component ID was created.

The eight city links and All Service Areas still use their existing # destinations because destination pages are absent. The two audience card destinations likewise remain #. Header/Footer and other page assignments were not changed. Native input placeholder, text type, required/read-only switches, label association, button disabled attribute and card text are editable through standard Elementor controls. Form's empty-actions persistence limitation is documented in the [milestone](milestones/2026-10-16-zip-and-homepage-refinements.md).

## Homepage CTA instance values — E10

Native instance-only edits on staging 154, 2026-10-16. This supersedes the earlier Hero/Final action order, not their structure or shared definitions.

| Saved Homepage instance | Existing Component | Current exposed values |
| --- | --- | --- |
| `18a239c4` Hero primary | 53 | `text`: CALL 847-656-3322; `link`: tel:+18476563322 |
| `a7bcc76` Hero secondary | 103 | `text`: REQUEST SERVICE; `link`: # |
| `37feb023` Final CTA | 80 | `cta_text`/`cta_link`: CALL 847-656-3322 / tel:+18476563322; `secondary_text`/`secondary_link`: REQUEST SERVICE / # |

Header CTA `cd66895` remains Request Service/#; Emergency Call/Request actions are unchanged. Fresh before/after reads of Header 113 and Footer 114 are equal. Six-page inventory still has no Request Service page. Do not use a production URL, fabricate a staging route or detach Components to resolve that gap. See [CTA milestone](milestones/2026-10-16-homepage-cta-strategy.md).

## Updating the map

Record environment, read date, source operation, exact type/title/ID and status. Keep numeric document/component IDs distinct from hexadecimal element IDs and global class IDs. Re-read element structure after mutations because replacements can assign new IDs. Update renamed/deleted entries and move superseded claims into reported history with an explanation.
