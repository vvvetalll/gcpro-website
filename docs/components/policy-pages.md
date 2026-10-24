# Policy pages and scoped enquiry corrections — 2026-10-24

Staging only. This record supersedes earlier contact-card presentation and visible staging notices. The owner’s final refinement affects only Contact496’s left column; no broader redesign was resumed. Final visual acceptance remains with the owner.

## Published destinations and factual basis

| Page | State and purpose | Source |
| --- | --- | --- |
| [Privacy Policy](https://vitaliiv1.sg-host.com/privacy-policy/) ·3 | Reused existing draft, completed and Published | Current GCPRO privacy commitments plus verified native form fields/storage and Google Maps/Trustindex embeds |
| [Website Terms of Use](https://vitaliiv1.sg-host.com/copyright/) ·494 | Reused Copyright page and URL, completed and Published; WordPress title preserved | Existing GCPRO copyright and content-use permissions; no service/payment/insurance terms added |
| SMS Terms & Conditions ·1952 | New **Draft**, slug `sms-terms`; not publicly linked | Working outline awaiting RingCentral campaign facts |

Sources read: [GCPRO privacy](https://gcprochicago.com/privacy-policy/), [GCPRO copyright](https://gcprochicago.com/copyright/), [RingCentral SMS registration requirements](https://support.ringcentral.com/sms-registration.html). Legacy irrelevant ecommerce/payment boilerplate was omitted. No fixed retention period, security guarantee, response time, insurance promise or legal approval was invented. No separate Cookie Policy was justified by the inspected configuration; this was not an exhaustive tracking audit.

**SMS publication remains blocked:** registered message types/use cases, actual sending number, frequency disclosure, HELP response/support routing, and consent/opt-out record workflow are unverified. Confirm these before completing1952. Any necessary consent wording revision requires owner approval before application. Until then no SMS Terms link points visitors to an unfinished draft. Draft editor: https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1952&action=edit.

## Native implementation and exact owners

Policy bodies use native Atomic containers, existing1318 first, existing71 in `section-heading--accent`, h3 subsections and16px body text; max-width760px, gap32px, existing spacing/color/typography tokens. Theme Header113/Footer114 remain in documented order. No shared visual definition, global style, plugin, asset or custom code was added. The new policies inherit existing Hero geometry and images.

Footer114 adds only native legal navigation6a188526 under119ffe98: Privacy41193072 → Page3 and Terms4f10c537 → Page494. Destinations are native object references; existing `gcpro-footer-link` styling retained. All original Footer nodes compare equal after excluding that new navigation.

Request492 SMS label1407c4c4 and Contact496 label33f0c08 now contain the inline **Our Privacy Policy** anchor. Standalone duplicates2b0747de/476f6d14 removed. Native escaped-HTML label supports inline markup but not a nested dynamic page selector: the absolute staging Privacy URL is an explicit manual-link exception; replace/retest it during migration. Plain consent wording is unchanged; links open separately and checkboxes remain optional/unchecked.

Visible staging/email notices were removed, including Request “After you submit.” Native success messages now state only that the request/message was saved. Both forms still use **Collect submissions only**. Email delivery is **unconfigured/unverified**, and no RingCentral sending integration was established. No callback or notification promise is made. No forms or test messages were submitted in this task.

Request left Call Now now uses existing Outline59 (instance1c9911a1), same `tel:+18476563322`. Native submit1b484549 uses existing primary orange class `button-primary`/g-92745fa; no shared56 change. Both SMS checkboxes use native local size/border/checked/focus variants, retaining their field IDs, optional status, default and values. Page-owned middle headings use existing graphite `color-text` (#334155); actual71 accent/subtitle and semantic levels remain.

Contact’s existing white right form panel664644b and form22adac6 remain. Existing map369bda8 moved intact into wide panel3dcbb7a2 below the columns, with address and existing Outline59 Directions34df5dbe on the left; mobile stacks the map full width. The MCP move reported `elementor_v3_not_supported`; the exact existing map subtree was relocated through registered native Elementor page metadata and verified unchanged. No replacement iframe/code was introduced.

**Final Contact left column:**60ce4cbd has32px (`space-lg`) gaps. Groups31225472/31317dd8/78582bb4 now have transparent backgrounds,0 padding/border/radius and no shadow;24px icon track +16px (`space-sm`) gap. Existing icon wrappers5e18baf5/4f611165/59e4b9d7 are transparent24×32, with existing24px orange outline SVGs. Titles: “Call Our Team”, “Email us”, “Visit our office”, graphite. Phone/email retain established clickable link color. Office708f4187 retains full verified address; link324d21ab “View map ↓” targets native ID `gcpro-office-map`, using the existing sticky-header scroll controller. No new scrolling code. This replaces the earlier white contact cards/light-blue icon tiles.

## Actual checks and limitations

- Saved-state comparison:492/496 Hero trees, URLs, page settings and authored SEO preserved; form field IDs/order, validation/options/defaults/actions and plain SMS text preserved. Header113 unchanged; Footer only the approved legal navigation addition. Map exact subtree preserved. Final column comparison confirms all nodes outside its eight authorized targets unchanged, including form, heading component and map panel.
- Latest Contact column inspected at **1440×1000 and393×852**, Chrome viewport emulation: three transparent groups, graphite headings, aligned orange icons, visible links/full address, no card padding/border/shadow, no clipping or horizontal overflow. Mobile View map reached the target. [Desktop evidence](../evidence/2026-10-24-policies/contact-desktop.jpg) · [Mobile evidence](../evidence/2026-10-24-policies/contact-mobile.jpg).
- Earlier in this task, the Contact form/map composition was inspected at the same desktop/mobile widths. Consent text was not clipped. Contact inline Privacy link received keyboard focus and opened the correct page without changing the unchecked checkbox; Space checked/unchecked the native control and showed focus. No submit action used.
- Website Terms inspected on desktop/mobile and Privacy on mobile: readable16px copy, heading hierarchy, no overflow. Footer rendered both correct staging destinations. Final Privacy desktop visual check, draft1952 visual check, Request’s latest button/heading/link interaction checks and footer keyboard activation were **not completed**; later instructions limited further verification to the Contact column. No tablet or physical-device claim for this task.
- Anonymous HTTP check: Privacy200; Terms, Request and Contact403. Authenticated rendering succeeded. Guest delivery is unresolved; authenticated screenshots do not establish availability for every visitor.
- Stale Elementor HTML/styles initially showed old Contact cards. Existing SiteGround purge and Elementor Clear Files & Data were used; final authenticated render showed saved changes. No cache setting was changed.

## Safe maintenance and delivery

Edit named page-local native controls and existing component Overrides. Do not edit shared1318/71/56, detach components, or restore an entire old page tree over newer work. Scoped pre-change snapshots and raw responses are retained privately outside Git. Reverting repository documentation alone does not revert staging.

AGENTS now consolidates actual component reuse,71 accent/subtitle, verified assumptions, proportional single-pass checks, reuse of unchanged checks, no website retest for documentation, finish/commit/stop and immediate stop of all tool activity on an explicit stop request. Remote commit verification is reported in the completion message. No legal approval or guaranteed compliance is claimed.
