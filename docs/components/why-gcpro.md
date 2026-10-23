# Why GCPRO — shared section and certifications

## Benefit icon editing — 2026-10-23 UTC

Component **1149, GCPRO / Why Choose Section**, remains the single shared owner. Its four benefit icons are native Atomic **e-svg** elements, rendered as inline SVG from WordPress media attachments; they are not text glyphs or Atomic Images. Current consumers include Home154/60cdf058, Residential484/225936ef, Commercial499/94c4cddb and Water514/43194cd8.

**Confirmed cause:** the existing Global Class **why-benefit / g-9bf65cb** contained `& svg { fill: none; }`. The uploaded property1397 and office1399 assets have filled paths without strokes. The inherited rule removed their only paint: rendered paths computed both fill:none and stroke:none. The existing shield/checklist/message assets use strokes and therefore remained visible. The files themselves contained valid vector geometry. Typography → Text Color intentionally supplies the native SVG's currentColor; it is not the asset selector.

Removed that existing descendant rule by retaining the class's native desktop grid, padding24px, gap16px,56px number track and align-items:start. Existing mobile variant and every component-local style remain intact. No new CSS, JS, PHP, asset, Variable, class, plugin or component definition. The unrelated icon-svg class and service icons were not changed.

### Native per-page selection

All four SVG fields are now exposed through supported native Component properties:

| Benefit | Existing element | Native Override key | Preserved default attachment |
|---|---|---|---|
|1|14eba757|prop-1792719457799-sbydh70|1397 property (1)|
|2|3acb5a30|prop-1792719460379-4twr4eg|206 shield|
|3|676c0b1c|prop-1792719463290-7ztj8s7|210 checklist|
|4|1e34cbcf|prop-1792719466312-9j3p4yk|211 message|

Open the desired page in Elementor → Structure → **Shared Why Choose GCPRO** → **Content → Benefit 1–4 icon → Upload → Media Library**. Select an existing SVG and click **Select**, then **Publish**. Upload opens the native Media dialog and can also import a reviewed SVG. **Select SVG** also opens the native selection dialog. Use the page instance for an independent replacement; use **Edit GCPRO / Why Choose Section** only when deliberately changing defaults for all inheriting instances. Never detach. No source editing is needed.

Native e-svg is an SVG control, not a general PNG/JPEG picker. This installation normalizes SVG root fill to currentColor: after removing the old blanket fill:none rule, the existing stroke-based defaults display as filled silhouettes. Their original source files are untouched. This change fixes invisible filled uploads but does **not** establish exact preservation of every third-party SVG's authored outline/multicolor treatment. An Atomic Image with an appropriately colored source is the supported alternative if exact authored paint is required; it was not substituted or claimed tested here. No additional CSS exception was introduced to conceal this limitation.

### Verification and preservation

- Replaced Home benefit1 through the visual Media Library with existing office1399, published, reloaded the editor and frontend: selection persisted, viewBox0 0 24 24,40×40px, painted orange rgb(240,90,41). Restored property1397 through the same visual controls; Home retains an explicit identical-to-default icon Override.
- Shared default remained1397, and Residential/Commercial/Water page bodies compare unchanged. Home changed only existing Why instance60cdf058 settings. Its unrelated sections were preserved.
- Component readback: same45 IDs and every style; only the four SVG fields changed to native overridable properties, with the same original attachment defaults. The pre-existing17 content/media properties remain.
- Rendered Home, Residential, Commercial and Water at1440,768 and393 CSSpx: four40×40 SVG icons with orange paint; benefits remain two columns desktop/tablet and single column mobile; no horizontal document overflow. Desktop Home and mobile Water visually checked. Browser viewport overrides reset. No physical-device or screen-reader certification.
- Native Elementor and staging SiteGround caches refreshed. Anonymous ordinary Home HTTP GET returned200. Responsive browser checks used the authenticated connected Chrome session; a separate incognito rendering test was unavailable and is not claimed.
- Direct component permalink editing loaded an incorrect preview; editing the existing shared component in context through Home worked. One MCP component-property update failed validation (`paragraph: invalid_value`); properties were added and saved through native Elementor instead, with focused readback confirming no unrelated component changes.

For recovery, use the private pre-change component/class snapshots, restoring only the affected SVG property definitions and the prior class variant with owner authorization. Reverting documentation does not revert staging. Restoring the old blanket fill:none rule also restores its incompatibility with filled SVG uploads.

## Current layout — 2026-10-22

Owner-approved refinement supersedes the earlier left-column logo placement, centered label and separator. After initially requesting borderless logos, the owner explicitly clarified that thin frames and hover must be added; the final design retains those in the full-width row. Existing Atomic Component **1149** is the single owner. Consumers remain Homepage154/60cdf058, Residential484/225936ef and Commercial499/94c4cddb. No page body, content Override, link, other section or production configuration was changed.

The main composition retains the left introduction and right 2×2 benefits grid. Existing copy, heading levels, typography, colors, icons and internal dividers are preserved. On tablet the introduction stacks above the two-column benefits; mobile benefits stack in one column with the existing horizontal dividers.

Existing group42ba4b31 moved from introduction6f83def0 to editorial container2b11da70, after benefits175b958f, spanning both grid columns. It forms a full-width, transparent continuation of the same navy section. Label48db000c remains a paragraph reading INDUSTRY CERTIFICATIONS & AFFILIATIONS, now left aligned, without flanking lines or a top separator. Its original11px typography/tokens remain.

## Native owners and media

- Existing local styles: editorial container2b11da70 retains desktop columns/gap and uses a single-column grid on tablet/mobile; introduction6f83def0 keeps normal flex flow instead of mobile display:contents; benefits175b958f no longer needs mobile ordering/margin to place logos; label48db000c owns alignment.
- Existing **trust-logos g-c8bf649**: full-width flex-wrap layout, centered evenly distributed logo frames,32px gaps/32px top margin desktop,24px gaps/margin mobile; group grid-column1/-1. Existing empty-media hiding condition retained. No border, card surface or side lines.
- Existing **trust-logo g-da9c4af**: transparent frames with1px white12% border,8px radius and8px padding,104px desktop/80px mobile, equal flexible desktop allocation; mobile wraps centered3+2. Native opacity68%→100% and translateY(-2px) on hover,180ms transition. Existing box-sizing/reduced-motion exceptions retained. Reduced motion disables movement/transition.
- Existing **trust-logo__image g-a5e0eea**: contain original proportions within140×86px maximum desktop and112×64px mobile. No redrawing, filter or new asset.

All45 original node IDs and content settings were preserved. No new Global Class, Variable, Atomic Component, Custom Code entry, JavaScript, PHP, theme stylesheet, plugin, dependency or media upload. The same five native media Overrides remain: trust_iicrc1294, trust_iaqa1295, trust_bbb1296, trust_ria1297, trust_ra1303. Optional Image11b161f2 remains available and empty on the three consumers.

Image mode: populate Image and clear the five logos. Trust mode: clear Image and populate the five logos. None: clear all six. This is the established native field convention, not a newly added dropdown. Image/None switching was not retested end to end in this refinement.

## Verification

Connected Chrome Commercial499 checks at exact1440/768/393/360 CSSpx: five images loaded, certifications below benefits, no horizontal document overflow, zero group border, transparent outlined frames. Initial borderless checks were superseded by the owner's explicit frame/hover correction; final frame/hover verification is recorded below. Logos form one row at1440/768 and two centered rows at393/360. Benefits retain two columns at1440/768 and one mobile column. Home154 and Residential484 checked at1440/360: five logos below main composition, no horizontal overflow. Final left-alignment checked after the owner's clarification. Staging SiteGround cache purged through its native toolbar.

Fresh MCP readback confirmed the same45 component node IDs and identical content settings. Page154/484/499 bodies compare exactly with their pre-task snapshots. No form submissions, phone calls, physical-device or screen-reader certification. No full visual-editor interaction or full-site restore test claimed. Public raw requests previously returned403 on service hubs; connected authenticated browser QA is not independent anonymous certification.

## Recovery and prior evidence

Restore the pre-refinement Component1149 snapshot plus the prior variants of the three existing trust classes together; explicitly publish1149, refresh Elementor assets as needed and purge staging cache. Restoring only one side can leave the old card layout with the new placement. Keep existing page media Overrides and unrelated current work. The prior class/component implementation and original asset evidence remain in [trust source](../evidence/2026-10-22-why-trust-source.json), [trust QA](../evidence/2026-10-22-why-trust.json) and [superseded separator](../evidence/2026-10-22-trust-separator.json). Private pre-task saved component backup retained outside Git.

Original assets1294–1297 are supplied static SVGs;1303 is the existing temporary transparent RA PNG. Unused failed trial1298 remains unplaced. Owner-supplied logos do not independently verify current accreditation; replacing the RA raster with a supplied true vector remains separate work.

Final owner clarification verified: certifications label computed text-align:left; all frames1px rgba(255,255,255,0.12),8px radius. Real pointer hover verified opacity0.68→1 and matrix translationY -2px with0.18s opacity/transform transitions. No marquee or automatic animation. Final1440/768/393/360 checks retain loaded images, no horizontal overflow and certifications below benefits. Small row-coordinate differences during hover reflect the intended2px movement, not another layout row.
