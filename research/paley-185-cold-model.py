#!/usr/bin/env python3
"""Round 185 cold call `cold-prime-picard-leaf-inequivalence`: shared model layer (own implementation).

Imported by the other paley-185-cold-*.py scripts (it is a module; running it prints a short
self-test).  It does not import or copy any earlier script.

Compact model (hypotheses (b4), (b-Jk), (b-T) as accepted in Round 184):
  * an object is described by its two-fibre weight data W = (A, B), each a multiset of integers
    stored as a sorted tuple of (weight, multiplicity);
  * the line J^k has W = ((-k), (+k)) and dimension 1;
  * tensor product: at each fibre the multiset of pairwise sums (fibre A with fibre A);
  * transport K: r' = (1/2) sum |w| over both fibres; new A = negatives of A + positives of B,
    new B = negatives of B + positives of A, each refilled with zeros up to r'.
Coefficients are complex balls (python-flint acb) that contain every value on the parameter
region Q x {p >= 10^6}:  t in a + [-2^-17, 2^-17](1 + i), a = 2031/128;  s^2 in [8, 8 + 8/(10^6-1)].
So every lower/upper bound computed from them is uniform on that region.
"""
from collections import Counter
from fractions import Fraction as Fr
from math import comb

from flint import arb, acb, ctx

ctx.prec = 160

# ------------------------------------------------------------------ parameter region (balls)
A_T = arb(2031) / 128
H17 = 2.0 ** -17                                   # exact binary number
T_BALL = acb(A_T + arb(0, H17), arb(0, H17))       # contains the closed square Q
S2_BALL = arb(8) + arb(4) / 999999 + arb(0, 4.1e-6)  # contains [8, 8 + 8/(10^6 - 1)]
S_BALL = S2_BALL.sqrt()
SQT = T_BALL.sqrt()                                 # principal branch; Re t > 15
TWO_SQT = 2 * SQT
BETA = acb(S2_BALL) / (4 * T_BALL)
VARPI = acb(S_BALL) / TWO_SQT                      # s / (2 sqrt t)
BETA_ABS_UP = float(abs(BETA).upper()) * (1 + 1e-12)
assert BETA_ABS_UP < 0.1261

LSER = 45   # series terms kept exactly; the rest is a rigorous ball tail


def _binom(alpha, l):
    r = Fr(1)
    for j in range(l):
        r = r * (alpha - j) / (j + 1)
    return r


def _tail(kind, l0):
    """sum_{l >= l0} M_l |beta|^l with |series coefficient_l| <= M_l (weights <= 1)."""
    b = BETA_ABS_UP
    tot = 0.0
    for l in range(l0, l0 + 400):
        if kind == "half":
            m = 1.0
        elif kind == "m12":
            m = 1.0
        elif kind == "m32":
            m = 2 * l + 1.0
        elif kind == "m52":
            m = (2 * l + 1.0) * (2 * l + 3.0) / 3.0
        else:                       # m72
            m = (2 * l + 1.0) * (2 * l + 3.0) * (2 * l + 5.0) / 15.0
        tot += m * b ** l
    return tot * 1.0000001 + 1e-300


_ALPHA = {"half": Fr(1, 2), "m12": Fr(-1, 2), "m32": Fr(-3, 2), "m52": Fr(-5, 2), "m72": Fr(-7, 2)}
_cache = {}


def _even_coef(kind, k):
    """coefficient of J^k (k even) in (1 + beta cos^2)^alpha"""
    i = abs(k) // 2
    val = acb(0)
    bp = acb(1)
    for _ in range(i):
        bp = bp * BETA
    for l in range(i, LSER):
        c = _binom(_ALPHA[kind], l) * Fr(comb(2 * l, l + i), 4 ** l)
        val += acb(arb(c.numerator) / arb(c.denominator)) * bp
        bp = bp * BETA
    tl = _tail(kind, LSER)
    return val + acb(arb(0, tl), arb(0, tl))


def _odd_coef(kind, k):
    """coefficient of J^k (k odd) in cos(theta) (1 + beta cos^2)^alpha"""
    kk = abs(k)
    l0 = (kk - 1) // 2
    val = acb(0)
    bp = acb(1)
    for _ in range(l0):
        bp = bp * BETA
    for l in range(l0, LSER):
        c = _binom(_ALPHA[kind], l) * Fr(comb(2 * l + 1, l + (kk + 1) // 2), 2 ** (2 * l + 1))
        val += acb(arb(c.numerator) / arb(c.denominator)) * bp
        bp = bp * BETA
    tl = _tail(kind, LSER)
    return val + acb(arb(0, tl), arb(0, tl))


def bprime(k):
    """b'_k: Phi_t(S) = 2 sqrt t sum b'_k J^k  (k even)"""
    key = ("bp", k)
    if key not in _cache:
        _cache[key] = _even_coef("half", k)
    return _cache[key]


def bhat(k):
    """bhat_k: Phi_t''(S) = (1/(2 sqrt t)) sum bhat_k J^k  (k even)"""
    key = ("bh", k)
    if key not in _cache:
        _cache[key] = _even_coef("m32", k)
    return _cache[key]


def ghat(k):
    """ghat_k: Phi_t'(S) = (s/(2 sqrt t)) sum ghat_k J^k  (k odd)"""
    key = ("g", k)
    if key not in _cache:
        _cache[key] = _odd_coef("m12", k)
    return _cache[key]


def ecoef(k):
    """e_k: Phi_t'''(S) = -(3 s/(2 sqrt t)^3) sum e_k J^k  (k odd)"""
    key = ("e", k)
    if key not in _cache:
        _cache[key] = _odd_coef("m52", k)
    return _cache[key]


def fcoef(k):
    """f_k (k even): Phi_t^(4)(S) = (3/(2 sqrt t)^3) sum f_k J^k,
    f = (4 beta cos^2 - 1)(1 + beta cos^2)^(-7/2) = 4(1 + beta cos^2)^(-5/2) - 5(1 + beta cos^2)^(-7/2)"""
    key = ("f", k)
    if key not in _cache:
        _cache[key] = 4 * _even_coef("m52", k) - 5 * _even_coef("m72", k)
    return _cache[key]


def coef_abs_up_tail(kind, k):
    """uniform upper bound of |coefficient of J^k| for any k (used for omitted ranges)"""
    b = BETA_ABS_UP
    if kind in ("bp", "bh"):
        l0 = abs(k) // 2
    else:
        l0 = (abs(k) - 1) // 2
    kk = {"bp": "half", "bh": "m32", "g": "m12", "e": "m52"}[kind]
    return _tail(kk, l0)


# ------------------------------------------------------------------ weight data
def mk(Acnt, Bcnt):
    return (tuple(sorted((w, c) for w, c in Acnt.items() if c)),
            tuple(sorted((w, c) for w, c in Bcnt.items() if c)))


def line(k):
    return (((-k, 1),), ((k, 1),))


def dim(W):
    return sum(c for _, c in W[0])


def shift(W, k):
    """J^k (x) W"""
    return (tuple((w - k, c) for w, c in W[0]), tuple((w + k, c) for w, c in W[1]))


def tensor(W1, W2):
    out = []
    for f in (0, 1):
        cnt = Counter()
        for w1, c1 in W1[f]:
            for w2, c2 in W2[f]:
                cnt[w1 + w2] += c1 * c2
        out.append(cnt)
    return mk(out[0], out[1])


def transport(W):
    """K(W) by (b4); asserts validity (refills >= 0)"""
    r2 = sum(abs(w) * c for w, c in W[0]) + sum(abs(w) * c for w, c in W[1])
    assert r2 % 2 == 0
    r = r2 // 2
    A = Counter()
    B = Counter()
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
    za = r - sum(A.values())
    zb = r - sum(B.values())
    assert za >= 0 and zb >= 0, "negative refill"
    if za:
        A[0] += za
    if zb:
        B[0] += zb
    return mk(A, B)


def valid(W):
    d = dim(W)
    return d == sum(c for _, c in W[1]) and sum(abs(w) * c for w, c in W[0] + W[1]) == 2 * d


def contains(Wsmall, Wbig):
    """multiset containment, fibre by fibre"""
    for f in (0, 1):
        big = dict(Wbig[f])
        for w, c in Wsmall[f]:
            if big.get(w, 0) < c:
                return False
    return True


def mirror(W):
    """fibre exchange (the other lift)"""
    return (W[1], W[0])


def lower_abs(z):
    """certified lower bound (float, rounded down) of |z| for an acb ball z"""
    v = abs(z).lower()
    return max(0.0, float(v) * (1 - 1e-12) - 1e-300) if v > 0 else 0.0


def upper_abs(z):
    return float(abs(z).upper()) * (1 + 1e-12) + 1e-300


# Outward printing.  Float sums of N <= 10^6 nonnegative terms have relative rounding error
# <= 2.3e-10; the 1e-9 relative margin below covers it, then lower bounds are floored and upper
# bounds ceiled at the printed digit.
import math as _math


def fl(x, d=6):
    """decimal string <= x (lower bounds)"""
    y = x - abs(x) * 1e-9 - 1e-15
    return f"{_math.floor(y * 10 ** d) / 10 ** d:.{d}f}"


def cl(x, d=6):
    """decimal string >= x (upper bounds)"""
    y = x + abs(x) * 1e-9 + 1e-15
    return f"{_math.ceil(y * 10 ** d) / 10 ** d:.{d}f}"


def ce(x, d=3):
    """scientific string >= x (upper bounds of small quantities)"""
    y = x + abs(x) * 1e-9 + 1e-300
    if y <= 0:
        return "0"
    e = _math.floor(_math.log10(y))
    m = _math.ceil(y / 10 ** e * 10 ** d) / 10 ** d
    return f"{m:.{d}f}e{e:+03d}"


if __name__ == "__main__":
    print("beta ball:", BETA)
    print("|beta| <=", BETA_ABS_UP)
    for k in (1, 3, 5):
        print(f"ghat_{k} =", ghat(k))
    for k in (0, 2, 4):
        print(f"bhat_{k} =", bhat(k), f" b'_{k} =", bprime(k))
    for k in (1, 3, 5):
        print(f"e_{k} =", ecoef(k))
    K2 = transport(line(2))
    print("K(J^2) =", K2, "K(J^-2) =", transport(line(-2)), "valid", valid(K2))
    print("K(J^1 K(J^2)) =", transport(shift(K2, 1)))
