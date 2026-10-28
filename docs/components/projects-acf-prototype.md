# ACF Free Projects prototype — 2026-10-26

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
