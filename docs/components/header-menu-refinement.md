# Header menu refinement — 2026-10-23

## Editorial pilot and quiet menu actions — 2026-10-30

Implemented on staging with ui-ux-pro-max guidance. Single Post123 and synced core pattern3159 remain the existing owners. Pale-blue full-width opening uses the site container, breadcrumb, white rounded topic chip, gray Montserrat700 H1, excerpt, two compact native publication/modified-date chips with decorative calendar/clock glyphs, and one4:3 featured image to the right; core Columns stack on narrow screens. Dates remain actual Post Date blocks; no invented byline, reading time, buttons, reviews or emergency mark. Body remains white with a centered760px reading column, Inter body text, gray Montserrat H2/H3, blue ordinary-weight links without orange underlines, and retained visible focus. User requested photo in the opening rather than duplicated below it.

Pilot Post2046 [Water Damage at Home: What to Do First](https://vitaliiv1.sg-host.com/what-to-do-if-you-notice-water-damage-in-your-home/) retains reviewed wording, URL, publication status, SEO fields, original date and featured media. Safety guidance is a warm#FFF7ED native Group with8px corners and NO colored side rule; existing factual observations form a pale-blue checklist. All six headings have native anchors with180px scroll offset. No TOC inserted because the short article does not need one. Three unsynced native patterns3435 Safety note,3442 Key points and3443 On this page are available in WordPress Patterns; inserted copies remain independently editable. Adjust TOC links to the actual article anchors when useful on a longer article. Other article bodies were not decorated or rewritten.

Single123 Post Content3307e90b is the sole scoped CSS owner for reading width, headings, links, anchor offset and opening alignment; superseded rules replaced there. Pattern3159 owns native dynamic header layout/typography/chips. No plugin, new field, per-post stylesheet or JS added. Final inset CTA80 unchanged. Archives124/2232 and SingleProject2231 protected settings compare unchanged. BeforeAfter493 Elementor data differs from the initial snapshot; this task made no writes to493, so the concurrent difference was preserved and not reverted.

Header113 primary Nav Menu7983af36 retains its existing sole Custom CSS owner. Removed decorative orange active inset and action outlines per owner steering; actions now have a very pale orange#FFF7ED fill, subtly stronger#FFEDD5 hover/focus, navy text and6px corners. Existing native links, order, main CTA and functional focus outline preserved. Ordinary menu items unchanged. This is not a claim of an exhaustive sitewide border audit. Source mirror is recovery documentation, not separately enqueued.

Verification: native saved settings and guest HTTP/HTML checks on pilot2046 and longer-title2050:200, one H1, noindex, self-canonical, one opening photograph, actual date fields; protected article fields unchanged. Archive124/2232 and SingleProject2231 settings unchanged;493 concurrent data difference preserved. Pilot AIOSEO differences are only updated/scan timestamps, not SEO title/description/canonical values. Saved menu rules checked. Actual Chrome screenshot observed the earlier split opening; final desktop/mobile screenshots, computed overflow, anchor-under-sticky and keyboard acceptance remain incomplete: the user stopped Computer Use with physical Escape after repeated simultaneous-input guards. No further Computer Use calls made. Settings/HTML checks are not browser acceptance.

Private recoverable pre-change snapshots remain outside Git in outputs/article-pilot-2026-10-30. Roll back native3159/123/113 settings and pilot2046 body from those snapshots through the supported editor/REST. No credentials, raw admin responses or private backups committed. Existing30-article SEO decisions and canonical URL inventory remain unchanged. Owner rejected the illustrative wall-staining cover as a weak visual choice; replacement selection remains outstanding and no uninspected replacement was silently substituted.


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
