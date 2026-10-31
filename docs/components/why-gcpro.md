# Why GCPRO — shared section and certifications

## 2026-10-31 — Requested thinner homepage icons: pending

Owner approved lighter rounded outlines and a consistent sitewide decorative-icon direction; see [design standard](../DESIGN_SYSTEM.md#current-icon-weight-and-sizing--owner-direction-2026-10-31) and [current asset/Override register](../ICONOGRAPHY.md#2026-10-31--lighter-outline-direction-and-homepage-trial).

First change is scoped to Home154/60cdf058's four existing SVG Overrides (current3857/3858/3859/3860), keeping40px boxes and all text/layout/color settings. Shared Component1149 defaults and other page consumers are outside this trial. The lighter appearance must be present in actual SVG contours; CSS stroke-width does not thin expanded filled outline paths.

**Actual state:** documentation updated; website icon replacement blocked and unperformed. Local execution cannot start because sandbox provisioning reports `helper_sandbox_lock_failed / Access is denied`; no SVG-upload/browser capability is exposed. Existing four icons remain assigned. No new media/classes/Variables/Components/CSS/JS/plugins/dependencies or publications; no new desktop/mobile validation. Recovery currently requires no WordPress action because no website change occurred.

**2026-10-23 — owner-selected icon direction:** The owner approved **Flaticon Uicons Regular Rounded** and reported applying **House-building / Shield-check / Diagram-project / Comments**. Comments supersedes Comment-check. This research/documentation session made no component/page/media edits and did not independently re-inventory the new SVG attachment IDs; historical IDs below must not be assumed current. Future changes must follow [ICONOGRAPHY](../ICONOGRAPHY.md) and the [approved style rule](../DESIGN_SYSTEM.md#approved-icon-family--flaticon-uicons-regular-rounded), retaining native per-instance Overrides and verifying real SVG paint before rollout.


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

## 2026-10-24 — Water Damage affiliation trial

Page514 alone now has a native navy affiliation section between Reviews and FAQ. Instance43194cd8 clears only the five trust-image Overrides; shared1149 and other pages are unchanged. Owner review is required before extending the larger section. See [implementation, source verification, screenshots and rollback](affiliations.md).


## 2026-10-31 — Homepage timing removal and verified Why copy (before audit)

Published Home154 only: deleted Hero response paragraph28bf295e rather than leaving an empty widget/gap; Process6d0939b9 description is now “Tell us what happened. We’ll help you understand the next step.” The24/7 mark, four process steps, Hero styles/media, audience overlap, Insurance3796 and current section order remain unchanged; no arrival guarantee substituted.

Home Why1149 instance60cdf058 uses supported content Overrides only. Introduction: “Company history and professional relationships you can verify.” Points: (1) “Locally owned & operated” / “A family business based in Lombard, Illinois.” (2) “Established in 2008” / “Serving Chicagoland homeowners and businesses since 2008.” (3) “BBB Accredited Business” / “GCPRO, LLC is accredited by the Better Business Bureau.” (4) “RIA member” / “Listed in the Restoration Industry Association’s member directory.” Local ownership and history are distinct supported company facts; accreditation and membership are explicitly separate relationships, not certifications or guarantees.

Evidence read2026-10-31: approved staging About497 copy and public company About https://gcprochicago.com/about-us/ identify local family ownership/Lombard and opening2008; BBB https://www.bbb.org/us/il/lombard/profile/fire-water-damage-restoration/gcpro-llc-0654-88372213 confirms accreditation and business-started5/2/2008; official RIA https://pro.restorationindustry.org/find-a-member/gcpro-llc lists GCPRO with matching website/address. Do not add current IICRC certification: existing affiliation record documents certificate valid only through12/31/2024. Current insurance/licensing, individual technician certifications, team headcount, IAQA/RA current renewal and guarantees remain unverified; published company license images alone were not treated as current proof. Existing credentials/affiliations1886 on service pages is preserved, not duplicated.

Consumer check: current1149 shared definition and actual instances Residential484/225936ef, Commercial499/94c4cddb and Water514/43194cd8 read before/after and compare identical. All unrelated Home subtrees compare identical; Home Why remains same shared component with its original design, icons and classes. Actual staging desktop confirms removed phrases/new trust copy/no horizontal overflow; native Elementor Mobile Portrait preview confirms wrapped/stacked Why text and retained process. No physical-device, independent anonymous cache-HIT, form submission or new architecture fix claimed. Pre-edit signed Home snapshot captured for scoped recovery. Restore only deleted paragraph and prior154 instance Overrides if rolling back; do not overwrite shared definitions or unrelated owner work. Architecture audit begins only after this content commit.


## 2026-10-31 — Owner's four homepage benefits and matching SVGs

Supersedes the earlier homepage history/BBB/RIA copy in this record. Published staging Home154 > Why component1149 instance60cdf058 only, using supported content/SVG Overrides. Navy section, existing heading/accent/eyebrow, typography, orange color-accent and responsive layout retained. No component detachment or duplicated shared definition. Separate Affiliations1886 with all five organizations is unchanged; shared1149 and checked Residential484, Commercial499 and Water514 consumers remain unchanged.

Approved copy:
- **From Cleanup to Rebuild** — One team for emergency cleanup, restoration and the repairs that follow.
- **24/7 Emergency Contact** — Reach our team day or night when property damage happens.
- **Local Chicagoland Team** — Based in Lombard, serving Chicago and the surrounding suburbs.
- **Restoring Your Property & Belongings** — Help with damaged spaces and the personal property inside.

Introduction: “Restoration support for your home or business, from the first cleanup through the repairs that follow.” Homepage optional trust-image Overrides are empty; no BBB/RIA or other association references remain in this block. This does not remove or reinterpret the separate affiliation facts.

Individual original SVGs downloaded from the owner's Flaticon account, all Uicons **Regular Rounded** (fi-rr, viewBox24), then uploaded through Elementor's native Upload SVG / Media Library controls and assigned to its four exposed SVG properties. No icon geometry edited, library enqueued or plugin installed:
| Benefit | Source | Media asset |
| --- | --- | --- |
| Cleanup | [Tools11270161](https://www.flaticon.com/free-icon-font/tools_11270161) |3857 tools.svg |
| Emergency | [Timer clock call16310024](https://www.flaticon.com/free-icon-font/timer-clock-call_16310024) |3858 timer-clock-call.svg |
| Local | [Map marker home5074065](https://www.flaticon.com/free-icon-font/map-marker-home_5074065) |3859 map-marker-home.svg |
| Property/belongings | [Warehouse alt9240018](https://www.flaticon.com/free-icon-font/warehouse-alt_9240018) |3860 warehouse-alt.svg |

Warehouse alt depicts a simple building with boxes, matching the property/belongings concept. Existing native SVG controls retain40×40px/orange currentColor. Premium download was available; no separate license certificate is claimed archived.

Decorative item numbers hidden only on Home using two scoped rules in its existing main container46c3aad4 local style: `& .why-benefit-number { display: none; }` and `& .why-benefit { grid-template-columns: minmax(0, 1fr); }`. The shared schema exposes no number-display Override; changing its definition would affect other pages. The second rule removes the now-empty number track, without duplicating base styling. No new global class/stylesheet/JS. An ineffective instance-local trial was removed; this is the sole active local owner. See CUSTOM_CODE.md. Process step numbers remain.

Verification: staging desktop shows four exact benefits with four orange40×40 SVGs and hidden item numbers, without horizontal overflow. Native Elementor Mobile Portrait preview shows stacked items, natural wrapping (including the long fourth heading), all four305px-wide benefit containers with scrollWidth305, all icons40×40 and numbers display:none. No clipping of card text or squeezed icons observed. Shared1149/Affiliations1886 saved trees and unrelated Home sections compare unchanged. Desktop editor restored and homepage reopened; browser transport then disconnected, so no final exported screenshot/physical-device or anonymous-cache certification is claimed. No production change. Architecture audit remains separate and unfinished; no architecture fixes implemented.

Recovery: restore only this Home instance's previous Overrides and remove these two main-container rules. Preserve shared1149/1886, other page consumers and unrelated homepage work. Uploaded icons can remain unused; do not delete shared assets blindly.
