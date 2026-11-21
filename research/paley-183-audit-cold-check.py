#!/usr/bin/env python3
"""Round 183 audit: independent checks for the cold seed-multiplier report
(research/native-claude-cold-prime-seed-multiplier-power-rate-183.md).

Written by the Round 183 auditor without reusing the report's code.  This is a
floating-point replay (numpy/scipy float64, labelled as such), except where it
says 'exact' (Fractions).  It checks the report's exact numbers; it certifies nothing.

C1  Fourier coefficients ghat_k(beta0) of g(theta) = cos(theta)(1+beta0 cos^2 theta)^(-1/2)
    (FFT, 2^16 points) against the report's exact brackets; the l^1 identity
    sum_k |bhat_k| = 1 for (1+beta0 cos^2)^(-3/2); rho_0 = sum (|k|+2)|bhat_k|.
C2  G_m(alpha) for the full seed multiplier M = sum_{|k|<=5} gamma_k M_k (Round 80 rule with J^k:
    fibre A shifted by -k, fibre B by +k; negatives stay, positives move to the other fibre;
    zeros refilled to r' = sum|s|/2), as a Charnes-Cooper LP over slot-count vectors with
    parent values |v| <= V (truncation from below), m = 1, 2, 3; plus the explicit family
    A = (-K, 0^(K/2-1)), B = (0^(K/2)) with K -> infinity (exact Fractions).
C3  Threshold kappa*_alpha = 1 - (1+alpha) inf_{0<u<=3/8} [p0/u + c(M0+u) u / 2] in the
    report's normalisation: sup_u [1 - fac p0/u - fcc c(M0+u) u], c(M) = 2(1+x/2)/(sqrt N (1-x)^(5/2)),
    x = M^2/N; fac = fcc = 1 (reading b1), fac = 1+alpha, fcc = (1+alpha)/2 (reading b1*).
C4  beta_max, the h-linear allowance X = beta_max sqrt N and A_max, recomputed from the
    report's (lam_S, C_S) and the closed-form H(A); and lam_S, C_S recomputed from the
    report's printed G_m values.

Replay: .venv/bin/python -B research/paley-183-audit-cold-check.py   (needs numpy, scipy)
"""
from fractions import Fraction as Fr
import math

import numpy as np
from scipy.optimize import linprog

A_CTR = 2031 / 128
N = 4 * (A_CTR - 2 ** -17)
SQN = math.sqrt(N)
BETA0 = 256 / 2031
VARPI = 0.355030238
GAMMA = {1: 0.478072561593, 3: 0.007039589281, 5: 0.000156385050}

# ------------------------------------------------------------------ C1
def c1():
    T = 2 ** 16
    th = 2 * np.pi * np.arange(T) / T
    gv = np.cos(th) / np.sqrt(1 + BETA0 * np.cos(th) ** 2)
    gh = np.fft.fft(gv) / T
    rep = {1: (0.478072428819, 0.478072428820), 3: (-0.007039456508, -0.007039456507),
           5: (0.000156252275, 0.000156252276), 7: (-0.000003858441, -0.000003858440),
           9: (0.000000100092, 0.000000100093)}
    for k, (lo, hi) in rep.items():
        v = gh[k].real
        assert lo - 1e-14 <= v <= hi + 1e-14, (k, v)
        assert abs(gh[-k].real - v) < 1e-15
    l1 = np.abs(gh.real).sum()
    bv = (1 + BETA0 * np.cos(th) ** 2) ** -1.5
    bh = np.fft.fft(bv).real / T
    kk = np.fft.fftfreq(T, 1 / T)
    rho0 = ((np.abs(kk) + 2) * np.abs(bh)).sum()
    print(f"C1 [float] ghat_k(beta0), k=1..9, inside the report's exact brackets; sum|ghat_k| = {l1:.12f}; "
          f"sum|bhat_k| = {np.abs(bh).sum():.12f}; rho_0(beta0) = {rho0:.6f} (report: <= 2.17565 uniformly), "
          f"rho_0/sqrt N = {rho0 / SQN:.9f}")
    return gh


# ------------------------------------------------------------------ C2
def child_map(fib, v, k):
    """slot (fib, v) under J^k: returns (fib', v') or None (value 0, absorbed into refill)."""
    s = v - k if fib == 0 else v + k
    if s == 0:
        return None
    if s < 0:
        return (fib, s)
    return (1 - fib, s)


def step(vec, ks):
    """vec: dict (fib, v) -> coefficient vector (np array over LP variables); apply M once."""
    out = {}
    for k, gam in ks:
        part = {}
        rr = 0
        nz = [0, 0]
        for (fib, v), coef in vec.items():
            s = v - k if fib == 0 else v + k
            rr = rr + abs(s) * coef / 2
            t = child_map(fib, v, k)
            if t is None:
                continue
            part[t] = part.get(t, 0) + coef
            nz[t[0]] = nz[t[0]] + coef
        part[(0, 0)] = part.get((0, 0), 0) + (rr - nz[0])
        part[(1, 0)] = part.get((1, 0), 0) + (rr - nz[1])
        for key, cf in part.items():
            out[key] = out.get(key, 0) + gam * cf
    return out


def price(vec, alpha):
    r = sum(abs(v) * cf / 2 for (f, v), cf in vec.items())
    z = vec.get((0, 0), 0) + vec.get((1, 0), 0)
    return r + alpha * z / 2


BIG = ()


def lp_G(m, alpha, V):
    ks = [(k, g) for kk, g in GAMMA.items() for k in (kk, -kk)]
    vals = list(range(-V, V + 1)) + [s * L for L in BIG for s in (1, -1)]
    keys = [(f, v) for f in (0, 1) for v in vals]
    nv = len(keys)
    vec = {key: np.eye(nv)[i] for i, key in enumerate(keys)}
    cur = vec
    for _ in range(m):
        cur = step(cur, ks)
    num = price(cur, alpha)
    den = price(vec, alpha)
    rvec = sum(abs(v) * vec[(f, v)] / 2 for (f, v) in keys)
    Aeq = [den]
    for f in (0, 1):
        Aeq.append(sum(vec[(f, v)] for v in vals) - rvec)
    res = linprog(-num, A_eq=np.array(Aeq), b_eq=[1, 0, 0], bounds=[(0, None)] * nv, method="highs")
    assert res.status == 0
    return -res.fun


def family_ratio(K, alpha, m):
    """exact ratio for A = (-K, 0^(K/2-1)), B = (0^(K/2)), m steps, weights GAMMA as Fractions."""
    gam = {k: Fr(str(g)) for k, g in GAMMA.items()}
    ks = [(k, g) for kk, g in gam.items() for k in (kk, -kk)]
    vec = {(0, -K): Fr(1), (0, 0): Fr(K // 2 - 1), (1, 0): Fr(K // 2)}
    cur = vec
    for _ in range(m):
        cur = step(cur, ks)
    return price(cur, Fr(alpha)) / price(vec, Fr(alpha))


def c2():
    rep = {(0, 1): 1.970484, (0, 2): 2.940449, (0, 3): 4.374161,
           (0.5, 1): 1.646972, (0.5, 2): 2.455376, (0.5, 3): 3.575284,
           (1, 1): 1.507429, (1, 2): 2.212839, (1, 3): 3.175845}
    for (alpha, m), G in rep.items():
        global BIG
        BIG = ()
        vals = [lp_G(m, alpha, V) for V in (20, 60)]
        BIG = (10 ** 4, 10 ** 6)
        big = lp_G(m, alpha, 60)
        fam = float(family_ratio(20000, alpha, m))
        assert max(vals + [big]) <= G + 1e-6, (alpha, m, vals, big)
        print(f"C2 [float LP] alpha={alpha} m={m}: LP(|v|<=20) = {vals[0]:.6f}, LP(|v|<=60) = {vals[1]:.6f}, "
              f"LP(|v|<=60 plus |v|=1e4,1e6) = {big:.6f}, family K=20000 (exact) = {fam:.6f}; "
              f"report exact sup {G:.6f}")


# ------------------------------------------------------------------ C3
def cM(M):
    x = M * M / N
    return 2 * (1 + x / 2) / (SQN * (1 - x) ** 2.5)


def kstar(fac, fcc, p0=0.01272, M0=4.823):
    us = np.linspace(1e-4, 3 / 8, 200001)
    vals = 1 - fac * p0 / us - fcc * np.array([cM(M0 + u) for u in us]) * us
    i = int(np.argmax(vals))
    lo, hi = us[max(i - 2, 0)], us[min(i + 2, len(us) - 1)]
    for _ in range(200):  # golden section
        a = lo + (hi - lo) * 0.381966
        b = lo + (hi - lo) * 0.618034
        fa = 1 - fac * p0 / a - fcc * cM(M0 + a) * a
        fb = 1 - fac * p0 / b - fcc * cM(M0 + b) * b
        if fa < fb:
            lo = a
        else:
            hi = b
    u = (lo + hi) / 2
    return 1 - fac * p0 / u - fcc * cM(M0 + u) * u, u


def c3():
    kb1, u1 = kstar(1, 1)
    print(f"C3 [float] reading b1: kappa* = {kb1:.10f} (report [0.77414706, 0.77414708]) at u = {u1:.5f}")
    assert 0.77414706 <= kb1 <= 0.77414708
    rep = {0: (0.83790251, 0.83790253), 0.25: (0.79737814, 0.79737816),
           0.5: (0.75685377, 0.75685379), 1: (0.67580502, 0.67580504)}
    out = {}
    for al, (lo, hi) in rep.items():
        k, u = kstar(1 + al, (1 + al) / 2)
        assert lo <= k <= hi, (al, k)
        out[al] = k
        print(f"C3 [float] reading b1*, alpha={al}: kappa* = {k:.10f} (report [{lo}, {hi}]), u = {u:.5f}")
    return kb1, out


# ------------------------------------------------------------------ C4
def Gall(y):
    return y * (2 * N - y * y) / (N - y * y) ** 1.5


def Gall_d(y):
    return N * (2 * N + y * y) / (N - y * y) ** 2.5


def H(A, s=2.828428539):
    return Gall(s + A) - Gall(s) - A * Gall_d(s)


def c4(kb1, kb1s):
    SIGH = 0.273091676
    rows = [("A, b1*, m0=8", 0, 0.53244, 1.3146, kb1s[0], 0.6179, 0.19359),
            ("pi1, b1*, m0=3", 1, 0.52224, 1.0256, kb1s[1], 0.2462, 0.14167),
            ("pi1, b1, m0=3", 1, 0.52224, 1.0256, kb1, 0.4029, 0.24001),
            ("pi1, b1, m0=1", 1, 0.53556, 1.0, kb1, 0.4007, 0.23859)]
    for name, al, lam, C, kap, amax_rep, bmax_rep in rows:
        bmax = (1 - lam) / C - (1 - kap)
        lo, hi = 0.0, 2.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if (1 + al) * (mid * SIGH + H(mid)) < bmax:
                lo = mid
            else:
                hi = mid
        print(f"C4 [float] {name}: beta_max = {bmax:.5f} (report >= {bmax_rep}); allowance X = beta_max*sqrt N = "
              f"{bmax * SQN:.4f}; A_max = {lo:.4f} (report lower end {amax_rep})")
        assert abs(bmax - bmax_rep) < 1e-4 and abs(lo - amax_rep) < 1e-3  # inputs are the report's rounded-up lam_S, C_S
    print(f"C4 [float] H(0.55) = {H(0.55):.5f}, H(1) = {H(1.0):.5f}, H(1.994573) = {H(1.994573):.5f}")
    # power forms from the report's printed G_m (alpha = 0, all m <= 8; alpha = 1, m <= 3)
    G0 = [1.970484, 2.940449, 4.374161, 6.278417, 8.992638, 12.751861, 18.062170, 25.495420]
    G1 = [1.507429, 2.212839, 3.175845]
    for name, Gs, m0 in (("alpha=0", G0, 8), ("alpha=1", G1, 3), ("alpha=1", G1, 1)):
        lamhat = Gs[m0 - 1] ** (1 / m0)
        C = max([1.0] + [Gs[r - 1] / lamhat ** r for r in range(1, m0)])
        print(f"C4 [float] {name} m0={m0}: lam_hat*varpi = {lamhat * VARPI:.5f}, C_S = {C:.4f} "
              f"(report lam_S incl. |k|>=7 tail, C_S)")


if __name__ == "__main__":
    c1()
    c2()
    kb1, kb1s = c3()
    c4(kb1, kb1s)
    print("ALL COLD AUDIT CHECKS DONE")
