from __future__ import annotations
from typing import List, Tuple
import pathlib, re, random, math, time

# -------- identifier scan --------
def collect_ids(path: str, limit: int = 1_000) -> list[str]:
    pat = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
    seen = set()
    for f in pathlib.Path(path).rglob("*.py"):
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for m in pat.finditer(txt):
            tok = m.group(0)
            if tok not in seen:
                seen.add(tok)
                if len(seen) >= limit:
                    return list(seen)
    return list(seen)

# -------- Damerau-Levenshtein --------
def dl(a: str, b: str) -> int:
    m, n = len(a), len(b)
    D = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): D[i][0] = i
    for j in range(n+1): D[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+cost)
            if i>1 and j>1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:
                D[i][j] = min(D[i][j], D[i-2][j-2]+1)
    return D[m][n]

# -------- dynamic budget --------
def budget(L:int, alpha=0.25, floor=1, ceil=4): 
    return max(floor, min(ceil, math.ceil(alpha*L)))

# -------- unified suggester --------
def suggest(typo:str,
            dic:List[str],
            mode:str="dynamic",
            *, top_k:int=5,
            alpha:float=0.25,
            floor:int=1, ceil:int=4,
            max_retry:int=5,
            max_dist:int=2) -> List[Tuple[str,int]]:
    start=time.time()
    if mode=="constant":
        k=max_dist
        cand=[(t,d) for t in dic if (d:=dl(typo,t))<=k]
    else:                                    # dynamic
        k=budget(len(typo),alpha,floor,ceil)
        for _ in range(max_retry+1):
            cand=[(t,d) for t in dic if (d:=dl(typo,t))<=k]
            if cand or k>=ceil+max_retry: break
            k+=1
    cand.sort(key=lambda x:(x[1],len(x[0])))
    print(f"time taken: {time.time()-start:.4f} sec")
    return cand[:top_k]

# -------- demo --------
if __name__=="__main__":
    random.seed(42)
    MODE="constant"      # "dynamic" or "constant"
    print(f"{MODE.capitalize()}-threshold Damerau–Levenshtein autocorrect")
    print("------------------------------------------------")
    ids=collect_ids("./src",1000)
    print("identifiers:",len(ids))
    typo="display_monstsr_invntoty"
    if MODE=="constant":
        res=suggest(typo,ids,mode="constant",top_k=5,max_dist=10)
    else:
        res=suggest(typo,ids,mode="dynamic",top_k=5)
    print("input :",typo)
    for t,d in res:
        print(f" • {t:<25} (d={d})")
