"""Verbatim content source for the GCPRO ASP kit.
Blocks reference line ranges in the original PDFs (lines.py), so text is never retyped by hand.
Run: python3 content.py  -> writes content.json and verifies word-for-word coverage.
"""
import json, re, collections
from lines import lines

CTRL = re.compile(r"[\x00-\x08\x0b-\x1f]")


def clean(t):
    t = CTRL.sub("", t).replace("\t", " ")
    return re.sub(r"\s+", " ", t).strip()


class Src:
    def __init__(self, key):
        self.key, self.L = key, lines(key)

    def txt(self, *ranges):
        parts = []
        for pg, pa, a, b in ranges:
            rows = self.L[(pg, pa)]
            parts += [clean(r["text"]) for r in rows[a:b + 1]]
        return clean(" ".join(parts))

    def items(self, *ranges):
        """bullet list: split on bullet chars"""
        t = self.txt(*ranges)
        return [clean(x) for x in re.split(r"•", t) if clean(x)]

    def lines_as_items(self, pg, pa, groups):
        rows = self.L[(pg, pa)]
        return [clean(" ".join(clean(rows[i]["text"]) for i in g)).lstrip("• ").strip() for g in groups]


C = {}

# ---------------- Leave Behind Trifold ----------------
s = Src("LB")
C["LB"] = {
    "cover_h1": s.txt((1, 2, 0, 2)),
    "flap_h2": s.txt((1, 0, 0, 0)),
    "flap_checklist": s.lines_as_items(1, 0, [[1], [2], [3, 4], [5, 6], [7, 8]]),
    "back_247": [s.txt((1, 1, 0, 0)), s.txt((1, 1, 1, 2))],
    "p1_h2": s.txt((2, 0, 0, 1)),
    "p1_h3": s.txt((2, 0, 2, 2)),
    "p1_p1": s.txt((2, 0, 3, 8)),
    "p1_p2": s.txt((2, 0, 9, 12)),
    "p2_h3a": s.txt((2, 1, 0, 0)),
    "p2_p1": s.txt((2, 1, 1, 6)),
    "p2_p2": s.txt((2, 1, 7, 11)),
    "p2_h3b": s.txt((2, 1, 12, 12)),
    "p2_p3": s.txt((2, 1, 13, 17)),
    "p2_h3c": s.txt((2, 1, 18, 18)),
    "p2_p4": s.txt((2, 1, 19, 25)),
    "p3_h2": s.txt((2, 2, 0, 2)),
    "p3_features": [
        {"h": s.txt((2, 2, 3, 3)), "p": s.txt((2, 2, 4, 7))},
        {"h": s.txt((2, 2, 8, 8)), "p": s.txt((2, 2, 9, 13))},
        {"h": s.txt((2, 2, 14, 14)), "p": s.txt((2, 2, 15, 21))},
    ],
    "code_out": s.txt((1, 1, 6, 6)),
    "code_in": s.txt((2, 1, 26, 26)),
}

# ---------------- Renewal Trifold Commercial ----------------
s = Src("RC")
C["RC"] = {
    "cover_h1": s.txt((1, 2, 0, 2)),
    "flap_h2": s.txt((1, 0, 0, 2)),
    "flap_features": [
        {"h": s.txt((1, 0, 3, 3)), "p": s.txt((1, 0, 4, 9))},
        {"h": s.txt((1, 0, 10, 10)), "p": s.txt((1, 0, 11, 16))},
        {"h": s.txt((1, 0, 17, 17)), "p": s.txt((1, 0, 18, 23))},
    ],
    "back_247": [s.txt((1, 1, 0, 0)), s.txt((1, 1, 1, 2))],
    "in_h1": s.txt((2, 0, 0, 0)),
    "a_h3": s.txt((2, 0, 1, 2)),
    "a_p1": s.txt((2, 0, 3, 8)),
    "a_p2": s.txt((2, 0, 9, 14)),
    "a_p3": s.txt((2, 0, 15, 19)),
    "a_p4": s.txt((2, 0, 20, 22)),
    "b_h3": s.txt((2, 0, 23, 23)),
    "b_p1": s.txt((2, 0, 24, 27)),
    "b_bullets": s.items((2, 0, 28, 31), (2, 1, 0, 2)),   # text flowed across panels in the original
    "b_p2": s.txt((2, 1, 3, 6)),
    "b_p3": s.txt((2, 1, 7, 9)),
    "c_h3": s.txt((2, 1, 10, 11)),
    "c_before": s.txt((2, 1, 12, 17)),
    "c_during": s.txt((2, 1, 18, 18)),
    "c_during_bullets": s.items((2, 1, 19, 29)),
    "c_after": s.txt((2, 1, 30, 30), (2, 2, 0, 4)),      # flowed across panels in the original
    "d_h3": s.txt((2, 2, 5, 5)),
    "d_p": s.txt((2, 2, 6, 9)),
    "services_h": s.txt((2, 2, 10, 10)),
    "services": [s.txt((2, 2, i, i)) for i in range(11, 16)],
    "code": s.txt((1, 1, 6, 6)),
}

# ---------------- Renewal Trifold Residential ----------------
s = Src("RR")
C["RR"] = {
    "cover_h1": s.txt((1, 2, 0, 2)),
    "flap_h2": s.txt((1, 0, 0, 3)),
    "flap_features": [
        {"h": s.txt((1, 0, 4, 4)), "p": s.txt((1, 0, 5, 9))},
        {"h": s.txt((1, 0, 10, 10)), "p": s.txt((1, 0, 11, 15))},
        {"h": s.txt((1, 0, 16, 16)), "p": s.txt((1, 0, 17, 22))},
    ],
    "back_247": [s.txt((1, 1, 0, 0)), s.txt((1, 1, 1, 2))],
    "in_h1": s.txt((2, 0, 0, 1)),
    "a_h3": s.txt((2, 0, 2, 2)),
    "a_p1": s.txt((2, 0, 3, 6)),
    "a_p2": s.txt((2, 0, 7, 10)),
    "b_h3": s.txt((2, 0, 11, 12)),
    "b_p1": s.txt((2, 0, 13, 18)),
    "b_p2": s.txt((2, 0, 19, 24)),
    "b_p3": s.txt((2, 0, 25, 27)),
    "c_h3": s.txt((2, 1, 0, 0)),
    "c_p1": s.txt((2, 1, 1, 4)),
    "c_p2": s.txt((2, 1, 5, 7)),
    "c_bullets": s.items((2, 1, 8, 18)),
    "services_h": s.txt((2, 2, 0, 0)),
    "services": [s.txt((2, 2, i, i)) for i in range(1, 6)],
    "code": s.txt((1, 1, 6, 6)),
}

# ---------------- Digital Flyer ----------------
s = Src("DF")
C["DF"] = {
    "eyebrow": s.txt((1, 0, 0, 0)),
    "h1": s.txt((1, 1, 0, 0)),
    "p1": s.txt((1, 1, 1, 5)),
    "p2": s.txt((1, 1, 6, 9)),
    "cta": "Call for an inspection at",
    "p3": s.txt((1, 1, 11, 16)),
    "p4": s.txt((1, 1, 17, 20)),
    "services_h": s.txt((1, 1, 21, 21)),
    "services": s.items((1, 1, 22, 26)),
    "rating": s.txt((1, 2, 0, 0)),
    "why_h2": s.txt((1, 2, 1, 2)),
    "why": s.items((1, 2, 3, 21)),
}

# ---------------- ERP Flyer ----------------
s = Src("ERP")
C["ERP"] = {
    "title": s.txt((1, 0, 0, 0)),
    "tagline": s.txt((1, 0, 1, 1)),
    "banner": s.txt((1, 0, 2, 3)),
    "intro1": s.txt((1, 0, 4, 5)),
    "intro2": s.txt((1, 0, 6, 8)),
    "before_h": s.txt((1, 0, 9, 9)),
    "before": s.items((1, 0, 10, 13)),
    "during_h": s.txt((1, 0, 14, 14)),
    "during": s.items((1, 0, 15, 20)),
    "after_h": s.txt((1, 0, 21, 21)),
    "after": s.items((1, 0, 22, 24)),
    "cta_h": s.txt((1, 0, 25, 25)),
    "cta_1": "Simply call GCPRO Restoration at",
    "cta_2": s.txt((1, 0, 27, 28)),
    "code": s.txt((1, 0, 30, 30)),
}

CONTACT = {"name": "GCPRO Restoration", "phone": "(847) 656-3322", "web": "gcprochicago.com",
           "label": "24-HOUR EMERGENCY SERVICE"}


# ---------------- verification ----------------
def words(t):
    return re.findall(r"[A-Za-z0-9’'“”\"$&/\-.,!?():;—%+]+", t)


def flat(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from flat(v)
    else:
        for v in o:
            yield from flat(v)


IGNORE = {"(847)", "656-3322", "gcprochicago.com", "GCPRO", "Restoration", "24-HOUR", "EMERGENCY",
          "SERVICE", "24/7", "|", "at"}

if __name__ == "__main__":
    json.dump({"pieces": C, "contact": CONTACT}, open("content.json", "w"), indent=1, ensure_ascii=False)
    ok = True
    for key in C:
        L = lines(key)
        src = collections.Counter(w.strip(".,!?:;") for rows in L.values() for r in rows for w in words(clean(r["text"])).__iter__())
        got = collections.Counter(w.strip(".,!?:;") for t in flat(C[key]) for w in words(t))
        missing = {w: c for w, c in (src - got).items() if w not in IGNORE and w}
        extra = {w: c for w, c in (got - src).items() if w}
        print(key, "missing:", missing or "-", "| extra:", extra or "-")
        ok &= not extra
    print("VERBATIM OK" if ok else "CHECK")
