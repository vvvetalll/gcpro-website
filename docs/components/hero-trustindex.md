# Shared Hero Trustindex reviews — 2026-10-26

Published on staging. The owner's later instruction to add reviews to the component supersedes the original Page514-only trial. Existing Shared Hero1318 and Water Hero1453 each contain one **Hero Trustindex Reviews** Atomic element beneath their existing buttons, in the left text column. Native alignment is flex-start with max-width100%; existing column spacing is retained. Text, photographs, masks, CTA destinations and other review sections are preserved.

## Editing and ownership

Edit the shared Hero, select **Hero Trustindex Reviews**, then use **Trustindex Widget ID** and **Display reviews** (Visible/Hidden). Current ID: `53edca7848d34139155693b18cf`. This is shared component content; changing it changes consumers. The widget's default is empty/Hidden, rendering no markup. No per-page badge override was added. The unused earlier empty paragraph was removed from1453; its legacy empty metadata key remains inert.

The owner explicitly approved extending the existing GCPRO Atomic plugin. Version0.4.3 registers `gcpro-trustindex` with native Atomic Text/Select controls. PHP and Twig are stored in `integrations/gcpro-atomic-masked-image/`. The Twig template validates the hexadecimal widget ID and embeds only Trustindex's official loader; no custom JavaScript, CSS or new plugin. Widget IDs are public locators. Existing masked-image implementation is unchanged.

The owner confirmed that the unrelated company is disabled in Trustindex's widget configuration. No Trustindex filters/settings were changed. The badge renders **5.0 Google |244 reviews**. Its actual click opens `https://www.trustindex.io/reviews/gcprochicago.com` in a new tab. That provider profile has its own aggregate/title; do not claim the badge's filtered total is the profile's full aggregate.

## Verification and limits

Installed update through WordPress's existing-plugin replacement; native schema and saved component child confirmed. Desktop Water514 and Commercial499 browser renders display the badge beneath the buttons. At393px Water514 badge bounds were x20–358px, width338px; page width378px, viewport393px, without horizontal overflow. Native Request Service still resolves to existing `/service-request/`, Call to `tel:+18476563322`. Home154 server-rendered content also includes the widget; its complete browser appearance was not checked. Provider styling remains unchanged: the current badge uses dark text, whose contrast on navy still needs owner presentation review. A provider admin-only shortcode advisory was dismissed locally; its message states it is absent for public visitors. Anonymous staging access remains restricted, so no guest-browser claim is made.

Owner visual acceptance remains pending. Screenshots are in workspace `outputs/trustindex-hero-desktop.png` and `outputs/trustindex-hero-mobile.png`.

Rollback: remove the single Trustindex child from each Hero and publish; leave all existing children intact. To disable temporarily, set Display reviews to Hidden. Plugin0.4.1 archive and private pre-change snapshots remain outside Git. No production changes.

## Related task checkpoint

Recent Hero metadata was updated for11 actually used photographs; saved metadata and rendered alt text verified, page document hashes unchanged. Sanitized record: `../audits/2026-10-26-hero-metadata.json`. Captions and image files/crops/focal points preserved; unused recent uploads and SVGs excluded.

Projects catalogue/project galleries and approved Header action styling are separate unfinished work. The native Tabs/Collection Loop example and gallery/lightbox must still be verified before the Projects rollout. No completion of those items is claimed by this badge milestone.
