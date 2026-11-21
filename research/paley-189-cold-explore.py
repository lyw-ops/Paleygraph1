#!/usr/bin/env python3
"""Round 189 cold call `cold-prime-perron-nonseed-price`: FLOATING orientation only (label (c)).

Nothing printed here is certified.  Double precision, compact model at t = a = 2031/128, s^2 = 8.

Reduction used (report Theorem 1): for a multiplier whose term set is closed under fibre exchange
(sigma, the other lift) and weight negation (nu) with equal coefficient moduli, the per-simple
path-summed pooled |w|-histogram evolves by a single symmetric measure omega on Z:
    slot of size a  ->  slots |a + x| with weight omega(x)   (zeros dropped, then refilled).
In row form, with psi_b = phi_b + phi_0 (b - 1) (psi_0 = 0):  (phi M)_a = sum_x omega(x) psi_{|a+x|}.
For the seed J^{+-m} with coefficient |beta_m|/2 each:  omega(+-m) = |beta_m|/2.
For a multiplier object G with coefficient c:  omega += (|c|/4) * [G_A + G_B + (-G_A) + (-G_B)].

Computes:
  1. beta_m, the Perron vector phi of the seed operator (Round 188's pi_phi), c_lo, c_hi.
  2. The Picard model of h (linear chain to depth D; nonlinear pieces to depth 3), coefficients.
  3. omega for the h-linear multiplier Phi''(S) h, and for the h-quadratic/cubic Taylor terms.
  4. The per-simple pi_phi ratio N(b) of B_h on the slot-size-b ray, its sup, and the ratio on the
     Perron slot law of the seed leaves.
  5. The joint growth rate (Perron root) of the seed plus B_h operator.
Replay: .venv/bin/python -B research/paley-189-cold-explore.py
"""
import itertools
import sys
from collections import Counter, defaultdict

import numpy as np

A_T = 2031 / 128
S2 = 8.0
S = np.sqrt(S2)
SQT = np.sqrt(A_T)
BETA = S2 / (4 * A_T)
NF = 1 << 14
TH = 2 * np.pi * np.arange(NF) / NF
C = np.cos(TH)
DEPTH = int(sys.argv[1]) if len(sys.argv) > 1 else 5


def fourier(f):
    F = np.fft.fft(f) / NF
    return lambda k: F[k % NF].real


# J^k <-> e^{ik theta};  S = s cos theta
gh = fourier(C * (1 + BETA * C * C) ** -0.5)          # Phi'(S) = (s/(2 sqrt t)) sum ghat_k J^k
bh = fourier((1 + BETA * C * C) ** -1.5)              # Phi''(S) = (1/(2 sqrt t)) sum bhat_k J^k
bp = fourier((1 + BETA * C * C) ** 0.5)               # Phi(S) = 2 sqrt t sum b'_k J^k
ec = fourier(C * (1 + BETA * C * C) ** -2.5)          # Phi'''(S) = -(3s/(2 sqrt t)^3) sum e_k J^k
fc = fourier((4 * BETA * C * C - 1) * (1 + BETA * C * C) ** -3.5)  # Phi''''(S) = (3/(2 sqrt t)^3) sum f_k J^k
VARPI = S / (2 * SQT)

# ---------------------------------------------------------------- 1. seed operator, Perron vector
MH = 41
wseed = {m: abs(VARPI * gh(m)) for m in range(1, MH + 1, 2)}   # = |beta_m|/2
lS = np.sqrt(1 - np.sqrt(4 * A_T / (4 * A_T + 8)))
print(f"[float] beta_1/2 = {wseed[1]:.10f}, beta_3/2 = {wseed[3]:.3e}; l_S = {lS:.9f}")
NB = 1500
XMAX = 400


def row_apply(omega, phi):
    """(phi M)_a = sum_x omega(x) psi_{|a+x|}, a = 0..NB-1; phi extended affinely."""
    s = phi[-1] - phi[-2]
    L = NB + XMAX + 5
    ext = np.concatenate([phi, phi[-1] + s * np.arange(1, L - NB + 1)])
    psi = ext + ext[0] * (np.arange(L) - 1.0)
    psi[0] = 0.0
    out = np.zeros(NB)
    a = np.arange(NB)
    for x, w in omega.items():
        out += w * psi[np.abs(a + x)]
    return out


def perron(omega, iters=3000):
    phi = np.ones(NB)
    phi[1:] = np.arange(1, NB)
    lam = 0
    for _ in range(iters):
        nw = row_apply(omega, phi)
        lam = nw[300] / phi[300]
        phi = nw / nw[300] * 300
    r = row_apply(omega, phi)[1:300] / phi[1:300]
    return float(np.median(r)), phi


omega_seed = Counter()
for m, w in wseed.items():
    omega_seed[m] += w
    omega_seed[-m] += w
lamA, phi = perron(omega_seed)
psi = phi + phi[0] * (np.arange(NB) - 1.0)
psi[0] = 0
c_lo = min(psi[b] / b for b in range(1, NB))
c_hi = max(psi[b] / b for b in range(1, NB))
print(f"[float] seed Perron root lambda_A = {lamA:.10f};  c_lo = {c_lo:.6f}, c_hi = {c_hi:.6f}, "
      f"K = {c_hi / c_lo:.6f}")
print("[float] psi_b/b, b = 1..8:", " ".join(f"{psi[b] / b:.4f}" for b in range(1, 9)))
KSTAR = 0.7741471
BUDGET = KSTAR - 0.4995143263
print(f"budget kappa* - lam_up = {BUDGET:.6f} (kappa* lower end 0.7741471, Round 182; (b1))")


def ratio_b(omega, bmax=600):
    """per-simple pi_phi ratio of the multiplier on the slot-size-b ray (and its limit)."""
    Om = sum(w * psi[abs(x)] for x, w in omega.items())
    out = []
    for b in range(1, bmax):
        num = sum(w * psi[abs(b + x)] for x, w in omega.items()) + (b - 1) * Om
        out.append(num / psi[b])
    tot = sum(omega.values())
    slope = psi[1000] - psi[999]
    lim = tot + Om / slope
    return np.array(out), lim


# right Perron vector of the seed (slot law of the leaves): column iteration
def right_perron(omega, iters=600, B=400):
    n = np.zeros(B)
    n[0] = 0
    n[2] = 1.0  # K(J^2): slots |-2|,|2| in A and zeros
    n[0] = 2.0
    for _ in range(iters):
        new = np.zeros(B)
        for a in range(B):
            if n[a] == 0:
                continue
            for x, w in omega.items():
                c = abs(a + x)
                if 0 < c < B:
                    new[c] += w * n[a]
        new[0] = sum((c - 1) * new[c] for c in range(1, B))
        n = new / new.sum()
    return n


nP = right_perron(omega_seed)
print("[float] seed right Perron slot law n_0..n_5:", " ".join(f"{v:.4f}" for v in nP[:6]))

# ---------------------------------------------------------------- 2. Picard model of h (weights)


def mk(Acnt, Bcnt):
    return (tuple(sorted((w, c) for w, c in Acnt.items() if c)),
            tuple(sorted((w, c) for w, c in Bcnt.items() if c)))


def line(k):
    return (((-k, 1),), ((k, 1),))


def shift(W, k):
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
    r2 = sum(abs(w) * c for w, c in W[0]) + sum(abs(w) * c for w, c in W[1])
    r = r2 // 2
    A, B = Counter(), Counter()
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
    za, zb = r - sum(A.values()), r - sum(B.values())
    assert za >= 0 and zb >= 0
    if za:
        A[0] += za
    if zb:
        B[0] += zb
    return mk(A, B)


def dim(W):
    return sum(c for _, c in W[0])


ROOTS = (2, -2, 4, -4, 6, -6)
SEEDK = (1, -1, 3, -3, 5, -5)
IH = (0, 2, -2, 4, -4, 6, -6)
EC = (1, -1, 3, -3, 5, -5)
TS = 2 * SQT

lin_by_depth = []
cur = {(kp,): (transport(line(kp)), TS * bp(kp)) for kp in ROOTS}
lin_by_depth.append(cur)
for j in range(1, DEPTH + 1):
    nxt = {}
    for p, (W, c) in cur.items():
        for k in SEEDK:
            nxt[p + (k,)] = (transport(shift(W, k)), c * VARPI * gh(k))
    lin_by_depth.append(nxt)
    cur = nxt
for j, d in enumerate(lin_by_depth):
    print(f"[float] linear depth {j}: {len(d)} simples, A-price {sum(abs(c) * dim(W) for W, c in d.values()):.6f}")


def objects_sum(objs):
    return sum(abs(c) * dim(W) for W, c in objs)


# nonlinear pieces to depth 3 (as Round 185): Q1 = 1/2 K(Phi'' h1^2), L_S Q1, X1 = K(Phi'' h1 L_S h1), C1 = 1/6 K(Phi''' h1^3)
h1 = list(lin_by_depth[0].values())
l1 = list(lin_by_depth[1].values())
inv2t = 1 / (2 * SQT)
Q1 = []
for i2 in IH:
    for (W1, c1), (W2, c2) in itertools.product(h1, h1):
        Q1.append((transport(shift(tensor(W1, W2), i2)), 0.5 * inv2t * bh(i2) * c1 * c2))
LSQ1 = [(transport(shift(W, k)), c * VARPI * gh(k)) for W, c in Q1 for k in SEEDK]
X1 = []
for i2 in IH:
    for (W1, c1), (W2, c2) in itertools.product(h1, l1):
        X1.append((transport(shift(tensor(W1, W2), i2)), inv2t * bh(i2) * c1 * c2))
C1 = []
e3 = -3 * S / TS ** 3
for cc in EC:
    for (W1, c1), (W2, c2), (W3, c3) in itertools.product(h1, h1, h1):
        C1.append((transport(shift(tensor(tensor(W1, W2), W3), cc)), e3 * ec(cc) * c1 * c2 * c3 / 6))
for name, objs in (("Q1", Q1), ("L_S Q1", LSQ1), ("X1", X1), ("C1", C1)):
    print(f"[float] {name}: {len(objs)} objects (ordered, unmerged), unsigned A-price {objects_sum(objs):.6f}")

# ---------------------------------------------------------------- 3. multiplier measures omega


def fibre_hist(objs):
    HA, HB = Counter(), Counter()
    for W, c in objs:
        for w, m in W[0]:
            HA[w] += abs(c) * m
        for w, m in W[1]:
            HB[w] += abs(c) * m
    return HA, HB


def omega_linear(HA, HB):
    """h-linear multiplier Phi''(S) h: terms (bhat_{2i}/(2 sqrt t)) J^{2i} (x) X."""
    om = Counter()
    for i2 in IH:
        k = abs(bh(i2)) * inv2t / 4
        for w, m in HA.items():
            om[w - i2] += k * m
            om[i2 - w] += k * m
        for w, m in HB.items():
            om[w + i2] += k * m
            om[-w - i2] += k * m
    return om


def conv(H1, H2):
    out = Counter()
    for w1, m1 in H1.items():
        for w2, m2 in H2.items():
            out[w1 + w2] += m1 * m2
    return out


def omega_taylor(HA, HB, order):
    """(1/m!) Phi^{(m+1)}(S) h^m, m = 2 (odd lines e_c) or m = 3 (even lines f_c); ordered products."""
    if order == 2:
        coefs = {cc: abs(3 * S / TS ** 3 * ec(cc)) / 2 for cc in (1, -1, 3, -3, 5, -5, 7, -7)}
        GA, GB = conv(HA, HA), conv(HB, HB)
    else:
        coefs = {cc: abs(3 / TS ** 3 * fc(cc)) / 6 for cc in (0, 2, -2, 4, -4, 6, -6)}
        GA, GB = conv(conv(HA, HA), HA), conv(conv(HB, HB), HB)
    om = Counter()
    for cc, k in coefs.items():
        k = k / 4
        for w, m in GA.items():
            om[w - cc] += k * m
            om[cc - w] += k * m
        for w, m in GB.items():
            om[w + cc] += k * m
            om[-w - cc] += k * m
    return om


def report(name, om):
    rb, lim = ratio_b(om)
    bmax = int(np.argmax(rb)) + 1
    # ratio on the seed right Perron law (pooled histogram nP, valid by construction)
    Om = sum(w * psi[abs(x)] for x, w in om.items())
    num = 0.0
    den = 0.0
    for b in range(1, len(nP)):
        if nP[b] < 1e-14:
            continue
        num += nP[b] * (sum(w * psi[abs(b + x)] for x, w in om.items()) + (b - 1) * Om)
        den += nP[b] * psi[b]
    print(f"[float] {name}: |omega| = A-cost (dim part) {sum(om.values()):.6f}; pi_phi ratio N(1) = {rb[0]:.6f}, "
          f"N(2) = {rb[1]:.6f}, N(3) = {rb[2]:.6f}, max_b N(b) = {rb.max():.6f} at b = {bmax}, limit {lim:.6f}; "
          f"on the seed Perron slot law {num / den:.6f}")
    return rb.max(), lim


pieces = {}
pieces["h1"] = h1
pieces["L_S^j h1, j=1..D"] = [x for d in lin_by_depth[1:] for x in d.values()]
pieces["nonlinear depth 2-3"] = Q1 + LSQ1 + X1 + C1
res = {}
for name, objs in pieces.items():
    HA, HB = fibre_hist(objs)
    res[name] = report(f"h-linear multiplier on {name}", omega_linear(HA, HB))
for j in range(1, DEPTH + 1):
    HA, HB = fibre_hist(list(lin_by_depth[j].values()))
    report(f"h-linear multiplier on L_S^{j} h1", omega_linear(HA, HB))
allobjs = [x for d in lin_by_depth for x in d.values()] + Q1 + LSQ1 + X1 + C1
HA, HB = fibre_hist(allobjs)
om1 = omega_linear(HA, HB)
report("h-linear multiplier, h = linear(<=D) + nonlinear(<=3)", om1)
om2 = omega_taylor(HA, HB, 2)
report("h-quadratic Taylor term (1/2)Phi'''(S) h^2", om2)
om3 = omega_taylor(HA, HB, 3)
report("h-cubic Taylor term (1/6)Phi''''(S) h^3", om3)
omB = Counter()
for om in (om1, om2, om3):
    for x, w in om.items():
        omB[x] += w
mB, limB = report("B_h (orders 1-3)", omB)
print(f"[float] lam_A + max_b N_B(b) = {lamA + mB:.6f}  vs kappa* = {KSTAR}")
# exact joint one-step norm of L_S + B_h in pi_phi
omL = Counter(omega_seed)
for x, w in omB.items():
    omL[x] += w
rL, limL = ratio_b(omL)
print(f"[float] joint one-step pi_phi norm of L_S + B_h: max_b = {rL.max():.6f} at b = {int(np.argmax(rL)) + 1}, limit {limL:.6f}")
lamL, phiL = perron(omL)
psiL = phiL + phiL[0] * (np.arange(NB) - 1.0)
psiL[0] = 0
print(f"[float] joint growth rate (Perron root) of L_S + B_h: {lamL:.6f};  K_L = "
      f"{max(psiL[b] / b for b in range(1, NB)) / min(psiL[b] / b for b in range(1, NB)):.4f}")
for name, keep in (("L_S + h1-linear", ["h1"]),):
    HA, HB = fibre_hist(h1)
    omx = Counter(omega_seed)
    for x, w in omega_linear(HA, HB).items():
        omx[x] += w
    print(f"[float] joint growth rate of {name}: {perron(omx)[0]:.6f}")
