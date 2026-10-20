# Process entry CTA and first Header exit — E62

2026-10-20, staging https://vitaliiv1.sg-host.com only. [Browser evidence](2026-10-20-process-cta-transition-results.json). Production and BEAF untouched.

## Verified causes and final behavior

At393px/y2900–3200, the How We Work section entered the viewport while the preceding Emergency Restoration Support phone button remained usable. Code903's competing-phone predicate hid Call Now. It returned at3300 after that button left view. E61 checked section center and missed this interval; section stacking was not the cause of this disappearance.

Removed the implicit phone collection/predicate entirely. After Hero, ordinary tel links in Emergency Support, Final CTA or Footer no longer hide the reusable panel. Existing menu/form/modal/input/zoom/short-viewport/opt-out and explicit region rules remain. This deliberately supersedes the earlier automatic competing-phone policy; use existing gcpro-cta-suppress only for an explicitly chosen task region.

The first Header exit had two remaining motion problems: it pinned briefly after becoming fixed while waiting for40px, and a larger gesture overshot the ideal handoff point, returning the shell toward fixed top before it animated away. First downward entry now starts hiding immediately. Its initial transform is measured from the actual rendered flow top minus fixed top, clamped to the fully hidden range. One transient transition:none/transform write, class change and geometry flush seeds the existing200ms CSS animation. Both inline properties are immediately cleared; no new animation API, frame loop, timer, dependency or lasting inline style. Subsequent40px down/24px up tolerance and menu/keyboard pinning remain.

## Exact storage and unchanged owners

Only **Elementor → Editor → Custom Elements → Custom Code903**, GCPRO / Scroll Navigation & Emergency CTA, was updated: Published, Entire site, Body End, priority5. Native code editor reload confirms full source equality with the wrapper of existing [CSS](../../integrations/scroll-navigation.css) and changed [JS](../../integrations/scroll-navigation.js). Neither mirror is separately enqueued. Staging cache purge control invoked before frontend reload.

No Homepage154/Header113/Footer114/CTA895/103/timeline582 settings, Atomic classes, Variables, native Core offsets/layers,590/847, theme files or BEAF integration were edited. No new Global Class/Variable/Component/Custom Code entry/DOM wrapper/plugin/library/listener/observer. The initial-entry flush occurs only when entering fixed while hiding, not on every scroll. Removed phone geometry checks reduce ordinary scroll work.

## Browser results

Authenticated Chrome responsive emulation, not a physical Android/iOS device:

- 360/393/430:12 downward and7 upward samples each, spanning650px before Process through its exit, keep Call Now visible. This covers the preceding call button, heading entry, timeline and subsequent section. Footer remains visible. Final393 y2900–3600 spot sweep after the Header motion adjustment also passes.
- 768/1440: panel hidden in every sweep sample. No document horizontal overflow at all five widths.
- Header at top visible; first downward entry hides without the old40px pause. Later upward return remains visible through30px downward movement and hides after50px, confirming the normal40px tolerance remains.
- Slow393 wheel80→90 and fast150px wheel from top: frame traces show progressive upward positions without a downward rebound. Fast traces at360/393/430/768/1440 are monotonic. The previously observed fast overshoot trace moved from top-104 back to-48.45; final393 starts fixed at-104 and proceeds toward-158.95. Temporary inline properties are empty afterward.
- 393 native menu aria-expanded true suppresses CTA; false restores it. Down/up after close hides/reveals Header. Reduced motion duration0s and no lingering inline properties.

Phone destination remains tel:+18476563322; no call was placed or link edited. Existing unresolved # routes remain unchanged. No claim of a new full form/popup, timeline timing, screen-reader or formal performance certification; those controllers were not rewritten. Prior anonymous403/cache-HIT and real-device limitations remain. One-time forced geometry is an explicit small cost at the handoff, not a measured performance benchmark.

## Rollback

Private pre-E62 Code903 source retained outside Git. Restore the style/script wrapper from commit215c80a603c6fcc452fdaa5378cf6e95b5eda7db into903, update, purge staging and reload to undo only E62. That restores the documented phone suppression and initial Header behavior. Git alone does not deploy WordPress. For full behavior disablement set903 Draft; no Atomic removal is needed. No full-site restore test performed.
