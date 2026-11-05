# ERP Property Management — review, 2026-11-05

Source: the released **ASP Agency ERP Flyer**, confirmed by the owner as “Agency EPR Flyer.” This is a text-only adaptation of that exact one-page PDF. Existing logo, ERP shield, header/title, three Before/During/After cards, colors, phone, QR, footer skyline and page geometry are retained. No new design or photo was introduced.

The colleague's supplied paragraph is retained word-for-word in `copy.json` and the PDF. The insurance-agent subtitle, banner, supporting card copy and CTA are adapted to property management using that supplied scope. Intro text is fitted into the existing two columns. The source print page remains 630 × 810 pt (8.75 × 11.25 inches); existing page boxes are preserved, with no new print certification claimed.

Owner spacing correction: list items now flow from their common top alignment with a consistent 9 pt gap after each item's actual text height. Bullet markers follow the new positions; old fixed positions are removed. Text, typography and card geometry are unchanged. Do not retain old bullet coordinates after changing copy length. Outside the text/list regions the artwork remains pixel-identical to the source at 144 dpi.

`GCPRO-ERP-Property-Management-REVIEW.pdf` is the review deliverable; PNG is its visual preview. `copy.json` and `build.py` are the editable source for this adaptation. To rebuild from this repository, install `requirements.txt` and run `python build.py`. Fonts and original PDF resolve relative to `marketing/`; no Downloads paths are used.

This review does not replace `releases/2026-10-20` or CURRENT_RELEASE.json. PM Brochure's separate water-photo request has not been applied to a guessed file; this Agency ERP layout has no existing photo slot. The user has not supplied a separate brochure/photo target in this test.
