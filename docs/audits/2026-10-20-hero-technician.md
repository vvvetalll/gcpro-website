# Technician Hero background — E68

**Historical E68:** Superseded by approved E70 activation and E71 BEAF visual. Old root background CSS is removed; Media961 retained for recovery. [Current main Hero](../components/hero-main-beaf.md).

2026-10-20. Owner supplied photograph, then requested an independent brand gradient, protected head framing, and a bounded composition shifted right with a soft right edge on wide screens. Implemented/published on staging https://vitaliiv1.sg-host.com only.

## Exact owners and final behavior

- Homepage154 → Main46c3aad4 → Hero a62cdd3 → **local e-7cfcd182-d44a**. Existing section/section--dark tokens retained; existing hero--panorama g-708f717 detached from this instance so its old gradients/canvas cannot conflict. Class definition and historical source mirror remain intact for recovery/other consumers; no shared class edited/deleted.
- Media Library **961**, `/wp-content/uploads/2026/10/gcpro-restoration-technician-hero.png`: owner-provided1915×821 PNG,1,762,486bytes, unchanged artwork. Native WordPress uploader used; no generated replacement or new dependency. Hash recorded in settings evidence. Image and gradients are editable through Hero → Style → local → Background; native image item was inspected in Elementor. Saved CSS uses the verified uploaded URL; do not claim a separately verified attachment-object binding.
- Desktop: native right gradient, left gradient and photograph above inherited primary navy#1A327D. Shared canvas1440px wide, center shifted **+80px**; top anchored. Image height auto preserves aspect ratio. Left gradient protects copy; right fades from transparent through35% opacity at85% to full navy by95%, retaining navy through100%. No stretched photograph or vertically centered crop cutting the head.
- Tablet<=1024: native navy gradient98% opacity left,90% at45%,35% right; photo cover,75% horizontal/top focus.
- Mobile<=767: native navy gradient94%→86%; photo cover,80% horizontal/top focus. Replaces the earlier black temporary overlay. Photograph itself is unchanged; its baked-in shading remains underneath the brand overlay.
- Hero layout1514b1c → **local e-6aa4b4bf-93f3**: native tablet one-column grid, instead of narrow half-width copy that split RESTORATION mid-word.
- Copy6cc20521 → existing **local e-43714d85-88b2**: native tablet width100%/max600px; mobile width/max100%. Fonts/H1/copy/CTA text unchanged.
- Existing placeholder17c26181 → **local e-34f4998e-a98d**: native display:none base/mobile. Placeholder and label708a5ff2 retained for reversible recovery; no empty mobile image panel shown.
- Hero remains12 saved nodes; no new widgets, wrappers, Global Classes, Variables, Atomic Components, JS/PHP, plugin or animation library. Existing Components286/53/103, class tokens and gcpro-cta-origin hook6092e1ab unchanged. Header/Footer/Core/BEAF/Code903/Kit6/production untouched.

## Necessary converter CSS and editing

Hero local e-7cfcd182-d44a → Custom CSS owns only composition `background-size`, `background-position`, `background-repeat` at normal/tablet/mobile variants. Native Background owns the image/gradient layers. Native conversion cannot preserve the shared comma-separated canvas sizes and calculated position; its generated auto/0% defaults precede the explicit local composition declarations. Keep a single final composition block per variant; no important or authored numeric page/element selector.

Normal: sizes1440px100%,1440px100%,1440pxauto; position calc(50% +80px) top; repeat repeat,repeat,no-repeat. Tablet/mobile: auto auto,cover;75%/80% top;repeat,no-repeat. Solid gradients may repeat over the same navy fallback; photograph never repeats. Do not separately enqueue CSS or reattach legacy panorama styling.

[Exact before/after12-node settings and asset hash](2026-10-20-hero-technician-settings.json) are the authoritative recovery record. The older panorama integration mirror is historical for this instance, not another active deployment.

## Verification and limits

[Measurements](2026-10-20-hero-technician-qa.json):360,393,430,768,1024,1025,1440,1920,2560px Chrome responsive emulation. No document horizontal overflow or clipped H1/body/actions; placeholder hidden. Tablet600px copy and one-column grid verified after fresh publish; desktop original copy typography/structure retained. Mobile stacked actions preserved. Wide screenshots checked soft edge/relative placement; top anchoring protects head framing across tested sizes. Final right fade became opaque by95% to avoid a faint photo boundary.

Native editor Background image control and initial imported image item inspected; final saved styles and browser CSSOM separately read. SiteGround staging cache purged after final save and frontend reloaded. This run used an authenticated frontend; independent incognito/cache-HIT and real Android/iOS/notched-device tests are not certified. No full accessibility/Lighthouse/Core Web Vitals claim; original1.76MB PNG retained, image optimization/performance measurement remains an optional later scope.

Hero native CALL still tel:+18476563322; REQUEST SERVICE remains the existing unresolved# (not activated/represented as a working destination). Actual Tab moved CALL→REQUEST SERVICE with visible white outline. No phone call, form submission or placeholder action triggered. Smart Bottom CTA/controller/origin were not changed.

## Complexity and rollback

Only four existing local owners changed;12 Hero nodes preserved. Background/photo role is unique to this requested preview, so no speculative shared Component/Class. Legacy panorama class is detached rather than rewritten for other consumers. Full variant replacement removed abandoned overlay/position values; final snapshot contains final native layer controls plus necessary composition fallback only.

Rollback: restore four affected nodes' classes/local styles from the before array, using replace for styles; reattach hero--panorama to a62cdd3, clear its new local composition, remove new tablet layout/copy overrides, clear placeholder display override. Preserve all unrelated descendants/content/links and shared definitions. Publish154, purge staging cache, repeat responsive/CTA checks. Retain Media961 unless separately authorized to remove it; Git revert alone does not roll back WordPress. A full database/files restore was not tested.
