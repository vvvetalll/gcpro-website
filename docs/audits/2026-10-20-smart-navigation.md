# E58 — Global smart navigation verification

2026-10-20, staging https://vitaliiv1.sg-host.com only. Approved implementation; [exact owners, behavior and rollback](../components/smart-navigation.md). Baseline Git997f307. Production untouched.

## Saved-state verification

- MCP connection and native UI/frontend all target the designated staging host.
- Theme Builder113/114 remain published, active include/general. No assignments changed. Native global Code903 is published/Body End/priority5/Entire site, jQuery opt-in unchecked. Reloaded code source exactly equals repository CSS+JS with documented wrappers.
- Original12-node Header Shell tree differs only by gcpro-smart-header. Separate new native Div block +895 instance added at document root. Original menu/logo/CTA fields remain unchanged.
- Homepage190 nodes before/after: only6092e1ab and6cb38139 class lists gain semantic markers; native styles/interactions/content equal. Core native local CSS is byte-equal in the returned plain representation.
- Shared Hero74 Copy gains only gcpro-cta-origin; its existing content/overrides/local styles remain. Search126 and404125 roots gain only gcpro-cta-off. No ID/slug lists in runtime logic.
- New895 exposes label/call_text/call_link; Header instance's Call Now resolves to verified tel:+18476563322. No call placed or form submitted. Existing Request Service# and other unresolved links remain pending, not replaced with guessed routes.
- Native Header editor Navigator displays the new instance, Edit Component action and override controls. Static CTA preview renders in editor; Publish remains disabled during read-only inspection. New class style props use native token bindings; only two documented scoped Custom CSS exceptions.
- Existing590/847, theme, BEAF records, page Custom CSS, SVGs, plugins and variables were not edited.

## Browser checks performed

Chrome desktop viewport emulation, authenticated WordPress session. [Raw viewport observations](2026-10-20-smart-navigation-viewport-results.json). Negative raw overflow differences at desktop/tablet represent the15px scrollbar; all tested scrollWidth values are at or below the viewport.

| Width | Header at top / down / up | Bottom CTA | Document overflow |
| --- | --- | --- | --- |
|360|Visible / hidden / visible|Hidden at top; visible both directions after intro|None|
|393|Visible / hidden / visible|Same; about70px high, button52.53px|None|
|430|Visible / hidden / visible|Same|None|
|768|Visible / hidden / visible|Hidden|None|
|1024|Visible / hidden / visible|Hidden|None|
|1440|Visible / hidden / visible|Hidden|None|

-393px menu activated by keyboard Enter: Header remains visible while scrolling; Bottom CTA hides; closing restores normal behavior. Native desktop Residential submenu activated by Enter; Header stays visible with keyboard focus and submenu, no overflow. Tab traversal through CTA verified; telephone href checked without placing a call.
- Core at393px y2350: intro top0 with Header hidden. Upward y2250: Header bottom78.95, intro top79. Native section release checked at y2900: intro top-61.21, no longer pinned. Existing opaque surface/padding retained.
- Additional [tablet/desktop sticky samples](2026-10-20-smart-navigation-sticky-results.json):768px remains static with no inline top;1440px native hidden-Header top96, returning-Header top135, settled Header bottom134.95 in the authenticated session. Immediate geometry samples can occur during the200ms transition; the desktop settled measurement is recorded separately.
- Actual initial defects fixed: returning Header overlapped native Core intro by79px; existing SiteGround admin chat launcher overlapped Call Now. Temporary Header clearance and measured launcher space address those verified collisions. Button wrapping caused by reduced space fixed within the new component only.
- Existing BEAF fullscreen popup opened through its button: panel hidden while popup displayed; existing close action restored page. Plugin content/styles/behavior unchanged.
- Existing SiteGround chat opened: new panel hidden; minimized launcher: panel occupies separate horizontal space. Adapter reads vendor shadow DOM only.
- Temporary browser-only main form/input inserted: panel suppressed while form visible/focused; removing fixture restored it. No saved WordPress form/content change.
-393×430 short viewport: panel hidden. Emulated pinch scale1.5: panel hidden. Reduced-motion emulation: Header transition duration0s; phone action remains available.
- Global ordinary404 and search routes each render exactly one Header/panel and the single controller, with gcpro-cta-off present. Homepage has marker and contextual behavior. Native published conditions remain unchanged.
- Safe-area bottom CSS and reserved flow/scroll clearance inspected; desktop emulation has no physical gesture navigation inset. No real Android/iOS validation claimed.

## Delivery and limitations

Staging Purge SG Cache control invoked after implementation; no cache HIT proof. Anonymous ordinary-root HTTP request returns403, x-proxy-cache-info DT:1. Therefore anonymous/incognito execution and guest cache freshness remain **unverified**. Logged-in ordinary frontend loads contain the final controller and component. Do not treat this as proof for all visitors.

Physical Android Chrome/Samsung Internet/iOS Safari, changing real browser bars, hardware keyboard/screen-reader certification, real virtual keyboard and full performance/CLS measurements remain unverified. No conversion lift claimed. Cookie banner absent; future vendor needs semantic/open-state integration. No real public contact form exists on this Homepage; browser fixture coverage is distinguished above. Shared Hero's hook is saved/read back; all draft/future page consumers were not exhaustively rendered.

## Complexity review

One new reusable composition with two content children, one unavoidable document-root host, six justified classes (two visual, four semantic), one active code entry, zero new variables/plugins/libraries/theme files. Existing Header/menu/button definitions reused. One scroll scheduler and one observer of each needed type; no independent CTA/Header scripts or duplicated active source. Narrow component CSS handles the two demonstrated native gaps. No unrelated cleanup.
