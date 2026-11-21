#!/usr/bin/env python3
"""Round 189 cold call `cold-prime-perron-nonseed-price`: shared layer (own implementation; imported by
paley-189-cold-seed-certify.py and paley-189-cold-nonseed-certify.py through importlib).

It does not import or copy any earlier script.  Conventions as accepted in Rounds 183-188:
  S = s cos(theta) on the Jacobi circle, J^k <-> e^{ik theta}, beta = s^2/(4t);
  Phi_t(S)      = 2 sqrt t        sum_k b'_k J^k,   b'  = coef of (1 + beta cos^2)^{1/2}            (k even)
  Phi_t'(S)     = (s/(2 sqrt t))  sum_k ghat_k J^k, ghat = coef of cos (1 + beta cos^2)^{-1/2}      (k odd)
  Phi_t''(S)    = (1/(2 sqrt t))  sum_k bhat_k J^k, bhat = coef of (1 + beta cos^2)^{-3/2}          (k even)
  Phi_t'''(S)   = -(3s/(2 sqrt t)^3) sum_k e_k J^k, e = coef of cos (1 + beta cos^2)^{-5/2}         (k odd)
  Phi_t''''(S)  = (3/(2 sqrt t)^3) sum_k f_k J^k,   f = 4 (1+beta cos^2)^{-5/2} - 5 (1+beta cos^2)^{-7/2} (k even)
Coefficients are complex balls (python-flint acb) by the binomial series
  [e^{ik th}] cos^j th (1 + beta cos^2 th)^alpha = sum_l binom(alpha, l) beta^l C(2l+j, (2l+j+|k|)/2) / 2^(2l+j),
with a rigorous tail: |binom(alpha,l)| <= P_alpha(l) (P = 1, 1, 2l+1, (2l+1)(2l+3)/3, (2l+1)(2l+3)(2l+5)/15 for
alpha = 1/2, -1/2, -3/2, -5/2, -7/2) and C(n, .)/2^n <= 1.
Parameter regions:
  POINT  : t = a = 2031/128, s^2 = 8 (the compact model at the real floor);
  QCOMPACT: t in the closed square Q (below), s^2 = 8 (the compact model on Q);
  REGION : t in a + [-2^-17, 2^-17] + i[-2^-17, 2^-17] (the closed square Q), s^2 in [8, 8 + 8/(10^6 - 1)]
           (eligible p >= 10^6).  Every ball contains all values on the region.
"""
from fractions import Fraction as Fr
from math import comb

import numpy as np
from flint import acb, arb, ctx

ctx.prec = 200
A_T = arb(2031) / 128
_H17 = arb(2) ** -17
_S2LO, _S2HI = arb(8), arb(8) + arb(8) / 999999


def _hull(lo, hi):
    """arb ball containing [lo, hi] (lo, hi exact-ish arbs)"""
    mid = (lo + hi) / 2
    rad = (hi - lo) / 2
    return arb(mid.mid(), rad.upper()) + arb(0, (mid.rad() + rad.rad()) * 2 + arb(2) ** -190)


def make_params(kind):
    if kind == "point":
        T = acb(A_T)
        S2 = arb(8)
    elif kind == "qcompact":
        T = acb(A_T + arb(0, _H17.upper()), arb(0, _H17.upper()))
        S2 = arb(8)
    elif kind == "region":
        T = acb(A_T + arb(0, _H17.upper()), arb(0, _H17.upper()))
        S2 = _hull(_S2LO, _S2HI)
    else:
        raise ValueError(kind)
    S = acb(S2.sqrt())
    SQT = T.sqrt()                      # principal branch, Re t > 15
    BETA = acb(S2) / (4 * T)
    return {"T": T, "S2": S2, "S": S, "SQT": SQT, "BETA": BETA, "kind": kind}


_ALPHA = {"half": Fr(1, 2), "m12": Fr(-1, 2), "m32": Fr(-3, 2), "m52": Fr(-5, 2), "m72": Fr(-7, 2)}


def _binom(alpha, l):
    r = Fr(1)
    for j in range(l):
        r = r * (alpha - j) / (j + 1)
    return r


def afr(x):
    """exact arb from an int or Fraction"""
    x = Fr(x)
    return arb(x.numerator) / x.denominator


def _palpha(kind, l):
    if kind in ("half", "m12"):
        return 1
    if kind == "m32":
        return 2 * l + 1
    if kind == "m52":
        return Fr((2 * l + 1) * (2 * l + 3), 3)
    return Fr((2 * l + 1) * (2 * l + 3) * (2 * l + 5), 15)


LS = 70   # series terms kept exactly


def _series_tail(kind, l0, q):
    """rigorous upper bound (arb) of sum_{l >= l0} P_alpha(l) q^l, q = |beta| upper (arb, < 0.2)."""
    tot = arb(0)
    for l in range(l0, l0 + 40):
        tot += afr(_palpha(kind, l)) * q ** l
    # remainder l >= l0 + 40: ratio of consecutive terms <= q * ((2l+7)/(2l+1))^3 <= q * 1.5^3 < 1 for q < 0.29
    l1 = l0 + 40
    rho = q * afr(Fr((2 * l1 + 7), (2 * l1 + 1))) ** 3
    assert rho.upper() < 1
    tot += afr(_palpha(kind, l1)) * q ** l1 / (1 - rho)
    return tot


def series_coef(P, kind, j, k):
    """[e^{ik th}] cos^j th (1 + beta cos^2 th)^alpha as an acb ball (k = j mod 2)."""
    kk = abs(k)
    assert (kk - j) % 2 == 0
    l0 = max(0, (kk - j + 1) // 2)
    BETA = P["BETA"]
    q = abs(BETA).upper()
    q = arb(q)
    val = acb(0)
    bp = acb(1)
    for _ in range(l0):
        bp = bp * BETA
    for l in range(l0, LS):
        n = 2 * l + j
        c = _binom(_ALPHA[kind], l) * Fr(comb(n, (n + kk) // 2), 2 ** n)
        val += acb(arb(c.numerator) / c.denominator) * bp
        bp = bp * BETA
    tl = _series_tail(kind, LS, q)
    return val + acb(arb(0, tl.upper()), arb(0, tl.upper()))


_cache = {}


def coef(P, kind, k):
    """coefficient of J^k (acb ball) in:  'phi0' Phi(S), 'phi1' Phi'(S), 'phi2' Phi''(S), 'phi3' Phi'''(S),
    'phi4' Phi''''(S).  Even in k (computed for |k|)."""
    key = (P["kind"], kind, abs(k))
    if key in _cache:
        return _cache[key]
    k = abs(k)
    TS = 2 * P["SQT"]
    if kind == "phi0":
        v = TS * series_coef(P, "half", 0, k) if k % 2 == 0 else acb(0)
    elif kind == "phi1":
        v = P["S"] / TS * series_coef(P, "m12", 1, k) if k % 2 == 1 else acb(0)
    elif kind == "phi2":
        v = series_coef(P, "m32", 0, k) / TS if k % 2 == 0 else acb(0)
    elif kind == "phi3":
        v = -3 * P["S"] / TS ** 3 * series_coef(P, "m52", 1, k) if k % 2 == 1 else acb(0)
    elif kind == "phi4":
        v = (3 / TS ** 3) * (4 * series_coef(P, "m52", 0, k) - 5 * series_coef(P, "m72", 0, k)) if k % 2 == 0 else acb(0)
    else:
        raise ValueError(kind)
    _cache[key] = v
    return v


def abs_lo(z):
    """exact arb lower bound (>= 0) of |z| for an acb ball z"""
    v = abs(z).lower()
    return v if v > 0 else arb(0)


def abs_hi(z):
    return abs(z).upper()


def seed_tail(P, m0):
    """bounds for the omitted seed harmonics m >= m0 (odd): sum w_m and sum m w_m, w_m = |coef of J^m in Phi'(S)|
    <= |s/(2 sqrt t)| q^{(m-1)/2}/(1-q), q = |beta|."""
    q = arb(abs(P["BETA"]).upper())
    vp = arb(abs(P["S"] / (2 * P["SQT"])).upper())
    pref = vp / (1 - q)
    x = q.sqrt()          # w_m <= pref * x^(m-1)
    # sum_{m >= m0, m odd} x^(m-1) = x^(m0-1)/(1-x^2);  sum m x^(m-1) = x^(m0-1) (m0/(1-x^2) + 2x^2/(1-x^2)^2)
    T0 = pref * x ** (m0 - 1) / (1 - x * x)
    T1 = pref * x ** (m0 - 1) * (arb(m0) / (1 - x * x) + 2 * x * x / (1 - x * x) ** 2)
    return T0.upper(), T1.upper()


def to_fr_lo(x):
    m, e = x.lower().man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))


def to_fr_hi(x):
    m, e = x.upper().man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))


# ---------------------------------------------------------------- pooled slot operators (Theorem 1 form)
# A symmetric measure omega on Z defines the row operator (phi M)_a = sum_x omega(x) psi_{|a+x|},
# psi_c = phi_c + phi_0 (c - 1) (psi_0 = 0).  phi is tabulated for b < BC and affine (s b + kappa) beyond.

class Trial:
    def __init__(self, phiq, BC):
        self.BC = BC
        self.tab = phiq[:BC]
        self.s = phiq[BC] - phiq[BC - 1]
        self.kap = phiq[BC] - self.s * BC
        self.phi0 = phiq[0]

    def phi(self, b):
        return self.tab[b] if b < self.BC else self.s * b + self.kap

    def psi(self, c):
        if c == 0:
            return Fr(0)
        return self.phi(c) + self.phi0 * (c - 1)


def float_perron(omega_float, NB=1600, BC=300, iters=3000):
    """floating proposal of the left Perron vector (row form); returns (lambda, phi array)."""
    xs = np.array(sorted(omega_float))
    ws = np.array([omega_float[x] for x in xs])
    XM = int(np.abs(xs).max())
    phi = np.ones(NB)
    phi[1:] = np.arange(1, NB)
    a = np.arange(NB)

    def apply(ph):
        s = ph[-1] - ph[-2]
        ext = np.concatenate([ph, ph[-1] + s * np.arange(1, XM + 3)])
        psi = ext + ext[0] * (np.arange(len(ext)) - 1.0)
        psi[0] = 0.0
        out = np.zeros(NB)
        for x, w in zip(xs, ws):
            out += w * psi[np.abs(a + x)]
        return out

    for _ in range(iters):
        nw = apply(phi)
        phi = nw / nw[BC] * BC
    r = apply(phi)[1:BC] / phi[1:BC]
    return float(np.median(r)), phi


def rationalize(phi, BC, den=2 ** 64):
    return [Fr(round(float(v) * den), den) for v in phi[:BC + 1]]
