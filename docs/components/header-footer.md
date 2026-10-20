# Header and Footer

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

Root **1687d698** → container119ffe98 → columns73b78d01. Identity7ac91d92 holds logo **4eac9eb** (asset232,local width200px) and intro1432e75b. Navigation39be2867 holds heading3a510c5f and WordPress Menu **1faf8090**. Contacte424c2c holds heading769d5e75 and paragraph30cd7524. Bottom1d11b99e holds year **890602e** (native current-date-time) and identity23d35135.

Classes section,section--dark,site-footer,container,footer-columns/footer-column,footer-meta,stack/navigation-links; standard tokens. Native columns stack responsively. Footer-meta owns a white25% color-mix border fallback; navigation-links owns vendor menu-link typography. No Footer custom JS, Custom Code or shortcode.

## Shared maintenance and limits

Elementor Pro Theme Builder/nav-menu widgets render the chosen WordPress menu. Header/Footer were historically include/general/published; current structures and frontend were read, conditions were not changed. Edit content/layout in113/114, menu items in Appearance → Menus, shared class styles in Design System; edit native theme fallbacks only in their separate source scope.

Most navigation/request/utility URLs remain#. Individual menu-object bindings were not audited end-to-end here; logo binding is saved data. Do not convert unresolved links to guessed production routes or publish draft pages. Contact factual accuracy/email delivery, full navigation keyboard audit and broad site regression remain pending. E57 cleans header class CSS without changing effective styles. Footer classes/structure and theme PHP are unchanged.
