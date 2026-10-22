# GC PRO — Chat Strategic Context

**Purpose:** Persistent, concise strategic memory for the planning ChatGPT ("Чат") working with the site owner. The implementation agent ("Ворк") continues to maintain technical milestone and implementation records in the existing project documentation.

## Mandatory reading on every new GC PRO conversation

1. Read this file in the latest GitHub revision.
2. Read `AGENTS.md`, `PROJECT_CONTEXT.md`, and `docs/DECISIONS.md`.
3. Read task-relevant files, especially `docs/seo/` when discussing SEO. Consult `docs/SEO_STRUCTURE.md`, `docs/SEO_AIOSEO.md`, `docs/SEO_URL_INVENTORY.csv`, and `docs/SITEMAP.md` as necessary.
4. Check the current repository branch and newest changes; historical documentation is not a live mirror.
5. Identify **approved decisions**, **proposals awaiting review**, **unknowns**, and **immediate next steps**. Never assume a draft is approved.

## Coordination and documentation rules

- GitHub is the persistent source of context across chat sessions. Keep this file focused on strategy, owner decisions, rationale, priorities, and handoffs; avoid duplicating Work implementation logs.
- Following any meaningful owner-approved strategic change, update this file and verify the GitHub commit. Do not claim a write before it succeeds.
- Work performs authorized research and implementation under existing repository rules. Chat helps with research planning, independent review and owner-facing decisions.
- Treat SEO vendor estimates, historical GSC observations, SERP checks, and editorial inferences as distinct evidence types. Do not fabricate missing search volumes.
- Never authorize WordPress/staging modifications merely by updating this document. Respect `AGENTS.md` boundaries and require explicit implementation approval.
- Preserve existing repository structure and files. Coordinate rather than duplicate SEO work.

## Current strategic objective — 2026-10-21

**Priority:** Develop and review one evidence-based master semantic strategy for commercially valuable GC PRO Restoration pages before proceeding with individual service landing pages.

**Research responsibilities (Work):**
- Analyze available Google Search Console, Ahrefs, Google Ads Keyword Planner and real Google SERPs for Chicago and confirmed service areas; document source, date, geography, and missing metrics.
- Cover Homepage, Residential Services hub, Commercial Services hub, and confirmed commercial-value service families and supporting services.
- Map one primary search-intent cluster to one preferred target URL; define secondary and long-tail clusters per page, SEO content briefs, business priorities, internal linking, and measurable opportunities.
- Explicitly examine Residential vs Commercial overlap (e.g. Water Damage) with evidence, without assuming either two separate pages or one merged page is automatically correct.
- Assess secondary services (water extraction, board-up, odor removal, dehumidification, moisture mapping, structural drying, plus others found in inventory) for standalone page, section, mention, or no targeting.
- Compare current Homepage/Residential/Commercial hub content with the proposed map. Avoid keyword-stuffing targets or arbitrary density rules.
- Preserve existing URLs and make recommendations rather than implementing them.
- Save SEO deliverables in the **existing** `docs/seo/` directory, cross-referencing established SEO documents elsewhere in `docs/`.
- Label unapproved proposals **DRAFT — AWAITING USER APPROVAL**, commit research documentation only, and verify remote commit.

**Status:** Research delegated to Work; master semantic map and page ownership **not yet reviewed or approved** by the owner.

**Existing documents checked:** `docs/seo/2026-10-21-residential-services.md` and `docs/seo/2026-10-21-commercial-services.md` contain page-specific briefs/implemented SEO choices; they are not a verified site-wide keyword ownership map. Both note limitations in query-to-URL attribution and/or source coverage. New research should reconcile their conclusions, not silently discard them.

## Decisions / proposals

### Approved process
- Use GitHub for long-lived project context rather than depending on chat history.
- Maintain one central research/semantic planning home under `docs/seo/`.
- Review proposed keyword ownership and page architecture together before implementing any additional service pages.
- Evaluate commercially relevant supporting service categories before deciding whether to include in navigation or grant distinct landing pages.

### Pending decisions
- Final primary and secondary keyword clusters for every commercial target page.
- Which generic restoration queries should target Homepage vs hub vs individual services.
- Residential/Commercial split for overlapping service intent.
- Which supporting services warrant standalone pages or navigation prominence.
- Any resulting content, heading, URL, or navigation changes.


### Approved semantic research principle — 2026-10-21

**Independent market and search-intent research takes precedence over the legacy site's existing SEO targeting.** Treat old page keywords, URLs, legacy city targeting, and historical GSC performance as diagnostic evidence, not as approved or inherently correct assignments.

Work should: (1) research Chicago-area market demand and real Google SERPs using Ahrefs, Google Ads Keyword Planner, and other available sources; (2) group keywords by actual search intent and business value *before* choosing target pages; (3) compare the needs for audience-neutral service pages versus distinct Residential and Commercial pages, without automatically assigning generic terms to Residential; (4) allocate one primary landing page per distinct query-intent cluster; and (5) only then compare proposed page ownership with legacy URLs, previous keyword maps, and GSC findings to diagnose gaps and plan possible migration.

Legacy local/city pages require independent evidence before being adopted into the new architecture. All page ownership, structure, and URL changes remain **DRAFT — AWAITING USER APPROVAL**. No website, URL, redirect, or navigation changes are authorized by this planning decision.

## Design / trust backlog — proposed, not approved for implementation (2026-10-21)

### Credentials, certifications and association logos

Owner supplied visual references featuring accreditation/certification/industry-association marks (including examples resembling IICRC, IAQA, BBB, RIA, and other restoration-sector marks). Investigate a clean, brand-consistent **trust / credentials strip** for the Homepage, but assess whether Homepage, About, Footer, or a combination provides the best hierarchy. Also consider a small BBB A+ accreditation/rating badge in the Footer, potentially linking to a genuine company verification profile.

**Do not assume any reference logo represents an actual current GC PRO credential or affiliation.** Verify official company membership/certification, current standing, legal permissions and approved brand assets before publication. BBB accreditation and A+ rating are distinct claims; confirm both separately. Do not recreate, recolor, distort, or misrepresent protected seals; obtain permitted versions and use accessible alt text.

### Company awards over multiple years

Owner states GC PRO has received awards over several years. Collect a verified inventory (award name, issuing organization, year, recipient/company entity, evidence/source, and usable official logo or image). Propose an elegant **Awards & Recognition** presentation. Assess placement on Homepage or About and whether compact trust snippets elsewhere help conversion without repeating content or overcrowding. Avoid invented award names/years and unverified superlatives.

### UX decision gate

Propose placement, hierarchy, visual treatment, mobile behavior, links, performance/accessibility considerations, and content verification before making any changes. Prefer one cohesive trust section over several competing badge clusters. This is a **future design idea only**: no authorization to edit Homepage, Footer, or other website pages at this time.

## Mandatory form requirement — RingCentral SMS consent (owner-confirmed, 2026-10-21)

**Status: Required functionality to preserve and design for; implementation details subject to RingCentral/legal verification.**

The owner reports that the contact form in the **legacy site footer** contains a distinct SMS opt-in checkbox and accompanying SMS disclosure, and that this was a condition for RingCentral to enable SMS messaging. The owner provided a screenshot showing the name/email/phone/comments form, a separate checkbox, links to Privacy Policy, and disclosure indicating that SMS messages may be received, message/data rates may apply, and users may opt out by replying STOP. This is a known business/compliance requirement, **not an optional stylistic detail**.

**Rules for future website design, audits and implementation:**
- Inventory every site form and lead-capture flow, including footer/contact, emergency/service request, and any popups or third-party embedded forms. For any flow that collects a phone number **and will request consent for SMS communications**, plan an explicit, clearly labeled, **unchecked by default** SMS opt-in (not bundled with privacy acceptance or general submit consent).
- Place approved SMS program disclosure and working links to Privacy Policy and any required Terms near the opt-in. Preserve adequate readability and keyboard/mobile accessibility.
- Record the affirmative consent reliably if submissions will trigger SMS, subject to privacy/security requirements. Do **not** send marketing texts based solely on a phone number or unchecked consent. Separate transactional and marketing purposes when provider requirements or applicable rules warrant it.
- Do not mechanically add a checkbox to unrelated forms that cannot lead to SMS; evaluate each flow, its intended communication channel and RingCentral's exact current approval requirements.
- **Before deploying or rewriting** any SMS-enabled form, verify exact approved language, opt-in/opt-out/help instructions, frequency disclosure, links, carrier/registration requirements and consent logging with the RingCentral account's approved campaign/requirements and, if necessary, legal counsel. The screenshot is historical evidence, not independently verified current legal compliance.
- Do not remove the existing legacy checkbox or replace consent language without an approved equivalent; the redesign must preserve operational eligibility for RingCentral SMS.
- No WordPress, Elementor, footer or form changes are authorized by this note alone.

**Action item:** In the next form/footer UX planning pass, audit all current and proposed forms for SMS consent and document shared reusable form requirements; obtain owner approval before any implementation.

## Mandatory Privacy Policy page — owner requirement (2026-10-21)

**Status: REQUIRED for the redesigned GC PRO website; not yet authorized for implementation.**

- The new website must include a dedicated, publicly accessible **Privacy Policy** page with a stable URL and a clearly visible link in the global Footer.
- Every applicable contact, Request Service, emergency, quote, and other personal-data collection form must have a working, appropriately placed Privacy Policy link. SMS-related forms must additionally comply with the RingCentral SMS opt-in requirements documented above; a Privacy Policy link alone does not establish SMS consent.
- Review and update policy content for the *actual* site data collection, contact forms, analytics/cookies, service providers, retention and rights practices; include SMS/RingCentral disclosures as applicable, and any relevant Terms links required by the messaging program.
- Check existing legacy legal pages/URLs and migration/redirect considerations so the policy remains accessible during launch. Test desktop/mobile links and forms.
- Do not copy generic or competitor legal language blindly or assert legal sufficiency without appropriate review. Request owner/legal approval of final policy text and provider-specific SMS wording.
- During page and footer implementation planning, include the policy in navigation/footer UX and the release checklist. No WordPress changes authorized by this documentation entry alone.

## Next steps

1. Confirm Work's new SEO research files and assess their provenance, completeness, and cross-page intent overlap.
2. Review page-to-keyword mapping and supporting-service page recommendations with owner.
3. Record explicit approval/amendments here and in canonical SEO files.
4. Only then issue page-specific implementation tasks following approved briefs.

## Notes for future Chat sessions

This file is an index and decision record, **not** an instruction to ignore new user requests or independently act on GitHub without task authorization. Review live GitHub state on each new session; if an entry is outdated, correct it with a dated update after verification.
