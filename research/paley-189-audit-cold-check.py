#!/usr/bin/env python3
"""Round 189 audit (session/r189-audit): independent checks of the cold report
`native-claude-cold-prime-perron-nonseed-price-189.md`.  Own implementation; imports no report script.

Part A (floating, periodic trapezoid rule with 4096 nodes in complex double precision): seed coefficients |[J^m] Phi_t'(S)| at the centre, the four corners
        of Q and both ends of the s^2 range, compared with the report's printed region balls (m = 1, 3, 5).
Part B (floating, a different method): the seed dimension growth rate by FORWARD iteration of pooled histograms
        (column form, refills Sum(|c|-1)), at the centre and at the corners, against the certified brackets.
Part C (exact): Theorem 1 by brute force (random configurations, random Gamma-invariant and non-invariant multiplier
        families, arbitrary positive phi); Theorem 1(iii) in the dimension price; Proposition 3's pooled evolution
        over a Gamma-orbit, two steps, by brute-force per-object transport.
Part D (exact Fractions): budget arithmetic, Remark 0.2, the per-unit root value 3.950, the class-robust corollary
        ||B_h|| >= lambda_L - ||L_S|| > budget, and the signed-source Duhamel form of Round 182 Proposition 2.
Replay: .venv/bin/python -B research/paley-189-audit-cold-check.py      (about 1 minute)
"""
import random
import sys
from collections import Counter, defaultdict
from fractions import Fraction as Fr

import numpy as np

OK = True


def check(name, cond):
    global OK
    OK &= bool(cond)
    print(f"  [{'OK' if cond else 'FAIL'}] {name}")


A_T = 2031 / 128
H17 = 2.0 ** -17
TH = 2 * np.pi * np.arange(4096) / 4096


def seed_coef(t, s2, m):
    """[e^{im th}] (s/(2 sqrt t)) cos th (1 + beta cos^2 th)^(-1/2), beta = s^2/(4t), principal branches
    (Re(1 + beta cos^2) > 0 on Q).  Trapezoid rule on the circle: exponentially accurate for this analytic integrand."""
    s = np.sqrt(s2)
    beta = s2 / (4 * t)
    f = np.cos(TH) * (1 + beta * np.cos(TH) ** 2 + 0j) ** (-0.5) * np.exp(-1j * m * TH)
    return s / (2 * np.sqrt(complex(t))) * f.mean()


print("Part A: seed coefficients by quadrature against the report's region balls")
balls = {1: (0.169729987392, 0.169730174588), 3: (2.499215e-03, 2.499225e-03), 5: (5.547411e-05, 5.547451e-05)}
pts = [(A_T, 8.0)]
for dx in (-1, 1):
    for dy in (-1, 1):
        for s2 in (8.0, 8.0 + 8.0 / 999999):
            pts.append((complex(A_T + dx * H17, dy * H17), s2))
okA = True
for m, (lo, hi) in balls.items():
    vals = [abs(seed_coef(t, s2, m)) for t, s2 in pts]
    inside = all(lo <= float(v) <= hi for v in vals)
    okA &= inside
    print(f"   m={m}: centre {vals[0]:.13g}; corners in [{min(vals):.13g}, {max(vals):.13g}]; "
          f"inside the report's ball: {inside}")
check("w_1, w_3, w_5 at the centre and the 8 corner/endpoint combinations lie inside the printed region balls", okA)
c0 = seed_coef(A_T, 8.0, 1)
check("w_1 at t = a, s^2 = 8 equals Round 188's beta_1/2 = 0.33946008419161/2 to 1e-12",
      abs(c0 - 0.33946008419161 / 2) < 1e-12)

print("Part B: forward pooled-histogram growth of the seed (different method from the report's row certificate)")


def forward_rate(w, NB=3000, steps=400):
    """w: dict m -> w_m (m > 0 odd).  Histogram n[c], c = 0..NB-1 (c = pooled |slot|).  One step: every slot of size a
    (zeros included) sends weight w_m to sizes |a - m| and a + m (size 0 dropped); then zeros = Sum (c - 1) n_c.
    Returns the asymptotic dimension growth ratio."""
    n = np.zeros(NB)
    n[2] = 1.0
    n[0] = 1.0
    ms = sorted(w)
    dims = []
    for _ in range(steps):
        out = np.zeros(NB)
        a = np.arange(NB)
        for mm in ms:
            wm = float(w[mm])
            # a + m
            out[mm:] += wm * n[:NB - mm]
            # |a - m|
            idx = np.abs(a - mm)
            np.add.at(out, idx, wm * n)
        out[0] = 0.0
        c = np.arange(NB)
        out[0] = np.sum((c[1:] - 1) * out[1:])
        dim = np.sum(c[1:] * out[1:])
        dims.append(dim)
        n = out / dim
    return dims[-1], n


def wvec(t, s2, M=23):
    return {m: abs(seed_coef(t, s2, m)) for m in range(1, M + 1, 2)}


rate_c, nlaw = forward_rate(wvec(A_T, 8.0))
print(f"   centre: forward growth rate {rate_c:.10f}; pooled slot law n_0..n_3 (normalized by dimension) "
      f"{nlaw[0]:.4f} {nlaw[1]:.4f} {nlaw[2]:.4f} {nlaw[3]:.4f}")
check("centre rate inside the report's point bracket [0.4995143243, 0.4995143256] (to 2e-10)",
      0.4995143243 - 2e-10 <= rate_c <= 0.4995143256 + 2e-10)
rates = []
for t, s2 in pts[1:]:
    r, _ = forward_rate(wvec(t, s2), steps=300)
    rates.append(r)
print(f"   corners: forward rates in [{min(rates):.10f}, {max(rates):.10f}]")
check("corner rates inside the report's region bracket [0.4995141305, 0.4995147825]",
      all(0.4995141305 <= r <= 0.4995147825 for r in rates))

print("Part C: Theorem 1 and the pooled evolution of Proposition 3 (exact, brute force)")
rng = random.Random(189)
phi0 = Fr(2, 5)
phi = lambda b: Fr(3, 10) + Fr(b) ** 1 * Fr(7, 9) + (Fr(1, 3) if b % 2 else 0) if b else phi0
psi = lambda c: Fr(0) if c == 0 else phi(c) + phi0 * (c - 1)


def rand_config():
    A = [rng.choice([-4, -3, -2, -1, 1, 2, 3, 4]) for _ in range(rng.randint(1, 4))]
    B = [rng.choice([-4, -3, -2, -1, 1, 2, 3, 4]) for _ in range(rng.randint(1, 4))]
    z = sum(abs(v) - 1 for v in A + B)
    zA = rng.randint(0, z)
    return (A + [0] * zA, B + [0] * (z - zA))


def gam(g, G):
    A, B = G
    if g in ("s", "sn"):
        A, B = B, A
    if g in ("n", "sn"):
        A, B = [-x for x in A], [-x for x in B]
    return (A, B)


def R_of(family, F):
    tot = Fr(0)
    for c, G in family:
        for f in (0, 1):
            for x in G[f]:
                for v in F[f]:
                    tot += c * psi(abs(x + v))
    return tot


def phiF(F):
    return sum(psi(abs(v)) for v in F[0] + F[1])


def omega_of(family):
    om = defaultdict(Fr)
    for c, G in family:
        for x in G[0] + G[1]:
            om[x] += c / 4
            om[-x] += c / 4
    return om


def Nb(om, b):
    Om = sum(v * psi(abs(x)) for x, v in om.items())
    return (sum(v * psi(abs(b + x)) for x, v in om.items()) + (b - 1) * Om) / psi(b)


okC = True
for trial in range(60):
    base = []
    for _ in range(rng.randint(1, 3)):
        G = ([rng.randint(-3, 3) for _ in range(rng.randint(1, 3))], [rng.randint(-3, 3) for _ in range(rng.randint(1, 3))])
        base.append((Fr(rng.randint(1, 5), rng.randint(1, 5)), G))
    inv = [(c, gam(g, G)) for c, G in base for g in ("e", "s", "n", "sn")]
    om = omega_of(inv)
    F = rand_config()
    pooled = Counter(abs(v) for v in F[0] + F[1] if v)
    med = sum(pooled[b] * psi(b) * Nb(om, b) for b in pooled) / sum(pooled[b] * psi(b) for b in pooled)
    okC &= (R_of(inv, F) / phiF(F) == med)
    # non-invariant family: max over the orbit of F dominates the mediant (Theorem 1(ii))
    om_b = omega_of(base)
    med_b = sum(pooled[b] * psi(b) * Nb(om_b, b) for b in pooled) / sum(pooled[b] * psi(b) for b in pooled)
    okC &= max(R_of(base, gam(g, F)) / phiF(gam(g, F)) for g in ("e", "s", "n", "sn")) >= med_b
    # Theorem 1(iii): with psi_b = b, sup_b N(b) = |omega| + sum omega |x|
    Wd = sum(om.values())
    W1 = sum(v * abs(x) for x, v in om.items())
    NbA = lambda b: (sum(v * abs(b + x) for x, v in om.items()) + (b - 1) * W1) / b
    okC &= all(NbA(b) <= Wd + W1 for b in range(1, 30)) and NbA(10 ** 6) == Wd + W1 - W1 / 10 ** 6
check("Theorem 1(i) mediant identity (60 random invariant families), (ii) orbit-max >= mediant, (iii) dimension-price sup",
      okC)


def transport(W):
    """Round 80 rule as used in Rounds 184-189: fibre A keeps w<0, sends w>0 to B; fibre B keeps w<0, sends w>0 to A;
    zeros dropped; refills z_f = (1/2) Sum |w| - #(nonzero slots in f)."""
    A, B = W
    nA = [w for w in A if w < 0] + [w for w in B if w > 0]
    nB = [w for w in B if w < 0] + [w for w in A if w > 0]
    r = Fr(sum(abs(w) for w in A + B), 2)
    zA, zB = r - len(nA), r - len(nB)
    return nA + [0] * int(max(zA, 0)), nB + [0] * int(max(zB, 0)), (zA, zB)


def tensor(G, F):
    return ([x + v for x in G[0] for v in F[0]], [x + v for x in G[1] for v in F[1]])


def pooled_hist(objs):
    h = Counter()
    for c, F in objs:
        for v in F[0] + F[1]:
            h[abs(v)] += c
    return h


def Qstep(h, om):
    out = Counter()
    for a, na in h.items():
        for x, w in om.items():
            cc = abs(a + x)
            if cc:
                out[cc] += na * w
    out[0] = sum((cc - 1) * v for cc, v in out.items() if cc)
    return out


okP = True
nonneg = True
root = transport(([-2], [2]))[:2]                      # K(J^2): ([-2, 2], [0, 0])
for trial in range(12):
    # Gamma-closed multiplier family of the shapes used in L_S + B_h: seed lines J^c (c odd) and
    # h-linear-type objects J^c (x) K(J^{+-2}) (c even), each with all four Gamma images
    base = [(Fr(rng.randint(1, 5), 4), ([-1], [1])), (Fr(rng.randint(1, 5), 40), ([-3], [3]))]
    for c in rng.sample([0, 2, -2], 2):
        base.append((Fr(rng.randint(1, 5), 12), ([x - c for x in root[0]], [x + c for x in root[1]])))
    inv = [(c, gam(g, G)) for c, G in base for g in ("e", "s", "n", "sn")]
    om = omega_of(inv)
    M0 = transport(tensor(([-1], [1]), root))[:2]       # a depth-1 transported object
    orbit = [(Fr(1), gam(g, M0)) for g in ("e", "s", "n", "sn")]
    h = pooled_hist(orbit)
    cur = orbit
    for step in range(2):
        nxt = []
        for c, F in cur:
            for cG, G in inv:
                A_, B_, z = transport(tensor(G, F))
                nonneg &= z[0] >= 0 and z[1] >= 0 and z[0].denominator == 1 and z[1].denominator == 1
                nxt.append((c * cG, (A_, B_)))
        h = Qstep(h, om)
        ph = pooled_hist(nxt)
        okP &= all(ph[k] == h[k] for k in set(h) | set(ph))
        cur = nxt
check("Proposition 3: pooled histograms of the path sums over a Gamma-orbit evolve exactly by Q_omega (2 steps, 12 cases)",
      okP)
check("   every brute-force transport had nonnegative integer refills (the test objects are valid under the rule)", nonneg)

print("Part D: arithmetic (exact Fractions)")
KS_LO, KS_HI = Fr(7741471, 10 ** 7), Fr(7741472, 10 ** 7)
LUP, LLO = Fr(199805913, 400000000), Fr(999028261, 2000000000)
LUP_Q = Fr(2497572429, 5000000000)
check("uniform budget kappa*_lo - lam_up >= 0.2746323", KS_LO - LUP >= Fr(2746323, 10 ** 7))
print(f"   kappa*_lo - lam_up = {float(KS_LO - LUP):.10f};  at s^2 = 8: {float(KS_LO - LUP_Q):.10f};  "
      f"kappa*_hi - lam_lo = {float(KS_HI - LLO):.10f}")
check("budget at s^2 = 8 >= 0.2746325 and largest possible budget <= 0.2746331",
      KS_LO - LUP_Q >= Fr(2746325, 10 ** 7) and KS_HI - LLO <= Fr(2746331, 10 ** 7))
K = Fr(2356002, 10 ** 6)
KA_LO = Fr(83790250, 10 ** 8)
kphi = 1 - K * (1 - KA_LO)
print(f"   Remark 0.2: 1 - K(1 - kappa*_A) = {float(kphi):.7f}; budget {float(kphi - LUP):.7f} (K rounded to 2.356002; "
      f"K is an upper end only if the report's K is rounded up)")
check("Remark 0.2 arithmetic: kappa*_phi >= 0.618098 and budget >= 0.118583 (with K = 2.356002)",
      kphi >= Fr(618098, 10 ** 6) - Fr(1, 10 ** 6) and kphi - LUP >= Fr(118583, 10 ** 6) - Fr(1, 10 ** 6))
psi1, psi3 = Fr(617365, 10 ** 6), Fr(3025298, 10 ** 6)
check("per-unit root ratio on the size-1 ray: psi_3/(2 psi_1) + 3/2 = 3.950 (against 4 in the dimension price)",
      abs(float(psi3 / (2 * psi1) + Fr(3, 2)) - 3.950) < 5e-4)
check("Theorem 2 joint form: lam_lo + N(1) = 0.4995141 + 0.294301 > kappa*_hi",
      Fr(4995141, 10 ** 7) + Fr(294301, 10 ** 6) > KS_HI)
for D, lam in ((5, Fr(783612, 10 ** 6)), (20, Fr(875829, 10 ** 6)), (80, Fr(936899, 10 ** 6))):
    print(f"   class-robust corollary at D = {D}: ||B_h||_pi_phi >= lambda_L - lam_up = {float(lam - LUP):.6f} "
          f"(budget <= {float(KS_HI - LLO):.7f})")
check("auditor's corollary: lambda_L(D=5) - lam_up = 0.284097 > largest budget, on every L-closed class",
      Fr(783612, 10 ** 6) - LUP > KS_HI - LLO)
# Round 182 Proposition 2 with a signed source sigma: feasible iff some u has sigma/u + Gamma c(M0+u) u < 1.
# c(M0+u) is increasing in u (Round 182) and c(M0 + 0.0321) <= 0.950126 (Round 182 table).
p0 = Fr(1272, 10 ** 5)
cU = Fr(950126, 10 ** 6)
for lamL in (Fr(936899, 10 ** 6), Fr(961, 1000)):
    Gam = 1 / (1 - lamL)
    u = Fr(int(float((p0 / (Gam * cU)) ** 0.5) * 10 ** 6), 10 ** 6)
    val = p0 / u + Gam * cU * u
    print(f"   signed source sigma = p0, Gamma = 1/(1 - {float(lamL):.6f}) = {float(Gam):.3f}: "
          f"u = {float(u):.5f} (<= 0.0321), sigma/u + Gamma c u <= {float(val):.4f}  -> feasible: {val < 1 and u <= Fr(321, 10 ** 4)}")
lam_star = 1 - 4 * p0 * cU
print(f"   with sigma = p0 and c <= 0.950126 the Duhamel condition stays feasible for every r below 1 - 4 p0 c = {float(lam_star):.5f}")
check("signed-source Prop. 2 (sigma = p0, c <= 0.950126) is not excluded by the certified lambda_L = 0.936899; threshold ~0.952 lies below the floating 0.961",
      Fr(936899, 10 ** 6) < lam_star < Fr(961, 1000))

print("\nALL AUDIT CHECKS OK" if OK else "\nSOME AUDIT CHECK FAILED")
sys.exit(0 if OK else 1)
