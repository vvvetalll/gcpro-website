# Shared Service Areas map integration

Staging owner: Atomic Component1140 plus Elementor Custom Code4134 (Body End, priority10, Entire Site). Native component links and Overrides are authoritative. Do not paste this runtime into consuming pages. Draft4104 now consumes the shared implementation without its old local HTML widget.

- `map-panel.html`: approved SVG geometry, compact controls and geographic footer.
- `map.css`: scoped approved layout/interaction styles; initial draft-only comment is historical provenance.
- `map.js`: central initializer, native destination resolution, pointer/keyboard/touch interactions, duplicate guards.
- `compile.py`: run `python integrations/service-areas-map/compile.py` from repository root to regenerate `custom-code.html`.
- `custom-code.html`: exact deployment artifact for4134; newline normalization on WordPress delivery is expected.
- `consumers.json`:21 published consumer browser checks,2026-11-03.

No runtime third-party dependency or geographic request. Existing site Elementor is required. Keep source and compiled artifact together. Do not deploy this staging-host-guarded code to production without a separate authorized migration. The inline payload is delivered sitewide despite component-scoped initialization.

[Task record, geographic provenance, responsive behavior, test limitations and surgical rollback](../../docs/components/service-areas.md#shared-interactive-map-rollout--2026-11-03).
