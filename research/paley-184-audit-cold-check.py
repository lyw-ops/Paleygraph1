#!/usr/bin/env python3
"""Round 184 audit: independent float replay of the cold h_1 report's main numbers.

Written by the Round 184 auditor; shares no code with paley-184-cold-*.py.  Float64 throughout,
so it certifies nothing; it checks the report's exact/outward values from an independent method.

  (A) Proposition A: d + mu/2 for every J^2i K(J^k) term, and beta_1, rho_1 from the printed
      coefficient bounds.
  (B) Proposition B: G_m for the seed multiplier and for the joint L_S + B_1, m <= 12, by an
      adjoint recursion on single slots plus a linear program over the cone of valid simples
      (slot counts n_X(v), |v| <= VLP, plus far columns), not by extreme-ray enumeration.
      Also an LP check of Lemma B1 (child refills >= 0 on every valid parent).
  (C) Proposition C: g = sum G_m, budgets 1/g - (1 - kappa*_A), and the allowances
      (a) A(h) < 0.7499, (b) 0.2689, (c) A(h - h_1) < 0.3411, with H and kappa*_A recomputed
      from the Round 182/183 formulas.
Replay:  .venv/bin/python -B research/paley-184-audit-cold-check.py   (about 1 min)
"""
import math
import numpy as np
from scipy.optimize import linprog

# ---------------------------------------------------------------- coefficients (report's uniform bounds)
VARPI = 0.355030238
GAM = {1: 0.478072476927, 3: 0.007039473893, 5: 0.000156253134}
BHAT = {0: 0.915418577549, 1: 0.040726603131, 2: 0.001510258432, 3: 0.000052273958}   # index i of b^_2i
BP = {2: 0.015286666447, 4: 0.000113374540, 6: 0.000001681793}                         # b'_k


# independent recomputation at beta0 (series), to see the printed bounds are consistent
def series_coeffs():
    b0 = 256 / 2031
    # (1 + b cos^2 th)^al = sum_l C(al,l) b^l cos^(2l); cos^(2l) has coefficient C(2l, l+i)/4^l at e^(2i th)
    def gen(al, i, L=60):
        s, c = 0.0, 1.0
        for l in range(L):
            if l >= abs(i):
                s += c * b0 ** l * math.comb(2 * l, l + abs(i)) / 4 ** l
            c *= (al - l) / (l + 1)
        return s
    bh = {i: gen(-1.5, i) for i in range(4)}
    bp = {k: gen(0.5, k // 2) for k in (2, 4, 6)}
    return bh, bp


bh0, bp0 = series_coeffs()

# ---------------------------------------------------------------- terms
def line(k):
    return ([-k], [k])


def KJ(k):
    if k > 0:
        return ([-k, k] + [0] * (k - 2), [0] * k)
    return ([0] * (-k), [k, -k] + [0] * (-k - 2))


def shift(T, s):
    return ([x - s for x in T[0]], [y + s for y in T[1]])


seed = []
for k in (1, 3, 5):
    for sg in (1, -1):
        seed.append((VARPI * GAM[k], line(sg * k)))
h1 = []
for k in (2, 4, 6):
    for sk in (1, -1):
        for i in range(-3, 4):
            h1.append((BHAT[abs(i)] * BP[k], shift(KJ(sk * k), 2 * i)))
print(f"terms: seed {len(seed)}, h_1 {len(h1)}")

# ---------------------------------------------------------------- (A) Proposition A
def d_mu(T):
    return len(T[0]), sum(abs(x) for x in T[0]) + sum(abs(y) for y in T[1])


beta1 = sum(c * (d + mu / 2) for c, T in h1 for d, mu in [d_mu(T)])
word = sum(BHAT[abs(i)] * BP[k] * 2 * (abs(2 * i) + 2) * k for k in (2, 4, 6) for i in range(-3, 4))
sbk = 2 * sum(BP[k] * k for k in BP)
print("(A) d + mu/2 for J^2i K(J^k), k > 0:")
for k in (2, 4):
    row = []
    for i in (0, 1, 2, 3):
        d, mu = d_mu(shift(KJ(k), 2 * i))
        row.append(f"2i={2*i}: {d + mu/2:g} (word {(2*i+2)*k})")
    print(f"    k={k}: " + "; ".join(row))
print(f"    beta_1 = {beta1:.6f} (report [0.129836, 0.129840]); word rule {word:.6f} (report 0.135052)")
print(f"    sum|b'_k||k| = {sbk:.9f} (report 0.062073723..0.062074356); rho_1 = {beta1/sbk:.5f} (report 2.0916-2.0917)")
rho_floor = 2 * abs(bh0[0]) + 2 * sum(abs(bh0[i]) for i in (1, 2, 3))
print(f"    Cor. A2 floor 2|b0| + sum_(i!=0)|b_2i| at beta0 = {rho_floor:.5f} (report 1.91541)")
print(f"    series at beta0 vs printed bounds: max rel diff b^ {max(abs(abs(bh0[i])-BHAT[i])/BHAT[i] for i in BHAT):.1e},"
      f" b' {max(abs(abs(bp0[k])-BP[k])/BP[k] for k in BP):.1e}")

# ---------------------------------------------------------------- (B) adjoint + LP
VG = 4000          # grid half-width for the adjoint recursion
VLP = 150          # LP columns |v| <= VLP ...
FAR = [300, 600, 1200, 2400]   # ... plus far columns (exact grid values)
XFAR = [10 ** 5, 10 ** 7]      # ... plus columns extrapolated affinely from |v| = 2000, 2400


def route(w, X):
    """fibre of a nonzero product weight w formed in fibre X (0 = A, 1 = B)"""
    if w < 0:
        return X
    return 1 - X


def adjoint(terms, M):
    """phi[m][X][v + VG]: m-step path-summed rank contributed by one slot of weight v in fibre X"""
    vs = np.arange(-VG, VG + 1)
    phi = [np.vstack([np.abs(vs) / 2.0, np.abs(vs) / 2.0])]
    for m in range(1, M + 1):
        prev = phi[-1]
        new = np.zeros_like(prev)
        z = (prev[0][VG], prev[1][VG])      # value of a zero slot in A', B'
        for c, T in terms:
            for X in (0, 1):
                acc = np.zeros(len(vs))
                rp = np.zeros(len(vs))
                nzA = np.zeros(len(vs))
                nzB = np.zeros(len(vs))
                for x in T[X]:
                    w = vs + x
                    rp += np.abs(w) / 2.0
                    ok = (w >= -VG) & (w <= VG)
                    for tgt in (0, 1):
                        sel = (w != 0) & (np.where(w < 0, X, 1 - X) == tgt)
                        idx = np.clip(w + VG, 0, 2 * VG)
                        acc += np.where(sel & ok, prev[tgt][idx], 0.0)
                        acc += np.where(sel & ~ok, np.nan, 0.0)
                        if tgt == 0:
                            nzA += sel
                        else:
                            nzB += sel
                acc += (rp - nzA) * z[0] + (rp - nzB) * z[1]
                new[X] += c * acc
        phi.append(new)
    return phi


def lp_sup(objA, objB, zA, zB):
    """max over valid simples (r = 1) of sum n_X(v) obj_X(v) + z_A zA + z_B zB.
    Columns: (X, v), v != 0 in the LP set.  z_A = r - sum_v n_A(v), r = 1/2 sum |v| n."""
    cols = [v for v in range(-VLP, VLP + 1) if v != 0] + FAR + [-f for f in FAR]
    c, Aeq, Aub0, Aub1 = [], [], [], []
    for X in (0, 1):
        for v in cols:
            o = (objA if X == 0 else objB)[v + VG]
            # contribution through the zero counts: z_A gets |v|/2 - [X==A], z_B gets |v|/2 - [X==B]
            gzA = abs(v) / 2 - (1 if X == 0 else 0)
            gzB = abs(v) / 2 - (1 if X == 1 else 0)
            c.append(-(o + gzA * zA + gzB * zB))
            Aeq.append(abs(v) / 2)
            Aub0.append(-gzA)
            Aub1.append(-gzB)
    for X in (0, 1):
        o = objA if X == 0 else objB
        for sgn in (1, -1):
            v1, v2 = sgn * 2000, sgn * 2400
            slope = (o[v2 + VG] - o[v1 + VG]) / (v2 - v1)
            v3 = sgn * 2200
            assert abs(o[v3 + VG] - (o[v1 + VG] + slope * (v3 - v1))) <= 1e-9 * max(1.0, abs(o[v3 + VG]))
            for vf in XFAR:
                v = sgn * vf
                ov = o[v2 + VG] + slope * (v - v2)
                gzA = abs(v) / 2 - (1 if X == 0 else 0)
                gzB = abs(v) / 2 - (1 if X == 1 else 0)
                c.append(-(ov + gzA * zA + gzB * zB))
                Aeq.append(abs(v) / 2)
                Aub0.append(-gzA)
                Aub1.append(-gzB)
    res = linprog(c, A_ub=np.array([Aub0, Aub1]), b_ub=[0, 0], A_eq=np.array([Aeq]), b_eq=[1],
                  bounds=(0, None), method="highs")
    return -res.fun


def growth(terms, M):
    phi = adjoint(terms, M)
    out = []
    for m in range(1, M + 1):
        P = phi[m]
        assert not np.isnan(P[:, VG - 3000:VG + 3001]).any()
        out.append(lp_sup(P[0], P[1], P[0][VG], P[1][VG]))
    return out


# Lemma B1 by LP: for each term and child fibre, min over valid parents of the child's refill
def refill_min(terms):
    worst = math.inf
    vs = np.arange(-VG, VG + 1)
    for _, T in terms:
        for tgt in (0, 1):
            obj = []
            for X in (0, 1):
                rp = np.zeros(len(vs))
                nz = np.zeros(len(vs))
                for x in T[X]:
                    w = vs + x
                    rp += np.abs(w) / 2
                    nz += (w != 0) & (np.where(w < 0, X, 1 - X) == tgt)
                obj.append(rp - nz)
            # minimise refill = -(max of -refill)
            val = -lp_sup(-obj[0], -obj[1], -obj[0][VG], -obj[1][VG])
            worst = min(worst, val)
    return worst


print("(B) Lemma B1 by LP (min child refill per unit parent rank over valid simples, |v| <= 150 + far):"
      f" seed {refill_min(seed):.3e}, h_1 {refill_min(h1):.3e}  (>= 0 expected)")
M = 12
gS = growth(seed, M)
gJ = growth(seed + h1, M)
rep_S = {1: 0.699581, 2: 0.370632, 4: 0.099749, 8: 0.006436, 12: 0.000403}
rep_J = {1: 0.829417, 2: 0.544535, 4: 0.217293, 8: 0.031128, 12: 0.004348}
print("    m   G_m(seed) LP   report    G_m(joint) LP   report")
for m in range(1, M + 1):
    print(f"   {m:2d}   {gS[m-1]:.6f}   {rep_S.get(m, float('nan')):.6f}   {gJ[m-1]:.6f}   {rep_J.get(m, float('nan')):.6f}")
gH1 = growth(h1, 1)[0]
print(f"    h_1 alone, one step: {gH1:.6f} (= beta_1 {beta1:.6f})")


# ---------------------------------------------------------------- (C) Duhamel budgets and allowances
def gsum(G):
    Gd = [1.0] + G
    head = sum(Gd)
    GM = Gd[-1]
    return head + GM / (1 - GM) * sum(Gd[1:])


Nq = 4 * (2031 / 128 - 2 ** -17)
SQN = math.sqrt(Nq)
S_UP = 2.828428539
P0, M0 = 0.01272, 4.823


def cM(Mv):
    x = Mv * Mv / Nq
    return 2 / SQN * (1 + x / 2) * (1 - x) ** -2.5


us = np.linspace(0.05, 0.35, 300001)
one_minus_kappa = min(P0 / u + cM(M0 + u) * u / 2 for u in us[::100])
uu = us[np.argmin([P0 / u + cM(M0 + u) * u / 2 for u in us[::100]]) * 100]
one_minus_kappa = min(P0 / u + cM(M0 + u) * u / 2 for u in np.linspace(uu - 1e-3, uu + 1e-3, 20001))
kappa = 1 - one_minus_kappa


def Gall(y):
    return y * (2 * Nq - y * y) / (Nq - y * y) ** 1.5


def Gall_d(y):
    return Nq * (2 * Nq + y * y) / (Nq - y * y) ** 2.5


def H(A):
    return Gall(S_UP + A) - Gall(S_UP) - A * Gall_d(S_UP)


rho0 = 2.175646
tauS, tau1 = 0.000386100, 0.000003134
A1 = 0.494530


def allow(g, fixed, Afix):
    budget = 1 / g - (1 - kappa)
    lo, hi = 0.0, 3.0
    if fixed + H(Afix) >= budget:
        return None, budget
    for _ in range(60):
        mid = (lo + hi) / 2
        if fixed + rho0 * mid / SQN + H(Afix + mid) < budget:
            lo = mid
        else:
            hi = mid
    return lo, budget


g_S, g_J = gsum(gS), gsum(gJ)
print(f"(C) kappa*_A = {kappa:.8f} (report [0.83790250, 0.83793100]); 1/(1-kappa) = {1/(1-kappa):.5f}")
print(f"    H(0.55) = {H(0.55):.5f}, H(1) = {H(1):.5f}, H(1.994573) = {H(1.994573):.5f}  (Round 183: 0.01932 / 0.07243 / 0.40151)")
print(f"    g_S = {g_S:.6f} (report <= 2.467879), g_J = {g_J:.6f} (report <= 3.290671)")
Xa, bS = allow(g_S, tauS, 0.0)
Xb, _ = allow(g_S, tauS + beta1 + tau1, A1)
Xc, bJ = allow(g_J, tauS + tau1, A1)
print(f"    budgets: seed {bS:.5f} (report 0.24310), joint {bJ:.5f} (report 0.14179)")
print(f"    (a) A(h) < {Xa:.4f} (report 0.7499);  (b) A(h-h_1) < {Xb:.4f} (report 0.2689);"
      f"  (c) A(h-h_1) < {Xc:.4f} (report 0.3411)")
# power form (Round 183 setting) for comparison
lamS8 = gS[7] ** (1 / 8)
CS8 = max([1.0] + [gS[j - 1] / lamS8 ** j for j in range(1, 8)])
print(f"    power form m0=8: lam_S = {lamS8:.5f} (report 0.53220), C_S = {CS8:.4f} (report 1.3146), "
      f"beta_max = (1-lam)/C - (1-kappa) = {(1-lamS8)/CS8 - (1-kappa):.5f} (Round 183: 0.19359)")
print("AUDIT COLD CHECK DONE (float; certifies nothing)")
