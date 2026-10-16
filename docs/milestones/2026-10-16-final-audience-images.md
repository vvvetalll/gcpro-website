# Final audience photographs — E31

2026-10-16, staging Homepage154 only. Owner supplied final wide photographs; visual approval pending.

## Implementation Summary

Native Atomic Image295bf90e selects Residential WebP629 instead of621; Image27ec40d5 selects Commercial WebP630 instead of616. Original JPG uploads627/628 preserved, as are older trial attachments. Alt text identifies the branded pickup outside a house and restoration trucks on a downtown Chicago street. Existing copy, linked-card hierarchy, arrows and destinations unchanged.

## Technical Changes

Both source JPGs1152×648 were converted without resize, upscale, cropping or retouching to WebP quality82/method6: Residential166,906 bytes; Commercial134,152 bytes. Repository assets are in assets/images/homepage. Native Full image selection retains WordPress responsive delivery. Existing audience-card__image g-77c2a17 native aspect ratio changes4:3→16:9 to match the supplied composition exactly, reducing image height25%. Cover/center remains unchanged; matching source/frame ratio avoids additional default crop.

No new classes, components or custom code. No new Variables, plugins or dependencies. Images remain individually editable in Homepage154 → respective Photo → General → Content → Select image. Shared ratio remains in Image → Style → audience-card__image → Size/Show more. No other class property changed in E31.

## Complexity Audit

Full saved Homepage before/after comparison: only the two image attachment settings differ; node count/structure unchanged. No duplicated frames, local styles or new nesting. Existing E30 hover CSS was preserved, not modified for this task; its previously pending source/documentation is synchronized separately below.

## Verification

Published staging154 and purged native SiteGround cache. Ordinary logged-out Chrome frontend, not incognito or physical-device testing:

| Viewport | Each image, CSS px | Equal card height, CSS px |
| --- | --- | --- |
|1440 |554.67×312 |450.13 |
|1200 |547×307.69 |445.81 |
|900 |397×223.31 |413.02 |
|390 |348.67×196.13 |364.65 |

Both assets loaded at all widths, main vehicles/logos visible, equal frames, existing24px corners and hidden overflow retained. No horizontal overflow or observed shift; no formal CLS/slow-network test. Actual native editor Image controls show Select image/Full and final alt/source. Desktop hover retains orange arrow, white glyph, scale1.025 and stationary card. Keyboard focus remains visibly outlined. Existing two # category links remain intentionally unresolved; no link changes or hardcoded destinations introduced.

Evidence: [1440](../evidence/E31/1440.jpg), [1200](../evidence/E31/1200.jpg), [900](../evidence/E31/900.jpg), [390](../evidence/E31/390.jpg), [hover](../evidence/E31/desktop-hover.jpg), [focus](../evidence/E31/keyboard-focus.jpg), [measurements](../evidence/E31/verification.json).

## GitHub

Sources, evidence, asset register, PROJECT_CONTEXT, CHANGELOG, DESIGN_SYSTEM and ELEMENTOR_MAP synchronized in gcpro-website/main; final report records commit/push/remote verification. Git does not deploy WordPress. Shared ROBYLO repository and production untouched.

## Outstanding Items

Visual approval; incognito and physical-device checks not performed. Existing placeholder links pending. Scoped prechange recovery JSON remains outside Git in project outputs/recovery/homepage154-before-final-photos.json and classes-before-final-photos.json. Restore621/616 and4:3 via native controls for E29 framing; these are configuration references, not a full backup or tested restore.

## E30 carryover — existing audience hover, documented without new deployment

The earlier hover refinement was deployed before E31 but its Git documentation was pending. Existing Global Classes audience-card g-38b29fb, card-action g-a5c0d65 and audience-card__image g-77c2a17 retain native280ms border/background/transform transitions. Native self-hover cannot control nested image/arrow; the authorized minimal parent→child exception lives in **Global Class audience-card → normal → Custom CSS**, not a widget/local field, theme or Code590. It is centralized in that existing class and scoped to its two verified154 consumers.

[integrations/audience-card-hover.css](../../integrations/audience-card-hover.css) is a readable canonical mirror, **not separately enqueued**. In the Global Class editor replace .audience-card with &; retain the editor's generated wrapper. Fine-pointer hover changes nested .card-action background to var(--color-accent), image transform to1.025, border to a35% primary/border color mix. Direct .layout-reset clips the image; focus-visible colors the arrow. Native controls retain geometry, typography, tokens and transition settings. No added classes, Components, Variables, JS, PHP, plugins or DOM. Publish native Global Class changes before testing frontend; connector conversion can omit media-query CSS, so verify actual served rules.

Current preservation checks confirm ordinary anonymous output, focus outline and stationary card. Touch does not rely on hover. **Reduced-motion limitation:** transitions are disabled, but the more specific existing hover selector retains instantaneous zoom; do not describe this as fully suppressed zoom. No CSS correction was made in the image-only E31 scope. Prior E30 baseline JSON remains outside Git in outputs/recovery/audience-classes-before-hover.json; rollback its scoped class properties via native controls, publish, purge and retest.
