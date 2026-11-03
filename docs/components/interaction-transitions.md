# Shared interaction transitions — 2026-10-23

## Global button fill sweep — 2026-11-03

Owner expanded the local1140 task to global buttons. Published on staging in existing Atomic classes `button-primary`, `button-secondary`, `button-outline`, `button-outline-orange`, `button-outline-white` → Style → Custom CSS. Positioned isolated `::before`, inset0, z-index−1, pointer-events:none, left-origin scaleX(0→1),280ms ease, smooth reverse on leave, hover/focus-visible with disabled guards; reduced-motion removes its transition. No JS, dependencies, new components, dimensions or layout edits. Pre-existing focus/box-sizing/white-space/disabled rules retained. Existing compatible local1140 sweep and width rules remain.

Original fill tokens: primary/secondary → color-primary-hover (#142862); outline → color-primary (#1A327D); orange outline → color-accent (#F05A29); white → color-white. Resting background remains beneath the layer, with existing text/border behavior. Secondary scoped variables preserve header transparent→primary and floating accent→primary-hover. White's transparent footer exception remains via `.site-footer`. Temporary class selections for global editing were removed before publication; original component class assignments retained.

Owner-reported orange corner fringe fixed on primary by changing only pseudo-element inner radius to `calc(var(--space-xs) - 1px)`. Outer8px radius and original border unchanged. Actual pointer hover verified matching navy fill/border without orange corner gap.

Authenticated Home154/Service Area495 checks: five delivered class rules include sweep, focus and reduced-motion. Actual pointer primary/header/white hover confirms original final colors and280ms; primary reverse reaches scale0. Home1140 tested at actual CSS widths1440,768,390, accounting for browser zoom: equal CTA widths and no settled overflow;390 buttons remain below map, both336.36×52.41px at this zoom. Popup1801 opens by desktop/mobile click and tablet Enter; Tab focus outline visible. Mobile All Service Areas reaches /service-area/. Emulated reduced motion gives0s for all button pseudo-elements. Viewport/media overrides cleared; staging cache purge invoked. Anonymous delivery, physical devices and every-page coverage not claimed; no call/form submission performed.

Rollback: remove added position/isolation, pseudo/sweep rules and secondary sweep variables; restore hover background tokens above, including white's nested hover/focus backgrounds. Keep original geometry/focus/disabled and header/footer rules. Local1140 rollback remains in service-areas.md. Other card/menu transitions remain outside this button change.

## Earlier transition baseline

Staging owner request: add smooth transitions to existing buttons and hover states site-wide. Existing Global Classes now store native Atomic transition controls at 200ms for background-color, color, border-color, box-shadow, opacity and transform. Existing hover outcomes, focus states, destinations, geometry and layout are unchanged; no new hover movement was added. Converter preserves native property/duration entries; easing remains the browser default ease.

Updated existing classes: service-card, text-link, image-led-card, city-link, process-timeline__number, card--interactive, card, button-primary, button-secondary, button-outline, service-card__action, button-outline-orange, button-outline-white, audience-card, card-action, audience-card__image, city-link__text, core-b-row, core-b-title, core-b-arrow, gcpro-footer-link, trust-logo.

Existing Header113 primary and utility menu transitions remain 160ms with their existing reduced-motion guard. No menu rewrite, new classes/components, custom CSS/JS, dependencies or asset changes. Existing class custom CSS unrelated to transitions is preserved. Shared classes apply to their existing consumers across pages; no per-page edits.

Verification: native saved transition property on primary button/card/trust-logo; authenticated Commercial frontend computed CTA and card transitions200ms, menu160ms. Static screenshot cannot demonstrate timing; computed render was checked. Owner final visual acceptance applies. No exhaustive device audit.

Editing: Elementor Design System → Classes → named class → transition controls. Rollback only these transition entries; preserve all other class properties and subsequent owner edits. Earlier exact transition values were not captured for every class; do not claim byte-exact pre-change recovery. No functional Before/After controls were changed.
