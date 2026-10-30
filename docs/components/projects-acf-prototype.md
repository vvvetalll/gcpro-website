# ACF Free Projects prototype — 2026-10-26

## Archive-only Hero cleanup — 2026-10-30

Archive2232 now uses shared Archive Hero3421/instance2125ae05 in place of serviceHero1318/15cd927e. Existing title **GCPRO Restoration Projects**, factual introduction, existing verified living-area photograph3008. Removed redundant Catalogue Heading71/af429be immediately below the Hero. No Call/Request/emergency/rating elements or empty action wrappers in3421. Filters1835bd2, LoopGridc61e6a3, paginationfacetfc8108f compare byte-for-byte unchanged against the private before snapshot. Card2233/data/URLs/SEO/status and Single Project2231 white opening preserved. Existing native city/service/sector metadata completion remains pending from the previous task, not silently implemented here.

Guest archive and representative case200/oneH1/noindex; Header Request Service retained. Actual authenticated Chrome screenshot confirms the new standard-height Projects Hero/photo/filter bar. This is a desktop visual observation, not a completed keyboard/filter/Load More/mobile regression. [Owners/Overrides](shared-hero.md#archive-hero3421--current-2026-10-30) · [Checks](../evidence/2026-10-30-archive-hero-checks.json).

## Latest native location selections — 2026-10-27

Automatic-membership follow-up: newly Published2755 (Reconstruction19/Commercial24/Schaumburg35) appears beside2666 in existing558 city query without editing the query. Single2231 reused; case gallery has six ordered images and native lightbox Right/Escape verified. [Publication checkpoint](../projects/dash-case-workflow.md#second-schaumburg-case--2026-10-27).

Subsequent checkpoint: Carol Stream543 section2eaef640/slot28d82d4f now queries Project Locations28 with the same native Loop Grid/Card2233. All ten city selections saved. Existing2572 Published after photo/content completion, preserving its path and Single2231. Actual Carol Stream selection verified; native345px Mobile Portrait shows one column/no overflow,20px heading. Existing13 original projects and26 BEAF comparisons unchanged. [Current case checkpoint](../projects/dash-case-workflow.md#carol-stream-draft-completed-and-published--2026-10-27).

Published native Loop Grid selections on Downers Grove527 (term39, slot4ea9dc2c), Elmhurst530 (term36, slot42fc91e1), Highland Park528 (term37, slot630a849e), Oak Brook536 (term38, slot609eec37). Same Card2233; native term queries, no hard-coded case IDs or code. Existing five selections remain; nine total. All four frontend selections show the correct local case/no horizontal overflow. Shared card18px computed on Downers Grove. Existing comparisons preserved. New Project2718 uses Single2231/Hero1318/attachment gallery with six chronological WebP images. [Evidence and unfinished scope](../projects/dash-case-workflow.md#downers-grove-publication-and-local-selections--2026-10-27).

## Owner-authorized cutover and populated review — 2026-10-26

**Current staging state supersedes the isolated-prototype status below.** The owner authorized /portfolio/ cutover, in-place migration preserving IDs/URLs, a temporary official Post Type Switcher, and publication of all existing projects. All **13 original projects2075–2087 are now Published** at their original /portfolio/{slug}/ URLs. Three demonstration clones2234–2236 remain Draft and excluded. Production is unchanged. Owner visual acceptance of the **Single Project design remains pending**; do not describe the current detail design as approved.

- [Live catalogue](https://vitaliiv1.sg-host.com/portfolio/), [Tinley Park detail for design review](https://vitaliiv1.sg-host.com/portfolio/from-ashes-to-excellence-tinley-park-home-restoration/), [newly populated Oak Brook detail](https://vitaliiv1.sg-host.com/portfolio/home-remodeling-oakbrook/).
- ACF CPT2225, key post_type_6adfa31130f30: rewrite slug **portfolio**, archive slug **portfolio**, with_front false. Saved configuration export updated. The native archive has no Page object; Archive2232 controls its presentation. Former catalogue Page1132 is preserved as Draft at portfolio-legacy-preserved, with its original body intact. No competing live Page owns /portfolio/.
- Official Post Type Switcher4.1.1 performed one bulk conversion of only2075–2087; it was subsequently deactivated **and deleted**. IDs/slugs and original publication states were preserved during conversion; the owner subsequently authorized publishing the remaining10. Original nonhierarchical CPT post_parent1132 values are retained as migration history; they do not drive these CPT permalinks. Old Page Single2125 is Draft with no conditions; Single2231 is the only active Project Single.
- Native menu items241/263 now use post_type_archive / gcpro_project, preserving labels, order and hierarchy. Four existing overview buttons on1007/497/498/484 point to /portfolio/. The installed Internal URL selector has no explicit arbitrary CPT-archive picker, and Archive URL is context-only; these four native URL fields are documented exceptions, without numeric Page1132 targets or custom code.

### Presentation owners and editing

- **Single2231:** shared Hero instance1318, one Post Content slot, one **native Gallery driven by Post Image Attachments (post-gallery)**, existing CTA80. Shared Hero1318 itself was not changed. Root local padding0 removes the inherited10px white gutter. Archive2232 root uses the same scoped correction. The ACF location field remains available as project data; the awkward standalone location display was removed from the shared template at the owner’s request. Confirmed locations remain in existing titles/excerpts.
- **Gallery presentation is now global.** One native Gallery in Single2231 controls columns2/2/1, 4:3 proportions, gaps24/24/16, Media File links, lazy loading and native lightbox. Removed all13 body-level Gallery sections; project-specific narrative and existing BEAF sections remain per project. The existing11 gallery media attachments were associated with their corresponding original projects; BEAF image references/files remain intact.
- **Per-project:** title, excerpt, featured image, native body, confirmed location, service/sector assignments and optional existing BEAF references. Upload project photos as media attached to that Project; reusing an existing Library item requires its native **Attach to / Uploaded to** relationship to point to the Project. Uploading only to the unassociated Library does not include it automatically. An attachment has one parent; this free approach is not a curated Gallery field or an arbitrary reusable ordered image selection.
- **ACF Free is sufficient for the tested global-gallery workflow.** The native Post Image Attachments source was runtime-tested on Oak Brook16 photographs, then centralized and checked on all13 projects/222 photographs. This supersedes the earlier assumption that global Gallery presentation necessarily requires PRO. ACF PRO would be justified for a project_gallery field with explicit drag-and-drop ordering, per-project curated selection and reuse of the same media across project galleries without changing attachment parents. Elementor exposes ACF Gallery Field, but PRO is not installed and that integration was **not runtime-tested**. If that workflow is desired, use official ACF PRO Personal (one-site license); confirm staging-license treatment for sg-host.com with ACF. No purchase is required for the demonstrated implementation.
- **Card2233:** photo, semantic H3 title and existing Blue Outline button59 only. Removed service/location excerpt at the owner's request. Caption5211cef6 is a flex column with grow1 and existing16px gap; native real action wrapper1d8b6d21 uses margin-top:auto and padding0. Buttons align along the row bottom without fixed mobile heights. One template owns all query cards.
- **Archive2232:** one content-width owner4bd14a99; native service tabs left, orange active underline; native All/Commercial/Residential segmented selector right. Native Taxonomy Filters still control LoopGridc61e6a3. Six per page, native Load More, 3/2/1 columns, no project-ID lists. Load More uses native Inter16/600 uppercase, navy thin outline,8px radius,14×28px padding,32px top gap and navy/white hover. No custom CSS/JS, HTML widgets, snippets or new runtime dependencies were introduced.

### Content and verification

- Imported **211 verified production gallery photographs** for the10 unfinished original records, inspected in contact sheets before factual metadata/covers were selected. New staging WebP derivatives max1600px total approximately21.8MB; no existing file was renamed/replaced/deleted. Existing11 photographs on the original three complete projects were reused. Location was omitted for both Helen Berkun projects rather than invented. Existing Western Spring spelling/path was retained; no inferred damage causes were added to renovation projects.
- [Sanitized record](../evidence/2026-10-26-projects-cutover.json): all13 original IDs/slugs retained, all13 anonymous browser-UA URLs200/noindex, one H1 each, one shared Gallery owner2231,222 gallery items total. Bodies contain zero Gallery widgets. Before & After493 saved tree matches its scoped before snapshot;26 comparisons and vendor integration are preserved.
- Actual frontend: Load More6→12→13; Fire→West School/Tinley; Commercial→Green Oaks/club; Fire+Commercial→native empty message; All services/All reset. Enter/Space operated filters. New publications entered the automatic query without editing IDs; the earlier controlled Draft lifecycle test remains valid for the unchanged native query. Draft clones remain absent.
- Card render has no excerpt paragraphs; first-row button bottoms match. Desktop and393px mobile emulation show no horizontal overflow and3/1 columns. Previous820px2-column test applies to the unchanged responsive grid setting. Native lightbox opens the attached photographs; ArrowRight changed16/16→1/16 and Escape closed it. No physical-device/screen-reader certification. [Actual desktop result](../evidence/2026-10-26-portfolio-cutover-desktop.png).
- Guest403 comparison: anonymous default script UA received nginx403; the same URL with a browser UA received200. Browser-UA anonymous and authenticated HTML hashes matched in the focused comparison. This demonstrates UA-dependent delivery, not an identified security-rule cause. No protections were weakened. Real UI verification used the existing logged-in browser, so separate anonymous JavaScript interactions are not certified.
- Cleared Elementor Files & Data and staging SG cache when stale generated output was observed. Corrected inherited page-template assignments to Default so newly migrated Projects actually use Single2231. Do not mistake saved metadata alone for rendered verification.

### Minimal project-page direction selected by owner

The owner selected the Helen Berkun exterior page as the simple baseline: Hero, short overview, project photographs and existing contact CTA. Simplified the earlier Tinley2077, Wonder Lake2078 and club2079 bodies to one short overview; removed redundant The Work/The Result sections and associated extra service buttons. Preserved all four existing comparison shortcode instances on2077/2078. Removed standalone location container657b92ef from Single2231; the location ACF data is retained. Native frontend Tinley shows no location line,4 Gallery photographs, preserved comparisons and no overflow. [Current simple page](../evidence/2026-10-26-project-simple.png). Further sections can be added later; the owner retains final visual acceptance.

### Maintainability, remaining review and recovery

Current owners are ACF model/fields, Single2231, Gallery in2231, Card2233 and Archive2232. Removed competing body Gallery owners and retired Page Single2125. No migration plugin remains. Fire service-query Section2257 remains a tested native term-query pattern; **automatic selections have not yet been rolled out across existing service pages**. Existing service BEAF sections were preserved. Final detail-page visual design and any service-selection rollout remain the next review stage; no claim of complete site-wide rollout.

Recovery: private scoped snapshots retain the13 original Pages, legacy catalogue1132, old Single2125, new templates and attachment parents outside Git. Restore catalogue1132 routing/conditions and use an explicitly authorized in-place reverse conversion if undoing migration; never disable ACF before preserving CPT data. The private raw snapshots/authentication data are not committed. The canonical URL inventory preserves every previous row and records this staging-only migration in each affected history.

---

Implemented on staging under the owner's explicit ACF Free installation authorization. This supersedes the earlier no-install capability assessment; it does not authorize migration. Official `advanced-custom-fields/acf` **6.8.10** is active alongside Elementor **4.3.5 / Pro 4.3.2**. No PRO, WP Grid Builder, other dependency or custom runtime code was installed.

## Configuration and ownership

| Owner | Actual configuration |
| --- | --- |
| ACF → Post Types → Projects | `gcpro_project`, public/nonhierarchical, REST enabled, title/content/excerpt/featured image/revisions/custom fields. Elementor editing enabled for this CPT. Temporary single rewrite and archive: `projects-prototype`; `with_front=false`. |
| ACF → Taxonomies → Project Services | `project_service`, hierarchical, attached only to Projects, REST enabled. Fire17, Water18, Reconstruction19, Mold20, Storm21, Contents22. |
| ACF → Taxonomies → Project Sectors | Separate `project_sector`, hierarchical, attached only to Projects, REST enabled. Residential23 / Commercial24. Commercial is not a service term. |
| ACF → Field Groups → GCPRO Project Details | `group_gcpro_project_details`, Projects-only. Optional text `project_location` (`field_gcpro_project_location`); optional multiple Post Object `project_beaf_references` (`field_gcpro_project_beaf`), restricted to existing Published `bafg` records, returned as IDs. |
| Single Project2231 | Published; condition **`include/singular/gcpro_project`**. Shared Hero1318 with dynamic title/excerpt/featured image; optional ACF location paragraph; exactly one Post Content; existing CTA80 with native Service Request492 and telephone. |
| Archive2232 | Published; condition **`include/archive/gcpro_project_archive`**, selected through actual native Display Conditions. `/projects-prototype/` only; `/portfolio/` unchanged. |
| Loop item2233 | Published; one Atomic article root. Existing `ba-card`, `ba-card__caption`, `ba-card__title`, 4:3 dynamic cover, post title/excerpt and Blue Outline59 with dynamic Post URL. No manual project IDs. |
| Service selection2257 | Published internal saved Section, no display conditions/site-wide placement. Native Loop Grid + same2233 card, Projects source, Include By Term → **Project Services: Fire**. Reusable automatic selection pattern; not deployed to existing service pages. Change the assigned term through native Query controls. |

[Portable ACF native JSON export](../config/acf-projects-prototype.json) contains the field group, CPT and both taxonomies. It contains no project content or credentials. Import via ACF → Tools only for recovery/another approved environment; do not import twice into the working site blindly. Term assignments remain native WordPress taxonomy data.

Archive tree: shared Hero1318 + Heading71 (`section-heading--accent`), followed by native Container1835bd2. Service Taxonomy Filter17c6407 and sector Taxonomy Filter59956a5 target Loop Gridc61e6a3. Source **Projects**, no manual include list; six items/page, native **Load on Click** pagination. Services and sectors have separate All reset controls, single selection, hidden empty terms, wrapping on mobile. Grid is3/2/1 columns. Native controls use existing `--container-max`, page-gutter, spacing and navy/white/border/orange variables; filter text uses the existing Inter family. Normal/active/hover states remain editable in Elementor. No CSS/JS/PHP storage or Custom Code entry was added.

The native empty message is **“No published projects match this selection.”** After cleanup there are no Published CPT projects, so the archive intentionally shows this empty state. The populated screenshots record the controlled test, not the current publication state.

## Editing workflow and global boundary

Add Project → enter verified title, excerpt, featured image, optional confirmed location and existing BEAF references → assign services and sector → enter project content/photo Gallery in Elementor → publish. Published projects enter archive and matching term queries automatically; Drafts stay excluded.

**Global:** Single2231 controls Hero, cover presentation, location metadata, Post Content position and final CTA. Card2233 controls every native catalogue/selection card. Archive2232 controls catalogue/filter presentation. Changing these owners updates their consumers without editing each project.

**Per project:** narrative and native Elementor Gallery are inside Post Content; Gallery selection/order/layout/lightbox controls remain editable in that project's body. This free solution does not centrally control each body Gallery's internal layout. Reuse the representative body as an editing starting pattern; do not duplicate catalogue membership lists. Title/excerpt/cover/taxonomies/ACF fields remain native project data.

Optional BEAF Post Object references are organizational metadata, not an automatic slider renderer. Existing native body Shortcode widgets render the selected comparisons on detail pages only. The example retains the source project's two body comparisons; empty references create no template section because no unconditional BEAF heading/renderer was added. No sliders were placed in AJAX-filtered cards.

## Representative records

| CPT item | Source preserved Page | Final status and preview |
| --- | --- | --- |
|2234 Home Restoration — Tinley Park, IL; Fire/Reconstruction, Residential; location Tinley Park, IL; BEAF1200/1205|2077|**Draft** — [editor preview](https://vitaliiv1.sg-host.com/?post_type=gcpro_project&p=2234&preview_id=2234&preview=true)|
|2235 Water Damage Reconstruction — Wonder Lake, IL; Water/Reconstruction, Residential; BEAF1199/1204|2078|**Draft**, retained controlled-test fixture; no Published test content left|
|2236 Club Interior Reconstruction — Chicago, IL; Reconstruction, Commercial; no confirmed BEAF association|2079|**Draft**, retained controlled-test fixture. Location restored to Chicago, IL after empty-field test|

Verified source narratives, featured images and body Gallery selections were reused without importing/replacing media or migrating the original Pages. Temporary project paths live under `/projects-prototype/`; no original project path is claimed by this CPT.

- [Temporary archive](https://vitaliiv1.sg-host.com/projects-prototype/).
- [Archive template preview](https://vitaliiv1.sg-host.com/?elementor_library=gcpro-projects-archive-prototype&preview=1&theme_template_id=2232).
- [Single template preview](https://vitaliiv1.sg-host.com/?elementor_library=gcpro-single-project-cpt-prototype&preview=1&theme_template_id=2231).
- [Saved service-selection preview](https://vitaliiv1.sg-host.com/?elementor_library=gcpro-projects-by-service-fire-prototype&preview=1&theme_template_id=2257).

Draft and template previews require a logged-in WordPress editor. Use the sample project's preview for the actual shared detail design; a bare Single-template preview may use a different editor preview context.

## Focused verification

Authenticated real frontend, desktop browser and viewport emulation:

- Three temporary Published CPT projects entered the automatic query. Fire → Tinley; Water → Wonder Lake; Commercial → Chicago; Fire+Commercial → zero; Fire+Residential → Tinley; Water+Residential → Wonder Lake; both All resets → three. Sector was tested independently before combined filters. Mobile Water filter returned Wonder Lake.
- Wonder Lake Published → Draft removed it on refresh (two cards); republishing restored all three without editing query IDs. Final cleanup returned **all2234/2235/2236 to Draft**.
- Native Include By Term → Fire returned Tinley only; saved as reusable Section2257, then restored the archive's unfiltered Projects query. No existing service page changed.
- Load on Click tested with two items/page: initially two, Load More appended the third and removed itself at the end. Final page size restored to six.
- All three dynamic cover/button URLs matched their CPT objects. Clicking Tinley opened its correct detail page under shared Single2231. Service Request links resolve to the existing page; telephone remains `tel:+18476563322`. Corrected an inherited CTA placeholder in this new template instance only.
- Native Gallery opened four full-size images. Next advanced2/4→3/4; close worked on desktop and mobile. Existing Gallery UI: Grid, Media File, Lightbox Yes, 4:3, native responsive columns. This is an actual supported Gallery, not static thumbnail fallback.
- Cleared Chicago optional location and references: metadata wrapper measured **0px**, empty paragraph0px, no blank section. Restored confirmed location afterward.
-1440 desktop /820 tablet /393 mobile: grid3/2/1, no horizontal overflow. Mobile filters wrap; sample detail/gallery stay within viewport. Screenshots: [desktop](../evidence/2026-10-26-acf-catalogue-desktop.png), [mobile](../evidence/2026-10-26-acf-catalogue-mobile.png). These show the temporary populated test.
- Staging SG cache was purged after stale archive output appeared. Anonymous HTTP checks for archive/sample returned **403**; guest delivery/interaction is therefore **not certified**. Authenticated real frontend was verified. No staging noindex settings were changed; toolbar still reports Search Engines Blocked. No physical-device/screen-reader certification.
- Original1132/2077/2078/2079 paths/status/template/native bodies unchanged against scoped before snapshots. Before & After493 native body and saved raw content unchanged, still **26 shortcode comparisons**. Rendered493 output differs dynamically, not its saved content. No original slider records/settings/plugin files were edited.

Owner performs final visual acceptance. All test items remain recoverable Drafts; catalogue becomes populated when approved actual CPT projects are published. Frontend guest delivery403 remains the concrete verification limitation, not evidence that native filtering failed.

## ACF Free vs PRO

**Free is sufficient for the demonstrated workflow**, with a native Gallery edited within each project body. Actual Gallery Dynamic Tags menu lists **ACF → ACF Gallery Field**. ACF Gallery is a PRO-only field, so no such field was created and its dynamic binding/runtime was **not tested**. The menu entry proves installed Elementor offers the integration, not that ACF Free supplies the field.

There is no demonstrated reason to buy PRO for the agreed content-Gallery solution. A concrete future reason would be requiring editors to manage an ordered Gallery in the ordinary project fields while one Gallery widget in Single2231 controls all project galleries centrally. That removes body-level Gallery setup and may materially improve a high-volume workflow; it requires a separately authorized PRO purchase and actual field/empty-state/runtime test. WP Grid Builder is not needed by the tested native service/sector filtering and does not supply the content model or Single template.

## Migration and recovery

The [URL-preserving cutover plan](projects-architecture-assessment.md#url-preserving-migration-plan--not-executed) remains **unexecuted**. Page1132 owns `/portfolio/`; do not enable a competing CPT archive there. A future approved cutover must snapshot/retain1132, resolve archive slug ownership and menu references, preserve original project slugs/IDs through an explicit in-place migration method and verify every full original URL. ACF registration does not migrate existing Pages automatically.

Recovery: unassign2231/2232 and remove any placed2257 instance; leave project records Draft. Export/recover CPT data before disabling ACF (its deactivation removes registration, not a safe content migration). Do not delete ACF fields, original Pages, media or BEAF to withdraw this prototype. Private scoped backups remain outside Git.

## Global minimal Elementor lightbox — 2026-10-26

Owner requested the setup globally, then explicitly chose to retain native gallery arrows. Native **Site Settings → Lightbox**, active **Kit6**, is the single configuration owner. Disabled Counter, Fullscreen, Zoom and Share (lightbox_enable_counter/fullscreen/zoom/share are empty switcher values); Title and Description set to None (lightbox_title_src/lightbox_description_src empty). Image Lightbox remains enabled. The upper toolbar contains only Close; native previous/next controls remain. No CSS/JS, new component or plugin was added. Applies to standard Elementor image lightboxes site-wide, respecting existing per-widget enable/disable choices; BEAF vendor popup settings/files are untouched.

Saved through the actual native editor and read back Kit6. Tinley Gallery opened with Close and previous/next controls, without counter, extra tools or captions.393px mobile emulation: no horizontal overflow and close remains within the viewport; Escape closes the overlay. Cleared staging SG cache after the global change. [Actual desktop lightbox](../evidence/2026-10-26-minimal-lightbox.png). No new full-site audit or physical-device test. Recovery: restore the four switchers and the former Title/Description sources in the same native panel; scoped Kit backup is private outside Git.

## Project Gallery image resolution — 2026-10-26

Owner reported blurred project-gallery photos. Shared Single2231 → Gallery89b76dd3 was using native default Image Resolution **Medium**, rendering300px derivatives in approximately546px desktop tiles. Changed **Image Resolution → Full** through the visual editor; saved thumbnail_image_size:full. Applies to all Project galleries through their existing Single template. No images/files/URLs were replaced or recompressed; layout, crops and minimalist lightbox are preserved. Native serialization omitted several default-valued settings; actual desktop2-column/mobile1-column behavior and media links remain correct.

Verified actual Tinley background/data-thumbnail URLs now reference the existing1200–1600px full files instead of300px derivatives; lightbox opens and Escape closes.393px mobile: one column, full sources, no overflow. A second project's anonymous HTTP200 gallery also contains full URLs with no300px suffixes. Cleared staging SG cache. [Actual gallery](../evidence/2026-10-26-project-gallery-full.png). Full means the highest available uploaded source, not fabricated extra detail. Recovery: choose Medium again in this same native control; private scoped Single backup retained outside Git.


### DASH publication checkpoint — 2026-10-27

Single2231 remains the presentation owner; each case owns narrative, native title/excerpt/featured image, Services/Sector/Location terms and attached image gallery files. New Published2580/2596/2604/2612/2624. Naperville532 LoopGridc095b66 queries Location31, shared card2233, four desktop columns (2 tablet/1 mobile). Empty optional BEAF references retained. No new code/dependency or shared layout duplicate. [Current case checks and limits](../projects/dash-case-workflow.md#active-publication-checkpoint--2026-10-27).


### Case batch checkpoint — 2026-10-27 21:21 UTC

[Actual case statuses, photo counts, native selection owners and limitations](../projects/dash-case-workflow.md#published-case-and-selection-checkpoint--2026-10-27-2121-utc). Shared Card2233 native local styles refined; Archive2232 location filter removed only. Geo query owners:532/526/533/556/558, each native location-term query with Card2233. Existing BEAF retained; six-photo backfill and remaining geo selections pending.


### Highland Park content checkpoint — 2026-10-28

Project2765 reuses Single2231, Gallery89b76dd3 and Card2233 unchanged. Highland Park528/LoopGridd426b2d automatically selects Location37; its Heading71 instance33ebb33d description now covers both published case scopes. Per-project content/media/SEO remain individual. [Actual tests](../projects/dash-case-workflow.md#highland-park-fallen-tree-reconstruction--2026-10-28).


### Highland Park four-case checkpoint — 2026-10-28

Native528/LoopGridd426b2d queries Location37 and now renders four projects automatically. Heading71 instance2e762973 replaces33ebb33d within existing accent wrapper609e51b2 with updated description. No query/card/shared template changes. [Actual cases and checks](../projects/dash-case-workflow.md#highland-park-reaches-four-cases--2026-10-28).


2026-10-28: Project2818 published using existing Single2231/Gallery89b76dd3/Card2233. Body76808999, Heading71 instance14d3d1ec, Button59 instances2d182849/437d7702/19d19e6f bind named Northbrook556/Water514/Reconstruction518. Six attached final-only media2820–2825; automatic556 Location34 selection verified with two cases. No shared design/query/code changes. See DASH workflow checkpoint.

2026-10-28: Project2828 body e76c1e1, Heading71/three Button59 named bindings556/514/518; shared Single2231/Gallery/Card unchanged. Media2830–2835, two Before then four final. Actual Northbrook556 Location34 selection contains three cases; frontend H1/gallery/links/noindex/overflow checked.

2026-10-28: Published2837 body5f03907e/Heading71/Buttons59 named527 and523; media2839–2844. Single2231/Gallery/Card unchanged. Automatic527 Location39 query shows two cases. Existing section-heading instance replaced within wrapper4592cb3d, new3c173548, for both scopes. No shared definition or query/layout code change.

2026-10-28: Published2847 body74563a4e, Heading71 and named Button59 links543/516; six attached WebP2849–2854. Existing543 Location28 query automatically shows two cases. Shared Single2231/Gallery/Card unchanged.527 heading3c173548 saved new description verified in MCP, frontend remains older after SG toolbar purge/reload; native render-cache follow-up pending, no new code.


### Lombard2856 publication — 2026-10-28

Native body/Heading71/Buttons59; Single2231, attachment Gallery89b76dd3 and Card2233 unchanged. Location32 automatically includes2856 alongside2624. Six chronological WebP images and saved SEO/taxonomy; actual desktop H1/gallery/links/noindex/overflow verified. No layout/code/dependency changes. [Evidence](../projects/dash-case-workflow.md#second-lombard-case--2026-10-28).


### Elmhurst2865 publication — 2026-10-28

Existing shared presentation preserved; native body/Heading71/Buttons59. Location36 query automatically includes2865 and2679. Six chronological WebP images; saved SEO/taxonomy and actual desktop H1/gallery/links/noindex/overflow verified. No new component/code/dependency. [Checkpoint](../projects/dash-case-workflow.md#second-elmhurst-case--2026-10-28).


### Glenview2874 publication — 2026-10-28

Existing shared Single/Gallery/Card retained; native body/Heading71/Buttons59. Location33 query automatically includes2874 and2632. Six chronological WebP images; actual desktop H1/gallery/links/noindex/overflow verified. No code, layout or dependency change. [Checkpoint](../projects/dash-case-workflow.md#second-glenview-case--2026-10-28).


### Commercial Elmhurst2883 — 2026-10-28

Shared Single/Gallery/Card retained, native body/Heading71/Buttons59. Location36 now automatically includes three cases. Six chronological WebP images and actual desktop H1/gallery/links/noindex/overflow verified. Rejected2890 detached/preserved. No component, layout, code or dependency change. [Checkpoint](../projects/dash-case-workflow.md#third-elmhurst-case-commercial-offices--2026-10-28).


### Lombard attic2894 — 2026-10-28

Existing shared owners unchanged; native body/Heading71/Buttons59. Location32 automatically includes three cases. Six chronological WebP images; saved content/metadata and actual desktop H1/gallery/links/noindex/overflow verified. No code/dependency changes. [Checkpoint](../projects/dash-case-workflow.md#third-lombard-case-attic-surfaces--2026-10-28).

### Northbrook patio2903 — 2026-10-28

Existing shared owners unchanged. Native body/Heading71/Buttons59, Reconstruction19/Location34. Six final WebP images; actual desktop H1/gallery/links/noindex/overflow verified. Automatic city selection now has four cases. No code/dependency change. [Checkpoint](../projects/dash-case-workflow.md#fourth-northbrook-case-patio-drainage--2026-10-28).

### Glenview parapet2912 — 2026-10-28

Existing shared owners unchanged. Native body/Heading71/Buttons59, Reconstruction19/Commercial24/Location33. Six chronological WebP images; actual desktop H1/gallery/links/SEO/noindex/overflow verified. Automatic city selection now has three cases. No code/dependency change. [Checkpoint](../projects/dash-case-workflow.md#third-glenview-case-parapet-membrane--2026-10-28).

### Schaumburg kitchen2921 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59, Water18/Reconstruction19/Residential23/Location35. Six chronological WebP images; actual desktop H1/gallery/links/noindex/overflow verified. City selection now has three cases. No code/dependency changes. [Checkpoint](../projects/dash-case-workflow.md#third-schaumburg-case-kitchen-and-interior--2026-10-28).

### Lombard siding2930 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59, Storm21/Reconstruction19/Residential23/Location32. Six chronological WebP images; actual desktop H1/gallery/links/SEO/noindex/overflow verified. City selection now has four cases. No code/dependency changes. [Checkpoint](../projects/dash-case-workflow.md#fourth-lombard-case-storm-siding--2026-10-28).

### Elmhurst overflow2939 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59 named530/514/518. Six chronological WebP images; saved bindings and actual desktop H1/gallery/links/noindex/overflow verified. Automatic Location36 selection now has four cases. No code/dependency changes. [Checkpoint](../projects/dash-case-workflow.md#fourth-elmhurst-case-bathroom-overflow-repairs--2026-10-28).

### Carol Stream commercial2948 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59 named543/499/518. Six final-condition WebP attachments. Saved binding and actual desktop H1/gallery/links/noindex/overflow checked. Automatic Location28 selection now has three cases. No custom code/dependency changes. [Checkpoint](../projects/dash-case-workflow.md#third-carol-stream-case-commercial-tenant-improvements--2026-10-28).

### Glenview ice-dam repairs2958 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59 named533/514/518. Six chronological WebP images. Saved bindings and actual desktop H1/gallery/links/noindex/overflow verified. Automatic Location33 selection now has four cases. No new code/dependencies. [Checkpoint](../projects/dash-case-workflow.md#fourth-glenview-case-ice-dam-interior-repairs--2026-10-28).

### Schaumburg frozen-pipe repairs2967 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59 named558/514/518. Six chronological WebP images. Saved bindings and actual desktop H1/gallery/links/noindex/overflow checked. Automatic Location35 selection now has four cases. No new code/dependencies. [Checkpoint](../projects/dash-case-workflow.md#fourth-schaumburg-case-frozen-pipe-reconstruction--2026-10-28).

### Carol Stream completion repairs2976 — 2026-10-28

Shared owners unchanged; native body/Heading71/Buttons59 named543/514/518. Six chronological WebP images. Saved bindings and actual desktop H1/gallery/links/noindex/overflow verified. Automatic Location28 selection now has four cases. No new code/dependencies. [Checkpoint](../projects/dash-case-workflow.md#fourth-carol-stream-case-drain-backup-repair-completion--2026-10-28).

### Downers Grove bathroom/interior repairs2985 — 2026-10-28

Shared owners unchanged. Native body/Heading71/Buttons59 named527/514/518, six WebP gallery attachments; actual desktop H1/gallery/links/noindex/overflow checked. Automatic Location39 selection now has three cases. No new code or dependencies. See latest dash-case-workflow checkpoint; mobile/lightbox/guest not retested.

### Downers Grove roof/interior repairs2994 — 2026-10-28

Shared owners preserved. Native Heading71/Buttons59 named527/514/518, six WebP gallery attachments. Saved settings plus actual desktop H1/gallery/links/noindex/overflow checked. Automatic Location39 query now has four. No new code/dependency; mobile/lightbox/guest not retested.

### Oak Brook home remodel3003 — 2026-10-28

Shared owners preserved; native Heading71/Buttons59 named536/518, six WebP attachments. Actual desktop H1/gallery/links/noindex/overflow checked. Automatic Location38 query now two. No new code/dependencies; original BEAF preserved. Mobile/lightbox/guest not retested.

### Oak Brook mold mitigation3012 — 2026-10-28

Shared owners unchanged; native Heading71/Buttons59 named536/516, six WebP attachments. Saved bindings and actual desktop H1/gallery/links/noindex/overflow checked. Location38 query now three. No code/dependencies/BEAF changes. Mobile/lightbox/guest not retested.

## Catalogue navigation and compact cards — 2026-10-28

Owner installed WP Grid Builder2.3.6; official Elementor add-on1.4.0 activated on staging. Archive2232 remains the sole catalogue owner and uses native Loop Grid c61e6a3 with Card2233. Replaced native taxonomy widgets with WPGB Service1, Location2, Property type3 and Reset4; native Load More5 is the only pagination owner. Elementor pagination is None. No custom filtering code, new query-ID lists or duplicate catalogue was introduced. Native index rebuilt:183 rows, queue empty at checkpoint.

Native WPGB Styles1/2/3 own dropdowns, Load More and Reset respectively. Inter13px labels,15px fields,14px actions; existing navy/border/orange colors. Reset has orange outline/text and white text on orange hover. Equal field/reset heights measured51.78px. Native Container1835bd2 owns pale-blue panel,24px padding,12px corners,16px field gap and responsive column stacking; fields27% desktop/full-width mobile. Load More widget fc8108f centered below the grid. Owner changed desktop grid to4 columns, tablet2/mobile1;8 initial results. Facet6 result counter is prepared but not connected: it did not appear in the add-on widget selector after native save/reload. Do not claim that the visible counter works.

Card2233 remains the shared archive/geo card. Whole card is one native post-URL anchor: image, title and View project text open the same case, one keyboard stop, no nested links. H3 draws from optional ACF Catalogue Title, key field_6ae2548010fbd / project_card_title in existing Group2228, populated for52 published projects without changing H1s, SEO titles or slugs. Fill this field for future projects; dynamic post-title fallback is not implemented. Native title18px desktop/tablet,17px mobile. Removed oversized Button59 instance; native paragraph3b612ec is14px semibold, pointer cursor, compact orange underline. Earlier text-link class imposed44px minimum height and default text cursor; detached only from this action and replaced with native local controls. Final saved action has no Custom CSS. No shared BEAF card class was changed.

Separate taxonomy location metadata remains incomplete: Atomic dynamic tags omit Post Terms; a native V3 Post Info/Title trial inside the Atomic caption did not render the location. Removed the trial rather than maintaining duplicate location text or changing taxonomy publication behavior. Do not claim this requirement complete.

Actual authenticated browser tests: original Elementor Fire→All→Load More reproduced six unchanged cards and disappearing button; generated next URL pointed to a case/2/ rather than the catalogue. WPGB6→12 yielded12 unique case URLs. Fire returned the four expected cases. After Reset, Load More again yielded12 unique cases. Direct click on View project opened the correct Oak Brook case. Final readback8 cards and exactly one Load More button; action pointer cursor and compact24.89px height verified. Full combined/empty/keyboard/mobile/guest regression remains pending; unauthenticated HTTP previously403, no security changes. New8-item pagination has not received the full earlier6-item test sequence. Do not certify all requirements complete.

Recoverable pre-edit templates/projects and component1345 snapshots are private outside Git. Native configuration snapshot: [projects-catalogue-facets.json](../projects/projects-catalogue-facets.json). Owner paused further design work to resume missing DASH cases. No case was added by this interface checkpoint.


### 2026-10-29 — Plain card typography and compact navigation action

Owner rejected the heading treatment and orange-underlined View project action. Shared Card2233 title763eccfb now uses existing font-body/Inter,500 weight,18px desktop/tablet and17px saved mobile,1.45 line-height and existing gray text token. Semantic H3 and ACF Catalogue Title binding remain; no project display copy, H1, SEO title, slug or URL changed. Action3b612ec now uses compact14px Inter500,8×12px padding,36px minimum height,6px corners and a fine border-color token frame. Native hover becomes navy with white text. Removed the orange underline. It remains inside the sole native post-URL card anchor, with no nested links or extra keyboard stops. Both changes are native local Atomic controls; no new element/class/code/dependency.

Private before/after backup retained outside Git. Native MCP staged the change but returned save_error for this Loop Item; publication completed in the native Elementor editor. Readback confirms only the two intended nodes differ, no added/removed nodes. Actual authenticated catalogue frontend confirms Inter18px/500 headings, Inter14px framed actions, no horizontal overflow and no nested anchors. Clicking the action itself reached the intended Oak Brook case. Existing photos,4-column grid, filters and Load More were untouched. Native360px editor preview had no overflow but lacked a representative visible dynamic action; full mobile frontend/guest regression was not certified. Owner visual acceptance pending.

## Focused guest audit — 2026-10-29

Archive2232/Loop c61e6a3 and shared Card2233 remain the only catalogue/card owners. Fixed two real empty-state issues with native controls: facets1/2/3 Show Empty Choices=true retains the selected zero-result value while disabling unavailable choices; globally unindexed locations remain absent. Disabled Elementor's additional Nothing Found message and set the WPGB message to “No published projects match this selection. Try another filter or clear your filters.” Exactly one message, selected Fire+Commercial retained, zero cards and no Load More verified.

Guest functional test: Fire4; Fire+Lombard1; +Residential1; Naperville4; Commercial7; Fire+Commercial0; All/reset; Water8→14→20→22 exact unique cases; complete All8→14→20→26→32→38→44→50→52 exact unique Published cases and no Drafts. Reset/Load More rechecked after empty-state changes:14 unique. Initial8, append6 is the existing supported WPGB configuration, not a skipped-results defect. Keyboard dropdown End/Enter retained focus on Service and updated Storm; Tab moved to Location. Mobile one column,17px title and no overflow. Shared gallery/lightbox opened full images, ArrowRight advanced and Escape closed on the representative Naperville case. Guest HTTP68 affected pages returned200/noindex; historical403 not reproduced and its original cause is not established.

Latest owner follow-up: title763eccfb uses ordinary Inter/body400,18px desktop/tablet and17px mobile. Native style only; action and layout untouched. Native editor publication/readback and guest geo render400 verified. Future optional short-title fallback and separate taxonomy location metadata remain unfinished as previously recorded; all52 current Published cards have explicit display titles. No new workaround added.

All10 geo loops resolve to their own assigned location: nine show4 current cases, Oak Brook3. Existing BEAF/older proof blocks remain separate. Each page retains one inset mid-page CTA after projects and one final CTA after FAQ. No project content, taxonomy assignments or URL/status changes.


### 2026-10-29 — Resources follow-up

Resources consistency2026-10-29: shared Card2233 action3b612ec uses restrained14px Inter500, no decorative underline/frame, native180ms translate/color hover; it remains a span inside the unchanged whole-card native anchor. No case/query/taxonomy/URL changes.

## Coordinated editorial Single Project opening — 2026-10-30

Owner explicitly authorized replacing the service-style Hero inside Single2231 only. Removed Component1318 instance32716b73 from that template; **shared1318/1453 definitions and service/geo Hero consumers untouched**. Native Atomic Opening45461274 is now first under root7c74f8e3. Container2f0173dd reuses container/stack/page gutters; breadcrumb2c811cb3 links Home through native Content154 and Projects through actual `/portfolio/` CPT archive route (there is no corresponding Published Page to bind). Type label60dacd90, dynamic H1a5c3ba4, native excerpt7b3ea96c without content fallback, then dynamic full featured image52cb2be4. White background, normal-case40/34/28px H1,18px introduction, max900px title and max1040px/fluid220–360px-high photograph. No emergency mark, review widget or conversion buttons in the opening.

Existing Post Content69a2b5bf remains sole native body slot; its existing template-scoped typography/link exception is the only project body styling owner. Existing Gallery89b76dd3, all attachment membership/chronology, gallery heading, BEAF integrations and final inset CTA1412a38b retained. No project body, title, SEO title, slug, publication status, taxonomy, image or date was edited. REST comparison of all52 Published Projects against the private before snapshot found zero changes in those fields. No extra cover added inside bodies/galleries.

**Unfinished requirement:** verified city/state and Services/Sector metadata still need native Post Info configuration in Single2231. These are `project_area`, `project_service`, `project_sector`; reuse them, do not independently fill duplicated `project_location` values. The connector lacks Post Info and Atomic text's dynamic schema excludes Post Terms. Elementor itself has native Post Info (already used on Archive124); this is a connector limitation, not missing Elementor capability. Repeated Chrome input-guard failures prevent visual-editor configuration. No hard-coded term lists, custom renderer, extra fields/plugins or empty hidden metadata placeholder were left behind. Omit missing values in the eventual native rows; do not derive locations from title text.

Guest HTTP checks on two legacy gallery projects2075/2076, long-title remodel3003 and mitigation3012 confirm200/oneH1/noindex/selfcanonical/one masthead photograph/no masthead sales widgets. Rendered lightbox-enabled anchors remain16/12/6/6 respectively. These are HTML/settings checks, **not** new browser lightbox/keyboard/crop/mobile acceptance. Actual browser work remains blocked by Chrome simultaneous-input guard despite owner authorization; prior task's lightbox pass is historical, not validation of this redesign. [Checks](../evidence/2026-10-30-editorial-template-checks.json).

Review examples: `/portfolio/oak-brook-kitchen-living-spaces-home-remodel/` and `/portfolio/oak-brook-mold-affected-basement-walls-opened-dried/`. Native template preview returned an unrelated Post context; use actual project URLs for accurate review. Rollback: remove45461274 and restore1318 instance/overrides from private Single2231 snapshot; restore only affected Post Content style owner. Original gallery/body/CTA nodes were preserved. Header/Footer, archives/facets, production and noindex unchanged by this template replacement.


### 2026-10-30 — Card consistency requested; save failure remains

Owner requested Project Card2233 visually match Article Card3133. Inspected current owners: both are single native post-url anchors, but2233 has inset4:3 photos,16px/400 title and left action, while3133 has edge-to-edge photos,20px/600 title, subtle shadow and bottom-right action. Proposed retaining project4:3 images and existing ACF short titles, with shared visual rhythm, compact18px headings and whole-card arrow hover/focus. No content/query/filter/taxonomy/URL change proposed.

Backed up2233 privately. Native manage-elements returned `Could not save document` for the grouped proposal and a single image-radius update; reconnecting through a fresh authenticated MCP session produced the same save failure. Current readback remains unchanged. The card redesign is NOT implemented and no new CSS owner is active. No raw Atomic JSON write, duplicate card or fallback framework introduced. Archive2232 and all ten native geo selections continue using existing2233. Browser editing was additionally interrupted by concurrent input. Resume through a working native editor/save path; do not claim successful publication.
