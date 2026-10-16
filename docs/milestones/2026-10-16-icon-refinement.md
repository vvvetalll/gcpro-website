# E24 — Service icon scale and Mold Remediation refinement

2026-10-16. Homepage154 Core Restoration Services38ed6da4. Owner approved B and requested only larger artwork plus a clearer mold symbol. No production/shared ROBYLO changes.

## Implementation Summary

Increased native SVG artwork32→36px (**12.5%**) inside the unchanged56×56 light-blue badges. Replaced B's mold shield with a navy spore and small orange cleaning sparkle. All six share centered36px SVG boxes; five other source designs and Media references596/597/599/600/601 remain unchanged.

## Technical Changes

- Existing `service-card__icon` g-b759e84: native padding12→10px only; width/height56px, rounding14px, background Variable, margins and other properties unchanged. The SVG fills the36px inner area. No local styling or SVG transforms/custom CSS needed. Edit in Elementor Service Card62 → Service Icon → existing Global Class → padding. The same shared icon size naturally applies to existing Service Card examples; no example content was edited. The class-usage scanner returned no direct page usages for the nested badge class, so its output is not evidence that no shared consumers exist.
- Updated only [B mold source](../../assets/icons/core-services/b-accent/mold-remediation.svg): same48×48 viewBox,2.25-unit rounded stroke and explicit navy/orange groups. Replaced shield paths with spore body/branches/details and cleaning sparkle. Other five source files match previous Git content exactly. Old source remains in parent commit6fdc620 and earlier history; no duplicate source variant added.
- One new reusable native **Media607**, mold-remediation-1.svg, imported through existing instance SVG Icon → Upload SVG → Media modal. Existing Mold instance4ac87e43 icon Override598→607; old Media598 retained. Existing Component62 definition/default icon/all five Overrides unchanged. Edit selection via the instance's standard SVG picker; edit artwork/color groups in the canonical SVG and re-import normally. No per-channel color picker is claimed.

**No new classes, components or custom code.** No new Variables/plugins/dependencies. No card spacing, button, typography, card background or layout rule was authored. Theme/PHP/JS/Header/Footer untouched.

## Complexity Audit

One existing class property and one icon Override suffice. No wrappers, new style abstractions, duplicate component, CSS selectors, inline styling, transform workaround or additional runtime. Native class readback shows custom_css:null and matches the before definition after changing only padding. Core section tree matches before after changing only Mold attachment; Component62 tree unchanged.

Full-page scope comparison also observed an unrelated addition of existing section--light g-1834399 on Residential during the task interval. Origin is not established; none of the authored operations requested this addition. It was left intact to preserve unrelated state rather than silently removed. Do not claim the entire Homepage differed solely by Mold. [Saved audit](../evidence/2026-10-16-icon-refinement/saved-audit.json).

## Verification

- Actual anonymous Chrome1440/900/390: all six SVG boxes36×36 inside56×56 badges, horizontal/vertical center offsets0, both brand strokes retained, Mold has four new paths. Existing CTA heights44px/# destinations preserved, no overflow or clipped artwork. Visual optical-weight/alignment review on desktop/mobile screenshots; uniform stroke system retained. [Frontend](../evidence/2026-10-16-icon-refinement/frontend.json), [desktop](../evidence/2026-10-16-icon-refinement/1440.jpg), [mobile](../evidence/2026-10-16-icon-refinement/390.jpg).
- Authenticated frontend also measures36px artwork/56px badges for all six. Before/after card sizes remain visually stable; minor subpixel rounding differs between browser captures. [Before](../evidence/2026-10-16-icon-refinement/before.json), [authenticated](../evidence/2026-10-16-icon-refinement/authenticated.json).
- Reloaded actual Homepage editor; selected Mold: standard SVG Icon/Upload SVG controls, content/link Overrides, attached component and disabled Publish visible. Native class resource verifies only padding changed and no custom CSS. [Native class](../evidence/2026-10-16-icon-refinement/native-class.json).
- New source XML checked and rendered offline at96/36/24px; served Media607 parsed as static svg/g/path,48×48 and2.25 stroke with both colors/no shield. The five other B source hashes equal previous Git versions. Native staging cache purged; anonymous browser and ordinary HTTP200/HIT deliver new spore/cleaning paths. [Source/cache evidence](../evidence/2026-10-16-icon-refinement/source-and-http.json).

## Outstanding Items / Recovery

Visual approval pending. Controlled incognito and physical-device tests were not performed; responsive checks are desktop browser emulation with a genuinely logged-out normal Chrome profile. Existing # destinations and E21 CTA contrast limitations unchanged. Separate Residential class delta above remains of unknown origin; not part of the icon refinement.

Restore badge padding12px and Mold Override598 to revert this task; previous media/source retained. Scoped local before snapshots: outputs/recovery/icon-refinement-before.json and icon-refinement-class-before.json, outside Git. These are not a tested full-site backup. Historical E22 concept sheets remain dated snapshots showing the older shield/32px artwork; current screenshots above supersede them for deployed B.
