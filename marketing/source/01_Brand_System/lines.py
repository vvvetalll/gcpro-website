import pymupdf as fitz, json, sys, re
SRC="/tmp/claude-0/-home-claude/70c4a61a-7f05-5862-8994-f767c6c90bbf/scratchpad/v4/GC_PRO_ASP_GCPRO_Chicago/"
PIECES={
 "LB":("GC PRO  FILL IN ASP  Leave Behind Trifold.pdf","tri"),
 "RC":("GC PRO FILL IN ASP New Client Renewal Trifold Commercial.pdf","tri"),
 "RR":("GC PRO FILL IN ASP New Client Renewal Trifold Residential.pdf","tri"),
 "DF":("GC PRO  FILL IN ASP Digital Flyer.pdf","df"),
 "ERP":("GC PRO  FILL IN ASP Agency ERP Flyer.pdf","one"),
}
def panel(kind,x,y):
    if kind=="tri": return 0 if x<264 else (1 if x<528 else 2)
    if kind=="df": return 0 if y<100 else (1 if x<300 else 2)
    return 0
def lines(key):
    f,kind=PIECES[key]; d=fitz.open(SRC+f); out={}
    for pn,p in enumerate(d):
        rows=[]
        for b in p.get_text("dict")["blocks"]:
            if b["type"]!=0: continue
            for l in b["lines"]:
                spans=[s for s in l["spans"] if s["text"].strip()]
                if not spans: continue
                t="".join(s["text"] for s in l["spans"])
                big=max(spans,key=lambda s:len(s["text"]))
                rows.append(dict(x=round(l["bbox"][0]),y=round(l["bbox"][1]),size=big["size"],font=big["font"],color=big["color"],text=t,
                     bold=[s["text"] for s in spans if ("Bold" in s["font"] or "Medium" in s["font"]) and "Bold" not in big["font"]]))
        # merge same-baseline fragments (bullets drawn as separate spans)
        rows.sort(key=lambda r:(panel(kind,r["x"],r["y"]),r["y"],r["x"]))
        merged=[]
        for r in rows:
            if merged and panel(kind,r["x"],r["y"])==panel(kind,merged[-1]["x"],merged[-1]["y"]) and abs(r["y"]-merged[-1]["y"])<=2:
                merged[-1]["text"]+=" "+r["text"]; merged[-1]["bold"]+=r["bold"]
            else: merged.append(r)
        for r in merged:
            out.setdefault((pn+1,panel(kind,r["x"],r["y"])),[]).append(r)
    return out
if __name__=="__main__":
    for (pg,pa),rows in sorted(lines(sys.argv[1]).items()):
        print(f"--- p{pg} panel{pa}")
        for i,r in enumerate(rows): print(f"{i:3d} {r['size']:4.1f} {r['font'][:16]:16} {r['text']!r} {('B:'+str(r['bold'])) if r['bold'] else ''}")
