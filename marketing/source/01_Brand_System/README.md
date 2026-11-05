# GCPRO ASP / PSP Marketing Kit — Source

Source files for the GCPRO Restoration marketing kit (Agency Support Program for insurance agents + Plumber Support Program for plumbers).
Layouts are HTML/CSS templates; a Python script renders print-ready PDFs (with bleed), preview PDFs (with trim/fold guides) and fillable PDFs.

For AI assistants: read `AI_CONTEXT.md` first (rules, brand, decisions). Photo slots and prompts: `PHOTOS.md`.

## Requirements
- Python 3.10+
- `pip install playwright pymupdf pillow` (Playwright uses Chromium: `playwright install chromium` if not installed)
- Fonts are local in `fonts/` (Montserrat, Inter) — no internet needed.

## Build
```bash
python3 build.py LB5 RC5 RR5 PSP5 DF5 ERP5 SR01 SR02 SR03 SR04_1 SR05 SR06_1 NB5 AP5 PR5 INV5
```
Output goes to `out/`:
- `<name>.pdf` — print file with 0.125" bleed
- `<name>_preview.pdf` — same with trim/fold guide lines (for review only, not for print)
- `<name> FILLABLE.pdf` — auto-created when the layout has form fields

## Piece keys
| Key | Document | Format |
|---|---|---|
| LB5 | ASP Leave Behind Trifold (for insurance agents) | Trifold 11x8.5, 2 pages |
| RC5 | ASP New Client Renewal Trifold – Commercial | Trifold |
| RR5 | ASP New Client Renewal Trifold – Residential | Trifold |
| PSP5 | PSP Plumber Leave Behind Trifold | Trifold |
| DF5 | ASP Digital Flyer | Letter |
| ERP5 | ASP Agency ERP Flyer | Letter |
| SR01, SR02, SR03, SR05 | ASP Special Reports (2 pages) | Letter |
| SR04_1, SR06_1 | ASP Special Reports 04, 06 (1-page versions) | Letter |
| NB5 | NonBinding Statement of Mutual Commitment (form) | Letter |
| AP5 | Preferred Agency Profile (form, 2 pages) | Letter |
| PR5 | Customer Policy Review & Coverage Risk Assessment (form, 2 pages) | Letter |
| INV5 | Hi-Tech Inspection Invoice (form) | Letter |

(`LB` = old v4 layout, `SR0x` without `_1` for 04/06 = 2-page variants; kept for reference, not used in the final kit.)

## Files
| File | What it is |
|---|---|
| `build.py` | All layouts (one function per piece), PDF rendering, fillable-field generation |
| `kit.css` | All styles. Many overrides are appended at the end — later rules win |
| `content.json` | ALL texts, verbatim from the original PDFs. Edit texts only here |
| `content.py`, `lines.py` | Scripts used to extract texts from the originals + verify word-for-word |
| `photos.json` | Photo slot → file, focus point (`object-position`), optional `zoom` |
| `assets/` | Logos (vector SVG), QR, backgrounds (city duotone, skyline line art), stamp, icons |
| `assets/photos/` | Photos used in the layouts (+ `*-src` originals for backgrounds) |
| `fonts/` | Montserrat + Inter (woff2, free, SIL Open Font License) |

## Common edits
- **Change a text:** edit `content.json` → rebuild the piece. (Texts must stay verbatim to the originals unless the owner approves a change.)
- **Change a photo:** put the file in `assets/photos/`, set `"file"` in `photos.json`; adjust `"focus": "X% Y%"` (lower Y = show more of the top of the image). Rebuild.
- **Change phone / website / company name:** `CONTACT` in `content.json` (`contact` block) → rebuild all.
- **Colors / fonts / spacing:** `kit.css` (`:root` variables; the last `:root` override wins).
- **Check a layout:** open `out/<name>_preview.pdf` — blue line = trim, dashed = folds.
