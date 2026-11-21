#!/usr/bin/env python3
"""Round 184 cold call: FLOATING diagnostic (evidence only, label (c)); own implementation.

Physical cold map with the Paley sign row on the subgroup of squares (same conventions as the
Round 182/183 diagnostics: K = real symmetric circulant with eigenvalues the Paley sign row,
t0 = n at the mark, real t, one real lift).  Picard pieces from the seed:
    W_0 = S = 2 sqrt(n) K e_0,  W_{j+1} = K Phi_t(W_j),  h_j = W_j - W_{j-1},  h = V_* - S.
Printed per prime: sup and RMS of h, h_1, h - h_1, h - h_1 - h_2, h - h_1 - L_S h_1 with
L_S h_1 = K(Phi_t'(S) h_1) (the first-order part of h_2), and sup |L_S h_1|; then the
normalized correlations between the pieces (near 0 = no l2-visible cancellation between pieces).  These are double-precision
proxies.  A(.) >= sup|.| at good coordinates (Round 181), so sup|h - h_1| is a floating proxy
for a LOWER bound on A(h - h_1); nothing here is a certified bound.

Replay:  .venv/bin/python -B research/paley-184-cold-h-rest-diagnostic.py      (about 1-3 min)
"""
import numpy as np


def is_prime(m):
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for b in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(b, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def next_prime_1mod4(m):
    while not (m % 4 == 1 and is_prime(m)):
        m += 1
    return m


def primitive_root(p):
    order = p - 1
    fac, m, d = [], order, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    g = 2
    while not all(pow(g, order // f, p) != 1 for f in fac):
        g += 1
    return g


def sign_row(p):
    """chi(1 - g^(2j)), j = 0..n-1, chi the quadratic character (Legendre symbol)"""
    n = (p - 1) // 2
    g = primitive_root(p)
    g2 = g * g % p
    pw = np.empty(n, dtype=np.int64)
    x = 1
    for j in range(n):
        pw[j] = x
        x = x * g2 % p
    arg = (1 - pw) % p
    sq = np.zeros(p, dtype=bool)
    sq[(np.arange(1, p, dtype=np.int64) ** 2) % p] = True
    out = np.where(sq[arg], 1.0, -1.0)
    out[arg == 0] = 0.0
    return out


def run(p, t, steps=600):
    sgn = sign_row(p)
    n = len(sgn)
    # K is the circulant whose eigenvalues are the sign row: K v = irfft(sign * rfft(v))
    eig = sgn[: n // 2 + 1]

    def K(v):
        return np.fft.irfft(eig * np.fft.rfft(v), n)

    tt = np.full(n, float(t))
    tt[0] = n
    e0 = np.zeros(n)
    e0[0] = 1.0
    S = 2 * np.sqrt(n) * K(e0)
    W = [S.copy()]
    V = S.copy()
    res = None
    for k in range(steps):
        Vn = K(np.sqrt(4 * tt + V * V))
        if k < 3:
            W.append(Vn.copy())
        res = np.sqrt(np.mean((Vn - V) ** 2))
        V = Vn
        if res < 1e-14 and k >= 3:
            break
    hs = [W[j] - W[j - 1] for j in range(1, len(W))]
    # L_S h_1 = K(Phi_t'(S) h_1), Phi_t'(x) = x / sqrt(4t + x^2) (mark: t0 = n)
    LSh1 = K(S / np.sqrt(4 * tt + S * S) * hs[0])
    return n, res, S, V - S, hs, LSh1


def st(v):
    return float(np.max(np.abs(v))), float(np.sqrt(np.mean(v * v)))


a = 2031 / 128
primes = [10009, 100049, 400009] + [next_prime_1mod4(m) for m in (1000000, 2000000, 4000000)]
print("[float] t = a = 2031/128, one real lift, double precision; evidence only")
print("[float]       p   sup|h|  RMS(h) | sup|h1|  RMS(h1) | sup|h-h1| RMS(h-h1) argmax | sup|h-h1-h2| | sup|h-h1-L_S h1| sup|L_S h1|")
for p in primes:
    n, res, S, h, hs, LSh1 = run(p, a)
    d1 = h - hs[0]
    d2 = d1 - hs[1]
    i_max = int(np.argmax(np.abs(d1)))
    print(f"[float] {p:>8} {st(h)[0]:.4f}  {st(h)[1]:.4f} | {st(hs[0])[0]:.4f}  {st(hs[0])[1]:.4f} | "
          f"{st(d1)[0]:.4f}   {st(d1)[1]:.4f}  j={i_max:<7d} | {st(d2)[0]:.4f}      | {st(d1 - LSh1)[0]:.4f}"
          f"           {st(LSh1)[0]:.4f}"
          f"   (final step RMS {res:.1e})")
    rest2 = d1 - LSh1
    def corr(x, y):
        return float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y)))
    print(f"[float]          correlations: <h1, h-h1> {corr(hs[0], d1):+.4f}; <h1, L_S h1> {corr(hs[0], LSh1):+.4f}; "
          f"<L_S h1, rest> {corr(LSh1, rest2):+.4f}; <h1, rest> {corr(hs[0], rest2):+.4f}; "
          f"RMS(L_S h1) {st(LSh1)[1]:.4f}, RMS(rest) {st(rest2)[1]:.4f}")
