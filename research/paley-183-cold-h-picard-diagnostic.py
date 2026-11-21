#!/usr/bin/env python3
"""Round 183 cold price: FLOATING diagnostic (evidence only, label (c)).

Physical cold map as in research/paley-182-cold-fixedpoint-diagnostic.py (same Paley sign
row, K the real symmetric circulant, t0 = n at the mark, real t = a = 2031/128, one real lift).
Splits h = V_* - S into Picard pieces started from the seed:
    W_0 = S,  W_{j+1} = K Phi_t(W_j),   h_j = W_j - W_{j-1}  (j >= 1),
so h = sum_j h_j.  The compact-model prediction for h_1 = K(bulk Phi_t(S)) is
    h_1 ~ 2 sqrt t sum_{k even != 0} b'_k K(J^k),  b'_2 = 0.015287 (beta0 = 256/2031),
with RMS(h_1) ~ sqrt(2) * 2 sqrt(a) * b'_2 = 0.1722 and sup(h_1) <= A(h_1) = 0.4946.
Printed: sup and RMS of h_1, of h - h_1, and of each h_j, j <= 6.  These are floating
proxies only; physical coordinates sample the coset, and no price A(.) is computed here.

Replay:  .venv/bin/python -B research/paley-183-cold-h-picard-diagnostic.py
"""
import numpy as np


def paley_sign(prime):
    order = prime - 1
    fac, m, d = [], order, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    root = next(g for g in range(2, prime) if all(pow(g, order // f, prime) != 1 for f in fac))
    character = np.full(prime, -1, dtype=np.int8)
    character[0] = 0
    character[[x * x % prime for x in range(1, prime // 2 + 1)]] = 1
    n = (prime - 1) // 2
    return np.array([character[(1 - pow(root, 2 * j, prime)) % prime] for j in range(n)])


def run(p, t=2031 / 128, steps=400):
    sign = paley_sign(p).astype(float)
    n = len(sign)
    mult = sign[: n // 2 + 1]

    def K(v):
        return np.fft.irfft(mult * np.fft.rfft(v), n)

    tt = np.full(n, float(t))
    tt[0] = n
    e0 = np.zeros(n)
    e0[0] = 1.0
    S = 2 * np.sqrt(n) * K(e0)
    W = [S.copy()]
    V = S.copy()
    for k in range(steps):
        Vn = K(np.sqrt(4 * tt + V * V))
        if k < 6:
            W.append(Vn.copy())
        res = np.sqrt(np.mean((Vn - V) ** 2))
        V = Vn
        if res < 1e-14 and k >= 6:
            break
    h = V - S
    hs = [W[j] - W[j - 1] for j in range(1, len(W))]
    return n, res, S, h, hs


def st(v):
    return np.max(np.abs(v)), np.sqrt(np.mean(v * v))


print("compact-model prediction: RMS(h_1) ~ 0.1722, sup(h_1) <= A(h_1) in [0.4945, 0.4946]")
for p in (10009, 100049, 400009):
    n, res, S, h, hs = run(p)
    s_h, r_h = st(h)
    s1, r1 = st(hs[0])
    sd, rd = st(h - hs[0])
    print(f"p={p} n={n} final step RMS={res:.1e}: sup|h|={s_h:.4f} RMS(h)={r_h:.4f} | "
          f"h_1: sup={s1:.4f} RMS={r1:.4f} | h-h_1: sup={sd:.4f} RMS={rd:.4f}")
    print("   Picard pieces h_j (j=1..6) sup/RMS: " +
          "  ".join(f"{st(x)[0]:.4f}/{st(x)[1]:.4f}" for x in hs))
    print("   sup|S|*|h_1| correlation (|<S,h_1>|/(|S||h_1|)) = "
          f"{abs(np.dot(S, hs[0])) / (np.linalg.norm(S) * np.linalg.norm(hs[0])):.4f}")
