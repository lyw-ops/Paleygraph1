#!/usr/bin/env python3
"""Round 189 cold call `cold-prime-perron-nonseed-price`, part 2 (label (a): outward arb/acb balls and exact
rationals): certified LOWER bounds, uniform on Q x {p >= 10^6} and both lifts, for
  (i)  the per-simple pi_phi one-step norm of the non-seed multiplier B_h (Round 188's Perron-weighted price), and
  (ii) the per-simple growth rate of L_S + B_h, which bounds below the one-step (and power) norm of the frozen
       multiplier in EVERY per-simple sup-dominating price (report Proposition 3),
in the compact model, with h represented by its Picard expansion (report Section 2).

Method (report Lemma 2 and Theorem 1).
  * Aggregated histograms: for a set of model objects with coefficients c_O, H_f(w) = sum_O |c_O| (# slots of
    weight w in fibre f of O).  Line shift, tensor product (b-T) and transport (R80) act LINEARLY on H (the refill
    z_A(O) = sum_slots (|w|/2 - [w<0, fibre A] - [w>0, fibre B]) is linear in the slot counts).  Replacing every
    |c_O| by a certified lower bound (products of lower bounds of |Fourier coefficients|) gives the aggregate of the
    same objects with smaller nonnegative weights, hence an entrywise lower bound.  Ball arithmetic contains that
    aggregate exactly; lower endpoints are taken only at the end.
  * Truncated term set T(D): roots |k'| <= KR, seed lines |k| <= KL, Taylor lines |c| <= KT, Picard depth <= D,
    h-Taylor orders m <= MHM, multiplier orders m <= MB.  T(D) is closed under fibre exchange and weight negation
    with equal coefficient moduli (all coefficients are even in the line index), see report Lemma 1.
  * Symmetrized slot measure of a multiplier: omega = (1/4) [G_A + G_B + (-G_A) + (-G_B)];
    per-simple pi_phi ratio on the slot-size-b ray: N(b) = [sum_x omega(x) psi_{|b+x|} + (b-1) sum_x omega(x) psi_|x|]/psi_b.
Replay: .venv/bin/python -B research/paley-189-cold-nonseed-certify.py [D]      (D = 8 default; about 2-4 min)
"""
import hashlib
import importlib.util
import os
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr
from math import factorial

from flint import arb

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("c189", os.path.join(_here, "paley-189-cold-common.py"))
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

T_START = time.time()
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
KR, KL, KT, MHM, MB = 8, 7, 8, 4, 3
BC = 300
KSTAR_HI = Fr(7741472, 10 ** 7)
KSTAR_A_HI = Fr(83793100, 10 ** 8)       # Round 184: kappa*_A in [0.83790250, 0.83793100]
LAM_REGION_LO = Fr(999028261, 2000000000)  # seed certificate (part 1), region lower end
LAM_REGION_UP = Fr(199805913, 400000000)
BUDGET_HI = KSTAR_HI - LAM_REGION_LO      # largest possible value of the budget on the region

ok_all = True


def check(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(f"  [{'OK' if cond else 'FAIL'}] {name}")


RG = C.make_params("region")
TAYLOR_KIND = {2: "phi2", 3: "phi3", 4: "phi4"}


def clo(kind, k):
    return C.abs_lo(C.coef(RG, kind, k))


# ------------------------------------------------------------------ histogram algebra (dict w -> arb), H = (A, B)
def h_zero():
    return (defaultdict(lambda: arb(0)), defaultdict(lambda: arb(0)))


def h_add_scaled(acc, H, s, c=0):
    """acc += s * (J^c (x) H)"""
    for w, v in H[0].items():
        acc[0][w - c] += s * v
    for w, v in H[1].items():
        acc[1][w + c] += s * v


def h_transport(H):
    r = arb(0)
    for f in (0, 1):
        for w, v in H[f].items():
            r += abs(w) * v
    r = r / 2
    out = h_zero()
    for w, v in H[0].items():
        if w < 0:
            out[0][w] += v
        elif w > 0:
            out[1][w] += v
    for w, v in H[1].items():
        if w < 0:
            out[1][w] += v
        elif w > 0:
            out[0][w] += v
    zA = r - sum(out[0].values(), arb(0))
    zB = r - sum(out[1].values(), arb(0))
    out[0][0] += zA
    out[1][0] += zB
    return out, min(zA.upper(), zB.upper())


def h_conv(H1, H2):
    out = h_zero()
    for f in (0, 1):
        it2 = list(H2[f].items())
        for w1, v1 in H1[f].items():
            for w2, v2 in it2:
                out[f][w1 + w2] += v1 * v2
    return out


def h_sum(Hs):
    out = h_zero()
    for H in Hs:
        h_add_scaled(out, H, arb(1))
    return out


def h_dim(H):
    return sum(H[0].values(), arb(0))


def h_clean(H):
    """drop exact zeros (keeps every nonzero ball)"""
    return tuple(defaultdict(lambda: arb(0), {w: v for w, v in H[f].items() if not (v == 0)}) for f in (0, 1))


# ------------------------------------------------------------------ 1. Picard aggregates of h by depth
print(f"== 1. aggregated Picard model of h (lower bounds, uniform on Q x {{p >= 10^6}}); D = {DMAX}, "
      f"roots |k'| <= {KR}, seed lines |k| <= {KL}, Taylor lines |c| <= {KT}, h-Taylor orders <= {MHM} ==")
seed_lines = [(k, clo("phi1", k)) for k in range(-KL, KL + 1) if k % 2]
roots = h_zero()
for kp in range(-KR, KR + 1):
    if kp == 0 or kp % 2:
        continue
    unit = h_zero()
    unit[0][-kp] += arb(1)
    unit[1][kp] += arb(1)          # J^{k'} as an object
    Kr, _ = h_transport(unit)
    h_add_scaled(roots, Kr, clo("phi0", kp))
taylor_lines = {m: [(c, clo(TAYLOR_KIND[m], c) / factorial(m)) for c in range(-KT, KT + 1)
                    if (c % 2 == m % 2) and clo(TAYLOR_KIND[m], c) > 0] for m in (2, 3, 4)}


def lin_step(H):
    acc = h_zero()
    for k, v in seed_lines:
        h_add_scaled(acc, H, v, k)
    return h_transport(acc)


Hlin = [roots]
Hnl = [h_zero()]
Htot = [roots]
convs = {1: [roots]}
for m in range(2, MHM + 1):
    convs[m] = []
min_refill = None
for d in range(1, DMAX + 1):
    hl, zr = lin_step(Hlin[d - 1])
    min_refill = zr if min_refill is None else min(min_refill, zr)
    parts = []
    if d >= 2:
        hn0, zr = lin_step(Hnl[d - 1])
        parts.append(hn0)
    for m in range(2, MHM + 1):
        e = d - m
        if e < 0:
            continue
        acc = h_zero()
        for c, v in taylor_lines[m]:
            h_add_scaled(acc, convs[m][e], v, c)
        t, zr = h_transport(acc)
        parts.append(t)
    hn = h_clean(h_sum(parts)) if parts else h_zero()
    Hlin.append(h_clean(hl))
    Hnl.append(hn)
    Htot.append(h_clean(h_sum([hl, hn])))
    convs[1].append(Htot[d])
    for m in range(2, MHM + 1):
        while len(convs[m]) <= d - 1:     # entries e <= d - 1 suffice for depth d + 1
            e = len(convs[m])
            acc = h_zero()
            for d1 in range(0, e + 1):
                if e - d1 < len(convs[m - 1]):
                    h_add_scaled(acc, h_conv(Htot[d1], convs[m - 1][e - d1]), arb(1))
            convs[m].append(h_clean(acc))
    print(f"  depth {d:2d}: linear A >= {float(h_dim(Hlin[d]).lower()):.6f}, nonlinear A >= "
          f"{float(h_dim(Hnl[d]).lower()):.6f}   ({time.time() - T_START:.0f} s)")
print(f"  depth  0: roots A >= {float(h_dim(roots).lower()):.6f}")
lin_tot = h_sum(Hlin)
all_tot = h_sum(Htot)
print(f"  unsigned Picard A-price of the truncation: linear >= {float(h_dim(lin_tot).lower()):.6f}, "
      f"total >= {float(h_dim(all_tot).lower()):.6f}")


# ------------------------------------------------------------------ 2. multiplier measures omega
def omega_from(G):
    om = defaultdict(lambda: arb(0))
    for f in (0, 1):
        for w, v in G[f].items():
            om[w] += v / 4
            om[-w] += v / 4
    return om


def mult_omega(H, orders):
    """symmetrized slot measure of sum_{m in orders} (1/m!) Phi^{(m+1)}(S) H^{(x)m}"""
    om = defaultdict(lambda: arb(0))
    P = None
    for m in range(1, max(orders) + 1):
        P = H if P is None else h_clean(h_conv(P, H))
        if m not in orders:
            continue
        kind = {1: "phi2", 2: "phi3", 3: "phi4"}[m]
        G = h_zero()
        for c in range(-KT, KT + 1):
            if c % 2 != (m + 1) % 2:
                continue
            v = clo(kind, c) / factorial(m)
            if v > 0:
                h_add_scaled(G, P, v, c)
        for x, v in omega_from(G).items():
            om[x] += v
    return om


def om_lo_fr(om, xmax=None, floor=Fr(1, 10 ** 40)):
    """exact Fraction lower bounds (>= 0) of a ball-valued measure, optionally truncated to |x| <= xmax and with
    entries below `floor` dropped (dropping only lowers the measure)."""
    out = {}
    for x, v in om.items():
        if xmax is not None and abs(x) > xmax:
            continue
        lo = v.lower()
        if lo > 0:
            q = C.to_fr_lo(lo)
            if q >= floor:
                out[x] = q
    return out


# ------------------------------------------------------------------ 3. the price pi_phi (same phi as part 1)
MHS = 23
wseed_lo = {}
for m in range(1, MHS + 1, 2):
    wseed_lo[m] = C.to_fr_lo(C.abs_lo(C.coef(C.make_params("point"), "phi1", m)))
omf = {}
for m, v in wseed_lo.items():
    omf[m] = float(v)
    omf[-m] = float(v)
lam_f, phi_f = C.float_perron(omf, BC=BC)
phiq = C.rationalize(phi_f, BC)
TR = C.Trial(phiq, BC)
sha = hashlib.sha256(repr([(x.numerator, x.denominator) for x in phiq]).encode()).hexdigest()
print(f"\n== 3. the price pi_phi: trial vector of part 1 (sha256 of its rationals {sha[:16]}...) ==")
c_lo = min([TR.psi(b) / b for b in range(1, BC + 1)] + [TR.s + TR.phi0])
print(f"  c_lo = {float(c_lo):.6f}; budget on the region <= {float(BUDGET_HI):.7f}")


def N_lo(om_fr, b):
    """exact lower bound of the pi_phi ratio on the symmetrized slot-size-b ray"""
    Om = sum(v * TR.psi(abs(x)) for x, v in om_fr.items())
    num = sum(v * TR.psi(abs(b + x)) for x, v in om_fr.items()) + (b - 1) * Om
    return num / TR.psi(b)


def N_limit_lo(om_fr):
    Om = sum(v * TR.psi(abs(x)) for x, v in om_fr.items())
    return sum(om_fr.values()) + Om / (TR.s + TR.phi0)


variants = []
H_lin5 = h_sum(Hlin[:min(DMAX, 5) + 1])
variants.append(("V1: h-linear term over the LINEAR Picard simples of depth <= 5 (pairwise distinct, Round 185 Prop. 1)",
                 mult_omega(H_lin5, (1,))))
H_d3 = h_sum(Htot[:min(DMAX, 3) + 1])
variants.append(("V2: B_h, orders 1-3, h = Picard truncation to depth 3", mult_omega(H_d3, (1, 2, 3))))
H_d5 = h_sum(Htot[:min(DMAX, 5) + 1])
variants.append(("V3: B_h, orders 1-3, h = Picard truncation to depth 5", mult_omega(H_d5, (1, 2, 3))))
variants.append((f"V4: B_h, orders 1-{MB}, h = Picard truncation to depth {DMAX}", mult_omega(all_tot, tuple(range(1, MB + 1)))))
print(f"\n== 4. per-simple pi_phi one-step norm of B_h: certified lower bounds on the slot-size-b rays ==")
OMS = {}
for name, om in variants:
    fr = om_lo_fr(om)
    OMS[name] = fr
    vals = [N_lo(fr, b) for b in (1, 2, 3, 4)]
    lim = N_limit_lo(fr)
    print(f"  {name}:")
    print(f"     A-mass of the multiplier >= {float(sum(fr.values())):.6f};  N(1) >= {float(vals[0]):.6f}, N(2) >= {float(vals[1]):.6f}, "
          f"N(3) >= {float(vals[2]):.6f}, N(4) >= {float(vals[3]):.6f}; large-slot limit >= {float(lim):.6f}")
    print(f"     N(1) > budget upper end {float(BUDGET_HI):.7f}: {vals[0] > BUDGET_HI}")
check("V2 (depth-3 Picard truncation): the pi_phi norm of B_h exceeds the budget on the slot-size-1 ray, uniformly",
      N_lo(OMS[variants[1][0]], 1) > BUDGET_HI)
print(f"  ({time.time() - T_START:.0f} s)")

# ------------------------------------------------------------------ 5. joint growth rate (all per-simple prices)
print("\n== 5. growth rate of the per-simple path sums of L_S + B_h (lower Collatz-Wielandt certificates) ==")
XCUT = 70
wseed_reg = {m: C.to_fr_lo(C.abs_lo(C.coef(RG, "phi1", m))) for m in range(1, MHS + 1, 2)}


def growth_lower(om_B_fr, label):
    om = defaultdict(Fr)
    for m, v in wseed_reg.items():
        om[m] += v
        om[-m] += v
    for x, v in om_B_fr.items():
        if abs(x) <= XCUT and v >= Fr(1, 10 ** 30):
            om[x] += v
    om = {x: v for x, v in om.items() if v > 0}
    # symmetrize downward (take the minimum of x and -x) so that sum x omega(x) = 0 exactly
    om = {x: min(v, om.get(-x, Fr(0))) for x, v in om.items()}
    om = {x: v for x, v in om.items() if v > 0}
    lamf, phiL = C.float_perron({x: float(v) for x, v in om.items()}, BC=BC, iters=2500)
    pq = C.rationalize(phiL, BC)
    T = C.Trial(pq, BC)
    X0 = max(abs(x) for x in om)
    sp = T.s + T.phi0
    W = sum(om.values())

    def ok(lam):
        for a_ in range(0, BC + X0):
            tot = sum(v * T.psi(abs(a_ + x)) for x, v in om.items())
            if tot < lam * T.phi(a_):
                return False
        slope = W * sp - lam * T.s
        const = W * (T.kap - T.phi0) - lam * T.kap
        return slope >= 0 and slope * (BC + X0) + const >= 0

    lam = Fr(int(lamf * 10 ** 6) - 2, 10 ** 6)
    while not ok(lam):
        lam -= Fr(1, 10 ** 4)
    ratios = [T.psi(b) / b for b in range(1, BC + 1)] + [sp]
    KL_ = max(ratios) / min(ratios)
    print(f"  {label}: [float] Perron root {lamf:.6f}; certified lambda_lo = {float(lam):.6f} "
          f"(phi_L M >= lambda_lo phi_L on every slot size, exact); K_L = {float(KL_):.4f}")
    return lam


GL = {}
for name, _ in variants:
    GL[name] = growth_lower(OMS[name], name.split(":")[0])
print(f"  thresholds: kappa*(b1) <= {float(KSTAR_HI):.7f} (Round 182);  kappa*_A <= {float(KSTAR_A_HI):.8f} (Round 184, A_X)")
v4 = variants[3][0]
check(f"V4: certified growth rate > kappa*(b1) = 0.7741472", GL[v4] > KSTAR_HI)
print(f"  V4 growth rate > kappa*_A = 0.838: {GL[v4] > KSTAR_A_HI}")
print(f"  minimum refill (upper end of the aggregated zero counts, must be >= 0): {float(min_refill):.3e}")
print(f"  total time {time.time() - T_START:.0f} s")
print("\nALL CHECKS OK" if ok_all else "\nSOME CHECK FAILED")
