# Header entry and post-menu scroll regression — E60

2026-10-20, staging https://vitaliiv1.sg-host.com only. Production and BEAF were not modified. [Sanitized observations](2026-10-20-header-cycle-fix-results.json).

## Verified causes

1. The previous fixed condition waited until the outer host bottom left the viewport. Its shell was already mostly offscreen, then switched to fixed top-40px on mobile and reappeared before hiding. Reproduction with the menu open isolates the position discontinuity: y155.33/top-109.33 versus y165.33/top-40. Open-menu pinning is expected; the discrete top change is not.
2. JS treated every active element within Header as a reason to pin it. After pointer menu close, the native toggle retained focus, aria-expanded=false and :focus-visible=false. Further downward scrolling to900 still left Header visible. E59 tested activation/close but missed this retained-focus scroll cycle.
3. Browser inspection also showed the Core intro crossing the bottom panel at section entry; its existing higher z-index partially covered the panel. This is an actual intersection, not a reason to rewrite Core sticky settings.

## Exact deployment and minimal changes

Only **Elementor → Editor → Custom Elements → Custom Code903**, GCPRO / Scroll Navigation & Emergency CTA, was edited. Published, Entire site, Body End, priority5. The native code editor was reloaded after saving and its full value compared exactly with the wrapper assembled from [existing CSS](../../integrations/scroll-navigation.css) and [existing JS](../../integrations/scroll-navigation.js). These mirrors are not separately loaded.

- Fixed handoff uses outer host top <= adminTop - utilityHeight, where normal and fixed positions align. Outer host min-height still preserves document flow.
- CSS :focus-within and utility :focus become :focus-visible. JS keyboard pinning uses the same focus-visible condition. Pointer/touch focus is retained naturally; no blur(), preventDefault, replacement click or cloned menu.
- Reset movement distance while nonfloating, keyboard-pinned or menu-open. Existing40px downward/24px upward thresholds and200ms transition remain.
- Existing intro collection adds a vertical collision check against viewport height minus measured panel height minus24px reserve. The panel yields during Core entry and returns when clear. Existing keyboard focus preservation remains.

Header113, CTA895/103, Homepage154, six semantic Atomic classes, design tokens, native Core style e-67ba0794-7b2b and BEAF settings are unchanged. These numeric values are editing locators, never new runtime dependencies. No new classes, Variables, components, Custom Code entries, plugins, libraries, theme edits, listeners or observers. Existing shared scheduler/observers remain the only controller.

## Browser verification

Authenticated Chrome responsive emulation, not a physical phone:

| Check | Result |
| --- | --- |
|360/393/430/768 pointer|Two complete cycles each: down hides → up reveals → click opens → scrolling with open menu pins → click closes → down hides → up reveals. No blur between close and scroll. Native toggle retains pointer focus with focus-visible=false.|
|393 touch input|Separate CDP touchStart/touchEnd activation opens/closes, subsequent down hides/up reveals with retained toggle focus. Scroll positions controlled through browser; this is not a physical swipe/device test.|
|393 normal/fixed entry|Top46 at y0, -24 at70, -34 at80, -40 at90; no reappearance jump. Native wheel80→90 confirms -34→-40 at handoff.|
|393 wheel after menu close|Native pointer open/close then actual wheel+200: y1400/hidden=true; wheel-200: y1200/hidden=false. No forced focus change between closing and scrolling.|
|Keyboard|Tab/Shift+Tab and Enter used. Header keyboard focus computes focus-visible=true and pins; Enter opens/closes native menu. Deliberate keyboard focus remains visible even after close.|
|1024/1440|Down hides/up reveals; returning to0 restores normal full Header. Bottom panel hidden; no positive document-width overflow.|
|Reduced motion|Computed transition-duration0s.|
|Core393|Hidden Header: intro top0, inline override removed. Revealed Header: bottom78.95, intro top79. Section release observed offscreen. Requested y2400/2200 retained, without scroll displacement.|
|Core panel collision360/393/430|Intro at about810px on852px viewport: panel hidden. Inside section: panel returns in both directions; Header still hides/reveals. Overflow0.|
|Saved deployment|903 full source equality after reload; global conditions/body-end5 retained. Staging Purge SG Cache invoked; final native menu/open/close/down/up cycle repeated after frontend reload.|

Affected tel destination remains tel:+18476563322; no link values or component overrides were edited. Existing unresolved # navigation routes remain pending; no claim of working destination pages or completed telephone call. Native Atomic visual editability follows from leaving component/class settings unchanged; this task verified the native903 editor, not a new visual-editor audit of every component.

No physical Android/iOS, screen-reader, formal performance or anonymous/cache-HIT certification. Prior anonymous403 limitation remains unresolved; authenticated reload is not proof of guest cache delivery. Browser safe-area behavior on a real device remains pending. No form/BEAF popup rewrite or full integration recertification was performed for this scoped Header correction.

## Complexity and rollback

One existing behavior owner; no additional DOM, classes, dependencies or event handlers. Collision check reuses already collected intro elements and existing measurements. No unrelated cleanup.

For behavioral rollback, set903 Draft, update and clear staging cache; fresh loads use native static Header/Core and hidden panel fallback. For this patch only, restore the two source files from main commit03b5a13bbaaa5968d2f34a41770d3c34ebff5900, paste their style/script wrapper into903, update and purge; that deliberately reintroduces the documented defects. Git revert alone does not deploy WordPress. A private scoped pre-change903 source was retained outside Git; no full-site backup/restore was performed here.
