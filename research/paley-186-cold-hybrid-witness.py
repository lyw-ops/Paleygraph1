#!/usr/bin/env python3
"""Round 186 cold call `cold-prime-hybrid-price`: FLOATING witness (evidence only, label (c)); own implementation.

Physical cold map with the Paley sign row on the subgroup of squares, as in the Round 182-185 diagnostics:
K = real symmetric circulant whose eigenvalues are the sign row chi(1 - g^(2j)); mark t_0 = n; real t = a;
one real lift (principal positive branch of Phi_t(x) = sqrt(4t + x^2)); double precision.

Printed per prime:
  (0) sanity: sum of the sign row, S_0 * sqrt(n) (exact value -2), sum S^2 / (4(n-1)) (exact value 1),
      max|S| against s_p, and the fixed-point residual.
  (1) actual non-seed multiplier B_h f = K((Phi_t'(V) - Phi_t'(S)) f), V = S + h the stationary row (proxy for V_602):
      sup and RMS of B_h S and B_h h_1 (structured inputs; these are what the true operator does).
  (2) adversarial multipliers with the SAME size as h, on the same input f = S:
      (a) |g| = sup|h| at every non-mark coordinate (same sup norm as h),
      (b) |g_x| = |h_x| (same modulus at every coordinate as h: same sup, same counting norm, same distribution),
      signs chosen to align with row x0 of K, x0 the best non-mark coordinate (found by an FFT convolution of the
      certified lower-bound weights), then the vector K((Phi'(S+g) - Phi'(S)) S) is evaluated explicitly.
      Reported: its value at x0, divided by sqrt(n) and by A(S) = s_p, and the Theorem N lower bound c_N(gamma, n).
  (3) the norm-only (counting) conversion factor sqrt(n) * ||B_h S||_{2,n} / ||B_h S||_inf, i.e. what pricing the
      product in counting norm and converting back to sup costs against the true sup.

Nothing here is a certified bound.  Replay: .venv/bin/python -B research/paley-186-cold-hybrid-witness.py  (~1-2 min)
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


A_T = 2031 / 128


def run(p, t=A_T, steps=400):
    sgn = sign_row(p)
    n = len(sgn)
    eig = sgn[: n // 2 + 1]

    def K(v):
        return np.fft.irfft(eig * np.fft.rfft(v), n)

    tt = np.full(n, float(t))
    tt[0] = n
    e0 = np.zeros(n)
    e0[0] = 1.0
    S = 2 * np.sqrt(n) * K(e0)
    V = S.copy()
    res = None
    for k in range(steps):
        Vn = K(np.sqrt(4 * tt + V * V))
        res = np.sqrt(np.mean((Vn - V) ** 2))
        V = Vn
        if res < 1e-14 and k >= 3:
            break
    h1 = K(np.sqrt(4 * tt + S * S)) - S
    return n, sgn, K, tt, S, V, h1, res


def dphi(x, tt):
    return x / np.sqrt(4 * tt + x * x)


def d2phi(x, tt):
    return 4 * tt / (4 * tt + x * x) ** 1.5


def circ_corr(u, w):
    """c[x0] = sum_x u[(x0 - x) mod n] w[x]  (circular convolution)"""
    n = len(u)
    return np.fft.irfft(np.fft.rfft(u) * np.fft.rfft(w), n)


def adversarial(n, K, tt, S, f, mod_g, x0_mask):
    """best non-mark row x0 for |g| = mod_g (sign-aligned), evaluated explicitly"""
    kappa = S / (2 * np.sqrt(n))                      # kappa(x) = (K e_0)_x = K(x, 0) = K(0, x)
    # certified-type lower weight: min over the two signs of |Phi'(S+eps m) - Phi'(S)| * |f|
    w = np.minimum(np.abs(dphi(S + mod_g, tt) - dphi(S, tt)), np.abs(dphi(S - mod_g, tt) - dphi(S, tt))) * np.abs(f)
    w[0] = 0.0
    lower = circ_corr(np.abs(kappa), w)
    lower[~x0_mask] = -np.inf
    x0 = int(np.argmax(lower))
    idx = np.arange(n)
    row = kappa[(x0 - idx) % n]                       # K(x0, x)
    eps = np.sign(row * f)
    eps[eps == 0] = 1.0
    g = mod_g * eps                                    # Phi_t' increasing on the reals: sign(dPhi') = sign(g)
    g[0] = 0.0
    out = K((dphi(S + g, tt) - dphi(S, tt)) * f)
    return x0, float(lower[x0]), float(out[x0]), float(np.max(np.abs(out[x0_mask]))), g


def cN(gamma, n, s=2.828428539, b0=3):
    m2 = 4 * A_T / (4 * A_T + (s + gamma) ** 2) ** 1.5
    return gamma * m2 * (8 * (n - 1) * (n - 1 - 1 / n) / (s * s * n ** 1.5) - 2 * b0 * np.sqrt(n - 1) / n) / s


primes = [10009, 100049, next_prime_1mod4(1000000), next_prime_1mod4(4000000)]
print("[float] t = a = 2031/128, mark t_0 = n, one real lift, double precision; evidence only")
for p in primes:
    n, sgn, K, tt, S, V, h1, res = run(p)
    h = V - S
    sp = 2 * np.sqrt(p / n)
    print(f"\n[float] p = {p}, n = {n}; fixed-point step RMS {res:.1e}")
    print(f"[float]  (0) sum sign row = {int(sgn.sum())}; sqrt(n) S_0 = {np.sqrt(n) * S[0]:+.6f} (exact -2);"
          f" sum S^2/(4(n-1)) = {np.sum(S * S) / (4 * (n - 1)):.12f}; max|S| = {np.max(np.abs(S)):.6f} vs s_p = {sp:.6f}")
    good = np.ones(n, dtype=bool)
    good[0] = False
    supH = float(np.max(np.abs(h[good])))
    rmsH = float(np.sqrt(np.mean(h * h)))
    Bh = dphi(V, tt) - dphi(S, tt)
    BS = K(Bh * S)
    Bh1 = K(Bh * h1)
    print(f"[float]  sup|h| = {supH:.4f}, RMS(h) = {rmsH:.4f}, sup|Phi'(V)-Phi'(S)| (non-mark) = {np.max(np.abs(Bh[good])):.4f}")
    print(f"[float]  (1) actual: ||B_h S||_inf = {np.max(np.abs(BS[good])):.4f}  RMS {np.sqrt(np.mean(BS ** 2)):.4f}  "
          f"sup/RMS {np.max(np.abs(BS[good])) / np.sqrt(np.mean(BS ** 2)):.2f};   ||B_h h1||_inf = {np.max(np.abs(Bh1[good])):.4f}  "
          f"RMS {np.sqrt(np.mean(Bh1 ** 2)):.4f}")
    # (2a) constant modulus = sup|h|
    x0, lw, val, supv, g = adversarial(n, K, tt, S, S, supH, good)
    print(f"[float]  (2a) |g| = sup|h| = {supH:.4f}: x0 = {x0}; value at x0 = {val:.3f} (lower-weight sum {lw:.3f});"
          f" value/sqrt(n) = {val / np.sqrt(n):.4f}; value/(s_p sqrt n) = {val / (sp * np.sqrt(n)):.4f};"
          f" Theorem N c_N/sqrt(n) = {cN(supH, n) / np.sqrt(n):.4f}; ratio to A(S): {val / sp:.2f} vs c_N = {cN(supH, n):.2f}")
    # (2b) same modulus profile as h
    modh = np.abs(h).copy()
    modh[0] = 0.0
    x0b, lwb, valb, supvb, gb = adversarial(n, K, tt, S, S, modh, good)
    print(f"[float]  (2b) |g_x| = |h_x| (same sup {np.max(np.abs(gb)):.4f}, same RMS {np.sqrt(np.mean(gb * gb)):.4f} as h): x0 = {x0b};"
          f" value at x0 = {valb:.3f}; value/sqrt(n) = {valb / np.sqrt(n):.4f}; ratio to A(S): {valb / sp:.2f}")
    # (2c) same modulus profile, input f = h_1 (A(h_1) = 0.4945 in the model)
    x0c, lwc, valc, supvc, gc = adversarial(n, K, tt, S, h1, modh, good)
    print(f"[float]  (2c) |g_x| = |h_x|, input f = h_1: value at x0 = {valc:.3f}; value/sqrt(n) = {valc / np.sqrt(n):.4f};"
          f" ratio to A(h_1) = 0.4945: {valc / 0.4945:.2f};  actual ||B_h h_1||_inf = {np.max(np.abs(Bh1[good])):.4f}")
    # (3) counting conversion
    conv = np.sqrt(n) * np.sqrt(np.mean(BS ** 2)) / np.max(np.abs(BS[good]))
    print(f"[float]  (3) counting route for the actual product: sqrt(n) RMS(B_h S) / sup|B_h S| = {conv:.1f}"
          f" (the factor lost by pricing the product in counting norm and converting back to sup)")
