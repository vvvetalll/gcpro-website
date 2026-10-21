# Authenticated production inventory and staging Partner Programs — E73

2026-10-21,America/Chicago. Located the owner's existing Chrome tab `https://gcprochicago.com/wp-admin/`, already authenticated. **Production strictly read-only**: navigated Dashboard/admin content lists, CPT UI registered-types listing, taxonomy lists, Reading Settings and public robots/XML sitemap; read rendered DOM/inline list metadata. No source editor opened, no field typed, no save/publish/delete/purge/install/export-download action or production REST mutation. Staging MCP/native REST remained restricted to `vitaliiv1.sg-host.com`; no staging credential was transmitted to production and no browser session secret was extracted.

## Actual content and status findings

| Production admin content type | Published | Draft | Total |
| --- | ---: | ---: | ---: |
| Pages |88|2|90|
| Posts |30|0|30|
| Portfolio |13|0|13|
| BEAF sliders |33|1|34|
| Elementor templates/global widgets/Kit |57|4|61|
| Post Grid |0|0|0|
| **Observed post objects** |**221**|**7**|**228**|

All list pagination traversed: Pages5,Posts2,Portfolio1,BEAF2,Elementor4,Post Grid empty. Page hierarchy repeats ancestors across pagination; records were deduplicated by native WP object ID (93 raw Page appearances→90 unique). Global-widget rows omit normal inline metadata; titles/statuses were read from visible row labels/classes instead. No Private,Pending,Future or Trash status count was exposed in these All lists. This certifies the current readable admin lists, not permanently deleted/revision/database history, hidden plugin stores or unexposed custom statuses. Media attachments, users, form submissions/customer data and revision internals are not SEO destination Pages and were not exported.

Fresh discoveries absent from earlier public-only Pages inventory:

- **Draft Page15553 — Elementor #15553**, parent0, saved slug empty. [Admin](https://gcprochicago.com/wp-admin/post.php?post=15553&action=edit).
- **Draft Page11856 — Barlett**, parent122(Service Area), saved slug empty. [Admin](https://gcprochicago.com/wp-admin/post.php?post=11856&action=edit). Preserve the exact title; do not assume it is the published Bartlett page or invent an old city URL.
- Draft BEAF8152 Kitchen1, slug kitchen1; Draft templates21215 Elementor Footer #21215,18921 Insurance,16219 Advantages,16214 Advantages. These are source dependencies, not approved new public Pages. No Draft is asserted to have been public previously.

Taxonomies read: News category49(count30),12 post tags,4 project-type terms,5 BEAF gallery terms =22 terms. Project Type includes an empty Mold Removal term73; BEAF Residential term80 is empty. Counts do not prove indexing/history. CPT UI read-only listing confirms Portfolio is public/queryable, has archive, nonhierarchical, show_in_rest and uses project-type; custom UI registers exactly1 type/1 taxonomy. Plugin-owned BEAF, templates and Post Grid were separately inspected. The Elementor library-category URL redirected to the template library, so its internal term inventory remains uncertified; no settings were changed to bypass it.

**Reading Settings now directly verified:** static Front Page40; Posts Page2187(Blog); indexing-discouragement checkbox unchecked. This resolves E13's unauthenticated uncertainty about current `page_for_posts`: Blog is the native posts index. It does not locate/approve historical custom PHP, template conditions or authorize changing routing. Portfolio remains the existing CPT archive with a separate source Page8929; do not manufacture duplicate staging Blog/Portfolio Pages from source Page IDs.

## XML sitemap comparison

Robots advertises `https://gcprochicago.com/sitemap.xml` and sitemap.rss. The current AIOSEO XML index lists **post-sitemap.xml31 URLs** and **page-sitemap.xml83 URLs**; their combined set was read in the browser, not inferred from public REST. Blog appears through the posts sitemap rather than being treated as an ordinary new Page.

Published Pages absent from that combined XML set:

| ID | Title | Observed production URL |
| --- | --- | --- |
|2406|Corporate signatures|https://gcprochicago.com/corporate-signatures2/|
|8136|test2|https://gcprochicago.com/test2/|
|456|Thank you|https://gcprochicago.com/thank-you/|
|15438|Welcome to GCPRO Restoration|https://gcprochicago.com/connect/|

**All13 published Portfolio items are also absent**; their titles/IDs/paths are individually listed in the [complete sitemap](../SITEMAP.md#portfolio--projects) and [reviewed source-object evidence](../evidence/2026-10-21-production-content-objects.json). All30 Posts are represented. Drafts and technical integration records are absent as separate destinations. Absence is a recorded observation, not automatic architecture debt, deindexing proof or an instruction to add everything to XML. No current anonymous HTTP/canonical/indexability sweep was performed; old metadata/HTTP timestamps remain explicit.

## Reconciliation and preservation

The canonical register grows **212→320** rows: **94 newly discovered source-object records +9 taxonomy URL records +5 new staging Partner Pages**. All228 observed production objects are reconciled. Three technical objects(22092 BEAF Mold Removal,10347 BEAF Fasade21-0495-CND,562 Default Kit) already had URL rows; those rows receive observed native IDs/types instead of duplicates. Existing category49's historical `/./news/` identity is preserved; normalized browser link `/news/` is recorded as an observation rather than creating a second term/object row.

New observation columns: production_admin_title/admin_url/current_slug/current_parent_id/observed_view_url/sitemap_status/taxonomy_relationships_json/observed_object_id/observed_object_type and staging_title. Original source identity/content-model decisions stay intact, including Blog/Portfolio special models and already inventoried technical/resource URLs. `production_object_id` is historical mapping; `production_observed_object_id/type` records the fresh exact native identity where prior fields were blank or classified the route differently. WordPress post IDs and term IDs have distinct namespaces.

Unpublished objects with no proven public URL use their admin object identity as inventory_url, leave production_url blank and record observed slug/parent separately. Preview links are not historical public URLs. No new source performance is fabricated; unmatched records explicitly have unavailable metrics. Current public status observations and append-only URL history are updated; all212 previous URL/slug/staging mapping/source-action/proposed/final-destination fields were checked unchanged.

[SEO_URL_INVENTORY.csv](../SEO_URL_INVENTORY.csv) remains the only editable map. [SITEMAP.md](../SITEMAP.md) is a generated human-readable hierarchy/review view covering every320 record, not a second mutable inventory. It includes all91 actual staging Pages, all retained51 cities, all source articles/projects, unmapped source Pages, taxonomies/archives and collapsed technical/history sections. Actual IDs/statuses and uncreated entries are explicitly distinguished. Future KEEP/UPDATE/MERGE/301 REDIRECT/REMOVE/REVIEW decisions remain proposals; no redirect, merge, deletion, removal or existing URL change occurred.

## Staging additions, validation and exact owners

[Partner Programs record](../components/partner-programs.md) owns exact Page982–986/admin/preview/Atomic IDs, source-name evidence, native menu13/items987–991, responsive QA and recovery. All five target Pages are Draft. Prepared native menu has no locations; existing Header uses Primary5 unchanged. Menu metadata saved normally is not publication of target Pages. No new class/Variable/library Component/CSS/JS/plugin/dependency; minimal15 Atomic nodes total.

[Sanitized evidence](../evidence/2026-10-21-production-admin-and-partners.json), [all228 reviewed source objects/22 terms](../evidence/2026-10-21-production-content-objects.json), [saved native structures](../evidence/2026-10-21-partner-atomic-settings.json), [actual preview tests](../evidence/2026-10-21-partner-preview-qa.json). All86 prior staging Page native fields and all prior approved intended paths preserved; Homepage154/Header113/Footer114 saved trees exactly equal before/after. No full website interaction/performance/accessibility regression certification claimed.

Remaining: full program content/design/formal Condo/HOA/commercial brand naming, activation of public Partner navigation only after publication approval, article/CPT imports/archive templates, prior8 URL review holds, any deeper deleted/history or internal-taxonomy audit. Existing GSC/GA4 figures remain historical. No production action or unfinished Page publication is needed to review the completed structure.
