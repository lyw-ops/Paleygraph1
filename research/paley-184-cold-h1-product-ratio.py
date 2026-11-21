#!/usr/bin/env python3
"""Round 184 cold call `cold-prime-h1-product-rule`: exact per-simple dimension-price ratios.

Written by the Round 184 native research session (own implementation; it does not import or
copy the Round 183 scripts).  Every printed bound is EXACT (python integers / Fractions) or an
OUTWARD interval (python-flint arb).  No floating-point number enters a certified statement.

Model (compact model, per simple; hypotheses (b4), (b-Jk), (b-T) of the report):
  * a negative simple F of dimension r = two fibres A, B with r integer weight slots each,
    sum of |w| over both fibres = 2r;
  * a product F (x) G has, at each fibre, the r*d pairwise sums w + x (Round 126 "fibre weights
    add under convolution"); its generic rank is r' = (1/2) sum |w + x| (Round 80 equality form);
  * transport K keeps negative weights in their fibre, sends positive weights to the other fibre,
    and refills each fibre with zeros up to r' (Round 80).
  * line J^k: fibre weights (-k | +k), dimension 1.
  * h_1 = 2 sqrt t sum_{k even != 0} b'_k(beta) K(J^k); K(J^k) (k>0) has A = (-k, k, 0^(k-2)),
    B = 0^k; for k<0 the fibres are exchanged.  Phi_t''(S) = (1/(2 sqrt t)) sum_i bhat_2i J^2i.
    Hence Phi_t''(S) h_1 = sum_{i,k} bhat_2i(beta) b'_k(beta) J^2i K(J^k): the factors 2 sqrt t
    cancel exactly.

Sections
  0. constants (outward)                       3. validity (refill >= 0) of every term, exact
  1. Fourier coefficients, uniform on Q          4. exact m-step growth: seed, h_1, joint
  2. one-step ratio = d + mu/2 (closed form)     5. kappa*_A, H, budgets and allowances
Replay:  .venv/bin/python -B research/paley-184-cold-h1-product-ratio.py      (about 1-2 min)
"""
from fractions import Fraction as Fr
from math import comb
import sys
import time

import flint
from flint import arb

flint.ctx.prec = 200
T0 = time.time()


def fr_hi(x):
    """Fraction >= every point of the arb ball x."""
    m, e = x.mid().man_exp()
    rm, re = x.rad().man_exp()
    mid = Fr(int(m)) * (Fr(2) ** int(e))
    rad = Fr(int(rm)) * (Fr(2) ** int(re))
    return mid + rad


def fr_lo(x):
    m, e = x.mid().man_exp()
    rm, re = x.rad().man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e)) - Fr(int(rm)) * (Fr(2) ** int(re))


def up(q, d=6):
    """decimal string >= q"""
    s = 10 ** d
    v = -((-q.numerator * s) // q.denominator)
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v // s}.{v % s:0{d}d}"


def dn(q, d=6):
    s = 10 ** d
    v = (q.numerator * s) // q.denominator
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v // s}.{v % s:0{d}d}"


def br(lo, hi, d=6):
    return f"[{dn(lo, d)}, {up(hi, d)}]"


# ---------------------------------------------------------------- 0. constants
a = Fr(2031, 128)
h17 = Fr(1, 2 ** 17)
Nq = 4 * (a - h17)                       # 2|sqrt t| >= sqrt N on Q
s2_up = 8 + Fr(8, 10 ** 6 - 1)           # s_p^2 = 8 + 8/(p-1), p >= 10^6
beta0 = Fr(256, 2031)                    # = 8/(4a)
t_abs_lo = a - h17                       # |t| >= Re t >= a - 2^-17
dt = Fr(3, 2) * h17                      # |t - a| <= sqrt2 2^-17 <= 1.5 2^-17
delta = (s2_up - 8) / (4 * t_abs_lo) + 2 * dt / (t_abs_lo * a)
bb = beta0 + delta                       # |beta| <= bb on Q x {p >= 10^6}
sqrtN = arb(Nq.numerator) / arb(Nq.denominator)
sqrtN = sqrtN.sqrt()
varpi = (arb(s2_up.numerator) / arb(s2_up.denominator) / (arb(Nq.numerator) / arb(Nq.denominator))).sqrt()
VARPI = fr_hi(varpi)                     # sup |s_p / (2 sqrt t)| = s_up / sqrt N
SQRTN_LO = fr_lo(sqrtN)
INV_SQRTN = fr_hi(1 / sqrtN)
tmax = (arb((a + dt).numerator) / arb((a + dt).denominator))
SQRT_T_UP = fr_hi(tmax.sqrt())           # |sqrt t| <= sqrt(|t|) <= sqrt(a + 1.5 2^-17)
s_up = fr_hi((arb(s2_up.numerator) / arb(s2_up.denominator)).sqrt())

print("== 0. constants (exact rationals / outward arb) ==")
print(f"N = 4(2031/128 - 2^-17); sqrt N >= {dn(SQRTN_LO, 9)};  1/sqrt N <= {up(INV_SQRTN, 9)}")
print(f"varpi = s_up/sqrt N <= {up(VARPI, 9)};  s_p <= {up(s_up, 9)} (p >= 10^6)")
print(f"beta0 = 256/2031; |beta - beta0| <= delta = {up(delta, 12)};  |sqrt t| <= {up(SQRT_T_UP, 9)}")

# ---------------------------------------------------------------- 1. Fourier coefficients
L = 40


def binom_gen(alpha, l):
    """binom(alpha, l) for rational alpha"""
    r = Fr(1)
    for j in range(l):
        r = r * (alpha - j) / (j + 1)
    return r


B_HALF = [binom_gen(Fr(1, 2), l) for l in range(L + 1)]
B_M32 = [binom_gen(Fr(-3, 2), l) for l in range(L + 1)]
C_L = [Fr(comb(2 * l, l), 4 ** l) for l in range(L + 1)]


def coef_series(kind, idx):
    """returns (value at beta0 as exact partial sum, truncation tail bound, delta-derivative bound)
    kind 'bp': b'_{2i}, idx=i; 'bh': bhat_{2i}, idx=i; 'g': ghat_k, idx=k odd."""
    val = Fr(0)
    der = Fr(0)
    if kind in ("bp", "bh"):
        i = abs(idx)
        A = B_HALF if kind == "bp" else B_M32
        for l in range(i, L + 1):
            w = Fr(comb(2 * l, l + i), 4 ** l)
            val += A[l] * beta0 ** l * w
            der += l * abs(A[l]) * bb ** max(l - 1, 0) * w
    else:
        k = abs(idx)
        for l in range((k - 1) // 2, L + 1):
            w = Fr(comb(2 * l + 1, l + (k + 1) // 2), 2 ** (2 * l + 1))
            val += (-1) ** l * C_L[l] * beta0 ** l * w
            der += l * C_L[l] * bb ** max(l - 1, 0) * w
    # tails: |coefficient_l| <= 2l+1 in all three cases, weights <= 1
    tail_v = sum(Fr(2 * l + 1) * bb ** l for l in range(L + 1, L + 60)) + Fr(1, 10 ** 40)
    tail_d = sum(Fr(l * (2 * l + 1)) * bb ** (l - 1) for l in range(L + 1, L + 60)) + Fr(1, 10 ** 40)
    return val, tail_v, der + tail_d


def coef_bounds(kind, idx):
    """(lo at beta0, hi at beta0, uniform upper bound of |.| on Q)"""
    val, tv, dd = coef_series(kind, idx)
    lo, hi = val - tv, val + tv
    uni = max(abs(lo), abs(hi)) + delta * dd
    return lo, hi, uni


def tail_geo(i0, weight):
    """sum_{|i| >= i0} weight(i) * sum_{l>=|i|} (2l+1) bb^l  (both signs of i)"""
    s = Fr(0)
    for i in range(i0, i0 + 80):
        s += 2 * weight(i) * sum(Fr(2 * l + 1) * bb ** l for l in range(i, i + 120))
    return s + Fr(1, 10 ** 30)


IMAX = 3   # J^{2i}, |2i| <= 6 kept exactly in the operator
KMAX = 3   # K(J^{2j}), |2j| <= 6 kept exactly in the operator
ITAIL = 14  # coefficients with |i| <= ITAIL are bounded by their exact series; beyond, tail_geo
bh, bp, gk = {}, {}, {}
for i in range(-ITAIL, ITAIL + 1):
    bh[i] = coef_bounds("bh", i)
for j in range(1, ITAIL + 1):
    bp[j] = coef_bounds("bp", j)
for k in (1, 3, 5, 7, 9):
    gk[k] = coef_bounds("g", k)

print("\n== 1. Fourier coefficients (exact brackets at beta0; uniform bounds on Q x {p>=10^6}) ==")
for k in (1, 3, 5, 7, 9):
    lo, hi, uni = gk[k]
    print(f"ghat_+-{k}: {br(lo, hi, 12)}  uniform |.| <= {up(uni, 12)}")
for i in range(0, IMAX + 1):
    lo, hi, uni = bh[i]
    print(f"bhat_+-{2*i}: {br(lo, hi, 12)}  uniform |.| <= {up(uni, 12)}")
for j in range(1, KMAX + 1):
    lo, hi, uni = bp[j]
    print(f"b'_+-{2*j}:  {br(lo, hi, 12)}  uniform |.| <= {up(uni, 12)}")

# rho_0 = sum_k (|k|+2)|bhat_k| uniform (recomputed); tail beyond |2i| <= 2 IMAX by tail_geo
rho0_up = sum(Fr(2 * abs(i) + 2) * bh[i][2] for i in range(-ITAIL, ITAIL + 1))
rho0_up += tail_geo(ITAIL + 1, lambda i: Fr(2 * i + 2))
rho0_lo = sum(Fr(2 * abs(i) + 2) * min(abs(bh[i][0]), abs(bh[i][1])) for i in range(-IMAX, IMAX + 1))
print(f"rho_0 = sum_k (|k|+2)|bhat_k| : at beta0 >= {dn(rho0_lo, 6)}; uniform <= {up(rho0_up, 6)} "
      f"(Round 183: 2.17565)")

# A(h_1) <= 2|sqrt t| sum_k |b'_k| |k|
Sbk_up = sum(2 * bp[j][2] * (2 * j) for j in range(1, ITAIL + 1)) + tail_geo(ITAIL + 1, lambda j: Fr(2 * j))
Sbk_lo = sum(2 * min(abs(bp[j][0]), abs(bp[j][1])) * (2 * j) for j in range(1, KMAX + 1))
A1_up = 2 * SQRT_T_UP * Sbk_up
sqrt_a_lo = fr_lo((arb(a.numerator) / arb(a.denominator)).sqrt())
print(f"sum_k |b'_k||k| : at beta0 >= {dn(Sbk_lo, 9)}; uniform <= {up(Sbk_up, 9)}")
print(f"A(h_1) <= 2|sqrt t| sum|b'_k||k| <= {up(A1_up, 6)} on Q;  at t=a: >= {dn(2 * sqrt_a_lo * Sbk_lo, 6)}"
      f"  (Round 183 model value [0.4945, 0.4946] at t=a)")

# ---------------------------------------------------------------- 2. one-step ratio
# A term T = (coefficient, weights in fibre A, weights in fibre B); dimension d = len(TA) = len(TB).


def line(k):
    return ([-k], [k])


def KJ(k):
    """K(J^k), k even != 0"""
    if k > 0:
        return ([-k, k] + [0] * (k - 2), [0] * k)
    m = -k
    return ([0] * m, [-m, m] + [0] * (m - 2))


def mul_line(G, s):
    """J^s (x) G"""
    return ([x - s for x in G[0]], [y + s for y in G[1]])


def mu(G):
    return sum(abs(x) for x in G[0]) + sum(abs(y) for y in G[1])


def dim(G):
    return len(G[0])


h1_terms = []        # (i, k, G')
for k in [2 * j for j in range(-KMAX, KMAX + 1) if j != 0]:
    for i in range(-IMAX, IMAX + 1):
        h1_terms.append((i, k, mul_line(KJ(k), 2 * i)))


def c_h1(i, k, which):
    """which='uni': uniform upper bound of |bhat_2i b'_k| on Q; 'lo': lower bound at beta0"""
    if which == "uni":
        return bh[i][2] * bp[abs(k) // 2][2]
    lb = min(abs(bh[i][0]), abs(bh[i][1]))
    lp = min(abs(bp[abs(k) // 2][0]), abs(bp[abs(k) // 2][1]))
    return lb * lp


def child_rank_F(G, FA, FB):
    """generic rank of F (x) G before transport, F given by its fibre lists"""
    return Fr(sum(abs(w + x) for w in FA for x in G[0]) + sum(abs(w + y) for w in FB for y in G[1]), 2)


print("\n== 2. one-step per-simple A-ratio of F -> K(G F): exactly d_G + mu(G)/2 (Prop. A) ==")
# (i) upper bound: triangle inequality (proved in the report).  (ii) the family
# F_K = (A: -K, 0^(K/2-1) | B: 0^(K/2)) approaches it; check exactly at K = 2*10^4.
ok = True
for (i, k, G) in h1_terms:
    d, m_ = dim(G), mu(G)
    Kb = 20000
    FA = [-Kb] + [0] * (Kb // 2 - 1)
    FB = [0] * (Kb // 2)
    # fast exact evaluation (zeros contribute sum |x|):
    rp = Fr(sum(abs(-Kb + x) for x in G[0]) + (Kb // 2 - 1) * sum(abs(x) for x in G[0])
            + (Kb // 2) * sum(abs(y) for y in G[1]), 2)
    ratio = rp / Fr(Kb, 2)
    bound = d + Fr(m_, 2)
    gap = bound - ratio
    if not (0 <= gap <= Fr(2 * (d + m_), Kb)):
        ok = False
print(f"for all {len(h1_terms)} terms J^2i K(J^k), |2i|<=6, |k|<=6: F_K ratio <= d+mu/2 and within "
      f"2(d+mu)/K of it at K=20000: {ok}")
print("  i=0: d + mu/2 = 2|k| (= the word rule (|0|+2)|k|, attained); table of d+mu/2 vs word (|2i|+2)|k|:")
for k in (2, 4):
    row = []
    for i in range(0, IMAX + 1):
        G = mul_line(KJ(k), 2 * i)
        row.append(f"2i={2*i}: {dim(G) + Fr(mu(G), 2)} vs {(2 * i + 2) * k}")
    print(f"  k=+-{k}: " + "; ".join(row))
# brute-force check of the triangle-inequality bound on random small simples (exact)
import random
random.seed(184)
viol = 0
for trial in range(3000):
    r = random.randint(1, 6)
    # random valid simple: 2r slots, sum |w| = 2r
    while True:
        ws = [random.randint(-4, 4) for _ in range(2 * r)]
        tot = sum(abs(w) for w in ws)
        if tot == 2 * r:
            break
    FA, FB = ws[:r], ws[r:]
    for (i, k, G) in h1_terms[:: 5]:
        if child_rank_F(G, FA, FB) > (dim(G) + Fr(mu(G), 2)) * r:
            viol += 1
print(f"triangle bound r' <= (d+mu/2) r on 3000 random valid simples x 9 terms: violations = {viol}")

beta1_up = sum(c_h1(i, k, "uni") * (dim(G) + Fr(mu(G), 2)) for (i, k, G) in h1_terms)
beta1_lo = sum(c_h1(i, k, "lo") * (dim(G) + Fr(mu(G), 2)) for (i, k, G) in h1_terms)
# tail of h_1 terms beyond the operator truncation (|2i| > 6 or |k| > 6): exact d+mu/2 per term
# for |i|, |j| <= ITAIL; beyond ITAIL the word bound (|2i|+2)|k| with tail_geo.
tail_h1 = Fr(0)
for jj in [j for j in range(-ITAIL, ITAIL + 1) if j != 0]:
    for i in range(-ITAIL, ITAIL + 1):
        if abs(jj) <= KMAX and abs(i) <= IMAX:
            continue
        G = mul_line(KJ(2 * jj), 2 * i)
        tail_h1 += bh[i][2] * bp[abs(jj)][2] * (dim(G) + Fr(mu(G), 2))
tail_h1 += (rho0_up * tail_geo(ITAIL + 1, lambda j: Fr(2 * j))
            + tail_geo(ITAIL + 1, lambda i: Fr(2 * i + 2)) * Sbk_up)
word1_up = sum(c_h1(i, k, "uni") * (2 * abs(i) + 2) * abs(k) for (i, k, G) in h1_terms)
rho1_lo = beta1_lo / Sbk_up
rho1_up = (beta1_up + tail_h1) / Sbk_lo
print(f"beta_1 := sup_F A-ratio of F -> K(Phi''(S) h_1 F) = sum |bhat b'|(d+mu/2):")
print(f"   at beta0 >= {dn(beta1_lo, 6)};  uniform on Q <= {up(beta1_up + tail_h1, 6)}  "
      f"(word rule: <= {up(word1_up + tail_h1, 6)})")
print(f"effective ratio rho_1 = beta_1 / sum|b'_k||k| in {br(rho1_lo, rho1_up, 4)}  "
      f"(word rule rho_0 = 2.17565; the i=0 terms alone force rho_1 >= 2|bhat_0|, Cor. A2)")
print(f"K(J^+-2), i=0 part alone: ratio exactly 2|k| = 4 per unit |b'_2| (not attained; approached by F_K)")

# ---------------------------------------------------------------- 3. validity (refill >= 0)
# Unit-slot contributions of a term T to (r', nz_A', nz_B') of the child, for a slot (v, f).


def slot_child(T, v, f):
    Tw = T[0] if f == 0 else T[1]
    rp2 = 0
    nz = [0, 0]
    dest = []
    for x in Tw:
        w = v + x
        rp2 += abs(w)
        if w < 0:
            nz[f] += 1
            dest.append((w, f))
        elif w > 0:
            nz[1 - f] += 1
            dest.append((w, 1 - f))
    return rp2, nz, dest            # r' contribution = rp2/2


def atom(v, f):
    """slot vector {(value, fibre): count} of the atom with one slot v in fibre f (|v|>=1)"""
    return {(v, f): Fr(1), (0, f): Fr(abs(v), 2) - 1, (0, 1 - f): Fr(abs(v), 2)}


def rays(vmax):
    """extreme rays of the cone of valid simples, values |v| <= vmax; each a dict slot->count"""
    out = []
    for f in (0, 1):
        for v in list(range(2, vmax + 1)) + list(range(-vmax, -1)):
            out.append(((("s", v, f)), atom(v, f)))
    for f in (0, 1):
        for e in (1, -1):
            a1 = atom(e, f)
            for u in list(range(1, vmax + 1)) + list(range(-vmax, 0)):
                a2 = atom(u, 1 - f)
                lam = abs(u)
                out.append((("p_other", e, f, u), add(scale(a1, lam), a2)))
            for u in list(range(3, vmax + 1)) + list(range(-vmax, -2)):
                a2 = atom(u, f)
                lam = abs(u) - 2
                out.append((("p_same", e, f, u), add(scale(a1, lam), a2)))
    return out


def scale(x, c):
    return {k: c * v for k, v in x.items()}


def add(x, y):
    z = dict(x)
    for k, v in y.items():
        z[k] = z.get(k, 0) + v
    return z


def check_valid(x):
    zA = x.get((0, 0), 0)
    zB = x.get((0, 1), 0)
    r = sum(Fr(abs(v), 1) * c for (v, f), c in x.items()) / 2
    nzA = sum(c for (v, f), c in x.items() if v != 0 and f == 0)
    nzB = sum(c for (v, f), c in x.items() if v != 0 and f == 1)
    return zA >= 0 and zB >= 0 and nzA + zA == r and nzB + zB == r and r > 0


VR = 40
RAYS = rays(VR)
print("\n== 3. validity of the rule on the cone of valid simples (exact) ==")
print(f"extreme rays (singles |v|>=2; pairs with a |v|=1 slot), |v| <= {VR}: {len(RAYS)}; all valid: "
      f"{all(check_valid(x) for _, x in RAYS)}")


def refills(T, x):
    rp2 = 0
    nzA = nzB = 0
    for (v, f), c in x.items():
        a2, nz, _ = slot_child(T, v, f)
        rp2 += c * a2
        nzA += c * nz[0]
        nzB += c * nz[1]
    rp = Fr(rp2) / 2 if not isinstance(rp2, Fr) else rp2 / 2
    return rp - nzA, rp - nzB


seed_terms = [line(k) for k in (1, -1, 3, -3, 5, -5)]
all_T = seed_terms + [G for (_, _, G) in h1_terms]
neg = 0
minref = None
for T in all_T:
    for _, x in RAYS:
        ra, rb = refills(T, x)
        if ra < 0 or rb < 0:
            neg += 1
        m_ = min(ra, rb)
        minref = m_ if minref is None else min(minref, m_)
print(f"refills r' - nz on every ray for {len(all_T)} terms (6 seed lines, {len(h1_terms)} h_1 terms): "
      f"negative in {neg} cases; minimum {minref}")
print("  (for |v| > max|x| the refill is affine in |v| on each ray family; slopes checked below)")
slope_bad = 0
for T in all_T:
    W = max(abs(x) for x in T[0] + T[1])
    for f in (0, 1):
        for sgn in (1, -1):
            v1, v2 = sgn * (W + 3), sgn * (W + 4)
            r1 = refills(T, atom(v1, f))
            r2 = refills(T, atom(v2, f))
            for c1, c2 in zip(r1, r2):
                if c2 - c1 < 0:
                    slope_bad += 1
print(f"  asymptotic single-atom refill slopes negative: {slope_bad} (pair families: checked up to |u|={VR})")

# ---------------------------------------------------------------- 4. exact m-step growth
D = 10 ** 15   # common denominator for coefficients (upper bounds rounded up / lower down)


def ceilD(q):
    return -((-q.numerator * D) // q.denominator)


def floorD(q):
    return (q.numerator * D) // q.denominator


def adjoint(terms, m, vmax):
    """terms: list of (C_int, T) with coefficient C_int/D.  Returns list Phi[j] for j=0..m with
    Phi[j][(v,f)] = 2^(j+1) D^j phi_j(v,f), phi_j = A-price of the j-step path sum of a unit slot.
    phi_0(v,f) = |v|/2."""
    W = max(max(abs(x) for x in T[0] + T[1]) for _, T in terms)
    R = vmax + m * W
    phi = {(v, f): abs(v) for v in range(-R, R + 1) for f in (0, 1)}   # 2 * |v|/2
    out = [phi]
    for j in range(m):
        R -= W
        new = {}
        z0, z1 = phi[(0, 0)], phi[(0, 1)]
        for v in range(-R, R + 1):
            for f in (0, 1):
                tot = 0
                for C, T in terms:
                    rp2, nz, dest = slot_child(T, v, f)
                    s = 2 * sum(phi[dd] for dd in dest) + rp2 * (z0 + z1) - 2 * nz[0] * z0 - 2 * nz[1] * z1
                    tot += C * s
                new[(v, f)] = tot
        phi = new
        out.append(phi)
    return out, W


def ray_value(phi, x, j):
    num = sum(c * phi[k] for k, c in x.items())
    den = sum(abs(v) * c for (v, f), c in x.items()) / 2
    return Fr(num) / (Fr(2 ** (j + 1)) * Fr(D) ** j) / den


def growth(terms, m, label=""):
    """exact sup over valid simples of the m-step path-summed A-ratio, for m=1..mmax"""
    phis, W = adjoint(terms, m, vmax=m * W_GLOBAL + 6)
    res = []
    for j in range(1, m + 1):
        Vaff = j * W
        Vtop = Vaff + 4
        best = Fr(0)
        arg = None
        rs = rays(Vtop)
        for key, x in rs:
            val = ray_value(phis[j], x, j)
            if val > best:
                best, arg = val, key
        # affine tails: on each ray family, values at Vaff+1..Vaff+4 are linear-fractional in |v|;
        # sup over |v| >= Vaff+1 is max(value at Vaff+1, limit).  Limit = from two points of the
        # affine numerator/denominator.
        lim_best = Fr(0)
        fam = {}
        for key, x in rs:
            if key[0] == "s":
                _, v, f = key
                fk = ("s", v > 0, f)
                av = abs(v)
            else:
                kind, e, f, u = key
                fk = (kind, e, f, u > 0)
                av = abs(u)
            if av in (Vaff + 2, Vaff + 3, Vaff + 4):
                num = Fr(sum(c * phis[j][k] for k, c in x.items())) / (Fr(2 ** (j + 1)) * Fr(D) ** j)
                den = sum(abs(v) * c for (v, f2), c in x.items()) / 2
                fam.setdefault(fk, {})[av] = (num, den)
        affine_ok = True
        for fk, pts in fam.items():
            (n2, d2), (n3, d3), (n4, d4) = pts[Vaff + 2], pts[Vaff + 3], pts[Vaff + 4]
            if n4 - 2 * n3 + n2 != 0 or d4 - 2 * d3 + d2 != 0:
                affine_ok = False
            sn, sd = n3 - n2, d3 - d2
            lim = sn / sd
            lim_best = max(lim_best, lim)
        G = max(best, lim_best)
        res.append((j, G, best, lim_best, arg, affine_ok))
    return res


def root_up(G, m):
    """rational >= G^(1/m)"""
    x = fr_hi(arb(G.numerator) / arb(G.denominator))
    r = arb(x.numerator) / arb(x.denominator)
    return fr_hi(r ** (arb(1) / m))


MMAX = 8
seed_unif = [(ceilD(gk[abs(k)][2]), line(k)) for k in (1, -1, 3, -3, 5, -5)]          # gamma_k (no varpi)
seed_unif_v = [(ceilD(VARPI * gk[abs(k)][2]), line(k)) for k in (1, -1, 3, -3, 5, -5)]  # varpi gamma_k
h1_unif = [(ceilD(c_h1(i, k, "uni")), G) for (i, k, G) in h1_terms]
seed_lo_v = [(floorD(fr_lo(varpi) * min(abs(gk[abs(k)][0]), abs(gk[abs(k)][1]))), line(k))
             for k in (1, -1, 3, -3, 5, -5)]
h1_lo = [(floorD(c_h1(i, k, "lo")), G) for (i, k, G) in h1_terms]

print("\n== 4. exact m-step growth G_m = sup_valid A(path-summed m-step child)/A(parent) ==")
W_GLOBAL = 5
t1 = time.time()
gS = growth(seed_unif, MMAX)
print("4a. seed multiplier, weights gamma_k (|k|<=5), regression against Round 183 Prop. 3 (alpha=0):")
r183 = {1: "1.970484", 2: "2.940449", 4: "6.278417", 8: "25.495420"}
for (j, G, best, lim, arg, aff) in gS:
    print(f"   m={j}: G <= {up(G, 6)} (finite rays {up(best, 6)}, |v|->inf limit {up(lim, 6)}, affine tails {aff})"
          + (f"  [Round 183: {r183[j]}]" if j in r183 else ""))
print(f"   ({time.time() - t1:.0f} s)")
g183 = {1: Fr("0.478072561593"), 3: Fr("0.007039589281"), 5: Fr("0.000156385050")}
gS183 = growth([(ceilD(g183[abs(k)]), line(k)) for k in (1, -1, 3, -3, 5, -5)], MMAX)
print("4a'. same with the Round 183 printed gamma_k (0.478072561593, 0.007039589281, 0.000156385050):")
print("   " + "; ".join(f"m={j}: {up(G, 6)}" for (j, G, *rest) in gS183)
      + "   [Round 183: 1.970484, 2.940449, 4.374161, 6.278417, 8.992638, 12.751861, 18.062170, 25.495420]")

W_GLOBAL = 12
t1 = time.time()
gSv = growth(seed_unif_v, MMAX)
gH = growth(h1_unif, 1)
MJ = 12   # joint growth computed to m = 12
gSv12 = growth(seed_unif_v, MJ)
gJ = growth(seed_unif_v + h1_unif, MJ)
gJlo = growth(seed_lo_v + h1_lo, MJ)
print("4b. h_1 part alone (one step, uniform weights): "
      f"G_1 <= {up(gH[0][1], 6)}; Section 2 closed form beta_1 <= {up(beta1_up, 6)}; "
      f"agree within coefficient rounding (<= 10^-12): {abs(gH[0][1] - beta1_up) <= Fr(1, 10 ** 12)}")
print("4c. joint L_S + B_1 (varpi gamma_k on J^k, |k|<=5; |bhat b'| on J^2i K(J^k), |2i|,|k|<=6):")
print("    m   G_m(seed, varpi)   G_m(joint, uniform)   G_m(joint, at t=a lower)   rate seed  rate joint")
for (j, G, *_), (_, GJ, b2, l2, arg, aff), (_, GL, *_) in zip(gSv12, gJ, gJlo):
    print(f"    {j}   {up(G, 6):>14}   {up(GJ, 6):>18}   {dn(GL, 6):>22}   "
          f"{up(root_up(G, j), 5):>8}  {up(root_up(GJ, j), 5):>8}   affine {aff} argmax {arg}")
print(f"   ({time.time() - t1:.0f} s)")

# ---------------------------------------------------------------- 5. budgets
print("\n== 5. kappa*_A (b1*), h-higher majorant H, and the allowance for A(h - h_1) ==")
p0 = Fr(1272, 100000)
M0 = Fr(4823, 1000)


def c_arb(M):
    """c(M) = (2/sqrt N)(1+x/2)(1-x)^(-5/2), x = M^2/N  (arb ball)"""
    Ma = arb(M.numerator) / arb(M.denominator)
    Na = arb(Nq.numerator) / arb(Nq.denominator)
    x = Ma * Ma / Na
    return 2 / Na.sqrt() * (1 + x / 2) * (1 - x) ** arb(-2.5)


def kappa_lower(u):
    """kappa*_A >= 1 - p0/u - c(M0+u) u / 2  (A price: c halves, Lemma 4(ii) of Round 183)"""
    val = 1 - (arb(p0.numerator) / arb(p0.denominator)) / (arb(u.numerator) / arb(u.denominator)) \
        - c_arb(M0 + u) * (arb(u.numerator) / arb(u.denominator)) / 2
    return fr_lo(val)


best_k, best_u = Fr(0), None
for num in range(1300, 1700, 2):
    u = Fr(num, 10000)
    kl = kappa_lower(u)
    if kl > best_k:
        best_k, best_u = kl, u
# upper bound: partition (0, 3/8] into pieces; on [u1,u2]: <= 1 - p0/u2 - c(M0+u1) u1/2
kap_hi = Fr(0)
grid = [Fr(j, 20000) for j in range(1, 7501)]
for u1, u2 in zip(grid, grid[1:]):
    val = 1 - (arb(p0.numerator) / arb(p0.denominator)) / (arb(u2.numerator) / arb(u2.denominator)) \
        - c_arb(M0 + u1) * (arb(u1.numerator) / arb(u1.denominator)) / 2
    kap_hi = max(kap_hi, fr_hi(val))
KAPPA = best_k
print(f"kappa*_A in {br(best_k, kap_hi, 8)} (certifying u = {best_u}); Round 183: [0.83790251, 0.83790253]")


def Gall(y):
    Na = arb(Nq.numerator) / arb(Nq.denominator)
    return y * (2 * Na - y * y) / (Na - y * y) ** arb(1.5)


def Gall_d(y):
    Na = arb(Nq.numerator) / arb(Nq.denominator)
    return Na * (2 * Na + y * y) / (Na - y * y) ** arb(2.5)


def H_ball(A):
    s = arb(s_up.numerator) / arb(s_up.denominator)
    Aa = arb(A.numerator) / arb(A.denominator)
    return Gall(s + Aa) - Gall(s) - Aa * Gall_d(s)


def H_up(A):
    return fr_hi(H_ball(A))


def H_lo_at(A, s_val):
    Aa = arb(A.numerator) / arb(A.denominator)
    return fr_lo(Gall(s_val + Aa) - Gall(s_val) - Aa * Gall_d(s_val))


for Av in (Fr(55, 100), Fr(1), Fr(1994573, 1000000)):
    print(f"H({float(Av):.6f}) in {br(fr_lo(H_ball(Av)), H_up(Av), 5)}   (Round 183: 0.01932 / 0.07243 / 0.40151)")

# seed tail |k| >= 7 per step (A price: ratio 1+|k| per unit coefficient)
gam_tail = sum((1 + k) * 2 * gk[k][2] for k in (7, 9)) + \
    2 * sum(Fr(1 + k) * bb ** ((k - 1) // 2) / (1 - bb) for k in range(11, 400, 2))
tauS = VARPI * gam_tail
tau1 = tail_h1
print(f"perturbations per step: seed |k|>=7: tau_S <= {up(tauS, 9)};  h_1 beyond |2i|,|k| <= 6: tau_1 <= {up(tau1, 9)}")


def power_form(gs, m0):
    """lam = G_m0^(1/m0) (rounded up), C = max_{j<m0} G_j / lam^j (>= 1)"""
    Gd = {j: G for (j, G, *rest) in gs}
    lam = root_up(Gd[m0], m0)
    C = Fr(1)
    for j in range(1, m0):
        C = max(C, Gd[j] / lam ** j)
    return lam, C


def allowance(lam, C, beta_fixed, use_h1_inA=True, rho=None):
    """largest X (grid 1e-4, lower end certified) with
       lam + C (beta_fixed + rho X / sqrt N + H(A1_up + X)) < 1 - C (1 - KAPPA)"""
    rho = rho0_up if rho is None else rho
    rhs = 1 - C * (1 - KAPPA)
    lo = None
    for j in range(0, 20001):
        X = Fr(j, 10000)
        cost = lam + C * (beta_fixed + rho * X * INV_SQRTN + H_up(A1_up + X))
        if cost < rhs:
            lo = X
        else:
            break
    return lo, rhs


rows = []
print("\nCriterion (Cor. 2.2 of Round 182, Prop. 2): lam + C beta' < 1 - C(1 - kappa*_A).")
print("(I) separate pricing (Round 183 form, with the exact one-step beta_1 of Section 2):")
print("     beta' = tau_S + beta_1 + tau_1 + rho_0 X/sqrt N + H(A(h_1)+X),  X = A(h - h_1)")
for m0 in range(1, MMAX + 1):
    lam, C = power_form(gSv, m0)
    X, rhs = allowance(lam, C, tauS + beta1_up + tau1)
    rows.append(("I", m0, lam, C, X))
    print(f"   m0={m0}: lam_S <= {up(lam, 5)}, C_S <= {up(C, 4)}: A(h-h_1) allowed below "
          + ("(none: X=0 already fails)" if X is None else f">= {dn(X, 4)}"))
print("(II) joint exact growth of L_S + B_1, perturbed by the rest:")
print("     beta' = tau_S + tau_1 + rho_0 X/sqrt N + H(A(h_1)+X)")
for m0 in range(1, MJ + 1):
    lam, C = power_form(gJ, m0)
    X, rhs = allowance(lam, C, tauS + tau1)
    rows.append(("II", m0, lam, C, X))
    print(f"   m0={m0}: lam_J <= {up(lam, 5)}, C_J <= {up(C, 4)}: A(h-h_1) allowed below "
          + ("(none: X=0 already fails)" if X is None else f">= {dn(X, 4)}"))
# floor for any per-simple rule on a generic simple G of h - h_1: d + mu(J^2i G)/2 >= 2d for i = 0
# and >= d otherwise, so rho >= rho_floor := 2|bhat_0| + sum_{i != 0} |bhat_2i| (at beta0).
rho_floor = 2 * min(abs(bh[0][0]), abs(bh[0][1])) + sum(min(abs(bh[i][0]), abs(bh[i][1]))
                                                        for i in range(-IMAX, IMAX + 1) if i != 0)
print(f"(III) as (II) with rho_floor = 2|bhat_0| + sum_(i!=0)|bhat_2i| >= {dn(rho_floor, 5)} for h - h_1 "
      "(no per-simple rule can price a generic simple of h - h_1 below this; an optimistic bound):")
for m0 in (4, 8, 12):
    lam, C = power_form(gJ, m0)
    X, rhs = allowance(lam, C, tauS + tau1, rho=rho_floor)
    print(f"   m0={m0}: A(h-h_1) allowed below " + ("(none)" if X is None else f">= {dn(X, 4)}"))

# ---------------------------------------------------------------- 6. direct Duhamel sum
# Round 182 Prop. 2 needs Gamma = sum_{m>=0} ||L^m|| < 1/(1 - kappa*) (sigma_k <= Gamma p0 unsigned).
# With ||L_0^a|| <= G_a and ||B'|| <= beta', expanding (L_0 + B')^m into words gives
#     sum_m ||(L_0 + B')^m|| <= sum_j beta'^j g^(j+1) = g / (1 - beta' g),   g = sum_{a>=0} G_a,
# so the criterion is beta' < 1/g - (1 - kappa*)  (no power-form constant C).
# Tail a > MJ: G_{q MJ + j} <= G_MJ^q G_j (submultiplicativity), so
#     sum_{a > MJ} G_a <= (G_MJ / (1 - G_MJ)) * sum_{j=0}^{MJ-1} G_j  +  (G_MJ itself counted once).
def g_sum(gs, mtop):
    Gd = {0: Fr(1)}
    Gd.update({j: G for (j, G, *rest) in gs})
    head = sum(Gd[j] for j in range(0, mtop + 1))
    GM = Gd[mtop]
    tail = GM / (1 - GM) * sum(Gd[j] for j in range(1, mtop + 1))
    return head + tail


def allowance_sum(g, beta_fixed, A_fixed, rho=None, step=Fr(1, 10000), xmax=2):
    """largest X on the grid with beta_fixed + rho X/sqrt N + H(A_fixed + X) < 1/g - (1 - KAPPA)"""
    rho = rho0_up if rho is None else rho
    rhs = 1 / g - (1 - KAPPA)
    lo = None
    j = 0
    while j * step <= xmax:
        X = j * step
        if beta_fixed + rho * X * INV_SQRTN + H_up(A_fixed + X) < rhs:
            lo = X
        else:
            break
        j += 1
    return lo, rhs


gS_sum = g_sum(gSv12, MJ)
gJ_sum = g_sum(gJ, MJ)
gam_star = 1 / (1 - KAPPA)
print("\n== 6. direct Duhamel sum: criterion sum_m ||L^m||_A < 1/(1 - kappa*_A) ==")
print(f"1/(1 - kappa*_A) >= {dn(gam_star, 5)};  g_S = sum_m G_m(seed) <= {up(gS_sum, 6)};  "
      f"g_J = sum_m G_m(joint) <= {up(gJ_sum, 6)}")
bmS = 1 / gS_sum - (1 - KAPPA)
bmJ = 1 / gJ_sum - (1 - KAPPA)
print(f"budget beta'_max = 1/g - (1 - kappa*):  seed only >= {dn(bmS, 5)} (power form, Round 183: 0.19359);"
      f"  joint >= {dn(bmJ, 5)}")
# (a) Round 183 setting: whole h priced by the word rule around the seed, X = A(h)
Xa, _ = allowance_sum(gS_sum, tauS, Fr(0))
print(f"(a) seed only, all of h by the word rule (Round 183 setting): A(h) allowed below >= {dn(Xa, 4)}"
      f"  (power form: 0.6179)")
# (b) separate: exact one-step beta_1 for h_1, word rule for h - h_1
Xb, _ = allowance_sum(gS_sum, tauS + beta1_up + tau1, A1_up)
print(f"(b) seed only, h_1 by its exact one-step ratio, h - h_1 by the word rule: "
      f"A(h - h_1) allowed below >= {dn(Xb, 4)}")
# (c) joint
Xc, _ = allowance_sum(gJ_sum, tauS + tau1, A1_up)
print(f"(c) joint L_S + B_1, h - h_1 by the word rule: A(h - h_1) allowed below >= {dn(Xc, 4)}")
Xd, _ = allowance_sum(gJ_sum, tauS + tau1, A1_up, rho=rho_floor)
print(f"(d) as (c) with the per-simple floor rho_floor for h - h_1 (optimistic): >= {dn(Xd, 4)}")
# what a given A(h - h_1) costs: show the margin at a few values
for Xv in (Fr(19, 100), Fr(25, 100), Fr(30, 100)):
    cst = tauS + tau1 + rho0_up * Xv * INV_SQRTN + H_up(A1_up + Xv)
    print(f"    (c) at A(h-h_1) = {float(Xv):.2f}: beta' <= {up(cst, 5)} vs budget >= {dn(bmJ, 5)}")

# ---------------------------------------------------------------- 7. model price of the Picard tail
# Compact-model evidence for the remaining input A(h - h_1): unsigned per-simple prices of the
# explicit pieces L_S^j h_1 (j >= 1) and Q_1 = (1/2) K(Phi''(S) h_1^2).  L_S h_1 = s sum ghat_k b'_k'
# K(J^k K(J^k')) (2 sqrt t cancels); the path-summed A-price of L_S^j h_1 is
#   <= 2|sqrt t| sum_k' |b'_k'| phi_j(K(J^k')),  phi_j the seed adjoint with weights varpi gamma_k.
# Round 80 (leaves of the leading field are mutually inequivalent) suggests these path sums are the
# actual A-prices of the pieces in the model, so they are not just crude majorants.  Evidence (c).
print("\n== 7. compact-model evidence: unsigned per-simple prices of the Picard tail of h ==")
phisS, _ = adjoint(seed_unif_v, MJ, vmax=10)


def slots_of(G):
    x = {}
    for v in G[0]:
        x[(v, 0)] = x.get((v, 0), 0) + 1
    for v in G[1]:
        x[(v, 1)] = x.get((v, 1), 0) + 1
    return x


def phi_val(phis, j, x):
    return Fr(sum(c * phis[j][k] for k, c in x.items()), 2 ** (j + 1) * D ** j)


pref = 2 * SQRT_T_UP
Aj = []
for j in range(1, MJ + 1):
    val = pref * sum(2 * bp[jj][2] * phi_val(phisS, j, slots_of(KJ(2 * jj))) for jj in range(1, KMAX + 1))
    Aj.append(val)
GSd = {jj: G for (jj, G, *rest) in gSv12}
tail_lin = Aj[-1] * GSd[1] / (1 - GSd[1]) if GSd[1] < 1 else None
S_lin = sum(Aj) + tail_lin
print("A_ps(L_S^j h_1), j=1..12 (uniform on Q): " + ", ".join(up(x, 4) for x in Aj))
print(f"sum_(j>=1) A_ps(L_S^j h_1) <= {up(S_lin, 4)}  (tail after j=12 by G_1(seed) = {up(GSd[1], 4)} per step)")
# Q_1 = (1/2) K(Phi''(S) h_1 h_1): coefficient (1/2)|bhat_2i b'_k| * 2|sqrt t| |b'_k''|
Q1 = Fr(0)
for jj in range(1, KMAX + 1):
    for sg in (1, -1):
        F = KJ(sg * 2 * jj)
        FA, FB = F
        for (i, k, G) in h1_terms:
            Q1 += Fr(1, 2) * c_h1(i, k, "uni") * pref * bp[jj][2] * child_rank_F(G, FA, FB)
print(f"A_ps(Q_1), Q_1 = (1/2) K(Phi''(S) h_1^2) <= {up(Q1, 4)};  A_ps(L_S^j Q_1) summed over j >= 0 "
      f"<= {up(Q1 * g_sum(gSv12, MJ), 4)} (crude: by G_j(seed))")
print(f"unsigned model estimate of A(h - h_1): about {up(S_lin + Q1 * g_sum(gSv12, MJ), 3)} "
      f"(linear tail + first quadratic piece; higher pieces not included)")
print(f"compare: certified allowance (c) >= {dn(Xc, 4)};  floating sup|h - h_1| ~ 0.21-0.22 (p >= 10^6)")
# [float] model RMS (normalized l2 = l2 norm of the coefficients if the simples are distinct and
# unit-normalized) at t = a, s = 2 sqrt 2, for comparison with the physical RMS of the diagnostic.
import math
bpf = {k: float(min(abs(bp[abs(k) // 2][0]), abs(bp[abs(k) // 2][1]))) for k in (2, -2, 4, -4, 6, -6)}
gkf = {k: float(gk[abs(k)][0]) for k in (1, -1, 3, -3, 5, -5)}
rms_h1 = 2 * math.sqrt(2031 / 128) * math.sqrt(sum(v * v for v in bpf.values()))
rms_LS = 2 * math.sqrt(2) * math.sqrt(sum((gkf[k] * bpf[kp]) ** 2 for k in gkf for kp in bpf))
print(f"[float] model RMS(h_1) = {rms_h1:.4f}, model RMS(L_S h_1) = {rms_LS:.4f}  "
      f"(physical, p = 4000037: 0.1724, 0.0414)")

# ---------------------------------------------------------------- 8. joint growth with L_S h_1 as well
# h = h_1 + h_2' + rest with h_2' := L_S h_1 = s sum ghat_k b'_k' C_{k,k'}, C_{k,k'} = K(J^k K(J^k')).
# B_2' = K(Phi''(S) h_2' .) has terms J^2i C_{k,k'} with coefficient |bhat_2i| s |ghat_k b'_k'| / (2|sqrt t|).
print("\n== 8. joint exact growth of L_S + B_1 + B_2' (B_2' = K(Phi''(S) L_S h_1 .)), and the allowance for rest ==")


def transport_child(G, T):
    """explicit child K(T (x) G) as fibre lists (rule of the module docstring)"""
    PA = [v + x for v in G[0] for x in T[0]]
    PB = [v + y for v in G[1] for y in T[1]]
    rp = (sum(abs(w) for w in PA) + sum(abs(w) for w in PB)) // 2
    A_ = [w for w in PA if w < 0] + [w for w in PB if w > 0]
    B_ = [w for w in PB if w < 0] + [w for w in PA if w > 0]
    assert len(A_) <= rp and len(B_) <= rp
    return (sorted(A_ + [0] * (rp - len(A_))), sorted(B_ + [0] * (rp - len(B_))))


K2 = (2, -2, 4, -4)
I2 = 2
h2_terms = []
A2_up = Fr(0)
for kp in K2:
    for k in (1, -1, 3, -3, 5, -5):
        C = transport_child(KJ(kp), line(k))
        cC = s_up * gk[abs(k)][2] * bp[abs(kp) // 2][2]       # |coefficient of C in h_2'| (2 sqrt t cancels)
        A2_up += cC * dim(C)
        for i in range(-I2, I2 + 1):
            G = mul_line(C, 2 * i)
            h2_terms.append((ceilD(bh[i][2] * cC * INV_SQRTN), G, cC, i, k, kp))
# truncation tails of h_2' itself (|k| >= 7 or |k'| >= 6) for A(h_2'), word bound dim(C) <= (|k|+1)|k'|
out_kk = Fr(0)
for kp2 in range(2, 2 * ITAIL + 1, 2):
    for kk in list(range(1, 10, 2)) + list(range(11, 200, 2)):
        if kp2 <= 4 and kk <= 5:
            continue
        gam = gk[kk][2] if kk <= 9 else bb ** ((kk - 1) // 2) / (1 - bb)
        out_kk += 2 * 2 * gam * bp[kp2 // 2][2] * (kk + 1) * kp2
out_kk += tail_geo(ITAIL + 1, lambda j: Fr(2 * j)) * 2 * sum((kk + 1) * (gk[kk][2] if kk <= 9 else 1) for kk in (1, 3, 5, 7, 9))
A2_up += s_up * out_kk
in_kk = sum(s_up * gk[abs(k)][2] * bp[abs(kp) // 2][2] * (abs(k) + 1) * abs(kp) for kp in K2 for k in (1, -1, 3, -3, 5, -5))
rho_out_i = sum(Fr(2 * abs(i) + 2) * bh[i][2] for i in range(-ITAIL, ITAIL + 1) if abs(i) > I2) \
    + tail_geo(ITAIL + 1, lambda i: Fr(2 * i + 2))
tau2 = INV_SQRTN * (rho0_up * s_up * out_kk + rho_out_i * in_kk)
print(f"h_2' = L_S h_1: {len(h2_terms) // (2 * I2 + 1)} simples C_(k,k'), dims "
      f"{sorted(set(dim(G) for _, G, *r in h2_terms))}; A_ps(h_2') <= {up(A2_up, 4)}; tail tau_2 <= {up(tau2, 6)}")
neg2 = 0
for C_, G, *r in h2_terms:
    for _, x in RAYS:
        ra, rb = refills(G, x)
        if ra < 0 or rb < 0:
            neg2 += 1
    Wg = max(abs(v) for v in G[0] + G[1])
    for f in (0, 1):
        for sgn in (1, -1):
            r1 = refills(G, atom(sgn * (Wg + 3), f))
            r2 = refills(G, atom(sgn * (Wg + 4), f))
            neg2 += sum(1 for c1, c2 in zip(r1, r2) if c2 - c1 < 0)
print(f"validity (Lemma B1) for the {len(h2_terms)} B_2' terms on the {len(RAYS)} rays (|v| <= {VR}) and "
      f"asymptotic single-atom slopes: negative cases = {neg2}")
beta2_one = sum(Fr(C_, D) * (dim(G) + Fr(mu(G), 2)) for C_, G, *r in h2_terms)
print(f"one-step exact ratio of B_2' (Prop. A): <= {up(beta2_one, 5)}  (word rule rho_0 A(h_2')/sqrt N <= "
      f"{up(rho0_up * A2_up * INV_SQRTN, 5)})")
M8 = 8
t1 = time.time()
terms8 = seed_unif_v + h1_unif + [(C_, G) for C_, G, *r in h2_terms]
W_GLOBAL = max(max(abs(x) for x in G[0] + G[1]) for _, G in terms8)
gJ2 = growth(terms8, M8)
W_GLOBAL = 12
gJ8 = [row for row in gJ if row[0] <= M8]
print("    m   G_m(L_S+B_1)   G_m(L_S+B_1+B_2')")
for (j, G1, *r1), (_, G2, *r2) in zip(gJ8, gJ2):
    print(f"    {j}   {up(G1, 6):>10}   {up(G2, 6):>12}   affine {r2[3]}")
print(f"   ({time.time() - t1:.0f} s)")
gJ2_sum = g_sum(gJ2, M8)
bmJ2 = 1 / gJ2_sum - (1 - KAPPA)
print(f"g = sum_m G_m(L_S+B_1+B_2') <= {up(gJ2_sum, 6)};  budget beta'_max >= {dn(bmJ2, 5)}")
Xe, _ = allowance_sum(gJ2_sum, tauS + tau1 + tau2, A1_up + A2_up)
print(f"(e) joint L_S + B_1 + B_2', rest = h - h_1 - L_S h_1 by the word rule: A(rest) allowed below "
      + ("(none)" if Xe is None else f">= {dn(Xe, 4)}"))
model_rest = sum(Aj[1:]) + tail_lin + Q1 * g_sum(gSv12, MJ)
print(f"    compact-model unsigned price of rest: sum_(j>=2) A_ps(L_S^j h_1) + A_ps(sum_j L_S^j Q_1) about "
      f"{up(model_rest, 3)};  floating sup|h - h_1 - L_S h_1| ~ 0.05")

print(f"\ntotal runtime {time.time() - T0:.0f} s")
print("ALL EXACT CHECKS OK" if ok and viol == 0 and neg == 0 and slope_bad == 0 and neg2 == 0 else "SOME CHECK FAILED")
