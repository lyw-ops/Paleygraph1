#!/usr/bin/env python3
r"""Round 184, call ordinary-prime-near-critical-slope-row-mass: square-field control.

In F_q with q = p^2 the subfield gives an exactly critical configuration
(Round 20, "The square control"): the law nu is uniform on I \ {0}, where I is
the annihilator of F_p^* in the character group of Q (the squares of F_q^*).
This script builds that configuration and computes, for g = |f|^2 and
h(z) = g(1-z):

  * the near-critical inputs: G, G_-, m_eff/m_0, the quadratic-character sum
    (tightness of Lemma S2), the Fourier mass outside the subfield coset (R151),
    the additive energy E(S)/|S|^3 of the flat support (R20 gap);
  * the slope-row quantities X = E_Q(h), max_xi W_xi, sup_{lambda != 1} C(lambda),
    the first mass M_w, and the Young bound (G-1)^2 Gamma_2.

Exact part: g takes the two values 1 (on F_p^*) and beta = 1/(h-1)^2 (on the rest
of Q). All counts are exact integers (FFT convolutions are rounded and the
rounding error is asserted < 1e-6); every quantity is assembled as a polynomial
in beta with integer coefficients and evaluated with Fractions. The closed forms
X_0 = (p-2)(p-3)^2 etc. for the subfield part g_0 = 1_{F_p^*} are checked.

Usage: .venv/bin/python -B research/paley-184-rowmass-square-control.py [p ...]
(default p = 5 7 11 13 17 19 23 29 31 37 41 43 47; numpy required).
"""
import sys
from fractions import Fraction
import numpy as np


def field(p):
    """F_{p^2} = F_p[w]/(w^2 - d); elements a + b w encoded as a + p*b."""
    d = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
    q = p * p

    def mul(u, v):
        a, b = u % p, u // p
        c, e = v % p, v // p
        return ((a * c + b * e * d) % p) + p * ((a * e + b * c) % p)

    # find a generator of F_q^*
    fac = []
    m = q - 1
    t = 2
    while t * t <= m:
        if m % t == 0:
            fac.append(t)
            while m % t == 0:
                m //= t
        t += 1
    if m > 1:
        fac.append(m)

    def power(u, k):
        r, b = 1, u
        while k:
            if k & 1:
                r = mul(r, b)
            b = mul(b, b)
            k >>= 1
        return r

    for gcand in range(2, q):
        if gcand % p == 0 and gcand // p == 0:
            continue
        if all(power(gcand, (q - 1) // f) != 1 for f in fac):
            gen = gcand
            break
    log = np.full(q, -1, dtype=np.int64)
    exp = np.zeros(q - 1, dtype=np.int64)
    x = 1
    for k in range(q - 1):
        exp[k] = x
        log[x] = k
        x = mul(x, gen)
    assert x == 1 and (log[1:] >= 0).all() and log[0] == -1
    return q, mul, log, exp


def neg(u, p):
    return ((-(u % p)) % p) + p * ((-(u // p)) % p)


def one_minus(u, p):
    return ((1 - (u % p)) % p) + p * ((-(u // p)) % p)


def mconv(a, b):
    """multiplicative convolution on the cyclic group Z/(q-1) via log index:
    out[k] = sum_i a[i] b[k-i] (circular). Exact for integer inputs."""
    n = len(a)
    r = np.fft.irfft(np.fft.rfft(a) * np.fft.rfft(b), n)
    ri = np.rint(r)
    assert np.max(np.abs(r - ri)) < 1e-6, np.max(np.abs(r - ri))
    return ri.astype(np.int64)


def mcorr(a, b):
    """out[k] = sum_i a[i] b[i+k] (circular)."""
    n = len(a)
    r = np.fft.irfft(np.conj(np.fft.rfft(a)) * np.fft.rfft(b), n)
    ri = np.rint(r)
    assert np.max(np.abs(r - ri)) < 1e-6, np.max(np.abs(r - ri))
    return ri.astype(np.int64)


def polyval(coeffs, beta):
    return sum(Fraction(int(c)) * beta ** k for k, c in enumerate(coeffs))


def run(p):
    q, mul, log, exp = field(p)
    N = q - 1
    n = N // 2
    hh = (p + 1) // 2  # |I|
    beta = Fraction(1, (hh - 1) ** 2)
    # elements by log index k: x = exp[k]; Q = even k; F_p^* = multiples of (p+1)
    k = np.arange(N)
    inQ = (k % 2 == 0)
    inF = (k % (p + 1) == 0)
    assert inF.sum() == p - 1 and (inF <= inQ).all()
    # verify F_p^* really is the prime subfield (b-coordinate 0)
    assert all(exp[i] // p == 0 for i in np.nonzero(inF)[0])
    # chi_q(x) = +1 on Q, -1 off Q
    # g = 1 on F_p^*, beta on Q \ F_p^*, 0 elsewhere: as indicator vectors (by log index)
    indF = inF.astype(np.int64)
    indR = (inQ & ~inF).astype(np.int64)
    # check f formula: f = (hh*1_F - 1)/(hh-1) on Q equals Fourier sum over I\{0}
    # (I = multiples of p-1 in Z/n; x = gamma^(2i), i = k/2)
    i_idx = k[inQ] // 2
    jj = np.arange(p - 1, n, p - 1)  # I \ {0}
    assert len(jj) == hh - 1
    fsum = np.exp(2j * np.pi * np.outer(i_idx, jj) / n).sum(axis=1).real / (hh - 1)
    fform = (hh * inF[inQ] - 1) / (hh - 1)
    assert np.max(np.abs(fsum - fform)) < 1e-9
    # shifted functions on F_q^* (log index): h(z) = g(1-z)
    sh = np.array([log[one_minus(int(exp[t]), p)] for t in range(N)])  # log(1-z), -1 if 1-z=0
    hF = np.zeros(N, dtype=np.int64)
    hR = np.zeros(N, dtype=np.int64)
    ok = sh >= 0
    hF[ok] = indF[sh[ok]]
    hR[ok] = indR[sh[ok]]
    # c_h(kappa) = sum_z h(z) h(kappa z) = A + 2 beta B + beta^2 C (integer arrays by log kappa)
    A = mcorr(hF, hF)
    Bc = mcorr(hF, hR)
    Bc2 = mcorr(hR, hF)
    Cc = mcorr(hR, hR)
    # kappa in Q \ {1}: log even, nonzero
    selQ = (k % 2 == 0) & (k != 0)
    # X = sum_{kappa in Q\{1}} c^2, polynomial in beta of degree 4
    c0, c1, c2 = A, Bc + Bc2, Cc
    Xc = [np.sum(c0[selQ] * c0[selQ]), np.sum(2 * c0[selQ] * c1[selQ]),
          np.sum(c1[selQ] ** 2 + 2 * c0[selQ] * c2[selQ]), np.sum(2 * c1[selQ] * c2[selQ]),
          np.sum(c2[selQ] ** 2)]
    X = polyval(Xc, beta)
    X0 = int(Xc[0])
    assert X0 == (p - 2) * (p - 3) ** 2, (X0, (p - 2) * (p - 3) ** 2)
    # m(r) = c_h(1-r) for 1-r in Q\{1}; as function of r by log index
    m_parts = []
    for cc in (c0, c1, c2):
        mr = np.zeros(N, dtype=np.int64)
        for t in range(N):
            r = int(exp[t])
            u = one_minus(r, p)
            if u == 0:
                continue
            lu = log[u]
            if lu % 2 == 0 and lu != 0:
                mr[t] = cc[lu]
        m_parts.append(mr)
    # W_xi = sum_r m(r) m(xi/r) = multiplicative convolution; C(lambda) = sum_r m(r) m(lambda r)
    W = [None] * 5
    Cl = [None] * 5
    for a in range(3):
        for b in range(3):
            Wab = mconv(m_parts[a], m_parts[b])
            Cab = mcorr(m_parts[a], m_parts[b])
            W[a + b] = Wab if W[a + b] is None else W[a + b] + Wab
            Cl[a + b] = Cab if Cl[a + b] is None else Cl[a + b] + Cab
    bf = float(beta)
    Wf = sum(W[t] * bf ** t for t in range(5))
    Cf = sum(Cl[t] * bf ** t for t in range(5))
    xi_max = int(np.argmax(Wf))
    maxW = polyval([W[t][xi_max] for t in range(5)], beta)
    lam = np.argmax(np.where(k != 0, Cf, -1))
    supC = polyval([Cl[t][lam] for t in range(5)], beta)
    # sanity: C(1) = X, sum W = M_1^2, W <= X
    C1 = polyval([Cl[t][0] for t in range(5)], beta)
    assert C1 == X
    M1c = [int(np.sum(mp)) for mp in m_parts]
    M1 = polyval(M1c, beta)
    sumW = polyval([int(np.sum(W[t])) for t in range(5)], beta)
    assert sumW == M1 * M1
    assert maxW <= X
    W0max = int(W[0].max())
    C0sup = int(np.max(Cl[0][1:]))
    # near-critical inputs
    G = (p - 1) + beta * int(indR.sum())
    assert G == p + 1
    Gam2 = (p - 2) + beta ** 2 * int(indR.sum())  # sum_{x != 1} g^2
    # sectors: T_eps = {x in Q\{1}: chi(1-x) = eps}
    chi1m = np.zeros(N, dtype=np.int64)
    for t in range(N):
        u = one_minus(int(exp[t]), p)
        chi1m[t] = 0 if u == 0 else (1 if log[u] % 2 == 0 else -1)
    assert (chi1m[inF & (k != 0)] == 1).all()  # subfield lies in T_+
    Gminus = beta * int(np.sum(indR[chi1m == -1]))
    Gplus = (p - 2) + beta * int(np.sum(indR[chi1m == 1]))
    sumgchi = Gplus - Gminus
    m0 = Fraction(n) / p  # n / sqrt(q)
    meff = Fraction(hh - 1)
    # R151 Fourier mass outside the coset B = F_p^*: ||1_{Q\B} f||^2 / ||f||^2 (f^2 = g)
    tB = (beta * int(indR.sum())) / G
    # first mass M_w = sum_kappa sum_{P != P'} mu mu' w(AD/(CY)); compute by brute force
    # only for small q (O(q^2)); w = g(1-g) is 0 on F_p^*, beta(1-beta) on Q\F_p^*
    Mw = None
    if q <= 530:
        Mw = first_mass(p, q, mul, log, exp, inF, inQ, beta)
    young = (G - 1) ** 2 * Gam2
    return dict(p=p, q=q, G=G, Gm=Gminus, sumgchi=sumgchi, meff_m0=meff / m0, tB=tB,
                Gam2=Gam2, X=X, X0=X0, maxW=maxW, W0max=W0max, supC=supC, C0sup=C0sup,
                M1=M1, Mw=Mw, young=young)


def first_mass(p, q, mul, log, exp, inF, inQ, beta):
    """M_w = sum over kappa in Q\\{1}, P=(Y,D), P'=(A,C) in R_kappa, P != P',
    of g(Y)g(D)g(A)g(C) w(AD/(CY)) (Round 182 Proposition 1), exact Fractions."""
    N = q - 1

    def gval(x):
        if x == 0:
            return Fraction(0)
        lx = log[x]
        if not inQ[lx]:
            return Fraction(0)
        return Fraction(1) if inF[lx] else beta

    def wval(x):
        gx = gval(x)
        return gx * (1 - gx)

    def inv(x):
        return int(exp[(-log[x]) % N])

    # labels in Q \ {1}
    labels = [int(exp[t]) for t in range(0, N, 2) if t != 0]
    rows = {}
    for D in labels:
        oD = one_minus(D, p)
        ioD = inv(oD)
        gD = gval(D)
        for Y in labels:
            if Y == D:
                continue
            kap = mul(one_minus(Y, p), ioD)
            if log[kap] % 2 != 0:
                continue
            rows.setdefault(kap, []).append((Y, D, gval(Y) * gD))
    tot = Fraction(0)
    for kap, lst in rows.items():
        for (Y, D, mu) in lst:
            if mu == 0:
                continue
            iCY_base = inv(Y)
            for (A, C, mu2) in lst:
                if mu2 == 0 or (A, C) == (Y, D):
                    continue
                s = mul(mul(A, D), inv(mul(C, Y)))
                ws = wval(s)
                if ws:
                    tot += mu * mu2 * ws
    return tot


def main():
    ps = [int(a) for a in sys.argv[1:]] or [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print("square control g = |f|^2, nu uniform on I\\{0} (I = annihilator of F_p^*), q = p^2")
    print(" p     q    G/sqrt(q) G_-    sum g chi(1-x)/sqrt(q) m_eff/m_0 t_B     Gamma_2/sqrt(q) "
          "X/q^1.5  X0=(p-2)(p-3)^2 maxW/q^1.5 supC/q^1.5 Young/q^1.5  M_w")
    for p in ps:
        r = run(p)
        sq = r['p']  # sqrt(q)
        q15 = Fraction(sq) ** 3
        mw = "n/a" if r['Mw'] is None else f"{float(r['Mw']):.3e}"
        print(f"{p:3d} {r['q']:6d} {float(r['G'] / sq):8.4f} {float(r['Gm']):6.3f} "
              f"{float(r['sumgchi'] / sq):10.4f}            {float(r['meff_m0']):7.4f} "
              f"{float(r['tB']):7.4f} {float(r['Gam2'] / sq):10.4f}      "
              f"{float(r['X'] / q15):7.4f}  {r['X0']:10d}      {float(r['maxW'] / q15):7.4f}"
              f"    {float(r['supC'] / q15):7.4f}    {float(r['young'] / q15):7.4f}   {mw}")
    print("checks: closed form X0 = (p-2)(p-3)^2, C(1) = X, sum_xi W_xi = M_1^2, max W <= X,"
          " f = (h 1_F - 1)/(h-1): OK")


if __name__ == "__main__":
    main()
