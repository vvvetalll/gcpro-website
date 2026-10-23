# Header menu refinement — 2026-10-23

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
