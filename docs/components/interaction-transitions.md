# Shared interaction transitions — 2026-10-23

Staging owner request: add smooth transitions to existing buttons and hover states site-wide. Existing Global Classes now store native Atomic transition controls at 200ms for background-color, color, border-color, box-shadow, opacity and transform. Existing hover outcomes, focus states, destinations, geometry and layout are unchanged; no new hover movement was added. Converter preserves native property/duration entries; easing remains the browser default ease.

Updated existing classes: service-card, text-link, image-led-card, city-link, process-timeline__number, card--interactive, card, button-primary, button-secondary, button-outline, service-card__action, button-outline-orange, button-outline-white, audience-card, card-action, audience-card__image, city-link__text, core-b-row, core-b-title, core-b-arrow, gcpro-footer-link, trust-logo.

Existing Header113 primary and utility menu transitions remain 160ms with their existing reduced-motion guard. No menu rewrite, new classes/components, custom CSS/JS, dependencies or asset changes. Existing class custom CSS unrelated to transitions is preserved. Shared classes apply to their existing consumers across pages; no per-page edits.

Verification: native saved transition property on primary button/card/trust-logo; authenticated Commercial frontend computed CTA and card transitions200ms, menu160ms. Static screenshot cannot demonstrate timing; computed render was checked. Owner final visual acceptance applies. No exhaustive device audit.

Editing: Elementor Design System → Classes → named class → transition controls. Rollback only these transition entries; preserve all other class properties and subsequent owner edits. Earlier exact transition values were not captured for every class; do not claim byte-exact pre-change recovery. No functional Before/After controls were changed.
