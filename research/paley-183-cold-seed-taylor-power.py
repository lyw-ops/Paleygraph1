#!/usr/bin/env python3
"""Round 183 cold price (call cold-prime-seed-multiplier-power-rate): exact m-step
growth of the FULL seed multiplier L_S = K Phi_t'(S) (seed-only Taylor terms included)
under the Round 80 per-simple rule, and the budget left for the non-seed part.

EXACT (Fractions and integer square roots, outward rounding):

 1. Fourier coefficients of the seed multiplier.  With S = s C, C = Re J, J = e^{i theta}
    at good coordinates, beta = s^2/(4t):
        Phi_t'(s cos th) = (s/(2 sqrt t)) * g_beta(th),  g_beta = cos th (1 + beta cos^2 th)^(-1/2)
        g_beta = sum_{k odd} ghat_k(beta) e^{i k th},
        ghat_k(beta) = sum_{l >= (|k|-1)/2} (-1)^l c_l beta^l binom(2l+1, l+(|k|+1)/2) / 2^(2l+1),
    c_l = binom(2l,l)/4^l.  Parameter set: t in the closed square Q (half-width 2^-17 about
    a = 2031/128), s = s_p with p >= P1 (s_p^2 = 8 + 8/(p-1)).  Then |beta - 256/2031| <= delta
    and |s/(2 sqrt t)| <= varpi := s_up/sqrt(N), N = 4(a - 2^-17).  gamma_k >= |ghat_k(beta)|
    uniformly (partial sum + tail + delta * derivative majorant).
 2. Per-simple rule for J^k (k odd): k-fold line multiplication, fibre A shifted by -k, B by +k,
    negative weights stay, positive weights change fibre, refill each fibre with zeros up to
    r' = (1/2) sum |w'|.  Refill is >= 0 for every valid parent (|k| = 1: Lemma below; |k| >= 3:
    r' >= r(|k|-1) >= 2r).  On slot-count vectors the step is linear, so the m-step path-summed
    price is a linear functional, computed here by the ADJOINT recursion phi_{j+1} = M^T phi_j
    with M = sum_{|k|<=K} gamma_k M_k.
    G_m(alpha) = sup over valid simples is a linear-fractional programme over atoms (one nonzero
    slot plus its induced zeros) with two constraints (zero counts >= 0); columns are the atoms
    |v| <= mK+6 and the four |v| -> infinity directions (exact affinity in |v| for |v| >= mK+2 is
    checked).  A floating LP proposes the support; the exact primal value on it (lower) and the
    exact dual objective at the exact dual point (upper) are computed in rationals.  lo == hi means
    G_m is computed exactly.  The Round 182 mediant value (dual point mu = 0) is printed as 'med'.
    |k| > K is a perturbation of one-step price <= sum (1+alpha)(1+|k|) gamma_k.
 3. Power constants from submultiplicativity, the beta-budget of Corollary 2.2 (Round 182),
    the h-linear price: Phi_t''(S) = (1/(2 sqrt t)) sum_k bhat_k J^k (k even), Fourier l1 = 1 by
    the alternating sign pattern, and the word-rank rule rank(H J^k F) <= (|k|+2) d r, so the cost
    is (1+alpha) A(h) sum_k (|k|+2)|bhat_k| / sqrt N; the h-higher Taylor word majorant (seed lines
    counted as factors); and the largest admissible A(h) per alpha.
    Two readings of the inherited constants: (b1) p0, c(M) transfer verbatim to pi_alpha (as in
    Round 182); (b1*) re-derived: p0' = (1+alpha) p0 (from A(R_602) <= P_5000(R_602)) and
    c' = ((1+alpha)/2) c(M) (the Round 162/174 Taylor words with output price <= (1+alpha) rank).
 4. Certified bracket of kappa*(p0) = sup_u [1 - p0/u - c(M0+u) u] (re-derived, outward).

Floating output is labelled [float]; every other printed bound is rounded outward
(lower bounds down, upper bounds up).

Replay:  .venv/bin/python -B research/paley-183-cold-seed-taylor-power.py
Standard library only.
"""
from fractions import Fraction as F
from math import comb, isqrt
import sys
import time

T0 = time.time()

# ----------------------------------------------------------------- exact helpers
BITS = 96


def sqrt_lo(q, bits=BITS):
    q = F(q)
    num, den = q.numerator, q.denominator
    return F(isqrt(num * den * 4 ** bits), den * 2 ** bits)


def sqrt_hi(q, bits=BITS):
    q = F(q)
    return sqrt_lo(q, bits) + F(1, q.denominator * 2 ** bits)


def round_up(q, den=10 ** 18):
    q = F(q)
    return F(-((-q.numerator * den) // q.denominator), den)


def round_dn(q, den=10 ** 18):
    q = F(q)
    return F((q.numerator * den) // q.denominator, den)


def up(q, d=6):
    """decimal string >= q"""
    q = F(q)
    s = 10 ** d
    v = -((-q.numerator * s) // q.denominator)
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v // s}.{v % s:0{d}d}"


def dn(q, d=6):
    """decimal string <= q"""
    q = F(q)
    s = 10 ** d
    v = (q.numerator * s) // q.denominator
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v // s}.{v % s:0{d}d}"


def root_up(G, m, prec=10 ** 9):
    """rational lam >= G^(1/m), within 1/prec"""
    G = F(G)
    lo, hi = F(0), max(F(1), G)
    while hi - lo > F(1, prec):
        mid = (lo + hi) / 2
        if mid ** m >= G:
            hi = mid
        else:
            lo = mid
    hi = round_up(hi, prec)
    assert hi ** m >= G
    return hi


# ----------------------------------------------------------------- constants
a = F(2031, 128)
N = 4 * (a - F(1, 2 ** 17))
SQN_LO = sqrt_lo(N)
SQN_HI = sqrt_hi(N)
P1 = 10 ** 6                                   # primes p >= P1 (all corrections beyond this are eps(p) -> 0)
S2_UP = 8 + F(8, P1 - 1)                       # s_p^2 = 8p/(p-1) <= S2_UP
S_UP = sqrt_hi(S2_UP)                          # s_p <= S_UP
S_LIM_LO = sqrt_lo(8)                          # 2 sqrt 2 <= s_p
VARPI = round_up(S_UP / SQN_LO)                # |s/(2 sqrt t)| <= s/sqrt N <= VARPI
BETA0 = F(256, 2031)                           # 8/(4a)
# |beta - beta0| <= (s^2-8)/(4|t|) + 2|t-a|/(|t| a),  |t| >= a - 2^-17, |t-a| <= sqrt2 2^-17 <= 1.5 * 2^-17
TMIN = a - F(1, 2 ** 17)
DELTA = round_up((S2_UP - 8) / (4 * TMIN) + 2 * F(3, 2) * F(1, 2 ** 17) / (TMIN * a))
BMAJ = BETA0 + DELTA
M0 = F(4823, 1000)
P0 = F(1272, 100000)

print("== constants (exact; printed outward) ==")
print(f"N = 4(2031/128 - 2^-17); sqrt N in [{dn(SQN_LO, 9)}, {up(SQN_HI, 9)}]")
print(f"primes p >= {P1}: s_p <= {up(S_UP, 9)} (limit 2 sqrt 2 >= {dn(S_LIM_LO, 9)})")
print(f"varpi = sup |s_p/(2 sqrt t)| <= {up(VARPI, 9)}   (182 per-line factor = varpi/2)")
print(f"beta0 = 256/2031 = {dn(BETA0, 9)}..; |beta - beta0| <= delta = {up(DELTA, 12)} on Q x {{p >= {P1}}}")


# ----------------------------------------------------------------- 1. Fourier coefficients
def c_l(l):
    return F(comb(2 * l, l), 4 ** l)


def ghat_partial(k, beta, L):
    k = abs(k)
    j = (k + 1) // 2
    s = F(0)
    for l in range((k - 1) // 2, L + 1):
        s += (-1) ** l * c_l(l) * beta ** l * F(comb(2 * l + 1, l + j), 2 ** (2 * l + 1))
    return s


LSER = 40
TAIL_L = BMAJ ** (LSER + 1) / (1 - BMAJ)              # sum_{l>L} c_l b^l w_{l,k} <= b^{L+1}/(1-b)
DER = F(1, 2) / (1 - BMAJ) / sqrt_lo(1 - BMAJ)        # sum_l l c_l b^(l-1) = (1/2)(1-b)^(-3/2)
KMAX_SER = 2 * LSER + 1
gamma = {}
ghat0 = {}
for k in range(1, KMAX_SER + 1, 2):
    g0 = ghat_partial(k, BETA0, LSER)
    ghat0[k] = g0
    gamma[k] = round_up(abs(g0) + TAIL_L + DELTA * DER)
    gamma[-k] = gamma[k]
# for |k| > 2 LSER + 1 the partial sum is empty: |ghat_k| <= b^((|k|-1)/2)/(1-b) (handled in tail)

print("\n== 1. seed multiplier Phi_t'(S) = (s/(2 sqrt t)) sum_k ghat_k(beta) J^k (exact bounds) ==")
for k in (1, 3, 5, 7, 9):
    print(f"k=+-{k}: ghat_k(beta0) in [{dn(ghat0[k], 12)}, {up(ghat0[k], 12)}] (series to l={LSER}, "
          f"tail <= {float(TAIL_L):.1e}); uniform gamma_k = {up(gamma[k], 12)}")
print(f"sign pattern: ghat_k(beta0) has sign (-1)^((|k|-1)/2) for |k| <= 9:",
      all((ghat0[k] > 0) == (((k - 1) // 2) % 2 == 0) for k in (1, 3, 5, 7, 9)))
s_abs = sum(abs(ghat0[k]) for k in range(1, KMAX_SER + 1, 2)) * 2
print(f"sum_k |ghat_k(beta0)| (|k|<={KMAX_SER}) = {dn(s_abs, 12)} .. vs 1/sqrt(1+beta0) = "
      f"[{dn(1 / sqrt_hi(1 + BETA0), 12)}, {up(1 / sqrt_lo(1 + BETA0), 12)}]  (no sign identity for odd k: l1 > sup)")
print(f"compare: linear seed term has ghat_{{+-1}} = 1/2 each, l1 mass 1")

KOP = 5                    # J^k with |k| <= KOP in the exact operator; |k| > KOP as perturbation
KS = [k for k in range(-KOP, KOP + 1) if k % 2]


def tail_cost_full(alpha):
    """sum_{|k|>KOP} (1+alpha)(1+|k|) |ghat_k(beta)|, uniform over the parameter set.
    |k| <= KMAX_SER: gamma_k (already uniform).  |k| > KMAX_SER: the partial sum is empty and
    |ghat_k(beta)| <= sum_{l>=(|k|-1)/2} c_l |beta|^l w_{l,k} <= b^((|k|-1)/2)/(1-b), b = BMAJ >= |beta|."""
    s = F(0)
    for k in range(KOP + 2, KMAX_SER + 1, 2):
        s += 2 * (1 + alpha) * (1 + k) * gamma[k]
    q = sqrt_hi(BMAJ)
    k0 = KMAX_SER + 2
    # sum_{k>=k0, odd} (1+k) q^(k-1) = q^(k0-1) [ (1+k0)/(1-q^2) + 2 q^2/(1-q^2)^2 ]
    geo = q ** (k0 - 1) * ((1 + k0) / (1 - q * q) + 2 * q * q / (1 - q * q) ** 2)
    s += 2 * (1 + alpha) * geo / (1 - BMAJ)
    return round_up(s)


# ----------------------------------------------------------------- 2. per-simple rule
A_, B_ = 0, 1


def shifted(v, fb, k):
    """slot (v,fb) under J^k: returns (w, dest_fibre or None if w == 0)"""
    w = v - k if fb == A_ else v + k
    if w < 0:
        return w, fb
    if w > 0:
        return w, 1 - fb
    return 0, None


def adjoint(m, alpha, coef, V0):
    """phi_m(t) = 2*pi_alpha( M^m e_t ) for |v| <= V0, M = sum_k coef[k] M_k"""
    K = max(abs(k) for k in coef)
    R = V0 + m * K
    phi = {(v, fb): F(abs(v)) + (alpha if v == 0 else 0) for v in range(-R, R + 1) for fb in (A_, B_)}
    for j in range(m):
        R -= K
        new = {}
        for v in range(-R, R + 1):
            for fb in (A_, B_):
                tot = F(0)
                for k, g in coef.items():
                    w, dfb = shifted(v, fb, k)
                    val = F(abs(w), 2) * (phi[(0, A_)] + phi[(0, B_)])
                    if dfb is not None:
                        val += phi[(w, dfb)] - phi[(0, dfb)]
                    tot += g * val
                new[(v, fb)] = tot
        phi = new
    return phi


def atoms(phi, alpha, V0):
    res = {}
    for v in range(-V0, V0 + 1):
        if v == 0:
            continue
        for fb in (A_, B_):
            zA = F(abs(v), 2) - (1 if fb == A_ else 0)
            zB = F(abs(v), 2) - (1 if fb == B_ else 0)
            n = phi[(v, fb)] + zA * phi[(0, A_)] + zB * phi[(0, B_)]
            d = abs(v) + alpha * (zA + zB)
            res[(v, fb)] = (n, d, zA, zB)
    return res


def solve(rows, rhs):
    n = len(rows)
    M = [list(map(F, r)) + [F(b)] for r, b in zip(rows, rhs)]
    for i in range(n):
        p = next((j for j in range(i, n) if M[j][i] != 0), None)
        if p is None:
            return None
        M[i], M[p] = M[p], M[i]
        for j in range(n):
            if j != i and M[j][i] != 0:
                f = M[j][i] / M[i][i]
                M[j] = [x - f * y for x, y in zip(M[j], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]


def lp_exact(co, dirs):
    """Exact sup over valid simples of the path-summed price ratio.
    Columns: atoms |v| <= V0 and the four |v|->infinity direction columns (exact affinity).
    Primal  max sum lam n  s.t. sum lam d = 1, sum lam zA >= 0, sum lam zB >= 0, lam >= 0
    (every valid simple is a nonnegative combination of atoms; conversely rational feasible
    combinations are valid simples after scaling; direction columns are limits).
    Dual    min_{mu >= 0} max_cols (n + muA zA + muB zB)/d.
    A floating LP (scipy/HiGHS) only proposes the support; the lower value is the exact primal
    value on that support, the upper value is the exact dual objective at the exact dual point.
    Returns (lower, upper); lower == upper means the sup is computed exactly."""
    import numpy as np
    from scipy.optimize import linprog
    cols = list(co.values()) + dirs
    c = -np.array([float(x[0]) for x in cols])
    Aeq = np.array([[float(x[1]) for x in cols]])
    Aub = -np.array([[float(x[2]) for x in cols], [float(x[3]) for x in cols]])
    res = linprog(c, A_ub=Aub, b_ub=[0.0, 0.0], A_eq=Aeq, b_eq=[1.0], bounds=(0, None), method="highs")
    assert res.status == 0
    xs = res.x
    support = [i for i in range(len(cols)) if xs[i] > 1e-11 * max(xs)]
    lo = None
    hi = max(n / d for (n, d, zA, zB) in cols)          # mu = 0: mediant bound
    for tight in ([], [0], [1], [0, 1]):
        if len(tight) + 1 != len(support):
            continue
        rows = [[cols[i][1] for i in support]] + [[cols[i][2 + T] for i in support] for T in tight]
        lam = solve(rows, [1] + [0] * len(tight))
        if lam is not None and all(l >= 0 for l in lam):
            zA = sum(l * cols[i][2] for l, i in zip(lam, support))
            zB = sum(l * cols[i][3] for l, i in zip(lam, support))
            if zA >= 0 and zB >= 0:
                val = sum(l * cols[i][0] for l, i in zip(lam, support))
                lo = val if lo is None else max(lo, val)
        # dual point: n_i + sum_T mu_T z_{T,i} = G d_i on the support
        drows = [[-cols[i][1]] + [cols[i][2 + T] for T in tight] for i in support]
        sol = solve(drows, [-cols[i][0] for i in support])
        if sol is None:
            continue
        mu = {T: sol[1 + j] for j, T in enumerate(tight)}
        if any(v < 0 for v in mu.values()):
            continue
        muA, muB = mu.get(0, F(0)), mu.get(1, F(0))
        g = max((n + muA * zA + muB * zB) / d for (n, d, zA, zB) in cols)
        hi = min(hi, g)
    if lo is None:
        lo = F(0)
    return lo, hi


def growth(m, alpha, coef):
    K = max(abs(k) for k in coef)
    V0 = m * K + 6
    phi = adjoint(m, alpha, coef, V0)
    co = atoms(phi, alpha, V0)
    # exact affinity of n_t in |v| for |v| >= mK+2 (d_t is affine by definition)
    dirs = []
    for fb in (A_, B_):
        for sg in (1, -1):
            vals = [co[(sg * v, fb)][0] for v in range(m * K + 2, V0 + 1)]
            assert len(vals) >= 3
            assert all(vals[i] - 2 * vals[i + 1] + vals[i + 2] == 0 for i in range(len(vals) - 2)), \
                ("affinity", m, alpha)
            dn_ = co[(sg * V0, fb)][0] - co[(sg * (V0 - 1), fb)][0]
            dirs.append((dn_, 1 + alpha, F(1, 2), F(1, 2)))
    gmed = max(max(n / d for (n, d, zA, zB) in co.values()), max(x[0] / x[1] for x in dirs))
    lo, hi = lp_exact(co, dirs)
    assert lo <= hi <= gmed
    return lo, hi, gmed


# ---- regression: the Round 182 seed-linear operator (gamma_{+-1} = 1) must reproduce its G_up
print("\n== 2a. regression against Round 182 (linear seed, coefficient 1 on J^{+-1}) ==")
R182 = {(F(0), 1): F(4), (F(0), 2): F(12), (F(0), 4): F(104), (F(0), 8): F(6928),
        (F(1), 1): F(3), (F(1), 2): F(9), (F(1), 4): F(75), (F(1), 8): F(4915)}
ok = True
for (al, m), val in R182.items():
    gl, gu, gmed = growth(m, al, {1: F(1), -1: F(1)})
    ok &= (gmed == val)
    print(f"alpha={al} m={m}: mediant G_up = {gmed} (Round 182: {val}); exact sup in [{dn(gl, 6)}, {up(gu, 6)}]")
print("regression OK:", ok)
assert ok

# ---- the full seed multiplier
COEF = {k: gamma[k] for k in KS}
print(f"\n== 2b. full seed multiplier, exact m-step growth (J^k, |k|<={KOP}; weights gamma_k) ==")
print("G_m(alpha) = sup over valid simples of pi_alpha(path-summed m-step child)/pi_alpha(parent),")
print("  ||L_S^m||_{pi_alpha} <= G_m varpi^m (+ |k|>5 perturbation).  [lo, hi] = exact primal/dual values;")
print("  lo == hi means exact.  'med' = Round 182 mediant method.  'lin' = exact sup for the linear seed")
print("  (coefficient 1/2 on J^{+-1}, same normalisation).  rate = G^(1/m) varpi, outward.")
ALPHAS = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
AFINE = [F(j, 16) for j in range(0, 17)]
MMAX = 8
GU, GL, GM = {}, {}, {}
nexact = 0
for al in AFINE:
    for m in range(1, MMAX + 1):
        gl, gu, gm = growth(m, al, COEF)
        GU[(al, m)], GL[(al, m)], GM[(al, m)] = gu, gl, gm
        nexact += (gl == gu)
        if al in ALPHAS:
            ll, lh, _ = growth(m, al, {1: F(1, 2), -1: F(1, 2)})
            ex = "exact" if gl == gu else "bracket"
            print(f"alpha={str(al):>3} m={m}: G in [{dn(gl, 6)}, {up(gu, 6)}] ({ex}) med={up(gm, 6)}"
                  f"  rate<={up(root_up(gu, m) * VARPI, 5)} | lin [{dn(ll, 6)}, {up(lh, 6)}]"
                  f" rate<={up(root_up(lh, m) * VARPI, 5)}")
    sys.stdout.flush()
print(f"exact (lo == hi) in {nexact} of {len(AFINE) * MMAX} (alpha, m) cases")
print(f"[time {time.time() - T0:.1f}s]")


# ----------------------------------------------------------------- 3. kappa* bracket (re-derived)
def c_up(M):
    x = F(M) ** 2 / N
    return 2 * (1 + x / 2) / (SQN_LO * (1 - x) ** 2 * sqrt_lo(1 - x, 64))


def c_lo(M):
    x = F(M) ** 2 / N
    return 2 * (1 + x / 2) / (SQN_HI * (1 - x) ** 2 * sqrt_hi(1 - x, 64))


def kappa_bracket(p0, fac, fcc=None):
    """sup_{0<u<=3/8} [1 - fac p0/u - fcc c(M0+u) u]; returns (lower, upper, u_at_lower)"""
    fcc = fac if fcc is None else fcc
    best, ubest = F(-10), None
    # coarse grid for lower bound
    grid = [F(i, 1500) * F(3, 8) for i in range(1, 1501)]
    vals = []
    for u in grid:
        v = 1 - fac * p0 / u - fcc * c_up(M0 + u) * u
        vals.append(v)
        if v > best:
            best, ubest = v, u
    # refine lower bound around ubest
    h = F(3, 8) / 1500
    uc = ubest
    for i in range(-200, 201):
        u = uc + h * F(i, 200)
        if 0 < u <= F(3, 8):
            v = 1 - fac * p0 / u - fcc * c_up(M0 + u) * u
            if v > best:
                best, ubest = v, u
    # upper bound: phi(u) <= 1 - fac p0/u_hi - fac c(M0+u_lo) u_lo on [u_lo,u_hi]; adaptive
    stack = [(F(0), F(3, 8))]
    upper = F(-10)
    tol = F(1, 10 ** 8)
    while stack:
        lo_, hi_ = stack.pop()
        if lo_ == 0:
            ubd = 1 - fac * p0 / hi_          # c >= 0
        else:
            ubd = 1 - fac * p0 / hi_ - fcc * c_lo(M0 + lo_) * lo_
        if ubd <= best + tol or hi_ - lo_ < F(1, 10 ** 9):
            upper = max(upper, ubd)
            continue
        mid = (lo_ + hi_) / 2
        stack += [(lo_, mid), (mid, hi_)]
    return best, max(upper, best), ubest


print("\n== 3. threshold kappa*(p0) of Proposition 1/Corollary 2.1 (exact, outward) ==")
K_B1 = kappa_bracket(P0, 1)
print(f"(b1)  p0=0.01272, c=c(M0+u): kappa* in [{dn(K_B1[0], 8)}, {up(K_B1[1], 8)}]")
KAP = {}
print("(b1*) re-derived transfer to pi_alpha: p0' = (1+alpha) p0 [A(R_602) <= P_5000(R_602), pi_alpha <= (1+alpha)A],")
print("      c' = ((1+alpha)/2) c(M) [Round 162/174 Taylor words: output price <= 2 rank in P_5000, <= (1+alpha) rank in pi_alpha]")
for al in AFINE:
    KAP[al] = kappa_bracket(P0, 1 + al, (1 + al) / 2)
    print(f"(b1*) alpha={str(al):>5}: kappa*_alpha in [{dn(KAP[al][0], 8)}, {up(KAP[al][1], 8)}]  (u={dn(KAP[al][2], 5)})")
print(f"[time {time.time() - T0:.1f}s]")


# ----------------------------------------------------------------- 4. budgets and h-terms
def power_form(al, m0):
    """(lam_S, C_S) with ||L_S^m||_{pi_alpha} <= C_S lam_S^m for all m (exact rationals)"""
    lamhat = root_up(GU[(al, m0)], m0)
    C = F(1)
    for r in range(1, m0):
        C = max(C, GU[(al, r)] / lamhat ** r)
    C = round_up(C, 10 ** 9)
    tau = tail_cost_full(al) * VARPI
    lamS = round_up(VARPI * lamhat + C * tau, 10 ** 9)
    return lamS, C


# h-linear multiplier Phi_t''(S) = (1/(2 sqrt t)) sum_k bhat_k(beta) J^k (k even), with
#   bhat_{2i}(beta) = sum_{l>=|i|} binom(-3/2,l) beta^l binom(2l,l+i)/4^l   (sign (-1)^i for real beta>0).
# Word-rank rule (moment form): H (dim d) * J^k * F (dim r) has generic rank <= (|k|+2) d r.
# So the h-linear cost in pi_alpha is <= (1+alpha) A(h) SIGH, SIGH = (1/sqrt N) sum_k (|k|+2)|bhat_k(beta)|.
def binom_m32(l):
    v = F(1)
    for i in range(l):
        v *= F(-3, 2) - i
        v /= i + 1
    return v


LB = 40
BH0 = {}
for i in range(0, LB + 1):
    BH0[i] = sum(binom_m32(l) * BETA0 ** l * F(comb(2 * l, l + i), 4 ** l) for l in range(i, LB + 1))
# tail l > LB: |binom(-3/2,l)| <= (2l+1) c_l <= 2l+1; weighted sum over k of (|k|+2) w <= (2l+2); bound
#   sum_{l>LB} (2l+1)(2l+2) b^l  <= b^(LB+1) (2LB+3)(2LB+4) / (1-b)^3   (crude, ratio test)
TAILB = BMAJ ** (LB + 1) * (2 * LB + 3) * (2 * LB + 4) / (1 - BMAJ) ** 3
# delta-part: sum_k (|k|+2)|bhat_k(beta)-bhat_k(beta0)| <= delta sum_l l |binom(-3/2,l)| b^(l-1) (2l+2)
DERB = sum(l * abs(binom_m32(l)) * BMAJ ** (l - 1) * (2 * l + 2) for l in range(1, 200)) \
    + BMAJ ** 199 * 400 ** 3 / (1 - BMAJ) ** 4
SUMB = BH0[0] * 2 + sum(2 * abs(BH0[i]) * (2 * i + 2) for i in range(1, LB + 1))
SIGH = round_up((SUMB + TAILB + DELTA * DERB) / SQN_LO)
SIG1 = round_up((abs(BH0[0]) + 2 * sum(abs(BH0[i]) for i in range(1, LB + 1)) + TAILB + DELTA * DERB) / SQN_LO)


def Gall(y, lo=False):
    """G_all(y) = sum_{l>=0} c_l (2l+2) y^(2l+1)/N^(l+1/2) = y(2N - y^2)/(N - y^2)^(3/2)"""
    D = N - y * y
    sq = sqrt_hi(D, 64) if lo else sqrt_lo(D, 64)
    return y * (2 * N - y * y) / (D * sq)


def Gall_d(y, lo=False):
    """G_all'(y) = N (2N + y^2)/(N - y^2)^(5/2)"""
    D = N - y * y
    sq = sqrt_hi(D, 64) if lo else sqrt_lo(D, 64)
    return N * (2 * N + y * y) / (D * D * sq)


def H_up(A):
    """h-higher (j>=2) word majorant, seed lines counted as factors (rank <= (2l+2) prod d):
       G_all(s+A) - G_all(s) - A G_all'(s); increasing in s, evaluated at s = S_UP"""
    s_ = S_UP
    assert (s_ + A) ** 2 < N
    return Gall(s_ + A) - Gall(s_, lo=True) - A * Gall_d(s_, lo=True)


def H_lo(A):
    s_ = S_LIM_LO
    return Gall(s_ + A, lo=True) - Gall(s_) - A * Gall_d(s_)


def cost_up(al, A):
    return (1 + al) * (A * SIGH + H_up(A))


def amax(al, budget):
    """certified A_lo with cost_up(A_lo) < budget, and A_hi with cost_up(A_hi) >= budget"""
    if budget <= 0:
        return F(0), F(0)
    lo, hi = F(0), F(2)
    for _ in range(40):
        mid = (lo + hi) / 2
        if cost_up(al, mid) < budget:
            lo = mid
        else:
            hi = mid
    lo = round_dn(lo, 10 ** 6)
    hi = round_up(hi, 10 ** 6)
    assert cost_up(al, lo) < budget <= cost_up(al, hi)
    return lo, hi


print("\n== 4. budget for the non-seed part B = K((Phi'(S+h) - Phi'(S)) .) ==")
print(f"h-linear multiplier Phi''(S) h = (1/(2 sqrt t)) sum_k bhat_k J^k h:")
print(f"  bhat_0, bhat_2, bhat_4 at beta0: {dn(BH0[0], 9)}, {dn(BH0[1], 9)}, {dn(BH0[2], 9)}; signs alternate:",
      all((BH0[i] > 0) == (i % 2 == 0) for i in range(0, 8)))
print(f"  sum_k |bhat_k| (beta0, |k|<={2 * LB}) = {dn(BH0[0] + 2 * sum(abs(BH0[i]) for i in range(1, LB + 1)), 12)}"
      f" (sign pattern: = value at theta=pi/2 = 1);  SIG1 = l1/sqrt N <= {up(SIG1, 9)}")
print(f"  rank rule H*J^k*F <= (|k|+2) d r:  SIGH = sum_k (|k|+2)|bhat_k| / sqrt N <= {up(SIGH, 9)}"
      f"  (= rho_eff/(1+alpha) / sqrt N; rho_eff = (1+alpha) * {up(SIGH * SQN_HI, 5)})")
print("  => h-linear cost <= (1+alpha) A(h) SIGH;  h-higher (j>=2) cost <= (1+alpha) H(A(h)),")
print("     H(A) = G_all(s+A) - G_all(s) - A G_all'(s), G_all(y) = y(2N-y^2)/(N-y^2)^(3/2) (seed lines counted)")
for A in (F(55, 100), F(1), F(1994573, 1000000)):
    print(f"  H(A={dn(A, 6)}) in [{dn(H_lo(A), 5)}, {up(H_up(A), 5)}]")
print("Corollary 2.2 (needs C_S >= 1): ||L^m|| <= C_S (lam_S + C_S beta)^m; criterion lam_S + C_S beta"
      " < 1 - C_S (1 - kappa*)")
print("beta_max = (1 - lam_S)/C_S - (1 - kappa*_lo);  A_max = sup A(h) with cost(A) < beta_max [lo, hi]")
rows = []
for al in AFINE:
    for m0 in range(1, MMAX + 1):
        lamS, C = power_form(al, m0)
        for label in ("b1", "b1*"):
            kap = K_B1[0] if label == "b1" else KAP[al][0]
            bmax = (1 - lamS) / C - (1 - kap)
            alo, ahi = amax(al, bmax)
            rows.append((al, m0, label, lamS, C, bmax, alo, ahi))
print(f"[time {time.time() - T0:.1f}s]")
print("alpha m0 read  lam_S(<=)  C_S(<=)   beta_max(>=)  A_max in")
for (al, m0, label, lamS, C, bmax, alo, ahi) in rows:
    if al in ALPHAS and m0 in (1, 2, 4, 8):
        print(f"{str(al):>5} {m0:2d} {label:4s} {up(lamS, 5)}   {up(C, 4)}   {dn(bmax, 5):>9s}   "
              f"[{dn(alo, 4)}, {up(ahi, 4)}]")
print("\nbest certified A_max per alpha and reading (max over m0 <= 8):")
BEST = {}
for label in ("b1", "b1*"):
    for al in AFINE:
        cand = [r for r in rows if r[0] == al and r[2] == label]
        r = max(cand, key=lambda r: r[6])
        BEST[(label, al)] = r
        print(f"  {label:4s} alpha={str(al):>5}: A_max in [{dn(r[6], 4)}, {up(r[7], 4)}] (m0={r[1]}, "
              f"lam_S<={up(r[3], 5)}, C_S<={up(r[4], 4)}, beta_max>={dn(r[5], 5)})")
for label in ("b1", "b1*"):
    r = max((BEST[(label, al)] for al in AFINE), key=lambda r: r[6])
    print(f"overall best ({label}): alpha={r[0]}, m0={r[1]}: A_max in [{dn(r[6], 4)}, {up(r[7], 4)}]")

print("\n== 5. the blocking term: the h-linear allowance X with rho_eff A(h) < X ==")
print("X(A) = (beta_max - (1+alpha) H(A)) * sqrt N  (best m0);  rho_eff = (1+alpha) * sum_k(|k|+2)|bhat_k|")
print("(Round 182 units: cost = rho A/sqrt N.  182: X = 1.925 in pi_1 without Taylor; audit 182 with the")
print(" seed-only Taylor charged: 1.094 (dimension cost) / 0.264 (doubled).)")
RHO1 = SIGH * SQN_HI
for label in ("b1", "b1*"):
    print(f"-- reading {label}")
    for al in ALPHAS:
        r = BEST[(label, al)]
        x0 = r[5] * SQN_LO
        x55 = (r[5] - (1 + al) * H_up(F(55, 100))) * SQN_LO
        rho = (1 + al) * RHO1
        print(f"   alpha={str(al):>3} (m0={r[1]}): X <= {up(x0 + F(1, 10 ** 6), 4)} (h-higher not charged), "
              f"X(0.55) <= {up(x55 + F(1, 10 ** 6), 4)};  rho_eff <= {up(rho, 4)} (without seed lines {2 * (1 + al)});"
              f"  A(h) needed < {dn(r[6], 4)}")
AH = F(1994573, 1000000)
for label in ("b1", "b1*"):
    best_rate = None
    for al in AFINE:
        for m0 in range(1, MMAX + 1):
            lamS, C = power_form(al, m0)
            lam_full = lamS + C * cost_up(al, AH)
            if best_rate is None or lam_full < best_rate[0]:
                best_rate = (lam_full, al, m0, C)
    kap = K_B1[0] if label == "b1" else KAP[best_rate[1]][0]
    print(f"full multiplier at A(h) <= 1.994573 (conditional b2), reading {label}: best power rate "
          f"lam <= {up(best_rate[0], 4)} (alpha={best_rate[1]}, m0={best_rate[2]}, C={up(best_rate[3], 4)}); "
          f"needed < 1 - C(1-kappa*) = {dn(1 - best_rate[3] * (1 - kap), 4)}; P_5000 one-step: 1.066")
for A in (F(55, 100), F(1), AH):
    print(f"H(A={dn(A, 6)}) in [{dn(H_lo(A), 5)}, {up(H_up(A), 5)}];  h-linear (alpha=0) <= {up(A * SIGH, 5)}")

print("\n== 6. seed-only Taylor terms: net effect of moving them into L_S (exact) ==")
for al in (F(0), F(1, 2), F(1)):
    ll, lh, _ = growth(1, al, {1: F(1, 2), -1: F(1, 2)})
    print(f"alpha={al}: one-step G (full Phi'(S)) in [{dn(GL[(al, 1)], 6)}, {up(GU[(al, 1)], 6)}] vs linear "
          f"{lh}: rate change {up((GU[(al, 1)] - ll) * VARPI, 5)} "
          f"(Round 182 crude charge for the seed-only Taylor part: +0.10425 in dimension price)")
print("\n== 7. model heuristic (NOT a bound on A(h)): first Picard correction of h ==")
print("h1 = K(bulk Phi_t(S)) = 2 sqrt t sum_{k even != 0} b'_k K(J^k),  b'_k Fourier of (1+beta cos^2)^(1/2);")
print("dim K(J^k) = |k| (two-fibre rule, weights (-k,+k)); A(h1) = 2|sqrt t| sum_{k!=0} |b'_k| |k| at t = a, beta = beta0")


def binom_half(l):
    v = F(1)
    for i in range(l):
        v *= F(1, 2) - i
        v /= i + 1
    return v


BP = {i: sum(binom_half(l) * BETA0 ** l * F(comb(2 * l, l + i), 4 ** l) for l in range(i, 41)) for i in range(1, 21)}
tailp = BETA0 ** 41 * 82 * 83 / (1 - BETA0) ** 3
mom = sum(2 * abs(BP[i]) * 2 * i for i in BP)
sq_a_lo, sq_a_hi = sqrt_lo(a), sqrt_hi(a)
print(f"b'_2 = {dn(BP[1], 9)}, b'_4 = {dn(BP[2], 9)}; A(h1) in [{dn(2 * sq_a_lo * mom, 4)}, {up(2 * sq_a_hi * (mom + tailp), 4)}]"
      f"; sup bound of h1 <= same; compare threshold 0.6179 (A-price, reading b1*) and float sup|h| ~ 0.55")
print(f"\n[total time {time.time() - T0:.1f}s]")
print("ALL EXACT CHECKS OK")
