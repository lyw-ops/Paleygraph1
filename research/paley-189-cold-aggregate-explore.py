#!/usr/bin/env python3
"""Round 189 cold call `cold-prime-perron-nonseed-price`: FLOATING orientation (label (c)) for the
full unsigned Picard model of h, by aggregated fibre histograms.

Key observation (report Lemma 2): in the compact model every operation of the Picard recursion is
LINEAR on |c|-weighted two-fibre weight histograms, when summed over all objects with |coefficient|:
  * line shift J^c: A -> A - c, B -> B + c;
  * tensor product (b-T): per fibre, convolution of the histograms (pairs of objects);
  * transport (R80): nonzero slots move linearly; the refill of fibre A is
        z_A' = sum n(w,f) (|w|/2) - #neg(A) - #pos(B),  linear in the slot counts.
So the unsigned per-simple (Picard-representation) data of h, depth by depth, needs no enumeration.

h = h_1 + L_S h + sum_{m>=2} K(Phi^{(m)}(S) h^m)/m!   (frozen-base fixed point, mark removed);
depth(O) = #transports - 1;  a product K(Phi^{(m)} X_1...X_m) has depth sum d_i + m.
B_h = sum_{m>=1} K((1/m!) Phi^{(m+1)}(S) h^m .).
Prints: unsigned A-price of h by depth (linear/nonlinear), the per-simple pi_phi ratio N(b) of B_h,
the seed-Perron-law ratio, and the joint growth rate of L_S + B_h.
Usage: .venv/bin/python -B research/paley-189-cold-aggregate-explore.py [DMAX] [MMAX]
"""
import sys
from math import factorial

import numpy as np

A_T = 2031 / 128
S = np.sqrt(8.0)
SQT = np.sqrt(A_T)
NF = 1 << 13
TH = 2 * np.pi * np.arange(NF) / NF
X = S * np.cos(TH)
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
MMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 6
WM = 260                      # weights kept in [-WM, WM]
L = 2 * WM + 1
KC = 31                       # Fourier lines kept |c| <= KC
import os
ROOTSCALE = float(os.environ.get("P189_ROOTSCALE", "1"))   # scale of h_1 (experiment; 1 = the model)
NLSCALE = float(os.environ.get("P189_NLSCALE", "1"))       # scale of the h-Taylor terms m >= 2 (experiment)


def taylor_derivs(x, t, M):
    """Phi^{(m)}(x), m = 0..M, Phi(x) = sqrt(4t + x^2), via power series of sqrt(u(y))."""
    u = np.zeros((M + 1, len(x)))
    u[0] = 4 * t + x * x
    u[1] = 2 * x
    if M >= 2:
        u[2] = 1.0
    r = np.zeros_like(u)
    r[0] = np.sqrt(u[0])
    for m in range(1, M + 1):
        acc = u[m] - sum(r[j] * r[m - j] for j in range(1, m))
        r[m] = acc / (2 * r[0])
    return [factorial(m) * r[m] for m in range(M + 1)]


D = taylor_derivs(X, A_T, MMAX + 2)


def coefs(f):
    F = np.fft.fft(f) / NF
    return {c: F[c % NF].real for c in range(-KC, KC + 1) if abs(F[c % NF].real) > 1e-300}


PHI = [coefs(D[m]) for m in range(MMAX + 2)]    # Phi^{(m)}(S) = sum_c PHI[m][c] J^c
print(f"[float] Phi'(S) J^1 coefficient {PHI[1][1]:.10f} (= beta_1/2); Phi''(S) J^0 {PHI[2][0]:.8f}")

# ------------------------------------------------------------------ histogram algebra
Z = WM                         # index of weight 0


def shift(H, c):
    HA, HB = H
    return np.roll(HA, -c), np.roll(HB, c)   # A - c, B + c (support kept far from the edges)


def transport(H):
    HA, HB = H
    w = np.arange(-WM, WM + 1)
    r = 0.5 * (np.abs(w) @ HA + np.abs(w) @ HB)
    nA = np.where(w < 0, HA, 0) + np.where(w > 0, HB, 0)
    nB = np.where(w < 0, HB, 0) + np.where(w > 0, HA, 0)
    zA = r - nA.sum()
    zB = r - nB.sum()
    assert zA > -1e-12 * max(r, 1e-300) and zB > -1e-12 * max(r, 1e-300), (zA, zB)
    nA[Z] += zA
    nB[Z] += zB
    return nA, nB


def conv(H1, H2):
    out = []
    for f in (0, 1):
        c = np.convolve(H1[f], H2[f])[WM:WM + L]
        out.append(c)
    return tuple(out)


def add(H1, H2, s=1.0):
    return H1[0] + s * H2[0], H1[1] + s * H2[1]


def zero():
    return np.zeros(L), np.zeros(L)


def dimsum(H):
    return H[0].sum()


def edge_mass(H):
    return H[0][:20].sum() + H[0][-20:].sum() + H[1][:20].sum() + H[1][-20:].sum()


def lin_step(H):
    acc = zero()
    for c, v in PHI[1].items():
        if c % 2:
            acc = add(acc, shift(H, c), abs(v))
    return transport(acc)


def taylor_mult(Hprod, m):
    """K( (1/m!) Phi^{(m)}(S) * Hprod ), unsigned"""
    acc = zero()
    for c, v in PHI[m].items():
        acc = add(acc, shift(Hprod, c), NLSCALE * abs(v) / factorial(m))
    return transport(acc)


# roots h_1 = 2 sqrt t sum b'_k K(J^k) = K(Phi(S)) minus the constant
roots = zero()
for c, v in PHI[0].items():
    if c != 0 and c % 2 == 0:
        roots = add(roots, transport(shift((np.eye(1, L, Z)[0], np.eye(1, L, Z)[0]), c)), ROOTSCALE * abs(v))
# line J^c as a histogram: A: -c, B: +c  -> shift of the unit object (0 | 0)
Hlin = [roots]
Hnl = [zero()]
Htot = [roots]
# conv_m[e] = sum over ordered (d_1..d_m), sum d_i = e, of H_{d_1} * ... * H_{d_m}
convs = {1: [roots]}
for m in range(2, MMAX + 1):
    convs[m] = []
print(f"[float] depth  0: linear A {dimsum(Hlin[0]):.6f}")
for d in range(1, DMAX + 1):
    hl = lin_step(Hlin[d - 1])
    hn = lin_step(Hnl[d - 1])
    for m in range(2, MMAX + 1):
        e = d - m
        if e < 0:
            continue
        hn = add(hn, taylor_mult(convs[m][e], m))
    Hlin.append(hl)
    Hnl.append(hn)
    Htot.append(add(hl, hn))
    # update ordered convolution powers for the new depth index d (all entries e <= d)
    convs[1].append(Htot[d])
    for m in range(2, MMAX + 1):
        while len(convs[m]) <= d:
            e = len(convs[m])
            acc = zero()
            for d1 in range(0, e + 1):
                if e - d1 < len(convs[m - 1]):
                    acc = add(acc, conv(Htot[d1], convs[m - 1][e - d1]))
            convs[m].append(acc)
    if d <= 8 or d % 4 == 0:
        print(f"[float] depth {d:2d}: linear A {dimsum(hl):.6f}, nonlinear A {dimsum(hn):.6f}, "
              f"edge mass {edge_mass(Htot[d]):.1e}")
TOT = zero()
for H in Htot:
    TOT = add(TOT, H)
print(f"[float] unsigned model A-price of h to depth {DMAX}: linear {sum(dimsum(H) for H in Hlin):.6f}, "
      f"nonlinear {sum(dimsum(H) for H in Hnl):.6f}, total {dimsum(TOT):.6f}")

# ------------------------------------------------------------------ omega of multipliers


def omega_of(Hmult):
    """symmetrized slot measure: (1/4)[G_A + G_B + (-G_A) + (-G_B)] (array over x in [-WM, WM])"""
    HA, HB = Hmult
    return 0.25 * (HA + HB + HA[::-1] + HB[::-1])


def mult_hist(m, H):
    """aggregated weight histogram of (1/m!) Phi^{(m+1)}(S) h^m (pre-transport multiplier objects)"""
    P = H
    for _ in range(m - 1):
        P = conv(P, H)
    acc = zero()
    for c, v in PHI[m + 1].items():
        acc = add(acc, shift(P, c), abs(v) / factorial(m))
    return acc


# seed omega
om_seed = np.zeros(L)
for c, v in PHI[1].items():
    if c % 2:
        om_seed[Z + c] += abs(v)
NB = 1500


def make_psi(phi):
    s = phi[-1] - phi[-2]
    ext = np.concatenate([phi, phi[-1] + s * np.arange(1, 2 * WM + 10)])
    psi = ext + ext[0] * (np.arange(len(ext)) - 1.0)
    psi[0] = 0.0
    return psi


xs = np.arange(-WM, WM + 1)


def row_apply(om, phi):
    psi = make_psi(phi)
    a = np.arange(NB)
    out = np.zeros(NB)
    for i in np.nonzero(om > 1e-300)[0]:
        out += om[i] * psi[np.abs(a + xs[i])]
    return out


def perron(om, iters=1500):
    phi = np.ones(NB)
    phi[1:] = np.arange(1, NB)
    for _ in range(iters):
        nw = row_apply(om, phi)
        phi = nw / nw[300] * 300
    r = row_apply(om, phi)[1:300] / phi[1:300]
    return float(np.median(r)), float(r.min()), float(r.max()), phi


lamA, _, _, phi = perron(om_seed)
psi = make_psi(phi)
print(f"[float] seed Perron root {lamA:.10f}")


def N_ratio(om, bmax=400):
    Om = float(om @ psi[np.abs(xs)])
    vals = []
    for b in range(1, bmax):
        vals.append((float(om @ psi[np.abs(b + xs)]) + (b - 1) * Om) / psi[b])
    slope = psi[1200] - psi[1199]
    return np.array(vals), om.sum() + Om / slope


# seed right Perron slot law (column iteration on pooled histograms)
def right_law(om, iters=400, B=300):
    n = np.zeros(B)
    n[2] = 1
    n[0] = 1
    idx = np.nonzero(om > 1e-300)[0]
    for _ in range(iters):
        new = np.zeros(B)
        for a in np.nonzero(n)[0]:
            for i in idx:
                c = abs(a + xs[i])
                if 0 < c < B:
                    new[c] += om[i] * n[a]
        new[0] = ((np.arange(B) - 1) * new)[1:].sum()
        n = new / new.sum()
    return n


nP = right_law(om_seed)


def law_ratio(om):
    Om = float(om @ psi[np.abs(xs)])
    num = sum(nP[b] * (float(om @ psi[np.abs(b + xs)]) + (b - 1) * Om) for b in range(1, len(nP)))
    den = sum(nP[b] * psi[b] for b in range(1, len(nP)))
    return num / den


BUDGET = 0.7741471 - 0.4995143263
print(f"budget {BUDGET:.6f}")
for Dcut in sorted(set([5, 20, 44, 90, DMAX])):
    if Dcut > DMAX:
        continue
    H = zero()
    for d in range(Dcut + 1):
        H = add(H, Htot[d])
    omB = np.zeros(L)
    parts = []
    for m in range(1, MMAX + 1):
        om = omega_of(mult_hist(m, H))
        rb, lim = N_ratio(om)
        parts.append(f"m={m}: N(1)={rb[0]:.5f}")
        omB += om
    rb, lim = N_ratio(omB)
    omL = om_seed + omB
    lamL, rmin, rmax, _ = perron(omL)
    print(f"[float] h to depth {Dcut:2d} (A {dimsum(H):.4f}): B_h pi_phi N(1) = {rb[0]:.5f}, max_b N = {rb.max():.5f} "
          f"(b={int(np.argmax(rb)) + 1}), limit {lim:.5f}, seed-law ratio {law_ratio(omB):.5f}; "
          f"joint growth rate {lamL:.5f} (CW ratios on sizes 1..299 in [{rmin:.5f}, {rmax:.5f}]); "
          f"A-sup ratio of L at large slots |omega_L| + sum omega_L |x| = {omL.sum() + omL @ np.abs(xs):.5f}")
    print("        " + "; ".join(parts))

# ------------------------------------------------------------------ proportional-cancellation test (orientation)
# omega_theta = omega_V1 + theta (omega_full - omega_V1): V1 = h-linear term over the linear Picard simples of
# depth <= 5 (pairwise distinct, Round 185); theta = fraction of the remaining (nonlinear and product) per-simple
# mass that survives cancellation, if cancellation were proportional.  Smallest theta reaching the thresholds.
H5 = zero()
for d in range(6):
    H5 = add(H5, Hlin[d])
om_V1 = omega_of(mult_hist(1, H5))
for Dcut in (20, 40):
    if Dcut > DMAX:
        continue
    H = zero()
    for d in range(Dcut + 1):
        H = add(H, Htot[d])
    om_full = np.zeros(L)
    for m in range(1, 4):
        om_full += omega_of(mult_hist(m, H))
    out = []
    for target, kind in ((0.2746331, "N(1)"), (0.7741472, "growth vs kappa*(b1)"), (0.838, "growth vs kappa*_A")):
        lo, hi = 0.0, 1.0
        for _ in range(30):
            th = (lo + hi) / 2
            om = om_V1 + th * (om_full - om_V1)
            val = N_ratio(om)[0][0] if kind == "N(1)" else perron(om_seed + om, iters=600)[0]
            if val >= target:
                hi = th
            else:
                lo = th
        out.append(f"{kind}: theta* = {hi:.4f}")
    print(f"[float] depth {Dcut}: proportional survival needed to reach the thresholds: " + "; ".join(out))
