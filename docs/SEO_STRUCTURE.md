# GCPRO SEO URL architecture and Draft skeleton

Verified 2026-10-16, America/Chicago. Environment: https://vitaliiv1.sg-host.com. Production was read only through public GET requests. **The skeleton is partially implemented: 15 root Draft Pages exist; 64 hierarchical Pages remain uncreated because the available native UI excludes Draft parents.** No launch, redirects, page publication, content rewrite or template construction occurred.

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
| New Draft Pages created and re-read | 15 | Exact root slugs, parent 0, no layout content |
| Pages awaiting Draft-parent capability | 64 | 6 residential + 6 commercial + 51 city + 1 careers; no IDs invented |
| Posts awaiting content import | 29 | Native `post`, not Pages; no posts created in this Page-skeleton task |
| Project items awaiting model/import | 13 | Production `portfolio` CPT; no duplicate Pages |
| Retained archive/taxonomy routes mapped | 30 | 12 tag archives + 16 date archives + blog archive + portfolio archive; not created as Pages |
| Other retained operational routes | 22 | 9 feeds, 5 pagination routes, 4 parameter variants, 3 administrative patterns, 1 resource |
| Retained source requiring review | 1 | `/team/` is currently 404 and absent from the public Page inventory |
| MERGE/301/REMOVE: no source objects created | 24 | Source decisions preserved; no redirects/deletions executed |
| Current-only sources requiring review | 5 | Four Pages and one category, no approved decision |
| Proposed pages not approved | 2 | No objects created |
| **Total** | **207** | Status groups are mutually exclusive |

There are **zero detected slug collisions or auto-suffixed new slugs**. Uncertainty/approval holds total **8**: retained `/team/`, five current-only rows and two proposed rows. These are separate from the 64 technical parent holds and pending imports/archive setup. Staging now has **21 Pages: 3 published, 18 Draft**, versus 6 before this task. Two unrelated private staging posts 131/133 are not GCPRO content migrations. Public staging taxonomy reads returned no tags and only Uncategorized 1; no matching business terms were reused.

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

## Hierarchy and native capability limitation

Preserve actual production URL hierarchy, not the sitemap's logical navigation column. The five supporting services remain at root. Residential and commercial services have their own six existing child paths. Preserve `/fire-smoke/` under each hub, not an invented `/fire-smoke-damage/`. All 51 retained city Pages belong under `/service-area/`; Careers belongs under `/about-us/`.

The CSV's `production_parent_id` comes from the live Page object. `intended_parent_path` is the URL parent; `intended_parent_staging_id` refers to the actual new Draft hub when one exists. The 64 pending children have blank `staging_object_id`, so nobody can mistake them for created Pages.

**Demonstrated blocker:** native WordPress Quick Edit's Parent select offers only published Pages 12, 154 and 2. Gutenberg Parent search finds published Sample Page but not existing Draft Privacy Policy. Its page Actions menu has no create-child command. The exposed `elementor_create_page` accepts title/post_type only; it does not expose native `slug` or `parent`. Elementor document settings are not a verified native `post_parent` interface.

Minimum required capability: a supported authenticated WordPress Page create/update interface exposing native `slug` and `parent` while retaining Draft status. For example, a connector exposing standard WordPress Page CRUD with those fields would suffice. No credential or role failure was demonstrated; the currently exposed controls cannot perform this relationship. Do not publish unfinished parents, fabricate flat child paths, edit the database, inject editor state or add workaround code. Complete the 64 children once that supported capability is available, then re-read full paths and IDs.

## Correct object models and unresolved SEO decisions

- `/blog/`: live body is a WordPress posts archive (`blog` class), although production REST also exposes Page 2187. Staging currently has no posts-page assignment. Plan native archive/Reading configuration later, retaining `/blog/`; do not create a duplicate Blog Page during this task.
- `/portfolio/`: live body is `post-type-archive-portfolio`, although REST also exposes Page 8929. Production type `portfolio` declares an archive. Staging public REST types and admin navigation expose no portfolio CPT. Confirm the supported project model/registration and archive before importing its 13 entries or connecting links. Do not register a new model/plugin within this skeleton task.
- `/team/`: audit says KEEP; current public response is 404 with no matching Page. Preserve that disagreement. Do not invent a destination or create a team Page without reconciliation.
- Current-only Pages `/connect/`, `/test2/`, `/corporate-signatures2/`, `/thank-you/` have no approved audit decision. The current category's REST link is `https://gcprochicago.com/./news/`; preserve the observed spelling and review canonical/route normalization before any mapping. All five are review items, not approved KEEP destinations.
- Proposed `/commercial-services/storm-damage/` and `/sewage-cleanup/` remain unapproved; the latter currently returns 404. No Pages created.
- Other live 404s include audited `/water-damage-restoration-naperville-6/` and a leaked plugin-directory artifact. Their original audit decisions remain authoritative pending review; this task executes none of them.
- Audit-vs-live title changes and non-self canonicals are recorded per URL, not silently repaired. Existing Product/review schema, business-data inconsistencies and unsupported claims are not copied into new Drafts. Future content migration still requires approved copy/media and correct metadata/schema implementation.

## Nine layout families and first representatives

Counts describe the existing 138-destination build queue, not 138 created Pages or nine completed templates.

| Family | Queue count | First representative | Current state |
| --- | ---: | --- | --- |
| Homepage | 1 | `/`, 154 | Existing; no changes |
| Residential service | 7 | `/residential-services/water-damage/` | Child object pending parent capability |
| Commercial service | 7 | `/commercial-services/water-damage/` | Child object pending parent capability |
| Supporting service | 5 | `/water-extraction/`, 487 | Blank Draft available |
| Service area / city | 52 | `/service-area/lombard/`; hub 495 | City object pending parent capability; hub Draft available |
| Project / case study | 14 | `/portfolio/reconstruction-after-water-damage-on-montana-street-chicago/` | CPT model/import pending; Before And After 493 is a Page in this family |
| Standard content | 7 | `/about-us/`, 497 | Blank Draft available; Team remains disputed |
| Blog and archive | 42 | `/blog/` plus first retained post | Native archive/posts/tags pending, no duplicate Pages |
| Conversion / contact | 3 | `/contact-us/`, 496 | Blank Draft; form functionality not implemented |

Recommended first internal template remains **Residential Water Damage**, followed by Commercial Water Damage, a city Page, project detail and About. Resolve the parent interface first. If work must proceed before that dependency, Water Extraction 487 is an unblocked supporting-service representative. Do not duplicate Homepage layouts into the skeleton.

## Internal link dependencies and handoff

No links, navigation or Component definitions were edited. Existing Homepage/Header/Footer full trees match pre-task reads. Their destinations must remain independent supported overrides; this task does not replay the separate dynamic-link implementation work.

`staging_link_dependencies_json` records current Homepage/Header element IDs, Component fields, existing destination and target candidate on the relevant destination row. It also records all 31 destination-bearing entries from the existing shared menu. The 32nd menu record, Resources 242, is a `#` grouping trigger with no destination Page; retain it rather than inventing one. Native menu UI currently shows **32 Custom Links with `#`**, not 32 working object links. Parent triggers may intentionally remain triggers; destination items should become native object links only after availability is verified. Header and Footer both consume this menu. No menu records were removed.

Dependency groups:

- Header utility Contact, Careers and Blog; Header Request Service; logo's existing Internal URL → 154 is preserved.
- Homepage audience hubs; six residential core services; three project cards; portfolio index; Testimonials; eight city links and Service Area hub; Hero/Emergency/Final Request Service.
- Header/Footer shared menu: both service hubs and their children, six featured cities and directory, Portfolio/Before And After, Blog, About/Team/Testimonials/Careers.
- All observed production internal outgoing and incoming source relationships remain in the same CSV for later article, city, project and content migration. This is a complete list for the collected source set and scoped staging documents, not a claim to have audited every future website link.

Service Request 492 and Contact 496 now **exist as Drafts**; earlier reports saying they do not exist describe the pre-skeleton baseline. They still are not publicly available. Keep their `#` links explicitly unresolved until approved content/functions are ready and publication is authorized. Do not substitute preview URLs or claim service-request submission works. Core-service links are mapped to residential candidates from the existing card purpose; review dual-audience routing in the later linking task without inventing shared service URLs.

## Safety and actual verification

- Before and after, native Reading Settings had Discourage search engines enabled, Homepage 154 and posts-page 0. No settings were saved. After work the anonymous staging root returned `<meta name='robots' content='noindex, nofollow' />`. `robots.txt` only disallows `/wp-admin/`; do not report a site-wide crawl block or access restriction. Noindex is advisory, not access control.
- Created IDs and saved Draft status were independently re-read through MCP; exact slugs/parent 0 were re-read from native Quick Edit-backed list values after reload. No `-2`/`-3` suffixes or duplicate intended new paths detected.
- Anonymous GET requests to the 15 intended Draft paths all returned 403. This is the observed public access result, not proof of the eventual published routing or a claim that WordPress Drafts universally return 403. Do not connect these paths as working public links; future publication requires its own route testing.
- All 15 new Elementor documents have empty element arrays. No styles, Components, Variables, plugins, code, final content or media were added. Native Default template was preserved; no family-specific visual template was constructed.
- Full saved content trees for Homepage 154, Header 113 and Footer 114 compare equal before/after. Homepage publication and front-page assignment remain unchanged. Existing navigation was read only. Production received public GET requests only; no production mutation or redirect operation occurred.
- No responsive/layout/keyboard QA replay was necessary or claimed: this task created blank Draft objects and changed no rendered layouts. The native Pages/Quick Edit UI was actually used; new visual template editing will be verified when a template is built.
- Local pre-task configuration snapshots were captured for the three preserved documents. A full database/files backup and restore test remains unverified; snapshots and this documentation do not substitute for it.

Recovery is scoped: retain the verified IDs/paths; any future authorized rollback can move only these 15 new blank Drafts to recoverable Trash after checking dependencies. Do not touch existing 154/3/2/7/12/50. A Git revert does not restore WordPress.

## Migration and launch checklist — pending, not executed

1. Resolve the native Draft-parent capability; create/re-read the 64 children with the exact planned parent IDs and paths, checking for collisions again.
2. Reconcile Team, current-only sources and proposed pages; preserve original decisions until approval changes them. Confirm CPT/archive/post/taxonomy model and import mappings.
3. Build the nine native layout families through approved representative Pages/objects. Preserve independently editable Components and object-bound links; do not bulk-copy Homepage markup.
4. Migrate approved content/media with source-to-attachment mapping, alt text, headings, relationships and verified business data. No automatic copy of incorrect schema, ratings or claims.
5. Transfer titles/descriptions/canonicals/robots accurately; compare current source evidence at migration time and ensure indexable destinations use correct self-canonicals. Validate archive, taxonomy, feed and pagination behavior separately.
6. Publish only after approval and staging functional checks. Replace intentional placeholders with native WordPress object menu items and supported Elementor Internal URL overrides; test actual frontend resolution and two-instance independence. Track unavoidable manual URLs and ID remapping.
7. Implement only approved MERGE/301/REMOVE behavior at the later authorized migration phase; test final targets, chains, loops, content equivalence and internal references. Reconcile unexpected live status drift before launch.
8. After domain migration, test every retained exact production path, metadata, canonicals, headings, media, forms, navigation, Components, redirects, sitemap membership and indexing. Remove staging restrictions on production only in the approved launch process; retain staging noindex. Native links reduce risk but do not eliminate testing.

## Editing the register

Use UTF-8 CSV with the existing stable header order. One row per exact original URL. JSON-valued cells preserve lists/relationships without a second inventory. Empty staging IDs mean no object was created; empty migration decisions mean no decision was approved. `destination_staging_object_id` is a target candidate lookup, not proof that a query variant/source URL is itself that object or publicly accessible. Preserve source action, historical/live separation, source timestamps and hashes when updating statuses. Never turn proposed IDs/paths or default Draft `?page_id=` preview behavior into verified public routes.
