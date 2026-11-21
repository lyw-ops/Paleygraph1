#!/usr/bin/env python3
"""Round 185 cold call: FLOATING physical diagnostic (evidence only, label (c)); own implementation.

Physical cold map as in the Round 182-184 diagnostics: K = real symmetric circulant whose
eigenvalues are the Paley sign row chi(1 - g^(2j)) on the subgroup of squares, t = a = 2031/128
except the mark t_0 = n at coordinate 0, one real lift, double precision.

Pieces (physical analogues of the model pieces):
  h = V_* - S (fixed point of V = K Phi_t(V) from S = 2 sqrt(n) K e_0),
  linear chain  l_0 = h_1 = K Phi_t(S) - S,  l_{j+1} = L_S l_j = K(Phi_t'(S) l_j),  Lin = sum_j l_j,
  nonlinear part  Nl = h - Lin,
  Q_1 = (1/2) K(Phi''(S) h_1^2),  X_1 = K(Phi''(S) h_1 l_1),  C_1 = (1/6) K(Phi'''(S) h_1^3),  L_S Q_1.
Two tests of the identification question:
  (i)  mean squares against the compact model: if every model object is one simple with unit mean
       square trace and distinct objects are inequivalent, the model predicts
       E|piece|^2 = sum |c|^2.  A coincidence of objects with equal (opposite) signs raises (lowers)
       the physical mean square; reducible objects raise it.
  (ii) normalized inner products <l_j, N>/<l_j, l_j> of linear pieces with nonlinear pieces.  Distinct
       simples are asymptotically orthogonal, so with no linear/nonlinear coincidence these tend to 0
       (like n^(-1/2)); a coincidence of total coefficient mass d on the simples of l_j gives a
       nonzero limit sum c_M d_M / sum |c_M|^2.
Replay:  .venv/bin/python -B research/paley-185-cold-physical-gram.py      (about 1 min)
"""
import contextlib
import io
import os
import runpy

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))


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
    while not all(pow(g, order // q, p) != 1 for q in fac):
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


# model mean squares from the leaves script (coefficient midpoints, floats)
os.environ["P185_DEPTH"] = "5"
with contextlib.redirect_stdout(io.StringIO()):
    L = runpy.run_path(os.path.join(_here, "paley-185-cold-picard-leaves.py"))


def f(z):
    return float(z.real.mid())


model_ms = {}
for j in range(6):
    model_ms[f"l_{j}"] = sum(f(L["COEF"][p]) ** 2 for p in L["LIN"] if len(p) == j + 1)
for kind, lab in (("Q_1", "Q_1"), ("L_S Q_1", "L_S Q_1"), ("X_1", "X_1"), ("C_1", "C_1")):
    model_ms[lab] = sum(f(v["coef"]) ** 2 for v in L["NL"].values() if v["kind"] == kind)
# naive alternative for Q_1 (rejected by the data): every diagonal product K(J^i (x) K(J^k) (x) K(J^k)) counted
# as two unit simples.  (Under the trivial-pairing picture only the i != 0 diagonal objects gain a
# root-type constituent K(J^i); their extra mean square is below 1e-8.)
model_ms_Q_split = sum(f(v["coef"]) ** 2 * (2 if len(set(k[2])) == 1 else 1)
                       for k, v in L["NL"].items() if v["kind"] == "Q_1")


def run(p, t=2031 / 128, steps=800):
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
    for k in range(steps):
        Vn = K(np.sqrt(4 * tt + V * V))
        res = np.sqrt(np.mean((Vn - V) ** 2))
        V = Vn
        if res < 1e-14 and k > 5:
            break
    h = V - S
    q = 4 * tt + S * S
    d1 = S / np.sqrt(q)
    d2 = 4 * tt / q ** 1.5
    d3 = -12 * tt * S / q ** 2.5
    h1 = K(np.sqrt(q)) - S
    ls = [h1]
    for j in range(80):
        ls.append(K(d1 * ls[-1]))
    Lin = sum(ls)
    Nl = h - Lin
    Q1 = 0.5 * K(d2 * h1 * h1)
    X1 = K(d2 * h1 * ls[1])
    C1 = K(d3 * h1 ** 3) / 6
    LQ1 = K(d1 * Q1)
    return n, h, ls, Lin, Nl, {"Q_1": Q1, "L_S Q_1": LQ1, "X_1": X1, "C_1": C1}


def ms(v):
    return float(np.mean(v * v))


primes = [next_prime_1mod4(m) for m in (100000, 400000, 1000000, 4000000)]
print("[float] t = a, one real lift; mean squares E|.|^2 (physical) vs compact model sum |c|^2 (no coincidences)")
for p in primes:
    n, h, ls, Lin, Nl, P = run(p)
    print(f"[float] p = {p}:")
    print("[float]   " + "; ".join(f"l_{j} {ms(ls[j]):.6f}/{model_ms[f'l_{j}']:.6f}" for j in range(4)))
    print("[float]   " + "; ".join(f"{k} {ms(v):.3e}/{model_ms[k]:.3e}" for k, v in P.items())
          + f"  (naive: every diagonal Q_1 product as two simples: {model_ms_Q_split:.3e})")
    print(f"[float]   E|Nl|^2 = {ms(Nl):.3e} (sum of depth<=3 model pieces Q_1+L_SQ_1+X_1+C_1: "
          f"{sum(model_ms[k] for k in P):.3e});  E|Lin - h_1|^2 = {ms(Lin - ls[0]):.3e}")
    rows = []
    for j in range(4):
        lj = ls[j]
        nn = float(np.dot(lj, lj))
        rows.append(f"<l_{j},Nl>/|l_{j}|^2 {np.dot(lj, Nl) / nn:+.4f}")
    print("[float]   " + "; ".join(rows))
    rows = []
    for k, v in P.items():
        best = max(range(5), key=lambda j: abs(np.dot(ls[j], v) / np.sqrt(np.dot(ls[j], ls[j]) * np.dot(v, v))))
        rows.append(f"{k}: max_j corr(l_j, .) {np.dot(ls[best], v) / np.sqrt(np.dot(ls[best], ls[best]) * np.dot(v, v)):+.4f} (j={best})")
    print("[float]   " + "; ".join(rows))
    LmH = Lin - ls[0]
    print(f"[float]   <Lin - h_1, Nl>/|Lin - h_1|^2 = {np.dot(LmH, Nl) / np.dot(LmH, LmH):+.4f};  "
          f"<h_1, Nl>/|h_1|^2 = {np.dot(ls[0], Nl) / np.dot(ls[0], ls[0]):+.4f};  "
          f"corr(Lin, Nl) = {np.dot(Lin, Nl) / np.sqrt(np.dot(Lin, Lin) * np.dot(Nl, Nl)):+.4f}")

# ------------------------------------------------------------------ mean-field (trivial-pairing) prediction
# Hypothesis (MF): each root X_k = K(J^k) has X_k (x) X_k containing the trivial object once, and
# X_k (x) X_l (k != l) does not (unit mean squares, mutual orthogonality: matches E|h_1|^2 above).
# Then (rank-2 roots, SL_2-type: X^(x)3 = Sym^3 + 2X; X (x) X (x) Y contains Y once)
#   Q_1 contains the roots K(J^i), i != 0, with coefficient (1/2)(1/(2 sqrt t)) bhat_i sum_k c_k^2,
#   C_1 contains the depth-1 simples K(J^c X_k) with coefficient (1/6) Phi3 e_c [3 c_k sum_{l!=k} c_l^2 + 2 c_k^3]
# (c_k = 2 sqrt t b'_k).  Predicted inner products <h_1, Q_1>, <l_1, C_1> (per coordinate):
c = {k: f(L["COEF"][(k,)]) for k in L["ROOTS"]}
TSf = f(L["TS"])
Sf = f(L["S"])
sig1 = sum(v * v for v in c.values())
pred_hQ = sum(c[i] * 0.5 / TSf * f(L["M"].bhat(i)) * sig1 for i in L["ROOTS"])
PHI3f = -3 * Sf / TSf ** 3
pred_lC = 0.0
for (k, cc) in [(k, cc) for k in L["ROOTS"] for cc in L["SEED"]]:
    d = PHI3f / 6 * f(L["M"].ecoef(cc)) * (3 * c[k] * (sig1 - c[k] ** 2) + 2 * c[k] ** 3)
    pred_lC += f(L["COEF"][(k, cc)]) * d
print("\n[float] mean-field (trivial pairing of roots) predictions vs physical inner products (per coordinate):")
for p in primes:
    n, h, ls, Lin, Nl, P = run(p)
    print(f"[float]   p = {p}: <h_1, Q_1> {np.mean(ls[0] * P['Q_1']):+.4e} (pred {pred_hQ:+.4e});  "
          f"<l_1, C_1> {np.mean(ls[1] * P['C_1']):+.4e} (pred {pred_lC:+.4e});  "
          f"<h_1, Nl>/|h_1|^2 {np.dot(ls[0], Nl) / np.dot(ls[0], ls[0]):+.5f} (pred {pred_hQ / sig1:+.5f})")
