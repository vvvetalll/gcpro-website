# Why GCPRO — shared section and certifications

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
