#!/usr/bin/env python3
"""Round 183 cold price: independent brute force of the Round 80 per-simple rule for the
FULL seed multiplier Phi_t'(S) = (s/(2 sqrt t)) sum_k ghat_k J^k (k odd), extending
research/paley-182-audit-cold-check.py Part 2 from J^{+-1} to J^k, |k| <= 5.

Independent of research/paley-183-cold-seed-taylor-power.py: explicit simples (two fibres of
weights), explicit children per path, no count-vector linearity, no adjoint, no mediant bound.

EXACT part (integers and Fractions):
  * every parent configuration of dimension r = 2..RMAX with sum|w| = 2r (audit enumeration);
  * child under J^k: fibre A shifted by -k, fibre B by +k, negative weights stay, positive
    weights change fibre, refill with zeros to r' = sum|w'|/2.  Refill >= 0 is CHECKED for
    k in {+-1, +-3, +-5, +-7} and all children up to depth MMAX (a stopped path is counted);
  * weighted m-step path sums  sum_paths prod(gamma_k) pi_alpha(child)/pi_alpha(parent), with
    gamma_k = |ghat_k(beta0)| from the exact series (beta0 = 256/2031), compared with the G_up
    values printed by the adjoint/mediant script (which use slightly larger uniform gamma_k);
  * the lemma "|k|=1: refill in the destination fibre of the shift is exactly zero" and
    "|k|>=3: r' >= r(|k|-1)" on every enumerated parent.
FLOATING part ([float], evidence only): numpy FFT of g_beta(th) = cos th (1+beta cos^2 th)^(-1/2)
  and of (1+beta cos^2 th)^(-3/2) at beta0, against the exact series and the sign-pattern
  identity sum_k |b_k| = 1.

Replay:  .venv/bin/python -B research/paley-183-cold-seed-taylor-bruteforce.py
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb
import time

T0 = time.time()
BETA0 = F(256, 2031)
RMAX = 4
MMAX = 3


def ghat(k, beta, L=40):
    k = abs(k)
    j = (k + 1) // 2
    return sum((-1) ** l * F(comb(2 * l, l), 4 ** l) * beta ** l * F(comb(2 * l + 1, l + j), 2 ** (2 * l + 1))
               for l in range((k - 1) // 2, L + 1))


GAM = {k: abs(ghat(k, BETA0)) for k in (1, 3, 5)}
GAM.update({-k: v for k, v in list(GAM.items())})
KS = sorted(GAM)


def configs(r):
    vals = range(-2 * r, 2 * r + 1)
    fib = {}
    for ms in combinations_with_replacement(vals, r):
        s = sum(abs(w) for w in ms)
        if s <= 2 * r:
            fib.setdefault(s, []).append(ms)
    for s, L1 in fib.items():
        for f1 in L1:
            for f2 in fib.get(2 * r - s, []):
                yield f1, f2


def to_state(f1, f2):
    return (frozenset(Counter(f1).items()), frozenset(Counter(f2).items()))


def rank(st):
    return sum(c for _, c in st[0])


def zeros(st):
    return dict(st[0]).get(0, 0) + dict(st[1]).get(0, 0)


def child(st, k):
    """explicit Round 80 rule for J^k; returns (child_state, refill_ok, info)"""
    A, B = dict(st[0]), dict(st[1])
    nA, nB = Counter(), Counter()
    tot = 0
    for w, c in A.items():
        x = w - k
        tot += c * abs(x)
        if x < 0:
            nA[x] += c
        elif x > 0:
            nB[x] += c
    for w, c in B.items():
        x = w + k
        tot += c * abs(x)
        if x < 0:
            nB[x] += c
        elif x > 0:
            nA[x] += c
    assert tot % 2 == 0
    r2 = tot // 2
    fa, fb = r2 - sum(nA.values()), r2 - sum(nB.values())
    if fa < 0 or fb < 0:
        return None, (fa, fb)
    if fa:
        nA[0] += fa
    if fb:
        nB[0] += fb
    return (frozenset(nA.items()), frozenset(nB.items())), (fa, fb)


def pi2(st, alpha):            # 2 pi_alpha = 2r + alpha Z
    return 2 * rank(st) + alpha * zeros(st)


MEMO = {}


def child_m(st, k):
    key = (st, k)
    if key not in MEMO:
        MEMO[key] = child(st, k)
    return MEMO[key]


ALPHAS = [F(0), F(1, 2), F(1)]
best = {(al, m): (F(0), None) for al in ALPHAS for m in range(1, MMAX + 1)}
best_lin = {(al, m): F(0) for al in ALPHAS for m in range(1, MMAX + 1)}
total = stopped = 0
lemma_k1 = lemma_k3 = True
for r in range(2, RMAX + 1):
    for f1, f2 in configs(r):
        total += 1
        st0 = to_state(f1, f2)
        # lemma checks on the parent
        for k in (1, -1):
            ch, (fa, fb) = child(st0, k)
            dest_fill = fa if k == 1 else fb       # J (k=+1): fibre A' gets exactly r' nonzero slots
            lemma_k1 &= (ch is not None and dest_fill == 0)
        for k in (3, -3, 5, -5, 7, -7):
            ch, _ = child(st0, k)
            lemma_k3 &= (ch is not None and rank(ch) >= r * (abs(k) - 1))
        layer = [(st0, F(1))]
        lin = [(st0, F(1))]
        ok = True
        for m in range(1, MMAX + 1):
            nxt = Counter()
            for st, wgt in layer:
                for k in KS:
                    ch, _ = child_m(st, k)
                    if ch is None:
                        ok = False
                        break
                    nxt[ch] += wgt * GAM[k]
                if not ok:
                    break
            if not ok:
                stopped += 1
                break
            layer = list(nxt.items())
            nl = Counter()
            for st, wgt in lin:
                for k in (1, -1):
                    ch, _ = child_m(st, k)
                    nl[ch] += wgt
            lin = list(nl.items())
            for al in ALPHAS:
                p0 = pi2(st0, al)
                val = sum(w * pi2(st, al) for st, w in layer) / p0
                if val > best[(al, m)][0]:
                    best[(al, m)] = (val, (f1, f2))
                vl = sum(w * pi2(st, al) for st, w in lin) / p0
                best_lin[(al, m)] = max(best_lin[(al, m)], vl)
print(f"Round 80 rule with J^k, |k|<=5, weights |ghat_k(beta0)|: {total} parents r=2..{RMAX}, "
      f"depth {MMAX}; {stopped} stopped (negative refill)")
print(f"lemma |k|=1 (destination fibre refill exactly 0) on all parents: {lemma_k1}")
print(f"lemma |k|>=3 (r' >= r(|k|-1), refill >= 0) for |k| in 3,5,7 on all parents: {lemma_k3}")
for k in (1, 3, 5):
    print(f"gamma_{k} = |ghat_{k}(beta0)| = {float(GAM[k]):.12e}")
# exact sup G_m (uniform gamma_k >= |ghat_k(beta)|) printed outward (6 dp) by
# paley-183-cold-seed-taylor-power.py, section 2b; finite-r maxima here must not exceed them
GUP_PRINTED = {
    (F(0), 1): "1.970484", (F(0), 2): "2.940449", (F(0), 3): "4.374161",
    (F(1, 2), 1): "1.646972", (F(1, 2), 2): "2.455376", (F(1, 2), 3): "3.575284",
    (F(1), 1): "1.507429", (F(1), 2): "2.212839", (F(1), 3): "3.175845",
}
for al in ALPHAS:
    for m in range(1, MMAX + 1):
        v, cfg = best[(al, m)]
        g = GUP_PRINTED[(al, m)]
        cmp = f" <= G {g}: {v <= F(g)}"
        assert v <= F(g)
        print(f"  alpha={str(al):>3} m={m}: max weighted path ratio {float(v):.6f}{cmp}  "
              f"(linear seed, coefficient 1/2 each: {float(best_lin[(al, m)] / 2 ** m):.6f})  argmax {cfg}")
print(f"[exact part {time.time() - T0:.1f}s]")

# ----------------------------------------------------------------- floating cross-checks
try:
    import numpy as np
    b = float(BETA0)
    n = 4096
    th = 2 * np.pi * np.arange(n) / n
    g = np.cos(th) / np.sqrt(1 + b * np.cos(th) ** 2)
    G = np.fft.fft(g) / n
    print("[float] FFT ghat_k(beta0) vs exact series:")
    for k in (1, 3, 5, 7):
        print(f"[float]   k={k}: fft {G[k].real:+.15e}  exact {float(ghat(k, BETA0)):+.15e}")
    h2 = (1 + b * np.cos(th) ** 2) ** -1.5
    Hc = np.fft.fft(h2) / n
    print(f"[float] sum_k |b_k| for (1+beta0 cos^2)^(-3/2): {np.abs(Hc).sum():.15f} (sign pattern => 1)")
    print(f"[float] signs of b_(2i), i=0..4: {[int(np.sign(Hc[2 * i].real)) for i in range(5)]}")
    print(f"[float] sum_k |ghat_k| = {np.abs(G).sum():.15f}; 1/sqrt(1+beta0) = {1 / np.sqrt(1 + b):.15f}")
    # pointwise: Phi'(S)/(S/(2 sqrt t)) = (1+beta cos^2)^(-1/2) in [ (1+beta)^(-1/2), 1 ]
except ImportError:
    print("[float] numpy unavailable; floating cross-checks skipped")
print("BRUTE FORCE CHECKS OK")
