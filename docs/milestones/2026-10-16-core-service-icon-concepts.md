# E22 — GCPRO original Core Services SVG concepts

2026-10-16 · Asset proposal only · Homepage154 section38ed6da4 / future Service Card62 SVG Override. Neither staging nor production modified. E21 button styling, all existing components/styles/URLs and shared ROBYLO remain unchanged.

## Implementation Summary

Created two complete original sets of six service icons: A Essential Outline/currentColor and B Restoration Accent/navy-orange. Same48×48 construction grid,2.25-unit rounded strokes, transparent backgrounds and consistent semantic silhouettes; B adds selective solid/open accent details. Recommend B on the existing light cards for brand recognition; A is the maximum-recolorability option. Both remain proposals until approval.

## Technical Changes

Canonical12 assets and style/import guide: [assets/icons/core-services](../../assets/icons/core-services/README.md). Two directories, one file per service. B has readable ink/accent groups and path names; A inherits currentColor through an inline SVG host. No third-party icon set copied. No new Global Classes, Variables, Atomic Components, website custom code, plugins or runtime dependencies.

New offline artifacts: [comparison](../previews/core-service-icons/concept-comparison.png) and desktop/mobile card mockups for both concepts, each with SVG source and PNG export. They exist solely to review the proposed assets in current card proportions; not a new design system, browser page or live Elementor implementation. Temporary HTML/CSS previews were removed in favor of these self-contained static deliverables. No preview CSS/JS/PHP remains in the repository.

Offline authoring rendered SVGs with resvg-py, installed only under local task outputs; this is not a website/repository dependency. Montserrat/Inter TTFs from the Google Fonts repository were used locally for preview typography, not bundled/deployed. Font sources: google/fonts ofl/montserrat and ofl/inter. Authoring scripts and tool packages are outside Git; final SVG source is directly editable and requires no generator.

## Complexity Audit

No site-side abstractions, icon framework, sprite loader, wrappers, CSS rules or component duplication. Exactly12 source icons; five vector presentation sheets and PNG companions are approval artifacts. Removed unneeded HTML/CSS preview scaffolding. No animations, filters or external SVG assets. Existing native media/SVG Override is the recommended later integration; no new plugin or control system.

## Verification

- XML parse/allow-list checks on all12 source files: identical viewBox/stroke/caps/joins, only svg/g/path elements, no script/events/style/href/url references or embedded rasters; logical monochrome/duotone color channels verified. [Structural record](../previews/core-service-icons/asset-validation.json).
- All12 exact SVGs rendered offline at24/32/64/384px. Alpha bounds leave margins at384px; no clipping or broken geometry. [Render record](../previews/core-service-icons/render-validation.json).
- Visually reviewed the full12-icon comparison, both desktop card sets at1440px and mobile390px compositions. Typography/content remain readable; cards stack; no icon clipping. Static compositions only, not responsive browser/runtime tests. Native accessibility/overrides/import tests remain pending because no assets were installed.
- Browser file-protocol preview was blocked. Did not bypass browser policy or expose a local server; inspected independently exported SVG/PNG artifacts instead. No live authenticated/anonymous checks or SiteGround purge needed: no website settings/assets/code changed.

## Outstanding Items

Owner chooses A or B; then a separately authorized integration can import the selected six assets and test native Component Overrides, color preservation, independent instances, responsive frontend/cache delivery and accessibility. Current permission/security restrictions were not changed or retested. Do not claim native per-channel duotone recoloring; source colors are explicit and editable. No new claims, certifications, destinations or functional behavior.

Delete the new proposal asset/preview folders and revert documentation to withdraw the study; no WordPress rollback needed. Normal Git milestone commit/push/remote verification applies.
