# AI_CONTEXT — rules for any AI assistant working on this kit

Read this before changing anything. These are the owner's decisions; follow them unless the owner says otherwise.

## Project
- Company: **GCPRO Restoration** (water / fire / mold / storm damage restoration, Chicago area).
- Contact on all materials: **(847) 656-3322**, **gcprochicago.com**, label "24-HOUR EMERGENCY SERVICE". Google rating shown as 5.0 with label "Google Rating".
- Source: a purchased marketing kit (Adobe InDesign → flat PDFs, generic template shared across companies). It was rebuilt from scratch in HTML/CSS in the GCPRO style.
- Two programs:
  - **ASP — Agency Support Program**: for insurance agents (15 pieces: 3 trifolds, 2 flyers, 6 special reports, 4 forms).
  - **PSP — Plumber Support Program**: for independent plumbing companies who refer restoration jobs to GCPRO (1 trifold so far).
- Owner: Vitalii (IT at GCPRO). He handles design/structure; the texts are not his responsibility.

## Hard rules
1. **Texts are fixed.** Never rewrite, shorten or "improve" copy. All text comes verbatim from the originals (`content.json`). After any change, verify word-for-word against the original PDFs (see `content.py`). Only design/structure changes are allowed.
2. **No vendor signatures/codes** from the original (e.g. "ASP LEAVE BEHIND TRIFOLD FS 07/20", copyright lines, "Replace with…" placeholders). Owner's decision.
3. **Brand colors, exact:** navy `#1a327d`, orange `#f05a29`. No other brand colors. Orange = accents only (a few highlighted words, list markers, short rules, the "/" in 24/7).
4. **Typography:** headings Montserrat bold/extra-bold, UPPERCASE (like the GCPRO website). Body text Inter. Both are free (OFL) and are also planned for the new website.
5. **One system.** Shared blocks must look identical across all pieces (headers, navy bands, footers, contact blocks, back panels, numbered lists). Change a shared block once, apply everywhere. Don't give one piece a new style unless asked — and when the owner asks for a change on one piece, don't silently roll it out to others.
6. **Even layout.** Pages filled evenly — no content bunched at the top with big empty areas; no huge gaps between fields/signatures; fields never overlap text.
7. **Forms come in two versions:** print (fill by hand) and FILLABLE (form fields). Generated automatically by `build.py` from `.fl i`, `.cb b`, `.sig i`, `.sr-row i`, `[data-field]` elements.
8. **No CSS gradients / CSS transparency for backgrounds** — they rendered pink in the owner's PDF viewer. Bake fades/tints into images (PNG/JPG) instead.
9. **Print:** trifold 11x8.5" + 0.125" bleed (panels 3.625 / 3.6875 / 3.6875"); Letter 8.5x11" + 0.125" bleed. Keep text ≥0.45" from trim on letter pages; keep faces/heads clearly inside trim (aim ≥0.15"). Backgrounds that touch an edge must run into the bleed (no thin strip left before the trim).

## Visual system (current)
- Letter pages: white header (logo + 24h phone), navy title band, content, navy footer with phone + QR. Footer has a light Chicago skyline line-art on the right, fading in from the left, running under the QR and into the bleed.
- Trifolds: back panel = logo, big **24/7 in navy with an orange "/"**, contact, services, QR, pale Chicago skyline line-art at the bottom (different crop per trifold). Front cover = photo + navy block with city-photo duotone texture. Inside right panel = navy with city duotone texture + numbered features + contact.
- City duotone background: grayscale skyline photo toned to navy so the **average color stays exactly #1a327d** (`assets/bg-city-wide.jpg`). Only on large navy blocks (cover block, full-height navy panel) — NOT on narrow bands/footers.
- Invoice: pastel inner headers (light blue with navy text), "PAID" as a large faint watermark behind the table.

## Photos
- AI-generated **people/scenes are OK**. AI-generated **equipment, water damage, stains** look fake — avoid; use real photos for equipment/work. Less detail = more realistic.
- GCPRO staff: navy polo/cap with GCPRO logo. PSP partner plumber: plain gray work shirt, no logo. Homeowners: casual clothes.
- Typical American (Chicago suburban) homes, not British-style kitchens.
- Don't let AI draw text/business cards/logos from scratch; supply a reference or composite the real asset afterward.
- Photos are placed with `object-fit: cover`; adjust `focus` in `photos.json`. See `PHOTOS.md` for the slot list and prompt templates.

## Workflow the owner expects
- Answer/report in Ukrainian; English copy for materials/emails in natural American English.
- Show a preview (`_preview.pdf`) for each change; update the final package only after approval.
- When asked for an opinion — be direct and critical, separate facts from guesses.
- Keep the final package organized: `1 Trifolds / 2 Flyers / 3 Special Reports (+Fillable) / 4 Forms (+Fillable) / 5 PSP`, full descriptive file names.

## Open items (as of 2026-09-30)
- PSP cover: same plumber as flap/inside (confident business-owner portrait) — done.
- PSP flap handshake photo: cap is close to the top trim — extend the image upward.
- Possible future: more PSP pieces; website redesign (Elementor Atomic + Claude) using the same fonts/colors; web pages for ASP/ERP programs.
