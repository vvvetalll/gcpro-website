# Final CTA and video experiment

**2026-10-23 — Water mid-page CTA:** Page514 adds instance6ac76cde of existing Component80 immediately after process13056416 and before projects2ddea39a. Owner clarified that it must use exactly the lower CTA design, superseding the initial compact custom layout. Only title/description Overrides differ: “DEALING WITH WATER DAMAGE?” and “Talk to GCPRO about the damage and the next steps for your property.” Existing telephone tel:+18476563322 and native Internal URL Service Request492 retained. Component80 and original final instance5d8662e unchanged. No new shared definition, styles, classes, code, asset or dependency. Desktop and approximately394px mobile emulation confirm readable content, preserved destinations and no horizontal overflow; mobile inset20px and rounded card retained. Visual acceptance pending. Remove only6ac76cde to roll back; private pre-change Page514 snapshot work/water-mid-cta-before.json stays outside Git.

## 2026-10-23 — Shared card rollout

Owner explicitly requested this CTA presentation everywhere, superseding the earlier Home-only pending scope below. Implemented on the existing shared Component80; no new component or wrapper. Existing Home compact card remains page-owned and unchanged.

| Native owner | Current change |
|---|---|
|Section324d9854, local e-28c5a874-46d0|Mobile padding-block24px (`space-md`), padding-inline20px|
|Container79c33bf7, local e-79b18c32-8f52|8px radius (`space-xs`) and overflow hidden at all breakpoints|
|Actions460a04b7, local e-47c9dd0d-e5e3|Mobile width100%, column, stretch|

Current consumers: Home154, Residential484, Commercial499, Residential Water514 and retained Page50. All keep independent existing six Overrides. Nine saved nodes before/after; all content, tags, interactions and nested button references compare preserved. No new classes, Variables, Components, custom CSS/JS/PHP, assets or dependencies. Existing847 still controls inner mobile padding32px20px, video masks/opacity/motion/data guards and inner square corners; the native rounded outer frame clips it. This is the same approved containment method already used by the compact Home card. Do not add a second CSS/video owner to force the inner panel radius.

Native manage-elements changes to a component need the component publish lifecycle before becoming live. Readback after explicit publish confirms all three local styles. No full-tree rebuild or instance detachment was used.

**Actual browser QA:** logged-out Chrome Home/Residential/Commercial/Water at393px and1440px; Home additionally360px and768px. Zero horizontal document overflow. At393px shared card starts20px from the left,338px width (15px browser scrollbar), frame8px/hidden and actions298px wide/stacked. Both Home CTA frames match. At1440px final panel remains1136px wide; desktop layout/content retained. Home screenshot after scrolling confirms lazy video remains visible. Browser viewport reset. Fresh public frontend delivered the change without a cache purge. Editor login was not available, so no interactive editor-session QA is claimed; controls are native and saved readback verified. Physical-device, full keyboard/focus/motion/video lifecycle and performance were not re-certified by this geometry-only change.

**Links:** existing call telephone URIs preserved. Home compact/final Request Service remain pre-existing `#`; no navigation fix was substituted during this visual task. Current routes on other consumers retained.

**Recovery:** with owner authorization remove only the three added local style variants above (root mobile padding, container radius/overflow, actions mobile sizing), then explicitly publish Component80. Preserve the panel's pre-existing local radius e-69831b6e-42d0 and all content/Overrides/code. Private before/after snapshots stay outside Git. Refresh affected staging caches only if stale output is observed.

### Historical context (superseded mobile geometry)

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

## Completed geo cohort mid-page CTA rollout — 2026-10-29

Published one existing Component80 inset CTA per completed geo page, after local Projects and before local office/team. Same approved pattern as Water514; no new/shared definition or custom code. Supported city copy Overrides, verified Call destination and native Internal URL Content → Service Request492. Hero, BEAF, case selections, FAQ/final CTA and original trees preserved.11 empty Published legacy shells and Drafts were excluded; no publication-status changes.

| Page | Object | CTA instance | Review |
|---|---|---|---|
|Expert Restoration Services in Lombard|526|2db720ba|[Staging](https://vitaliiv1.sg-host.com/service-area/lombard/)|
|Downers Grove|527|4ed34b8c|[Staging](https://vitaliiv1.sg-host.com/service-area/downers-grove/)|
|Highland Park|528|56de8388|[Staging](https://vitaliiv1.sg-host.com/service-area/highland-park/)|
|Expert Restoration Services in Elmhurst|530|44f8056d|[Staging](https://vitaliiv1.sg-host.com/service-area/elmhurst/)|
|Expert Restoration Services in Naperville|532|797cdaca|[Staging](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|Expert Restoration Services in Glenview|533|762ace7|[Staging](https://vitaliiv1.sg-host.com/service-area/glenview/)|
|Expert Restoration Services in Oak Brook|536|31d2d016|[Staging](https://vitaliiv1.sg-host.com/service-area/oak-brook/)|
|Carol Stream|543|2fd16e08|[Staging](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|
|Expert Restoration Services in Northbrook|556|28491194|[Staging](https://vitaliiv1.sg-host.com/service-area/northbrook/)|
|Schaumburg|558|4d33796|[Staging](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|

Readback verified all10 placements/copy/native destinations; removing each new CTA node yields its exact original tree. Lombard desktop/mobile and structurally different Naperville desktop rendered correctly: mobile gutters20px, stacked buttons, no overflow. Component80 native radius retained. Private recoverable before/after snapshots remain outside Git. Sanitized verification is in `docs/evidence/2026-10-29-geo-mid-cta.json`.
