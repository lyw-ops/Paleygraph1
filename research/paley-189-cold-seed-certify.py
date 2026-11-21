#!/usr/bin/env python3
"""Round 189 cold call `cold-prime-perron-nonseed-price`, part 1 (label (a): exact rationals and outward
arb/acb balls): the seed dimension-price certificate of Round 188 extended from the real floor t = a to the
closed complex square Q (and to s^2 in [8, 8 + 8/(10^6-1)], i.e. every eligible p >= 10^6), both lifts.

Pooled seed operator (Round 188 Lemma 1, accepted under (R80)): with w_m = |coefficient of J^m in Phi_t'(S)|
(= |beta_m|/2 at t = a), P(t) = sum_{m odd} w_m(t) P_m, row form (phi P_m)_0 = 2 psi_m,
(phi P_m)_a = [a != m] psi_{|a-m|} + psi_{a+m}.  The second lift is the fibre exchange (Round 184 lift remark,
Round 185 Lemma 0): P_m is fibre-free, so P is the same operator for both lifts (report Lemma 0').
One rational trial vector phi (proposed in floating point at t = a, then checked exactly) is used at every
point of the region, so the price pi_phi(chi_M) = phi(n_M)/(2 c_lo) does not depend on t.
Replay: .venv/bin/python -B research/paley-189-cold-seed-certify.py     (about 1 min)
"""
import importlib.util
import os
from fractions import Fraction as Fr

from flint import arb

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("c189", os.path.join(_here, "paley-189-cold-common.py"))
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

ok_all = True


def check(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(f"  [{'OK' if cond else 'FAIL'}] {name}")


MH = 23
BC = 300
KSTAR_LO, KSTAR_HI = Fr(7741471, 10 ** 7), Fr(7741472, 10 ** 7)   # Round 182 exact bracket of kappa*

PT = C.make_params("point")
QC = C.make_params("qcompact")
RG = C.make_params("region")
print("== 1. seed coefficients w_m = |[J^m] Phi_t'(S)| (outward balls) ==")
w = {}
for name, P in (("point", PT), ("qcompact", QC), ("region", RG)):
    w[name] = {}
    for m in range(1, MH + 1, 2):
        z = C.coef(P, "phi1", m)
        w[name][m] = (C.to_fr_lo(C.abs_lo(z)), C.to_fr_hi(C.abs_hi(z)))
    print(f"  {name}: w_1 in [{float(w[name][1][0]):.12f}, {float(w[name][1][1]):.12f}], "
          f"w_3 in [{float(w[name][3][0]):.6e}, {float(w[name][3][1]):.6e}], "
          f"w_5 in [{float(w[name][5][0]):.6e}, {float(w[name][5][1]):.6e}]")
check("point value w_1 agrees with Round 188 beta_1/2 = 0.33946008419161/2 (to 1e-12)",
      abs(float(w["point"][1][0]) - 0.33946008419161 / 2) < 1e-12)
lS2 = 1 - (4 * C.A_T / (4 * C.A_T + 8)).sqrt()
pars = sum((2 * C.afr(w["point"][m][0]) ** 2 for m in w["point"]), arb(0))
T0p, T1p = C.seed_tail(PT, MH + 2)
check("Parseval at the point: sum 2 w_m^2 <= l_S^2 <= that + 2 (tail)^2",
      pars.upper() <= lS2.upper() and lS2.lower() <= (pars + 2 * T0p ** 2 + arb(2) ** -150).upper())
TAIL = {}
for name, P in (("point", PT), ("qcompact", QC), ("region", RG)):
    T0, T1 = C.seed_tail(P, MH + 2)
    TAIL[name] = (C.to_fr_hi(arb(T0)), C.to_fr_hi(arb(T1)))
    print(f"  {name}: harmonic tail m >= {MH + 2}: sum w_m <= {float(TAIL[name][0]):.3e}, sum m w_m <= {float(TAIL[name][1]):.3e}")

print("\n== 2. trial vector (floating proposal at t = a, rationalized, then checked exactly) ==")
omf = {}
for m, (lo, hi) in w["point"].items():
    omf[m] = float(lo)
    omf[-m] = float(lo)
lam_f, phi_f = C.float_perron(omf, BC=BC)
print(f"  [float proposal] Perron root at t = a: {lam_f:.12f}")
phiq = C.rationalize(phi_f, BC)
TR = C.Trial(phiq, BC)
import hashlib
print("  sha256 of the rational trial vector:",
      hashlib.sha256(repr([(x.numerator, x.denominator) for x in phiq]).encode()).hexdigest()[:16] + "...")
check("phi > 0 on tabulated sizes, slope s > 0, affine part positive",
      all(v > 0 for v in TR.tab) and TR.s > 0 and TR.kap + TR.s * BC > 0)
sp = TR.s + TR.phi0
kap_max = max(max(TR.psi(c) - sp * c for c in range(0, BC + 1)), TR.kap - TR.phi0)


def row(wd, a_):
    tot = Fr(0)
    for m, wm in wd.items():
        if a_ == 0:
            tot += wm * 2 * TR.psi(m)
        else:
            tot += wm * ((TR.psi(abs(a_ - m)) if a_ != m else 0) + TR.psi(a_ + m))
    return tot


def upper_cert(wd, tail, lam):
    T0, T1 = tail
    a0 = BC + MH
    for a_ in range(0, a0):
        if row(wd, a_) + 2 * sp * (a_ * T0 + T1) + 2 * kap_max * T0 > lam * TR.phi(a_):
            return False, a_
    W = sum(wd.values())
    slope = 2 * W * sp + 2 * sp * T0 - lam * TR.s
    const = 2 * W * (TR.kap - TR.phi0) + 2 * sp * T1 + 2 * kap_max * T0 - lam * TR.kap
    return (slope <= 0 and slope * a0 + const <= 0), "affine"


def lower_cert(wd, lam):
    a0 = BC + MH
    for a_ in range(0, a0):
        if row(wd, a_) < lam * TR.phi(a_):
            return False, a_
    W = sum(wd.values())
    slope = 2 * W * sp - lam * TR.s
    const = 2 * W * (TR.kap - TR.phi0) - lam * TR.kap
    return (slope >= 0 and slope * a0 + const >= 0), "affine"


def search(fn, start, step, up, n=60):
    """smallest (up) / largest (down) value on the grid start +- step * j that passes; doubling then bisection"""
    def val(j):
        return start + step * j if up else start - step * j
    if fn(val(0))[0]:
        return val(0)
    hi = 1
    while not fn(val(hi))[0]:
        hi *= 2
        if hi > 2 ** n:
            return None
    lo = hi // 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if fn(val(mid))[0]:
            hi = mid
        else:
            lo = mid
    return val(hi)


print("\n== 3. Collatz-Wielandt certificates ==")
res = {}
for name in ("point", "qcompact", "region"):
    whi = {m: v[1] for m, v in w[name].items()}
    wlo = {m: v[0] for m, v in w[name].items()}
    start = Fr(round(lam_f * 10 ** 10), 10 ** 10)
    lam_up = search(lambda L: upper_cert(whi, TAIL[name], L), start, Fr(1, 10 ** 10), True)
    lam_lo = search(lambda L: lower_cert(wlo, L), start, Fr(1, 10 ** 10), False)
    res[name] = (lam_lo, lam_up)
    check(f"{name}: phi P_lo >= lam_lo phi on every slot size (exact; affine range included)", lam_lo is not None)
    check(f"{name}: phi P_hi + harmonic tail <= lam_up phi on every slot size (exact; affine range included)",
          lam_up is not None)
    print(f"  {name}: certified dimension-price rate in [{float(lam_lo):.10f}, {float(lam_up):.10f}]  "
          f"(lam_lo = {lam_lo}, lam_up = {lam_up})")
check("point bracket lies inside Round 188's [0.4995143223, 0.4995143263] (consistency)",
      res["point"][0] >= Fr(4995143223, 10 ** 10) - Fr(1, 10 ** 10) and res["point"][1] <= Fr(4995143263, 10 ** 10) + Fr(2, 10 ** 10))

print("\n== 4. constants of pi_phi and the non-seed budget ==")
ratios = [TR.psi(b) / b for b in range(1, BC + 1)] + [sp]
c_lo, c_hi = min(ratios), max(ratios)
check("psi_b/b = (s + phi_0) + (kappa - phi_0)/b beyond BC (monotone), so [c_lo, c_hi] covers all b",
      all(TR.psi(b) / b == sp + (TR.kap - TR.phi0) / b for b in range(BC, BC + 40)))
print(f"  c_lo = {float(c_lo):.6f} (b = {ratios.index(c_lo) + 1}), c_hi = {float(c_hi):.6f}; K = {float(c_hi / c_lo):.6f}")
print("  pi_phi(chi_M) := phi(n_M)/(2 c_lo) >= dim M (sup-dominating); ||L_S||_{pi_phi} <= lam_up (C_S = 1) at every t in Q, both lifts")
for name in ("point", "qcompact", "region"):
    lo, up = res[name]
    print(f"  {name}: non-seed budget kappa* - ||L_S|| in [{float(KSTAR_LO - up):.7f}, {float(KSTAR_HI - lo):.7f}]")
bud_region = KSTAR_LO - res["region"][1]
check("uniform budget on Q x {p >= 10^6} (both lifts) is >= 0.2746323", bud_region >= Fr(2746323, 10 ** 7))
check("uniform budget on Q in the compact model s^2 = 8 (both lifts) is >= 0.2746325",
      KSTAR_LO - res["qcompact"][1] >= Fr(2746325, 10 ** 7))
check("the uniform seed rate stays below kappa*_A = 0.8379025 (Round 184) and 1/2", res["region"][1] < Fr(1, 2))
KA_LO = Fr(83790250, 10 ** 8)            # Round 184: kappa*_A in [0.83790250, 0.83793100] (A_X, from D1-D4)
Kup = c_hi / c_lo
kphi = 1 - Kup * (1 - KA_LO)
print(f"  (b1) replaced by the A_X inputs with loss K: p0_phi <= K p0, c_phi <= K c_A, so kappa*_phi >= 1 - K (1 - kappa*_A)"
      f" >= {float(kphi):.6f};  budget >= {float(kphi - res['region'][1]):.6f} (uniform on the region)")
check("without (b1) (A_X constants times K) the pi_phi budget is still positive", kphi - res["region"][1] > 0)
print("  psi_b for b = 0..6 (exact rationals, as floats):", " ".join(f"{float(TR.psi(b)):.6f}" for b in range(7)))
print("\nALL CHECKS OK" if ok_all else "\nSOME CHECK FAILED")
