# ACF Free Projects prototype — 2026-10-26

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
