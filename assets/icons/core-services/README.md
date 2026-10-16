# GCPRO Core Restoration Services — original SVG proposals

**Current E24 refinement:** B remains approved. Its Mold icon is now a navy spore with an orange cleaning sparkle (Media607); the previous shield remains in Git history. Existing badge class now displays artwork36px inside56px. Five other B designs unchanged. [Current deployed screenshots and technical record](../../../docs/milestones/2026-10-16-icon-refinement.md). E22 concept sheets below are historical32px/shield studies, not current deployed previews.

2026-10-16 · E22 source study / E23 staging integration · **Owner selected B; its six icons now used on staging Homepage154. A remains an unused alternative.** [Attachment IDs, native import method and actual QA](../../../docs/milestones/2026-10-16-icon-b-integration.md).

Twelve original, hand-authored vector assets for the six existing Service Card62 instances in Homepage154 section38ed6da4. No third-party icon library, raster tracing or generated bitmap is used. The two treatments deliberately share recognizable silhouettes so a future switch need not change service meaning.

## Concepts

**A — Essential Outline:** pure single-color rounded outline. Quiet, precise and flexible. All strokes use `currentColor`; the native host should supply the existing navy icon color. Without a host color a standalone SVG/image can fall back to black. No fixed orange details.

**B — Restoration Accent:** navy #1A327D structure plus selective #F05A29 orange service details, with limited filled areas. Approved for GCPRO's light service cards. Water level, ember, mold cleaning sparkle, repair joint/beam, lightning and packing band are the accents. A's older shield is a service metaphor, not a certification claim.

Both: `viewBox="0 0 48 48"`, transparent background,2.25-unit stroke, round caps/joins, no fixed display dimensions. SVGs contain only svg/g/path; no text, fonts, scripts, CSS, external references, filters, masks, embedded images or editor metadata. Geometry stays within a safe margin. Source part names are readable; B uses `ink`/`accent` groups and semantic path IDs. IDs are not used as CSS hooks.

## Source assets

| Existing service | A: monochrome | B: accent |
| --- | --- | --- |
| Water Damage | [SVG](a-outline/water-damage.svg) | [SVG](b-accent/water-damage.svg) |
| Fire & Smoke Damage | [SVG](a-outline/fire-smoke-damage.svg) | [SVG](b-accent/fire-smoke-damage.svg) |
| Mold Remediation | [SVG](a-outline/mold-remediation.svg) | [SVG](b-accent/mold-remediation.svg) |
| Reconstruction | [SVG](a-outline/reconstruction.svg) | [SVG](b-accent/reconstruction.svg) |
| Storm Damage | [SVG](a-outline/storm-damage.svg) | [SVG](b-accent/storm-damage.svg) |
| Personal Property Restoration | [SVG](a-outline/personal-property-restoration.svg) | [SVG](b-accent/personal-property-restoration.svg) |

## Preview and intended placement

[All12 icons](../../../docs/previews/core-service-icons/concept-comparison.png), [A cards desktop](../../../docs/previews/core-service-icons/cards-a-desktop.png), [B cards desktop](../../../docs/previews/core-service-icons/cards-b-desktop.png), [A mobile](../../../docs/previews/core-service-icons/cards-a-mobile.png), [B mobile](../../../docs/previews/core-service-icons/cards-b-mobile.png). Matching SVG presentation sheets are in the same preview folder for vector inspection. Presentation sheets contain labels/backgrounds; **only the12 individual SVG files are icon assets**.

Card-context sheets are offline approval mockups using the existing56px badge/32px artwork, card surfaces, content and compact CTA labels. They do not prove live Elementor rendering or propose changes to card dimensions/text/destinations. Montserrat/Inter were used for offline preview text. No functioning preview buttons or new website runtime exist.

## Native Elementor import and future reuse

E23 verified: generic WordPress Media upload rejects SVG, while existing instance → SVG Icon → Upload SVG → native Media modal imports these static assets successfully. Use that native SVG-specific entry point; no unrestricted-upload setting or new importer is needed. B colors survived on all six actual instances. The below guidance remains applicable to future reuse; independently adjustable native color channels are still not established.

1. Select a concept; import only the chosen six sanitized SVGs through the existing authorized SVG Media Library workflow. Do not enable unrestricted SVG uploads or install plugins. Current upload permissions were not retested during this asset-only task.
2. Use existing native Atomic SVG element4a4396ac in Service Card62, exposed `icon`/SVG Icon Component Override. Select the corresponding attachment independently on each Homepage instance; retain the component, badge classes and all other Overrides. Do not paste SVG into HTML widgets or detach components.
3. Reuse `service-card__icon` g-b759e84 and `icon-svg` g-b84ed52; A's currentColor should inherit the existing navy color when SVG is rendered inline by the native element. An ordinary img element does not inherit page currentColor into an SVG image document.
4. B explicitly stores both brand colors in its logical groups/filled paths. Do not promise independent dual-color picker overrides: these new assets have not been imported/tested. If native controls cannot preserve both channels, edit the clearly named source groups and re-import a revised asset through normal controls. No CSS selector workaround or recoloring plugin is needed.
5. Verify two different instance assets persist independently, both colors survive native rendering, and no existing SVG style flattens accents. Check24/32px, desktop/mobile, decorative accessibility semantics, anonymous delivery/cache and visual editability before deploying. Service headings already communicate meaning, so icons should remain decorative without duplicate announcements.

All future approved changes use the project documentation/commit/push workflow. No production or shared ROBYLO changes authorized by these proposals.
