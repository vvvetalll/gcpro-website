# Shared Service Areas map integration

Staging owner: Atomic Component1140 plus Elementor Custom Code4134 (Body End, priority10, 21 explicit published-page conditions). Native component links and Overrides are authoritative. Do not paste this runtime into consuming pages. Draft4104 retains its native shared instance but is outside the published-page allowlist; use a published consumer for the enhanced preview.

- `map-panel.html`: approved SVG geometry, compact controls and geographic footer.
- `map.css`: scoped approved layout/interaction styles; initial draft-only comment is historical provenance.
- `map.js`: central initializer, native destination resolution, pointer/keyboard/touch interactions, duplicate guards.
- `compile.py`: simplifies only decorative land rings to a maximum 0.45 SVG-unit deviation, using Shapely already used by the Census builder; featured municipalities/water remain exact. Run `python integrations/service-areas-map/compile.py` from repository root to regenerate `custom-code.html`.
- `custom-code.html`: exact deployment artifact for4134; newline normalization on WordPress delivery is expected.
- `consumers.json`:21 published consumer browser checks,2026-11-03.

No runtime third-party dependency or geographic request. Existing site Elementor is required. Keep source and compiled artifact together. Do not deploy this staging-host-guarded code to production without a separate authorized migration. The inline payload is emitted only on the 21 page IDs in `consumers.json`. Add a native Elementor Include → Singular → Pages condition when adding a consumer. The SVG remains inline and has no independent cache entry; no new network failure mode was introduced.

[Task record, geographic provenance, responsive behavior, test limitations and surgical rollback](../../docs/components/service-areas.md#shared-interactive-map-rollout--2026-11-03).

Runtime 1.1.0 matches verified native URL paths to GEOIDs, tolerates partial unmatched lists, and leaves native labels/destinations authoritative. Native links provide keyboard navigation and focus highlighting; the SVG is a single descriptive image, not 12 additional tab stops. Arrow keys on zoom controls pan while zoomed. Published pages initialize once after DOM readiness without a body MutationObserver. The active Elementor editing canvas retains its native editable tree; test the enhanced view through frontend Preview Changes. No page definitions, map CSS, CTA styles or coverage claims changed.

[Optimization measurements, current tests, limitations and rollback](../../docs/components/service-areas.md#technical-optimization--2026-11-03).
