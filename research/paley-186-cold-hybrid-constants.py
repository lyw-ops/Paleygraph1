#!/usr/bin/env python3
"""Round 186 cold call `cold-prime-hybrid-price`: certified constants (exact rationals and outward arb balls).

Every printed bound is outward: lower bounds are printed rounded down, upper bounds rounded up.
Nothing here certifies a saved rounded input; these are statements about exact constants.

Sections
  0. Exact identities for the physical Paley operator K (checked with integers on small primes):
     sum of the sign row = -1, exactly one zero eigenvalue, hence S_0 = -2/sqrt(n), sum_x S_x^2 = 4(n-1).
  1. m''(gamma): lower bound for Phi_a'' on [-(s+gamma), s+gamma] at real t = a.
  2. Theorem N constants: c_N(gamma, n) lower bound for sup_{|g|<=gamma} P(B_g S)/P(S); thresholds n_0.
  3. Counting-route horizon arithmetic for q in {0.518, 0.5145, 0.535, 0.545}.
  4. Hybrid seminorm H_lambda: Taylor constant kappa_2(u)/2 against c_A(M0+u) = c(M0+u)/2.
  5. Counting rates of the seed multiplier and of B_h; the would-be Round 184 test-2 cost.

Replay: .venv/bin/python -B research/paley-186-cold-hybrid-constants.py   (a few seconds)
"""
from fractions import Fraction as F

from flint import arb, ctx

ctx.prec = 200

# ---------------------------------------------------------------- inherited exact parameters
a = F(2031, 128)
N = 4 * (a - F(1, 2 ** 17))              # 2|sqrt t| >= sqrt N on Q
t_abs_up = a + F(1, 2 ** 16)             # |t| <= a + sqrt2 2^-17 < a + 2^-16 on Q
S_UP = F(2828428539, 10 ** 9)            # s_p <= 2.828428539 for p >= 10^6 (Rounds 183/184)
M0 = F(4823, 1000)                       # Round 174 dimension budget of V_602
P0 = F(1272, 100000)                     # A_X(R_602) < 0.01272 (Round 184 D1)
B177 = F(1963, 1000)                     # ||V_602 - S||_inf < 1.963 (Round 177)
G_S_UP = F(2467879, 10 ** 6)             # g_S = sum_m G_m(L_S) <= 2.467879 (Round 184 Prop. C)
BUDGET_SEED = F(24310, 10 ** 5)          # Round 184 Prop. C seed-only non-seed budget beta' >= 0.24310
RHO0 = F(2175646, 10 ** 6)               # Round 184 uniform rho_0 <= 2.175646
SQRTN_LO = F(7966725769, 10 ** 9)        # sqrt N >= 7.966725769 (Round 183/184 printed)


def A(x):
    return arb(x.numerator) / arb(x.denominator) if isinstance(x, F) else arb(x)


def _frac(e):
    m, ex = e.man_exp()
    return F(int(m)) * (F(2) ** int(ex))


def _bounds(x):
    """exact rational [lower, upper] enclosing the arb x"""
    mid = _frac(x.mid())
    rad = _frac(x.rad())
    return mid - rad, mid + rad


def lo(x, d=6):
    """certified lower bound, printed rounded down to d decimals"""
    l, _ = _bounds(x)
    q = F((l * 10 ** d).__floor__(), 10 ** d)
    return f"{float(q):.{d}f}" if abs(q) < 10 ** 12 else f"{float(q):.6e}"


def up(x, d=6):
    """certified upper bound, printed rounded up to d decimals"""
    _, u = _bounds(x)
    q = F((u * 10 ** d).__ceil__(), 10 ** d)
    return f"{float(q):.{d}f}" if abs(q) < 10 ** 12 else f"{float(q):.6e}"


def is_prime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True


def prim_root(p):
    fac, m, d = [], p - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    g = 2
    while not all(pow(g, (p - 1) // f, p) != 1 for f in fac):
        g += 1
    return g


print("== 0. exact identities for the physical Paley operator K (integers) ==")
print("K = real symmetric circulant on Z/n with eigenvalues lambda_j = chi(1 - g^(2j)), j mod n (Round 96: K^2 = I - P_1).")
print("Claim: sum_j lambda_j = -1 and lambda_j = 0 iff j = 0; hence ||K e_0||^2 = (n-1)/n, sum_x S_x^2 = 4(n-1),")
print("       S_0 = 2 sqrt(n) (K e_0)_0 = (2/sqrt n) sum_j lambda_j / ... = -2/sqrt(n).  (proof in the report, Lemma 1)")
ok = True
for p in [p for p in range(5, 2000) if p % 4 == 1 and is_prime(p)]:
    n = (p - 1) // 2
    g = prim_root(p)
    sq = set((x * x) % p for x in range(1, p))
    lam = []
    for j in range(n):
        arg = (1 - pow(g, 2 * j, p)) % p
        lam.append(0 if arg == 0 else (1 if arg in sq else -1))
    zeros = [j for j in range(n) if lam[j] == 0]
    sym = all(lam[j] == lam[(n - j) % n] for j in range(n))
    if sum(lam) != -1 or zeros != [0] or not sym:
        ok = False
        print("  FAIL at p =", p, sum(lam), zeros, sym)
print(f"  all primes p = 1 mod 4, 5 <= p < 2000: sum lambda = -1, unique zero at j = 0, lambda_j = lambda_(n-j): {ok}")

print()
print("== 1. m''(gamma) := min_{|xi| <= s+gamma} Phi_a''(xi) = 4a/(4a + (s+gamma)^2)^(3/2)  (real t = a, outward) ==")
print("Phi_a''(xi) = 4a/(4a+xi^2)^(3/2) > 0 is even and decreasing in |xi|; s = s_p <= 2.828428539.")
GAMMAS = [("RMS(h) ~ 0.1749 [float input]", F(1749, 10000)), ("3/8", F(3, 8)),
          ("sup|h| ~ 0.61 [float input]", F(61, 100)), ("Round 177 sup bound 1.963", B177), ("1", F(1))]


def m2(gamma):
    y = A(S_UP) + A(gamma)
    return 4 * A(a) / (4 * A(a) + y * y) ** (A(F(3, 2)))


for name, gm in GAMMAS:
    print(f"  gamma = {float(gm):.4f} ({name}): m''(gamma) >= {lo(m2(gm))}")

print()
print("== 2. Theorem N: sup over real g with ||g||_inf <= gamma of ||K((Phi_a'(S+g)-Phi_a'(S)) S)||_inf,good / P(S) ==")
print("Lower bound (Lemma 2 + Theorem N; b0 = number of non-good coordinates, taken b0 <= 3):")
print("  c_N(gamma,n) = gamma m''(gamma) [ 8(n-1)(n-1-1/n)/(s^2 n^(3/2)) - 2 b0 sqrt(n-1)/n ] / s,")
print("  using P(S) <= A(S) = s_p <= s, sum|S| >= sum S^2/s, sum S^2 = 4(n-1), S_0^2 = 4/n.")
print("  asymptotically c_N ~ (8 gamma m''(gamma)/s^3) sqrt(n).")
B0 = 3


def cN(gamma, n):
    n = A(F(n))
    s = A(S_UP)
    main = 8 * (n - 1) * (n - 1 - 1 / n) / (s * s * n * n.sqrt())
    err = 2 * B0 * (n - 1).sqrt() / n
    return A(gamma) * m2(gamma) * (main - err) / s


def first_n_exceeding(gamma, target):
    lo_n, hi_n = 2, 2
    while not (cN(gamma, hi_n) > A(target)):
        hi_n *= 2
    while hi_n - lo_n > 1:
        mid = (lo_n + hi_n) // 2
        if cN(gamma, mid) > A(target):
            hi_n = mid
        else:
            lo_n = mid
    return hi_n


for name, gm in GAMMAS:
    slope = 8 * A(gm) * m2(gm) / A(S_UP) ** 3
    n1 = first_n_exceeding(gm, BUDGET_SEED)
    n2 = first_n_exceeding(gm, F(1))
    n3 = first_n_exceeding(gm, F(1066, 1000))
    print(f"  gamma = {float(gm):.4f}: slope 8 gamma m''/s^3 >= {lo(slope)};  c_N > 0.24310 (Prop. C seed budget) for all n >= {n1};"
          f"  c_N > 1 for n >= {n2};  c_N > 1.066 for n >= {n3}")
for n in (5004, 50024, 500016, 2000018, 10 ** 12):
    print(f"  n = {n}: c_N(0.61, n) >= {lo(cN(F(61, 100), n), 4)};  c_N(0.1749, n) >= {lo(cN(F(1749, 10000), n), 4)}")
print("  (c_N is increasing in n for n >= 10; monotone bisection is valid there. Checked below on a grid.)")
mono = all(cN(F(61, 100), k) < cN(F(61, 100), k + 1) for k in range(10, 400)) and \
    all(cN(F(1749, 10000), k) < cN(F(1749, 10000), k + 1) for k in range(10, 400))
print(f"  c_N(gamma, k) < c_N(gamma, k+1) for 10 <= k < 400, gamma in {{0.61, 0.1749}}: {mono}")
print("  ||K||_{inf->inf} = sum_x |kappa(x)| >= 2(n-1)/(s sqrt n):",
      " n = 10^6 gives >= " + lo(2 * A(F(10 ** 6 - 1)) / (A(S_UP) * A(F(10 ** 6)).sqrt()), 3))


def cLS(n):
    """Lemma 3: ||L_S||_{inf->inf,good} >= [8(n-1)(n-1-1/n)/(s^2 n^(3/2) sqrt(4a+s^2)) - 2 b0 sqrt(n-1)/n]"""
    n = A(F(n))
    s = A(S_UP)
    w = (4 * A(a) + s * s).sqrt()
    return 8 * (n - 1) * (n - 1 - 1 / n) / (s * s * n * n.sqrt() * w) - 2 * B0 * (n - 1).sqrt() / n


slopeLS = 8 / (A(S_UP) ** 2 * (4 * A(a) + A(S_UP) ** 2).sqrt())
print(f"  Lemma 3 (seed operator on sup): ||L_S||_(inf->inf,good) >= c_LS(n), slope 8/(s^2 sqrt(4a+s^2)) >= {lo(slopeLS)};"
      f"  c_LS(10^6) >= {lo(cLS(10 ** 6), 3)};  c_LS > 1 for n >= {next(k for k in range(10, 10 ** 4) if cLS(k) > 1)}")

print()
print("== 3. Counting route: a B-factor followed by b contracting steps costs sqrt(n) q^b in sup (Proposition 5) ==")
print("Horizon k_n = ceil((4/7) log2 n).  sqrt(n) q^b <= 1 needs b >= theta(q) log2 n, theta(q) = 1/(2 log2(1/q)).")
print("Fraction of the horizon in which a B-factor can be priced by counting with factor <= 1: 1 - theta(q)/(4/7).")
for q in (F(518, 1000), F(5145, 10000), F(535, 1000), F(545, 1000)):
    th = 1 / (2 * (1 / A(q)).log() / A(2).log())
    frac = 1 - th / (A(F(4, 7)))
    print(f"  q = {float(q):.4f}: theta(q) in [{lo(th)}, {up(th)}];  usable fraction of the horizon in [{lo(frac, 5)}, {up(frac, 5)}]")
print("  exact: 0.545^8 < 2^-7 :", F(545, 1000) ** 8 < F(1, 2 ** 7), " (so theta(0.545) < 4/7; Round 173)")
print("  exact: 0.545^8 > 2^-7 - 10^-4 :", F(545, 1000) ** 8 > F(1, 2 ** 7) - F(1, 10 ** 4), " (the margin in Round 173's cutoff is tiny)")

eps0 = F(907, 100) * F(1, 10 ** 209)   # limsup ||R_602||_{2,n} < 9.07e-209 (Round 180, ineffective)
q177 = F(545, 1000)
qS = None
print("  Norm-only confinement (Criterion D with Lambda_n = sqrt n): ||U_j||_inf <= sqrt(n) eps0/(1-q), eps0 = 9.07e-209.")
for eta in (F(1, 8),):
    bound = (F(3, 8) - eta) * (1 - q177) / eps0
    import math
    l10 = math.log10(bound.numerator) - math.log10(bound.denominator)
    print(f"  holds while sqrt(n) < (3/8 - {eta})(1 - 0.545)/eps0 = 10^{l10:.3f}, i.e. n < 10^{2 * l10:.3f};"
          " fails for all large n because liminf ||R_602||_{2,n} > 0 (Round 180)")

print()
print("== 4. Hybrid seminorm H_lambda = A_X infimal-convolved with lambda ||.||_{l2} (lambda >= 1): Taylor constant ==")
print("H(T(U)) <= c_A A(a)^2 + kappa_2 A(a) lambda||b|| + (kappa_2/(2 lambda)) (lambda||b||)^2 <= max(c_A, kappa_2/2) H(U)^2")
print("kappa_2(u) := sup |Phi_t''| on the radius-u polydisk about V_602 <= 4|t|/(N - 2(1.963+u)^2)^(3/2) (Round 177 geometry)")


def cM(Mv):
    x = A(Mv) ** 2 / A(N)
    return 2 / A(N).sqrt() * (1 + x / 2) * (1 - x) ** A(F(-5, 2))


for u in (F(747, 5000), F(3, 8)):
    Bv = B177 + u
    kap2 = 4 * A(t_abs_up) / (A(N) - 2 * A(Bv) ** 2) ** A(F(3, 2))
    cA = cM(M0 + u) / 2
    print(f"  u = {float(u):.4f}: kappa_2(u) <= {up(kap2)}, kappa_2/2 <= {up(kap2 / 2)};  c_A(M0+u) = c(M0+u)/2 >= {lo(cA)};"
          f"  kappa_2/2 < c_A: {bool(kap2 / 2 < cA)}")
cA0 = cM(M0) / 2
kap38 = 4 * A(t_abs_up) / (A(N) - 2 * A(B177 + F(3, 8)) ** 2) ** A(F(3, 2))
print(f"  all u in (0, 3/8]: kappa_2(u)/2 <= kappa_2(3/8)/2 <= {up(kap38 / 2)} < c_A(M0) = c(M0)/2 >= {lo(cA0)} <= c_A(M0+u): {bool(kap38 / 2 < cA0)}")
print("  => the H_lambda Taylor constant is c_A itself for every u <= 3/8; kappa*_H = kappa*_A in")
print("     [0.83790250, 0.83793100] (Round 184), so the Duhamel threshold Gamma < 1/(1-kappa*_A) >= 6.16912 is unchanged.")

print()
print("== 5. Counting rates and the Round 184 test-2 cost ==")
qS = A(S_UP) / (A(N) + A(S_UP) ** 2).sqrt()
print(f"  ||L_S||_(2->2) <= sup |Phi_t'(S)| <= s/sqrt(N + s^2) <= {up(qS)}   (|4t + x^2| >= Re 4t + x^2 >= N + x^2 for real x)")
k20 = 4 * A(t_abs_up) / (A(N) - 2 * A(B177) ** 2) ** A(F(3, 2))
print(f"  ||B_h||_(2->2) <= sup|Phi_t'(V_602) - Phi_t'(S)| <= kappa_2(0) * 1.963 <= {up(k20 * A(B177))}   (Round 177 sup bound)")


def Hmaj(Av):
    s = A(S_UP)
    Nn = A(N)

    def G(y):
        return y * (2 * Nn - y * y) / (Nn - y * y) ** A(F(3, 2))

    def Gp(y):
        return Nn * (2 * Nn + y * y) / (Nn - y * y) ** A(F(5, 2))
    return G(s + A(Av)) - G(s) - A(Av) * Gp(s)


for name, x in (("0.61 [float sup|h|]", F(61, 100)), ("0.7499", F(7499, 10000)), ("1.963 [Round 177]", B177)):
    cost = A(RHO0) * A(x) / A(SQRTN_LO) + Hmaj(x)
    print(f"  would-be sup-priced cost rho_0 x/sqrt N + H(x) at x = {name}: in [{lo(cost)}, {up(cost)}]"
          f"  (< 0.24310: {bool(cost < A(BUDGET_SEED))})")
print("  Theorem N: no sup-dominating price admits this cost as a bound in terms of x = ||h||_inf; see report §3.")

print()
print("== 6. Seed part of the hybrid and the per-simple floor ==")
# lower bound of the per-step path-summed seed ratio: Round 182 Lemma 3.1, r'_+ + r'_- = 4r - NZ >= 2r, so the
# J^{+-1} pair alone gives path-summed A-ratio >= 2 |s/(2 sqrt t)| |ghat_1|; children of valid simples are valid.
s_lo = A(F(8)).sqrt()                                         # s_p >= 2 sqrt 2
varpi_lo = s_lo / (2 * A(t_abs_up).sqrt())                    # |s/(2 sqrt t)| >= s/(2 sqrt|t|)
ghat1_lo = A(F(478072428819, 10 ** 12)) - A(F(216957, 10 ** 12)) * A(F(1, 2)) * (1 - A(F(1281, 10000))) ** A(F(-3, 2))
# |ghat_1(beta) - ghat_1(beta0)| <= delta (1/2)(1-b)^(-3/2) with delta <= 2.17e-7, b = beta0 + delta <= 0.1281 (Round 183 Lemma 1)
per_step = 2 * varpi_lo * ghat1_lo
print(f"  per-step path-summed seed A-ratio >= 2 varpi_lo |ghat_1|_lo >= {lo(per_step)};  counting rate q_S <= {up(qS)};"
      f"  q_S < per-step lower bound: {bool(qS < per_step)}")
print("  => G_m >= (per-step)^m > q_S^m for all m, so ||L_S^m||_H <= max(G_m, q_S^m) = G_m and g_H = g_S <= 2.467879.")
floor = F(191541, 100000)                                     # Round 184 Cor. A2 floor at beta0 (per-simple)
two_sqrt_t_up = 2 * A(t_abs_up).sqrt()
for Ah in (F(912537, 10 ** 6), F(1004901, 10 ** 6)):
    lin = A(floor) * A(Ah) / two_sqrt_t_up
    print(f"  model A(h) = {float(Ah):.6f}: per-simple h-linear cost >= floor*A(h)/(2|sqrt t|) >= {lo(lin)}"
          f" (budget 0.24310 leaves <= {up(A(BUDGET_SEED) - lin)} for the h-higher terms; their majorant H(A(h)) in"
          f" [{lo(Hmaj(Ah))}, {up(Hmaj(Ah))}])")
# What any per-simple one-step bookkeeping of B could allow in the seed-only Prop. C form (NOT an allowance:
# the floor is a lower bound for the h-linear ratio, Round 184 Cor. A2; it bounds the room from above).
ceil0 = A(BUDGET_SEED) * two_sqrt_t_up / A(floor)
print(f"  optimistic ceiling, h-higher terms free and h-linear ratio at the floor: A(h) < {up(ceil0)}"
      " (vs certified model A(h_<=3) >= 0.912537)")
lo_A, hi_A = F(0), F(2)
for _ in range(40):
    mid = (lo_A + hi_A) / 2
    if A(floor) * A(mid) / two_sqrt_t_up + Hmaj(mid) < A(BUDGET_SEED):
        lo_A = mid
    else:
        hi_A = mid
print(f"  with the h-higher majorant H kept: floor*A/(2|sqrt t|) + H(A) < 0.24310 iff A(h) < {float(hi_A):.4f} (bisection; float print)")
