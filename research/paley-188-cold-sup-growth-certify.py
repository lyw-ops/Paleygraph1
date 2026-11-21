#!/usr/bin/env python3
"""Round 188 cold call `cold-prime-compact-sup-growth`: certified (label (a)) dimension-price growth rate of the
compact seed iterates L_S^k d at the real floor t = a, and its comparison with l_S and Criterion D's allowances.

Own implementation.  python-flint arb balls (outward rounding) for every transcendental constant; exact Fractions
for every inequality that is certified.  numpy floats are used ONLY to propose trial vectors; each proposed vector
is then rationalized and all inequalities are checked in exact rational arithmetic, so the floats certify nothing.

Model (compact, subsequential, Rounds 79/80/179; per-simple rule of Round 80 / Round 182, hypothesis (b4)):
  Phi_a'(sqrt8 cos th) = sum_{m odd} beta_m cos(m th);  L_S chi_M = sum_{m odd} (beta_m/2) [K(J^m M) + K(J^-m M)].
  Summed over the two children J^{+m}, J^{-m}, the pooled |w|-histogram n of a simple evolves by P_m:
     slot size a >= 1 -> sizes |a-m| (dropped if 0) and a+m;  size 0 -> two slots of size m;
     then sum_{b>=1} (b-1) n'_b zeros are added (fill).        (fibre labels drop out; see the explore script)
  With w_m = |beta_m|/2 and P = sum_m w_m P_m, the dimension price of L_S^k chi_M is mass(P^k n_M)/2,
  mass(n) = sum_b b n_b = 2 r.  For a row vector phi >= 0 put psi_b = phi_b + phi_0 (b-1) (b >= 1); then
     (phi P_m)_0 = 2 psi_m,   (phi P_m)_a = [a != m] psi_{|a-m|} + psi_{a+m}   (a >= 1),
  and on valid histograms (n_0 = sum (b-1) n_b) phi(n) = sum_{b>=1} psi_b n_b.

Certified here:
  1. l_S^2 = 1 - sqrt(4a/(4a+8)) (Round 187 Lemma 3(a), recomputed).
  2. beta_m (m <= MH odd) by rigorous arb integration; tail |beta_m|/2 <= M_R R^-m (Cauchy on |z| = R = 4);
     Parseval cross-check sum beta_m^2/2 = l_S^2.
  3. Exact closed form for the J^{+-1} term alone: rate 2 sqrt2 w_1 with an explicit Q(sqrt2) eigenvector
     (checked in arb for b <= 60; the algebraic identity is proved in the report).
  4. Collatz-Wielandt certificates for the full P (all odd harmonics):
       lower: phi P_lo >= lam_lo phi on every slot size (P_lo: m <= MH, lower ends of w_m; dropping harmonics
              only lowers the nonnegative operator);
       upper: phi P_hi + (harmonic tail m > MH = 23) <= lam_up phi on every slot size.
     The infinite range of slot sizes is handled exactly: phi is affine (s b + kappa) beyond B_c, and for
     b >= B_c + MH both sides are affine in b (slope and one value checked).
  5. Constants c_lo <= psi_b / b <= c_hi, giving for every valid simple of dimension r and every k >= 0
        (c_lo/c_hi) lam_lo^k r  <=  A(L_S^k chi_M)  <=  (c_hi/c_lo) lam_up^k r,
     and the ratios theta = lam / l_S against 1/q_rho (Criterion D) and 1/q_ang(2.338) >= 2.1610 (angular variant).
Replay: .venv/bin/python -B research/paley-188-cold-sup-growth-certify.py   (about 1 min)
"""
from fractions import Fraction as Fr

import numpy as np
from flint import acb, arb, ctx

ctx.prec = 212
a = arb(2031) / 128
four_a = 4 * a
s8 = arb(8).sqrt()
PI = arb.pi()
MH = 23          # harmonics m <= MH computed by integration
BC = 300         # phi tabulated for b < BC, affine beyond
NUM_B = 1500     # size of the floating trial-vector problem


def flo(x):
    m, e = x.lower().man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))


def fhi(x):
    m, e = x.upper().man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))


def fmt(x, d=10):
    return f'[{float(x.lower()):.{d}f}, {float(x.upper()):.{d}f}]'


ok_all = True


def check(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(f'  [{"OK" if cond else "FAIL"}] {name}')


print('== 1. seed counting rate l_S at t = a ==')
lS2 = 1 - (four_a / (four_a + 8)).sqrt()
lS = lS2.sqrt()
print(f'  l_S^2 in {fmt(lS2, 12)};  l_S in {fmt(lS, 12)}')

print('\n== 2. Fourier coefficients beta_m of Phi_a\'(sqrt8 cos th) (rigorous arb integration) ==')
beta = {}
for m in range(1, MH + 1, 2):
    def integrand(z, an, m=m):
        c = z.cos()
        return s8 * c * (m * z).cos() / (four_a + 8 * c * c).sqrt(analytic=an)
    I = acb.integral(integrand, 0, PI, rel_tol=arb(2) ** -150)
    check(f'beta_{m}: imaginary part of the integral contains 0', I.imag.contains(0))
    beta[m] = 2 * I.real / PI
    print(f'  beta_{m:<2d} in [{beta[m].str(14, radius=False)} +/- {float(beta[m].rad()):.1e}]')
R = arb(4)
cR = (R + 1 / R) / 2
MR = s8 * cR / (four_a - 8 * cR * cR).sqrt()
check('annulus 1/4 <= |z| <= 4 avoids the branch locus: 8 c_R^2 < 4a', (8 * cR * cR < four_a))
print(f'  Cauchy tail: |beta_m|/2 <= M_R 4^-m with M_R = {fmt(MR, 6)} (R = 4)')
for m in range(1, MH + 1, 2):
    check(f'|beta_{m}|/2 <= M_R 4^-{m} (consistency)', abs(beta[m]) / 2 <= MR * R ** (-m))
MRq = fhi(MR)
x = Fr(1, 4)
m0 = MH + 2
T0 = MRq * x ** m0 / (1 - x * x)
T1 = MRq * x ** m0 * (Fr(m0) / (1 - x * x) + 2 * x * x / (1 - x * x) ** 2)
print(f'  harmonic tail (m >= {m0}): sum w_m <= {float(T0):.3e}, sum m w_m <= {float(T1):.3e}')
pars = sum((beta[m] ** 2 / 2 for m in beta), arb(0))
tail2 = 2 * MR * MR * arb(16) ** (-m0) / (1 - arb(1) / 256)
check('Parseval: sum_{m<=MH} beta_m^2/2 <= l_S^2 <= that + tail bound',
      pars.lower() <= lS2.upper() and lS2.lower() <= (pars + tail2).upper())
print(f'  sum_(m<=MH) beta_m^2/2 in {fmt(pars, 14)}, l_S^2 in {fmt(lS2, 14)}')
w_lo = {m: max(Fr(0), flo(abs(beta[m]) / 2)) for m in beta}
w_hi = {m: fhi(abs(beta[m]) / 2) for m in beta}

print('\n== 3. the J^{+-1} term alone: exact Perron data in Q(sqrt 2) ==')
r2 = arb(2).sqrt()
mu = r2 - 1
lam1 = 2 * r2          # growth of the path-summed dimension per unit coefficient
phi1 = [r2 - 1] + [arb(b - 1) + (2 - r2) * mu ** (b - 1) for b in range(1, 80)]
psi1 = [None] + [phi1[b] + phi1[0] * (b - 1) for b in range(1, 80)]
res = []
res.append((2 * psi1[1] - lam1 * phi1[0]))
res.append((psi1[2] - lam1 * phi1[1]))                       # a = 1: |1-1| = 0 dropped
for b in range(2, 60):
    res.append((psi1[b - 1] + psi1[b + 1] - lam1 * phi1[b]))
check('left eigen-equations phi P_1 = 2 sqrt2 phi hold (b <= 59, arb balls contain 0)',
      all(r.contains(0) for r in res))
rat = [psi1[b] / b for b in range(1, 80)]
print(f'  psi_b/b ranges from {fmt(rat[0], 6)} (b = 1) up to the limit sqrt2; c_hi/c_lo = sqrt2/(2 - sqrt2) = 1 + sqrt2')
rate1 = lam1 * beta[1] / 2
rate_lin = lam1 * (arb(2) / a).sqrt() / 2
print(f'  rate with the exact J^{{+-1}} coefficient beta_1/2: 2 sqrt2 * beta_1/2 = sqrt2 beta_1 in {fmt(rate1, 10)};'
      f' / l_S in {fmt(rate1 / lS, 6)}')
print(f'  rate with the seed-linear coefficient s/(4 sqrt a) (Round 182): {fmt(rate_lin, 10)} (Round 182 conjectured 0.50206)')

print('\n== 4. Collatz-Wielandt certificates for the full dimension-price operator ==')
# floating trial vector (proposal only)
wf = {m: float(beta[m]) / 2 for m in beta}
wf = {m: abs(v) for m, v in wf.items()}
phi = np.ones(NUM_B)
phi[1:] = np.arange(1, NUM_B)


def apply_float(ph):
    s = ph[-1] - ph[-2]
    ext = np.concatenate([ph, ph[-1] + s * np.arange(1, 40)])
    psi = ext + ext[0] * (np.arange(len(ext)) - 1)
    out = np.zeros(NUM_B)
    for m, wm in wf.items():
        out[0] += wm * 2 * psi[m]
        idx = np.arange(1, NUM_B)
        lo = np.abs(idx - m)
        term = np.where(lo != 0, psi[lo], 0.0) + psi[idx + m]
        out[1:] += wm * term
    return out


lam_f = 0
for it in range(4000):
    nw = apply_float(phi)
    lam_f = nw[BC] / phi[BC]
    phi = nw / nw[BC] * BC
lam_f = float(np.median(apply_float(phi)[1:BC] / phi[1:BC]))
print(f'  [float proposal] Perron root of sum_m |beta_m|/2 P_m: {lam_f:.12f}')
DEN = 2 ** 64
phiq = [Fr(round(float(v) * DEN), DEN) for v in phi[:BC + 1]]
s_q = phiq[BC] - phiq[BC - 1]
kap = phiq[BC] - s_q * BC
phiq = phiq[:BC]


def PHI(b):
    return phiq[b] if b < BC else s_q * b + kap


def PSI(b):
    return PHI(b) + phiq[0] * (b - 1)


def apply_exact(w, a_):
    if a_ == 0:
        return sum(wm * 2 * PSI(m) for m, wm in w.items())
    return sum(wm * ((PSI(abs(a_ - m)) if a_ != m else 0) + PSI(a_ + m)) for m, wm in w.items())


check('trial vector phi > 0 on tabulated sizes and slope s > 0', all(v > 0 for v in phiq) and s_q > 0 and kap + s_q * BC > 0)
lam_lo = Fr(round((lam_f - 2e-9) * 10 ** 12), 10 ** 12)
lam_up = Fr(round((lam_f + 2e-9) * 10 ** 12), 10 ** 12)
# lower certificate
low_ok = all(apply_exact(w_lo, a_) >= lam_lo * PHI(a_) for a_ in range(0, BC + MH))
W_lo = sum(w_lo.values())
slope_lo = 2 * W_lo * (s_q + phiq[0]) - lam_lo * s_q
const_lo = 2 * W_lo * (kap - phiq[0]) - lam_lo * kap
a0 = BC + MH
low_tail = slope_lo >= 0 and slope_lo * a0 + const_lo >= 0
check(f'lower: phi P_lo >= lam_lo phi for sizes 0..{BC + MH - 1} (exact)', low_ok)
check(f'lower: affine range b >= {a0}: slope {float(slope_lo):.3e} >= 0 and value at {a0} >= 0', low_tail)
# upper certificate with the harmonic tail
kap_max = max(max(phiq[b] - s_q * b for b in range(BC)), kap)
sp = s_q + phiq[0]


def tail_bound(a_):
    return 2 * sp * (a_ * T0 + T1) + 2 * kap_max * T0


up_ok = all(apply_exact(w_hi, a_) + tail_bound(a_) <= lam_up * PHI(a_) for a_ in range(0, BC + MH))
W_hi = sum(w_hi.values())
slope_up = 2 * W_hi * sp + 2 * sp * T0 - lam_up * s_q
const_up = 2 * W_hi * (kap - phiq[0]) + 2 * sp * T1 + 2 * kap_max * T0 - lam_up * kap
up_tail = slope_up <= 0 and slope_up * a0 + const_up <= 0
check(f'upper: phi P_hi + tail <= lam_up phi for sizes 0..{BC + MH - 1} (exact)', up_ok)
check(f'upper: affine range b >= {a0}: slope {float(slope_up):.3e} <= 0 and value at {a0} <= 0', up_tail)
print(f'  certified dimension-price rate lambda_A in [{float(lam_lo):.10f}, {float(lam_up):.10f}]')
print(f'    (exact rationals lam_lo = {lam_lo}, lam_up = {lam_up})')

print('\n== 5. constants and comparisons ==')
ratios = [PSI(b) / b for b in range(1, BC + 1)] + [sp]
c_lo, c_hi = min(ratios), max(ratios)
check('psi_b/b = (s + phi_0) + (kappa - phi_0)/b beyond B_c (monotone, so its range lies between the value at B_c and s + phi_0)', all(PSI(b) / b == sp + (kap - phiq[0]) / b for b in range(BC, BC + 50)))
print(f'  c_lo = {float(c_lo):.6f}, c_hi = {float(c_hi):.6f}; K = c_hi/c_lo = {float(c_hi / c_lo):.6f}')
print(f'  => (1/K) lam_lo^k r <= A(L_S^k chi_M) <= K lam_up^k r for every valid simple M of dimension r, all k >= 0')
L_lo, L_up = arb(lam_lo.numerator) / lam_lo.denominator, arb(lam_up.numerator) / lam_up.denominator
th_lo, th_up = L_lo / lS, L_up / lS
print(f'  theta_A = lambda_A / l_S in [{float(th_lo.lower()):.8f}, {float(th_up.upper()):.8f}]')
for qv in ('0.5145', '0.5174', '0.518', '0.5193', '0.535', '0.5441', '0.545'):
    inv = 1 / arb(qv)
    check(f'theta_A > 1/q = {float(inv.upper()):.5f} (q = {qv}); rate threshold q^-1 l_S = {float((inv * lS).upper()):.6f}',
          th_lo.lower() > inv.upper())
check('theta_A < 2.1610 <= 1/q_ang(2.338) (angular variant allowance, Round 187 Lemma 3(c))', th_up.upper() < arb('2.1610'))
print(f'  margins: theta_A / 1.94363 - 1 >= {float((th_lo / (1 / arb("0.5145"))).lower() - 1):.4f};'
      f' 2.1610 / theta_A - 1 >= {float((arb("2.1610") / th_up).lower() - 1):.4f}')
r1 = (lam1 * beta[1] / 2) / lS
print(f'  J^(+-1) term alone: theta in {fmt(r1, 8)} (> 1.94363: {bool(r1.lower() > (1 / arb("0.5145")).upper())})')
print('  required full L^2 rate for the conditional transfer to R^comp: l_* < lam_lo * q_rho;'
      f' at q = 0.5145: l_* < {float(lam_lo * Fr(5145, 10000)):.6f}')

print('\n== 5b. by-product for the price programme (Round 182 Proposition 1 / Corollary 2.2, under its (b1)) ==')
print('  Perron-weighted price pi_phi(chi_M) = phi(n_M)/(2 c_lo) >= dim M (sup-dominating); one-step norm of L_S <= lam_up, C_S = 1.')
kstar_lo = Fr(7741471, 10 ** 7)
print(f'  non-seed budget beta_max = kappa* - lam_up >= {float(kstar_lo - lam_up):.6f}'
      f'  (Round 182: 0.24159 from pi_1 with the seed-linear part only)')
lin_rate = 2 * arb(2).sqrt() * (arb(2) / a).sqrt() / 2
print(f'  same price for the seed-linear operator alone at t = a: one-step rate 2 sqrt2 * sqrt(2/a)/2 in {fmt(lin_rate, 6)}'
      f' (Round 182 pi_1: 0.53255 at |sqrt t| >= sqrt(N)/2)')

print('\n== 6. L^2 side of the conditional transfer to the full increments (real floor) ==')
print('  Under decoupling (D) E(|f|^2 | U_602) = ||f||^2 and Round 80 (4) E(U^2 | J) = S^2 + eta, eta = ||U_602 - S||_2^2,')
print('  Jensen for the concave y -> y/(4a+y) gives  ||Phi_a\'(U_602)||_2^2 <= 1 - 4a/sqrt((4a+eta)(4a+eta+8)) =: l_*(eta)^2.')
print('  The transfer needs l_* < lam_lo * q, i.e. eta < eta_max(q) = sqrt(16 + (4a/(1-T))^2) - 4 - 4a, T = (lam_lo q)^2:')
for qv in ('0.5145', '0.5174', '0.518', '0.535', '0.545'):
    T = (L_lo * arb(qv)) ** 2
    Kq = four_a / (1 - T)
    eta_max = (16 + Kq * Kq).sqrt() - 4 - four_a
    print(f'    q = {qv}: eta_max in {fmt(eta_max, 5)}, i.e. ||U_602 - S||_2 < {float(eta_max.sqrt().lower()):.4f}')
for eta in ('0', '0.0306', '0.25', '3.853'):
    e_ = arb(eta)
    ls = (1 - four_a / ((four_a + e_) * (four_a + e_ + 8)).sqrt()).sqrt()
    print(f'    eta = {eta}: l_*(eta) in {fmt(ls, 6)}')
print('    (eta = 0.0306 is the [float input] RMS(h)^2 = 0.175^2 of Round 182; eta = 3.853 is the proved sup cap 1.963^2)')

print('\nALL CHECKS OK' if ok_all else '\nSOME CHECK FAILED')
