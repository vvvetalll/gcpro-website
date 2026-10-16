# E28 — Residential / Commercial photograph trial

E29 below supersedes only the Residential attachment; E28 describes the original paired-image trial.

2026-10-16, America/Chicago. Authorized staging only: vitaliiv1.sg-host.com, Homepage154. Visual trial; owner approval pending. E27 copy proposal was not implemented.

## Implementation Summary

Uploaded the two supplied scene images as native Media615 (residential house) and616 (commercial downtown Chicago), with descriptive alt text. Optimized delivery copies preserve the square compositions at1440×1440, WebP82, with no retouching. [Assets/source provenance](../../assets/images/homepage/README.md).

Only photo presentation changed in section7b416658. Existing card4c8810dc/photo frame6e5afc98 now contains Atomic Image295bf90e; card2066a26/frame4c8bb651 contains Image27ec40d5. Replaced placeholder paragraphs1e618ea6/5f6ea042. Both existing frames use layout-reset instead of section--light/media-placeholder. Full saved Homepage tree comparison confirms other node settings, all card bodies, descriptions, H3s, arrows, links and other sections unchanged. No Header/Footer/Component/production changes.

## Technical Changes

One new **native Global Class audience-card__image g-77c2a17** is shared by the two images: display:block, width100%, height:auto, aspect-ratio4/3, object-fit:cover, object-position50%50%. All six rules converted to native Atomic properties; saved custom_css:null, image/frame styles[] empty. Existing classes inspected first: media-placeholder includes padding, border/background and flex placeholder layout; image-led-card is a parent layout; header-logo has logo-specific constraints. A single photograph class avoids altering unrelated consumers or duplicating per-image styles. Edit via Image → Style → class → Size/Show more. No new Component, Variable, custom code, plugin or external dependency. Classes90→91, Components16/Variables36 unchanged.

Both native image controls bind attachment IDs with Full resolution, independently selectable in General → Content → Select image. Native WordPress alt text and responsive srcset render. Existing audience-card retains24px radius, overflow:hidden and border. No empty image widgets or added wrappers. Aspect ratio4:3 rather than16:9 retains more vertical truck/building context; separately inspected both images and retained centered positioning for each. No source pixels were destructively cropped. A rendered16:9 comparison was not retained/performed; this choice is based on the square compositions and verified4:3 output.

## Complexity Audit

Reused existing frames and card/body/arrow trees, replaced two paragraph nodes with two image nodes: unchanged node count, no extra nesting/components or per-image classes. One shared native media class is the only style addition. No hidden styling, widget Custom CSS, HTML widget, inline styles, theme/shared ROBYLO changes, JS/PHP or dependency. Old media-placeholder rules remain intact for all other placeholders. Existing generated frame class names were preserved; their saved local styles remain empty.

## Verification

Purged staging via the native Purge SG Cache toolbar action. Actual ordinary frontend in a separate logged-out Chrome profile has no logged-in body class/admin bar, includes both current images, and loads them successfully. This was not an incognito or physical-device test. Authenticated frontend and actual Elementor editor also checked; both image General/Style controls accessible, shared native class selected in editor, no detaching required. No temporary content edit was needed to inspect controls; replacement/save/reload persistence itself was verified.

| Actual CSS viewport | Equal card height | Equal image height / ratio | Result |
| --- | --- | --- | --- |
|1440 |554.13px |416px /4:3 |Both images load, vehicles/logos retained, corners preserved, no horizontal overflow |
|1200 |548.38px |410.25px /4:3 |Same; single aligned pair |
|900 |487.46px |297.75px /4:3 |Same; tablet pair, wrapped headings/descriptions accommodated |
|390 |430.02px |261.50px /4:3 |Stacked pair, all vehicles/logos visible, no clipping or overflow |

At900 the first immediate observation preceded responsive-image loading; subsequent read and screenshot confirmed both loaded successfully. No image errors in captured guest browser error log. Width/height attributes plus native ratio reserve image geometry; no layout shift observed, but no formal CLS/performance benchmark or slow-network measurement was run. Native srcset selected1024px derivatives on tablet/mobile. Existing two linked cards remain intentional # placeholders; unchanged, not working category destinations. No new navigation target or hardcoded internal link introduced. No new interactive behavior; card keyboard behavior was not retested in this image-only task.

Evidence: [Desktop1440](../evidence/E28/anonymous-1440.jpg), [1200](../evidence/E28/anonymous-1200.jpg), [Tablet900](../evidence/E28/anonymous-900.jpg), [Mobile390](../evidence/E28/anonymous-390.jpg), [native editor](../evidence/E28/editor-native-image.jpg), [native properties/measurements](../evidence/E28/verification.json).

## GitHub

Assets, this milestone, PROJECT_CONTEXT, CHANGELOG, DESIGN_SYSTEM and ELEMENTOR_MAP updated in gcpro-website/main. Commit/push and remote SHA verification recorded in the final task report; Git does not deploy WordPress content. Shared ROBYLO repository unchanged.

## Outstanding Items and Recovery

Owner visual approval pending; no final image acceptance or marketing-copy approval implied. Physical-device/incognito and formal performance/CLS checks not run. Existing category # destinations remain pending approved public objects.

Scoped before/after Homepage154 and audience JSON snapshots are outside Git at project outputs/recovery/homepage154-before-images.json, homepage154-after-images.json and audience-images-before.json. They are configuration recovery references, not a full site backup or tested restore. Originals remain untouched in Downloads. To reverse, remove only the two new image children, restore the two original paragraph labels and photo-frame classes from the scoped snapshot using native Elementor controls, save/publish staging, purge cache and recheck anonymous output. Restore photo aspect ratio centrally in audience-card__image if only the trial framing is rejected. Keep Media615/616 available; do not permanently delete assets or remove a class while used.

## E29 — Alternate Residential photograph trial

2026-10-16, America/Chicago. Owner requested the supplied From Concept to Completion.jpg as a Residential visual trial. Uploaded native Media621, GCPRO Residential Pickup Outside House, descriptive alt in [asset register](../../assets/images/homepage/README.md). Existing Image295bf90e selects621 instead of615; Full resolution/native srcset. Shared class audience-card__image,4:3 cover/center and all other settings retained. Separately inspected framing: full main pickup, wheels/logo and house remain visible. Source's embedded vertical lettering remains part of the photograph; no new overlay or image editing beyond resize/compression.

**Complexity:** No new classes, components or custom code. No new Variables/plugins/dependencies, DOM or styling changes. Full saved Homepage tree/node-count comparison shows only Image295bf90e attachment reference changed; Commercial616/27ec40d5 and all other nodes match baseline. Existing # destinations preserved and still unresolved. Existing Media615 retained; source JPG unchanged. OptimizedWebP1440×1440,395,462 bytes versus1,437,882 original.

**Verification:** native staging cache toolbar purge, anonymous ordinary Chrome frontend at1440/1200/900/390; both images loaded, equal card heights554.13/548.38/487.46/430.02px, same4:3 frames, no horizontal overflow, rounded corners/body/copy/arrows preserved. Native editor image controls rechecked; authenticated frontend shows621 and new alt. Desktop/mobile emulation, not physical-device/incognito, screen-reader or formal CLS/performance test. Evidence: [1440](../evidence/E29/1440.jpg), [1200](../evidence/E29/1200.jpg), [900](../evidence/E29/900.jpg), [390](../evidence/E29/390.jpg), [measurements](../evidence/E29/verification.json). Initial desktop capture preceded stable screenshot rendering and was replaced by the settled pair view.

**Editing/reversal:** Homepage154 → Residential Restoration Photo → General → Content → Select image. Choose retained Media615 to restore E28's truck-group image; no class/layout change needed. Scoped fresh Homepage snapshot before this change is outside Git at project outputs/recovery/homepage154-before-pickup.json; not a full backup/tested restore. Staging only; no production/shared ROBYLO changes. Visual approval pending. Documentation/assets/evidence committed to gcpro-website/main; final report records push/remote SHA.
