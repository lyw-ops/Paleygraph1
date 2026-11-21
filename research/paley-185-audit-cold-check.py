#!/usr/bin/env python3
"""Round 185 audit: independent float replay of the cold Picard-leaf report.

Written by the Round 185 auditor. It imports nothing from the report's scripts. The compact-model
rules are re-implemented from their verbal statement (Round 184 (b4), (b-Jk), (b-T)):
  * the line J^k has two-fibre weight data A = (-k), B = (+k), dimension 1;
  * J^k (x) W shifts fibre A by -k and fibre B by +k; tensor = pairwise sums fibre by fibre;
  * transport K: r' = (1/2) sum |w| over both fibres; new A = negatives of A + positives of B,
    new B = negatives of B + positives of A, both refilled with zeros up to r' (refill >= 0).
Coefficients are computed by an FFT on a 4096-point grid at the single parameter point
t = a = 2031/128, s^2 = 8 (float; certifies nothing; the report's balls are uniform on a region).

Checks:
  1. linear path simples to depth 5: validity, distinct weight data, collisions and how they separate;
  2. depth prices P(L_S^j h_1), j = 0..5;
  3. depth <= 3 nonlinear pieces Q_1, L_S Q_1, X_1, C_1 (merged over tensor permutations):
     object counts, unsigned prices, containment ("touching") masses and opposite-sign masses;
  4. Theorem 3 / Corollary 5 arithmetic from the printed numbers, in exact decimals, with the
     direction of rounding.
Usage: .venv/bin/python -B research/paley-185-audit-cold-check.py
"""
from collections import Counter
from decimal import Decimal as D
import itertools
import sys

import numpy as np

OK = True


def check(cond, msg):
    global OK
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        OK = False


# ---------------------------------------------------------------- coefficients (FFT, float)
a = 2031 / 128
s2 = 8.0
beta = s2 / (4 * a)
NG = 4096
th = 2 * np.pi * np.arange(NG) / NG
cs = np.cos(th)


def fourier(vals):
    c = np.fft.fft(vals) / NG          # c[k] = mean f e^{-ik theta}
    return lambda k: float(np.real(c[k % NG]))


b_prime = fourier((1 + beta * cs ** 2) ** 0.5)          # Phi = 2 sqrt t sum b'_k J^k
g_hat = fourier(cs * (1 + beta * cs ** 2) ** -0.5)      # Phi' = s/(2 sqrt t) sum ghat_k J^k
b_hat = fourier((1 + beta * cs ** 2) ** -1.5)           # Phi'' = 1/(2 sqrt t) sum bhat J^k
e_c = fourier(cs * (1 + beta * cs ** 2) ** -2.5)        # Phi''' = -(3 s/(2 sqrt t)^3) sum e_c J^c
sqt = a ** 0.5
varpi = s2 ** 0.5 / (2 * sqt)

ROOTS = [2, -2, 4, -4, 6, -6]
SEED = [1, -1, 3, -3, 5, -5]
BH = [0, 2, -2, 4, -4, 6, -6]
EC = SEED


# ---------------------------------------------------------------- weight data
def freeze(A, B):
    return (tuple(sorted(A.items())), tuple(sorted(B.items())))


def line(k):
    return freeze(Counter({-k: 1}), Counter({k: 1}))


def shift(W, k):
    A = Counter({w - k: c for w, c in W[0]})
    B = Counter({w + k: c for w, c in W[1]})
    return freeze(A, B)


def tensor(W1, W2):
    out = []
    for f in (0, 1):
        cnt = Counter()
        for w1, c1 in W1[f]:
            for w2, c2 in W2[f]:
                cnt[w1 + w2] += c1 * c2
        out.append(cnt)
    return freeze(*out)


def K(W):
    r2 = sum(abs(w) * c for w, c in W[0]) + sum(abs(w) * c for w, c in W[1])
    assert r2 % 2 == 0
    r = r2 // 2
    A, B = Counter(), Counter()
    for w, c in W[0]:
        if w < 0:
            A[w] += c
        elif w > 0:
            B[w] += c
    for w, c in W[1]:
        if w < 0:
            B[w] += c
        elif w > 0:
            A[w] += c
    za, zb = r - sum(A.values()), r - sum(B.values())
    if za < 0 or zb < 0:
        return None
    if za:
        A[0] += za
    if zb:
        B[0] += zb
    return freeze(A, B)


def dim(W):
    return sum(c for _, c in W[0])


def contains(small, big):
    for f in (0, 1):
        bd = dict(big[f])
        for w, c in small[f]:
            if bd.get(w, 0) < c:
                return False
    return True


# ---------------------------------------------------------------- 1-2. linear chain
print("== 1-2. linear chain (own implementation) ==")
lin = {}     # path -> (pre, W, coef)
frontier = {}
for k in ROOTS:
    pre = line(k)
    W = K(pre)
    lin[(k,)] = (pre, W, 2 * sqt * b_prime(k))
    frontier[(k,)] = W
for depth in range(1, 6):
    new = {}
    for p, Wp in frontier.items():
        for c in SEED:
            pre = shift(Wp, c)
            W = K(pre)
            assert W is not None
            lin[p + (c,)] = (pre, W, lin[p][2] * varpi * g_hat(c))
            new[p + (c,)] = W
    frontier = new
check(len(lin) == 55986, f"linear paths to depth 5: {len(lin)}")
byW = {}
for p, (pre, W, c) in lin.items():
    byW.setdefault(W, []).append(p)
coll = [ps for ps in byW.values() if len(ps) > 1]
check(len(byW) == 55982 and len(coll) == 4, f"distinct weight data {len(byW)}; colliding classes {len(coll)}")
sep = all(len({lin[p][0] for p in ps}) == len(ps) for ps in coll)
check(sep, "every colliding pair has different pre-transport data (separated by K injectivity)")
for ps in coll:
    print("     ", ps, "dims pre", [dim(lin[p][0]) for p in ps], "signs", [int(np.sign(lin[p][2])) for p in ps])
mono = all(dim(lin[p][1]) > dim(lin[p[:-1]][1]) for p in lin if len(p) > 1)
check(mono, "dimension strictly increases along every path")
rep = [0.494525, 0.260138, 0.122824, 0.062240, 0.030630, 0.015370]
for j in range(6):
    P = sum(abs(c) * dim(W) for p, (pre, W, c) in lin.items() if len(p) == j + 1)
    check(abs(P - rep[j]) < 2e-6, f"P(L_S^{j} h_1) = {P:.6f} (report midpoint {rep[j]})")
d1 = sum(abs(c) * dim(W) for p, (pre, W, c) in lin.items() if len(p) == 2 and dim(W) == 3)
check(abs(d1 - 0.248) < 1e-3, f"dim-3 simples carry {d1:.4f} of the depth-1 price")

# ---------------------------------------------------------------- 3. nonlinear depth <= 3
print("== 3. depth <= 3 nonlinear pieces ==")
root = {k: lin[(k,)] for k in ROOTS}
dep1 = {p: v for p, v in lin.items() if len(p) == 2}
NL = {}


def add(key, pre, coef, kind):
    W = K(pre)
    assert W is not None, "invalid object"
    if key in NL:
        NL[key][2] += coef
    else:
        NL[key] = [pre, W, coef, kind]


inv2 = 1 / (2 * sqt)
# Q_1 = 1/2 K(Phi'' h_1^2)
for i in BH:
    for k in ROOTS:
        for l in ROOTS:
            pre = shift(tensor(root[k][1], root[l][1]), i)
            add(("Q", i, tuple(sorted((k, l)))), pre, 0.5 * inv2 * b_hat(i) * root[k][2] * root[l][2], "Q_1")
Qkeys = [k for k in NL if k[0] == "Q"]
# L_S Q_1
for c in SEED:
    for qk in Qkeys:
        pre = shift(NL[qk][1], c)
        add(("LQ", c, qk), pre, varpi * g_hat(c) * NL[qk][2], "L_S Q_1")
# X_1 = K(Phi'' h_1 L_S h_1)
for i in BH:
    for k in ROOTS:
        for p, v in dep1.items():
            pre = shift(tensor(root[k][1], v[1]), i)
            add(("X", i, k, p), pre, inv2 * b_hat(i) * root[k][2] * v[2], "X_1")
# C_1 = 1/6 K(Phi''' h_1^3)
for c in EC:
    for k in ROOTS:
        for l in ROOTS:
            for m in ROOTS:
                pre = shift(tensor(tensor(root[k][1], root[l][1]), root[m][1]), c)
                add(("C", c, tuple(sorted((k, l, m)))), pre,
                    (1 / 6) * (-3 * s2 ** 0.5 * inv2 ** 3) * e_c(c) * root[k][2] * root[l][2] * root[m][2], "C_1")
counts = Counter(v[3] for v in NL.values())
check(counts == Counter({"Q_1": 147, "L_S Q_1": 882, "X_1": 1512, "C_1": 336}), f"object counts {dict(counts)}")
price = {kind: sum(abs(v[2]) * dim(v[1]) for v in NL.values() if v[3] == kind) for kind in counts}
reprice = {"Q_1": 0.024198, "L_S Q_1": 0.013503, "X_1": 0.026803, "C_1": 0.000668}
for kind in reprice:
    check(abs(price[kind] - reprice[kind]) < 2e-6, f"unsigned price {kind} = {price[kind]:.6f} (report {reprice[kind]})")
tot = sum(price.values())
check(abs(tot - 0.065172) < 3e-6, f"total nonlinear depth <= 3: {tot:.6f}")

L13 = [p for p in lin if 2 <= len(p) <= 4]
L03 = [p for p in lin if len(p) <= 4]
L0 = [p for p in lin if len(p) == 1]
pre_lin = {p: lin[p][0] for p in L03}
T13 = T03 = O13 = O0 = 0.0
for key, (pre, W, c, kind) in NL.items():
    pr = abs(c) * dim(W)
    h13 = [p for p in L13 if contains(pre_lin[p], pre)]
    h0 = [p for p in L0 if contains(pre_lin[p], pre)]
    if h13:
        T13 += pr
        if any(np.sign(c) * np.sign(lin[p][2]) < 0 for p in h13):
            O13 += pr
    if h13 or h0:
        T03 += pr
    if h0 and any(np.sign(c) * np.sign(lin[p][2]) < 0 for p in h0):
        O0 += pr
check(abs(T13 - 0.010630) < 3e-6, f"touching depth 1-3 linear: {T13:.6f} (report 0.010630)")
check(abs(T03 - 0.027188) < 3e-6, f"touching depth 0-3 linear: {T03:.6f} (report 0.027188)")
check(abs(O13 - 0.002608) < 3e-6, f"opposite-sign touching depth 1-3: {O13:.6f} (report 0.002608)")
check(abs(O0 - 0.001617) < 3e-6, f"opposite-sign touching roots: {O0:.6f} (report 0.001617)")
eqW = [k for k, v in NL.items() if v[1] in byW]
check(not eqW, "no nonlinear depth <= 3 object has the full weight data of a linear simple of depth <= 5")
# mean-field collision: Q objects K(J^{2i} K(J^k) K(J^k)) containing a root of opposite sign
mf = sorted((round(v[2], 9), k) for k, v in NL.items() if k[0] == "Q" and k[1] != 0 and k[2][0] == k[2][1] and abs(k[2][0]) == 2)
print("      Q_1 diagonal objects with k = l = +-2, i != 0:", [(f"{c:+.3e}", k) for c, k in mf][:6])
P13 = sum(abs(lin[p][2]) * dim(lin[p][1]) for p in L13)
P03 = sum(abs(lin[p][2]) * dim(lin[p][1]) for p in L03)
print(f"      own float values: linear 1-3 {P13:.6f}, 0-3 {P03:.6f}; truncation lower {P13 - T13:.6f} / {P03 - T03:.6f}")

# ---------------------------------------------------------------- 4. arithmetic
print("== 4. Theorem 3 / Corollary 5 arithmetic from the printed numbers (exact decimals) ==")
check(D("0.445201") - D("0.010630") == D("0.434571"), "0.445201 - 0.010630 = 0.434571")
check(D("0.939725") - D("0.027188") == D("0.912537"), "0.939725 - 0.027188 = 0.912537")
check(D("0.445201") - D("0.002608") == D("0.442593"), "0.445201 - 0.002608 = 0.442593")
check(D("0.939725") - D("0.002608") - D("0.001617") == D("0.935500"), "0.939725 - 0.002608 - 0.001617 = 0.935500")
c5 = D("0.445201") - D("0.002608") - D("0.003542") - D("0.022598") - D("0.0001685")
print(f"      Corollary 5 from printed components: {c5} (printed 0.416286; difference "
      f"{D('0.416286') - c5}: internal unrounded values, printed components are rounded outward)")
c5h = D("0.939725") - D("0.002608") - D("0.001617") - D("0.003542") - D("0.004351") - D("0.022598") - D("0.0001685") - D("0.0000271")
print(f"      Corollary 5 (h) from printed components: {c5h} (printed 0.904816)")
check(D("0.416286") - D("0.3411") >= D("0.0751") and D("0.904816") - D("0.7499") >= D("0.1549"),
      "survival thresholds N5 >= 0.0751 / 0.1549 rounded down")
check(c5 - D("0.3411") > D("0.0750") and c5h - D("0.7499") > D("0.1548"),
      "even from the outward-rounded printed components the margins exceed 0.0750 / 0.1548")
check(D("0.015393") * D("1.468064") <= D("0.022598"), "T2: 0.015393 * 1.468064 <= 0.022598")

print("ALL AUDIT CHECKS OK" if OK else "SOME CHECKS FAILED")
sys.exit(0 if OK else 1)
