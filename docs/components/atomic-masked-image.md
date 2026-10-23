# Atomic Masked Image — staging prototype

Implemented 2026-10-23; owner visual approval pending. Scope: Water Damage Page514 only.

## Location and editing

- Page514: first Hero instance270ba3ed → **GCPRO — Water Masked Hero Prototype**, Component1453. [Edit page](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=514&action=elementor).
- [Edit isolated prototype definition1453](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1453&action=elementor). This is a native copy of1318 because the original has an image override, not a replaceable media-element slot. Original1318 and its other consumers are unchanged.
- Media element527d7a93, type `gcpro-masked-image`, inside Hero Media → Hero Media Frame. Existing layout/classes, H1, introduction and nested Emergency286/Call53/Request103 retained. Request still uses WordPress Internal URL to492.
- Select the Hero instance, open **Hero media**. **Photo** and **SVG Mask** are separate native Media Library controls. Photo remains1242. Mask1455 is the separate `gcpro-flow-mask.svg` silhouette.
- **Mask: SVG or None** restores a rectangle without removing either asset. **Photo fit** selects Cover/Contain. **Focal point X/Y (%)** positions the photograph independently; defaults50/50. Use per-instance overrides for future reuse; do not edit the definition to change a single instance's assets.

## Implementation and complexity

Authoritative source: `integrations/gcpro-atomic-masked-image/`. Installed as the standalone **GCPRO Atomic Masked Image0.1.0** staging plugin. Two PHP files plus one Twig template; no custom JavaScript, extra libraries, CDN, global classes or Variables. Registered through `elementor/widgets/register`, extends installed4.3.5 `Atomic_Widget_Base`, uses native Image/Select/Number controls and `Has_Template` for editor/frontend rendering.

The SVG is an independently replaceable Media Library attachment, never an embedded CSS path or permanent asset URL. The actual `<img>` receives CSS alpha `mask-image` and WebKit equivalent. No decorative overlay. Mask contain/center preserves proportions; a4:3 wrapper reserves space; native Hero columns handle responsive stacking. Existing image/srcset/alt metadata remains sourced from Media1242. The mask does not render as an accessible image.

Limitations: native Image selectors accept more than SVG, so select an SVG in the clearly labeled mask field. Frame ratio4:3 is fixed in this minimal prototype; X/Y and Fit are shared across breakpoints. Same photograph/mask adapt to all sizes. Atomic API compatibility is verified for Elementor4.3.5; recheck on major Elementor updates. No rollout to other pages.

## Essential checks

- Native editor lists the custom element under Atomic Elements; Page514 Hero exposes separate Photo and SVG Mask controls, Fit, None and X/Y.
- Both Media Library selectors were exercised with final existing assets1242/1455, then saved through Elementor. No duplicate photo upload or photo-file alteration.
- Editor preview: None removes mask CSS; X=30 changes `object-position` to30%50% without changing the photo; restored SVG mode and50/50. Final photograph remains1242. A test using alternate photo/mask files and a second-page reuse was not performed; those are not claimed as verified.
- Frontend `<img>` itself has the resolved SVG mask URL. Checked actual CSS widths360,393,430,768,1440: mask retained, no horizontal overflow. Desktop/mobile screenshots supplied for owner review. Desktop browser emulation, not physical-device testing.
- Page514's non-Hero children compared equal to the pre-change snapshot before final editor save. Production and1318 were not modified. Anonymous command-line request returned403; public delivery outside the authenticated staging session remains unverified.

## Rollback

Immediate visual rollback: set instance **Mask: None**, publish; original Photo1242 stays selected. Full architecture rollback: replace only Page514's first instance with existing Component1318 and the original Water overrides (H1/introduction, emergency label, phone/link, Request492, image1242). Pre-change page snapshot retained privately under `work/masked-hero/page514-before.json`; never commit the raw backup. Restore the original instance before deactivating the custom plugin. No core or third-party plugin edits were made.
