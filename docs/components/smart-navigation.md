# Smart Header and Mobile Emergency CTA

## Current threshold — 2026-10-30

Owner requested bottom panel after20–30% scroll. Existing Custom Code903 now uses25% of current scrollable range, replacing introductory-origin fallback and article50% rule. Removed unused origin lookup; old marker classes can remain harmlessly. Mobile-only width gate, menu/modal/chat/form/input/zoom guards and keyboard-focus pin unchanged. CSS, Header movement and panel design unchanged; no new controller/enqueue.

Native Update/reload confirmed saved threshold and Home script. Authenticated390px: hidden at top/15.0%, visible at29.1%; no horizontal overflow. Later visible at78.8%. Menu suppression not successfully retested; no renewed claim. No calls/submissions. Source mirror integrations/scroll-navigation.js matches saved script after newline normalization. Rollback restores prior threshold lines/origin lookup. Production/noindex unchanged.

**E64,2026-10-20:** Existing903 CSS now reserves panel clearance inside .site-footer instead of body, removing the verified white tail. Mobile native footer baseline is retained with max(section-spacing-mobile, measured barHeight+24 + safe-area inset); last content stays above the fixed panel.903 JS, Header/Core/895 settings unchanged. [Current footer configuration, tests and recovery](../audits/2026-10-20-footer-refresh.md).

Implemented on **staging only, 2026-10-20 (E58)**. Production was not accessed or changed. These are global site-shell features; numeric IDs below are editing locators only. [Verification and limitations](../audits/2026-10-20-smart-navigation.md).

## Global placement and native editing

Theme Builder Header **113**, “ROBYLO / Universal Header”, remains published with **include/general**. Its existing root **4ef1aa21**, Header Shell, keeps site-header and gains gcpro-smart-header. All original header children, menu selection, native object links and design styles remain unchanged.

The rendered outer `<header>` is a direct body child with no transform, containment or clipping. The moving shell is its first child. A separate document-root Div block **feba833**, local native style **e-63fbbef4-8ac8** (padding0/min-width0), contains component instance **18849090 →895**. This sibling is outside the moving shell. The outer header remains static and receives a measured runtime min-height to preserve flow when its shell becomes fixed. No header/menu clone or reparenting script exists.

**Atomic Component895**, “GCPRO / Mobile Emergency CTA”, UID component-9ee4de7d-4608-4b17-b780-3c450684119b:

- Root **175d43eb**: native Flexbox, tag aside, gcpro-mobile-cta.
- Paragraph **111fcda3**: Emergency help, gcpro-mobile-cta__label.
- Nested existing Emergency Service Mark **286**, instance **1acf10db**, blank caption override; existing white numbers/orange slash render to the right of the label.
- Nested existing Primary CTA Button **53**, instance **2077bfde**, orange normal state. No duplicate button/mark definition. E63 replaced the former Outline103 and regenerated the three original element IDs through native component publication;895 ID/UID and exposed keys are stable.
- Supported overrides: **label**, **call_text**, **call_link**. Header instance overrides call_text to **Call Now**; telephone destination resolves to **tel:+18476563322**. Component origin text is Call847-656-3322. No new placeholder route.

Edit global placement/instance overrides in [Header editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=113&action=elementor), or the shared [CTA definition](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=895&action=elementor). Select Global Mobile Emergency CTA in Navigator, then Edit Component. The component's editor-only class exception shows it in normal flow; the controller is disabled in Elementor editing/preview. Never detach it to change a label or telephone destination.

## Atomic ownership and additions

Six new Global Classes, taking103 identities to109; priority of existing classes is unchanged:

| Class / ID | Purpose and owner |
| --- | --- |
| gcpro-smart-header / g-8706951 | Empty semantic hook on existing Header Shell; no visual declarations |
| gcpro-cta-origin / g-b9ab0d8 | Empty introductory-action hook; Homepage154/Hero Actions6092e1ab and shared Hero74/Copy2bd621f1 |
| gcpro-mobile-cta / g-6771860 | Native panel layout, navy/white colors, orange1px border,8px radius, xs/sm spacing; display:none fallback |
| gcpro-mobile-cta__label / g-4d22e61 | Native Inter14px/600/1.4 white label, margin0 |
| gcpro-sticky-intro / g-43749f7 | Empty hook on Core B intro6cb38139 for verified Header clearance conflict |
| gcpro-cta-off / g-3cbfd16 | Empty page/template policy hook; 404125/root7351ac06 and Search126/root7071a479 |

Reuse color-primary, color-white, color-accent, font-body and space-xs. E63 uses existing53 for primary colors/hover/focus/radius and existing286 for branded24/7. Their shared definitions remain unchanged. The panel owns its own8px padding and compact nested-button size; no new Global Variables, palette, plugin, library, theme file or PHP.

Design System → Classes → gcpro-mobile-cta → Custom CSS owns only:

```css
& .button-primary { flex-shrink: 0; white-space: nowrap; padding: var(--space-xs); min-height: 44px; font-size: 14px; }
& .emergency-mark { flex-shrink: 0; }
& .emergency-mark__label:empty { display: none; }
&:where(.elementor-editor-active *) { display: flex; position: relative; }
```

The button guard keeps a44px-high compact action when the existing admin chat launcher reserves width. The mark guard preserves its shape and hides only its blank caption within this panel; Hero286 is unaffected. Editor rule permits static native editing while frontend fallback stays hidden. Nested53 exposes text/link, not compact size, so this existing class-owned exception avoids modifying every shared Primary button. [Current E63 owners/tests/rollback](../audits/2026-10-20-mobile-cta-orange-247.md); [historical E58 class snapshot](../audits/2026-10-20-smart-navigation-classes.json).

## One controller and active deployment

Elementor → Editor → Custom Elements → Code **903**, **GCPRO / Scroll Navigation & Emergency CTA**: Published, **Entire site**, **Body End**, **priority5**. Always load jQuery is unchecked. Repository sources [scroll-navigation.css](../../integrations/scroll-navigation.css) and [scroll-navigation.js](../../integrations/scroll-navigation.js) are pasted together into903, wrapped respectively in style#gcpro-scroll-navigation-css and script#gcpro-scroll-navigation-js. They are not separately enqueued. Saved source equality was verified after reloading the native code editor.

One passive scroll listener, one resize listener, one pageshow listener, focusin/focusout, visualViewport resize and a scoped existing-chat click listener share one requestAnimationFrame scheduler. One ResizeObserver measures the Header; one MutationObserver detects menu/overlay state and inserted forms. No IntersectionObserver, recurring timer, continuous RAF, library or per-page script. Queries inspect known semantic/vendor roots; no full DOM geometry scan per frame.

The explicit staging-host guard prevents activation on other hosts. It is an environment safety boundary, not a page binding. Any approved future production release must deliberately review this guard, native global conditions and existing integrations. No production deployment is implied.

## Responsive behavior and configuration

**Header, all widths (E62):** normal full Header at page top. The shell becomes fixed when the outer host top reaches adminTop minus utilityHeight. On first downward entry, hiding starts immediately, without the subsequent40px tolerance pause. A measured initial transform accounts for scroll overshoot; a one-time style flush seeds the existing transition at its actual flow position. Temporary inline transform/transition are removed immediately. Later floating navigation shows on24px accumulated upward movement and hides after40px downward movement. Direction changes reset distance; while not floating, keyboard-focused or menu-open, it stays visible and resets distance so closing a menu requires fresh movement. Utility bar scrolls away; only :focus-visible within it reveals the full shell. Main-navigation keyboard focus preserves its current top position. Open native menus/submenus or keyboard-visible Header focus pin it; retained pointer/touch focus after close does not. No forced blur or menu click interception. Transform transition200ms; reduced motion removes it. The same original navigation remains focusable; no aria-hidden/inert is applied to the moving Header. [Current behavior, frame traces and limits](../audits/2026-10-20-process-cta-transition.md); [earlier menu correction](../audits/2026-10-20-header-cycle-fix.md).

**Bottom panel, below768px only:** appears after the marked introductory action passes above the usable viewport. It stays in both scroll directions. On pages without a marker it falls back to the Header leaving view. New bespoke Hero compositions should mark their action group; the existing reusable Hero74 has the marker on its Copy group, ending at its CTA. Pages deliberately lacking the global Header do not initialize this controller.

Suppress the panel when a content form/task is in view, an input is focused, a menu/modal is open, the visible viewport is under480px high or the page is pinch-zoomed. **E62 removes automatic suppression for other telephone buttons everywhere:** after Hero, Call Now stays available even when an Emergency Support or Final CTA phone button is visible. E61 had excluded only footer phones and missed the Process-entry interval; that narrower behavior is superseded. Use existing explicit gcpro-cta-suppress region policy when a particular action genuinely needs the space, rather than inferring it from tel links. E60's Core-intro intersection gate remains removed after correcting native Core stacking. Existing CTA keyboard-focus pinning remains unless a menu/modal/chat takes over, so a focused action is not unexpectedly removed. Hidden panel has display:none, inert and aria-hidden. Tablet/desktop never display the panel.

Use **gcpro-cta-off** on a page/template root for contact/request forms, confirmation, legal, careers or campaign pages where a floating call action is inappropriate; review each page's purpose rather than using a slug/ID list. Current404 and search templates carry this policy. **gcpro-cta-suppress** is a reserved optional region hook and **gcpro-cta-overlay** a reserved optional overlay/cookie-banner hook; neither was created as an unused Global Class. Add through native controls only when such content exists. Existing main forms are detected automatically, including dynamically inserted forms. No cookie banner was present in this session; a future vendor needs explicit open-state integration/test.

Existing read-only adapters: native aria-expanded menus, dialog[open], aria-modal=true, BEAF .bafg_popup_preview, and SiteGround's existing .sg-ai-floating-chat shadow-root panel. Closed admin chat launcher reserves its measured horizontal footprint; open chat suppresses the new panel. Vendor styles/markup/settings are untouched. No BEAF files, shortcode, CSS, popup logic or saved selectors changed.

Runtime classes: **gcpro-nav-ready** on html; **is-floating/is-hidden** on marked Header; **is-visible** on panel. Runtime custom properties: --gcpro-admin-top, --gcpro-utility-height, --gcpro-header-clearance, --gcpro-bottom-reserve, --gcpro-bottom-clearance, --gcpro-cta-right. These are geometry values, not Atomic design tokens. The standard WordPress #wpadminbar is measured only for logged-in clearance; it is not an Elementor-generated ID.

The panel uses8px edge clearance plus env(safe-area-inset-bottom). Since E64, mobile .site-footer reserves max(section-spacing-mobile, measured panel height+24px+safe-area inset); body has no reserve padding. The footer stays navy to the end, with last content above the panel. Scroll padding accounts for current Header/panel clearance. Real-device safe-area/browser-toolbar testing remains pending.

## Core Services B: verified conflict only

Before adding clearance, Chrome393px upward scroll at y2250 returned the Header with bottom78.95px while Core intro remained top0: an actual79px overlap. After the semantic hook, the controller temporarily sets an inline top equal to the greater of the native baseline and visible Header clearance, only when the intro's computed position is sticky. It removes the inline value when Header hides; resize re-reads native baseline. Tablet static positioning is unaffected.

**Current saved native style e-67ba0794-7b2b (E61):** desktop sticky96px, tablet static/auto, mobile sticky0/local z1/opaque alternate surface/padding16px. Core section3fd180bb local style e-3ed21e1f-ddd9 now has z0, containing the intro beneath global Header z10000 and bottom panel9998. How We Work4681b8f5 similarly contains its internal number layers with native local z0. Grid, sticky offsets, padding and native release remain unchanged. [E61 changes, tests and rollback](../audits/2026-10-20-section-layers-footer.md). No sticky rewrite, placeholder or section clone.

## Rollback

1. Set **Code903 to Draft**, update and clear staging cache. On a fresh load the Header is static, panel is hidden by its native class and Core uses its original native top values. This is the single behavioral rollback switch.
2. For full removal, remove Header113's new Div block feba833/component18849090; remove the four semantic hooks from Header113, Homepage154's two nodes, Hero74 Copy and404/Search roots. Restore only those class lists, preserving all original local styles/links.
3. Archive895 and remove the six new classes only after checking no additional consumers have been added. Preserve existing Components53/103/286,36 variables, menu,590,847 and all BEAF integration.
4. Recheck saved state, desktop/mobile layout and anonymous delivery. Reverting Git alone does not change WordPress; there is no automatic deployment.

Private scoped pre-change tree snapshots were captured in the task's work directory. They are not full site/database backups or a tested full restore. No raw session/admin response or credential is committed.

## 2026-10-24 — Scrolled Request Service colors

Existing903/style#gcpro-scroll-navigation-css adds two scoped rules for `.gcpro-nav-ready .gcpro-smart-header.is-floating .header-row .button-secondary`: accent/white normal, primary-hover/white on hover/focus-visible. Existing floating class is the sole state; script/listeners/show-hide/menu logic unchanged. Native56 geometry/base styling remains. [Results and limitations](../audits/2026-10-24-service-consistency.md).
