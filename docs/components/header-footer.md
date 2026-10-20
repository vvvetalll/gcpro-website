# Header and Footer

**Current E64,2026-10-20:** Global Footer114 refreshed with quiet CTA, native responsive grid, individually separated service/contact rows, Chicago/Chicagoland context and grouped copyright/Home. Existing menu remains in Header only. New classes gcpro-footer-link g-373d928/gcpro-footer-item g-aca1669; existing103/286 and tokens reused. Root-scoped orange interaction accents maintain white text contrast.903 CSS moves the mobile reserve into the navy footer; Header113 behavior unchanged.154 native Hide Title removes the unwanted theme title. [Current full structure, code owners, destinations, responsive rules, limitations and rollback](../audits/2026-10-20-footer-refresh.md); [saved settings](../audits/2026-10-20-footer-refresh-settings.json).

**E63,2026-10-20:** Existing Header113 instance18849090 still references895 globally; its label/phone overrides remain.895 now contains existing Primary53 and Emergency Mark286, rendering orange Call Now and24/7 beside Emergency help. Header positioning/menu/controller unchanged. [Exact IDs and class owner](../audits/2026-10-20-mobile-cta-orange-247.md).

**Current E62,2026-10-20:** Code903 starts first downward hiding at fixed entry without a40px pause and seeds the animation from the current flow position, eliminating fast-gesture bounce. Subsequent40px down/24px up tolerance, native menu/focus pinning and reduced motion remain. The bottom panel also stops auto-hiding for ordinary phone buttons, including main content. No Header113/Footer114/CTA895 saved settings changed. [Full verification and rollback](../audits/2026-10-20-process-cta-transition.md).

**E61,2026-10-20:** Code903 now ignores plain footer telephone links for competing-action suppression, retaining mobile Call Now through the footer. Main-content call actions, menu/form/overlay rules remain. No Header113/Footer114 or CTA895 definition changes. Core native layer correction also removes the need for E60's intro-intersection hiding gate. [Current verification and rollback](../audits/2026-10-20-section-layers-footer.md).

**Current E60,2026-10-20:** Code903 now enters fixed positioning at a matching top edge and pins Header for open menus/keyboard-visible focus only. Retained pointer focus after closing the menu no longer blocks downward hiding. Movement distance resets while pinned. Two full pointer cycles per360/393/430/768 and separate touch393 pass; native Header113/Atomic/menu definitions remain unchanged. [Current evidence, limitations and rollback](../audits/2026-10-20-header-cycle-fix.md).

**Historical E59,2026-10-20:** Corrected the utility-row40px displacement on pointerdown, but did not cover subsequent down-scroll with retained toggle focus. Its focus behavior is superseded by E60. [Original evidence](../audits/2026-10-20-menu-focus-fix-results.json).

**E58,2026-10-20:** Header113 remains global include/general. Existing shell4ef1aa21 gains gcpro-smart-header; a separate new root Div block feba833/instance18849090 mounts reusable895 outside the moving shell. Shared Code903/Entire site/body-end5 controls direction/menu/focus behavior. Original shell children/styles/links and Footer are unchanged. [Exact structure, classes, visual controls, new code and rollback](smart-navigation.md); this supersedes older “no Header JavaScript” statements below.

Separate Theme Builder documents, not children of Homepage154. Re-read assignments before shared edits.

## Header113

Root **4ef1aa21** → information bar72aaeb6f → row1f7b9126 → links35ada30 (273b2dbd/1853f25b/4979c34). Main inner **2a03c167** → identity22f189ae/logo **72df1b0c**, WordPress Menu **7983af36**, CTA **cd66895 →56**.

Classes site-header,info-bar,info-row,info-links,info-text,header-row,header-brand/header-logo and navigation--primary; existing fonts/navy/white/border/spacing tokens. Logo uses native Internal URL to Page154; menu selects robylo-primary. Desktop navigation becomes native Menu Toggle/dropdown on mobile; expanded393px menu stays within viewport. No custom menu JavaScript or Custom Code entry.

**Custom CSS owners:** Design System Classes navigation--primary,header-row,info-row,info-bar,info-links,info-text,site-header. E57 removes verified superseded declarations and replaces numeric menu coupling with **& .gcpro-menu-item--header-hidden { display:none }** in navigation--primary desktop Custom CSS. Appearance → Menus → ROBYLO Primary → Resources item242 → CSS Classes now stores gcpro-menu-item--header-hidden. Only that menu field changed; Header hides Resources, Footer keeps it visible. [Exact owners/QA/rollback](../audits/2026-10-20-phase1-cleanup.md). No blind removal or generic .elementor-item refactor.

## Footer114

Root **1687d698** → container119ffe98 → quiet CTA671c4f66, columns73b78d01, coverage5245645d and bottom1d11b99e. Identity7ac91d92 retains logo **4eac9eb** (asset232/200px) and intro1432e75b, adds existing286 instance bdfaa44. Services39be2867 contains heading7ffa59b5 and six native informational rows. Contacte424c2c retains native robylo-contact ID, now heading779deb5e, phone641a5869/email25e52737/address2a44b1ed and Directions37cec545→103. Copyright group578307c4 holds existing native year **890602e** and identity23d35135; Home5a520a4e is a native154 object link. Footer V3 menu1faf8090 removed in E64; WordPress menu and Header consumer retained.

Existing section/section--dark/site-footer/container/stack/footer-column/footer-meta/heading-label/layout-reset classes and tokens reused. Two new reusable classes gcpro-footer-link g-373d928 and gcpro-footer-item g-aca1669 own plain actions and eight separated rows. Native local grid is3 desktop/2 tablet/1 mobile columns. Footer root owns scoped orange hover/focus overrides and divider style/color converter CSS; Code903 supplies mobile panel clearance inside .site-footer. No Footer JS, separate Custom Code entry or shortcode. [Exact values and locations](../audits/2026-10-20-footer-refresh-settings.json).

## Shared maintenance and limits

Elementor Pro Theme Builder renders the global Header/Footer, both include/general/Published/active at E64 readback. Header uses the unchanged WordPress menu; Footer uses native Atomic rows/actions. Edit content/layout in113/114, Header menu items in Appearance → Menus and shared class styles in Design System. Footer hover/focus exceptions are local to its root;903 remains the single scroll-controller entry.

Header/request/utility unresolved URLs remain#; Footer has only verified telephone/mail/Maps/Home actions, while service/city rows stay informational until real business destinations are published. Do not guess routes or publish Drafts for navigation. E64 verifies footer hover/focus, responsive wrapping and Maps destination; physical devices, independent incognito/cache-HIT, email delivery, broader Header route audit and full restore remain pending. Theme PHP and production were not edited.
