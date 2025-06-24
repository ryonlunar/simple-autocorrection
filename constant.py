from typing import List, Tuple
import pathlib, re, csv, random
import time

def collect_identifiers(root: str, limit: int = 1000) -> list[str]:
    id_pattern = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
    seen = set()

    for file in pathlib.Path(root).rglob("*.py"):
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
        except FileNotFoundError:
            continue
        for m in id_pattern.finditer(text):
            tok = m.group(0)
            if tok not in seen:
                seen.add(tok)
                if len(seen) >= limit:
                    break
        if len(seen) >= limit:
            break
    return list(seen)

def damerau_levenshtein(s: str, t: str) -> int:
    m, n = len(s), len(t)
    # DP table (m+1) × (n+1)
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # initialisation: transform empty prefix
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    # main loop
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s[i-1] == t[j-1] else 1

            # three standard operations
            deletion      = D[i-1][j] + 1
            insertion     = D[i][j-1] + 1
            substitution  = D[i-1][j-1] + cost
            D[i][j] = min(deletion, insertion, substitution)

            # transposition: check previous characters
            if (
                i > 1 and j > 1 and
                s[i-1] == t[j-2] and
                s[i-2] == t[j-1]
            ):
                D[i][j] = min(D[i][j], D[i-2][j-2] + 1)

    return D[m][n]

def suggest_token(
    typo: str,
    dictionary: List[str],
    max_distance: int = 2,
    top_k: int = 5
) -> List[Tuple[str, int]]:
    start = time.time()
    candidates = []
    for token in dictionary:
        dist = damerau_levenshtein(typo, token)
        if dist <= max_distance:
            candidates.append((token, dist))
    candidates.sort(key=lambda x: (x[1], len(x[0])))
    end = time.time()
    print(f"time taken: {end - start:.4f} sec")
    return candidates[:top_k]

if __name__ == "__main__":
    code_dict = collect_identifiers("./src")
    
    print("Constant-threshold Damerau–Levenshtein autocorrect")
    print("------------------------------------------------")
    print(f"Collected {len(code_dict)} identifiers from the codebase.")

    user_input = "display_monstsr_invntoty"
    suggestions = suggest_token(user_input, code_dict, max_distance=10, top_k=5)

    print(f"Input  : {user_input}")
    print("Suggestions (token, distance):")
    for token, dist in suggestions:
        print(f"  • {token:<20}  (d={dist})")

