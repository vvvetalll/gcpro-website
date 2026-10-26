# Header menu refinement — 2026-10-23

## 2026-10-26 — selective dropdown actions

Owner-approved minimal CSS exception: existing menu5 items1102/1103 Request Service→Page492,262 View All Service Areas→495 and263 All Projects→1132 now have `gcpro-menu-action`. Their native object links, hierarchy, order and existing classes are retained. Header's main CTA and ordinary links are unchanged.

Existing Header113 → Nav Menu7983af36 → Advanced Custom CSS is the sole owner. Two appended scoped rules add a thin brand-orange border,6px corners,10×14px padding,8px top gap and pale-orange hover/focus. Existing focus-visible outline/reduced-motion rules remain. [Source mirror](../../integrations/header-primary-menu.css) is not separately enqueued. No new widgets, duplicate links or scripts.

Saved menu objects and frontend computed styles confirm all four actions in desktop/mobile markup have orange borders and original destinations. Mobile toggle opens with Enter and Residential submenu opens. Full pointer interactions on desktop were not certified separately. Native controls cannot target selected WordPress items; the owner explicitly authorized this existing-owner CSS exception. Rollback removes only the appended rules and the semantic class on these four items.

Published on staging only. Shared Theme Builder Header113 retains its existing structure: utility navigation4ebecbc6 (menu15), identity/logo, primary navigation7983af36 (menu5), existing Request Service component56 and smart-navigation controller903. No menu destinations, labels or hierarchy changed.

## Presentation and owners

The existing legacy Nav Menu widgets remain inside the Atomic Header. Native pointer is None. Each widget owns its own Advanced Custom CSS, with explicit generated Header/widget scoping to prevent utility/main style leakage. Source snapshots: [primary](../../integrations/header-primary-menu.css), [utility](../../integrations/header-utility-menu.css). These files are recovery/reference sources, not another deployed stylesheet.

Primary navigation: Inter15px/600, navy text, pale-blue interaction surface, restrained orange active indicator. Utility navigation: Inter13px/500, white text on the existing navy strip, translucent white hover. White dropdowns use14px text,12px corners and a soft shadow. Existing logo, CTA, main white background, utility navy background and global layout tokens are preserved. Explicit !important declarations override established legacy Header rules within these two widgets only.

At the existing1200px collapse breakpoint, the native toggle opens a white scrollable panel with16px/600 top-level text,52px rows, subtle separators and softer nested submenus. Widget position becomes static so the dropdown anchors at the existing relative Header Inner2a03c167 bottom. Zero top margin and square top corners remove the navy gap between Header and panel. No arbitrary pixel header offset or new JavaScript.

Visible keyboard focus and reduced-motion support retained. Native Elementor/SmartMenus still owns opening, closing and submenu behavior. No new widget, class, component, asset, plugin, library or dependency; two existing widget CSS owners only. Code903 and emergency CTA895 are unchanged.

## Checks and limitations

Authenticated Homepage desktop: both navigation styles render independently; Residential dropdown opens with its existing12 destinations. Mobile browser emulation at approximately394 CSS px: toggle and nested Residential submenu open/close, panel meets Header without a navy gap, menu scrolls, and no horizontal page overflow. This is browser emulation, not a physical-device test. Guest Homepage HTTP200/MISS references the current Header stylesheet and the stylesheet contains both menu revisions and mobile-panel rules. Guest browser interactions and exhaustive device/page matrices were not tested. The shared Header supplies the change to all its existing page instances. Final visual acceptance belongs to the owner.

## Recovery

Private pre-change Header snapshot: workspace work/menu-refinement-before.json, excluded from Git. Restore only the two original widget local styles and pointer=underline, then publish Header113; do not restore the entire Header over newer owner edits. No WordPress menu/content rollback is necessary.
