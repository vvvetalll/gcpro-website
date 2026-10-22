# How We Work

**2026-10-22 — native heading alignment:** Component582 H3s39735454/6a28b840/7ee454a0/7f4076aa now reserve two existing1.3em line boxes with native Atomic `min-height:2.6em` on desktop. Tablet/mobile reset to0px for natural wrapping. No copy, numbering, circles, connectors, interactions, shared classes, typography or existing animation code changed. See [Water final refinements](water-damage.md#final-ui-refinements--2026-10-22).

**E77 current:** Complete original section now shared1152 (nested582 retained), Homepage6d0939b9/Residential5412e337. Code590 source unchanged, Entire-site native condition enables identical touch sequence. Source4681b8f5 is historical. [Current exact locations and checks](residential-services.md).

**Current E62,2026-10-20:** Code903's implicit competing-phone rule, not Process styling, caused Call Now to disappear during section entry: the preceding Emergency Support call button was still on screen. That rule is removed globally. Full entry/inside/exit sweeps in both directions at360/393/430 now retain the panel;768/1440 keep it hidden. E61's section-center check missed this transition. Component582/590/native section settings remain unchanged in E62. [Evidence and rollback](../audits/2026-10-20-process-cta-transition.md).

**E61,2026-10-20:** Homepage section4681b8f5 local native style e-1ed92cbb-13f6 now owns z-index0, containing internal timeline layers. No sticky positioning or z9999 was found here; numbers use existing necessary z1. Component582, its overrides/classes, Code590 and theme ripple CSS are unchanged. At mobile360/393/430 the global Call Now remains visible through Process; section exit hit tests show no remaining Process layer over subsequent content. [Exact change and limits](../audits/2026-10-20-section-layers-footer.md).

Four-step explanation: Contact → Assessment → Restoration → Review. Homepage content remains native Atomic; decorative effects are explicitly separate.

## Location and structure

Homepage154/main46c3aad4 → section **4681b8f5** → container **4a8f9eb5**. Eyebrow35bc6a06; section-heading instance **5494e63e →71**; Process Steps5a7e87b2 → instance **79a67ca3 → Component582**.

Component582 root **16ae2220** has four step articles7984adb7/2f3b9293/33a931c1/77469dc6. Numbers43b49516/cc0c097/28f4497/2679cdee; connectors e0cbfd7/71b5b770/78f0dfd0 between the first three steps; copy wrappers hold each H3 and description. Twelve supported overrides expose each step's number/title/description.

## Styles, code and dependencies

Global Classes process-timeline g-a12d836, process-timeline__step g-07d3365, process-timeline__number g-e17507d, process-step-number g-af5ab08, process-timeline__connector g-261ecb6, plus standard section/container/stack. Uses font-heading/body, color-primary/primary-hover/accent/white and existing spacing tokens.

Native class controls own base layout, circles, typography and transitions. Desktop parent-hover ripple CSS is appended to **active theme robylo-starter/assets/css/fallback.css**; canonical client block [theme-overrides/process-timeline.css](../../theme-overrides/process-timeline.css). No separate enqueue. Theme file updates can overwrite this block.

**Elementor Custom Code590**, “GCPRO / Process Timeline — Mobile Sequence”, published, body-end priority10, Page154 condition, contains [CSS](../../integrations/process-timeline-mobile.css) and [JavaScript](../../integrations/process-timeline-mobile.js). Saved source matches these files after whitespace normalization on2026-10-20. Always load jQuery is unnecessary; this integration uses native APIs. No timeline shortcode/HTML widget/additional plugin; requires Elementor Pro Components/Custom Code.

## Behavior, limits and safe reuse

Horizontal desktop/tablet timeline becomes vertical on mobile. Fine-pointer hover triggers two1000ms rings160ms apart, plus1160ms number color. Touch/coarse-pointer IntersectionObserver plays once at10% visibility, with400ms step offsets, then unobserves; reduced-motion gates suppress the decorative sequence. CSS class hooks are reusable; the **display condition** is intentionally Page154-only. A native page condition is an acceptable document reference, not CSS coupling.

Edit page-specific copy through the12 instance overrides; edit shared structure only in582 after consumer checks. Another page needs its own intentionally chosen Custom Code condition; copying the Component alone does not deploy590. Changing step count also requires reviewing nth-child delays and connector logic. Do not detach582 or add an observer per step.

Current audit checked storage/source agreement and responsive layout, not a new end-to-end animation timing, physical-device, screen-reader or performance certification. Prior animation QA remains dated in the milestones. No new JS/CSS was deployed by this audit.
