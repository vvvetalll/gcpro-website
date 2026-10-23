# Final CTA and video experiment

**2026-10-23 — approved mobile card correction, NOT IMPLEMENTED:** The owner supplied a mobile screenshot of Home's compact Emergency Restoration Support card and requested the bottom Home CTA use the same inset-card presentation on mobile: visible side gutters, rounded card corners and surrounding breathing space, preserving its own copy, buttons and final-CTA role. This is also the default for future CTA sections until explicitly changed by the owner; see [permanent design rule](../DESIGN_SYSTEM.md#permanent-cta-card-presentation--owner-instruction-2026-10-23). Immediate target is Home154 final instance37feb023 →80; recorded locators below are historical and require a fresh native read before editing. No mass change of other consumers is authorized.

The current Work environment was reset and `/root/mcp-config.json` is absent. No WordPress, Elementor, class, video-code or browser changes were made in this task; no current frontend/editor/responsive verification is claimed. Restore the authorized MCP connection before implementing. Never reconstruct credentials from chat history or silently change editing channels. The repository change records the owner's rule and the still-pending implementation, not completion of the mobile fix.

**2026-10-22 — compact Home consumer:** Home Emergency Restoration Support section6cde656f now uses native panel1c4978f9 with the existing cta-panel semantic hook, reusing847's actual846 video/masking/opacity/motion fallback. Its219px desktop card is shorter than the original267.578px final panel; original80, its Home instance, styles and847 code remain unchanged. Native outer-frame clipping preserves rounded mobile corners without altering the existing final-CTA media rules. [Current layout, owners, preservation checks and existing Request # limitation](emergency-response.md). This is reuse of the existing staging mechanism, not a newly installed video renderer.

**E77 current:** CTA80 is shared unchanged design/content Overrides. Native panel5ec4592 now owns8px radius, obsolete Homepage local rule removed. Existing847 is Entire site, semantic .cta-panel initialization, same original video/mobile/reduced-motion behavior; no duplicated script. Earlier Homepage-only experiment notes below are historical. [Current exact locations and checks](residential-services.md).

Native Component80 supplies reusable copy/actions. **A separate live Custom Code experiment847 modifies its rendered instance.** Absence of a saved video widget does not mean absence of a runtime video.

## Location, children and overrides

Homepage154/main46c3aad4 → instance **37feb023 → Component80**. Definition root **324d9854** → container79c33bf7 → panel **5ec4592** → copy7c20b93d (H2 2aca64be, paragraph12ea707c) and actions460a04b7 (nested53 instance699f9898; nested103 instance6aa9a1a0).

Supported overrides: title,description,cta_text,cta_link,secondary_text,secondary_link. Homepage primary calls tel:+18476563322; secondary REQUEST SERVICE is#. Edit these overrides independently, not shared button defaults.

## Native styles versus active code

Classes section,container,cta-panel g-e1d4327,section--dark,stack,cluster and existing button classes; existing navy/accent/white/font/spacing tokens. Native Component/class controls own normal layout and color. Homepage main local style **e-685133d2-110f** contains the sole radius exception: & .cta-panel { border-radius:8px; }. E57 removed its authored interaction-ID dependency while retaining the local main scope and current single-panel contract; shared80 is unchanged.

**Custom Code847**, “GCPRO / EXPERIMENT — Final CTA Video (staging only)”, published, body-end priority1, Page154 condition. Exact CSS/JS are stored together in that code editor and mirrored in [integrations/cta-video-experiment.html](../../integrations/cta-video-experiment.html), not separately enqueued. Component80/theme/widgets do not store the video code. [Code register](../CUSTOM_CODE.md#custom-code-847--live-final-cta-video-experiment) owns technical details and rollback.

847 queries .gcpro-homepage .cta-panel, adds gcpro-cta-video-test and gcpro-cta-section-test classes and injects an aria-hidden/inert video layer using attachment846's staging MP4 URL. E57 adds the visual-neutral Atomic scope gcpro-homepage g-d0c199c only on154/main46c3aad4; exactly one panel matches. No new Component.

## Responsive behavior and interaction

Native CTA is inset desktop with wrapping copy/actions. 847 adds a right-side masked,40%-opacity screen-blended video layer; mobile≤767 moves it to the lower right,70% height/34% opacity, removes outer gutters and forces square corners plus32px/20px panel padding with !important. Local panel overflow:hidden intentionally contains decorative video bleed; this is not a body/html overflow workaround.

IntersectionObserver300px preload margin, passive scroll/requestAnimationFrame, resize and visibility listeners coordinate muted/loop/playsinline playback and pause offscreen. Reduced motion and Save-Data skip/remove video; reduced-motion CSS hides the layer. Existing media remains an experiment; no playback/performance/contrast certification is claimed here.

## Safe editing, debt and rollback

Keep instance copy in native overrides, shared appearance in Atomic, experimental media in847. Do not add another active video script or enqueue a repository mirror. The source retains its staging host/media URL and native Page154 condition; authored page/element numeric selectors were removed E57. It lacks a native editable video widget; it is a documented staging exception, **not a portable Component feature**.

Before a structural replacement, review a native video/background-video composition or semantic opt-in class contract, consumer effects, fallback poster, mobile geometry, motion/data preferences and source portability. Obtain owner approval for that change. E57 changes only scope/panel selectors; all other847 source is unchanged. [Saved locations, regression evidence and rollback](../audits/2026-10-20-phase1-cleanup.md).

Rollback of847: set the existing Custom Code entry to Draft through WordPress, reload/purge staging cache and verify native CTA. This removes script-added classes/layers on fresh load; native8px rule remains. Do not remove847 solely because older E55 docs called video unplaced. Request route and final video decision remain pending.
