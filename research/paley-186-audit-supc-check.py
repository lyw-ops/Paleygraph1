#!/usr/bin/env python3
r"""Round 186 audit (session/r186-audit): independent checks of the sup C report
research/native-claude-ordinary-prime-sup-c-heavy-price-186.md.

Written by the auditor; it does not import or copy the report's scripts.  Exponent
formulas below are re-derived from the statements of Lemma M, Lemma S1, Reiher-Schoen
BSG and Stevens-de Zeeuw Theorem 4 (exponents of p; constants dropped).

Part A  EXACT (fractions.Fraction): Lemma M exponent algebra on random rational inputs;
        Proposition P exponents; Theorem A/B balances; binding configurations; the
        Round 184/180 propagation; Proposition X pair rows (including rows the report's
        table leaves implicit); the BSG-sensitivity formula; a configuration showing that
        (HC) on heights [p^{-1/15},1] alone does not close the scheme at p^{4/3}.
Part B  FLOAT LP (scipy): my own max-min LP over component configurations for
        Theorems A and B, and the worst case of the restricted-(HC) scheme.
Part C  EXACT integers at small p: weighted quadrilinear Cauchy-Schwarz,
        Lemma M incidence structure, sum m = alpha N; FLOAT: Lemma S1 for level subsets
        of every size (no sqrt p cap) for actual-type g = |f|^2.

Prints ALL AUDIT CHECKS OK at the end.
"""
import math
import random
import sys
from fractions import Fraction as F
from itertools import product

OK = True


def check(cond, msg):
    global OK
    print(("ok   " if cond else "FAIL ") + msg)
    OK = OK and bool(cond)


# =====================================================================  Part A
print("== A1. Lemma M exponent algebra (random rational exponents) ==")
rng = random.Random(186)
allgood = True
for _ in range(4000):
    a = F(rng.randint(0, 120), 120)          # log_p alpha
    n = F(rng.randint(0, 120), 120)          # log_p N
    k = F(rng.randint(0, 60), 120)           # log_p K'
    vb = n + k                               # log_p |VB| (upper bound)
    s, b = min(a, vb), max(a, vb)
    mn = min(a, vb)
    # SdZ (with the ab^2 > n^3 reduction): t N <= s^3 b^2 / h^4  =>  t <= s^3 b^2/(N h^4)
    allgood &= (3 * s + 2 * b == 2 * a + 2 * vb + mn)
    H = (a + 2 * k + mn) / 3                  # H^3 = alpha K'^2 min
    # energy: H alpha N  and  alpha^2 K'^2 N min / H^2 both equal the claimed bound
    claim = F(4, 3) * a + n + F(2, 3) * k + mn / 3
    allgood &= (H + a + n == claim) and (2 * a + 2 * k + n + mn - 2 * H == claim)
    # SdZ hypothesis: (size of smaller set) * (#lines) <= min * alpha N^2 / h at h >= H
    an = mn + a + 2 * n - H
    allgood &= an <= F(4, 3) * a + 2 * n
    # the bound is never below the trivial alpha N (sum of m)
    allgood &= claim >= a + n
check(allgood, "Lemma M: s^3 b'^2 = (alpha |VB|)^2 min; balance H^3 = alpha K'^2 min gives "
      "alpha^{4/3} N K'^{2/3} min^{1/3}; an <= alpha^{4/3} N^2 at h >= H (4000 random points)")

# the ab^2 > n^3 reduction: I <= a n <= a^{3/4} b^{1/2} n^{3/4} when a <= b, a b^2 > n^3
good = True
for _ in range(4000):
    a = F(rng.randint(0, 100), 100); b = a + F(rng.randint(0, 100), 100)
    nn = F(rng.randint(0, 300), 100)
    if a + 2 * b > 3 * nn:
        good &= (a + nn <= F(3, 4) * a + b / 2 + F(3, 4) * nn)
check(good, "reduction: a b^2 > n^3, a <= b  =>  a n <= a^{3/4} b^{1/2} n^{3/4}")

print("== A2. Proposition P from Lemma M, Lemma S1 and Reiher-Schoen (auditor's derivation) ==")


def phase_params(e, mu):
    """log_p of K (S1 at t = a/2 on a remainder of size >= M), min piece, total size 2M."""
    M = F(1, 2) - mu
    K = F(1, 2) + 2 * e - M                   # K <= C sqrt p / (a^2 M)
    bmin = M - K / 2                          # |B| >= (1/2) K^{-1/2} M
    return K, bmin, M


def pair_formI(e_s, mu_s, A_g, e_g, c=4, sigma=F(1, 2)):
    """log_p of a_s a_g E(X_s; D)^{1/2}: sum over pieces of (|D|^{5/3} |B| K'^{2/3})^{1/2}."""
    K, bmin, M = phase_params(e_s, mu_s)
    bmin = M - sigma * K
    return F(5, 6) * A_g + F(c, 3) * K + M - bmin / 2 - e_s - e_g


def pair_formII(e_s, mu_s, A_g, e_g, c=4):
    K, bmin, M = phase_params(e_s, mu_s)
    return F(2, 3) * A_g + F(c, 2) * K + M - bmin / 3 - e_s - e_g


good = True
for _ in range(2000):
    es, eg = F(rng.randint(0, 84), 1008), F(rng.randint(0, 84), 1008)
    ms = F(rng.randint(-int(es * 1008), 30), 1008)
    mg = F(rng.randint(-int(eg * 1008), 30), 1008)
    A = F(1, 2) - mg
    I = pair_formI(es, ms, A, eg)
    II = pair_formII(es, ms, A, eg)
    good &= I == F(2, 3) + F(13, 6) * es + F(13, 12) * ms - eg - F(5, 6) * mg
    good &= II == F(2, 3) + F(10, 3) * es + F(3, 2) * ms - eg - F(2, 3) * mg
    good &= F(5, 6) * A + F(1, 4) + F(19, 6) * es + F(13, 12) * ms - es - eg == I
check(good, "Prop. P: E(X_s;D)^{1/2} <~ p^{5A/6 + 1/4 + 19e_s/6 + 13mu_s/12}; pair excess "
      "c = 13e_s/6 + 13mu_s/12 - e_g - 5mu_g/6 (form I) and 10e_s/3 + 3mu_s/2 - e_g - 2mu_g/3 (form II)")
check(phase_params(F(1, 37), F(-1, 37))[0] == F(1, 37), "whole level set at height p^{-e}: K <= p^e (doubling claim)")


def sdz(es, mus, roles=("pt", "ln", "pt", "ln")):
    th = {"pt": F(5, 8), "ln": F(3, 4)}
    return sum(-e + th[r] * (F(1, 2) - m) for e, m, r in zip(es, mus, roles))


check(sdz([0] * 4, [0] * 4) == F(11, 8), "SdZ price at height 1, size sqrt p: 11/8")

print("== A3. Theorem B / A balances and binding configurations ==")
dB = F(1, 24) / (1 + F(22, 15))
check(dB == F(5, 296), "Theorem B: Gamma (1 + 22/15) = 1/24  =>  Gamma = 5/296")
check(F(5, 8) * F(1, 37) == F(5, 296), "leftover stop delta = 1/37 gains (5/8) delta = 5/296")
check(F(1, 4) * F(1, 12) > F(5, 296), "a slot with e > 1/12 gains > 1/48 > 5/296")
check(F(4, 3) * (F(1, 2) + F(1, 12)) + 2 * (F(1, 2) + F(1, 12)) < 2,
      "Lemma M hypothesis alpha^{4/3} N^2 <= p^{35/18} when all heights e <= 1/12")
check(F(19, 14) < F(11, 8) - F(5, 296), "Step L p^{19/14} below")
for es in ([0, 0, F(1, 37), F(1, 37)], [F(1, 74)] * 4):
    mus = [-e for e in es]
    S = sdz(es, mus)
    P12 = min(pair_formI(es[0], mus[0], F(1, 2) - mus[1], es[1]), pair_formI(es[1], mus[1], F(1, 2) - mus[0], es[0]),
              pair_formII(es[0], mus[0], F(1, 2) - mus[1], es[1]), pair_formII(es[1], mus[1], F(1, 2) - mus[0], es[0]))
    P34 = min(pair_formI(es[2], mus[2], F(1, 2) - mus[3], es[3]), pair_formI(es[3], mus[3], F(1, 2) - mus[2], es[2]),
              pair_formII(es[2], mus[2], F(1, 2) - mus[3], es[3]), pair_formII(es[3], mus[3], F(1, 2) - mus[2], es[2]))
    check(S == F(11, 8) - F(5, 296) and P12 + P34 == F(11, 8) - F(5, 296),
          f"binding {tuple(str(x) for x in es)}: SdZ = best pair price = 11/8 - 5/296 (form II not cheaper)")
dA = F(1, 24) / (1 + F(24, 5))
check(dA == F(5, 696) and F(5, 8) / 87 == F(5, 696), "Theorem A: Gamma = 5/696, delta = 1/87")
# Phase 1 (capped): K = a^{-2}, pieces >= a sqrt p, component <= p^{1/2+e}
P1 = lambda es, Ag, eg: F(5, 6) * Ag + F(4, 3) * 2 * es + (F(1, 2) + es) - (F(1, 2) - es) / 2 - es - eg
check(P1(F(1, 87), F(1, 2) + F(1, 87), F(1, 87)) == F(2, 3) + 3 * F(1, 87), "Phase-1 pair excess at equal heights 3e")

print("== A4. propagation (Round 184 Prop. 1(i)/(iii), Round 180 chain) ==")
for d, cov in ((F(5, 296), F(2125, 1184)), (F(5, 696), F(625, 348)), (F(1, 664), F(1193, 664))):
    e = 2 + (F(11, 8) - d) / 2 + 0          # sum W^{3/2} <= M1 (sup C M1^2)^{1/2}
    check(e == F(43, 16) - d / 2 and F(9, 8) + e / 4 == cov == F(115, 64) - d / 8,
          f"delta_C = {d}: E(mu) = 43/16 - delta/2, covariance {cov}")
    check(2 * F(34, 23) < 2 + F(11, 8) - d and 2 * F(31, 21) < 2 + F(11, 8) - d, "  X^2 below sup C M_1^2")
check(F(2125, 1184) > F(43, 24), "2125/1184 still above the scheme floor 43/24")

print("== A5. Proposition X rows (eps = 1/42, delta = 1/126, capped extraction) ==")
eps, de = F(1, 42), F(1, 126)
T = F(31, 42)
rows = {
    "light-light Young": F(3, 4) - eps / 2,
    "P1-P1 (min e structured)": F(2, 3) + 3 * eps,
    "P1 structured vs leftover (row not in report table)": P1(eps, F(1, 2) - de, 0),
    "P2 structured vs any (mu_g >= -e_g)": F(2, 3) + F(13, 6) * eps + F(13, 12) * de,
    "LO-LO trivial": F(3, 2) * (F(1, 2) - de),
    "LO-light ||c||_inf ||c||_1, ||c||_inf <= ||v||_2||v'||_2": (F(1, 2) - de + F(1, 2) - eps + 2 * (F(1, 2) - de) + 1) / 4,
    "P1 structured vs light layer cake": F(2, 3) - eps / 6 + F(19, 6) * eps,
    "P2 structured vs light layer cake": F(2, 3) - eps / 6 + F(13, 6) * eps + F(13, 12) * de,
    "light below p^-1/4 vs piece, ||c||_2 <= |X| |L_s|^{1/2}": F(5, 8),
}
for k, v in rows.items():
    check(v <= T, f"{k}: {v} <= 31/42")
check(F(4, 3) * (F(3, 4)) + 2 * F(1, 2) <= 2, "light layer cake: Lemma M hypothesis for s >= p^{-1/4} with N <= sqrt p")
check(2 * T == F(31, 21) and F(31, 21) < F(34, 23), "E^x(h) = p^{31/21} < p^{34/23}")

print("== A6. BSG sensitivity (doubling K^c, size loss K^{-sigma}) ==")


def deltaC(c, sigma=F(1, 2)):
    exc = F(c) / 3 + F(sigma) / 2 - F(2, 3) if isinstance(c, F) else c / 3 + float(sigma) / 2 - 2 / 3
    return F(1, 24) / (1 + F(8, 5) * exc) if isinstance(exc, F) else (1 / 24) / (1 + 1.6 * exc)


check(deltaC(F(4)) == F(5, 296) and deltaC(F(3)) == F(5, 232) and deltaC(F(8, 3)) == F(15, 632),
      "delta_C(c) reproduces 5/296 (c=4), 5/232 (c=3), 15/632 (c=8/3)")
cRS = math.log(4) / math.log(27 / 16)
dRS = deltaC(cRS)
print(f"   c_RS = log4/log(27/16) = {cRS:.6f}: delta_C = {dRS:.6f} vs 15/632 = {15/632:.6f}")
check(dRS > 15 / 632, "CORRECTION: at the Reiher-Schoen lower exponent 2.649 (< 8/3) the ceiling is ~0.02386, "
      "slightly above 15/632; 15/632 is the value at c = 8/3")

print("== A7. (HC) on heights [p^{-1/15},1] only: a configuration it does not close ==")
# slot 1 (point): whole level set at height p^{-1/14} (outside the (HC) range);
# slot 2 (line): phase component at height 1 with mu = 1/60; slots 3,4: whole sets at height 1.
e1, m1, e2, m2 = F(1, 14), -F(1, 14), F(0), F(1, 60)
S = sdz([e1, e2, 0, 0], [m1, m2, 0, 0])
opts12 = {
    "form I (2->1)": pair_formI(e2, m2, F(1, 2) - m1, e1),
    "form II (2->1)": pair_formII(e2, m2, F(1, 2) - m1, e1),
    "form I (1->2)": pair_formI(e1, m1, F(1, 2) - m2, e2),
    "form II (1->2)": pair_formII(e1, m1, F(1, 2) - m2, e2),
    "trivial": ((F(1, 2) - m1) + (F(1, 2) - m2) + min(F(1, 2) - m1, F(1, 2) - m2)) / 2 - e1 - e2,
}
best12 = min(opts12.values())
best34 = F(2, 3)          # (HC) at height 1 (also Lemma M with u = 0)
for k, v in opts12.items():
    print(f"   pair (1,2) {k}: excess {v - F(2, 3)}")
print(f"   SdZ exponent 11/8 - {F(11, 8) - S};   best pair route 4/3 + {best12 + best34 - F(4, 3)}")
check(min(S, best12 + best34) > F(4, 3),
      "CORRECTION: min(SdZ, pairs) = 4/3 + 1/840 > 4/3 at (e1,mu1;e2,mu2) = (1/14,-1/14; 0,1/60): "
      "(HC) must cover every height down to c p^{-1/6} (or at least pairs with one slot outside [p^{-1/15},1])")

# =====================================================================  Part B
print("== B. float LP (scipy): auditor's max-min over component configurations ==")
try:
    import numpy as np
    from scipy.optimize import linprog
    have_lp = True
except Exception as exc:  # pragma: no cover
    have_lp = False
    print("   scipy not available:", exc)

if have_lp:
    TH = [5 / 8, 3 / 4, 5 / 8, 3 / 4]

    def lp_maxmin(kinds, delta, emax):
        """variables x = (e1,m1,...,e4,m4,t). kinds[i] in {'P1','P2','U'} (U = uncapped phase).
        maximize t s.t. t <= SdZ, t <= 4/3 + exc12_i + exc34_j for all option pairs."""
        nv = 9
        A, b = [], []

        def lin(coefs, const):  # returns (row over x, const) for a linear form
            return np.array(coefs, float), float(const)

        def size(i):  # log size of component i as (coef row, const)
            r = np.zeros(nv)
            if kinds[i] == "P1":
                r[2 * i] = 1.0; return r, 0.5      # <= p^{1/2+e}
            r[2 * i + 1] = -1.0; return r, 0.5      # 2M = p^{1/2-mu}

        def excess_opts(s, g):
            out = []
            Ar, Ac = size(g)
            for form in ("I", "II"):
                r = np.zeros(nv); c = -2 / 3
                es, ms = 2 * s, 2 * s + 1
                if kinds[s] == "P1":
                    K = {es: 2.0}; Kc = 0.0; M = {es: 1.0}; Mc = 0.5; bm = {es: -1.0}; bmc = 0.5
                else:
                    K = {es: 2.0, ms: 1.0}; Kc = 0.0; M = {ms: -1.0}; Mc = 0.5
                    bm = {ms: -1.5, es: -1.0}; bmc = 0.5
                wA, wK, wb = (5 / 6, 4 / 3, -1 / 2) if form == "I" else (2 / 3, 2.0, -1 / 3)
                r += wA * Ar; c += wA * Ac
                for kk, v in K.items(): r[kk] += wK * v
                c += wK * Kc
                for kk, v in M.items(): r[kk] += v
                c += Mc
                for kk, v in bm.items(): r[kk] += wb * v
                c += wb * bmc
                r[es] -= 1.0; r[2 * g] -= 1.0
                out.append((r, c))
            return out

        def pair_opts(i, j):
            return excess_opts(i, j) + excess_opts(j, i)

        sd = np.zeros(nv); sdc = 0.0
        for i in range(4):
            r, c = size(i)
            sd += TH[i] * r; sdc += TH[i] * c; sd[2 * i] -= 1.0
        # t - SdZ <= 0
        row = -sd.copy(); row[8] = 1.0; A.append(row); b.append(sdc)
        for (r1, c1) in pair_opts(0, 1):
            for (r2, c2) in pair_opts(2, 3):
                row = -(r1 + r2); row[8] = 1.0; A.append(row); b.append(4 / 3 + c1 + c2)
        bounds = []
        for i in range(4):
            bounds.append((0, emax))
            bounds.append((None, None) if kinds[i] != "P1" else (0, 0))
        bounds.append((None, None))
        for i in range(4):
            if kinds[i] == "P1":
                continue
            row = np.zeros(nv); row[2 * i + 1] = 1.0; A.append(row); b.append(delta)       # mu <= delta
            lo = 0.0 if kinds[i] == "P2" else None
            row = np.zeros(nv); row[2 * i + 1] = -1.0
            if kinds[i] == "P2":
                A.append(row); b.append(0.0)                                                # mu >= 0
            else:
                row[2 * i] = -1.0; A.append(row); b.append(0.0)                             # mu >= -e
        cobj = np.zeros(nv); cobj[8] = -1.0
        res = linprog(cobj, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method="highs")
        return -res.fun, res.x

    best = -1
    for kinds in product(("U",), repeat=4):
        v, x = lp_maxmin(kinds, 1 / 37, 1 / 12)
        best = max(best, v)
    print(f"   Theorem B LP (uncapped phases, e <= 1/12, delta = 1/37): 11/8 - {11/8 - best:.7f}")
    check(abs((11 / 8 - best) - 5 / 296) < 1e-9, "LP agrees with 5/296")
    best = -1
    for kinds in product(("P1", "P2"), repeat=4):
        v, x = lp_maxmin(kinds, 1 / 87, 1 / 7)
        best = max(best, v)
    print(f"   Theorem A LP (capped phases P1/P2, e <= 1/7, delta = 1/87): 11/8 - {11/8 - best:.7f}")
    check(abs((11 / 8 - best) - 5 / 696) < 1e-9, "LP agrees with 5/696")
    # Note: e <= 1/7 for Theorem A includes heights where Lemma M's hypothesis fails; the LP
    # value equals the hand value, so those heights are not binding (SdZ alone covers e > 1/12).

# =====================================================================  Part C
print("== C. exact replays at small p ==")


def legendre_sq(p):
    return {x * x % p for x in range(1, p)}


for p in (13, 17, 29):
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    R = random.Random(p)
    pts = list(range(2, p))
    # C1 weighted quadrilinear Cauchy-Schwarz (integer weights)
    f = [{x: R.randint(0, 3) for x in pts} for _ in range(4)]

    def mrow(fa, fb):
        out = [0] * p
        for Y in pts:
            for D in pts:
                if Y != D:
                    out[(Y - D) * inv[(1 - D) % p] % p] += fa[Y] * fb[D]
        return out

    def cvec(fa, fb):  # c_{v_a,v_b}(k) = sum_z v_b(z) v_a(k z), v(z) = f(1-z)
        out = [0] * p
        for k in range(1, p):
            out[k] = sum(fb[(1 - z) % p] * fa[(1 - k * z) % p] for z in range(1, p)
                         if (1 - z) % p in fb and (1 - k * z) % p in fa)
        return out
    m12, m34 = mrow(f[0], f[1]), mrow(f[2], f[3])
    c12, c34 = cvec(f[0], f[1]), cvec(f[2], f[3])
    E12, E34 = sum(x * x for x in c12), sum(x * x for x in c34)
    good = sum(x * x for x in m12) <= E12 and sum(x * x for x in m34) <= E34
    for lam in range(2, p):
        brute = 0
        for Y1, D1, Y3, D3 in product(pts, repeat=4):
            if Y1 != D1 and Y3 != D3 and ((Y1 - D1) * (1 - D3) - lam * (Y3 - D3) * (1 - D1)) % p == 0:
                brute += f[0][Y1] * f[1][D1] * f[2][Y3] * f[3][D3]
        viarow = sum(m12[lam * r % p] * m34[r] for r in range(1, p))
        good &= (brute == viarow) and brute * brute <= E12 * E34
    check(good, f"p={p}: C#[f1..f4] = sum_r m12(lam r) m34(r) and C#^2 <= ||c12||^2 ||c34||^2, all lam, integer weights")
    # C2 Lemma M structure with A != B, V = B^{-1}
    A = set(R.sample(pts, R.randint(3, p // 2))); B = set(R.sample(pts, R.randint(3, p // 2)))
    V = {inv[x] for x in B}; VB = {v * y % p for v in V for y in B}
    m = [0] * p
    for x in A:
        for y in B:
            m[(1 - y) * inv[(1 - x) % p] % p] += 1
    good = sum(m) == len(A) * len(B) and m[0] == 0
    lines = {(v * u % p, v * (1 - u) % p) for u in range(1, p) for v in V}
    good &= len(lines) == (p - 1) * len(V) and all(s != 0 for s, _ in lines)
    for h in range(1, max(m) + 1):
        Th = [u for u in range(1, p) if m[u] >= h]
        Ls = {(v * u % p, v * (1 - u) % p) for u in Th for v in V}
        I = sum(1 for (s, c) in Ls for x in A if (s * x + c) % p in VB)
        good &= I >= h * len(Th) * len(V)
    sA, sB = min(len(A), len(VB)), max(len(A), len(VB))
    good &= sA ** 3 * sB ** 2 == (len(A) * len(VB)) ** 2 * min(len(A), len(VB))
    check(good, f"p={p}: Lemma M lines distinct/nonhorizontal, sum m = alpha N, I >= h|T_h||V| for every h")

# C3 Lemma S1 for level subsets of every size (float; actual-type g)
import cmath
good = True
worst = 1e9
for p in (101, 197, 389):
    n = (p - 1) // 2
    # primitive root
    for gr in range(2, p):
        if all(pow(gr, (p - 1) // q, p) != 1 for q in {2} | {q for q in range(3, p) if (p - 1) % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))}):
            break
    Qlog = {pow(gr, 2 * j, p): j for j in range(n)}
    R = random.Random(p)
    for trial in range(6):
        S = R.sample(range(n), R.randint(2, max(3, int(1.5 * math.sqrt(p)))))
        nu = 1 / len(S)
        g = {}
        for x, j in Qlog.items():
            fx = sum(cmath.exp(2j * math.pi * j * k / n) for k in S) * nu
            g[x] = abs(fx) ** 2
        for t in (0.9, 0.5, 0.25, 0.1):
            W0 = [x for x in g if x != 1 and g[x] >= t]
            for W in (W0, R.sample(W0, len(W0) // 2) if len(W0) > 3 else W0):
                if len(W) < 2:
                    continue
                Ws = set(W); cnt = {}
                for x in W:
                    for y in W:
                        cnt[x * y % p] = cnt.get(x * y % p, 0) + 1
                E = sum(v * v for v in cnt.values())
                lhs = t * t * len(W) ** 4 / (n * nu)
                worst = min(worst, E / lhs)
                good &= E >= lhs * (1 - 1e-9)
check(good, f"Lemma S1 E^x(W) >= t^2|W|^4/(n max nu) for whole and half level sets, no size cap "
      f"(p = 101, 197, 389; min ratio {worst:.3f})")

print("ALL AUDIT CHECKS OK" if OK else "SOME AUDIT CHECK FAILED")
sys.exit(0 if OK else 1)
