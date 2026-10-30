# Current main Hero — approved split layout with BEAF

**Current,2026-10-22:** The page-owned Hero described below has been replaced by a complete instance of [GCPRO — Shared Hero1318](shared-hero.md), using a native Image and independent content/link Overrides. Earlier Hero element IDs, slider instructions and layout descriptions below are historical. Other page sections and BEAF galleries are preserved.

E70–E71, 2026-10-20. Implemented/published only on https://vitaliiv1.sg-host.com. Owner first approved Concept B as main, requested removal of old background code, then explicitly requested the first existing BEAF comparison in the CURRENT main Hero. No duplicate Hero or new experiment created by E71. Production untouched.

## Exact Elementor storage

Homepage154 → Main46c3aad4 → **01 Hero a62cdd3**, still first of ten sections. The nine other section subtrees, including original comparison section4221ba60, compare exactly unchanged before/after E71. Header113, Footer114, Core positioning, Code903, plugin records and shared component definitions were not edited.

| Role | Current element / native owner |
| --- | --- |
| Hero root | a62cdd3 / local e-7cfcd182-d44a: section/section--dark; native color-primary navy, vertical space-2xl64px; mobile space-xl48px |
| Container | 67b7c63f; existing container,1200px max/gutters32px and20px mobile |
| Grid | 3637829f / e-684a98d6-1453; layout-reset; native1fr1.15fr,48px gap,center; <=1024px one column/32px gap |
| Copy | 41b35720 / e-483c967e-e645; stack/max600px/gap24px; mobile max100% |
| Emergency mark | 25cebce7 → Component286, existing Emergency Restoration override |
| H1 | 7f9397ab; unchanged wording Property restoration in Chicago, existing typography tokens |
| Supporting paragraph | 1d8de660 / e-5a22681a-5033; text-lead/max520px; existing copy, project&nbsp;information wrapping retained |
| Actions | 55056501 / e-10c57ad9-241d; cluster/gcpro-cta-origin,16px gap; existing Code903 integration |
| Call / Request | 7790eda8 →53 / 36d1fd50 →103; existing tel:+18476563322 and unresolved# preserved |
| Visual | **484c13ec / e-401e0bb0-ed4f**; layout-reset; native overflow:hidden/radius8px, same4:3 dimensions |
| Hero comparison | **30e0c45**, native legacy Shortcode widget, Content → Shortcode **[bafg id="723"]**; copied in native Elementor from eb597a1, not detached HTML or a cloned BEAF record |

Native editor was used to copy/paste the existing Shortcode into the existing visual wrapper, remove image3f2d6acf and publish. Shortcode source was visibly `[bafg id="723"]`. MCP deliberately reports empty legacy widget settings; do not mistake that for missing content. The new reference is the existing Tinley Park fire comparison: original `tinley-6.jpg` and `tinley-6-6.jpg`, unchanged meaningful alt text and initial50% divider. Both original images are4:3, matching the replaced1440×1080 concept image without cropping or sizing overrides.

## Hero-only fullscreen suppression and dependencies

Only new custom rule, under **484c13ec → Style → local e-401e0bb0-ed4f → Custom CSS**:

```css
& .popup_button { display: none; }
```

Elementor generates the necessary local selector. No manually hardcoded page/template/element/plugin-record IDs in this CSS, no new Global Class. Native Atomic controls cannot configure vendor-generated popup controls per shortcode instance. Changing BEAF723 record settings would affect the original comparison, so that shared record is preserved. The local rule removes this Hero's fullscreen entry point from rendering and keyboard navigation; it is not a security boundary against developer-console invocation.

Read the served vendor `bafg-custom-pro.js`: ordinary fullscreen is bound to `.popup_button`; image navigation requires `bafg-enable-img-link=1`. Current723 has empty image-link/click-to-move/hover/autoslide attributes, no linked image wrapper/lightbox. Actual Hero image click opens no popup. No extra click interceptor, observer, initialization or replacement JS is necessary. Existing plugin initializes both723 instances independently; desktop/touch clipping changes were measured.

**Originals unchanged:** eb597a1→723,6a2a094→742,961e3c2→767 under66b1c7d4 retain their saved shortcodes, images, divider and fullscreen. Kit6 shared BEAF presentation remains untouched. Existing vendor jQuery/twentytwenty/BEAF Pro assets remain the only comparison dependencies; no new plugin, library, PHP, Custom Code entry or runtime JS. Existing global Code903 still owns Header/Bottom CTA behavior and overlay yielding.

## Background cleanup and retained experiment

E70 replaced the old Hero child tree with the tested native split composition and wiped **all old local background variants**, including technician photo961, gradients,1440px canvas/+80px offset, repeat/cover/position rules. Current root computes background-image:none and solid navy. No old composition CSS is needed.

Global hero--panorama g-708f717 was already detached. A fresh all-page Elementor usage scan returned no consumers; its saved variants were empty. Retired it after that check, reducing classes112→111; Variables36 unchanged. [Retirement evidence](../audits/2026-10-20-hero-panorama-retirement.json). [Historical source mirror](../../integrations/hero-panorama-composition.css) is now a comment-only tombstone, never enqueued; old rules remain in Git history. No unrelated class cleanup.

Draft970 remains the separately previewable static Concept B; Media973 remains its optimized illustrative image and is **not** deleted. [Draft configuration/image/preview](hero-concept-b.md). Media961 is retained for recovery. No new reusable library Component created; Components286/53/103 and existing tokens/classes reused. Hero remains12 saved nodes (image replaced1:1 by shortcode). Native image radius/object-fit/aspect-ratio duplicates had already been removed during E69; native wrapper owns rounding.

## Verification and limits

[Saved current Hero](../audits/2026-10-20-hero-beaf-settings.json), [E71 browser results](../audits/2026-10-20-hero-beaf-qa.json), [E70 static activation checks](../audits/2026-10-20-hero-concept-b-activation-qa.json). Tested360/393/430/768/1024/1440px in Chrome responsive emulation. After the vendor resize handler settles, visual dimensions are320×240,353.33×265,390×292.5,688.67×516.5,944.67×708.5 and581.96×436.47 respectively. Initial immediate resize measurements were transient; final ratio checks passed every width. No horizontal overflow. Same navy/layout/spacing/text/buttons/corners. Copy/actions precede visual on mobile/tablet; split desktop retained.

Continuous mouse drag changes clipping in Hero and all three originals at1440. Hero393 CDP touch drag changed before-image clipping254.166px→106px while scrollY stayed351.33; vertical touch gesture over the image scrolled391.33→496. Hero ordinary click produced zero popup; its popup button computes display:none, all three original buttons remain display:flex. Original fullscreen opened/closed all three at1440. Mobile test sequence was interrupted;742 popup visibly open on recovery and closed,767 separately opened/closed. Do not claim a completed mobile original-drag suite from that interrupted sequence.

E70 actual keyboard Tab Call→Request had white visible outlines; URLs and existing overrides remain unchanged in E71. Reduced-motion emulation, mobile menu opening/closing, Bottom CTA hidden at Hero/visible after origin and suppressed by open menu were checked at E70; no controller changes made in E71. No phone call/form submission. Existing Request Service# remains an unresolved route, not a working submission claim. Vendor divider is still a non-keyboard DIV; full slider keyboard accessibility is not fixed by this scoped integration. Existing CTA contrast limitation remains inherited.

SiteGround staging cache purged after publication. Actual tests used authenticated Chrome; independent incognito/cache-HIT delivery and physical Android/iOS remain unverified. No new animation introduced. Screenshot proof: outputs/gcpro-main-hero-beaf-desktop.png. Saved settings are browser-verified, but no full-site accessibility/Core Web Vitals certification or completed restore drill is claimed.

## Editing and rollback

Edit comparison content only in existing BEAF723 when all its consumers should change. For Hero presentation use visual484c13ec's native controls/local CSS. Keep popup suppression local; never change shared Kit6,723 fullscreen setting or the original three shortcodes for this Hero-only requirement.

To restore static E70: save current state, delete only Shortcode30e0c45 through Elementor, insert native Image973 into visual484c13ec with width100%/height:auto/display:block, remove only its popup suppression rule; preserve radius8px/clipping and all other Hero settings. [E70 exact settings](../audits/2026-10-20-hero-concept-b-activation-settings.json) are a scoped recovery record. Publish154, purge staging cache and recheck six widths/links/menu/Bottom CTA. This does not affect Draft970 or originals.

To restore prior technician Hero, use [reviewed E70 before-state](../audits/2026-10-20-hero-concept-b-activation-before.json) for only the154 Hero subtree, retaining961. Re-read current state first; do not overwrite later unrelated sections. Restoring the deleted empty panorama class is unnecessary for either E70 static or the E68 technician recovery, neither references it. Git revert alone does not undo WordPress changes.


## Current owner-approved homepage Hero — 2026-10-30

Supersedes the earlier Home Hero descriptions for the active page. After reviewing Draft3625, the owner explicitly authorized replacing only the Homepage154 Hero while retaining the existing headline/introduction. Homepage now has native page-local section3253a11: navy background, left copy/actions/reviews, right existing Shortcode8d1585a `[bafg id="723"]`. Existing component1318 and its other consumers remain unchanged. This is not yet a universal shared Hero with a media selector.

Preserved headline `Property restoration in Chicago`, original introduction, Call tel:+18476563322 and Request Service internal page492. Existing emergency component286 is first in left container11fdef8; existing Google widget ID68cbfa084c2c4209d756fb278a2 is under the buttons, locally aligned left. No review number hardcoded. Original Tinley images and BEAF723 unchanged; new instance reuses the existing record.

Caption9057c36 is12px, #AAB8D4, right aligned: `Tinley Park, IL · Fire restoration · View project →`, linking directly to the published Tinley case. One scoped native Shortcode Custom CSS rule applies12px border radius/overflow:hidden to its own comparison only; no BEAF plugin/global changes.

Actual saved authenticated frontend: old H1 and introduction present, comparison right of text, images loaded, one initialized divider; pointer drag changed handle left276px→350.889px. No horizontal overflow. Native editor mobile345px: scrollWidth345=clientWidth345. Initial mobile evaluation timed out during device reload; subsequent check passed. Mobile slider interaction, anonymous delivery and an exhaustive width matrix were not tested in this checkpoint. Staging robots remains noindex,nofollow.

All nine following Homepage sections were compared as complete native settings/styles subtrees against the fresh pre-swap snapshot and are identical. Homepage Settings→Reading, menus and production unchanged apart from the separately authorized staging Header typography correction.

Draft3625 remains Draft at https://vitaliiv1.sg-host.com/?page_id=3625&preview=true and contains only the blue Hero study; full concise homepage prototype remains incomplete. Its native Shortcode was changed723→742 in editor and the Glenview image pair rendered, then restored/saved723 and verified in preview. This proves a different comparison can be selected in a page-local media container; it does not prove arbitrary content overrides inside a shared component.

Next owner request: prepare one universal Hero with per-page image OR existing Before/After selection. Current1318 Photo override remains image-only. Do not describe the universal selector as implemented or roll out page copies. Existing Components documentation describes exposed field overrides: https://elementor.com/help/components-2/ . Native generic slot support has not been established.

Private recovery: homepage-prototype-20261030/home154-before-hero-swap.json and home154-after-hero-swap.json under local private backups. To roll back, restore only the former first Hero instance6380d020, preserving later changes and all following sections.


2026-10-30 owner typography trial: Homepage H1 element4048506 now has native local text-transform:none, rendering the existing source text `Property restoration in Chicago` in sentence case. This is a reversible Homepage-Hero-only test, not a global heading rollout. Other heading styles and copy remain unchanged.
