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

## Next steps

1. Confirm Work's new SEO research files and assess their provenance, completeness, and cross-page intent overlap.
2. Review page-to-keyword mapping and supporting-service page recommendations with owner.
3. Record explicit approval/amendments here and in canonical SEO files.
4. Only then issue page-specific implementation tasks following approved briefs.

## Notes for future Chat sessions

This file is an index and decision record, **not** an instruction to ignore new user requests or independently act on GitHub without task authorization. Review live GitHub state on each new session; if an entry is outdated, correct it with a dated update after verification.
