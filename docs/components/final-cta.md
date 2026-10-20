# Final CTA and video experiment

Native Component80 supplies reusable copy/actions. **A separate live Custom Code experiment847 modifies its rendered instance.** Absence of a saved video widget does not mean absence of a runtime video.

## Location, children and overrides

Homepage154/main46c3aad4 → instance **37feb023 → Component80**. Definition root **324d9854** → container79c33bf7 → panel **5ec4592** → copy7c20b93d (H2 2aca64be, paragraph12ea707c) and actions460a04b7 (nested53 instance699f9898; nested103 instance6aa9a1a0).

Supported overrides: title,description,cta_text,cta_link,secondary_text,secondary_link. Homepage primary calls tel:+18476563322; secondary REQUEST SERVICE is#. Edit these overrides independently, not shared button defaults.

## Native styles versus active code

Classes section,container,cta-panel g-e1d4327,section--dark,stack,cluster and existing button classes; existing navy/accent/white/font/spacing tokens. Native Component/class controls own normal layout and color. Homepage main local style **e-685133d2-110f** contains the sole radius exception: & [data-interaction-id="5ec4592"] { border-radius:8px; }. This is an existing per-instance override with unnecessary element coupling; it was not moved into a shared class without consumer review.

**Custom Code847**, “GCPRO / EXPERIMENT — Final CTA Video (staging only)”, published, body-end priority1, Page154 condition. Exact CSS/JS are stored together in that code editor, not in Component80, the theme or an HTML widget. [Code register](../CUSTOM_CODE.md#custom-code-847--live-final-cta-video-experiment) owns technical details and rollback.

847 queries .elementor-154 .cta-panel[data-interaction-id="5ec4592"], adds gcpro-cta-video-test and gcpro-cta-section-test classes and injects an aria-hidden/inert video layer using attachment846's staging MP4 URL. No new Atomic class/component was created by the experiment or by this audit.

## Responsive behavior and interaction

Native CTA is inset desktop with wrapping copy/actions. 847 adds a right-side masked,40%-opacity screen-blended video layer; mobile≤767 moves it to the lower right,70% height/34% opacity, removes outer gutters and forces square corners plus32px/20px panel padding with !important. Local panel overflow:hidden intentionally contains decorative video bleed; this is not a body/html overflow workaround.

IntersectionObserver300px preload margin, passive scroll/requestAnimationFrame, resize and visibility listeners coordinate muted/loop/playsinline playback and pause offscreen. Reduced motion and Save-Data skip/remove video; reduced-motion CSS hides the layer. Existing media remains an experiment; no playback/performance/contrast certification is claimed here.

## Safe editing, debt and rollback

Keep instance copy in native overrides, shared appearance in Atomic, experimental media in847. Do not add another active video script or enqueue a repository mirror. The source hardcodes host, page, element and media URL and lacks a native editable video widget; it is a documented staging exception, **not a portable Component feature**.

Before a structural replacement, review a native video/background-video composition or semantic opt-in class contract, consumer effects, fallback poster, mobile geometry, motion/data preferences and source portability. Obtain owner approval for that change. No experimental code was deleted or refactored in this audit.

Rollback of847: set the existing Custom Code entry to Draft through WordPress, reload/purge staging cache and verify native CTA. This removes script-added classes/layers on fresh load; native8px rule remains. Do not remove847 solely because older E55 docs called video unplaced. Request route and final video decision remain pending.
