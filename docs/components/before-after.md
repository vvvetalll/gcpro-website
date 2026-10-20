# Before / After

**Current E66,2026-10-20:** A later explicit owner request authorizes shared presentation-only correction. Existing Kit6 Site Settings Custom CSS now owns restrained10px dark-translucent/white labels and36px desktop/44px mobile expand buttons,16px glyph, orange focus. No page-ID dependence in the new style. Historical Homepage CSS below was absent on fresh native read; do not restore alongside Kit6. Plugin files/shortcodes/records/images/handle code unchanged. [Exact source, tests, limits and rollback](../audits/2026-10-20-beaf-presentation.md). The following E57 boundary and earlier CSS record are historical Phase1 evidence.

**Phase1 boundary (E57):** BEAF Pro is an existing third-party plugin and is entirely excluded from refactoring. Its files, shortcodes, CSS overrides, popup behavior, selectors and Elementor integration are untouched. Necessary Homepage/page-body/grid/slider scoping is an intentional isolation exception, not an automatic architecture defect. Rendered BEAF page CSS equals the E56 baseline byte-for-byte; [verification](../audits/2026-10-20-phase1-cleanup.md).

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

**Current owner: Kit6 → Site Settings → Custom CSS.** Shared plugin-class selectors style inline/body-mounted popup labels and expand buttons; source mirror integrations/beaf-presentation.css. Homepage154 Custom CSS was empty on fresh E66 native read. The former body.elementor-page-154/grid data-id66b1c7d4 override is historical, not a parallel current owner. The E57 isolation exception was intentional at that time.

Plugin CSS/JS owns handles, clipping and fullscreen Ajax: **Ultimate Before After Image Slider & Gallery–BEAF4.7.21 + BEAF Pro4.5.7** (some asset URLs still say4.5.6). jQuery/twentytwenty and plugin popup code are vendor dependencies. No GCPRO-developed comparison JS or Custom Code entry. No HTML widget.

## Behavior and safe modification

Current labels10px/white on black60%, ordinary opacity1; popup AFTER clears close control by56px. Expand buttons36px desktop/44px mobile or coarse pointer,16px white existing SVG, black52% background, subtle border, orange hover/focus. Vendor focus suppression requires one scoped !important. No GCPRO comparison JavaScript. Edit media/options in existing BEAF records; Atomic owns captions/grid; Kit6 owns presentation. All3 inline drags and all3 fullscreen open/close tested at1440/393; six-width layouts tested. Existing non-keyboard handle/close semantics remain a vendor limitation. See E66 for exact evidence and recovery.

Historical E56 verification:

393px fullscreen723 opened and closed in Chrome with document/popup width393 and no horizontal overflow; page grid checked360/393/430/768/1440. All three inline pairs rendered. Current handles are DIVs with no role, tabindex or ARIA value: keyboard slider semantics are missing. Fullscreen fit-to-window/keyboard coverage, physical-device and anonymous access remain separate QA. Historical endpoint403/security issue is not resolved by disabling site security in this audit. Portfolio still#; Northbrook location remains owner-unconfirmed.
