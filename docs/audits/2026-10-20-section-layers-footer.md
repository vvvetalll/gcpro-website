# Section stacking and footer Call Now — E61

2026-10-20, staging https://vitaliiv1.sg-host.com only. Owner identified Core Services, How We Work and disappearing bottom Call Now near the footer. [Browser observations](2026-10-20-section-layers-footer-results.json).

## Findings and exact changes

| Native editing location | Before → after | Reason |
| --- | --- | --- |
|Homepage154 → Core Services B section3fd180bb → local Style, e-3ed21e1f-ddd9|No explicit z-index →0|Bounds child stacking inside this section; no global class or runtime numeric selector.|
|Same section → grid61328a99 → B Introduction6cb38139 → local Style e-67ba0794-7b2b, mobile|z-index9999 →1|Accidental page-level high layer was above global bottom CTA9998. In a temporary browser-only trial, auto caused a service row to paint over intro text; reload removed that trial. Local1 preserves opaque coverage of own rows, inside section0.|
|Homepage154 → How We Work section4681b8f5 → local Style e-1ed92cbb-13f6|No explicit z-index →0|Owner identified this area too. No9999 or sticky positioning was found here; existing numbers have z1. Contain those necessary internal layers without deleting number/ripple behavior. No independent high-z occlusion defect was reproduced in Process.|
|Elementor → Editor → Custom Elements → Code903, JS|All document telephone links → main-content telephone links only|At the bottom, only footer phone was visible and Call Now was hidden. Plain footer contact text should not suppress the emergency panel.|
|Same Code903, JS|Remove introOverlap calculation/suppression|E60 hid the panel to avoid being covered by Core9999. Correcting the source stacking makes that workaround unnecessary; removal prevents its brief disappearance at Core entry.|

Native section wrappers already compute position:relative; z0 establishes local stacking contexts without new wrappers, clipping or overflow rules. Intro native desktop96px/tablet static/mobile0 positioning, padding16px, opaque background and Header's measured clearance are preserved. Existing Header113/Footer114, CTA895/103, timeline582, Code590/847, theme files, design tokens, BEAF and all links are untouched. Number z1 is meaningful component-internal layering, not an accidental9999 dependency.

Fresh154 saved readback:190 nodes before/after, exactly the three style owners above differ, including native local style class references. No other content/settings/structure differs. Code903 remains Published/Entire site/Body End/priority5; native editor reload source equals existing repository CSS/JS wrapper. Only [scroll-navigation.js](../../integrations/scroll-navigation.js) changes in repository runtime sources; CSS is unchanged and neither mirror is separately enqueued.

## Verification

Authenticated Chrome responsive simulation at360/393/430/768/1440, after staging cache purge and frontend reload:

- 360/393/430: Core section z0/intro z1; point hit tests confirm intro remains above its own rows. At Core entry Call Now is visible and hit-testable above intro. It stays visible inside How We Work and at the footer. Document horizontal overflow0.
- Core intro releases by section exit at all widths. Process section exits normally; point(100,100) after exit is not contained in Process. No sticky Process behavior was added. Tablet intro remains static; desktop remains sticky.
- 768/1440: bottom panel stays hidden, section stacking is0, no horizontal overflow.
- 393: near-footer menu opens and suppresses Call Now; close restores it. Core downward scroll hides Header/intro top0, upward scroll shows Header/intro top79. All content remains native and the same190 nodes persist.
- Footer phone remains tel:+18476563322. No actual telephone call was placed. Existing # destinations remain unresolved, unchanged.

The previously approved menu/form/modal/competing **main** action rules remain: a fully usable Final CTA call button can still suppress the bottom panel before reaching the footer. This is distinct from the corrected plain footer-phone case. No cookie/banner integration was introduced.

No physical Android/iOS, screen-reader, formal performance, full sequence-timing or anonymous/cache-HIT certification. Native saved style/control ownership is verified by MCP readback; no new full visual-editor audit is claimed. Native Component582/590/theme effects were not rewritten. Prior anonymous403 remains a delivery limitation. Purge control invocation and authenticated reload do not prove guest cache delivery.

## Complexity and rollback

No new Global Classes/Variables/Components/Custom Code entries/plugins/libraries/listeners/observers or DOM wrappers. Two native section declarations replace unbounded child layering; removal of the obsolete gate reduces custom JS. Numeric editing locators above do not enter runtime logic. BEAF remains untouched.

Scoped private pre-change local styles and903 source were retained outside Git. For only this milestone: remove local z0 from the two section wrappers, restore intro mobile9999 if deliberately reproducing the old state, and restore Code903 wrapper from commit c0b043af31a793fd4769749a90ea4394e330ba12. Publish154/update903, purge staging cache and retest. This restores the documented old defects. To disable all smart behavior instead, set903 Draft; no Git command automatically deploys WordPress. No full-site restore test was performed.
