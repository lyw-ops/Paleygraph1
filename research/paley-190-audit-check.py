#!/usr/bin/env python3
"""Round 190 audit (session/r190-audit): independent checks for the three Round 190 reports.

Part A  exact Fractions: MPRRS Theorem 37 internal constraints at |A| ~ sqrt p (including the
        second condition of Lemma 33 and the logarithm power hidden in the tilde), the 45/26
        translation, the stocktake's ranking and J-class arithmetic, the slope-band loss of the
        first-mass composition, and the NC exponents.
Part B  Lemma 1 of the NC report rebuilt from Round 20's explicit formula L = P - l l^T / l_0
        (P an orthogonal projection, 2P = I - J - rho K in the Round 151 / 183 convention
        I - rho K = 2 P_sigma + J), compared with V_{-rho}; sign sanity check on a law
        concentrated on T_rho.  Floating point, p <= 109.
Part C  the diluted-interval laws D_theta built independently: energy ratio, maximal overlap,
        min g on I I^{-1} against 4/pi^2, coset counts, and T_0 >= (4/pi^2)^5 X(1_I) through a
        brute-force Round 189 chart (mu(r,b) = g(Y) g(D), Delta(lambda,0) = sum mu(r,b) mu(lambda r,b)).
        Floating point evidence at p ~ 10^3.
Part D  geometric-progression sector runs R(zeta) by plain-Python brute force at a few primes,
        compared with the values printed by research/paley-190-nc-gpclique.py.

Usage: .venv/bin/python -B research/paley-190-audit-check.py
"""
from fractions import Fraction as F
import math
import numpy as np

ok = True


def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok &= bool(cond)


# ---------------------------------------------------------------- Part A
print("== Part A: exact exponent arithmetic")
h = F(1, 2)
# Theorem 34 with D1 = M^5 log|A|, D2 = M^(3/2): output M^(33/13) |A|^(32/13) log^(6/13 + 12/13)
check("Thm 37: M power 5*6/13 + (3/2)*2/13 = 33/13", 5 * F(6, 13) + F(3, 2) * F(2, 13) == F(33, 13))
check("Thm 37: hidden log power 6/13 + 12/13 = 18/13", F(6, 13) + F(12, 13) == F(18, 13))
# wlog bound |B| <= 4|A|^4 / E with E >= 4 M^(33/13)|A|^(32/13): |B| <= |A|^(20/13) M^(-33/13)
check("Thm 37: |B| exponent 4 - 32/13 = 20/13", 4 - F(32, 13) == F(20, 13))
# Lemma 33 first condition M|A|^2|B| <= p^2  <=>  |A|^(46/13) M^(-20/13) <= p^2  <=>  |A| <= p^(13/23) M^(10/23)
check("Thm 37: 2 + 20/13 = 46/13 and 1 - 33/13 = -20/13", 2 + F(20, 13) == F(46, 13) and 1 - F(33, 13) == F(-20, 13))
check("Thm 37: (46/13)^(-1)*2 = 13/23 and (20/13)/(46/13) = 10/23", 2 / F(46, 13) == F(13, 23) and F(20, 13) / F(46, 13) == F(10, 23))
# Lemma 33 second condition max(|AA|,|B|) <= (|A||AA||B|)^(1/2): with |AA| = M|A| it reads M <= |B| <= M|A|^2.
# Upper end: |B| <= |A|^(20/13) <= |A|^2.  Lower end |B| < M: trivial E(A+a,B) <= |A||B|^2 <= M^(1/2)|A||B|^(3/2).
check("Lemma 33 cond 2 (upper): 20/13 <= 2", F(20, 13) <= 2)
# Lemma 32: |AA| <= p^(2/3); at |A| = p^(1/2), M = O(1)
check("Lemma 32 at |A| ~ p^(1/2): 1/2 < 2/3", h < F(2, 3))
check("size: 1/2 < 13/23", h < F(13, 23))
# constraint remark in the proof: new bound beats Lemma 33 iff M < |A|^(1/27): (33/13 - 3/2) = 27/26 vs 1/26
check("Thm 37 vs Lemma 33: 33/13 - 3/2 = 27/26, ratio (1/26)/(27/26) = 1/27", F(33, 13) - F(3, 2) == F(27, 26))
e37p = F(32, 13) * h
check("p-exponent 16/13 = 5/4 - 1/52", e37p == F(5, 4) - F(1, 52))
check("covariance 1/2 + 16/13 = 45/26 = 7/4 - 1/52", h + e37p == F(45, 26) == F(7, 4) - F(1, 52))
check("45/26 < 7/4 and 45/26 < 43/24 (cap moves below 43/24)", F(45, 26) < F(7, 4) and F(45, 26) < F(43, 24))
check("16/13 < 31/24 by 1/312", F(31, 24) - F(16, 13) == F(19, 312))
# gap of (GP) to its own target |I|^2: 32/13 - 2 = 6/13 (3/13 in p)
check("GP gap 6/13 in |I|, 3/13 in p", F(32, 13) - 2 == F(6, 13) and (F(32, 13) - 2) * h == F(3, 13))
# Stocktake ranking (first-moment units: covariance 3/2 + d  <->  first moment 1 + d/2)
fm = lambda cov: 1 + (cov - F(3, 2)) / 2
check("one-match 43/24 -> fm gap 7/48", fm(F(43, 24)) - 1 == F(7, 48))
check("diagonal 9/4 -> fm gap 3/8", fm(F(9, 4)) - 1 == F(3, 8))
check("first mass gap 1/3 < 3/8 by 1/24", F(3, 8) - F(1, 3) == F(1, 24))
check("M_w via C-S on R179 diagonal: 1/4 + 9/8 = 11/8", F(1, 4) + F(9, 8) == F(11, 8))
check("J classes 0,1: 1/2 - 1/1280 + 4/3 = 7037/3840", h - F(1, 1280) + F(4, 3) == F(7037, 3840))
check("J classes 0,1 recorded: 1/2 - 1/1280 + 11/8 = 2399/1280", h - F(1, 1280) + F(11, 8) == F(2399, 1280))
check("per-class D_J: 1/2 + 4/3 = 11/6", h + F(4, 3) == F(11, 6))
check("7037/3840 > 3/2 (J classes 0,1 still open)", F(7037, 3840) > F(3, 2))
# Composition B1 on a slope band g ~ p^(-s): |f| ~ p^(-s/2), w ~ p^(-s): sum |f| P <= p^(s/2) M_w
for s in (F(1, 4), F(1, 2), F(3, 4)):
    check(f"band g~p^-{s}: loss exponent -s/2 + s = s/2 = {s/2}", -s / 2 + s == s / 2)
# Low bands already paid at sigma >= 1 - 2 gamma (R164) with gamma <= 1/54: the open sigma range is (0, 1-2gamma)
check("open band range reaches sigma = 1 - 1/27 at gamma = 1/54", 1 - 2 * F(1, 54) == F(26, 27))
# NC: Criterion 5.2 with Thm 37 instead of Lemma 33: obstruction removed for delta < 5 kappa below 16/13
check("NC Cor 4.1(i) threshold with Thm 37: 16/13", e37p == F(16, 13))

# ---------------------------------------------------------------- helpers
def prim_root(p):
    fac, m, d = [], p - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


def legendre(p):
    chi = np.full(p, -1, dtype=np.int64)
    chi[(np.arange(1, p, dtype=np.int64) ** 2) % p] = 1
    chi[0] = 0
    return chi


# ---------------------------------------------------------------- Part B
print("== Part B: Lemma 1 from Round 20's L = P - l l^T / l_0")
rng = np.random.default_rng(190)
worst = 0.0
for p in (13, 29, 37, 53, 61, 101, 109):
    n = (p - 1) // 2
    g0 = prim_root(p)
    g2 = g0 * g0 % p
    xs = [pow(g2, k, p) for k in range(n)]
    chi = legendre(p)
    s = np.array([chi[(1 - x) % p] for x in xs], dtype=float)  # s(x) = chi(1-x), s(1) = 0
    # character matrix Psi[j,k] = psi^j(gamma^{2k}) = e(jk/n); transform vhat = Psi^T v
    jj = np.arange(n)
    Psi = np.exp(2j * np.pi * np.outer(jj, jj) / n)
    # K = (1/n) Psi diag(s) Psi^*  (multiplication by s in x-space), built from k(i-j)
    K = (Psi @ np.diag(s) @ Psi.conj().T) / n
    K = K.real
    I = np.eye(n)
    J = np.ones((n, n)) / n
    for rho in (1, -1):
        P = (I - J - rho * K) / 2           # I - rho K = 2P + J
        assert np.allclose(P, P.T) and np.allclose(P @ P, P)
        e0 = np.zeros(n); e0[0] = 1
        l = P @ e0
        L = P - np.outer(l, l) / l[0]       # Round 20 formula
        assert np.allclose(L @ L, L)
        for _ in range(4):
            b = rng.random(n); b[0] = 0
            r = b.mean()
            nu = b / b.sum()
            f = Psi.T @ nu                   # f(x_k) = sum_j nu_j e(jk/n)
            T = (s == -rho)
            V = np.sum(np.abs(f[T] - f[T].mean()) ** 2)
            lhs = np.sum((L @ b) ** 2) / n / r ** 2
            Gm = np.sum(np.abs(f[T]) ** 2)
            lhsP = np.sum((P @ b) ** 2) / n / r ** 2
            worst = max(worst, abs(lhs - V) / max(V, 1e-300), abs(lhsP - Gm) / Gm)
            assert abs(np.sum(f[T])) <= (math.sqrt(p) + 1) / 2 + 1e-9
        # sign sanity: nu concentrated where f lives on T_rho gives small ||L b||; build b from g on T_rho
        T_rho = (s == rho)
        # law nu proportional to the transform of a nonnegative function on {1} U T_rho is not a law in general;
        # instead check the multiplier: the projection kills T_rho and x=1, keeps T_{-rho}
        mult = (Psi.T @ P @ Psi.conj()) / n
        d = np.real(np.diag(mult))
        assert np.allclose(d[T_rho], 0) and np.allclose(d[s == -rho], 1) and abs(d[0]) < 1e-9
check(f"Lemma 1: ||L b||^2/r^2 = V_(-rho) and ||P b||^2/r^2 = G_(-rho), max rel err {worst:.1e}", worst < 1e-10)
check("P_sigma is the Fourier projection onto T_(-rho) (kills x = 1 and T_rho)", True)


# ---------------------------------------------------------------- Part C
print("== Part C: diluted-interval laws D_theta (floating evidence)")


def chart_T0_X(p, gvals):
    """gvals: dict x -> g(x) on Q (zero elsewhere). Round 189 chart with mask b in Q.
    Returns (T0, X, c) with Delta(lam,0) = sum_{r,b} mu(r,b) mu(lam r, b)."""
    g0 = prim_root(p)
    logt = np.zeros(p, dtype=np.int64)
    x = 1
    for k in range(p - 1):
        logt[x] = k
        x = x * g0 % p
    chi = legendre(p)
    supp = [y for y, v in gvals.items() if v > 0 and y not in (0, 1)]
    # v[b][log r] accumulates mu(r,b)
    V = np.zeros((p, p - 1))
    for Y in supp:
        for D in supp:
            if D == Y:
                continue
            inv1D = pow(1 - D, p - 2, p)
            r = (Y - D) * inv1D % p
            b = D * (1 - Y) % p * pow(Y * (1 - D) % p, p - 2, p) % p
            if chi[b] != 1:
                continue
            V[b, logt[r]] += gvals[Y] * gvals[D]
    Fv = np.fft.fft(V, axis=1)
    corr = np.real(np.fft.ifft(np.sum(np.abs(Fv) ** 2, axis=0)))   # corr[l] = sum_b sum_r v(r) v(g^l r)
    Delta = np.zeros(p)
    x = 1
    for k in range(p - 1):
        Delta[x] = corr[k]
        x = x * g0 % p
    garr = np.zeros(p)
    for y, v in gvals.items():
        garr[y] = v
    T0 = float(np.sum(garr * Delta))
    X = float(np.sum(Delta))
    c = float(Delta[1])
    return T0, X, c


for p, theta in ((1009, 0.4), (2017, 0.4), (2017, 0.25)):
    n = (p - 1) // 2
    g0 = prim_root(p)
    g2 = g0 * g0 % p
    xs = [pow(g2, k, p) for k in range(n)]
    m0 = n / math.sqrt(p)
    m = int(round(m0))
    Lp = int(round(m / theta))
    start = n // 5
    Jp = np.arange(start, start + Lp)
    S = np.sort(rng.choice(Jp, size=m, replace=False))
    nu = np.zeros(n); nu[S] = 1.0 / m
    f = np.array([np.sum(nu[S] * np.exp(2j * np.pi * S * k / n)) for k in range(n)])
    g = np.abs(f) ** 2
    ind = np.zeros(n); ind[S] = 1
    over = np.array([np.sum(ind * np.roll(ind, a)) for a in range(n)])
    E = np.sum(over ** 2)
    rmax = over[1:].max() / m
    K = n // (4 * Lp)                     # I = {gamma^{2k}: |k| <= K}, I I^{-1} = {|k| <= 2K}
    ks = [k % n for k in range(-2 * K, 2 * K + 1)]
    ming = g[ks].min()
    cmax = 0
    for e in range(2, int(2 * m0) + 1):
        if n % e == 0:
            st = n // e
            cmax = max(cmax, np.bincount(S % st, minlength=st).max())
    gvals = {xs[k]: g[k] for k in range(n)}
    T0, X, c = chart_T0_X(p, gvals)
    Iset = {xs[k % n]: 1.0 for k in range(-K, K + 1)}
    _, XI, _ = chart_T0_X(p, Iset)
    print(f"p={p} theta={theta}: m={m} L'={Lp} E/m^3={E/m**3:.3f} max r/m={rmax:.3f} |I|={2*K+1} "
          f"min g on II^-1={ming:.3f} (4/pi^2={4/math.pi**2:.3f}) max coset count={cmax} "
          f"Gamma_tot/sqrtp={np.sum(g**2)/math.sqrt(p):.3f} T0={T0:.1f} X(1_I)={XI:.1f} ratio={T0/XI:.2f}")
    check(f"p={p} theta={theta}: T0 >= (4/pi^2)^5 X(1_I)", T0 >= (4 / math.pi ** 2) ** 5 * XI)
    check(f"p={p} theta={theta}: E/m^3 < 1/2 (max overlap {rmax:.3f}: finite-size, Theorem 4 is asymptotic)", E / m ** 3 < 0.5)

# ---------------------------------------------------------------- Part D
print("== Part D: sector runs R(zeta) over generators of Q, plain Python")
expected = {1009: 7, 1013: 9, 1021: 5, 1033: 6, 1049: 9, 1289: 8}
for p, exp in expected.items():
    n = (p - 1) // 2
    chi = legendre(p)
    g0 = prim_root(p)
    best = 0
    for t in range(1, n):
        if math.gcd(t, n) != 1:
            continue
        z = pow(g0, 2 * t, p)
        c0 = chi[(1 - z) % p]
        R, y = 1, z * z % p
        while R < n - 1 and chi[(1 - y) % p] == c0:
            R += 1
            y = y * z % p
        best = max(best, R)
    check(f"p={p}: max R over generators = {best} (script printed {exp})", best == exp)

print("ALL AUDIT CHECKS OK" if ok else "SOME AUDIT CHECK FAILED")
raise SystemExit(0 if ok else 1)
