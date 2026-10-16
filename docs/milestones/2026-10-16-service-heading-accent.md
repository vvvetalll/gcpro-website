# E25 — Shared Service Card heading accent

2026-10-16. Staging Homepage154, Core Restoration Services38ed6da4; shared ROBYLO / Service Card62. Production and shared ROBYLO repository untouched.

## Implementation Summary

Added one native decorative Div block in the shared definition, rendering the same orange accent beneath all six service H3s. Line36×3px, radius2px, existing color-accent #F05A29. Heading, line and description use8px gaps. Existing typography/color, six SVG selections, content, CTA labels/dimensions and # destinations preserved. No optional accent hover: the always-visible detail meets the requirement without ancestor-state CSS or extra interaction complexity.

## Technical Changes

Component62 root6cd5ab9f now contains existing SVG4a4396ac, new Service Copy74f0f62a, and existing CTA210ecf0d. Service Copy contains original H3 4a877e1a, new Heading Accent336aa061, original description295090e4. Original node settings/style/interaction data and all five Override keys (icon/title/description/cta_text/cta_link) are unchanged. No instance edits or Homepage tree changes.

Two reusable native Global Classes are necessary; no existing class expressed either the small rounded bar or an8px responsive copy gap:

| Class | Purpose and justification | Editing |
| --- | --- | --- |
| heading-accent g-01bd1bd |36×3px orange bar, radius2px; neutralizes native Div padding/min-width. Reuses color-accent; reusable decoration, not a six-instance rule. | Edit Component62 → Heading Accent → Style → heading-accent; native Size, Spacing, Background, Border controls. |
| stack--tight g-19f58a6 |8px gap via existing space-xs. Existing stack--compact is16px; changing it would affect unrelated consumers. Existing stack supplies flex-column layout/reset. Desktop and mobile variants keep8px; priority before stack. | Edit Component62 → Service Copy → Style → stack--tight → Layout gap/responsive controls. |

Global Classes89→91; Variables36 and Components16 unchanged. New nodes have no local styles. New classes' custom_css fields are null; no custom CSS, JS, PHP, code files, plugins, dependencies, Variables or Components. Existing service-card, stack, icon-svg/service-card__icon and button-outline-orange/service-card__action reused. No global typography change: saved/rendered H3 remains Montserrat and existing color-text #334155, rather than introducing a new color override.

## Complexity Audit

One copy wrapper splits the original16px title/description gap into8+8px around the3px bar, preserving icon/copy/CTA spacing. Only two native nodes added per shared definition (5→7). No duplicate card, six independent decorations, semantic HR, hidden code or unnecessary hover. Existing class registry/order is preserved after filtering the two additions; Variables unchanged. [Saved scope audit](../evidence/2026-10-16-heading-accent/saved-audit.json), [native class data](../evidence/2026-10-16-heading-accent/native-classes.json).

Shared consumers, including existing Style Guide50 examples, inherit this definition; their content was not edited. Style Guide rendering was not separately rechecked in this milestone.

## Verification

- Actual anonymous Chrome1440/900/390px: six36×3px accents, #F05A29/radius2px; gaps8px above/below; no horizontal overflow. Personal Property Restoration wraps onto two lines with the accent below the complete heading. Equal-height desktop rows and bottom CTA alignment visually preserved. Mobile card heights increased exactly3px against baseline; desktop difference approximately3px with browser rounding. [Before/after metrics](../evidence/2026-10-16-heading-accent/qa.json), [desktop](../evidence/2026-10-16-heading-accent/1440.jpg), [mobile](../evidence/2026-10-16-heading-accent/390.jpg).
- Authenticated frontend1516px: same six accents/geometry/gaps. [Authenticated read](../evidence/2026-10-16-heading-accent/authenticated.json).
- Actual Homepage editor → Edit ROBYLO / Service Card: Navigator exposes Service Copy/Heading Accent. Selecting heading-accent displays native Width36px/Height3px controls; five Component properties remain. No temporary edits made. All seven local style arrays empty; new class declarations native with custom_css:null. [Editor verification](../evidence/2026-10-16-heading-accent/editor-verification.txt).
- Purged relevant staging cache through existing Purge SG Cache, reloaded actual logged-out Chrome. This is an anonymous normal profile, not controlled incognito. Supplementary PowerShell HTTP request returned403; no successful source/cache-header verification claimed from that client. [HTTP limitation](../evidence/2026-10-16-heading-accent/anonymous-http.json).
- Six links remain explicitly approved unresolved # placeholders; no new hardcoded destination. Decorative empty Div adds no focus stop/text; CTA interaction rules unchanged. No new animation/script/asset request. Keyboard/screen-reader/performance benchmarking not repeated for this noninteractive decoration.

## Outstanding Items / Recovery

Await visual approval. Incognito and physical-device tests not performed; mobile evidence is desktop browser emulation. Existing # destinations and E21 contrast limitation unchanged. No new functional blocker.

Scoped before backup outside Git: outputs/recovery/service-heading-accent-before.json. To revert natively, move original H3 and description back to root between SVG and CTA, remove only Heading Accent and Service Copy, then detach/remove the two new classes after checking usages. Original5 nodes/Override targets retained. Snapshot is not a tested full-site backup.
