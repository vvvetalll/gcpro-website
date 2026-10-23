# Compact Emergency Restoration Support CTA

Implemented2026-10-22 on **Home154 only**, replacing the former full-width navy strip while retaining its heading, description and both action labels/destinations. The existing page-owned section remains page-owned; genuine shared Atomic Heading71 and Buttons53/103 remain attached instances. No new shared definition, media, Global Class, Variable, custom CSS/JS/PHP, plugin or dependency.

## Current owners

| Element | Owner / purpose |
|---|---|
|6cde656f|Existing mid-page section, retained in the same Home position between services and Process |
|591277e|Compact Emergency Card Frame; existing container class, native8px radius and overflow clipping |
|1c4978f9|Compact Emergency Video Panel; existing cta-panel + section--dark classes |
|2566ff3c /2566fd1a →71|Copy wrapper / original heading and description through independent Overrides |
|7dc9fb97|Actions wrapper, existing cluster class |
|3ded65a6 →53|Call 847-656-3322, unchanged tel:+18476563322 |
|b132592 →103|Request Service, unchanged pre-existing # destination |

Old container2bf35876 and its three instance locators are superseded by the native layout rebuild; shared definitions71/53/103 were not copied, detached or edited. Heading remains **Emergency Restoration Support**, H2, description **Call to discuss your restoration needs.**

## Reused final-CTA treatment

This deliberately opts the mid-page panel into the **existing** staging video mechanism in Custom Code847 through its established semantic cta-panel class. It uses exactly the final CTA's existing attachment846 source, /wp-content/uploads/2026/10/gcpro-cta-test.mp4.847, original Final CTA80 and all global owners are unchanged. It is reuse of the installed mechanism, not a new native Atomic video widget or a newly deployed script.

Same navy #1A327D base, right-side masked video, cover/center media, screen blending and opacity0.4 desktop/tablet,0.34 mobile. Existing mechanism owns muted/autoplay/loop/playsinline, offscreen/tab playback pausing, error cleanup, reduced-motion/Save-Data suppression and pointer-inert/aria-hidden decoration. Native navy remains a readable static fallback before loading, on video failure, or when motion/data policy suppresses playback. No new decorative asset or effect.

Desktop panel is a horizontal native flex row: copy left, existing buttons right; padding48px vertical/32px horizontal,32px gap, natural height. Exterior section has32px vertical white breathing space and existing container gutters. Tablet stacks copy above wrapping horizontal buttons with32px panel padding and24px gap. Mobile stacks the buttons, retains existing847's32px/20px panel padding, and has24px exterior vertical space/20px side gutters. A native8px clipped outer frame preserves rounded mobile corners despite847's existing inner-panel square-corner rule. No final-CTA mobile rule was edited and no !important override/custom CSS was added. No fixed height or spacer.

## Focused verification

| Chrome viewport | Mid-panel width × height | Layout | Document overflow |
|---|---|---|---|
|1440|1136 ×219.1875|Copy/actions horizontal; buttons53px high|none|
|768|689 ×222.96875|Copy above two side-by-side actions|none|
|393|338 ×326.75|Copy and both298px-wide actions stacked|none|

Desktop original Final CTA panel remains **1136 ×267.578125**, exactly its pre-change height; full final section remains its separate taller composition. The mid-card is219px, within the requested approximate desktop180–220px range. Both body and heading compute white, video playback is unpaused with readyState4, source/mask/blend/opacity match the final baseline. Mobile video's observed opacity is0.34, frame radius8px/overflow hidden, static navy preserved. Existing reduced-motion stylesheet and script contract were inspected; reduced-motion emulation, physical touch devices and performance certification were not separately tested.

All Home subtrees outside6cde656f compare equal after HTML entity normalization, including Hero, Process, BEAF, other shared sections and Final80 instance/Overrides. Complete native Final80 definition compares identical before/after. No FAQ, SEO, other page or original video-code write. Existing button labels/URL settings compare preserved; no call or form submitted. Native Elementor/SG staging caches refreshed once after writes; viewport overrides reset.

**Existing link limitation:** Request Service was already # before this task. It was intentionally preserved under the explicit requirement to retain both CTA destinations. It does not open the request page, so full request navigation is **not** reported as verified/functional. Correcting that destination is a separate owner decision; no alternate URL was silently substituted. Click-to-call retains its existing valid telephone URI.

## Safe reuse and recovery

Edit this page's content through its native71/53/103 Overrides; use existing classes/Variables for shared design. Structural layout belongs only to6cde656f, not Final80. The existing847 mechanism retains its documented staging hostname gate and is not claimed production-portable. Do not duplicate its code or change Final80 to customize this compact card. To roll back with authorization, restore only the original6cde656f subtree from the private pre-change snapshot and refresh native caches, preserving later Home work. Reverting Git docs alone does not revert WordPress.
