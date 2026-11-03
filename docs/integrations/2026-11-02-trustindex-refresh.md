# Trustindex design refresh — 2026-11-02

Owner scope: leave Home's current widget unchanged; use the same Slider II design for separate service widgets with their existing filters; use a shared general component on pages without service selections. Staging only.

Home154 remains native Shortcode02441ff with public widget `d274cef84f6389753e464c4df17` (Trustindex848974). Actual desktop design inspected: Excellent/stars/company review count at left, three review cards at right on the existing pale-blue section. Preserve Light background/Poppins and native vendor controls. No new styling or vendor code.

Nine independent copies were created through Trustindex Clone Widget, explicitly restricting the source to GCPRO Restoration (not the dental source). Each is named `GCPRO | Service Reviews II | <service>`. Six tag filters use all-rating eligibility, minimum1 character, newest first, maximum10. Three manual sets preserve the exact five review IDs in the 2026-10-24 canonical mapping. Company aggregate remains245 in the checked previews; filtered cards do not redefine the company rating.

| Service | Admin ID | Public ID | Pages |
|---|---|---|---|
| Water Damage |849190|bfc9d1a84d3c919cdc06f2f7c44|514|
| Fire & Smoke |849191|e2d7f0284c2e919c5016f47dcc1|517,520|
| Reconstruction |849192|c58ae68844da91919826aa1d551|518,524|
| Storm Damage |849194|f38999784a35919a7346d3f397d|523|
| Contents Restoration |849195|4e1cca5848ee91941d560ee6d75|521,525|
| General Contracting |849197|07222db8404991923d7602c7e3b|522|
| Mold Remediation |849198|094136e84ccf9197cb869a9a89f|516,519|
| Dehumidification |849200|4fe096c84a299204f20655f58fe|491|
| Commercial Water Damage |849202|15449fd848bc92028326af36028|515|

Generated WordPress code was read from each saved widget dialog. Service sections remain page-local, with existing native Shortcode children; only their widget ID changes. Their section/heading/layout and unrelated page trees remain intact.

## Shared fallback

New native Component4051 **GCPRO / General Reviews**, root63c2f53d, uses the already installed `gcpro-trustindex` Atomic widget with `widget_id=d274cef84f6389753e464c4df17`, `visibility=show`. No new plugin or runtime code. The first attempt to copy Home's whole section was rejected because native components cannot contain legacy Shortcode widgets; no component was created by that failed call. Existing Atomic Trustindex functionality supplies the compatible implementation. Consumers487 Water Extraction,488 Board-Up,489 Odor Removal,490 Moisture Mapping replace only the old shortcode node with a component instance, preserving their section/heading/position. Home itself remains unchanged.

Editor: https://vitaliiv1.sg-host.com/wp-admin/post.php?post=4051&action=elementor

## Storage and recovery

The existing registered WordPress REST Elementor metadata interface updates native saved trees. Immediately-before and after documents are local/private in `work/reviews-2026-11-02/`, outside the repository. Scope-only shortcode/node replacement; statuses, slugs, parents, templates, URLs and titles checked unchanged. Restore only the changed review child from that page's baseline, after checking later edits. Old Trustindex widgets remain available and unmodified.

Vendor Trustindex remains CSS/JS owner. No new Global Classes, Variables, custom CSS/JS/PHP, plugins or external dependencies. One new native component and nine external widget configurations are intentional reusable/general versus independent/service owners. No added nested wrappers.

## Verification status

Completed and published on staging: 13 page-local service shortcodes and four native Component4051 instances. All17 saved IDs and unchanged status/slug/parent/template/link/title checked again after final native saves. Trustindex saves and exact manual selections confirmed in UI. Home was not edited.

Elementor retained stale rendered element output after REST metadata writes; SG purge alone did not clear it. Re-saving each existing native H2 with the same title through manage-elements, followed by publish-document, refreshed Elementor output without changing the heading. Final SG cache purge performed. Water Damage authenticated frontend now renders new public ID with layout5; Water Extraction renders Home public ID with layout5 through Component4051. Desktop screenshots show rating plus three cards within the existing section and navy credentials boundary. Water mobile390 override (375px content viewport) has equal scroll/client width375 and stacks rating above the review. Override reset. No extra styling was needed.

Limitations: anonymous HTTP probe returned403, so anonymous delivery is not verified. Mobile Next locator was unavailable; desktop Next/Read more actions were issued, but resulting state was not conclusively verified, so no interaction-pass claim. No exhaustive viewport/page matrix or physical-device test. Owner final visual acceptance remains. Existing source links were inspected; service clone review-count link points to the GCPRO Trustindex summary, while the shared Home widget preserves its original destination. No page links were changed.

Private local evidence: water-reviews.png, results.json, final-check.json and scoped before/after records under work/reviews-2026-11-02. No private backup or raw admin response is committed. No production writes.

## Published preview links

WordPress editor login required for preview URLs.

- [514 — residential-services/water-damage/](https://vitaliiv1.sg-host.com/residential-services/water-damage/?preview_id=514&preview=true)
- [517 — residential-services/fire-smoke/](https://vitaliiv1.sg-host.com/residential-services/fire-smoke/?preview_id=517&preview=true)
- [520 — commercial-services/fire-smoke/](https://vitaliiv1.sg-host.com/commercial-services/fire-smoke/?preview_id=520&preview=true)
- [518 — residential-services/reconstruction/](https://vitaliiv1.sg-host.com/residential-services/reconstruction/?preview_id=518&preview=true)
- [524 — commercial-services/reconstruction/](https://vitaliiv1.sg-host.com/commercial-services/reconstruction/?preview_id=524&preview=true)
- [523 — residential-services/storm-damage/](https://vitaliiv1.sg-host.com/residential-services/storm-damage/?preview_id=523&preview=true)
- [521 — residential-services/personal-property-restoration/](https://vitaliiv1.sg-host.com/residential-services/personal-property-restoration/?preview_id=521&preview=true)
- [525 — commercial-services/personal-property-restoration/](https://vitaliiv1.sg-host.com/commercial-services/personal-property-restoration/?preview_id=525&preview=true)
- [522 — commercial-services/general-contracting/](https://vitaliiv1.sg-host.com/commercial-services/general-contracting/?preview_id=522&preview=true)
- [516 — residential-services/mold-removal/](https://vitaliiv1.sg-host.com/residential-services/mold-removal/?preview_id=516&preview=true)
- [519 — commercial-services/mold-removal/](https://vitaliiv1.sg-host.com/commercial-services/mold-removal/?preview_id=519&preview=true)
- [491 — dehumidification/](https://vitaliiv1.sg-host.com/dehumidification/?preview_id=491&preview=true)
- [515 — commercial-services/water-damage/](https://vitaliiv1.sg-host.com/commercial-services/water-damage/?preview_id=515&preview=true)
- [487 — water-extraction/](https://vitaliiv1.sg-host.com/water-extraction/?preview_id=487&preview=true)
- [488 — board-up/](https://vitaliiv1.sg-host.com/board-up/?preview_id=488&preview=true)
- [489 — odor-removal/](https://vitaliiv1.sg-host.com/odor-removal/?preview_id=489&preview=true)
- [490 — moisture-mapping/](https://vitaliiv1.sg-host.com/moisture-mapping/?preview_id=490&preview=true)
## Page522 clipping investigation — 2026-11-03

General Contracting522 retains its service-specific849197 shortcode, not4051. Live comparison with515 confirmed the same Slider II/layout5 configuration and835px desktop viewport with three278.323px cards; mobile390 showed one full card. Parent overflow is visible; vendor overflow hides offscreen slides and autoplay briefly exposes partial neighbors. Persistent clipping not reproduced, prior cause unconfirmed; no settings/global/page CSS changes. [Detailed evidence and limitations](../components/service-page-rollout-2026-10-23.md#commercial-general-contracting522-optimization--2026-11-03).
