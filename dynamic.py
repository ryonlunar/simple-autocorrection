from __future__ import annotations
from typing import List, Tuple
import pathlib, re, random, string, math
import time

def collect_identifiers(root: str, limit: int = 1_000) -> list[str]:
    id_pattern = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
    seen: set[str] = set()

    for file in pathlib.Path(root).rglob("*.py"):
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for m in id_pattern.finditer(text):
            tok = m.group(0)
            if tok not in seen:
                seen.add(tok)
                if len(seen) >= limit:
                    return list(seen)
    return list(seen)

def damerau_levenshtein(a: str, b: str) -> int:
    m, n = len(a), len(b)
    D = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): D[i][0] = i
    for j in range(n+1): D[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            D[i][j] = min(
                D[i-1][j]   + 1,         # deletion
                D[i][j-1]   + 1,         # insertion
                D[i-1][j-1] + cost       # substitution
            )
            if (i > 1 and j > 1 and
                a[i-1] == b[j-2] and
                a[i-2] == b[j-1]):
                D[i][j] = min(D[i][j], D[i-2][j-2] + 1)  # transposition
    return D[m][n]

def edit_budget(length: int,
                alpha: float = 0.25,
                floor: int = 1,
                ceiling: int = 4) -> int:
    """Return a length-scaled edit allowance."""
    return max(floor, min(ceiling, math.ceil(alpha * length)))

def suggest_token(typo, dictionary, *, top_k=5, alpha=0.25,
                floor=1, ceiling=4, max_retry=5):
    start = time.time()
    k = edit_budget(len(typo), alpha, floor, ceiling)

    for _ in range(max_retry + 1):
        candidates = [
            (tok, d) for tok in dictionary
            if (d := damerau_levenshtein(typo, tok)) <= k
        ]
        if candidates or k >= ceiling + max_retry:
            break
        k += 1
    candidates.sort(key=lambda x: (x[1], len(x[0])))
    end = time.time()
    print(f"time taken: {end - start:.4f} sec")
    return candidates[:top_k]

if __name__ == "__main__":
    random.seed(42)

    print("Dynamic-threshold Damerau–Levenshtein autocorrect")
    print("------------------------------------------------")
    code_dict = collect_identifiers("./src", limit=1_000)
    print(f"Identifiers collected : {len(code_dict)}")

    user_input = "display_monstsr_invntoty"
    suggestions = suggest_token(user_input, code_dict, top_k=5)

    print(f"\nInput    : {user_input}")
    print("Suggestions (token, distance):")
    for tok, dist in suggestions:
        print(f" • {tok:<25}  (d = {dist})")
