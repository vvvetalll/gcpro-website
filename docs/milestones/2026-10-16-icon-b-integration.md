# E23 — Approved B icons on staging Homepage154

2026-10-16. Owner selected **B / Restoration Accent** after E22. Applied only to six Core Restoration Services instances in Homepage154 section38ed6da4. Production/shared ROBYLO, Header/Footer, component definitions and global styles untouched.

## Implementation Summary

Imported the approved six SVGs through the existing native Atomic SVG media uploader, then assigned their attachment IDs through each Service Card62 instance's supported `icon` Override. Navy structure/orange details and selected solid fills render correctly. No detachment or component duplication. A remains an unused source alternative.

| Service | Homepage instance | Previous asset | New Media ID | Approved source |
| --- | --- | --- | --- | --- |
| Water Damage |28d9f7c|192|596|[SVG](../../assets/icons/core-services/b-accent/water-damage.svg)|
| Fire & Smoke Damage |7ce1a666|193|597|[SVG](../../assets/icons/core-services/b-accent/fire-smoke-damage.svg)|
| Mold Remediation |4ac87e43|206|598|[SVG](../../assets/icons/core-services/b-accent/mold-remediation.svg)|
| Reconstruction |95336d4|207|599|[SVG](../../assets/icons/core-services/b-accent/reconstruction.svg)|
| Storm Damage |318ea723|208|600|[SVG](../../assets/icons/core-services/b-accent/storm-damage.svg)|
| Personal Property Restoration |22d372d7|209|601|[SVG](../../assets/icons/core-services/b-accent/personal-property-restoration.svg)|

## Technical Changes

Six new reusable **Media attachments596–601**, one per approved service artwork; previous generic icons did not contain the approved B geometry/colors. Edit/select via Elementor instance → SVG Icon → Select SVG / Upload SVG. Media metadata remains native; files are in staging uploads2026/10. Source artwork remains readable in this repository. Native uploader stores static SVGs with both brand colors retained; returned files parsed successfully as only svg/g/path with the expected48×48 viewBox. Existing `service-card__icon` g-b759e84 and `icon-svg` g-b84ed52 supply unchanged56px badge/32px artwork geometry. Component62 retains all five Override keys.

**Import finding:** ordinary WordPress Media → Add Media File rejected water-damage.svg with “Sorry, you are not allowed to upload this file type.” In the actual Homepage editor, selecting the existing instance then **SVG Icon → Upload SVG → native Media modal → Select Files** successfully imported596. The other five succeeded through that same modal. No global/unrestricted-upload setting, capability, PHP, theme file or plugin was changed; no generic Media retry or custom importer was needed. Distinguish these two entry points before declaring native SVG import unavailable.

Page edits used native supported Overrides; existing published staging page154 was saved/promoted after each verification stage. No new classes, components or custom code. No new Variables/plugins/dependencies. No changes to the existing Orange Outline CTA or card styles. Fixed SVG source color groups are preserved; no separate native per-color picker was introduced/promised.

## Complexity Audit

Only six media files and six instance attachment references added/changed. Shared Component62 definition is byte-for-byte unchanged. Full saved Homepage154 tree matches baseline after substituting exactly the six new icon IDs; all other content, link Overrides, styles, responsive rules and structures match. No additional nodes, classes, wrappers, CSS selectors, new icon system, theme modifications or shared repository changes. Existing old assets retained for other consumers/rollback.

## Verification

- Independence: first changed only Water192→596 and published/read back; the other five remained193/206/207/208/209. Then assigned the remaining five approved icons. [Saved audit](../evidence/2026-10-16-icon-b/saved-audit.json).
- Logged-out normal Chrome at1440/1200/900/390: six48×48 SVGs, each containing actual navy and orange computed strokes; orange fills retained where designed.56×56 badges and44px CTA heights,3/3/2/1 columns, no horizontal overflow, no clipped icons. All six existing # CTA destinations remain unchanged. [Frontend QA](../evidence/2026-10-16-icon-b/frontend.json).
- Authenticated frontend independently confirms both colors on all six. [QA](../evidence/2026-10-16-icon-b/authenticated.json). Reloaded actual Elementor editor, selected Water instance: SVG preview, Select SVG/Upload SVG and existing content/link controls remain exposed; component attached, Publish disabled. No temporary style edits or component restructuring.
- Native Purge SG Cache after final save. Actual anonymous browser shows current icons; subsequent plain HTTP200/HIT contains exactly six new48×48 SVGs and accent stroke. [HTTP](../evidence/2026-10-16-icon-b/http.json), [media mapping](../evidence/2026-10-16-icon-b/media.json), [desktop screenshot](../evidence/2026-10-16-icon-b/1440.jpg), [mobile screenshot](../evidence/2026-10-16-icon-b/390.jpg).
- Tests used browser viewport emulation and a genuine logged-out normal Chrome profile. Controlled incognito/physical-phone checks not performed. No screen-reader or performance benchmark; no new controls/interaction added. Decorative media alt text left empty; existing native SVG semantics preserved.

## Outstanding Items and Recovery

Visual review of deployed B remains pending. Six service # destinations and E21 CTA brand contrast limitation remain unchanged. Incognito/physical-device checks remain pending; this does not establish all-device compatibility or independent native duotone color pickers.

Restore the six previous IDs in the table through the same native instance Overrides to undo. Scoped local pre-change section/component/full-Homepage snapshots are in outputs/recovery/icon-b-before.json and icon-b-full-home-before.json outside Git; not a tested full-site backup. Leave old/new assets intact unless removal is separately authorized and usages reviewed. Git docs do not deploy/restore Elementor configuration.
