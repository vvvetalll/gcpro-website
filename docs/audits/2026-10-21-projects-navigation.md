# E76 — Projects index navigation correction

2026-10-21; staging only. Completes the latest owner steering after the E74/E75 structure and Header changes.

## Exact changes

No native staging Page with slug `portfolio` existed. Staging WordPress had no registered `portfolio` REST content type; the external anonymous `/portfolio/` request returned403, which alone was not treated as proof of a missing Page. Created one approved structural **Page1132 All Projects**, slug`portfolio`, parent0, Published at `/portfolio/`. Marked built with Elementor; empty per-Page tree reuses existing Theme Builder Single Page1008, adding one explicit native include condition (80 total). One dynamic H1/development notice; no fake project cards, imported project records or duplicated layouts. The existing13 production project URL records/content remain unchanged and inventory-only until separate migration.

Existing primary native menu5 / Header113 Nav Menu7983af36: top item241 Projects and child263 All Projects now both use native Page-object references to1132. Item263 was an existing Draft placeholder; converted to a real Page item and Published, not a new project record. Existing child264 Before & After stays bound to493 at `/before-and-after/`, order2. All Projects order1. No other Page slug, parent, menu hierarchy or destination changed. No redirects, permalink-setting changes, plugin or production edits.

Header retains final E75 five-item service-first main row and standard1200px content grid. Partner Programs remains in desktop utility and the one mobile hamburger. Existing native SmartMenus supports Space to expand, Tab among links, Escape to close; no custom keyboard code. New header CSS/JS/classes/Variables/components/dependencies for E76: **none**. Only native menu object references, one Page and one existing template condition.

## Verification

Native Page status/slug/parent/permalink and menu item object IDs read back. Desktop Projects keyboard expansion shows exactly All Projects and Before & After; both correct URLs. Following All Projects opens Page1132 in the connected browser. Responsive and mobile checks are recorded in `../evidence/2026-10-21-staging-navigation/e76-projects-qa.json`. E75 final Header checks cover360,393,430,768,1024,1280,1440,1920 plus1100/1199/1200; no overflow, unchanged200px desktop/tablet and140px mobile logo, main16px. Native Elementor cache cleared. The new template condition initially read back correctly but was not active on the frontend; saved all80 conditions through the native Theme Builder Edit Conditions → Save & Close interface, then confirmed `.elementor-1008`, one H1 and development notice at all eight widths. No custom rendering workaround. Browser viewport/touch emulation, not physical devices.

Staging noindex checked before creating/publishing this placeholder. External anonymous `/portfolio/` returns nginx403, while the connected browser opens the real structural Page; therefore anonymous accessibility of this route is **not certified**. Existing Contact496 has the same external-client limitation. No security setting/bypass was used. No separate incognito browser session available. Full project content/13 record migration remains pending; Blog/Our Team also still await real staging destinations.

## Documentation and rollback

Canonical migration register remains321 rows: updated the existing production `/portfolio/` record `url-146f018b7c43` with staging Page1132 and dated history, retaining original production ID8929, source archive-type expectation and future migration proposals. No duplicate inventory URL created. Current WordPress Pages93:88 Published/5 Draft. Sitemap now links to All Projects and retains all source-only projects.

For an explicitly requested rollback, restore menu241→493 and return263 to its pre-change Draft native configuration; remove only1132's include condition from1008. Preserve `/portfolio/` history and Page; Draft it only with owner rollback authorization, do not delete it. Git revert does not restore WordPress. [Page admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1132&action=edit) · [Menu5](https://vitaliiv1.sg-host.com/wp-admin/nav-menus.php?action=edit&menu=5) · [prior exact Header owners](2026-10-21-staging-structure-and-navigation.md).
