# Projects architecture assessment — 2026-10-26

Status: **blocked at the content-model prerequisite; not a working portfolio approval prototype**. Owner requires a dedicated Projects CPT, service taxonomy, structured fields, one Single Project template, a separate archive and automatic service-page selections. No installation, custom code, migration or replacement of the existing catalogue is authorized in this assessment.

## Actual staging test

- Installed Elementor **4.3.5**, Pro **4.3.2**. Authenticated native WordPress types/taxonomies and installed-plugin reads show no Projects CPT, no project-field manager, and no taxonomy attached to Pages. Category and Tag belong to Posts only. No production writes.
- Created only Draft Page **2171**, `Projects Portfolio — Isolated Native Capability Prototype`: [logged-in preview](https://vitaliiv1.sg-host.com/?page_id=2171&preview_id=2171&preview=true), [editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=2171&action=elementor). Shared Hero1318 is an instance, unchanged globally. Draft includes a clear prerequisite notice, not simulated project results.
- Tested the actual visual editor, beyond MCP: native **Loop Grid** and **Taxonomy Filter** are available. Loop Grid's Source offers Posts, Pages, Manual Selection, Current Query and Related; no Projects source exists. Set the isolated test to Pages. Native Taxonomy Filter `7e28b6f` connects to Loop Grid `1b73b73`, but its Taxonomy dropdown contains only **Select a taxonomy**, with no selectable terms/taxonomies. Saved as Draft, never published. Loop has no card template assigned; these are diagnostic controls, not a functioning catalogue.
- Atomic Collection Loop schema supports content queries, include/exclude terms and optional previous/next pagination with page reload/AJAX. These are **editor query controls**, not evidence of an interactive visitor filter. Its currently advertised sources are post/page/manual/current_query. Compatibility of the separate Taxonomy Filter with Atomic Collection Loop is not established. Do not describe the existing manual Tabs queries as automatic classification.
- Stop point: registering the missing CPT/taxonomy/fields requires an additional content-model dependency or approved registration code. Neither is allowed now. No hardcoded project selection, duplicate project bodies, public test project or fake category confirmation was added.

## Smallest proposed system, subject to a subsequent authorized test

Use **one content-model/field dependency plus existing Elementor Pro**, before considering a filtering plugin. ACF PRO is a suitable single-dependency candidate: CPT/taxonomy registration, location text, gallery field and optional BEAF-reference text; WordPress already supplies title, body, excerpt and Featured Image. ACF Free registers CPT/taxonomy and simple fields, but its Gallery field requires PRO. This is a proposal, not a purchase or installation, and does not establish that every free alternative is unsuitable.

| Responsibility | Proposed owner | Current status |
| --- | --- | --- |
| Project record | CPT key `gcpro_project`; title/body/excerpt/Featured Image | Not registered |
| Confirmed location | Optional text; leave unknown locations empty | Field absent |
| Services | `project_service` taxonomy, multiple assigned terms | Taxonomy absent |
| Commercial classification | Separate project-sector taxonomy; Commercial is a sector, not a restoration service | Absent; use with Fire/Water in one query/filter strategy only after tested |
| Gallery | Ordered image field rendered by one native Gallery in Single Project | Existing per-page galleries work; field binding not tested here |
| Optional Before/After | Preserve original BEAF records and references; render only on detail pages initially | Existing shortcodes preserved; dynamic optional field/empty state untested |
| Detail design | One Theme Builder Single Project with dynamic title, cover, location, services, Gallery and Post Content | Native Theme Builder exists; current Single Page2125 already demonstrates dynamic title/excerpt/cover/content for the three Pages |
| Archive | One archive template and one query of Published `gcpro_project` | Blocked by missing CPT |
| Visitor filtering | Prefer native Loop Grid + Taxonomy Filter; separate Fire/Water service facets and Commercial-sector behavior need a real combined test | Widget available; project classification/filter behavior not testable yet |
| Service-page selections | Reuse one card design; query assigned service term, exclude drafts, never maintain project IDs | Blocked by missing taxonomy |

Owner workflow after implementation: add Project, enter verified content/location, select cover/gallery and optional existing comparisons, assign services/sector, publish. Published-only queries supply archive and service selections automatically. Template edits control presentation globally; field values remain project-specific. Test a temporary categorized project and return it to Draft before accepting this workflow.

The representative **existing** design references remain [catalogue](https://vitaliiv1.sg-host.com/portfolio/) and [Tinley Park project](https://vitaliiv1.sg-host.com/portfolio/from-ashes-to-excellence-tinley-park-home-restoration/). They were not rebuilt or relabelled as the new architecture. No separate representative Single Project prototype was created: it would lack the required registered type and field bindings. Desktop/mobile cards, category switching/All reset, automatic membership, new-project publication and field-driven Gallery remain **unverified for the proposed system**. Existing earlier gallery/layout verification is historical, not a new pass.

## URL-preserving migration plan — not executed

1. Retain the canonical exact URL register in `docs/SEO_URL_INVENTORY.csv`; snapshot all existing project Pages, IDs, parent relationships, metadata, media, BEAF references, templates and internal links. Include the ten existing project Drafts, not just the three Published sources.
2. Initially register/test the CPT with a temporary isolated rewrite/archive route, outside `/portfolio/`. Do not enable a second owner for `/portfolio/` while Page1132 owns it.
3. At a separately approved cutover, preserve Page1132 as a recoverable Draft snapshot at a nonconflicting private legacy slug. Activate CPT archive `/portfolio/` and a Theme Builder archive condition for `gcpro_project`. Existing menu object references to Page1132 need explicit conversion to the supported archive destination; do not leave them pointing to the relocated Page.
4. Configure nonhierarchical CPT single rewrite `portfolio`, `with_front=false`, retain each original `post_name`, and migrate records **in place only with an approved migration method**. Changing post type alone is not permalink preservation. Preserve IDs, bodies, metadata, attachments, SEO and BEAF references; remove obsolete Page-parent assumptions. No migration utility/code was installed here.
5. The following must resolve at exactly the same full paths after conversion, without relying on guessed redirects:
   - 2077: `/portfolio/from-ashes-to-excellence-tinley-park-home-restoration/`
   - 2078: `/portfolio/restoring-elegance-water-damage-reconstruction-of-a-wonder-lake-residence/`
   - 2079: `/portfolio/reconstruction-in-boys-and-girls-clubs-of-chicago/`
6. Retarget Single Page2125 conditions to one Single Project owner only at cutover; preserve the body galleries/BEAF until verified dynamic replacements match them. Refresh rewrite rules once, then verify archive, all preserved Published paths, draft exclusion, canonical/noindex state, native destinations and no `/portfolio/` slug conflict. Abort/restore snapshot and route ownership if any path changes. No production redirect or URL change is authorized by this plan.

## WP Grid Builder and BEAF

**A paid frontend filtering plugin is not proven necessary.** Native Pro already provides visitor taxonomy filtering with Loop Grid. WP Grid Builder would supply a query/grid/card layer, taxonomy/field facets, reset and AJAX/pagination if native filtering fails the actual registered-model test. It would not replace CPT/taxonomy registration, field editing, the Single Project template or the URL migration plan. Atomic integration must be tested rather than assumed.

Keep BEAF sliders on detail pages at first; category-filter catalogue cards containing ordinary cover images can link to them. Project services can organize associated comparisons later, but one comparison may have several project/service associations. Do not duplicate BEAF records to categorize them. No slider initialization after AJAX, drag behavior, optional-field empty-state handling or filtered-grid lightbox compatibility was tested; no promise is made about those behaviors.

Sources: [Elementor Taxonomy Filter](https://elementor.com/help/taxonomy-filter-widget/), [ACF registration](https://www.advancedcustomfields.com/resources/post-types-and-taxonomies/), [ACF PRO Gallery](https://www.advancedcustomfields.com/resources/how-to-use-the-gallery-field/), [Elementor field integrations](https://elementor.com/help/which-widgets-support-acf-and-pods-custom-fields/), [WP Grid Builder capabilities](https://wpgridbuilder.com/). Product documentation establishes candidate capabilities, not an installed integration test.

## Separate owner correction during assessment

Residential484 contains an existing third comparison with **BEAF1596** attic mold images but a stale Water/Glenview caption. Changed only heading `efa4830` to **Attic Mold Remediation** and paragraph `2a86831` to **Attic roof sheathing and framing before and after mold-removal work.** Published on staging. Existing genuine Glenview742 card and heading introduction remain valid; no photo, pair, plugin, URL or shared component changed. Mold516, gallery493 and Lombard526 already use1596 in a mold context; no extra rollout needed. No location added to the corrected card.

Saved and rendered text verified in the authenticated frontend. Anonymous HTTP verification returned403, so guest delivery is not certified; authenticated output was current. Private before snapshots remain outside Git. Proof: workspace outputs `attic-mold-caption-fixed.png` and `projects-native-taxonomy-gap.png`. Final design approval belongs to the owner. Revert only the two caption fields if needed; Draft2171 can remain isolated or be trashed later without affecting the catalogue.
