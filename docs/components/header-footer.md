# Header and Footer

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
