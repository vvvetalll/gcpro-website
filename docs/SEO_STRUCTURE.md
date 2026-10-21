# GCPRO SEO URL architecture and Draft skeleton

**Current E77,2026-10-21:** Residential Services484 is a completed nine-section Atomic service hub. Existing Homepage designs promoted once into shared How We Work1152, Why1149 and Service Areas1140 and placed on both Pages; residential content uses Overrides. Existing CTA80/Code847 now share video/radius behavior;590 shares touch timeline animation. No new Global Classes/Variables/plugins/dependencies; three actual shared definitions,52 Page nodes/no new local Page CSS. Header/Footer/Core/BEAF unaffected.93 Pages88 Published/5 Draft;321 URL records preserved. Seven-width browser tests pass; anonymous403, editor loading and rendered meta-description remain explicit limits. [Exact owners, reuse, evidence and rollback](components/residential-services.md).

**Current E76,2026-10-21:** Projects now links to real structural Page1132 `/portfolio/`, with native All Projects / Before & After dropdown. Existing13 project records/URLs untouched. Standard-grid five-item Header and utility Partner Programs retained.93 staging Pages:88 Published/5 Draft;321 migration rows. No new E76 CSS/JS/classes/plugins/dependencies. [Exact storage, checks and limitations](audits/2026-10-21-projects-navigation.md).

**Current E75 (includes pending E74 sync), 2026-10-21:** Staging structural publication:92 Pages,87 Published/5 Draft;84 newly published approved targets including Resources1007,51 city Pages and Partner982–986. Native shared Single Page1008 supplies79 structural placeholders. Final service-first Header113:five main sections (Residential/Commercial/Service Areas/Projects/About), utility Partner Programs with four children/Careers/Contact Us; Blog and Our Team await real staging destinations. Standard1200px grid/logo sizes retained, native toggle below1200, one complete mobile menu. No production/BEAF/Footer/Homepage-content/903 edits.321 canonical migration rows preserve prior source mappings/decisions. [Exact storage, tests, limitations and rollback](audits/2026-10-21-staging-structure-and-navigation.md) · [Actual hierarchy](SITEMAP.md).

**Current E73,2026-10-21:** Authenticated production admin read-only inventory completed for visible content lists:90 Pages(88 Published/2 Draft),30 Posts,13 Portfolio,34 BEAF and61 Elementor objects;22 relevant terms. Newly found Draft Pages15553/11856 have no saved slug or proven public history. Combined XML omits4 published Pages and all13 projects. Reading Settings directly confirm front40/posts2187(Blog). Canonical register now320 rows, preserving prior212 URL/mapping/action records. Staging adds Partner Programs982 with four Draft children983–986, minimal native Atomic headings and prepared unassigned menu13; existing Header/Homepage/Footer/BEAF untouched. [Complete navigable sitemap](SITEMAP.md) · [Audit, counts, limits and exact owners](audits/2026-10-21-production-admin-and-partners.md).

## Preservation baseline and future migration map — E72

Owner clarification,2026-10-21: **preserve every existing URL now; current paths are not a final long-term architecture decision.** Future optimization may update, merge, redirect or remove only after separately approved evidence-based decisions. Historical audit recommendations never authorize execution. No redirects/deletions/removals/slug or URL changes/publications were performed.

The approved Page skeleton is already complete. Fresh authenticated native WordPress Pages REST reads (including publish/draft/pending/private/future/trash) verify **86 Pages:83 Draft/3 published**, all81 approved mapped IDs/statuses/saved paths and51 city children. All existing intended paths match complete saved parent chains; no new objects or duplicate skeleton needed. Additional970 is the existing Hero experiment. Layout construction, native posts/CPT imports and archive setup are distinct future milestones; this clarification does not authorize speculative objects for the8 existing URL holds.

### Single canonical register and field contract

[SEO_URL_INVENTORY.csv](SEO_URL_INVENTORY.csv) remains the sole editable URL inventory/migration map. It now has **212 rows**: every207 prior source/proposal row unchanged in all original fields, plus5 staging-only Pages2/7/12/50/970. New columns are appended, preserving legacy header order and all original exact scheme/host/query variants and IDs. `inventory_url` is the exact discovered identity; `inventory_scope` distinguishes source/proposed production rows from staging-only rows. For staging-only rows, production_url/production_object_id remain blank: never invent production equivalents or history. Stable original url_id values remain unchanged; staging-only identities use a distinct stable prefix.

| Requested information | Authoritative fields / interpretation |
| --- | --- |
| Original production URL/object/type | production_url,production_object_id,production_parent_id,source_content_type,required_wp_object_type. Installation IDs remain distinct from staging IDs. Archive/operational rows may have no singular WP content ID; absence is not a fabricated Page |
| Current publication/status evidence | production_publication_status,production_status_checked_at_utc,production_status_evidence; staging_status,staging_checked_at_utc. Public REST absence is unverified, not draft/deleted. HTTP status is separate from publication status |
| Proposed staging destination | proposed_staging_url,staging_url_basis plus existing verified_staging_slug/parent/full path/staging_object_id. A Draft path is intended future routing, not a working public URL. 108 additional preservation-only staging URL candidates are derived from existing proposed targets, labeled unimplemented/unverified; unbuilt archive/import/review routes remain explicitly uncreated |
| SEO metadata/canonical | Existing live_seo_title,live_meta_description,live_canonical/live_robots_meta/live_x_robots_tag; seo_metadata_observed_at_utc mirrors the original observation date. audit_* fields remain separate historical source evidence; blank means unavailable, never invented |
| Available search performance | search_performance_json: exact per-URL source GSC clicks/impressions/CTR/position, Ahrefs keyword/backlink/referring-domain counts and GA4 organic sessions/key events; performance_evidence identifies source/export/hash. Numeric zero remains0; missing metrics remain JSON null |
| Orphan/history | orphan_assessment distinguishes incoming links observed vs candidate within dated collected set vs unassessed. public_history_status and append-only url_history_json preserve dated observations. Never infer prior public accessibility from Draft existence |
| Future recommendation | future_action uses KEEP / UPDATE / MERGE / 301 REDIRECT / REMOVE / REVIEW; future_action_status is proposal_only_not_execution_authorization; recommendation_reason/evidence retain exact source justification and evidence IDs |
| Proposed/final target | future_destination_url retains source proposed target; final_destination_url stays blank until the specific restructuring destination is approved. Existing proposed_destination_url and legacy migration_decision remain preservation-baseline history, not final architecture approval |

**Vocabulary correction:** The legacy migration_decision mapped UPDATE→KEEP and REDIRECT301→301 for the earlier build queue. It is retained without rewriting history. Use the new future_action for future optimization:133 UPDATE,43 KEEP,2 MERGE,9 301 REDIRECT,13 REMOVE,12 REVIEW (7 prior unapproved/current-only proposals plus5 staging-only objects). Do not treat any of these as approved redirects/removals. Review can supersede any source recommendation with dated evidence; never drop the source row.

### Sources, coverage and limits

Fresh read-only production public REST exposes88 Pages,30 posts and13 portfolio items. Every exact public object URL already exists in the207-row baseline; production IDs are matched only on exact returned URLs. No production write/authentication or staging credential transmission to production occurred. Current source-object status reads are dated separately from the2026-10-16 HTML/metadata observations. This is not a new190-URL SEO crawl or current canonical certification.

Original audit workbook `GCPRO-SEO-audit-and-migration.xlsx`, SHA256 b4619b0a733652e845f5ef78702344c8e5beb59a0d905ec2eb615f52d4bb1774, was read without editing. Its200 URL rows and Migration map supplied exact recommendations/reasons/targets/evidence.125 URLs have GSC clicks available; GSC window2025-10-01 through2026-09-30, export2026-10-15, Web property scope. CTR is a fraction. Ahrefs/backlink/GA4 figures keep their source labels and may have different scope/freshness; no mixed-period totals were synthesized. No live Search Console/GA4 connection or fresh performance export was available/claimed. Planned query targets are not an observed query-to-page join. Low/zero/missing traffic alone does not justify removal.

**Coverage gaps retained explicitly:** no authenticated production Draft/private/trash export, no complete historical redirect/access-log/backlink/archive discovery beyond supplied sources, and no definitive site-wide orphan proof. Production unpublished completeness cannot be certified from public REST. Include any later-discovered unpublished/historical/orphaned URL in this same register immediately, with status/date/source and REVIEW if no justified decision exists. A production Draft without proven historical URL gets no invented previously public address. The existing51 city drafts and all discovered historical/query/admin/resource rows remain accounted for. Unrelated staging private-post fixtures are not GCPRO migration content and are not promoted into business URL mappings.

### Maintenance and approval gate

Append discoveries; do not normalize away exact source variants, remove retired rows, overwrite original metadata or equate missing data with zero. Preserve proposed vs approved vs executed action states separately and append dated decision/URL-history entries. Before later restructuring, obtain authenticated production inventory including unpublished objects, refresh crawl/canonicals/link graph and full URL-level performance/backlink evidence, choose/approve final destinations, then separately authorize execution. Only that later phase may implement redirects or URL changes and must test chains/loops/equivalence/internal links. Draft approval/building is not redirect/publication approval.

Validation: all original207 rows/cells preserved;212 unique stable IDs; all81 mapped Pages independently match saved status/slug/parent/full path; source workbook hash and200 exact URL matches checked; available125 GSC rows transferred with missingness retained. [Sanitized reconciliation evidence](evidence/2026-10-21-url-preservation-reconciliation.json). No rendered website changes, custom code/classes/Variables/Components/plugins/dependencies or responsive QA were introduced/required. Everything below is dated E12–E14 history and should be read with this clarification.


Verified 2026-10-16, America/Chicago. Environment: https://vitaliiv1.sg-host.com. **The approved native Page skeleton is complete: 15 earlier root Drafts + 64 new hierarchical Drafts + 2 reused business Pages cover all 81 verified retained Page destinations.** Eight unresolved URL decisions, native posts/CPT imports and archive setup remain separate. No launch, redirects, page publication, content rewrite or template construction occurred. E14 used authenticated native WordPress REST on staging only; the E13 production archive findings from commit `6b53d20` remain unchanged.

## Authoritative inventory and source decisions

[SEO_URL_INVENTORY.csv](SEO_URL_INVENTORY.csv) is the single canonical machine-readable URL register. Do not maintain a second editable URL inventory in another format. The tables here are summaries and ID references, not competing registers.

The source workbook is `GCPRO-SEO-audit-and-migration.xlsx`, dated 2026-10-15, SHA-256 `b4619b0a733652e845f5ef78702344c8e5beb59a0d905ec2eb615f52d4bb1774`. Its URL inventory and Migration map each contain 200 records. Its Proposed sitemap contains 138 retained destinations and two unapproved proposals. The earlier `GCPRO-url-by-url-build-register.csv` supplies layout families and build order, with 138 queued retained destinations. Workbook sources were read without modification. No new search metrics were generated.

The master register contains **207 URLs: 200 audited + 2 proposed + 5 current-only**. Exact original URLs are preserved, including host/scheme/query variants and administrative patterns. `url_id` is a stable `url-` plus the first 12 SHA-256 characters of that exact URL. Do not normalize away source rows.

Original audit actions remain in `source_audit_action`: UPDATE 133, KEEP 43, MERGE 2, REDIRECT 301 9, REMOVE 13. For the required migration vocabulary only, UPDATE maps to KEEP and REDIRECT 301 maps to 301 in `migration_decision`; this does not overwrite the audit or approve new redirects. KEEP totals 176, including operational routes that must not become Pages. All 176 retain their exact source destination URL in the register. Seven unaudited/proposed rows deliberately have no approved migration decision.

Public production REST inventories identified 88 Pages, 30 posts, 13 `portfolio` items, 12 tags and one category. These are source-installation IDs, never staging IDs. Live HTML was collected for 190 URLs: 185 returned 200, four returned 404, one request failed. Administrative patterns, queries and similar artifacts were deliberately not requested. Public metadata is dated by each row's UTC collection timestamp; it is not a claim to have repeated the entire SEO research.

The CSV records live title, description, canonical, meta/X-Robots directives, complete observed H1–H6 sequence, internal outgoing URLs, incoming source URLs within the collected set, media src/alt/srcset, content-source URL and HTML hash. Historical audit metadata remains in separate columns. Live body/media observations can include shared navigation, footer and assets; they do not establish ownership, licensing, article relevance or content approval. Raw HTML and private configuration snapshots remain local and are not committed.

## Exact implementation counts

| Inventory status | URLs | Actual outcome |
| --- | ---: | --- |
| Existing objects reused | 2 | Homepage 154 published; Privacy Policy 3 Draft, existing body preserved |
| New Draft Pages created and re-read | 79 | 15 root Drafts in E12 + 64 child Drafts in E14; no layout content |
| Pages awaiting Draft-parent capability | 0 | Resolved through existing same-host authentication and native REST; all 64 children verified |
| Posts awaiting content import | 29 | Native `post`, not Pages; no posts created in this Page-skeleton task |
| Project items awaiting model/import | 13 | Production `portfolio` CPT; no duplicate Pages |
| Retained archive/index/taxonomy routes mapped | 30 | 12 tag archives + 16 date archives + Blog posts-index candidate + Portfolio archive; not created as Pages |
| Other retained operational routes | 22 | 9 feeds, 5 pagination routes, 4 parameter variants, 3 administrative patterns, 1 resource |
| Retained source requiring review | 1 | `/team/` is currently 404 and absent from the public Page inventory |
| MERGE/301/REMOVE: no source objects created | 24 | Source decisions preserved; no redirects/deletions executed |
| Current-only sources requiring review | 5 | Four Pages and one category, no approved decision |
| Proposed pages not approved | 2 | No objects created |
| **Total** | **207** | Status groups are mutually exclusive |

There are **zero detected duplicate nonempty Page paths, slug collisions or auto-suffixed new slugs**. Uncertainty/approval holds remain **8**: retained `/team/`, five current-only rows and two proposed rows. None was created. The 64 technical parent holds are resolved; pending posts/CPT imports and archive setup remain separate. Staging now has **85 Pages: 3 published, 82 Draft**, versus 21 before E14 and 6 before E12. Two unrelated private staging posts 131/133 are not GCPRO content migrations. Public staging taxonomy reads returned no tags and only Uncategorized 1; no matching business terms were reused.

## Created root Drafts and verified paths

All rows below are actual saved objects, not planned IDs. Intended paths are future public routes; **none of these Draft paths is a working public destination**. Native Quick Edit explicitly saved each slug; the Pages list was reloaded and its UI-backed values re-read. Status remains Draft and parent remains 0 for every row. MCP re-read all 15 documents and returned empty Elementor element arrays. Their native page template remains Default; layout family is planning metadata in the CSV, not a newly built Elementor template.

| Page | Staging ID | Verified intended path | Family |
| --- | ---: | --- | --- |
| Residential Services | 484 | `/residential-services/` | Residential service |
| Commercial Services | 499 | `/commercial-services/` | Commercial service |
| Apply | 486 | `/apply/` | Conversion / contact |
| Water extraction | 487 | `/water-extraction/` | Supporting service |
| Board Up | 488 | `/board-up/` | Supporting service |
| Odor Removal | 489 | `/odor-removal/` | Supporting service |
| Moisture mapping | 490 | `/moisture-mapping/` | Supporting service |
| Dehumidification | 491 | `/dehumidification/` | Supporting service |
| Service Request | 492 | `/service-request/` | Conversion / contact |
| Before And After | 493 | `/before-and-after/` | Project / case study |
| Copyright | 494 | `/copyright/` | Standard content |
| Service Area | 495 | `/service-area/` | Service area / city |
| Contact Us | 496 | `/contact-us/` | Conversion / contact |
| About Us | 497 | `/about-us/` | Standard content |
| Testimonials | 498 | `/testimonials/` | Standard content |

Existing Privacy Policy 3 already has `privacy-policy`, parent 0, Draft; it was reused without rewriting its generic body. Homepage 154 remains the published static front page. Existing Pages 2, 7, 12 and 50 remain unrelated retained staging objects, not reused business destinations.

## Completed hierarchical Drafts — E14

Created **64 native WordPress Pages, IDs 514–577**, all Draft with empty raw content and Default native template. No Elementor layout, shared Component instance or page-design content was generated. All full path/ID mappings live only in the canonical CSV; the following groups summarize them.

| Parent Page / intended prefix | New Draft children | Representative verified IDs/paths |
| --- | ---: | --- |
| Residential Services **484**, `/residential-services/` | 6 | Water Damage **514**, Mold Removal **516**, Fire & Smoke **517**, Reconstruction **518**, Personal Property **521**, Storm Damage **523** |
| Commercial Services **499**, `/commercial-services/` | 6 | Water Damage **515**, Mold Removal **519**, Fire & Smoke **520**, General Contracting **522**, Reconstruction **524**, Personal Property **525** |
| Service Area **495**, `/service-area/` | 51 | Lombard **526**, Downers Grove **527**, Highland Park **528**; all 51 exact city slugs in CSV |
| About Us **497**, `/about-us/` | 1 | Careers **534**, `/about-us/careers/` |

**Water Extraction 487 remains `/water-extraction/`, parent 0, Supporting service.** It is not Residential Water Damage **514**, `/residential-services/water-damage/`, parent 484, or Commercial Water Damage **515**, `/commercial-services/water-damage/`, parent 499. The original three distinct production paths and purposes are preserved.

For every new child: authenticated create returned 201; an independent GET re-read saved ID/slug/parent/Draft/empty content; the complete parent chain reproduced the exact approved path; native `permalink_template` filled with the **saved slug** matched that path. A final all-Page read confirmed 64 added IDs, 85 total Pages, no duplicate nonempty paths and unchanged saved native fields of all 21 preexisting Pages. All **81** verified retained Page destinations now map to actual objects. These are verified intended future paths, **not anonymous public route-resolution tests or published destinations**.

WordPress's Draft `generated_slug` suggestion differs from the explicitly saved slug in 19 children because titles differ from approved URL slugs. It must not replace the saved `slug`; do not turn a title suggestion into a migration URL change. Recheck actual public routes at authorized publication/migration.

The native editor for 514 actually displayed Draft, slug `water-damage`, Parent Residential Services and the standard Edit with Elementor action. No editor field was changed and no page design was started. [Sanitized E14 verification](evidence/2026-10-16-completed-page-skeleton.json) records actual counts, IDs, auth/capability checks, unchanged-resource hashes and limits without credentials or full private snapshots.

## Hierarchy and resolved native interface limitation

Preserve actual production URL hierarchy, not the sitemap's logical navigation column. The five supporting services remain at root. Residential and commercial services have their own six existing child paths. Preserve `/fire-smoke/` under each hub, not an invented `/fire-smoke-damage/`. All 51 retained city Pages belong under `/service-area/`; Careers belongs under `/about-us/`.

The CSV's `production_parent_id` comes from the live production Page object. `intended_parent_path` is the URL parent; `intended_parent_staging_id` refers to the actual staging hub. All 64 former pending children now have real `staging_object_id`, saved slug/parent and verified full path, `created_draft_verified` status and `not_public_draft` link readiness. Other uncreated objects still have blank IDs.

**Historical E12 interface limitation, resolved in E14:** native WordPress Quick Edit's Parent select offered only published Pages 12, 154 and 2. Gutenberg Parent search found published Sample Page but not existing Draft Privacy Policy. The exposed `elementor_create_page` accepts title/post_type only, not native `slug` or `parent`; Elementor document settings are not a native `post_parent` interface. These interface limits are not a WordPress prohibition on Draft parents.

E14 found an **existing configured same-host Basic Authorization header** for the staging MCP connection. A normal authenticated `GET /wp-json/wp/v2/pages/484?context=edit` succeeded. Native Pages OPTIONS confirmed `slug:string`, `parent:integer`, `status:string`; current-user capability read confirmed `edit_pages`. This existing authentication also permits standard WordPress Page REST requests; no new credential, plugin, code, security change or browser-session extraction was needed. Credentials stayed in local configuration and were never copied into Git/evidence/output. Requests were constrained to HTTPS staging with redirects refused.

Created children with standard `POST /wp-json/wp/v2/pages` containing approved `title`, `slug`, Draft `parent` ID, `status=draft`, empty content; only create operations were sent, no existing Page/settings updates or publishing. Duplicate checks preceded each write; a persistent local operation record prevented blind retries/re-creation. Independent GETs and final inventory reads verified outcomes. This is native API orchestration, not deployed PHP/JS/CSS or a workaround to the WordPress object model. See [WordPress Pages reference](https://developer.wordpress.org/rest-api/reference/pages/), [authentication](https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/) and [workflow](WORKFLOWS.md#native-draft-page-hierarchy--e14). Do not publish parents, change globals, alter the database or inject editor state to assign hierarchy.

## Correct object models and unresolved SEO decisions

- `/blog/`: current public signals are consistent with a WordPress posts index (`blog` body class and a native Page-based menu item for 2187), rather than the owner's January 2026 category archive. The exact current Reading/query configuration is not authenticated/verified. The CSV now marks this as a posts-index candidate pending confirmation; see the historical/current comparison below. Preserve `/blog/` and do not create a duplicate Page or assume the old category title hooks still run. Staging currently has no posts-page assignment.
- `/portfolio/`: live body is `post-type-archive-portfolio`, although REST also exposes Page 8929. Production type `portfolio` declares an archive. Staging public REST types and admin navigation expose no portfolio CPT. Confirm the supported project model/registration and archive before importing its 13 entries or connecting links. Do not register a new model/plugin within this skeleton task.
- `/team/`: audit says KEEP; current public response is 404 with no matching Page. Preserve that disagreement. Do not invent a destination or create a team Page without reconciliation.
- Current-only Pages `/connect/`, `/test2/`, `/corporate-signatures2/`, `/thank-you/` have no approved audit decision. The current category's REST link is `https://gcprochicago.com/./news/`; preserve the observed spelling and review canonical/route normalization before any mapping. All five are review items, not approved KEEP destinations.
- Proposed `/commercial-services/storm-damage/` and `/sewage-cleanup/` remain unapproved; the latter currently returns 404. No Pages created.
- Other live 404s include audited `/water-damage-restoration-naperville-6/` and a leaked plugin-directory artifact. Their original audit decisions remain authoritative pending review; this task executes none of them.
- Audit-vs-live title changes and non-self canonicals are recorded per URL, not silently repaired. Existing Product/review schema, business-data inconsistencies and unsupported claims are not copied into new Drafts. Future content migration still requires approved copy/media and correct metadata/schema implementation.

## Blog/Portfolio historical PHP and current routing follow-up — E13

Owner-supplied history, recorded 2026-10-16: in January 2026 `/blog/` was a category archive with `archive category category-blog category-1`. PHP targeted `is_category('blog')` to control document title, Elementor page title `BLOG`, archive title and meta description. Portfolio used a `portfolio` CPT archive plus an Elementor Archive Template. A `nav_menu_css_class` filter also adjusted Blog/Portfolio active states for archive and single content. This is attributed historical information, not a verified copy of current source code; its source file and present execution are unknown.

Fresh direct public GET/REST checks at 2026-10-16 17:00 UTC and actual IAB DOM reads establish:

| Signal | `/blog/` | `/portfolio/` |
| --- | --- | --- |
| Public response / canonical | 200; same `/blog/` self-canonical | 200; same `/portfolio/` self-canonical |
| Current body/query markers | `blog`; no `archive category category-blog category-1` in the served body | `archive post-type-archive post-type-archive-portfolio` |
| Rendered Elementor document | Archive **6858** | Archive **8412** |
| REST source objects | Published Page **2187**, slug `blog` | Registered `portfolio` type, `has_archive=true`, taxonomy `project-type`; also published Page **8929** |
| Current document title | `Property Overhaul: Our Restoration Blog \| GCPRO` | `Portfolio \| GCPRO` |
| Current H1 | `Blog: All About Property Restoration` | `Portfolio` |
| Meta description | `Dive into our blog for top property restoration tips, from damage repair to full-scale renovations. Your guide to revitalizing spaces` | No description observed in the checked HTML |
| Native Footer menu object markers | Page-based item **2905**, object Page 2187; not a category item | Post-type-archive item **10146**, object `portfolio` |

Both render Header **21168** and Footer **21217** on production; these are unrelated to staging 113/114. A sampled article 21140 renders Single Post template **5897**; project 10625 renders template **7996** (returned frontend `data-elementor-type=single-post`, body `single-portfolio`). These are verified rendered IDs, **not verified Theme Builder Display Conditions**, post_meta settings or portable staging IDs.

The public category inventory currently exposes only News **49**, slug `news`, link `/./news/`; no `blog` term was returned. This does not prove that an old hidden/empty term or custom query cannot exist. Together with the `blog` body marker, Page-based menu reference and `current_page_parent` on the sampled article, this supports a **current posts-index interpretation**. It does not prove native `page_for_posts=2187` or the removal of historical PHP: body/menu classes and templates can be customized. Earlier E12 wording that definitively called it a posts archive is superseded by this qualified mapping. Portfolio's CPT archive is independently confirmed by both the registered type and rendered body.

### Access limits and exact code locations

Production `/wp-admin/` redirects to the WordPress login form in the internal browser. Anonymous `/wp-json/wp/v2/settings` and a targeted public `elementor_library` query for templates 6858/8412 both return **401 `rest_forbidden`**. The available Elementor MCP remains connected to staging, not production. Production Reading Settings, Theme Builder conditions and theme/plugin/snippet PHP are therefore not available through current authenticated access. [Sanitized read-only evidence](evidence/2026-10-16-archive-routing.json) records the actual responses and frontend markers.

Served assets/body identify the production theme directory **`wp-content/themes/custom-dev-theme-elementor-master/`**. That verifies the directory name only. **No current production PHP file path, line number, hook implementation or active code storage location has been verified.** Do not claim the historical hooks are in `functions.php`, a snippet plugin or a specific archive file. The locally available `functions-before-svg-import.php` identifies itself as ROBYLO Starter staging code and does not contain those Blog/Portfolio hooks; it is not evidence of production PHP. The GCPRO repository contains documentation, not an authenticated production theme source/export.

### Actual menu behavior and migration requirements

- On `/blog/`, the custom Header's desktop/mobile Blog items have `active`; Footer item 2905 has `current-menu-item`, `current_page_item`, Elementor active-link styling and `aria-current=page`.
- On `/portfolio/`, the Header Showcase parent has `active` and its mobile parent is `active open`; native Footer Portfolio item 10146 has current-item/Elementor active classes and `aria-current=page`.
- On sampled article `/signs-of-hidden-water-damage-in-your-home/`, Header Blog items have **no active marker**. Footer Blog has `current_page_parent current-menu-item current_page_item` on the LI, but its anchor lacks Elementor active class and `aria-current`. On sampled project `/portfolio/reconstruction-after-water-damage-on-montana-street-chicago/`, the Header has **no active item**; Footer Portfolio similarly gains LI current classes while its anchor lacks active class/`aria-current`.
- These observed LI-class additions on singles are compatible with the reported custom filter, but do not identify its cause or prove the filter still runs. Do not describe Header/Footer active behavior as consistently correct. Mouse/touch behavior and CSS-computed active colors were not audited in this read-only follow-up.

Later archive-template phase must: (1) authenticate a read-only review of production Reading Settings, rewrite/query behavior and complete category objects; (2) locate the exact current title/meta/menu code and Theme Builder conditions; (3) choose the supported native posts-index/category architecture while preserving `/blog/`, pagination, post/category relationships and SEO output; (4) preserve `/portfolio/`, project detail paths and its native CPT archive/taxonomy model; (5) configure archive headings, document titles, descriptions and canonical/pagination output through supported WordPress/Elementor/SEO controls; (6) test Blog/Portfolio active states across archive, pagination and single views in Header/Footer, with appropriate current/ancestor semantics. Use native object menu items and supported archive conditions first; do not copy `is_category('blog')` or `nav_menu_css_class` workarounds without a demonstrated remaining native gap and separate code authorization.

**No new Page, archive, PHP or website setting was created/changed in this follow-up.** No production or staging writes occurred. Public URLs remain unchanged. Title implementation, exact routing and code locations remain explicit review items, not guessed completion.

## Nine layout families and first representatives

Counts describe the existing 138-destination build queue, not 138 created Pages or nine completed templates.

| Family | Queue count | First representative | Current state |
| --- | ---: | --- | --- |
| Homepage | 1 | `/`, 154 | Existing; no changes |
| Residential service | 7 | `/residential-services/water-damage/`, 514 | Blank child Draft available |
| Commercial service | 7 | `/commercial-services/water-damage/`, 515 | Blank child Draft available |
| Supporting service | 5 | `/water-extraction/`, 487 | Blank Draft available |
| Service area / city | 52 | `/service-area/lombard/`, 526; hub 495 | All 51 city Drafts and hub available |
| Project / case study | 14 | `/portfolio/reconstruction-after-water-damage-on-montana-street-chicago/` | CPT model/import pending; Before And After 493 is a Page in this family |
| Standard content | 7 | `/about-us/`, 497 | Blank Draft available; Team remains disputed |
| Blog and archive | 42 | `/blog/` plus first retained post | Native archive/posts/tags pending, no duplicate Pages |
| Conversion / contact | 3 | `/contact-us/`, 496 | Blank Draft; form functionality not implemented |

Recommended first internal template is **Residential Water Damage 514**, followed by Commercial Water Damage 515, city Lombard 526, a project detail once its CPT model/import is ready, and About 497. Water Extraction 487 remains a distinct supporting-service representative. Do not duplicate Homepage layouts into the skeleton. E14 creates no visual templates and does not authorize starting those designs.

## Internal link dependencies and handoff

No links, navigation or Component definitions were edited. Existing Homepage/Header/Footer full trees match pre-task reads. Their destinations must remain independent supported overrides; this task does not replay the separate dynamic-link implementation work.

`staging_link_dependencies_json` records current Homepage/Header element IDs, Component fields, existing destination and target candidate on the relevant destination row. It also records all 31 destination-bearing entries from the existing shared menu. The 32nd menu record, Resources 242, is a `#` grouping trigger with no destination Page; retain it rather than inventing one. Native menu UI currently shows **32 Custom Links with `#`**, not 32 working object links. Parent triggers may intentionally remain triggers; destination items should become native object links only after availability is verified. Header and Footer both consume this menu. No menu records were removed.

Dependency groups:

- Header utility Contact, Careers and Blog; Header Request Service; logo's existing Internal URL → 154 is preserved.
- Homepage audience hubs; six residential core services; three project cards; portfolio index; Testimonials; eight city links and Service Area hub; Hero/Emergency/Final Request Service.
- Header/Footer shared menu: both service hubs and their children, six featured cities and directory, Portfolio/Before And After, Blog, About/Team/Testimonials/Careers.
- All observed production internal outgoing and incoming source relationships remain in the same CSV for later article, city, project and content migration. This is a complete list for the collected source set and scoped staging documents, not a claim to have audited every future website link.

Service Request 492, Contact 496 and all 64 new child Pages **exist as Drafts**; earlier missing-page/parent-blocked reports describe the prior baseline. They are not publicly available. Destination dependencies now identify created child IDs and `draft_not_public`; saved website links/menu records were not edited. Keep their `#` links explicitly unresolved until approved content/functions are ready and publication is authorized. Do not substitute preview URLs or claim service-request submission works. Core-service links remain residential candidates from the existing card purpose; review dual-audience routing in the later linking task without inventing shared service URLs.

## Safety and actual verification

- Before and after, native Reading Settings had Discourage search engines enabled, Homepage 154 and posts-page 0. No settings were saved. After work the anonymous staging root returned `<meta name='robots' content='noindex, nofollow' />`. `robots.txt` only disallows `/wp-admin/`; do not report a site-wide crawl block or access restriction. Noindex is advisory, not access control.
- Created IDs and saved Draft status were independently re-read through MCP; exact slugs/parent 0 were re-read from native Quick Edit-backed list values after reload. No `-2`/`-3` suffixes or duplicate intended new paths detected.
- Anonymous GET requests to the 15 intended Draft paths all returned 403. This is the observed public access result, not proof of the eventual published routing or a claim that WordPress Drafts universally return 403. Do not connect these paths as working public links; future publication requires its own route testing.
- All 15 new Elementor documents have empty element arrays. No styles, Components, Variables, plugins, code, final content or media were added. Native Default template was preserved; no family-specific visual template was constructed.
- Full saved content trees for Homepage 154, Header 113 and Footer 114 compare equal before/after. Homepage publication and front-page assignment remain unchanged. Existing navigation was read only. Production received public GET requests only; no production mutation or redirect operation occurred.
- No responsive/layout/keyboard QA replay was necessary or claimed: this task created blank Draft objects and changed no rendered layouts. The native Pages/Quick Edit UI was actually used; new visual template editing will be verified when a template is built.
- Local pre-task configuration snapshots were captured for the three preserved documents. A full database/files backup and restore test remains unverified; snapshots and this documentation do not substitute for it.

E14 safety check: native Reading UI remains discouraged/noindex, front page 154 and posts-page 0; anonymous root still emits `noindex, nofollow`. All 21 existing native Page records and registered native settings are unchanged. Full saved Homepage154/Header113/Footer114 trees and Global Classes/Variables resource responses and Component registry match before/after. The latter is a registry comparison, not a replay of every Component's visual behavior. Source audit actions/destination URLs, the eight review holds and the two E13 archive rows/findings are preserved; production was not accessed for writes or reconfigured. No responsive QA replay is claimed for blank, unpublished Pages.

Recovery is scoped: E14 added only IDs **514–577**. Any future authorized rollback must first check new dependencies and unchanged Draft content, then use recoverable native Trash only for the intended added objects. Preserve the earlier 15 root Drafts and existing 154/3/2/7/12/50; do not trash parent hubs while children depend on them. Scoped private snapshots/operation records complement recovery; full database/files backup and restore remain unverified. A Git revert does not restore WordPress.

## Migration and launch checklist — pending, not executed

1. The 64 Draft children are created and verified. At later authorized publication/migration, recheck saved hierarchy, collisions, IDs and actual public responses; do not recreate existing destinations.
2. Reconcile Team, current-only sources and proposed pages; preserve original decisions until approval changes them. Confirm CPT/archive/post/taxonomy model and import mappings.
3. Build the nine native layout families through approved representative Pages/objects. Preserve independently editable Components and object-bound links; do not bulk-copy Homepage markup.
4. Migrate approved content/media with source-to-attachment mapping, alt text, headings, relationships and verified business data. No automatic copy of incorrect schema, ratings or claims.
5. Transfer titles/descriptions/canonicals/robots accurately; compare current source evidence at migration time and ensure indexable destinations use correct self-canonicals. Validate archive, taxonomy, feed and pagination behavior separately.
6. Publish only after approval and staging functional checks. Replace intentional placeholders with native WordPress object menu items and supported Elementor Internal URL overrides; test actual frontend resolution and two-instance independence. Track unavoidable manual URLs and ID remapping.
7. Implement only approved MERGE/301/REMOVE behavior at the later authorized migration phase; test final targets, chains, loops, content equivalence and internal references. Reconcile unexpected live status drift before launch.
8. After domain migration, test every retained exact production path, metadata, canonicals, headings, media, forms, navigation, Components, redirects, sitemap membership and indexing. Remove staging restrictions on production only in the approved launch process; retain staging noindex. Native links reduce risk but do not eliminate testing.

## Editing the register

Use UTF-8 CSV with the existing stable header order. One row per exact original URL. JSON-valued cells preserve lists/relationships without a second inventory. Empty staging IDs mean no object was created; empty migration decisions mean no decision was approved. `destination_staging_object_id` is a target candidate lookup, not proof that a query variant/source URL is itself that object or publicly accessible. Preserve source action, historical/live separation, source timestamps and hashes when updating statuses. Never turn proposed IDs/paths or default Draft `?page_id=` preview behavior into verified public routes.
