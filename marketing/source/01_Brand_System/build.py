import os
"""Build GCPRO ASP kit PDFs from content.json + kit.css (v3 editorial style).
Usage: python3 build.py [LB ...]  -> out/<name>.pdf (print, bleed) + out/<name>_preview.pdf (fold/trim guides)
Texts come only from content.json. Display-only case styling via tc() (letters unchanged).
"""
import json, sys, html, re, pathlib

tc = lambda s: s  # headings keep source case; CSS sets uppercase
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
DATA = json.load(open(ROOT / "content.json"))
C, K = DATA["pieces"], DATA["contact"]
PHOTOS = json.load(open(ROOT / "photos.json")) if (ROOT / "photos.json").exists() else {}
B = 0.125
e = html.escape

SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "on", "or", "the", "to", "with", "is"}


def tc_unused(s):
    """Display title case for ALL-CAPS source headings (same words/letters, only case)."""
    if s != s.upper():
        return s
    out = []
    for i, w in enumerate(s.split(" ")):
        core = re.sub(r"[^A-Za-z]", "", w)
        if core in {"GCPRO", "ASP", "ERP"}:
            out.append(w)
        elif i and w.lower() in SMALL:
            out.append(w.lower())
        else:
            lw = w.lower()
            m = re.search(r"[a-z]", lw)
            out.append(lw[:m.start()] + lw[m.start()].upper() + lw[m.start() + 1:] if m else lw)
    return " ".join(out)


def panel(x, w, cls="", first=False, last=False, body=""):
    left = 0 if first else B + x
    width = w + (B if first else 0) + (B if last else 0)
    c = " ".join(filter(None, ["panel", cls, "first" if first else "", "last" if last else ""]))
    return f'<div class="{c}" style="left:{left}in;width:{width}in">{body}</div>'


def guides(folds):
    g = "".join(f'<div class="fold" style="left:{B + f}in"></div>' for f in folds)
    return f'<div class="guides">{g}<div class="trim"></div></div>'


SLOGAN = ('<div class="slogan">RECOVER <i></i> RESTORE <i></i> REBUILD</div>')


def photo(slot, style="", extra=""):
    ph = PHOTOS.get(slot)
    if ph and ph.get("file"):
        f = ROOT / "assets/photos/graded" / ph["file"]
        if not f.exists():
            f = ROOT / "assets/photos" / ph["file"]
        if f.exists():
            rel = f.relative_to(ROOT).as_posix()
            return (f'<div class="photo" style="{style}"><img src="{rel}" '
                    f'style="object-position:{ph.get("focus", "center")};transform:scale({ph.get("zoom", 1)});transform-origin:{ph.get("focus", "center")}">{extra}</div>')
    return f'<div class="photo" style="{style}"><span>PHOTO · {e((ph or {}).get("idea", slot))}</span></div>'


def bleed(top=False, left=False, right=False, bottom=False, first=False, last=False, mt="0"):
    """negative margins so a block runs to the trim+bleed edge of its panel"""
    t = "calc(-1 * (var(--b) + var(--safe)))" if top else mt
    bt = "calc(-1 * (var(--b) + .3in))" if bottom else "0"
    l = ("calc(-1 * (var(--b) + var(--safe)))" if first else "calc(-1 * var(--safe))") if left else "0"
    r = ("calc(-1 * (var(--b) + var(--safe)))" if last else "calc(-1 * var(--safe))") if right else "0"
    return f"margin:{t} {r} {bt} {l};"


def contact(name=True):
    n = f'<div class="h3" style="margin:0 0 .04in">{e(K["name"])}</div>' if name else ""
    return (f'<div class="contact"><div class="kicker">{e(K["label"])}</div>{n}'
            f'<div class="phone">{e(K["phone"])}</div><div class="web">{e(K["web"])}</div></div>')


# ---------------------------------------------------------------- Leave Behind
def LB(preview):
    c = C["LB"]
    # OUTSIDE: [flap 3.625][back 3.6875][cover 3.6875]
    items = "".join(f'<li><span class="n">{i+1:02d}</span><span class="t">{e(t)}</span></li>'
                    for i, t in enumerate(c["flap_checklist"]))
    flap = (photo("LB.flap", bleed(top=True, left=True, right=True, first=True) + "height:3.7in")
            + f'<div style="margin-top:.34in" class="h2">{e(tc(c["flap_h2"]))}</div><div class="accent"></div>'
            + f'<ul class="numlist">{items}</ul>')

    back = (f'<img src="assets/logo.svg" style="width:2.05in;margin-top:.1in">'
            f'<div style="flex:1"></div>'
            f'<div style="font-family:var(--head);font-weight:900;font-size:50pt;line-height:.95;color:var(--ink-navy);letter-spacing:-.02em">{e(c["back_247"][0])}</div>'
            f'<div class="kicker" style="color:var(--ink-navy);margin-top:.1in">{e(c["back_247"][1])}</div>'
            f'<div class="hair" style="margin:.3in 0 .26in"></div>'
            f'<div class="h3">{e(K["name"])}</div>'
            f'<div class="contact"><div class="phone">{e(K["phone"])}</div><div class="web">{e(K["web"])}</div></div>'
            f'<img src="assets/qr.svg" style="width:.8in;height:.8in;margin-top:.42in">'
            f'<div style="flex:1"></div>'
            '')

    cover = (f'<img src="assets/logo-white.svg" style="width:1.55in">'
             f'<div style="flex:1"></div>'
             f'<div class="kicker">{e(c["flap_h2"])}</div>'
             f'<div class="display" style="margin-top:.14in">{e(tc(c["cover_h1"]))}</div>'
             f'<div class="hair" style="margin:.28in 0 .14in"></div>'
             f'<div class="kicker" style="color:rgba(255,255,255,.6)">{e(K["label"])}</div>'
             f'<div style="font-family:var(--head);font-weight:800;font-size:15pt;color:#fff;margin-top:.05in">{e(K["phone"])}'
             f'<span style="font-family:var(--sans);font-size:8pt;color:rgba(255,255,255,.65);margin-left:.14in">{e(K["web"])}</span></div>'
             + photo("LB.cover", "flex:0 0 3.55in;" + bleed(left=True, right=True, bottom=True, last=True, mt=".3in")))
    out = (panel(0, 3.625, "paper", first=True, body=flap)
           + panel(3.625, 3.6875, "", body=back)
           + panel(7.3125, 3.6875, "dark", last=True, body=cover))

    # INSIDE: [3.6875][3.6875][3.625]
    p1 = (photo("LB.inside1", bleed(top=True, left=True, right=True, first=True) + "height:3.35in")
          + f'<div style="margin-top:.34in" class="h2">{e(tc(c["p1_h2"]))}</div><div class="accent"></div>'
          f'<div class="h3">{e(c["p1_h3"])}</div><p>{e(c["p1_p1"])}</p>'
          f'<div style="flex:1"></div><div class="quote"><p>{e(c["p1_p2"])}</p></div>')
    p2 = (f'<div class="h2">{e(tc(c["p2_h3a"]))}</div><div class="accent"></div>'
          f'<p>{e(c["p2_p1"])}</p><p>{e(c["p2_p2"])}</p>'
          f'<div class="hair"></div>'
          f'<div class="h3">{e(c["p2_h3b"])}</div><p>{e(c["p2_p3"])}</p>'
          f'<div class="h3" style="margin-top:.08in">{e(c["p2_h3c"])}</div><p>{e(c["p2_p4"])}</p>'
          + photo("LB.inside2", "flex:1;min-height:1in;margin-top:.12in")
          )
    feats = "".join(f'<div class="feature"><div class="n">{i+1:02d}</div><div><div class="h3">{e(f["h"])}</div>'
                    f'<p style="margin:0">{e(f["p"])}</p></div></div>' for i, f in enumerate(c["p3_features"]))
    p3 = (f'<img src="assets/logo-white.svg" style="width:1.25in;margin-bottom:.4in">'
          f'<div class="h2">{e(tc(c["p3_h2"]))}</div><div class="accent"></div>{feats}'
          f'<div style="flex:1"></div><div class="hair"></div>{contact(name=False)}')
    inn = (panel(0, 3.6875, "paper", first=True, body=p1)
           + panel(3.6875, 3.6875, "", body=p2)
           + panel(7.375, 3.625, "dark", last=True, body=p3))

    g1 = guides([3.625, 7.3125]) if preview else ""
    g2 = guides([3.6875, 7.375]) if preview else ""
    return (f'<section class="sheet tri">{out}{g1}</section>'
            f'<section class="sheet tri">{inn}{g2}</section>'), (11 + 2 * B, 8.5 + 2 * B)


def rings(size, x, y, color="rgba(255,255,255,.14)", n=7, gap=.13):
    """brand motif: concentric rings echoing the logo mark (cropped by panel)"""
    circles = "".join(f'<circle cx="50" cy="50" r="{49 - i * gap * 100 / size:.2f}" fill="none" stroke="{color}" stroke-width=".28"/>'
                      for i in range(n))
    return (f'<svg class="rings" viewBox="0 0 100 100" style="width:{size}in;height:{size}in;left:{x}in;top:{y}in">{circles}</svg>')


def emph_tail(s, n=2):
    """colour the last n words (style only)"""
    w = s.split(" ")
    return e(" ".join(w[:-n])) + " <em>" + e(" ".join(w[-n:])) + "</em>"


# ---------------------------------------------------------------- shared v5 blocks
def lead(text, prefix):
    """bold the lead-in words that were bold in the original (style only)"""
    if text.startswith(prefix):
        return f'<strong style="color:#fff;font-weight:700">{e(prefix)}</strong>{e(text[len(prefix):])}'
    return e(text)


T247 = ('<span style="color:var(--navy)">24</span>/<span style="color:var(--navy)">7</span>' if os.environ.get('SPLIT247', '1') != '0' else '24/7')


def back_v5(code, services_h=None, services=None):
    icon247 = ROOT / "assets/icon-247.svg"
    mark = (f'<img src="assets/icon-247.svg" style="height:.8in">' if icon247.exists() else
            f'<div style="font-family:var(--head);font-weight:900;font-size:50pt;line-height:.9;letter-spacing:-.02em;color:var(--ember)">{T247}</div>')
    svc = ""
    if services:
        svc = (f'<div class="kicker" style="color:var(--navy);margin:.34in 0 .08in">{e(services_h)}</div>'
               + "".join(f'<div class="svc">{e(x)}</div>' for x in services))
    deco = ('<div class="skyline"></div>' if os.environ.get('SKYLINE', '1') != '0'
            else rings(5.6, 1.0, 4.6, color="rgba(26,50,125,.10)"))
    return (deco
            + f'<img src="assets/logo.svg" style="width:2.1in">'
            f'<div style="height:.95in;flex-shrink:0"></div>' + mark +
            f'<div class="kicker" style="color:var(--navy);margin-top:.12in;font-size:8pt">EMERGENCY SERVICE</div>'
            f'<div class="accent"></div>'
            f'<div class="h3" style="color:var(--ink)">{e(K["name"])}</div>'
            f'<div style="font-family:var(--head);font-weight:800;font-size:21pt;color:var(--navy)">{e(K["phone"])}</div>'
            f'<div style="font-size:9pt;color:var(--body);margin-top:.04in">{e(K["web"])}</div>'
            + svc +
            f'<div style="flex:1"></div>'
            f'<img src="assets/qr-black.svg" style="width:.78in;height:.78in">'
            '')


def cover_v5(slot, h1, kicker=None, tail=2):
    k = (f'<div class="kicker" style="height:.16in">{e(kicker)}</div>' if kicker
         else '<div style="height:.16in"></div>')
    return (photo(slot, bleed(top=True, left=True, right=True, last=True) + "flex:0 0 4.05in")
            + f'<div class="cvnavy" style="background:var(--ink-navy);flex:1;display:flex;flex-direction:column;margin:0 calc(-1 * (var(--b) + var(--safe))) calc(-1 * (var(--b) + .3in)) calc(-1 * var(--safe));'
            f'padding:.3in calc(var(--b) + var(--safe)) calc(var(--b) + .32in) var(--safe);position:relative">'
            f'<img src="assets/logo-white.svg" style="width:1.45in;margin-bottom:.26in">{k}'
            f'<div class="display" style="margin-top:.1in">{emph_tail(h1, tail)}</div>'
            f'<div style="margin-top:auto;padding-top:.14in;border-top:.6pt solid rgba(255,255,255,.2)">'
            f'<div class="kicker" style="color:rgba(255,255,255,.6)">{e(K["label"])}</div>'
            f'<div style="font-family:var(--head);font-weight:800;font-size:16pt;margin-top:.04in">{e(K["phone"])}</div></div></div>')


def feats_light(fs):
    return "".join(f'<div style="display:grid;grid-template-columns:.46in 1fr;padding:.13in 0;border-top:.6pt solid var(--hair)">'
                   f'<span class="bignum">{i+1:02d}</span><div><div class="h3">{e(f["h"])}</div>'
                   f'<p style="margin:0">{e(f["p"])}</p></div></div>' for i, f in enumerate(fs))


def bullets(items, dark=False):
    return '<ul class="dots' + (' dk' if dark else '') + '">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def contact_dark():
    return (f'<div style="border-top:.6pt solid rgba(255,255,255,.16);padding-top:.16in">'
            f'<div class="kicker">{e(K["label"])}</div>'
            f'<div style="font-family:var(--head);font-weight:800;font-size:20pt;margin-top:.05in">{e(K["phone"])}</div>'
            f'<div style="font-size:9pt;color:rgba(255,255,255,.8);margin-top:.03in">{e(K["web"])}</div></div>')


def navy_foot(text, first=False):
    left = "calc(-1 * (var(--b) + var(--safe)))" if first else "calc(-1 * var(--safe))"
    pl = "calc(var(--b) + var(--safe))" if first else "var(--safe)"
    return (f'<div class="quote5" style="margin:0 calc(-1 * var(--safe)) calc(-1 * (var(--b) + .3in)) {left};'
            f'padding:.22in var(--safe) calc(var(--b) + .34in) {pl}"><div class="bar"></div><p>{e(text)}</p></div>')


# ---------------------------------------------------------------- Leave Behind (shared blocks)
def LB5(preview):
    c = C["LB"]
    items = "".join(f'<li><span class="bignum">{i+1:02d}</span><span class="t">{e(t)}</span></li>'
                    for i, t in enumerate(c["flap_checklist"]))
    flap = (photo("LB.flap", bleed(top=True, left=True, right=True, first=True) + "height:2.45in;flex-shrink:0")
            + f'<div style="margin-top:.3in" class="h2">{e(c["flap_h2"])}</div><div class="accent"></div>'
            + f'<ul class="list5">{items}</ul>')
    back = back_v5(c["code_out"])
    cover = cover_v5("LB.cover", c["cover_h1"], tail=2)
    out = (panel(0, 3.625, "", first=True, body=flap)
           + panel(3.625, 3.6875, "", body=back)
           + panel(7.3125, 3.6875, "ink5", last=True, body=cover))

    p1 = (photo("LB.inside1", bleed(top=True, left=True, right=True, first=True) + "height:3.85in")
          + f'<div style="margin-top:.3in" class="h2">{e(c["p1_h2"])}</div><div class="accent"></div>'
          f'<div class="h3">{e(c["p1_h3"])}</div><p>{e(c["p1_p1"])}</p>'
          f'<div style="flex:1"></div>' + navy_foot(c["p1_p2"], first=True))
    p2 = (f'<div class="h2">{e(c["p2_h3a"])}</div><div class="accent"></div>'
          f'<p>{e(c["p2_p1"])}</p><p>{e(c["p2_p2"])}</p>'
          f'<div class="hair"></div>'
          f'<div class="h3">{e(c["p2_h3b"])}</div><p>{e(c["p2_p3"])}</p>'
          f'<div class="h3" style="margin-top:.08in">{e(c["p2_h3c"])}</div><p>{e(c["p2_p4"])}</p>'
          + photo("LB.inside2", "flex:1;min-height:1in;margin-top:.12in")
          )
    feats = "".join(f'<div style="display:grid;grid-template-columns:.46in 1fr;padding:.15in 0;border-top:.6pt solid rgba(255,255,255,.16)">'
                    f'<span class="bignum">{i+1:02d}</span><div><div class="h3">{e(f["h"])}</div>'
                    f'<p style="margin:0">{e(f["p"])}</p></div></div>' for i, f in enumerate(c["p3_features"]))
    p3 = (rings(4.2, 2.1, -2.3)
          + f'<div class="h2" style="margin-top:.05in">{e(c["p3_h2"])}</div><div class="accent"></div>{feats}'
          f'<div style="flex:1"></div>' + contact_dark())
    inn = (panel(0, 3.6875, "", first=True, body=p1)
           + panel(3.6875, 3.6875, "", body=p2)
           + panel(7.375, 3.625, "navy5", last=True, body=p3))
    g1 = guides([3.625, 7.3125]) if preview else ""
    g2 = guides([3.6875, 7.375]) if preview else ""
    return (f'<section class="sheet tri v5 t-lb">{out}{g1}</section>'
            f'<section class="sheet tri v5 t-lb">{inn}{g2}</section>'), (11 + 2 * B, 8.5 + 2 * B)


# ---------------------------------------------------------------- Renewal Trifold Commercial
def RC5(preview):
    c = C["RC"]
    flap = (photo("RC.flap", bleed(top=True, left=True, right=True, first=True) + "height:2.45in;flex-shrink:0")
            + f'<div style="margin-top:.3in" class="h2">{e(c["flap_h2"])}</div><div class="accent"></div>'
            + feats_light(c["flap_features"]))
    back = back_v5(c["code"], c["services_h"], c["services"])
    cover = cover_v5("RC.cover", c["cover_h1"], tail=2)
    out = (panel(0, 3.625, "compact", first=True, body=flap)
           + panel(3.625, 3.6875, "", body=back)
           + panel(7.3125, 3.6875, "ink5", last=True, body=cover))

    p1 = (photo("RC.inside1", bleed(top=True, left=True, right=True, first=True) + "height:2.2in")
          + f'<div style="margin-top:.3in" class="h2">{e(c["in_h1"])}</div><div class="accent"></div>'
          f'<div class="h3">{e(c["a_h3"])}</div><p>{e(c["a_p1"])}</p><p>{e(c["a_p2"])}</p><p>{e(c["a_p3"])}</p>'
          f'<div style="flex:1"></div>' + navy_foot(c["a_p4"], first=True))
    p2 = (f'<div class="h2">{e(c["b_h3"])}</div><div class="accent"></div>'
          f'<p>{e(c["b_p1"])}</p>' + bullets(c["b_bullets"]) +
          f'<p>{e(c["b_p2"])}</p>'
          f'<div class="offer"><p>{e(c["b_p3"])}</p></div>'
          + photo("RC.inside2", "flex:1;min-height:.9in;margin-top:.16in"))
    p3 = (rings(4.2, 2.1, -2.3)
          + f'<div class="h2" style="margin-top:.05in">{e(c["c_h3"])}</div><div class="accent"></div>'
          f'<div class="step"><p>{lead(c["c_before"], "Before the loss")}</p></div>'
          f'<div class="step"><p style="margin-bottom:.05in">{lead(c["c_during"], "During the loss")}</p>{bullets(c["c_during_bullets"], True)}</div>'
          f'<div class="step"><p>{lead(c["c_after"], "After the loss")}</p></div>'
          f'<div class="step"><div class="h3">{e(c["d_h3"])}</div><p>{e(c["d_p"])}</p></div>'
          f'<div style="flex:1"></div>' + contact_dark())
    inn = (panel(0, 3.6875, "", first=True, body=p1)
           + panel(3.6875, 3.6875, "", body=p2)
           + panel(7.375, 3.625, "navy5 tight", last=True, body=p3))
    g1 = guides([3.625, 7.3125]) if preview else ""
    g2 = guides([3.6875, 7.375]) if preview else ""
    return (f'<section class="sheet tri v5 t-rc">{out}{g1}</section>'
            f'<section class="sheet tri v5 t-rc">{inn}{g2}</section>'), (11 + 2 * B, 8.5 + 2 * B)


# ---------------------------------------------------------------- Renewal Trifold Residential
def RR5(preview):
    c = C["RR"]
    flap = (photo("RR.flap", bleed(top=True, left=True, right=True, first=True) + "height:2.45in;flex-shrink:0")
            + f'<div style="margin-top:.3in" class="h2">{e(c["flap_h2"])}</div><div class="accent"></div>'
            + feats_light(c["flap_features"]))
    back = back_v5(c["code"], c["services_h"], c["services"])
    cover = cover_v5("RR.cover", c["cover_h1"], tail=3)
    out = (panel(0, 3.625, "compact", first=True, body=flap)
           + panel(3.625, 3.6875, "", body=back)
           + panel(7.3125, 3.6875, "ink5", last=True, body=cover))

    p1 = (photo("RR.inside1", bleed(top=True, left=True, right=True, first=True) + "height:3.85in")
          + f'<div style="margin-top:.3in" class="h2">{e(c["in_h1"])}</div><div class="accent"></div>'
          f'<div class="h3">{e(c["a_h3"])}</div><p>{e(c["a_p1"])}</p><p>{e(c["a_p2"])}</p>')
    p2 = (f'<div class="h2">{e(c["b_h3"])}</div><div class="accent"></div>'
          f'<p>{e(c["b_p1"])}</p><p>{e(c["b_p2"])}</p>'
          + photo("RR.inside2", "flex:1;min-height:1in;margin:.08in 0 .3in")
          + navy_foot(c["b_p3"]))
    p3 = (rings(4.2, 2.1, -2.3)
          + f'<div class="h2" style="margin-top:.05in">{e(c["c_h3"])}</div><div class="accent"></div>'
          f'<p>{e(c["c_p1"])}</p><p>{e(c["c_p2"])}</p>' + bullets(c["c_bullets"], True) +
          f'<div style="flex:1"></div>' + contact_dark())
    inn = (panel(0, 3.6875, "", first=True, body=p1)
           + panel(3.6875, 3.6875, "", body=p2)
           + panel(7.375, 3.625, "navy5", last=True, body=p3))
    g1 = guides([3.625, 7.3125]) if preview else ""
    g2 = guides([3.6875, 7.375]) if preview else ""
    return (f'<section class="sheet tri v5 t-rr">{out}{g1}</section>'
            f'<section class="sheet tri v5 t-rr">{inn}{g2}</section>'), (11 + 2 * B, 8.5 + 2 * B)


# ---------------------------------------------------------------- Letter (8.5x11) shared blocks
def letter_header(right_html=""):
    return (f'<div class="lhead"><img src="assets/logo.svg" style="width:1.7in">{right_html}</div>')


def letter_footer(code=""):
    """same contact block as the trifold navy panels (contact_dark), plus QR on the right"""
    c = contact_dark().replace('border-top:.6pt solid rgba(255,255,255,.16);padding-top:.16in', 'border:0;padding:0')
    return (f'<div class="lfoot">{c}'
            f'<div style="display:flex;align-items:flex-end;gap:.16in">'
            f'{f"<div class=code style=color:rgba(255,255,255,.5)>{e(code)}</div>" if code else ""}'
            f'<div style="background:#fff;padding:.05in;line-height:0"><img src="assets/qr-black.svg" style="width:.62in;height:.62in"></div></div>'
            f'</div>')

# ---------------------------------------------------------------- Digital Flyer
def DF5(preview):
    c = C["DF"]
    right = (f'<div class="hcontact"><div class="kicker">{e(c["eyebrow"])}</div>'
             f'<div class="hphone">{e(K["phone"])}</div></div>')
    star = ('<svg viewBox="0 0 24 24" style="width:.2in;height:.2in"><path fill="#f5b301" '
            'd="M12 2.2l2.9 6.3 6.9.7-5.2 4.7 1.5 6.8L12 17.2l-6.1 3.5 1.5-6.8L2.2 9.2l6.9-.7z"/></svg>')
    gfile = next((f for f in ("assets/google-g.svg", "assets/google-g.png") if (ROOT / f).exists()), None)
    gicon = f'<img src="{gfile}" style="width:.34in;height:.34in">' if gfile else ""
    rating = (f'<div class="rating5">{gicon}<span class="rnum">{e(c["rating"])}</span>'
              f'<span style="display:flex;flex-direction:column;gap:.035in"><span class="rstars">{star * 5}</span>'
              f'<span class="rlabel">{e(K.get("rating_label", ""))}</span></span></div>')
    svc = "".join(f'<div class="svc">{e(x)}</div>' for x in c["services"])
    body = (letter_header(right)
            + photo("DF.hero", "height:2.05in;margin:0 calc(-1 * (var(--b) + var(--lsafe)));flex-shrink:0")
            + f'<div class="lband"><div class="display" style="font-size:25pt">{emph_tail(c["h1"], 3)}</div></div>'
            + f'<div class="lcols">'
              f'<div class="lcol"><p class="lead">{e(c["p1"])}</p><p>{e(c["p2"])}</p><p>{e(c["p3"])}</p><p style="margin:0">{e(c["p4"])}</p></div>'
              f'<div class="whycard"><div class="h2" style="font-size:13pt">{e(c["why_h2"])}</div><div class="accent" style="margin:.09in 0 .1in"></div>'
              f'{bullets(c["why"])}</div>'
            f'</div>'
            + f'<div class="ctastrip"><div class="offer" style="margin:0"><p style="font-size:12pt">{e(c["cta"])} '
              f'<span style="color:var(--ember)">{e(K["phone"])}</span></p></div>{rating}</div>'
            + f'<div class="lsvc"><div class="kicker" style="color:var(--navy);margin-bottom:.08in">{e(c["services_h"])}</div><div class="svcrow">{svc}</div></div>'
            + letter_footer())
    g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
    return f'<section class="sheet letter v5"><div class="lpage">{body}</div>{g}</section>', (8.5 + 2 * B, 11 + 2 * B)


# ---------------------------------------------------------------- ERP Flyer
def ERP5(preview):
    c = C["ERP"]
    right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
             f'<div class="hphone">{e(K["phone"])}</div></div>')
    def col(i, h, items):
        return (f'<div class="whycard phase"><span class="bignum">{i:02d}</span>'
                f'<div class="h3" style="margin:.07in 0 .1in">{e(h)}</div>{bullets(items)}</div>')
    body = (letter_header(right)
            + f'<div class="lband" style="display:flex;align-items:center;gap:.24in">'
              f'<img src="assets/erp-shield.png" class="erpshield">'
              f'<div><div class="display" style="font-size:23pt;white-space:nowrap">{emph_tail(c["title"], 2)}</div>'
              f'<div style="font-family:var(--head);font-weight:600;font-size:11.5pt;color:rgba(255,255,255,.85);margin-top:.07in">{e(c["tagline"])}</div></div></div>'
            + f'<div class="erp-intro3"><div class="offer" style="margin:0 0 .16in"><p style="font-size:12pt">{e(c["banner"])}</p></div>'
              f'<div class="lcols" style="padding:0"><p style="margin:0">{e(c["intro1"])}</p><p style="margin:0">{e(c["intro2"])}</p></div></div>'
            + f'<div class="phases">{col(1, c["before_h"], c["before"])}{col(2, c["during_h"], c["during"])}{col(3, c["after_h"], c["after"])}</div>'
            + f'<div class="erp-cta"><div class="h2" style="font-size:13.5pt">{e(c["cta_h"])}</div><div class="accent" style="margin:.09in 0 .09in"></div>'
              f'<p style="margin:0;font-size:10pt">{e(c["cta_1"])} <strong style="color:var(--ember);font-family:var(--head)">{e(K["phone"])}</strong> {e(c["cta_2"])}</p></div>'
            + letter_footer())
    g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
    return f'<section class="sheet letter v5"><div class="lpage">{body}</div>{g}</section>', (8.5 + 2 * B, 11 + 2 * B)

# ---------------------------------------------------------------- Special Reports (2 pages, 2-col flow)
def sr_block(b):
    k, t = b["k"], e(b["t"])
    if k == "lead":  return f'<p class="sr-lead">{t}</p>'
    if k == "h":     return f'<div class="sr-h"><div class="h3">{t}</div></div>'
    if k == "li":    return f'<div class="sr-li">{t}</div>'
    if k == "close": return f'<p class="sr-close">{t}</p>'
    return f'<p>{t}</p>'


def SR(key):
    def fn(preview):
        c = C[key]
        B = c["blocks"]
        title = next(b["t"] for b in B if b["k"] == "title")
        close = next((b["t"] for b in B if b["k"] == "close"), "")
        flow = "".join(sr_block(b) for b in B if b["k"] not in ("title", "close", "tiny"))
        right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
                 f'<div class="hphone">{e(K["phone"])}</div></div>')
        contact = (f'<div class="sr-contact">'
                   f'<p class="sr-close">{e(close)}</p>'
                   f'<div class="sr-card">'
                   f'<div class="sr-row"><span>Company</span><b>{e(K["name"])}</b></div>'
                   f'<div class="sr-row"><span>Phone</span><b>{e(K["phone"])}</b></div>'
                   f'<div class="sr-row"><span>Website</span><b>{e(K["web"])}</b></div>'
                   f'<div class="sr-row"><span>Salesperson</span><i></i></div>'
                   f'<div class="sr-row"><span>Phone</span><i></i></div>'
                   f'<div class="sr-row"><span>Email</span><i></i></div></div></div>')
        foot = '<div class="sr-foot"></div>'
        p1 = (letter_header(right)
              + f'<div class="lband">'
                f'<div class="display" style="font-size:20pt">{e(title)}</div></div>'
              + photo(f"{key}.hero", "height:2.3in;margin:0 calc(-1 * (var(--b) + var(--lsafe)));flex-shrink:0")
              + f'<div class="sr-cols" id="c1">{flow}</div>' + foot)
        p2 = (f'<div class="sr-top"><img src="assets/logo.svg" style="width:1.25in"><span class="kicker" style="color:var(--muted)">{e(c["code"])}</span></div>'
              + f'<div class="sr-cols" id="c2"></div>' + contact
              + letter_footer() + foot.replace('sr-foot', 'sr-foot on-dark'))
        g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
        js = """<script>window.__layout=function(){
          var a=document.getElementById('c1'), b=document.getElementById('c2');
          var ph=a.previousElementSibling; var all=Array.from(a.children);
          function over(el){return el.scrollWidth>el.clientWidth+2||el.scrollHeight>el.clientHeight+2}
          function flow(h){
            ph.style.height=h+'in';
            all.forEach(function(n){n.classList.remove('cont');a.appendChild(n);});
            while(over(a)&&a.lastElementChild){b.insertBefore(a.lastElementChild,b.firstChild);}
            while(a.lastElementChild&&a.lastElementChild.classList.contains('sr-h')){b.insertBefore(a.lastElementChild,b.firstChild);}
            var f=b.firstElementChild; if(f&&f.classList.contains('sr-li')) f.classList.add('cont');
            return !over(b);
          }
          function split(){
            var hd=null, n=b.firstElementChild;
            if(n&&n.classList.contains('sr-h')){ hd=n; n=hd.nextElementSibling; a.appendChild(hd);
              if(over(a)||!n){ b.insertBefore(hd,b.firstChild); return; } }
            var ok=trysplit(n); if(!ok&&hd) b.insertBefore(hd,b.firstChild);
          }
          function trysplit(n){
            if(!n||n.children.length) return false;
            if(!(n.tagName=='P'&&!n.className)&&!n.classList.contains('sr-li')) return false;
            var w=n.textContent.split(' '), part=n.cloneNode(false); part.classList.remove('cont'); a.appendChild(part);
            var lo=0,hi=w.length-1;
            while(lo<hi){var m=Math.ceil((lo+hi)/2); part.textContent=w.slice(0,m).join(' '); if(over(a)) hi=m-1; else lo=m;}
            if(lo<6||w.length-lo<6){a.removeChild(part);return false;}
            part.textContent=w.slice(0,lo).join(' '); part.classList.add('split');
            if(n.classList.contains('cont')) part.classList.add('cont');
            n.textContent=w.slice(lo).join(' '); n.classList.add('cont','splitrest'); return true;
          }
          for(var h=3.6;h>=0.9;h-=0.1){ if(flow(h)){ split(); return; } }
          flow(0.9);
        }</script>"""
        return (f'<section class="sheet letter v5"><div class="lpage">{p1}</div>{g}</section>'
                f'<section class="sheet letter v5"><div class="lpage">{p2}</div>{g}</section>{js}'), (8.5 + 2 * B_, 11 + 2 * B_)
    return fn

def SR1(key):
    """Special Report on ONE page, no photo; font auto-fits"""
    def fn(preview):
        c = C[key]
        B = c["blocks"]
        title = next(b["t"] for b in B if b["k"] == "title")
        close = next((b["t"] for b in B if b["k"] == "close"), "")
        flow = "".join(sr_block(b) for b in B if b["k"] not in ("title", "close", "tiny"))
        right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
                 f'<div class="hphone">{e(K["phone"])}</div></div>')
        contact = (f'<div class="sr-contact one">'
                   f'<p class="sr-close">{e(close)}</p>'
                   f'<div class="sr-card">'
                   f'<div class="sr-row"><span>Company</span><b>{e(K["name"])}</b></div>'
                   f'<div class="sr-row"><span>Phone</span><b>{e(K["phone"])}</b></div>'
                   f'<div class="sr-row"><span>Website</span><b>{e(K["web"])}</b></div>'
                   f'<div class="sr-row"><span>Salesperson</span><i></i></div>'
                   f'<div class="sr-row"><span>Phone</span><i></i></div>'
                   f'<div class="sr-row"><span>Email</span><i></i></div></div></div>')
        body = (letter_header(right)
                + f'<div class="lband">'
                  f'<div class="display" style="font-size:18pt">{e(title)}</div></div>'
                + f'<div class="sr-cols one" id="c1">{flow}</div>' + contact
                + letter_footer())
        g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
        js = """<script>window.__layout=function(){
          var a=document.getElementById('c1');
          function over(el){return el.scrollWidth>el.clientWidth+2||el.scrollHeight>el.clientHeight+2}
          for(var fs=9.4; fs>=7.6; fs-=0.1){ a.style.setProperty('--fs', fs+'pt'); if(!over(a)) {document.body.dataset.fs=fs.toFixed(1); return;} }
          document.body.dataset.fs='OVERFLOW';
        }</script>"""
        return f'<section class="sheet letter v5"><div class="lpage">{body}</div>{g}</section>{js}', (8.5 + 2 * B_, 11 + 2 * B_)
    return fn



B_ = B


# ---------------------------------------------------------------- Non-Binding agreement
def NB5(preview):
    c = C["NB"]
    right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
             f'<div class="hphone">{e(K["phone"])}</div></div>')
    goals = "".join(f'<li><span class="bignum">{i+1:02d}</span><span class="t">{e(t)}</span></li>' for i, t in enumerate(c["goals"]))
    sig = "".join(f'<div class="sig"><i></i><span>{e(x)}</span></div>' for x in c["sig"])
    body = (letter_header(right)
            + f'<div class="lband"><div class="display" style="font-size:19pt">{e(c["title"])}</div></div>'
            + f'<div class="nb-body"><div class="nb-sec"><div class="h2" style="font-size:14pt">{e(c["h_you"])}</div><div class="accent" style="margin:.09in 0 .1in"></div>'
              f'<p>{e(c["p_you"])}</p><ul class="list5 nb-goals">{goals}</ul></div>'
            + f'<div class="whycard nb-el"><p style="margin:0 0 .1in">{e(c["p_elements"])}</p>{bullets(c["elements"])}</div>'
            + f'<div class="nb-sec"><div class="h2" style="font-size:14pt">{e(c["h_us"])}</div><div class="accent" style="margin:.09in 0 .1in"></div>'
              f'<p>{e(c["p_us"])}</p><div class="offer" style="margin:.06in 0 0"><p style="font-size:9.6pt;font-weight:600">{e(c["note"])}</p></div></div>'
            + f'<div class="nb-sig">{sig}</div></div>'
            + letter_footer())
    g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
    return f'<section class="sheet letter v5"><div class="lpage">{body}</div>{g}</section>', (8.5 + 2 * B, 11 + 2 * B)


# ---------------------------------------------------------------- form helpers
def fline(label, grow=1):
    return f'<div class="fl" style="flex:{grow}"><span>{e(label)}</span><i></i></div>'


def cbox(label):
    return f'<span class="cb"><b></b>{e(label)}</span>'


def fsec(h, inner):
    return (f'<div class="fsec"><div class="h2" style="font-size:12pt">{e(h)}</div>'
            f'<div class="accent" style="margin:.07in 0 .12in"></div>{inner}</div>')


# ---------------------------------------------------------------- Agency Profile (internal form, 2 pages)
def AP5(preview):
    c = C["AP"]
    right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
             f'<div class="hphone">{e(K["phone"])}</div></div>')
    info = "".join(f'<div class="frow">{"".join(fline(x, 1.6 if i == 0 and len(r) > 1 else 1) for i, x in enumerate(r))}</div>' for r in c["info"])
    n, pz = c["staff_labels"]
    staff = "".join(f'<div class="frow staff">{fline(n,1.6)}{fline(pz,1)}<span class="vsep"></span>{fline(n,1.6)}{fline(pz,1)}</div>' for _ in range(3))
    chal = f'<div class="cbrow">{"".join(cbox(x) for x in c["chal"][:-1])}</div><div class="frow">{cbox(c["chal"][-1])}<div class="fl" style="flex:1"><i></i></div></div>'
    p1 = (letter_header(right)
          + f'<div class="lband"><div class="display" style="font-size:22pt">{e(c["title"])}</div></div>'
          + f'<div class="fbody roomy">'
          + f'<div class="fsec">{info}</div>'
          + fsec(c["staff_h"], staff)
          + fsec(c["chal_h"], chal)
          + '</div>' + letter_footer())
    meth = f'<div class="cbrow"><span class="lbl">{e(c["q2_m"])}</span>{"".join(cbox(x) for x in c["m"])}</div>'
    p2 = (f'<div class="sr-top"><img src="assets/logo.svg" style="width:1.25in"><span class="kicker" style="color:var(--muted)">{e(c["title"])}</span></div>'
          + f'<div class="fbody">'
          + fsec(c["q1_h"], f'<div class="cbrow">{"".join(cbox(x) for x in c["q1"])}</div>')
          + fsec(c["q2_h"], f'<div class="cbrow">{"".join(cbox(x) for x in c["q2"])}</div>{meth}'
                 f'<div class="frow">{fline(c["contact"])}</div><div class="frow">{fline(c["specify"])}</div>')
          + fsec(c["q3_h"], f'<div class="cbrow">{"".join(cbox(x) for x in c["m"])}</div>'
                 f'<div class="frow">{fline(c["contact"])}</div><div class="frow">{fline(c["specify"])}</div>')
          + fsec(c["q4_h"], "".join(f'<div class="cbrow">{cbox(x)}</div>' for x in c["q4"]))
          + fsec(c["q5_h"], f'<div class="cbrow">{cbox(c["q5"])}</div><div class="frow">{fline(c["name"],1)}{fline(c["email"],1)}</div>')
          + '</div>' + letter_footer())
    g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
    return (f'<section class="sheet letter v5"><div class="lpage">{p1}</div>{g}</section>'
            f'<section class="sheet letter v5"><div class="lpage">{p2}</div>{g}</section>'), (8.5 + 2 * B, 11 + 2 * B)


# ---------------------------------------------------------------- Policy Review (client form, 2 pages)
def PR5(preview):
    c = C["PR"]
    right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
             f'<div class="hphone">{e(K["phone"])}</div></div>')
    def stackrow(items):
        return '<div class="frow staff">' + "".join(fline(l, g) for l, g in items) + '</div>'
    def sec(h, ps, cbs=None, sug=None, cols=4):
        inner = "".join(f'<p>{e(x)}</p>' for x in ps)
        if cbs:
            inner += f'<div class="cbgrid" style="grid-template-columns:repeat({cols},auto)">' + "".join(cbox(x) for x in cbs) + '</div>'
        if sug:
            inner += f'<p class="sug">{e(sug)}</p>'
        return fsec(h, inner)
    info = "".join(stackrow(r) for r in c["fields"])
    p1 = (letter_header(right)
          + f'<div class="lband"><div class="display" style="font-size:21pt">{e(c["title"])}</div></div>'
          + f'<div class="fbody pr p1">'
          + f'<div class="fsec"><p class="sr-lead" style="font-size:10.4pt;margin-bottom:.2in">{e(c["intro"])}</p>{info}</div>'
          + sec(c["s1_h"], c["s1_p"], c["s1_c"], c["s1_s"], 3)
          + sec(c["s2_h"], c["s2_p"], c["s2_c"], c["s2_s"], 4)
          + sec(c["s5_h"], [c["s5_p"]])
          + '</div>' + letter_footer())
    refs = "".join(stackrow([(c["ref"][0], 1.3), (c["ref"][1], 1), (c["ref"][2], 1.5)]) for _ in range(3))
    p2 = (f'<div class="sr-top"><img src="assets/logo.svg" style="width:1.25in"><span class="kicker" style="color:var(--muted)">{e(c["title"])}</span></div>'
          + f'<div class="fbody pr p2">'
          + sec(c["s3_h"], c["s3_p"], c["s3_c"], c["s3_s"], 4)
          + sec(c["s4_h"], c["s4_p"], c["s4_c"], c["s4_s"], 3)
          + fsec(c["s6_h"], f'<p>{e(c["s6_p"])}</p>{refs}')
          + '</div>' + letter_footer())
    g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
    return (f'<section class="sheet letter v5"><div class="lpage">{p1}</div>{g}</section>'
            f'<section class="sheet letter v5"><div class="lpage">{p2}</div>{g}</section>'), (8.5 + 2 * B, 11 + 2 * B)


# ---------------------------------------------------------------- Hi-Tech Inspection Invoice
STAMP = (ROOT / 'assets/paid-stamp.svg').read_text()

def INV5(preview):
    c = C["INV"]
    F = lambda name, cls="": f'<i class="ic {cls}" data-field="text" data-name="{name}"></i>'
    right = (f'<div class="hcontact"><div class="kicker">{e(K["label"])}</div>'
             f'<div class="hphone">{e(K["phone"])}</div></div>')
    band = (f'<div class="lband inv-band"><div class="display" style="font-size:26pt">{e(c["title"])}</div>'
            f'<div class="inv-meta"><div><span>{e(c["date"])}</span>{F("Date")}</div>'
            f'<div><span>{e(c["num"])}</span>{F("Invoice_No")}</div></div></div>')
    addr = "".join(f'<div class="inv-box"><div class="inv-h">{e(x)}</div><i class="ib" data-field="multi" data-name="{x.replace(" ","_")}"></i></div>'
                   for x in (c["bill"], c["ship"]))
    meta = "".join(f'<div class="inv-box"><div class="inv-h">{e(x)}</div>{F(x)}</div>' for x in c["meta"])
    q, d, r, a = c["cols"]
    rows = ""
    for n in range(1, 11):
        desc = f'<span class="pre">{e(c["item1"])}</span>' if n == 1 else F(f"Description_{n}")
        rows += f'<tr><td>{F(f"Qty_{n}")}</td><td>{desc}</td><td>{F(f"Rate_{n}")}</td><td>{F(f"Amount_{n}")}</td></tr>'
    rows += (f'<tr class="tot"><td></td><td class="tl">{e(c["total"])}</td>'
             f'<td class="cur">{e(c["cur"])}</td><td>{F("Total")}</td></tr>')
    table = (f'<table class="inv-t"><thead><tr><th>{e(q)}</th><th>{e(d)}</th><th>{e(r)}</th><th>{e(a)}</th></tr></thead>'
             f'<tbody>{rows}</tbody></table>')
    sig = "".join(f'<div class="sig"><i></i><span>{e(x)}</span></div>' for x in c["sig"])
    body = (letter_header(right) + band
            + f'<div class="inv-body"><div class="wm"><span>{e(c["stamp"])}</span></div><div class="inv-addr2">{addr}</div>'
            + f'<div class="inv-meta3">{meta}</div>' + table
            + f'<div class="inv-sig">{sig}</div></div>'
            + letter_footer())
    g = '<div class="guides"><div class="trim"></div></div>' if preview else ""
    return f'<section class="sheet letter v5"><div class="lpage">{body}</div>{g}</section>', (8.5 + 2 * B, 11 + 2 * B)


# ---------------------------------------------------------------- PSP Plumber Leave Behind Trifold
def PSP5(preview):
    c = C["PSP"]
    items = "".join(f'<li><span class="bignum">{i+1:02d}</span><span class="t">{e(t)}</span></li>'
                    for i, t in enumerate(c["flap_checklist"]))
    flap = (photo("PSP.flap", bleed(top=True, left=True, right=True, first=True) + "height:2.45in;flex-shrink:0")
            + f'<div style="margin-top:.3in" class="h2">{e(c["flap_h2"])}</div><div class="accent"></div>'
            + f'<ul class="list5">{items}</ul>')
    back = back_v5(c["code"])
    cover = cover_v5("PSP.cover", c["cover_h1"], tail=2)
    out = (panel(0, 3.625, "", first=True, body=flap)
           + panel(3.625, 3.6875, "", body=back)
           + panel(7.3125, 3.6875, "ink5", last=True, body=cover))
    secs = lambda ss: "".join(f'<div class="h3"{" style=margin-top:.1in" if i else ""}>{e(x["h"])}</div><p>{e(x["p"])}</p>'
                              for i, x in enumerate(ss))
    p1 = (photo("PSP.inside1", bleed(top=True, left=True, right=True, first=True) + "flex:1;min-height:1.5in")
          + f'<div style="margin-top:.26in" class="h2">{e(c["p1_h2"])}</div><div class="accent"></div>'
          + secs(c["p1_secs"]))
    last = c["p2_secs"][-1]
    p2 = (photo("PSP.inside2", bleed(top=True) + "flex:1;min-height:1.5in;margin-left:calc(-1 * var(--safe));margin-right:calc(-1 * var(--safe))")
          + f'<div style="margin-top:.26in"></div>' + secs(c["p2_secs"][:-1])
          + f'<div class="quote5" style="margin:.2in calc(-1 * var(--safe)) calc(-1 * (var(--b) + .3in)) calc(-1 * var(--safe));'
            f'padding:.22in var(--safe) calc(var(--b) + .34in) var(--safe)"><div class="bar"></div>'
            f'<div class="h3" style="color:#fff">{e(last["h"])}</div><p>{e(last["p"])}</p></div>')
    feats = "".join(f'<div style="display:grid;grid-template-columns:.46in 1fr;padding:.15in 0;border-top:.6pt solid rgba(255,255,255,.16)">'
                    f'<span class="bignum">{i+1:02d}</span><div><div class="h3">{e(f["h"])}</div>'
                    f'<p style="margin:0">{e(f["p"])}</p></div></div>' for i, f in enumerate(c["p3_features"]))
    p3 = (f'<div class="h2" style="margin-top:.05in">{e(c["p3_h2"])}</div><div class="accent"></div>{feats}'
          f'<div style="flex:1"></div>' + contact_dark())
    inn = (panel(0, 3.6875, "", first=True, body=p1)
           + panel(3.6875, 3.6875, "", body=p2)
           + panel(7.375, 3.625, "navy5", last=True, body=p3))
    g1 = guides([3.625, 7.3125]) if preview else ""
    g2 = guides([3.6875, 7.375]) if preview else ""
    return (f'<section class="sheet tri v5 t-psp">{out}{g1}</section>'
            f'<section class="sheet tri v5 t-psp">{inn}{g2}</section>'), (11 + 2 * B, 8.5 + 2 * B)


PIECES = {"PSP5": ("GCPRO PSP Plumber Leave Behind Trifold v5", PSP5), "INV5": ("GCPRO ASP Hi-Tech Inspection Invoice v5", INV5), "PR5": ("GCPRO ASP Policy Review v5", PR5), "AP5": ("GCPRO ASP Agency Profile v5", AP5), "NB5": ("GCPRO ASP NonBinding Agreement v5", NB5), "LB": ("GCPRO ASP Leave Behind Trifold v4", LB), "LB5": ("GCPRO ASP Leave Behind Trifold v5", LB5), "RC5": ("GCPRO ASP Renewal Trifold Commercial v5", RC5), "RR5": ("GCPRO ASP Renewal Trifold Residential v5", RR5), "DF5": ("GCPRO ASP Digital Flyer v5", DF5), "ERP5": ("GCPRO ASP Agency ERP Flyer v5", ERP5), **{f"SR{i:02d}": (f"GCPRO ASP Special Report {i:02d} v5", SR(f"SR{i:02d}")) for i in range(1, 7)}, **{f"SR{i:02d}_1": (f"GCPRO ASP Special Report {i:02d} 1page", SR1(f"SR{i:02d}")) for i in range(1, 7)}}


# ---------------------------------------------------------------- fillable version
FIELD_JS = """() => {
  const out = []; const secs = [...document.querySelectorAll('section.sheet')];
  const used = {};
  function uniq(n){ n = n.replace(/[^A-Za-z0-9]+/g,'_').replace(/^_|_$/g,'') || 'field'; used[n]=(used[n]||0)+1; return used[n]>1? n+'_'+used[n] : n; }
  secs.forEach((sec, pi) => {
    const r0 = sec.getBoundingClientRect();
    const push = (el, type, label) => { const r = el.getBoundingClientRect();
      out.push({page: pi, type, name: uniq(label), x: r.left - r0.left, y: r.top - r0.top, w: r.width, h: r.height}); };
    sec.querySelectorAll('.fl i').forEach(i => { const sp = i.parentElement.querySelector('span'); push(i, 'text', sp ? sp.textContent : 'field'); });
    sec.querySelectorAll('.cb b').forEach(b => push(b, 'check', b.parentElement.textContent));
    sec.querySelectorAll('.sig i').forEach(i => push(i, 'text', i.parentElement.querySelector('span').textContent));
    sec.querySelectorAll('.sr-row i').forEach(i => push(i, 'text', i.parentElement.querySelector('span').textContent));
    sec.querySelectorAll('[data-field]').forEach(el => push(el, el.dataset.field, el.dataset.name || 'field'));
  });
  return out;
}"""


def make_fillable(pdf_path, fields):
    import pymupdf as fitz
    doc = fitz.open(str(pdf_path))
    k = 0.75  # css px -> pt
    for f in fields:
        page = doc[f["page"]]
        x0, y0, w, h = f["x"] * k, f["y"] * k, f["w"] * k, f["h"] * k
        wd = fitz.Widget()
        wd.field_name = f["name"]
        if f["type"] == "multi":
            wd.field_type = fitz.PDF_WIDGET_TYPE_TEXT
            wd.rect = fitz.Rect(x0 + 3, y0 + 3, x0 + w - 3, y0 + h - 3)
            wd.field_flags = fitz.PDF_TX_FIELD_IS_MULTILINE
            wd.text_font = "Helv"; wd.text_fontsize = 10; wd.text_color = (0.1, 0.2, 0.49)
            wd.border_width = 0
        elif f["type"] == "check":
            wd.field_type = fitz.PDF_WIDGET_TYPE_CHECKBOX
            wd.rect = fitz.Rect(x0, y0, x0 + w, y0 + h)
            wd.border_width = 0
        else:
            wd.field_type = fitz.PDF_WIDGET_TYPE_TEXT
            hh = max(min(h, 18), 15)
            wd.rect = fitz.Rect(x0, y0 + h - hh, x0 + w, y0 + h - 1)
            wd.text_font = "Helv"; wd.text_fontsize = 10; wd.text_color = (0.1, 0.2, 0.49)
            wd.border_width = 0
        page.add_widget(wd)
    out = str(pdf_path).replace(".pdf", " FILLABLE.pdf")
    doc.save(out, garbage=3, deflate=True)
    print("wrote", out, len(fields), "fields")


def render(keys):
    out = ROOT / "out"; out.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        for k in keys:
            name, fn = PIECES[k]
            for preview in (False, True):
                body, (w, h) = fn(preview)
                doc = (f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit.css">'
                       f'<style>@page{{size:{w}in {h}in;margin:0}}</style></head><body>{body}</body></html>')
                f = ROOT / f"_{k}.html"; f.write_text(doc)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.evaluate("window.__layout && window.__layout()")
                fs = pg.evaluate("document.body.dataset.fs || ''")
                if fs: print(k, "font", fs)
                dst = out / (name + ("_preview" if preview else "") + ".pdf")
                pg.pdf(path=str(dst), width=f"{w}in", height=f"{h}in", print_background=True,
                       margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
                print("wrote", dst)
                if not preview:
                    fields = pg.evaluate(FIELD_JS)
                    if fields:
                        make_fillable(dst, fields)
        br.close()


if __name__ == "__main__":
    render(sys.argv[1:] or list(PIECES))
