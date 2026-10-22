# Residential Services SEO content brief and implementation — E79

**Later semantic-planning reference:** This implementation record is preserved. The new [master strategy](SEO_STRATEGY.md) and [page briefs](PAGE_SEO_BRIEFS.md) are **DRAFT — AWAITING USER APPROVAL**. After approval they govern future targeting; this note does not change existing implemented copy or settings.


2026-10-21, staging only. Actual Page484, production source Page8; `/residential-services/` unchanged. [Preview](https://vitaliiv1.sg-host.com/residential-services/) · [WordPress / AIOSEO](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=484&action=edit).

## Intent, evidence and keyword choice

Primary intent: a local residential restoration service-category hub, helping homeowners identify the right specialist service and call GCPRO. This is an inference from the original source content and page role, not a measured keyword-to-page ranking claim. Child pages retain water/fire/mold/storm/reconstruction/contents specificity.

Evidence: existing `GCPRO-SEO-audit-and-migration.xlsx` (SHA256 `b4619b0a733652e845f5ef78702344c8e5beb59a0d905ec2eb615f52d4bb1774`), its URL inventory, keyword map, migration map, GSC and Ahrefs-derived sheets; canonical SEO register; [original production Residential page](https://gcprochicago.com/residential-services/) read only on2026-10-21. Source page already uses “Residential Restoration Services in Chicago” and the six service categories. Existing GSC URL metrics for2025-10-01–2026-09-30:23 clicks,5,785 impressions,CTR0.004,position7.71; source export2026-10-15. Workbook keyword-to-target mapping is proposed allocation, not a full query-page export. Current Ahrefs export records0 keywords/backlinks/referring domains for this URL; this is not proof of no demand. Missing GA4 data remains unknown, not zero. No fresh Search Console/Ahrefs account pull was available or claimed.

Primary keyphrase: **residential restoration services in Chicago**. Related language used naturally: home restoration, residential property restoration, water/fire/mold/storm damage, reconstruction, personal property restoration, Chicago/Chicagoland. No fabricated search volumes, service guarantees, qualifications, insurer arrangements, prices, response times or office hours.

## Configured metadata

- **seo_title:** Residential Restoration Services in Chicago | GCPRO
- **meta_description:** Water, fire, mold or storm damage at home? GCPRO offers residential restoration services in Chicago and Chicagoland. Call 847-656-3322 to discuss your project.
- **primary_keyword:** residential restoration services in Chicago
- **Canonical:** `https://vitaliiv1.sg-host.com/residential-services/` — staging self-canonical; production host switch is a future launch task.
- **Robots:** actual rendered `noindex, nofollow, max-image-preview:large`; WP Reading protection retained.
- **Social:** explicit matching title/description, OG website, featured Media747 (`glenview-house-2.jpg`,1600×1200), Twitter uses OG with `summary_large_image`.
- **Schema:** existing native WebPage/BreadcrumbList/WebSite/Organization plus one native AIOSEO Service graph `#residential-restoration-service`. Provider references the existing Organization. No offers/prices, ratings, hours, custom JSON-LD or duplicate FAQ graph.

Storage: native `aioseo_meta_data` on Page484, managed by installed AIOSEO Pro; `title`, `description`, `focus_keyword`, `canonical_url`, OG/Twitter fields and `schema.graphs`. Native AIOSEO settings API/registered WordPress REST fields were used, not direct database editing. The Elementor MCP exposes Atomic controls/resources but no AIOSEO-specific ability in this installation. WordPress title and excerpt also updated to the approved H1 and description; empty core post_content was not filled with a duplicate content mirror.

AIOSEO Search Appearance snippet UI verifies the saved title/description; its title preview reports479/600 recommended pixels. This is a plugin preview, not an actual indexed Google result or an arbitrary character-count target. Noindex prevents a meaningful live staging SERP test.

## Final visible hierarchy

**H1:** Residential Restoration Services in Chicago

**Hero intro:** Water, fire, mold or storm damage? GCPRO restores homes across Chicago and Chicagoland.

- **H2:** Restoration Services for Your Home
- **H3:** Water Damage Restoration
- **H3:** Fire & Smoke Damage Restoration
- **H3:** Mold Removal & Remediation
- **H3:** Storm Damage Restoration
- **H3:** Home Reconstruction
- **H3:** Personal Property Restoration
- **H2:** From Damage Assessment to a Restored Home
- **H2:** How Home Restoration Works
- **H3:** Discuss Your Needs
- **H3:** Assess the Damage
- **H3:** Restore Your Home
- **H3:** Review the Work
- **H2:** Why Homeowners Choose GCPRO
- **H3:** Services for Your Home
- **H3:** Cleanup Through Reconstruction
- **H3:** Coordinated Project Work
- **H3:** Clear Project Updates
- **H2:** See Real Home Restoration Projects
- **H3:** Fire Damage Restoration â€” Tinley Park, IL
- **H3:** Water Damage Restoration â€” Glenview, IL
- **H2:** Serving Chicago and Surrounding Communities
- **H2:** Residential Restoration Questions
- **H2:** Let's Talk About Restoring Your Home

Numbered eyebrows remain01–07: 01 / RESIDENTIAL SERVICES; 02 / RESTORATION SOLUTIONS; 03 / OUR PROCESS; 04 / WHY GCPRO; 05 / REAL RESULTS; 06 / LOCAL COVERAGE; 07 / HOMEOWNER QUESTIONS. Final CTA remains unnumbered, consistent with the approved shared design. H1 uppercase styling is inherited, unchanged.

## Complete content and exact editable storage

Page484 → `_elementor_data`; existing Component public Overrides only. IDs below are editor location references, never CSS/runtime dependencies. Shared definitions are unchanged.

### Instance `48d8e79c`

**`title`:** Restoration Services for Your Home

**`description`:** Find the right starting point for your property, from damage cleanup and repairs to rebuilding and caring for affected belongings.

### Instance `170443ba`

**`title`:** Water Damage Restoration

**`description`:** Leaks and flooding can affect walls, floors and everything around them. We remove water, dry affected areas and plan the repairs needed to restore your home.

**`cta_text`:** Water damage restoration

### Instance `3ed0e60b`

**`title`:** Fire & Smoke Damage Restoration

**`description`:** From smoke residue and odors to damaged interiors, our fire restoration services cover cleanup and repairs based on the condition of your home.

**`cta_text`:** Fire and smoke restoration

### Instance `dedb673`

**`title`:** Mold Removal & Remediation

**`description`:** Address mold in affected rooms and the moisture conditions behind it. Our team assesses the area and plans removal, cleanup and restoration.

**`cta_text`:** Mold removal and remediation

### Instance `740bef0f`

**`title`:** Storm Damage Restoration

**`description`:** Repair storm-damaged areas and protect your home's structure and finishes. We assess the damage and coordinate cleanup, restoration and reconstruction as needed.

**`cta_text`:** Storm damage restoration

### Instance `44127e7c`

**`title`:** Home Reconstruction

**`description`:** When cleanup alone is not enough, reconstruction brings damaged spaces back together, from structural repairs to flooring, drywall and finishing work.

**`cta_text`:** Home reconstruction services

### Instance `16d63af0`

**`title`:** Personal Property Restoration

**`description`:** Furniture, clothing and other belongings may be restorable after property damage. Ask about cleaning, packing and storage options for the items affected in your home.

**`cta_text`:** Personal property restoration

### Instance `26c8a5b5`

**`title`:** From Damage Assessment to a Restored Home

**`description`:** Damage rarely stops at the surface. Water can reach floors and wall cavities, smoke can affect finishes and belongings, and storms can leave several parts of a home needing attention. GCPRO starts with an assessment, then helps define the cleanup, repairs and reconstruction your property needs. You can discuss the work with one restoration team as the project moves forward.

**`cta_text`:** Discuss Your Home Restoration

### Instance `5412e337`

**`heading`:** How Home Restoration Works

**`description`:** Know what happens next, from your first conversation through the final review.

**`step_1_title`:** Discuss Your Needs

**`step_1_description`:** Tell us what happened and which rooms or belongings were affected by the damage to your home.

**`step_2_title`:** Assess the Damage

**`step_2_description`:** Review the affected areas with our team and discuss the cleanup, repairs or rebuilding needed.

**`step_3_title`:** Restore Your Home

**`step_3_description`:** Our team coordinates the agreed cleanup, repairs and reconstruction work to restore your home.

**`step_4_title`:** Review the Work

**`step_4_description`:** Walk through the completed restoration with our team and review the work, finishing touches and final project details.

### Instance `225936ef`

**`62a085d4`:** Why Homeowners Choose GCPRO

**`31a44bf8`:** Property damage is disruptive. We bring the restoration services, project coordination and communication needed to help you move forward.

**`11debea0`:** Services for Your Home

**`46074ea9`:** Restoration for damaged living spaces, building finishes and the household belongings affected by a loss.

**`74658ef6`:** Cleanup Through Reconstruction

**`2195b550`:** Water, fire, mold and storm damage services, with rebuilding work when your home needs more than cleanup.

**`133bbae9`:** Coordinated Project Work

**`44c64cc8`:** An assessment and agreed scope help connect the different stages of your home restoration project.

**`49c6ac5f`:** Clear Project Updates

**`65cfbe6e`:** Discuss the work, ask questions and stay informed as your property moves through the restoration process.

### Instance `5cd7bb8a`

**`title`:** See Real Home Restoration Projects

**`description`:** Compare actual GCPRO projects in Tinley Park and Glenview. Drag the divider to see each interior before and after restoration.

### Instance `54087252`

**`text`:** View All Restoration Projects

### Instance `5ced3ca1`

**`heading`:** Serving Chicago and Surrounding Communities

**`description`:** Based in Lombard, GCPRO serves Chicago and surrounding Chicagoland communities. Browse local service information below, or contact our team to discuss your property's location.

**`directory_text`:** View All Service Areas

**`availability_text`:** Ask About Your Location

### Instance `44dce85e`

**`title`:** Residential Restoration Questions

**`description`:** Answers to common questions about damage, repairs and working with GCPRO.

### Instance `719bb94f`

**`question_1`:** What do residential restoration services include?

**`answer_1`:** Residential restoration services address damage to a home and its contents after water, fire, mold or a storm. The work may include cleanup, drying, repairs, reconstruction and restoration of belongings, depending on the damage. GCPRO will discuss the services your property needs.

**`question_2`:** Can one project include cleanup and reconstruction?

**`answer_2`:** Yes. Some homes need both damage cleanup and rebuilding. GCPRO can coordinate restoration and reconstruction within the agreed scope, so the plan addresses damaged areas as well as the finishes that need to be replaced.

### Instance `25373f2d`

**`question_1`:** How do I get started with GCPRO?

**`answer_1`:** Call 847-656-3322 to describe what happened, where the property is located and which rooms or belongings are affected. Photos and details about the damage can help guide the initial conversation. Our team will discuss the next steps for an assessment.

**`question_2`:** Can damaged belongings be restored?

**`answer_2`:** Some furniture, clothing and other household items can be cleaned or restored. The options depend on the item, the type of damage and its condition. Ask our team about evaluating affected belongings and available cleaning, packing or storage services.

### Instance `7d01127d`

**`question_1`:** Do you provide residential restoration throughout Chicagoland?

**`answer_1`:** GCPRO serves Chicago and surrounding communities from its Lombard office. The service-area links on this page provide local information. Call our team to discuss your property's address and the restoration work needed.

**`question_2`:** Where can I see examples of your work?

**`answer_2`:** The before-and-after comparisons on this page show actual GCPRO residential projects in Tinley Park and Glenview. You can also visit our project portfolio to explore additional restoration work.

### Instance `728c4896`

**`title`:** Let's Talk About Restoring Your Home

**`description`:** Need help after water, fire, mold or storm damage? Call GCPRO to discuss your home, the damage and the next steps.

### Native text widgets

- `12e30c52` → `title`: Residential Restoration Services in Chicago
- `4292b809` → `paragraph`: Water, fire, mold or storm damage? GCPRO restores homes across Chicago and Chicagoland.
- `567882a1` → `paragraph`: Drag the divider to see this Glenview living room before and after restoration.
- `5489a838` → `title`: Fire Damage Restoration â€” Tinley Park, IL
- `7dafa7eb` → `paragraph`: Damaged framing and finishes transformed into a completed interior in Tinley Park.
- `1a1cca70` → `title`: Water Damage Restoration â€” Glenview, IL
- `a22cb97` → `paragraph`: Ceiling damage repaired and a Glenview living space restored.

Hero call/Request Service destinations and labels preserved. Final CTA call/Request Service labels preserved. The six cards use existing native destinations514/517/516/523/518/521; the process uses existing1152; Why1149; areas1140; FAQ83; Section Heading71/Image+Text77; CTA80; buttons53/103/59/100; Emergency Mark286. No shared default copy, class, token or definition was rewritten.

## Verification and limitations

- Independently saved/read back native content, AIOSEO metadata/focus and schema; rendered browser title/description/canonical/OG/Twitter match.
- Exactly one title, one description, one canonical, one H1;8 H2 and16 H3. Seven meaningful eyebrows retained. Existing six FAQ items work; first toggled with Enter.
- Chrome simulated360/393/430/768/1024/1280/1440: no horizontal overflow, overflowing heading or paragraph/anchor. Actual viewport/client/scroll widths in sanitized evidence. Desktop/mobile screenshots retained locally, not admin screenshots in Git.
- Seven main-content images have meaningful existing alt text, including original comparison images. No global attachment alt changed.
- All21 unique main-content internal destinations resolve to existing Published staging Page objects; actual browser navigation verified representative `/portfolio/`. These destination Pages remain mostly structural placeholders, including Request Service; no form-submission or migrated-project-content claim.
- Existing non-Hero native tree/styles/classes/page settings/link destinations/original comparison widgets remain unchanged; content uses Overrides, with the separately requested Hero change documented below. Final native node count53. Home154/Header113/Footer114 Atomic bodies/settings are byte-identical to pre-task snapshots. Homepage SEO head exception is separately authorized and documented globally.
- Elementor Clear Files & Data succeeded; SG cache purged. Anonymous Residential request still403; authenticated frontend was used. No independent incognito/cache-HIT, physical Android/iOS or Google rich-result-fetch test claimed.
- Native AIOSEO Optimization sidebar displays the saved focus keyword, but cannot analyze empty WordPress post_content in Code Editor; it explicitly recommends Elementor. The actual integrated Elementor toolbar exists but its editor stays LOADING / Can't Edit with blank preview, and its N/A button does not expose a usable panel. No Safe Mode/global editor settings changed. Consequently no fabricated TruSEO score or “100%” claim; final content and technical checks are independent rendered-DOM QA. Headline Analyzer reports54; that is not a keyword/content SEO score. Do not duplicate Atomic content into core content just to inflate plugin analysis.
- Separate Local SEO addon is not active/installed; address/hours LocalBusiness output is NOT claimed. Verified existing footer address remains220 Eisenhower Lane North, Lombard, IL60148. See global settings record.

## Rollback

Restore only Page484 native text/Override values plus title/excerpt/AIOSEO fields from the private pre-E79 snapshot or a scoped WordPress revision. Do not restore shared definitions, links or URLs. Remove just the one Service graph through native AIOSEO Schema if required. Private snapshots are in the task work directory and intentionally excluded from Git. Clear Elementor/SG cache and repeat rendered head/content/noindex QA. Global settings recovery is separate; never import a complete database or disable staging protections.

## Owner-requested Hero and process refinements during E79

The owner additionally requested the existing same-room Before/After in Residential Hero, a shorter intro and symmetrical process copy. These are implemented on Page484 only; Homepage Hero/Global Header/Footer remain unchanged.

- Hero static Image1ebe662e (Media747) becomes an existing-ID native Atomic frame, local style `e-307475c6-d852`, with one native Shortcode widget `c7b53cfa`, `[bafg id="742"]`. Uses original Glenview `glenview-house-1.jpg` / `glenview-house-2.jpg` (after image Media747), not new media or a duplicate BEAF record. Frame100% wide, existing8px global radius token, native overflow:hidden and explicit native four-side0px padding replace the default10px container inset. No Custom CSS/JS. Native Page nodes52→53; one necessary shortcode child, no new library Component/class/Variable. Existing results widgets5c5184f0→723 and9bb91a0b→742 remain exactly unchanged. Plugin files/options/images/shared BEAF styling/fullscreen settings unchanged; existing fullscreen remains available on this reused742 instance. No new Hero-specific fullscreen suppression requested/applied.
- Hero intro4292b809 is now the short two-sentence copy above. Caption567882a1 explains dragging. H1 font/uppercase/layout/CTAs remain unchanged.
- Process1152 instance5412e337: only existing step title/description Overrides changed to short parallel verbs and balanced paragraphs. At1440px all four headings measure31.198px (one line), all four descriptions102.375px (four lines), with no forced heights or additional CSS. Original Homepage instance content is untouched; no shared definition edit.
- Mobile393 touch drag moved the Hero divider176.667→260px while the original lower742 stayed176.667px. Vertical touch over the image scrolled the page. Desktop1440 mouse drag moved Hero409.132→275.667px while the lower742 stayed278px. These are simulated browser gestures, not physical-device tests. All three Page comparison instances render. Final responsive results and current text are in the sanitized evidence.
- Hero rollback: replace only frame1ebe662e with the prior native Image node Media747 and restore the prior caption/intro from the scoped pre-change snapshot. Do not edit/delete slider742, its media or lower instance. Process rollback restores only the eight content Override values, never shared1152.
