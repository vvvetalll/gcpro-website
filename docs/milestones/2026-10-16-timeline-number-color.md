# E20 — Ripple-synchronized step-number color

2026-10-16, staging Homepage154 / Process Timeline582 / existing Elementor Custom Code590. Owner authorized white→GCPRO orange→white during the existing desktop whole-step hover and mobile01→04 ripple sequence.

## Smallest implementation

Updated **only `integrations/process-timeline-mobile.css`**, deployed inside the existing `gcpro-process-mobile-style` block of Code590 through its standard CodeMirror editor. Same native Page154-only condition, Published, body-end/priority10; no sitewide injection, theme/shared ROBYLO changes, new snippet or JavaScript edits. Saved source was reloaded and compared exactly; the anonymous frontend CSS and JS also match canonical sources.

Added one property-only keyframe **`gcpro-process-number`**: white at0/100%, existing accent token at20–65%, ease-in-out. It changes **color only**, never transform, background, typography or geometry. Duration1160ms equals the unchanged1000ms first ring +160ms second-ring delay. One iteration, no persistent fill: number returns to its native white default while pointer stays over the step.

Desktop uses the existing `.process-timeline__step:hover .process-timeline__number` relationship. Mobile uses the existing `.process-timeline[data-gcpro-ripple="played"]` marker and the existing child2/3/4 starts400/800/1200ms. The color ends with each ring pair; total mobile sequence still2360ms. No observer, trigger, timer, class or DOM additions. Both modes explicitly require `prefers-reduced-motion: no-preference`. The existing navy background and desktop navy-hover shade are preserved.

Native Atomic content/layout controls and the12 existing Component Overrides are unchanged. Synchronizing a child color keyframe to the already-authorized CSS pseudo-element ripple/viewport state requires this minimal extension to the same centralized integration; an independent native interaction would create competing timing/triggers. This is one color track within the existing effect, not a second animation system. No new executable file, Global Class, Variable, Component, plugin or dependency.

## Verification

- Authenticated IAB and actual logged-out Chrome profile: desktop1440 whole-step description hover turns01 orange, then smoothly white again while still hovering. Other numbers remain white. Navy circle remains stationary64px; original ring1000ms/+160ms timing retained.
- Both visitor states,390 and430 touch emulation: initial below-viewport state waiting and all numbers white. Entry marks played; sampled colors show each of01→04 reaches exact `rgb(240,90,41)`, intermediate fade colors, then all return to `rgb(255,255,255)`. Circle geometry56px, transform:none and Montserrat sizing constant throughout; no overflow.
- Guest leave/re-entry after completion: all white, no replay. Reduced-motion430 in both visitor states: white numbers, animation:none, no mobile observer marker after entry. No hover-dependent content.
- Native staging SiteGround purge after deployment. Repeated ordinary cookie-free homepage requests are cache HIT with one current style/script/keyframe; guest runtime source exact. No guest console warnings/errors captured. Public theme fallback checksum remains **42eb1062b9890ed5ff8f4d33ea3ac480**, unchanged from E16.
- Fresh saved Homepage154 equals its E19 tree exactly. No page/Component/layout/Global Class/link writes. Existing navigation and unresolved destinations were untouched; no internal URL added.

[Measurements](../evidence/2026-10-16-timeline-number-color/qa.json), [HTTP/cache](../evidence/2026-10-16-timeline-number-color/http.json), [theme checksum](../evidence/2026-10-16-timeline-number-color/theme-check.json), [desktop sample](../evidence/2026-10-16-timeline-number-color/desktop-1440.jpg), [mobile sample](../evidence/2026-10-16-timeline-number-color/mobile-390.jpg). Static screenshots illustrate a frame; time-sampled colors establish progression and reset.

## Editing, complexity and recovery

Edit the existing CSS file's `gcpro-process-number` keyframe for the color envelope, then update the style block in [Code590](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=590&action=edit), preserve unchanged canonical JS and conditions, purge relevant staging cache and reverify anonymous behavior. Duration1160ms is coupled to the current ring pair; mobile start offsets mirror the existing sequence. Reuse the existing condition only on future authorized pages, never duplicate injection.

Only22 CSS lines added (plus comment update); no wrappers, styles on individual widgets, duplicate classes, new observer, runtime dependency or timer. Ring declarations/keyframe and JS are unchanged. Scoped pre-edit Code590 source is stored outside Git at outputs/recovery/code-590-before-number-color.txt; restore it and purge staging cache to roll back only this refinement. Git alone does not deploy/revert WordPress code.

## Limits and accessibility

Actual guest testing used a separate logged-out regular Chrome profile, **not incognito**. Responsive checks are desktop touch emulation, **not a physical Android test**; owner should verify the new color refinement on the S25 Ultra. E18's owner physical-device confirmation concerns the earlier ripple, not this new color track. Controlled incognito verification remains pending through unavailable connected surfaces. No screen-reader/performance benchmark.

Approved orange/navy contrast is **3.45:1** on#1A327D and **4.11:1** on desktop hover#142862: below4.5:1 for normal-sized text. White is still the default/end state, and headings identify every step independently; no information depends on the transient orange color. Brand colors and number typography were preserved as explicitly requested. This contrast limitation is reported, not silently corrected.
