#!/usr/bin/env python3
"""Round 188 audit (session/r188-audit): independent replay of the cold report
`native-claude-cold-prime-compact-sup-growth-188.md` (COLD).

Own implementation; imports no report script.

Part A (exact rationals + arb): the Fourier coefficients beta_m of Phi_a'(sqrt8 cos th), a = 2031/128, by a
  DIFFERENT method from the report (binomial series of (1 + rho cos^2)^(-1/2), rho = 256/2031, with a rigorous
  tail), the Parseval identity sum beta_m^2/2 = l_S^2, and l_S.
Part B (exact Fractions): an independent Collatz-Wielandt certificate for the dimension-price operator
  P = sum_m (|beta_m|/2) P_m (own trial vector, own truncation BC = 160, harmonics m <= 41, own tail bound).
Part C (exact, Q(sqrt2) arithmetic): Theorem 2's eigenvector, the constants 2 - sqrt2 <= psi_b/b < sqrt2.
Part D (exact integers): the per-fibre rule.  Lemma 1 (histogram identity) on random configurations;
  Lemma F (nonnegative per-fibre fill) exhaustively for r <= 5 and EVERY shift 1 <= |e| <= 6
  (the report's exhaustive run used odd e only); smallest child dimensions along the K(J^2) tree.
Part E (arb): theta, margins, the angular allowance, eta_max and l_*(eta), the non-seed budget.
Part F (floating, orientation): step ratios of A(L_S^k chi_M) and the signed rate.
Replay: .venv/bin/python -B research/paley-188-audit-cold-check.py   (under a minute)
"""
import itertools
import math
import random
from collections import Counter
from fractions import Fraction as F

import numpy as np
from flint import arb, ctx, fmpq

ctx.prec = 200
OK = True


def check(name, cond):
    global OK
    OK &= bool(cond)
    print(f'  [{"OK" if cond else "FAIL"}] {name}')


# ---------------------------------------------------------------- Part A
print('== Part A: beta_m by the binomial series (independent method) ==')
a = F(2031, 128)
rho = F(8) / (4 * a)                     # = 256/2031
assert rho == F(256, 2031)
KMAX = 260
MHA = 41                                 # harmonics kept


def binom_mhalf(k):                       # binom(-1/2, k)
    r = F(1)
    for i in range(k):
        r *= F(-1, 2) - i
        r /= i + 1
    return r


coef = [binom_mhalf(k) * rho ** k / F(4) ** k for k in range(KMAX + 1)]
# beta_m / sqrt(rho) = sum_{k >= (m-1)/2} coef_k binom(2k+1, k - (m-1)/2)  (+ tail)
tail = rho ** (KMAX + 1) / (1 - rho)      # |sum_{k > KMAX}| <= sum rho^k (binom(2k+1,j) <= 4^k)
sq = arb(fmpq(rho.numerator, rho.denominator)).sqrt()
beta = {}
for m in range(1, MHA + 1, 2):
    j0 = (m - 1) // 2
    s = sum(coef[k] * math.comb(2 * k + 1, k - j0) for k in range(j0, KMAX + 1))
    beta[m] = (arb(fmpq(s.numerator, s.denominator)) + arb(0, float(tail) * 1.0000001)) * sq
print(f'  beta_1 = {beta[1].str(16, radius=False)} (radius {float(beta[1].rad()):.1e}); beta_3 = {beta[3].str(16, radius=False)};'
      f' beta_5 = {beta[5].str(16, radius=False)}')
rep = {1: '0.33946008419161', 3: '-0.0049984361254126', 5: '0.00011094848301093', 7: '-2.7397237971492e-6'}
check('beta_1, beta_3, beta_5, beta_7 agree with the report\'s arb integrals to the printed digits',
      all(abs(float(beta[m].mid()) - float(rep[m])) <= 1e-13 * max(1e-6, abs(float(rep[m]))) * 10 for m in rep))
lS2 = 1 - arb(fmpq(4 * a.numerator, 4 * a.numerator + 8 * a.denominator)).sqrt()
lS = lS2.sqrt()
pars = sum((beta[m] ** 2 / 2 for m in beta), arb(0))
# tail of beta_m for m > MHA:  |beta_m| <= sqrt(rho) rho^((m-1)/2) / (1 - rho)
tail_m = lambda m: float(sq.upper()) * float(rho) ** ((m - 1) / 2) / (1 - float(rho))
par_tail = sum(tail_m(m) ** 2 / 2 for m in range(MHA + 2, 400, 2))
check(f'Parseval: sum_(m<=41) beta_m^2/2 = {pars.str(14)} vs l_S^2 = {lS2.str(14)} (tail <= {par_tail:.1e})',
      pars.lower() <= lS2.upper() and lS2.lower() <= pars.upper() + par_tail)
check(f'l_S = {lS.str(12)} matches 0.2400606', abs(float(lS.mid()) - 0.2400605605) < 1e-9)
# independent tail bound used below: sum_{m>MHA, odd} |beta_m|/2 and sum m |beta_m|/2
T0 = F(0)
T1 = F(0)
sqq = F(int(float(sq.upper()) * 10 ** 12) + 1, 10 ** 12)
r_hi = F(int(math.sqrt(float(rho)) * 10 ** 12) + 1, 10 ** 12)     # >= sqrt(rho)
assert r_hi * r_hi >= rho
q = r_hi * r_hi                                                  # step factor per odd m (m -> m+2): rho
first = sqq * r_hi ** (MHA + 1) / (1 - rho) / 2                  # bound for |beta_(MHA+2)|/2
T0 = first / (1 - q)
T1 = first * (F(MHA + 2) / (1 - q) + 2 * q / (1 - q) ** 2)
print(f'  tail m >= {MHA + 2}: sum |beta_m|/2 <= {float(T0):.2e}, sum m |beta_m|/2 <= {float(T1):.2e}')

# ---------------------------------------------------------------- Part B
print('\n== Part B: independent Collatz-Wielandt certificate (exact Fractions) ==')
wlo = {}
whi = {}
for m, b in beta.items():
    lo, hi = abs(b).lower(), abs(b).upper()
    wlo[m] = max(F(0), F(int(lo.man_exp()[0])) * F(2) ** int(lo.man_exp()[1]) / 2)
    whi[m] = F(int(hi.man_exp()[0])) * F(2) ** int(hi.man_exp()[1]) / 2
BC = 160
NB = 900
wf = {m: float(whi[m]) for m in whi}
# floating proposal: truncated matrix, power iteration on the row vector
phi = np.arange(NB, dtype=float)
phi[0] = 0.4


def apply_f(ph):
    sl = ph[-1] - ph[-2]
    ext = np.concatenate([ph, ph[-1] + sl * np.arange(1, MHA + 2)])
    psi = ext + ext[0] * (np.arange(len(ext)) - 1)
    out = np.zeros(NB)
    idx = np.arange(1, NB)
    for m, wm in wf.items():
        out[0] += 2 * wm * psi[m]
        lo = np.abs(idx - m)
        out[1:] += wm * (np.where(lo != 0, psi[lo], 0.0) + psi[idx + m])
    return out


for _ in range(3000):
    nw = apply_f(phi)
    phi = nw / nw[BC] * BC
lam_f = float(apply_f(phi)[BC] / phi[BC])
print(f'  [float proposal] Perron root {lam_f:.12f}')
DEN = 2 ** 60
ph = [F(round(v * DEN), DEN) for v in phi[:BC + 1]]
s_ = ph[BC] - ph[BC - 1]
kap = ph[BC] - s_ * BC
ph = ph[:BC]
PH = lambda b: ph[b] if b < BC else s_ * b + kap
PS = lambda b: PH(b) + ph[0] * (b - 1)
check('trial vector positive, slope positive', all(v > 0 for v in ph) and s_ > 0 and kap + s_ * BC > 0)


def apply_q(w, x):
    if x == 0:
        return sum(2 * wm * PS(m) for m, wm in w.items())
    return sum(wm * ((PS(abs(x - m)) if x != m else 0) + PS(x + m)) for m, wm in w.items())


lam_lo = F(round((lam_f - 1e-9) * 10 ** 12), 10 ** 12)
lam_up = F(round((lam_f + 1e-9) * 10 ** 12), 10 ** 12)
top = BC + MHA
low_ok = all(apply_q(wlo, x) >= lam_lo * PH(x) for x in range(top))
Wl = sum(wlo.values())
low_aff = (2 * Wl * (s_ + ph[0]) - lam_lo * s_ >= 0) and (2 * Wl * ((s_ + ph[0]) * top + kap - ph[0]) - lam_lo * PH(top) >= 0)
kmax = max(max(ph[b] - s_ * b for b in range(BC)), kap)
sp = s_ + ph[0]
tailb = lambda x: 2 * sp * (x * T0 + T1) + 2 * kmax * T0
up_ok = all(apply_q(whi, x) + tailb(x) <= lam_up * PH(x) for x in range(top))
Wh = sum(whi.values())
up_aff = (2 * Wh * sp + 2 * sp * T0 - lam_up * s_ <= 0) and \
         (2 * Wh * (sp * top + kap - ph[0]) + tailb(top) - lam_up * PH(top) <= 0)
check(f'lower: phi P_lo >= lam_lo phi, sizes 0..{top - 1} exact, affine beyond', low_ok and low_aff)
check(f'upper: phi P_hi + tail <= lam_up phi, sizes 0..{top - 1} exact, affine beyond', up_ok and up_aff)
print(f'  independent bracket: lambda_A in [{float(lam_lo):.11f}, {float(lam_up):.11f}]')
rep_lo, rep_up = F(9990286447, 2 * 10 ** 10), F(9990286527, 2 * 10 ** 10)
check('the independent bracket intersects the report\'s [0.4995143223, 0.4995143263] and is consistent with it',
      lam_lo <= rep_up and rep_lo <= lam_up)
ratios = [PS(b) / b for b in range(1, BC + 1)] + [sp]
c_lo, c_hi = min(ratios), max(ratios)
print(f'  own constants: c_lo = {float(c_lo):.6f}, c_hi = {float(c_hi):.6f}, K = {float(c_hi / c_lo):.6f} (report 2.356002; '
      f'K depends on the trial vector)')
th_lo = arb(fmpq(lam_lo.numerator, lam_lo.denominator)) / lS
th_up = arb(fmpq(lam_up.numerator, lam_up.denominator)) / lS
print(f'  theta_A in [{float(th_lo.lower()):.8f}, {float(th_up.upper()):.8f}]')

# ---------------------------------------------------------------- Part C
print('\n== Part C: Theorem 2 exactly in Q(sqrt2) ==')


class Q2:
    """x + y sqrt2 with rational x, y"""
    def __init__(s, x, y=0):
        s.x, s.y = F(x), F(y)

    def __add__(s, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(s.x + o.x, s.y + o.y)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(s.x - o.x, s.y - o.y)

    def __rsub__(s, o):
        return Q2(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(s.x * o.x + 2 * s.y * o.y, s.x * o.y + s.y * o.x)

    __rmul__ = __mul__

    def is_zero(s):
        return s.x == 0 and s.y == 0

    def sign(s):                       # exact sign of x + y sqrt2
        if s.y == 0:
            return (s.x > 0) - (s.x < 0)
        if s.x == 0:
            return (s.y > 0) - (s.y < 0)
        if (s.x > 0) == (s.y > 0):
            return 1 if s.x > 0 else -1
        # opposite signs: compare x^2 and 2 y^2
        d = s.x * s.x - 2 * s.y * s.y
        return (1 if s.x > 0 else -1) * ((d > 0) - (d < 0))


r2 = Q2(0, 1)
mu_ = r2 - 1
lam1 = 2 * r2
NB2 = 400
mpow = [Q2(1)]
for _ in range(NB2 + 2):
    mpow.append(mpow[-1] * mu_)
phi1 = [r2 - 1] + [Q2(b - 1) + (2 - r2) * mpow[b - 1] for b in range(1, NB2 + 2)]
psi1 = [None] + [phi1[b] + phi1[0] * (b - 1) for b in range(1, NB2 + 2)]
eq = [(2 * psi1[1] - lam1 * phi1[0]).is_zero(), (psi1[2] - lam1 * phi1[1]).is_zero()]
eq += [(psi1[b - 1] + psi1[b + 1] - lam1 * phi1[b]).is_zero() for b in range(2, NB2)]
check(f'phi P_1 = 2 sqrt2 phi exactly for slot sizes 0..{NB2 - 1}', all(eq))
check('psi_1 = 2 - sqrt2 and psi_b/b strictly increasing towards sqrt2 (exact, b < 400)',
      (psi1[1] - (2 - r2)).is_zero()
      and all((psi1[b + 1] * b - psi1[b] * (b + 1)).sign() > 0 for b in range(1, NB2))
      and all((psi1[b] - r2 * b).sign() < 0 for b in range(1, NB2)))
check('theta_1 = sqrt2 beta_1 / l_S in [1.99978311, 1.99978312]',
      1.99978310 < float((arb(2).sqrt() * beta[1] / lS).lower()) and float((arb(2).sqrt() * beta[1] / lS).upper()) < 1.99978312)
check('G_8 = 6928 <= (1 + sqrt2) 8^4 = 9888.9 and >= (sqrt2 - 1) 8^4 / ... (Round 182 table consistent)',
      6928 <= (1 + math.sqrt(2)) * 8 ** 4)

# ---------------------------------------------------------------- Part D
print('\n== Part D: the per-fibre rule (exact integers) ==')
TRIV, QUAD = 0, 1


def child(fib, e):
    """Round 80 rule as stated in COLD (R80): trivial fibre shifts by -e, quadratic by +e; negative weights stay,
    positive weights move to the other fibre; zeros dropped; each fibre refilled to r' = sum|w'|/2."""
    new = ([], [])
    tot = 0
    for f_, vals in enumerate(fib):
        for v in vals:
            w = v - e if f_ == TRIV else v + e
            tot += abs(w)
            if w < 0:
                new[f_].append(w)
            elif w > 0:
                new[1 - f_].append(w)
    assert tot % 2 == 0
    r1 = tot // 2
    fills = [r1 - len(new[0]), r1 - len(new[1])]
    out = tuple(sorted(new[k] + [0] * max(0, fills[k])) for k in (0, 1))
    return out, fills, r1


def Pm(h, m):
    out = Counter()
    for x, c in h.items():
        if x == 0:
            out[m] += 2 * c
        else:
            if x != m:
                out[abs(x - m)] += c
            out[x + m] += c
    z = sum((b - 1) * c for b, c in out.items() if b >= 1)
    out = Counter({b: c for b, c in out.items() if b})
    out[0] += z
    return out


def hist(fib):
    return Counter(abs(v) for vals in fib for v in vals)


rng = random.Random(188188)
cnt = 0
okh = True
for _ in range(3000):
    r = rng.randint(1, 10)
    # random configuration with sum |w| = 2r and at most r nonzero per fibre
    while True:
        vals = []
        tot = 2 * r
        while tot:
            v = rng.randint(1, min(tot, 5))
            vals.append(v * rng.choice((-1, 1)))
            tot -= v
        fib = ([], [])
        for v in vals:
            fib[rng.randint(0, 1)].append(v)
        if len(fib[0]) <= r and len(fib[1]) <= r:
            fib = (fib[0] + [0] * (r - len(fib[0])), fib[1] + [0] * (r - len(fib[1])))
            break
    for m in (1, 3, 5, 7, 9):
        tot = Counter()
        for e in (m, -m):
            ch, fills, r1 = child(fib, e)
            hh = Counter(abs(v) for vals in ch for v in vals if v)
            hh[0] += fills[0] + fills[1]
            tot += Counter({k: v for k, v in hh.items()})
            tot[0] = tot.get(0, 0)
        cnt += 1
        ref = Pm(hist(fib), m)
        okh &= all(tot.get(k, 0) == ref.get(k, 0) for k in set(tot) | set(ref))
check(f'Lemma 1: pooled children histogram = P_m(parent) on {cnt} (configuration, m) pairs, m odd <= 9', okh)

neg = Counter()
cases = Counter()
example = None
for r in range(1, 6):
    pool = list(itertools.combinations_with_replacement(range(-2 * r, 2 * r + 1), r))
    for FA in pool:
        sa = sum(map(abs, FA))
        if sa > 2 * r:
            continue
        for FB in pool:
            if sa + sum(map(abs, FB)) != 2 * r:
                continue
            for e in (1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6):
                ch, fills, r1 = child((list(FA), list(FB)), e)
                cases[abs(e)] += 1
                if min(fills) < 0:
                    neg[abs(e)] += 1
                    if example is None and abs(e) == 2:
                        example = (FA, FB, e, fills)
print('  exhaustive r <= 5: children per |e|:', dict(sorted(cases.items())))
print('  negative per-fibre fills per |e|:   ', {k: neg.get(k, 0) for k in sorted(cases)})
check('Lemma F holds for every odd |e| <= 5 and for |e| = 4, 6 (no negative fill)',
      all(neg.get(k, 0) == 0 for k in (1, 3, 4, 5, 6)))
check(f'Lemma F FAILS for |e| = 2 (as stated "every integer e >= 1"): e.g. fibres {example[:2]}, e = {example[2]}, '
      f'fills {example[3]}', neg.get(2, 0) > 0)
# the proof's last display for e = 2 has the negative term (e - 3)u = -u at u = 1: consistent with the failure

# smallest child dimensions along the K(J^2) tree with odd shifts (are all nodes of dimension > 1?)
root = ((-2, 2), (0, 0))
layer = {root: 1}
mind = 99
dims_seen = Counter()
for depth in range(1, 9):
    nxt = Counter()
    for M, c in layer.items():
        for e in ((1, -1, 3, -3) if depth <= 4 else (1, -1)):
            ch, fills, r1 = child([list(M[0]), list(M[1])], e)
            dims_seen[r1] += 1
            mind = min(mind, r1)
            key = (tuple(ch[0]), tuple(ch[1]))
            if depth < 8:
                nxt[key] += c
    layer = nxt
print(f'  K(J^2) tree (+-1, +-3 to depth 4, +-1 to depth 8): smallest child dimension {mind}; '
      f'dimensions <= 2 seen: {sum(v for k, v in dims_seen.items() if k <= 2)}')
check('no child of dimension 0 or 1 in the K(J^2) tree (Lemma 2 needs dimension > 1 at every node)', mind >= 2)
# formal configurations can have a zero-dimensional child: all slots u = 1 (|w| = 1), e = +1
ch, fills, r1 = child(([1, 1, 1], [-1, -1, -1]), 1)
print(f'  formal valid configuration ([1,1,1], [-1,-1,-1]) under J^(+1): child dimension {r1} (degenerate; '
      f'excluded only through the inherited (R80))')

# which leaves share weight data (mod shift, negation) in the +-1 tree from K(J^2)?  (report: "presumably
# the dual/mirror pairs")
def canon(fib):
    best = None
    for sg in (1, -1):
        g_ = [sorted(sg * v for v in f_) for f_ in fib]
        mn = min(v for f_ in g_ for v in f_)
        g_ = tuple(tuple(v - mn for v in f_) for f_ in g_)
        best = g_ if best is None or g_ < best else best
    return best


for depth in (4, 8):
    leaves = {}
    for path in itertools.product((1, -1), repeat=depth):
        M = ((-2, 2), (0, 0))
        for e in path:
            ch, fills, r1 = child([list(M[0]), list(M[1])], e)
            M = (tuple(ch[0]), tuple(ch[1]))
        leaves[path] = M
    cl = {}
    for pth, M in leaves.items():
        cl.setdefault(canon(M), []).append(pth)
    pairs = [v for v in cl.values() if len(v) == 2]
    mirror = sum(1 for v in pairs if v[1] == tuple(-x for x in v[0]))
    negated = sum(1 for v in pairs
                  if leaves[v[1]] == tuple(tuple(sorted(-x for x in f_)) for f_ in leaves[v[0]]))
    flip13 = sum(1 for v in pairs if {v[0], v[1]} == {v[0], tuple(-x if i in (0, 2) else x for i, x in enumerate(v[0]))})
    print(f'  depth {depth}: {len(pairs)} pairs; pairs of the form (e, -e): {mirror}; pairs with exactly negated '
          f'weights (same fibres): {negated}; pairs differing by the signs of e_1 and e_3: {flip13}')
    if depth == 4:
        check('depth 4: every pair has exactly negated weight data (dual-type), and none is the sign mirror (e, -e)',
              negated == len(pairs) and mirror == 0)

# ---------------------------------------------------------------- Part E
print('\n== Part E: comparisons (arb) ==')
lam_rep_lo = arb(fmpq(9990286447, 2 * 10 ** 10))
lam_rep_up = arb(fmpq(9990286527, 2 * 10 ** 10))
thA_lo, thA_up = lam_rep_lo / lS, lam_rep_up / lS
check(f'theta_A (report bracket) in [{float(thA_lo.lower()):.8f}, {float(thA_up.upper()):.8f}] = [2.08078462, 2.08078464]',
      2.08078461 < float(thA_lo.lower()) and float(thA_up.upper()) < 2.08078465)
inv_q = 1 / arb('0.5145')
check(f'theta_A > 1/0.5145 = {float(inv_q.upper()):.6f}; margin {float((thA_lo / inv_q).lower()) - 1:.4f}',
      thA_lo.lower() > inv_q.upper())
qang = arb('0.462748')          # Round 187 Lemma 3(c) upper bound for q_ang(2.338)
check(f'2.1610 <= 1/q_ang(2.338): 1/0.462748 = {float((1 / qang).lower()):.7f}; theta_A < 2.1610 (margin '
      f'{float((arb("2.1610") / thA_up).lower()) - 1:.4f})', (1 / qang).lower() >= arb('2.1610') and thA_up.upper() < arb('2.1610'))
check('rate thresholds: 1.94363 l_S = 0.46659; 2.1610 l_S = 0.51877',
      abs(float((inv_q * lS).mid()) - 0.46659) < 5e-6 and abs(float((arb('2.1610') * lS).mid()) - 0.51877) < 5e-6)
fa = arb(fmpq(4 * a.numerator, a.denominator))
for qv, rep_eta in (('0.5145', 0.60613), ('0.535', 0.99833), ('0.545', 1.19692)):
    T = (lam_rep_lo * arb(qv)) ** 2
    Kq = fa / (1 - T)
    em = (16 + Kq * Kq).sqrt() - 4 - fa
    ls_at = (1 - fa / ((fa + em) * (fa + em + 8)).sqrt()).sqrt()
    check(f'eta_max(q={qv}) = {float(em.mid()):.5f} (report {rep_eta}); l_*(eta_max) = lam_lo q = {float(ls_at.mid()):.6f}',
          abs(float(em.mid()) - rep_eta) < 1e-5 and abs(float(ls_at.mid()) - float((lam_rep_lo * arb(qv)).mid())) < 1e-12)
for eta, rep_l in (('0', 0.240061), ('0.0306', 0.240952), ('0.25', 0.247225), ('3.853', 0.329703)):
    e_ = arb(eta)
    ls_ = (1 - fa / ((fa + e_) * (fa + e_ + 8)).sqrt()).sqrt()
    check(f'l_*({eta}) = {float(ls_.mid()):.6f} (report {rep_l})', abs(float(ls_.mid()) - rep_l) < 1e-6)
check('Jensen step: y -> y/(4a+y) concave increasing; E[1/(A + 8cos^2)] = (A(A+8))^(-1/2) (numerical spot check)',
      abs(np.mean(1 / (70.0 + 8 * np.cos(np.linspace(0, np.pi, 200001)[:-1]) ** 2)) - 1 / math.sqrt(70 * 78)) < 1e-9)
kstar = F(7741471, 10 ** 7)
bud = kstar - rep_up
check(f'non-seed budget kappa*_lo - lam_up = {float(bud):.9f}: >= 0.274632 holds; the report\'s ">= 0.274633" '
      f'is {float(F(274633, 10 ** 6) - bud):.1e} too high (rounding; correction)',
      bud >= F(274632, 10 ** 6) and bud < F(274633, 10 ** 6) and abs(float(kstar) - 0.53255 - 0.24159) < 1e-5)
check('seed-linear J^(+-1) rate at t = a: 2 sqrt2 * sqrt(2/a)/2 = 2/sqrt(a) = 0.5020882',
      abs(2 / math.sqrt(float(a)) - 0.5020882046) < 1e-9)

# ---------------------------------------------------------------- Part F
print('\n== Part F: floating orientation ==')
wfl = {m: abs(float(beta[m].mid())) / 2 for m in beta}
wsg = {m: float(beta[m].mid()) / 2 for m in beta}


def step(h, w):
    out = Counter()
    for m, wm in w.items():
        for k, v in Pm(h, m).items():
            out[k] += wm * v
    return out


def mass(h):
    return sum(k * v for k, v in h.items())


h = Counter({2: 2, 0: 2})            # K(J^2): fibres {-2, 2}, {0, 0}
prev = mass(h)
rat = []
for k in range(26):
    h = step(h, wfl)
    h = Counter({kk: v for kk, v in h.items() if kk <= 400})
    mm = mass(h)
    rat.append(mm / prev)
    prev = mm
print('  A step ratios from K(J^2):', ' '.join(f'{x:.5f}' for x in rat[:6]), '...', f'{rat[-1]:.7f}')
check('A step ratios converge to 0.49951', abs(rat[-1] - 0.4995143) < 2e-6)
# signed operator (all leaves at + dimension): Perron root of the signed truncated matrix
NBs = 500
Mt = np.zeros((NBs, NBs))
for x in range(NBs):
    hx = Counter({x: 1})
    if x >= 1:
        hx[0] = x - 1               # a slot of size x with its fill
    for m, wm in wsg.items():
        for k, v in Pm(Counter({x: 1}), m).items():
            if k < NBs:
                Mt[k, x] += wm * v
ev = np.linalg.eigvals(Mt)
print(f'  signed operator sum beta_m/2 P_m (truncated {NBs}): spectral radius {max(abs(ev)):.7f} (report 0.4619104)')
check('signed rate 0.46191 reproduced (floating)', abs(max(abs(ev)) - 0.4619104) < 1e-5)

print('\nALL AUDIT CHECKS OK' if OK else '\nSOME AUDIT CHECK FAILED')
