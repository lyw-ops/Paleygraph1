#!/usr/bin/env python3
r"""Round 186 audit (session/r186-audit): independent checks of the cold report
research/native-claude-cold-prime-hybrid-price-186.md.

Written by the auditor; it does not import or copy the report's scripts.

Part 1  EXACT (integers): Lemma 1 (sum_j lambda_j = -1, unique zero, lambda_{n-j} = lambda_j)
        for all p = 1 mod 4, 5 <= p < 3000, with the Legendre symbol by Euler's criterion.
Part 2  FLOAT (numpy FFT, evidence-grade): kappa = K e_0 from the eigenvalues, S = 2 sqrt(n) kappa;
        sum S^2 = 4(n-1), S_0 = -2/sqrt n; Lemma 2 (sum|kappa| >= 2(n-1)/(s_p sqrt n));
        Theorem N's aligned multiplier g_x = gamma sgn(kappa(x0-x) S_x) evaluated directly at
        every x0, compared with c_N(gamma, n) computed with the actual s_p = max|S| and b0 = 3;
        Lemma 3's aligned sign vector for L_S.
Part 3  EXACT (Fractions / Decimal with 50 digits): Proposition 5 fractions, Corollary 6 window,
        the Section 5 remark arithmetic, and the small-n threshold remark ((I1) range).

Phi_a'(y) = y / sqrt(4a + y^2) on the real principal sheet at t = a = 2031/128, as stated in the
report (Theorem N, step 1).  Prints ALL AUDIT CHECKS OK at the end.
"""
import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

import numpy as np

OK = True


def check(cond, msg):
    global OK
    print(("ok   " if cond else "FAIL ") + msg)
    OK = OK and bool(cond)


def is_prime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True


def prim_root(p):
    fac = [q for q in range(2, p) if (p - 1) % q == 0 and is_prime(q)]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


def chi(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


# --------------------------------------------------------------------- Part 1
print("== 1. Lemma 1 exact ==")
good = True
cnt = 0
for p in range(5, 3000):
    if p % 4 != 1 or not is_prime(p):
        continue
    n = (p - 1) // 2
    g = prim_root(p)
    lam = [chi(1 - pow(g, 2 * j, p), p) for j in range(n)]
    good &= sum(lam) == -1 and lam[0] == 0 and all(l != 0 for l in lam[1:])
    good &= all(lam[j] == lam[(n - j) % n] for j in range(n))
    cnt += 1
check(good, f"sum lambda = -1, unique zero at j=0, lambda_(n-j) = lambda_j for all {cnt} primes p = 1 mod 4 < 3000")

# --------------------------------------------------------------------- Part 2
print("== 2. Theorem N, Lemmas 2-3 at moderate p (float) ==")
a = 2031 / 128


def phi1(y):
    return y / np.sqrt(4 * a + y * y)


def phi2(y):
    return 4 * a / (4 * a + y * y) ** 1.5


for p in (10009, 100049, 400009):
    if not is_prime(p) or p % 4 != 1:
        continue
    n = (p - 1) // 2
    g = prim_root(p)
    # Legendre table by squares
    leg = -np.ones(p, dtype=np.int64)
    leg[0] = 0
    leg[(np.arange(1, p, dtype=np.int64) ** 2) % p] = 1
    pw = np.empty(n, dtype=np.int64)
    x = 1
    g2 = g * g % p
    for j in range(n):
        pw[j] = x
        x = x * g2 % p
    lam = leg[(1 - pw) % p].astype(float)
    kappa = np.real(np.fft.ifft(lam))          # kappa(x) = (1/n) sum_j lam_j e^{2 pi i j x/n}
    S = 2 * math.sqrt(n) * kappa
    sp = float(np.max(np.abs(S)))
    check(abs(lam.sum() + 1) < 1e-9 and abs(S[0] * math.sqrt(n) + 2) < 1e-6
          and abs((S ** 2).sum() / (4 * (n - 1)) - 1) < 1e-9,
          f"p={p}: sum S^2 = 4(n-1), sqrt(n) S_0 = -2; s_p = max|S| = {sp:.6f}")
    sk = np.abs(kappa).sum()
    check(sk >= 2 * (n - 1) / (sp * math.sqrt(n)) * (1 - 1e-12),
          f"p={p}: ||K||_(inf->inf) = sum|kappa| = {sk:.2f} >= 2(n-1)/(s_p sqrt n) = {2*(n-1)/(sp*math.sqrt(n)):.2f}")
    # W(x0) = sum_{x != 0} |kappa(x0 - x)| |S_x| for all x0 (circular correlation by FFT)
    absS = np.abs(S).copy()
    absS[0] = 0.0
    W = np.real(np.fft.ifft(np.fft.fft(np.abs(kappa)) * np.fft.fft(absS)))
    x0 = int(np.argmax(W[1:])) + 1
    for gam in (0.1749, 0.61):
        # aligned multiplier for row x0: g_x = gam sgn(kappa(x0-x) S_x), g_0 = 0
        idx = (x0 - np.arange(n)) % n
        sg = np.sign(kappa[idx] * S)
        sg[sg == 0] = 1
        gg = gam * sg
        gg[0] = 0.0
        val = float(np.sum(kappa[idx] * (phi1(S + gg) - phi1(S)) * S))
        mpp = 4 * a / (4 * a + (sp + gam) ** 2) ** 1.5
        cN = gam * mpp * (8 * (n - 1) * (n - 1 - 1 / n) / (sp ** 2 * n ** 1.5) - 2 * 3 * math.sqrt(n - 1) / n) / sp
        check(val / sp >= cN and val >= gam * mpp * W[x0] * (1 - 1e-9),
              f"p={p}, gamma={gam}: aligned (B_g S)(x0)/s_p = {val/sp:.3f} >= c_N = {cN:.3f}; "
              f"/sqrt(n) = {val/math.sqrt(n):.4f}")
    # Lemma 3: aligned sign vector for L_S
    idx = (x0 - np.arange(n)) % n
    f = np.sign(kappa[idx] * phi1(S))
    f[0] = 0.0
    vL = float(np.sum(kappa[idx] * phi1(S) * f))
    cLS = 8 * (n - 1) * (n - 1 - 1 / n) / (sp ** 2 * n ** 1.5 * math.sqrt(4 * a + sp ** 2)) - 2 * 3 * math.sqrt(n - 1) / n
    check(vL >= cLS, f"p={p}: Lemma 3 (L_S f)(x0) = {vL:.3f} >= c_LS = {cLS:.3f}, ||f||_inf = 1")

# --------------------------------------------------------------------- Part 3
print("== 3. exact arithmetic ==")
getcontext().prec = 50
D = Decimal
for q, lo, hi in ((D("0.5145"), D("0.08736"), D("0.08737")), (D("0.518"), D("0.07795"), D("0.07796")),
                  (D("0.535"), D("0.03035"), D("0.03036")), (D("0.545"), D("0.00076"), D("0.00077"))):
    theta = 1 / (2 * ((1 / q).ln() / D(2).ln()))
    frac = 1 - theta * D(7) / D(4)
    check(lo <= frac <= hi, f"Prop. 5: q = {q}: theta = {theta:.6f}, usable fraction {frac:.6f} in [{lo},{hi}]")
check(F(545, 1000) ** 8 < F(1, 128) and F(545, 1000) ** 8 > F(1, 128) - F(1, 10 ** 4), "0.545^8 < 2^-7, margin < 1e-4")
w = (D(3) / 8 - D(1) / 8) * (1 - D("0.545")) / D("9.07e-209")
check(abs(w.log10() - D("207.098")) < D("0.0005"), f"Cor. 6 window: sqrt n < 10^{w.log10():.4f}, n < 10^{2*w.log10():.3f}")
# Section 5 remark (|sqrt t| at t = a; the report's floor 1.91541 and budget 0.24310 are inherited inputs)
rt = D(2031) / D(128)
rt = rt.sqrt()
v = D("1.91541") * D("0.912537") / (2 * rt)
check(D("0.219397") <= v <= D("0.219400"), f"floor*A(h)/(2|sqrt t|) at t = a: {v:.6f} (report >= 0.219397; t in Q may shift the 6th digit)")
ceil = D("0.24310") * 2 * rt / D("1.91541")
check(abs(ceil - D("1.011122")) < D("0.00001"), f"optimistic ceiling A(h) < {ceil:.6f}")
# (I1) range remark: s = 2.828428539 is stated for p >= 1e6; at p = 10009 the actual s_p is larger
check(2.828568 > 2.828428539, "NOTE: Cor. N2 thresholds (n >= 151 etc.) use s = 2.828428539, stated only for p >= 1e6; "
      "the conclusion for p >= 1e6 (c_N(0.61) >= 14.8) is unaffected")

print("ALL AUDIT CHECKS OK" if OK else "SOME AUDIT CHECK FAILED")
sys.exit(0 if OK else 1)
