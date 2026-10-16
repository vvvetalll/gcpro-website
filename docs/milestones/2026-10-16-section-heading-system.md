# E26 — Optional H2 section accents; remove card H3 accents

2026-10-16, GCPRO staging. This supersedes E25's service-card decoration following the owner's in-task instruction: remove H3 accents. Production, Header/Footer and shared ROBYLO source untouched.

## Implementation Summary

Five Homepage154 informational H2s now have a40×3px orange line, radius2px,16px below the full heading. Existing heading text, Montserrat typography, colors, semantics and component content remain. Emergency, Why GCPRO, Testimonials, Hero, Final CTA and Footer headings receive no new decoration. On owner direction, removed all six existing service-card H3 bars and their copy wrapper; cards retain original five-node layout and five Overrides.

## Technical Changes / Native capability findings

Audited Section Heading71: root1ba080c, Title66d8f464, Description2d2aa2b4. Three supported Overrides: title, heading_tag, description. Actual instance panel confirms these fields. Native Div schema exposes tag/link; Divider exposes no content/visibility properties. No supported visibility/style toggle for a decorative line was verified, so none was invented. Adding a line to71 by default would affect excluded consumers.

Instead, use one optional reusable **Global Class section-heading--accent g-a537304** on the existing native container directly holding71. Component71 itself and its three Overrides remain unchanged. This is the minimum CSS exception: a scoped generated empty ::after, no DOM node, widget CSS, local style, JS, theme code or plugin. Existing stack, color-accent and space-sm are reused. The old heading-accent class required a real decorative node and could not provide optional selective H2 decoration without adding markup.

Canonical mirror: [integrations/section-heading-accent.css](../../integrations/section-heading-accent.css). It is **not** an additional loaded stylesheet. Deployed source is the existing Elementor kit's GLOBAL class → Custom CSS, not an individual container's local Custom CSS. Selector in that editor: `& > .stack > h2::after`. The source mirror uses the explicit class selector. No broad HTML Default or sitewide h2 rule.

| Selected H2 / Component71 instance | Existing container with opt-in class |
| --- | --- |
| Residential & Commercial /300decb5 |1b98920a |
| Core Restoration Services /44ad547c |5ddaa828 |
| How We Work /5494e63e |4a8f9eb5 |
| Projects & Before / After /6b4663fc |14d7e71c |
| Service Areas /2554ebe8 |3dc285eb |

Other Homepage71 consumers2631f818/68cd33d2/13bdbfdf are excluded. Style Guide50 has two71 consumers5dc391e1/1e5f5dc9 under6ac9b7dd; no opt-in class was added there. Nested Component consumers were read as part of the16-definition audit; no71 definition changed or default accent was added.

**Editing:** Navigator → corresponding existing container → Style → Classes: attach/remove section-heading--accent. Text/heading level/description stay in the71 instance's normal controls. For line geometry, select the GLOBAL class button first, then Custom CSS; width40px/height3px/radius2px live in this one documented rule. Color and upper spacing use existing Variables. Geometry is a CSS edit, **not** claimed to be native size sliders. Current approved headings are all start/left aligned; centered/right-aligned future variants require a scoped alignment review before reuse. Do not alter stack or broad H2 defaults to align the line.

Service Card62: moved original H3 4a877e1a and description295090e4 back between SVG4a4396ac and CTA210ecf0d; removed Service Copy74f0f62a and Heading Accent336aa061. No text, icons, CTA configuration, dimensions, existing class rules or Override targets changed. Native class usage scan plus all16 Component definitions showed no remaining references to E25 heading-accent g-01bd1bd / stack--tight g-19f58a6; removed both obsolete classes. Classes91→90 net (one added, two removed). Variables36 and Components16 unchanged.

## Complexity Audit

One optional class and one short centrally managed pseudo-element rule replace manual decorations. No new wrappers/components/assets/JS/PHP/plugins/dependencies. H3 removal reduces Component62 from7 to5 nodes. Full saved Homepage compares equal to baseline after removing only the five new class attachments; original card nodes/settings match after the specified structural removal. [Saved scope audit](../evidence/2026-10-16-section-heading-accent/saved-audit.json), [native class](../evidence/2026-10-16-section-heading-accent/native-class.json), [class usage scan](../evidence/2026-10-16-section-heading-accent/class-usages.json).

## Verification

- Actual logged-out Chrome frontend1440/1200/900/390: exactly five H2 pseudo-element accents, each40×3px/#F05A29/radius2px/16px upper gap; zero H3 pseudo accents and zero old decorative Divs. No horizontal overflow. Residential/Core/Projects wrap on390 with line below the complete heading. Existing navy/dark sections retain white headings without accidental accents. All selected lines align with their existing start-aligned H2. [Metrics](../evidence/2026-10-16-section-heading-accent/frontend.json).
- Actual authenticated IAB also shows five H2 accents/no H3 accents. [Authenticated](../evidence/2026-10-16-section-heading-accent/authenticated.json). Final [desktop](../evidence/2026-10-16-section-heading-accent/1440-core.jpg), [mobile Core](../evidence/2026-10-16-section-heading-accent/390-core.jpg), [mobile Areas](../evidence/2026-10-16-section-heading-accent/390-areas.jpg) visually inspected.
- Actual Elementor Navigator/Style displays opt-in class on the existing Core container; selecting that GLOBAL class displays the scoped CSS. No verification edits. Existing71 content controls still present; local CSS remains untouched. [Editor evidence](../evidence/2026-10-16-section-heading-accent/editor-verification.txt).
- Purged staging SiteGround cache after final card/class changes, reloaded ordinary public root in genuinely logged-out normal Chrome profile. Controlled incognito and physical-device tests unavailable/unperformed; mobile evidence is browser emulation. No universal visitor claim from an authenticated preview.
- All saved links/content unchanged; existing # destinations remain documented unresolved placeholders. The empty generated line adds no reading content, focus stop or animation. No new asset requests/scripts; formal screen-reader/performance benchmark not performed.

## Outstanding Items / Recovery

Visual review pending. Native visibility Override unavailable; optional class attachment is the supported fallback, geometry requires its documented centralized CSS. Future centered/right-aligned heading treatment is not verified. Existing destination/contrast issues outside this decoration remain unchanged.

Disable H2 accents by removing class from the five listed containers; remove the global class only after usage review. H3 decoration stays removed per owner. Scoped recovery snapshots outside Git: outputs/recovery/section-heading-accent-before.json and section-heading-accent-card62-before.json. E25 node/class values remain in prior history/evidence if explicitly requested later; do not restore them blindly. No tested full-site restore claimed.
