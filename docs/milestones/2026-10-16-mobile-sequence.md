# Mobile timeline viewport sequence — E17

Verified2026-10-16, America/Chicago. Staging Homepage154 only; extends [E16](2026-10-16-process-ripple.md), preserving its desktop effect exactly. Owner explicitly permitted minimal IntersectionObserver if native Elementor cannot reasonably trigger the same effect. No production/shared starter/theme changes.

## Native-first capability finding

Read installed `elementor://interactions/schema` and the current editor interaction tool contract. `scrollIn`/replay configuration exists, but exposed actions are fade/slide/scale/custom opacity/transform on actual elements. No exposed CSS-state toggle or pseudo-element animation target starts the existing pair of rings. Applying these transforms to the numbered circle would violate the stationary-circle requirement; adding eight ring elements would add unnecessary markup. A small observer feeding the existing CSS animation is the supported, authorized simpler exception. No native scroll interaction was applied to the live circle as a test.

## Exact additions and edit locations

| Addition | Purpose / why necessary | Reuse / editing |
| --- | --- | --- |
| [integrations/process-timeline-mobile.js](../../integrations/process-timeline-mobile.js) | Minimal IntersectionObserver supplies the unavailable native pseudo-element trigger. One observer, no scroll listener/library. | Existing process root selector; threshold/media checks editable here and in native Code590. |
| [integrations/process-timeline-mobile.css](../../integrations/process-timeline-mobile.css) | Touch-only ring generation and four-step delays, reusing existing keyframes/token; later rings stay hidden until their delay. | Same Component582 pattern; timing/stroke editable here/Code590. Desktop file unchanged. |
| Native Custom Code590 | Central supported deployment of these two sources without modifying theme/PHP or adding a plugin. | [Edit590](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=590&action=edit); body-end, priority10, Include→Singular→Pages→154, forced jQuery unchecked. |

There were zero native Custom Code entries before this task; only590 was created. It is `elementor_snippet`, not a new Page or Atomic Component. No new Global Class, Global Variable, Atomic Component, content wrapper, plugin or external dependency. Runtime marker **`data-gcpro-ripple`** is waiting→played on the existing `.process-timeline`, not a stored style or global class. No inline style attributes, HTML widgets, widget Custom CSS or undocumented snippets.

The one centralized native Code entry contains the CSS in `<style id="gcpro-process-mobile-style">` and JS in `<script id="gcpro-process-mobile-sequence">`. Both saved editor field and actual frontend text matched source exactly after reload. Native Page selector resolves object154; no hardcoded domain/page URL appears in runtime code. This entry and its condition must migrate with the Homepage object. No automatic deployment exists: edit canonical files, apply their combined contents to the same entry, update/read back, then verify frontend. Content and ordinary design continue to use Component582's standard12 overrides/classes.

## Trigger / timing / safety behavior

- Guard: `(hover:none) and (pointer:coarse)`, no reduced-motion preference, IntersectionObserver available, and not the actual Elementor editor (`elementor-editor-active`). Body-end location means timeline markup already exists. Unsupported API/no JS leaves complete static content.
- Observe the **existing timeline grid**, threshold0.1. At least10% must intersect the viewport, so the first circle is visible before starting; seeing the section heading alone does not start hidden circles. Default root margins, no premature load animation.
- Observer marks played and unobserves that root. It runs once per timeline per document load, not once per scroll, and does not loop. Reloading the document intentionally resets it. No polling or continuous scroll listener.
- Step01/02/03/04 start at0/400/800/1200ms. Each emits two1000ms rings, second ring160ms later: total2360ms. Reuse **`gcpro-process-ripple`** from unchanged E16 theme file and existing accent Variable,2px stroke. Mobile fill is forwards, not backwards: future rings remain opacity0 before their delays; finished rings remain transparent.
- Only pseudo-elements scale/fade. Numbered circles, connectors, typography, geometry, text and links remain unchanged. Pointer-events:none on decorative rings; no button cursor or animation-dependent information.
- Reduced motion gates both JS initialization and mobile ring CSS. E16's existing reduced-motion transition rule remains untouched. Touch never needs hover; desktop's new media query is false and observer is not created.

## Actual verification

| Test | Result |
| --- | --- |
|390×844 touch, initial page top|Timeline top4279px, marker waiting, no ring animation while below viewport. |
|430×932 touch, initial page top|Timeline top4245px, waiting/no rings before entry. |
|Both widths, actual entry|Marker played only with timeline in viewport; sampled opacity shows01→02→03→04 starts, correct first/second ring delays, one iteration and eventual0 opacity for all8 rings. |
|Both widths, leave and re-enter|Marker stays played; all rings remain finished/transparent, no replay. |
|Both widths, reduced-motion page loads|No observer marker, generated rings or animations after scrolling into timeline. |
|Geometry/readability|Circles56×56, transform:none throughout; document-position rounding below0.001px. Vertical connectors remain centered/continuous, no overflow/inline style attributes. |
|Desktop1440|No mobile marker; real description hover still triggers E16 rings with circle:hover=false,1000ms/+160ms/one iteration; stationary64px circle and original background. |
|Scope/integrity|Page2 has neither source style nor script. Theme fallback text matches saved E16 bytes; saved Homepage154/Component582 trees compare exactly before/after. No links changed. |
|Native editing|Opened actual Homepage editor, selected existing Process Timeline:12 contenteditable fields, Publish disabled; body has editor-active guard class. Code590 standard editor shows source/location/priority/Page154 condition. |

[Compact QA evidence](../evidence/2026-10-16-mobile-sequence/qa.json), [390px sequence sample](../evidence/2026-10-16-mobile-sequence/mobile-390-sequence.jpg), [430px sequence sample](../evidence/2026-10-16-mobile-sequence/mobile-430-sequence.jpg). Screenshots are static moments, not animation recordings. Actual time-sampled opacity/readback tests establish progression/completion. Checks use browser touch/reduced-motion emulation, not physical phones, screen-reader testing or a performance benchmark. Dynamic preference toggling/cross-session persistence were not tested or added.

## Complexity review and recovery

Reused existing four-step structure, classes, tokens, native code-management UI and one keyframe. One entry/two small source files, no extra design abstraction, class, ring DOM nodes, plugin, PHP or event/polling framework. Native desktop pseudo-element definitions are fine-pointer-gated; the exclusive touch definitions intentionally repeat only necessary ring geometry to keep the desktop/theme bytes untouched. Base text/layout rules are not duplicated.

No existing code entry was overwritten; saved page/component snapshots were captured before activation and compared afterward. To disable this addition, set **Code590 to Draft** through native status controls; E16 desktop effect remains. To restore/edit the mobile integration, use these tracked sources and its recorded native condition. Full database/files restore and automated deployment remain unverified. Git revert alone does not change the saved WordPress code record.

No implementation blocker remains. Await visual approval. Future service pages must explicitly extend this same entry's native display conditions after authorization; do not duplicate the integration or expose Draft pages.

## Later verification correction — E18

The E17 browser checks above were authenticated emulation. They did not establish anonymous HTML delivery. Owner failure was traced to stale SiteGround guest HTML missing both Code590 blocks; native staging cache purge restored delivery and logged-out runtime checks passed. [E18](2026-10-16-anonymous-timeline-cache.md) supersedes any implication that E17 proved guest or physical-device operation.
