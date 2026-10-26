# Native WordPress content links — 2026-10-26

Owner requested a staging-wide correction of numeric page references so link controls select WordPress content by its title. Read159 Pages/posts/templates (108 with Elementor data), all29 available shared Components and49 WordPress menu items. No production writes.

## Actual changes

-47 existing documents:212 changed bindings.100 bare `destination` query objects were replaced with **Dynamic Tags → Internal URL → Content**, retaining exactly the same target WordPress object.112 existing selector labels were added/refreshed from actual WordPress titles. This changes the stored selection label, not visible button text or page titles. All other document data, styling, image selections, layout, status and destination object IDs were compared unchanged. Draft SMS Terms1952 remains Draft.
- Shared Service Areas1140: named native content selectors for the twelve city links and directory link; full31 editable properties retained. Its availability action still opens native Popup1801; it was not converted to an ordinary page link. Non-link content and styles match the earlier read.
- Water Hero1453: Request Service origin now selects **Service Request** through Internal URL, rather than an unnamed bare492 query. All15 active content/media override fields retained. Removed only the stale `rating_badge` exposure that pointed to an already deleted paragraph; the actual Trustindex widget/controls remain. A concurrent owner change of its Widget ID from53edca… to68cbfa… was observed and preserved, not reverted. Other content/media/styles compare unchanged.
- All49 menu items already use WordPress `post_type` object references; no Custom Link replacements, navigation label/order or menu styling changes were required.

Numeric IDs remain WordPress's underlying relationship keys, as required by native Elementor. The editable selectors now include the real content title; they are not numeric URL strings, `#post-id-…` placeholders or manually typed slug substitutes. Content titles can be duplicated across service branches, so the underlying original objects remain unchanged.

## Checks and exact exceptions

Fresh read of all159 documents found273 named Internal URL selectors, zero bare destination queries, zero missing internal-link titles and zero rendered numeric hrefs in their content. All29 Component definitions were re-read with zero such unresolved fields.47 changed documents preserve their non-link trees and publication status. Native component metadata confirms31 active properties on1140 and15 on1453.

Anonymous frontend link checks covered all42 changed Published Pages:41 returned200 with no numeric hrefs; Contact496 returned403 in that pass, so anonymous frontend certification for it is unavailable. Its saved native bindings were read back successfully. No security setting was changed or bypassed. Header/Footer/template changes are included in those consuming-page responses; no layout or physical-device audit was needed for these configuration-only changes.

Two exceptions remain in the existing **checkbox consent text** on Request492 and Contact496: the inline Privacy Policy anchors are HTML inside the native label's rich-text prop, which has no separate Internal URL/content-selector field. They retain the verified `/privacy-policy/` destination; the forms, consent wording and layout were not rebuilt to force an unsupported binding. Email and telephone anchors in Privacy/Terms text are normal `mailto:`/`tel:` links and need no page selector. No new custom code, plugin, hidden resolver or duplicate page was added.

[Sanitized counts and frontend results](../evidence/2026-10-26-native-named-links.json). Private source/fresh backups and per-field changes are retained outside Git in workspace work/link-audit-2026-10-26. Restore only affected link values/labels if necessary, preserving current owner edits and the current Trustindex ID. Components were staged and republished with their full existing property maps; never replace an exposure map with a single key.

## Authoring rule

For future Elementor internal links, select **Internal URL → Content** and save both the native `post_id.id` and its actual WordPress title in `post_id.label`. Do not use the bare `{id:…}` destination union even if accepted by the schema. In Component instances, retain the appropriate independently editable override. Use native Post URL for current-item loop links. Keep normal external, email, telephone, popup and genuine anchor actions unchanged. Preserve documented rich-text inline exceptions where no native separate link control exists.

## Homepage Core and shared Footer → Residential services — 2026-10-26

Owner-authorized staging-only activation of the six previously informational Core rows and six Footer service rows. Verified all six actual Published destinations under Residential484 from WordPress titles/hierarchy and anonymous browser-UA HTTP200 responses before binding. No missing or ambiguous target. No production change.

| Core / Footer service | Selected WordPress page (Residential) | Verified destination |
| --- | --- | --- |
| Water Damage / Water Damage Restoration | Water Damage (514) | /residential-services/water-damage/ |
| Fire & Smoke Damage / Fire & Smoke Restoration | Fire & Smoke (517) | /residential-services/fire-smoke/ |
| Mold Remediation | Mold Removal (516) | /residential-services/mold-removal/ |
| Reconstruction | Reconstruction (518) | /residential-services/reconstruction/ |
| Storm Damage / Storm Damage Restoration | Storm Damage (523) | /residential-services/storm-damage/ |
| Personal Property / Contents | Personal Property Restoration (521) | /residential-services/personal-property-restoration/ |

Home154 Core rows54ee8d2d/97cc573/2ebf3e02/24281f6b/2890630/463d381e now have native link fields. They render whole-row anchors with the existing core-b-row presentation. Footer114 service elements1a57ae23/7e3dc0fd/2a175611/15d483d9/147c396c/308c7b8f are native e-button anchors, converted in place from paragraphs so the **existing** gcpro-footer-link style applies to the actual link. IDs/text/local styles and gcpro-footer-item borders/spacing are retained. No new class definition/component/code/dependency. All12 links use Dynamic Tags → Internal URL → Content: native post_id.id plus actual title in post_id.label, never hand-typed URLs or numeric display placeholders.

Owner reiterated Footer styling: existing white text with orange2px underline at5px offset on hover/focus, plus orange focus outline. Reused its existing class/root state rules unchanged; no permanent browser-default paragraph-link underline. Native Footer touch rows remain44px on393px mobile.

Read back all12 named selectors. Public frontend Home200 verifies12 hrefs; /portfolio/200 verifies all6 shared Footer hrefs, with staging noindex retained. Browser Home confirms all12, keyboard Enter on the Water Core card opens the correct Residential page, and Footer hover/focus shows the existing orange underline.393px mobile has all6 Core anchors/all6 Footer anchors,44px Footer rows and no horizontal overflow. No physical-device certification. Commercial Home499 binding and every unrelated Home/Footer node/style match scoped before snapshots; only the new link fields and six intentional Footer paragraph→styled-anchor conversions differ. Other Footer phone/email/Maps/social/legal/city links and Header menus were not changed. Cleared staging SG cache.

[Sanitized binding/HTTP evidence](../evidence/2026-10-26-home-footer-residential-links.json) · [Actual Footer hover/focus](../evidence/2026-10-26-footer-service-links.png). Private before/fresh snapshots remain outside Git in work/service-links. Recovery: remove only the12 new bindings; restore the six original Footer paragraph widgets/classes from scoped snapshots if withdrawing activation. Preserve unrelated current edits. The earlier212-binding site-wide count above is historical, not a fresh whole-site audit.
