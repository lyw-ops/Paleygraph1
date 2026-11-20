"""Round 182 cold price: exact one-step and m-step growth of the seed-linear
multiplier f -> K(S f / (2 sqrt t)) under the Round 80 per-simple weight rule.

Per-simple rule (Round 80, astra-dissipation-80.md lines 82-112): a negative
simple of dimension r has two boundary fibres A, B with r weight slots each,
pooled first absolute moment r (sum of |w| over both fibres = 2r).  The seed
is s_p C = (s_p/2)(J + J^-1); J^e shifts fibre A by -e and fibre B by +e.
The positive product has generic rank r' = (1/2) sum |w'|; transport gives a
negative simple of dimension r', keeping negative weights in their fibre,
moving positive weights to the other fibre and filling each fibre with zeros
up to r'.  Hence on count vectors x (number of slots of each (value, fibre))
each step x -> M_e x is LINEAR, and the m-step sum over the 2^m sign paths is
(M_+ + M_-)^m.  Price per simple: pi_alpha = r + alpha * (zeros)/2.
The seed-linear operator has per-line coefficient s_p/(4|sqrt t|), so

   ||L_S^m||_{pi_alpha} <= G_m(alpha) * (s_p/(4|sqrt t|))^m ,
   G_m(alpha) = sup over valid simples of pi_alpha(sum_paths child)/pi_alpha(parent).

Certified quantities (exact integers/Fractions):
  G_up = max over single slot types t of n_t/d_t   (mediant bound; valid for all
         nonnegative combinations, hence an UPPER bound for G_m), with the
         large-|v| tail handled by exact affinity in |v| (checked below);
  G_lo = max over feasible extreme rays (supports <= 3 types, constraints tight),
         a LOWER bound attained by valid weight configurations of the rule.
G is submultiplicative (children of valid simples are valid simples), which
gives the power bound G_m <= C lam^m with lam = G_m0^(1/m0).
Limit factor s_p/(4|sqrt t|) -> sqrt(2)/sqrt(N) = 0.177521... (s_p -> 2 sqrt 2,
|sqrt t| >= sqrt(N)/2).  This is a compact-model statement per simple, at each
prime, before physical O(n^-1/2) corrections.
Replay:  python3 -B research/paley-182-cold-seed-power-check.py
"""
from fractions import Fraction as F
from itertools import combinations
import math

A, B = 0, 1


def step(x, e):
    """apply M_e to a count vector x: dict {(v, fib): count} -> dict.  Values exact ints."""
    r2 = 0                       # 2 r'
    out = {}
    for (v, fb), c in x.items():
        if c == 0:
            continue
        w = v - e if fb == A else v + e
        r2 += c * abs(w)
        if w < 0:
            out[(w, fb)] = out.get((w, fb), 0) + c
        elif w > 0:
            out[(w, 1 - fb)] = out.get((w, 1 - fb), 0) + c
    nzA = sum(c for (w, fb), c in out.items() if fb == A)
    nzB = sum(c for (w, fb), c in out.items() if fb == B)
    # r2 is even for valid states (linear identity); keep r2/2 as Fraction for linearity
    out[(0, A)] = out.get((0, A), 0) + F(r2, 2) - nzA
    out[(0, B)] = out.get((0, B), 0) + F(r2, 2) - nzB
    return out


def price2(x, alpha):
    """2 * pi_alpha = (sum |v| over slots) + alpha * (number of zero slots)"""
    s = sum(c * abs(v) for (v, fb), c in x.items())
    z = x.get((0, A), 0) + x.get((0, B), 0)
    return s + alpha * z


def functional(m, alpha, V):
    """coefficients w[t] = 2 pi_alpha((M_+ + M_-)^m e_t) for all types |v|<=V (incl. zeros)."""
    types = [(v, fb) for v in range(-V, V + 1) for fb in (A, B)]
    w = {}
    for t in types:
        layer = [{t: 1}]
        for _ in range(m):
            nxt = {}
            for st in layer:
                for e in (1, -1):
                    for k, c in step(st, e).items():
                        nxt[k] = nxt.get(k, 0) + c
            layer = [nxt]        # linear: sum over paths = single summed vector
        w[t] = price2(layer[0], alpha)
    return w


def coeffs(w, alpha, V):
    """for nonzero types t, numerator n_t and denominator d_t (both for 2*pi) after
    substituting the induced zeros: zeros_F = r - NZ_F with r = sum|v|/2."""
    res = {}
    for v in range(-V, V + 1):
        if v == 0:
            continue
        for fb in (A, B):
            # one slot of type t induces |v|/2 zeros in each fibre, minus 1 in its own fibre
            zA = F(abs(v), 2) - (1 if fb == A else 0)
            zB = F(abs(v), 2) - (1 if fb == B else 0)
            n = w[(v, fb)] + zA * w[(0, A)] + zB * w[(0, B)]
            d = abs(v) + alpha * (zA + zB)
            res[(v, fb)] = (n, d, zA, zB)
    return res


def g_upper(co):
    return max(n / d for (n, d, zA, zB) in co.values())


def g_lower(co):
    """max ratio over feasible extreme rays: supports of size 1-3, zero counts >= 0."""
    items = list(co.items())
    best = F(0)
    for k in (1, 2, 3):
        for sub in combinations(items, k):
            # solve for weights lam_i >= 0 (sum = 1) making the binding constraints tight
            # enumerate which of the two zero constraints are tight: need k-1 tight ones
            for tight in ([] if k == 1 else ([[0], [1]] if k == 2 else [[0, 1]])):
                # equations: sum lam_i z_F(i) = 0 for F in tight, sum lam_i = 1
                rows = [[it[1][2 + Fi] for it in sub] for Fi in tight] + [[1] * k]
                rhs = [0] * len(tight) + [1]
                lam = solve(rows, rhs)
                if lam is None or any(l < 0 for l in lam):
                    continue
                zA = sum(l * it[1][2] for l, it in zip(lam, sub))
                zB = sum(l * it[1][3] for l, it in zip(lam, sub))
                if zA < 0 or zB < 0:
                    continue
                n = sum(l * it[1][0] for l, it in zip(lam, sub))
                d = sum(l * it[1][1] for l, it in zip(lam, sub))
                best = max(best, n / d)
            if k == 1:
                n, d, zA, zB = sub[0][1]
                if zA >= 0 and zB >= 0:
                    best = max(best, n / d)
    return best


def solve(rows, rhs):
    n = len(rows)
    M = [list(map(F, r)) + [F(b)] for r, b in zip(rows, rhs)]
    for i in range(n):
        p = next((j for j in range(i, n) if M[j][i] != 0), None)
        if p is None:
            return None
        M[i], M[p] = M[p], M[i]
        for j in range(n):
            if j != i and M[j][i] != 0:
                f = M[j][i] / M[i][i]
                M[j] = [a - f * b for a, b in zip(M[j], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]


def tail_check(m, alpha, V):
    """exact affinity of n_t, d_t in |v| for |v| > m+1: second differences vanish."""
    w = functional(m, alpha, V)
    co = coeffs(w, alpha, V)
    ok = True
    for fb in (A, B):
        for sg in (1, -1):
            vals = [co[(sg * v, fb)][0] for v in range(m + 2, V + 1)]
            ok &= all(vals[i] - 2 * vals[i + 1] + vals[i + 2] == 0 for i in range(len(vals) - 2))
    # limit ratios n/d as |v| -> infinity
    lim = max((co[(sg * V, fb)][0] - co[(sg * (V - 1), fb)][0]) /
              (co[(sg * V, fb)][1] - co[(sg * (V - 1), fb)][1])
              for fb in (A, B) for sg in (1, -1))
    return ok, lim, co


SQ = math.sqrt(2) / math.sqrt(4 * (2031 / 128 - 2 ** -17))   # limit of s_p/(4|sqrt t|)
print("limit per-line factor s_p/(4|sqrt t|) =", f"{SQ:.6f}")
print("columns: m, alpha, G_lo, G_up (incl. |v|->inf limit), G_up^(1/m), rate = G_up^(1/m)*factor")
results = {}
for alpha in (F(0), F(1, 2), F(1)):
    for m in range(1, 9):
        V = m + 6
        ok, lim, co = tail_check(m, alpha, V)
        assert ok, "affinity in |v| failed"
        gu = max(g_upper(co), lim)
        gl = g_lower(co)
        results[(alpha, m)] = (gl, gu)
        print(f"m={m} alpha={str(alpha):>3}: G_lo={float(gl):.6f} G_up={float(gu):.6f}"
              f"  G_up^(1/m)={float(gu) ** (1 / m):.6f}  rate={float(gu) ** (1 / m) * SQ:.5f}")

print("\nreference: 2*sqrt(2) =", f"{2 * math.sqrt(2):.6f}", "(leading-field growth, rate 0.50206)")
print("\nPower bounds G_m <= C lam^m via submultiplicativity (lam from m0=8):")
for alpha in (F(0), F(1, 2), F(1)):
    g8 = float(results[(alpha, 8)][1])
    lam = g8 ** (1 / 8)
    C = max(1.0, max(float(results[(alpha, r)][1]) / lam ** r for r in range(1, 8)))
    print(f"alpha={str(alpha):>3}: lam_hat={lam:.6f} (rate {lam * SQ:.5f}), C={C:.4f}")
