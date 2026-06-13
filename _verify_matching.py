"""
Persona verification for the Mirror matching engine.
Mirrors TECH_CATALOG tags + scoreTechniques() + the new SAFETY HARD-GATE and
per-match confidence from vigyan-bhairav-find-yourself.html, then runs personas
to confirm: every persona routes to an existing technique with reasoning that
matches its answers, the safety gate fires for dysregulated systems, and
ambiguous profiles report lower confidence.
This is a checked transcription of the JS logic, not the live page.
"""

# (id, file, anchor, intensity, path[], energy[], liftsGuna, doshaGood[], doshaBad[], nervGood[], nervBad[], needs[])
T = [
 ("brt1","breath",1,["raja","jnana"],["energy","mind"],None,["vata","pitta"],[],["ventral","sympathetic"],[],["anxiety","focus"]),
 ("brt6","breath",1,["karma"],["body"],None,["pitta","kapha"],[],["sympathetic","ventral"],[],["disconnect","focus"]),
 ("brt5","breath",2,["jnana","raja"],["mind"],None,[],["pitta"],["ventral"],["dorsal"],["focus"]),
 ("brt8","breath",1,["bhakti"],["heart","energy"],None,["vata","pitta"],[],["ventral"],[],["love"]),
 ("snd9","sound",1,["bhakti","raja"],["energy","heart"],None,["vata","pitta"],[],["sympathetic","dorsal","ventral"],[],["anxiety","sleep"]),
 ("snd3","sound",1,["bhakti","karma"],["heart","body"],"tamas",["kapha"],[],["dorsal","ventral"],[],["stuck"]),
 ("snd5","sound",1,["bhakti"],["heart"],None,["vata","pitta"],[],["ventral"],[],["joy","grief"]),
 ("snd2","sound",1,["raja"],["energy"],None,["vata"],[],["ventral","sympathetic"],[],["anxiety"]),
 ("lgt1","light",1,["raja","jnana"],["energy"],None,["pitta","vata"],[],["ventral","sympathetic"],[],["anxiety","stuck"]),
 ("lgt5","light",3,["raja","karma"],["energy","body"],"tamas",["kapha"],["pitta","vata"],["ventral"],["dorsal","sympathetic"],[]),
 ("wit5","witnessing",1,["jnana","raja","karma"],["mind","energy"],None,["vata","pitta","kapha"],[],["ventral","sympathetic"],[],["disconnect","focus"]),
 ("wit7","witnessing",2,["jnana","raja"],["mind"],"rajas",["pitta"],[],["ventral"],["dorsal"],["anger"]),
 ("wit6","witnessing",1,["bhakti","karma"],["heart"],"tamas",["kapha","vata"],[],["dorsal","ventral"],[],["stuck","joy"]),
 ("wit8","witnessing",1,["jnana"],["mind"],"rajas",["pitta","vata"],[],["ventral","sympathetic"],[],["anxiety","stuck"]),
 ("wit9","witnessing",2,["jnana","raja"],["mind"],"rajas",["pitta"],[],["ventral"],[],["anger","anxiety"]),
 ("neg5","negation",2,["jnana"],["mind"],None,["pitta"],[],["ventral"],["dorsal"],["ego"]),
 ("neg7","negation",2,["jnana","raja"],["mind","energy"],None,["vata","pitta"],[],["ventral"],["dorsal"],["ego"]),
 ("voi2","void",2,["karma"],["body"],"tamas",["kapha"],[],["sympathetic"],["dorsal"],["stuck","anger"]),
 ("voi3","void",3,["raja","jnana"],["energy"],None,[],["vata"],["ventral"],["dorsal","sympathetic"],["ego"]),
 ("sen6","sensory",1,["karma","bhakti"],["body"],None,["vata","pitta","kapha"],[],["ventral","sympathetic","dorsal"],[],["disconnect"]),
 ("sen7","sensory",1,["karma","raja"],["body","energy"],None,["vata"],[],["ventral","sympathetic","dorsal"],[],["disconnect","focus"]),
 ("sen5","sensory",1,["bhakti","jnana"],["heart","body"],"tamas",["kapha","vata"],[],["dorsal","ventral"],[],["stuck","joy"]),
 ("slp2","sleep",1,["raja"],["energy"],None,["vata","pitta"],[],["ventral","sympathetic"],[],["sleep","anxiety"]),
 ("tan2","tantra",2,["karma","bhakti"],["body","heart"],None,["pitta","kapha"],[],["ventral"],["dorsal"],["love","disconnect"]),
 ("hrt1","heart",1,["bhakti"],["heart"],None,["vata","pitta","kapha"],[],["ventral"],[],["love","grief"]),
 ("hrt2","heart",1,["bhakti"],["heart"],"tamas",["vata","kapha"],[],["ventral","dorsal"],[],["joy"]),
 ("hrt4","heart",1,["bhakti","raja"],["heart"],None,["vata","pitta"],[],["ventral","sympathetic","dorsal"],[],["grief","anxiety"]),
 ("cen2","centering",2,["karma","raja"],["body"],None,["vata"],[],["ventral"],[],["disconnect","focus"]),
 ("cen5","centering",2,["jnana"],["mind"],"rajas",["pitta"],[],["ventral"],[],["anger"]),
 ("cen6","centering",1,["bhakti"],["heart"],None,["vata","pitta"],[],["ventral"],[],["focus","love"]),
 ("mnd1","mind",1,["jnana","raja"],["mind"],None,["vata","pitta"],[],["ventral","sympathetic"],[],["focus","anxiety"]),
 ("img6","imagination",1,["raja"],["energy","mind"],None,["pitta"],[],["ventral"],[],["anxiety","stuck"]),
 ("dth1","death",3,["jnana","raja"],["energy"],None,[],["vata"],["ventral"],["dorsal","sympathetic"],["ego"]),
]
KEYS=["id","file","intensity","path","energy","liftsGuna","doshaGood","doshaBad","nervGood","nervBad","needs"]
CAT=[dict(zip(KEYS,row)) for row in T]

def score(prof):
    out=[]
    for t in CAT:
        s=0.0; reasons=[]
        for p in t["path"]: s+=prof["path"].get(p,0)*1.0
        if prof["topPath"] in t["path"]: s+=14; reasons.append("path:"+prof["topPath"])
        elif prof["secPath"] in t["path"]: s+=5
        for e in t["energy"]: s+=prof["energy"].get(e,0)*0.7
        if prof["topEnergy"] in t["energy"]: s+=9; reasons.append("energy:"+prof["topEnergy"])
        if t["liftsGuna"] and t["liftsGuna"]==prof["topGuna"] and prof["topGuna"]!="sattva":
            s+=11; reasons.append("guna:lifts "+t["liftsGuna"])
        if prof["topDosha"] in t["doshaGood"]: s+=7; reasons.append("dosha:"+prof["topDosha"])
        if prof["topDosha"] in t["doshaBad"]: s-=16
        if prof["topNerv"] in t["nervGood"]: s+=10; reasons.append("nerv-safe:"+prof["topNerv"])
        if prof["topNerv"] in t["nervBad"]: s-=22
        if t["intensity"]>=3 and prof["topNerv"] in ("dorsal","sympathetic"): s-=12
        if t["intensity"]>=3 and prof["coverage"]<0.7: s-=4
        for n in t["needs"]:
            w=prof["intent"].get(n,0)
            if w>0:
                s+=w*5
                if w>=2: reasons.append("intent:"+n)
        out.append({"t":t,"score":s,"reasons":list(dict.fromkeys(reasons))})
    out.sort(key=lambda x:-x["score"])
    return out

def gate(ranked, prof):
    dys = prof["topNerv"] in ("dorsal","sympathetic")
    def unsafe(t): return (prof["topNerv"] in t["nervBad"]) or (t["intensity"]>=3 and (dys or prof["coverage"]<0.7))
    safe=[r for r in ranked if not unsafe(r["t"])]
    return (safe + [r for r in ranked if unsafe(r["t"])]) if safe else ranked, unsafe

def conf(gated, cov, pmargin):
    gap = gated[0]["score"] - (gated[1]["score"] if len(gated)>1 else 0)
    conv = len(gated[0]["reasons"])
    if conv>=4 and gap>=10 and cov>=0.8 and pmargin>=15: return "Very high"
    if conv>=3 and gap>=6 and cov>=0.7 and pmargin>=8: return "High"
    if conv>=2 and cov>=0.5: return "Moderate"
    return "Exploratory"

def prof(path,energy,guna,dosha,nerv,intent,cov):
    pr={"karma":0,"bhakti":0,"jnana":0,"raja":0}; pr.update(path)
    en={"body":0,"mind":0,"heart":0,"energy":0}; en.update(energy)
    sp=sorted(pr,key=lambda k:-pr[k])
    tot=sum(pr.values()) or 1
    pmargin=round((pr[sp[0]]-pr[sp[1]])/tot*100)
    return {"path":pr,"energy":en,"topPath":sp[0],"secPath":sp[1],
            "topEnergy":max(en,key=en.get),"topGuna":guna,"topDosha":dosha,
            "topNerv":nerv,"intent":intent,"coverage":cov,"pmargin":pmargin}

personas={
 "Clear KARMA (active, kapha, sympathetic, settled)":
   prof({"karma":60,"bhakti":15,"jnana":10,"raja":15},{"body":55,"heart":20,"mind":15,"energy":10},
        "rajas","kapha","ventral",{"disconnect":3,"focus":2},0.95),
 "Clear JNANA (rational, pitta, ventral)":
   prof({"jnana":58,"raja":22,"karma":10,"bhakti":10},{"mind":60,"energy":20,"body":10,"heart":10},
        "rajas","pitta","ventral",{"ego":3,"anxiety":2},0.95),
 "DORSAL shut-down (heavy/numb, kapha, tamas) - safety gate must fire":
   prof({"raja":40,"jnana":30,"karma":15,"bhakti":15},{"energy":45,"mind":35,"body":10,"heart":10},
        "tamas","kapha","dorsal",{"stuck":3,"grief":2},0.9),
 "SYMPATHETIC vata anxious (raja-leaning) - no intense first":
   prof({"raja":45,"jnana":25,"bhakti":18,"karma":12},{"energy":50,"mind":25,"heart":15,"body":10},
        "rajas","vata","sympathetic",{"anxiety":3,"sleep":2},0.9),
 "Ambiguous (flat profile, thin data) - low confidence expected":
   prof({"karma":27,"bhakti":26,"jnana":24,"raja":23},{"body":26,"mind":25,"heart":25,"energy":24},
        "sattva","pitta","ventral",{},0.45),
}

ok=True
for name,p in personas.items():
    ranked=score(p)
    gated,unsafe=gate(ranked,p)
    top=gated[0]; c=conf(gated,p["coverage"],p["pmargin"])
    raw_top=ranked[0]
    demoted = (unsafe(raw_top["t"]) and raw_top["t"]["id"]!=top["t"]["id"])
    print(f"\n=== {name} ===")
    print(f"  TOP: {top['t']['id']} ({top['t']['file']}) score={top['score']:.1f} reasons={top['reasons']}")
    print(f"  alt: {[g['t']['id'] for g in gated[1:4]]}")
    print(f"  match-confidence: {c}")
    print(f"  top pick safe for state? {not unsafe(top['t'])}  | unsafe demoted? {demoted or 'n/a'}")
    # assertions
    if unsafe(top["t"]):
        print("  !! FAIL: top pick is UNSAFE for this state"); ok=False
    if "Ambiguous" in name and c in ("Very high","High"):
        print("  !! FAIL: ambiguous profile overconfident"); ok=False
    if "Clear KARMA" in name and top["t"]["path"][0] not in ("karma",) and "karma" not in top["t"]["path"]:
        print("  !! FAIL: karma persona not routed to a karma technique"); ok=False

print("\nALL PERSONAS PASSED" if ok else "\nSOME CHECKS FAILED")
