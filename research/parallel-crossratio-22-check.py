"""Exact finite checks for parallel-crossratio-22.md (standard library only)."""

from collections import Counter
from math import sqrt
import sys


def check(p, b):
    B = {r for r in range(1, p) if pow(r, b, p) == 1}
    assert len(B) == b and p - 1 in B and (p - 1) % (2 * b) == 0
    inv = [0] + [pow(x, -1, p) for x in range(1, p)]
    cosets = {}
    for x in range(1, p):
        if x not in cosets:
            cosets.update((x * r % p, x) for r in B)
    shifted_inv = [(1 + inv[x]) % p for x in range(p)]

    # The symmetric product cell and its original (X,Y) definition.
    cells, fixed, original, anchored = Counter(), Counter(), Counter(), Counter()
    for x in range(1, p):
        for c in B:
            z = x * c % p
            gamma = shifted_inv[x] * shifted_inv[z] % p
            if gamma in (0, 1):
                continue
            cell = (gamma, cosets[x])
            cells[cell] += 1
            if x == z:
                fixed[cell] += 1
            else:
                u = (1 + x) * inv[(1 + z) % p] % p
                assert u not in (0, 1) and (1 - u * c) % p != 0 and u != c
                assert x == (u - 1) * inv[(1 - u * c) % p] % p
                assert gamma * ((u - 1) ** 2 * inv[u] % p) % p == (c - 1) ** 2 * inv[c] % p
                anchored[cell] += 1
        if p <= 4177:
            for product in B:
                lam = ((product - 1) * x + product) * inv[x] ** 2 % p
                if lam not in (0, 1):
                    original[(1 - lam) % p, cosets[x]] += 1
    if p <= 4177:
        assert original == cells
    assert max(fixed.values(), default=0) <= 2
    assert anchored == cells - fixed

    # Build the projected grid and count its ordered pairs in B-directions.
    P = {
        (r * (1 - s) * inv[(r * s - 1) % p] % p,
         s * (1 - r) * inv[(r * s - 1) % p] % p)
        for r in B - {1} for s in B - {1} if r * s % p != 1
    }
    assert len(P) == (b - 1) * (b - 2)
    all_directions = admissible = 0
    for u in B:
        counts = Counter((a + u * d) % p for a, d in P)
        for t, m in counts.items():
            all_directions += m * (m - 1)
            x, z = inv[t], u * inv[t] % p
            if t and (1 + x) % p and (1 + z) % p and (1 + x + z) % p:
                gamma = shifted_inv[x] * shifted_inv[z] % p
                n = cells[gamma, cosets[x]]
                assert m == n - 1 - (x != z)
                admissible += m * (m - 1)
    moment2 = sum(n * n for n in cells.values())
    moment25 = sum(n * n * sqrt(n) for n in cells.values())
    moment3 = sum(n**3 for n in cells.values())
    factorial3 = sum(n * (n - 1) * (n - 2) for n in cells.values())
    swap_terms = sum(2 * (n - fixed[c]) * (n - 2) for c, n in cells.items())
    assert factorial3 == admissible + swap_terms
    assert 0 <= all_directions - admissible <= 4 * b**3

    # Independently evaluate the original anchored overlaps on the small field.
    if p == 97:
        for a in B - {1}:
            S = {(x - a) * inv[x - 1] % p for x in B - {1, a}}
            for u in range(2, p):
                if u == a or u * a % p == 1:
                    continue
                x = (u - 1) * inv[(1 - u * a) % p] % p
                z = x * a % p
                cell = (shifted_inv[x] * shifted_inv[z] % p, cosets[x])
                assert cells[cell] == len(S & {u * s % p for s in S}) + 2

    # A direct normalized 3/2 moment of the all-anchor mean.
    D = {inv[x - 1] for x in B - {1}}
    ratios = [0] * p
    for t in D:
        differences = [(z - t) % p for z in D - {t}]
        for w in differences:
            w_inv = inv[w]
            for z in differences:
                ratios[z * w_inv % p] += 1
    assert ratios[1] == (b - 1) * (b - 2)
    assert all(ratios[u] == ratios[(1 - u) % p] == ratios[inv[u]] for u in range(2, p))
    r32 = sum((k / (b - 1)) ** 1.5 for k in ratios[2:]) / p
    print(f"{p=:6} {b=:3}  N2={moment2/b**3:.3f}  N2.5={moment25/b**3:.3f}"
          f"  N3={moment3/b**3:.3f}  J={all_directions/b**3:.3f}"
          f"  J_adm={admissible/b**3:.3f}  R3/2={r32:.3f}", flush=True)


if __name__ == "__main__":
    for prime, size in ((97, 12), (1153, 32), (4177, 72), (10193, 98)):
        check(prime, size)
    if "--larger" in sys.argv:
        check(40801, 200)
