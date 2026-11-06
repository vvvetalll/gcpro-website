# ERP Property Management Flyer — final proofreading, 2026-11-06

Output: **GCPRO-ERP-Property-Management-FINAL.pdf** and its PNG preview. This is the requested final file candidate; promotion into the approved marketing release still awaits owner approval.

Exactly four corrections were applied to the existing review PDF:

1. Help simplifying after-hours emergencies. → Help simplify after-hours emergencies.
2. Help controlling unexpected costs. → Help control unexpected costs.
3. Support for resident retention and protection of NOI. → Support resident retention and help protect NOI.
4. WE ARE THERE FOR YOU AFTER → WE ARE THERE FOR YOU AFTER A LOSS.

The fourth change retains the first header line and extends only its second line to YOU AFTER A LOSS. All corrected text keeps its original typeface, point size, color, baseline and existing line spacing. Bullets and other list positions remain unchanged. At 144 dpi, artwork outside the four correction rectangles is pixel-identical to the prior PDF. The colleague's full paragraph is unchanged. No other obvious grammar error requiring correction was found; no stylistic rewrite was performed.

The required concepts remain present: FREE ERP, Property Management, property-specific response plan, customized emergency application, 24/7 mitigation, full restoration, business continuity, resident retention and NOI. All fonts are embedded, copy fits, no missing glyphs or unintended form fields were introduced.

Print geometry: unchanged media/crop size 8.75 × 11.25 inches; TrimBox explicitly marks the existing 8.5 × 11 inch trim, with 0.125 inch bleed on each side. This is a metadata clarification, not a visible layout change. Existing color treatment is retained; no PDF/X or printer-specific CMYK certification is claimed.

QR verification: decoded both original and final rendered QR images with ZXing. Both encode **https://gcprochicago.com/**; the QR artwork is pixel-identical. Read-only public opening on 2026-11-06 confirmed the GCPRO homepage with restoration services and contact information. It is a homepage destination, not a dedicated ERP landing page. The URL was not changed.

Editable sources: `corrections.json` defines only the requested replacements; `copy.json` preserves the complete copy with those corrections; `build.py` applies the patches to the preceding review PDF. Install requirements and run `python build.py` from a full repository checkout. No Downloads path is required. `checks.json` records exact-copy, design, geometry, font and QR checks.

Saved on a separate review branch. The October 20 base release, CURRENT_RELEASE.json, original ERP review and all PM Trifold files remain untouched.
