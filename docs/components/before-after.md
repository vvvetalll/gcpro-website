# Before / After

Three project comparisons; plugin records own the images and comparison behavior, Atomic owns the surrounding layout.

## Location and structure

Homepage154/main46c3aad4 → section **4221ba60** → container14d7e71c; heading instance6b4663fc →71; grid **66b1c7d4**; portfolio instance2364d92a →59.

| Project wrapper → image wrapper → Shortcode widget | Saved shortcode | Caption title |
| --- | --- | --- |
| 22e7aed8 →33681ad8 →**eb597a1** | [bafg id="723"] | 0fccf2a, residential fire/Tinley Park |
| b72017c →55241554 →**6a2a094** | [bafg id="742"] | 3a39c79b, water/Glenview |
| 31087133 →5f199388 →**961e3c2** | [bafg id="767"] | 5931ddb6, garage fire/Northbrook |

Shortcodes freshly read in the visual editor; actual images rendered. Slider record IDs are required plugin references. Do not replace them with guessed IDs after migration.

## Styles, JavaScript and dependencies

Atomic grid/local controls own three/two/one columns at desktop/tablet/mobile,16px media/caption gaps and22px desktop/tablet,20px mobile project titles. Shared heading/container/section/grid-3 classes and font/color tokens apply to native text.

**Homepage154 → Page Settings → Advanced → Custom CSS** owns inline/popup labels and all expand buttons. Fresh editor/CSSOM inspection confirms body.elementor-page-154 and grid data-id66b1c7d4 selectors. Popup content is body-mounted, outside the Atomic section, so an ordinary section descendant cannot alone scope it. This is a documented existing exception, not a reusable styling convention. [Register and migration proposal](../CUSTOM_CODE.md).

Plugin CSS/JS owns handles, clipping and fullscreen Ajax: **Ultimate Before After Image Slider & Gallery–BEAF4.7.21 + BEAF Pro4.5.7** (some asset URLs still say4.5.6). jQuery/twentytwenty and plugin popup code are vendor dependencies. No GCPRO-developed comparison JS or Custom Code entry. No HTML widget.

## Behavior and safe modification

Inline labels9px/60% opacity; popup labels11px/white on black55%, AFTER shifted48px to clear close control. Fullscreen buttons36px,44px on mobile/coarse pointer; visible focus outline uses one necessary !important because the plugin suppresses focus outlines. Transparent inline label background also uses !important. Preserve documented plugin override exceptions until a verified alternative replaces them.

Edit images/options in WordPress → Before and After Slider → matching record; captions/grid in Homepage; labels/buttons only in the page CSS field. Do not edit generated uploads/elementor/css files. Reusable scoping should use a semantic comparison class plus a reliable popup-owner hook, with inline/popup consumer tests; removing body scope blindly would affect other comparisons.

393px fullscreen723 opened and closed in Chrome with document/popup width393 and no horizontal overflow; page grid checked360/393/430/768/1440. All three inline pairs rendered. Current handles are DIVs with no role, tabindex or ARIA value: keyboard slider semantics are missing. Fullscreen fit-to-window/keyboard coverage, physical-device and anonymous access remain separate QA. Historical endpoint403/security issue is not resolved by disabling site security in this audit. Portfolio still#; Northbrook location remains owner-unconfirmed.
