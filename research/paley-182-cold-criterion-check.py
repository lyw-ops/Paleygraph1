"""Round 182 cold price: exact constants for the small-ball criterion (Prop. 1)
and its finite-horizon Duhamel/power form (Prop. 2).

Exact rational arithmetic (fractions.Fraction) throughout; square roots enter
only through squared comparisons, so every printed inequality is a certified
rational statement.  No floating point is used for any claim; floats appear
only in the human-readable echo of exact rationals.

Objects (see research/native-claude-cold-prime-signed-nonseed-price-182.md):
  N    = 4(2031/128 - 2^-17)
  c(M) = (2/sqrt N)(1+x/2)(1-x)^(-5/2),  x = M^2/N      (Round 174 coefficient)
  M0   = 4.823 (dimension bound of V_602), M = M0 + u on the price ball u.
  c(M) <= g  <=>  4(1+x/2)^2 <= g^2 N (1-x)^5     (both sides positive, x<1).
Prop. 1: some u in (0, 3/8) with p0 + k0 u + c(M0+u) u^2 < u.
  kappa*(p0) := sup_u [1 - p0/u - c(M0+u) u]   (exact threshold of the form).
Prop. 2: with Gamma = sum_{m<k} ||L^m||_P <= C/(1-lam) and sigma <= Gamma p0,
  some u with Gamma p0 + Gamma c(M0+u) u^2 < u;  lam_max(C) := sup over such lam.
Replay:  python3 -B research/paley-182-cold-criterion-check.py
"""
from fractions import Fraction as F

N = 4 * (F(2031, 128) - F(1, 2**17))
M0 = F(4823, 1000)
P0 = F(1272, 100000)


def c_le(M, g):
    """certified: c(M) <= g"""
    x = M * M / N
    assert 0 < x < 1
    return 4 * (1 + x / 2) ** 2 <= g * g * N * (1 - x) ** 5


def _bisect(M, digits):
    lo, hi = F(0), F(10)          # invariant: c(M) > lo,  c(M) <= hi
    assert c_le(M, hi) and not c_le(M, lo)
    q = F(1, 10**(digits + 2))
    while hi - lo > q:
        mid = (lo + hi) / 2
        if c_le(M, mid):
            hi = mid
        else:
            lo = mid
    return lo, hi


def c_upper(M, digits=12):
    """decimal g (10^-digits grid) with c(M) <= g (certified)"""
    lo, hi = _bisect(M, digits)
    g = F(-((-hi.numerator * 10**digits) // hi.denominator), 10**digits)
    assert c_le(M, g)
    return g


def c_lower(M, digits=12):
    """decimal g with c(M) > g (certified)"""
    lo, hi = _bisect(M, digits)
    g = F((lo.numerator * 10**digits) // lo.denominator, 10**digits)
    assert not c_le(M, g)
    return g


def sqrt_lower(a, digits=14):
    """rational s with s^2 <= a"""
    lo, hi = F(0), max(F(1), a)
    q = F(1, 10**digits)
    while hi - lo > q:
        mid = (lo + hi) / 2
        if mid * mid <= a:
            lo = mid
        else:
            hi = mid
    return lo


def fmt(x, d=7):
    return f"{float(x):.{d}f}"


# ---------------------------------------------------------------------------
print("== Audit statements (Round 181), exact ==")
print("c(4.936) <= 1.0043 :", c_le(F(4936, 1000), F(10043, 10000)))
print("c(4.936) <= 1.0042 :", c_le(F(4936, 1000), F(10042, 10000)))
print("c(5.198) <  1.22   :", c_le(F(5198, 1000), F(122, 100)))
print("c(5.198) <= 1.2182 :", c_le(F(5198, 1000), F(12182, 10000)))
print("c(4.873) <  1      :", c_le(F(4873, 1000), F(1)))
c4936 = F(10043, 10000)
for k0 in [F(7739, 10000), F(77394, 100000), F(77395, 100000)]:
    disc = (1 - k0) ** 2 - 4 * c4936 * P0
    print(f"  constant c=1.0043, k0={fmt(k0,5)}: discriminant>0 = {disc > 0}")


def lower_kappa(p0, grid):
    """certified lower bound on kappa*(p0): best over grid radii u of
    1 - p0/u - g(u) u with g(u) >= c(M0+u) certified."""
    best = None
    for u in grid:
        g = c_upper(M0 + u)
        k = 1 - p0 / u - g * u
        if best is None or k > best[0]:
            best = (k, u, g)
    return best


def upper_kappa(p0, umin, umax, target, tol=F(1, 10**7)):
    """certified upper bound on kappa*(p0) = sup_{0<u<=umax} 1 - p0/u - c(M0+u)u.
    c is increasing in M, so on [a,b] the bracket is <= 1 - p0/b - c_low(M0+a) a.
    For u<umin it is <= 1 - p0/umin.  Adaptive bisection of intervals whose
    bound exceeds target+tol (target = certified lower bound)."""
    best = 1 - p0 / umin
    stack = []
    a, r = umin, F(21, 20)
    while a < umax:
        b = min(a * r, umax)
        stack.append((a, b))
        a = b
    while stack:
        a, b = stack.pop()
        bound = 1 - p0 / b - c_lower(M0 + a, 9) * a
        if bound <= target + tol or b - a < F(1, 10**9):
            best = max(best, bound) if bound > target + tol else max(best, min(bound, target + tol))
            continue
        m = (a + b) / 2
        stack += [(a, m), (m, b)]
    return best


print("\n== Prop. 1 threshold kappa*(p0) (exact bracket) ==")
for p0, lo_u, hi_u in [(P0, F(1, 50), F(3, 8)), (F(1, 1000), F(1, 200), F(3, 8)),
                       (F(1, 10**6), F(1, 10**5), F(1, 100)),
                       (F(1, 10**12), F(1, 10**8), F(1, 10**5))]:
    # coarse grid search then refine around the best
    grid = [lo_u + (hi_u - lo_u) * i / 400 for i in range(1, 401)]
    k, u, g = lower_kappa(p0, grid)
    fine = [u + (hi_u - lo_u) * F(j, 400 * 50) for j in range(-50, 51) if u + (hi_u - lo_u) * F(j, 400 * 50) > 0]
    k, u, g = lower_kappa(p0, fine)
    # check invariance at the certifying radius: p0 + k u + g u^2 <= u
    assert p0 + k * u + g * u * u <= u
    kup = upper_kappa(p0, lo_u / 4, F(3, 8), k)
    print(f"p0={float(p0):.0e}: kappa* in [{fmt(k)}, {fmt(kup)}];"
          f" certifying radius u={fmt(u,5)}, c(M0+u)<={fmt(g,6)}")

# Is 0.77395 itself admissible with the self-consistent c?  (strict slack needed)
u = F(11255, 100000)
g = c_upper(M0 + u)
k0 = F(77395, 100000)
print("\nself-consistent check k0=0.77395, u=0.11255: p0+k0 u+c u^2 < u :",
      P0 + k0 * u + g * u * u < u, " c(M0+u)<=", fmt(g, 7))
k0 = F(77396, 100000)
print("self-consistent check k0=0.77396, u=0.11255: p0+k0 u+c u^2 < u :",
      P0 + k0 * u + g * u * u < u)

# ---------------------------------------------------------------------------
print("\n== Prop. 2 (finite-horizon Duhamel) with power bound ||L^m||_P <= C lam^m ==")
print("condition: exists u<=3/8 with (C/(1-lam))(p0 + c(M0+u)u^2) < u")


def lam_max(C, p0, grid):
    """certified lower bound on sup{lam: exists u in grid with C(p0+g u^2) < (1-lam)u}"""
    best = None
    for u in grid:
        g = c_upper(M0 + u)
        lam = 1 - C * (p0 + g * u * u) / u
        if best is None or lam > best[0]:
            best = (lam, u)
    return best


grid = [F(i, 2000) for i in range(20, 751)]
for C in [F(1), F(5, 4), F(3, 2), F(2), F(3)]:
    lam, u = lam_max(C, P0, grid)
    print(f"C={float(C):.2f}: need lam < {fmt(lam,5)} (u={fmt(u,4)})")

print("\n== Necessity of an n-uniform finite-horizon price resolvent (exact arithmetic) ==")
# With only the proved one-step bound kappa=1.066, Gamma_k <= sum_{m<k} 1.066^m.
# Show that Gamma_{k_n} -> infinity: k_n = ceil((4/7) log2 n); 1.066^{k_n} >= n^{(4/7)log2 1.066}.
# Certify (4/7) log2(1.066) > 1/20 via 1.066^(80/7) > 2  <=>  1.066^80 > 2^7.
print("1.066^80 > 2^7 (so 1.066^{k_n} >= n^{1/20}):", F(1066, 1000) ** 80 > 2 ** 7)

print("\n== Crude non-seed multiplier costs in dimension price (conditional inputs) ==")
# beta_h = 2 A(h)/sqrt(N) with A(h) <= M0 - 2 sqrt 2 (designated seed, s_p >= 2sqrt2)
s_lo = sqrt_lower(F(8))          # <= 2 sqrt 2
Ah = M0 - s_lo                    # >= M0 - 2sqrt2, an upper bound for A(h)
sqrtN_lo = sqrt_lower(N)
beta_h = 2 * Ah / sqrtN_lo
print("A(h) <=", fmt(Ah, 6), "; h-linear dimension cost 2A(h)/sqrt N <=", fmt(beta_h, 5))
# seed-linear dimension rate s_p/(2 sqrt N/2)... = 2 s_p/sqrt(N) * (1/2)*2 ; limit 2*2sqrt2/sqrtN /2
print("seed-linear plain dimension rate limit 2*sqrt(8)/sqrt(N) =",
      fmt(2 * sqrt_lower(F(8)) / sqrtN_lo, 5), "(upper, using sqrt N lower)")
print("seed-linear weighted (alpha=1) rate limit (3/4)*sqrt(8)/(sqrt(N)/2) =",
      fmt(F(3, 4) * 2 * (s_lo + F(1, 10**13)) / sqrtN_lo, 5))


def sqrt_upper(a, digits=14):
    s = sqrt_lower(a, digits)
    return s + F(1, 10**digits)


def G_bounds(y_lo, y_hi):
    """bounds for G(y) = sum_{l>=1} c_l (2l+2) y^(2l+1) / N^(l+1/2)
       = (y/sqrt N)[2(1-x)^(-1/2) + x(1-x)^(-3/2) - 2],  x = y^2/N  (increasing in y).
    returns (lower bound at y_lo, upper bound at y_hi)."""
    def val(y, up):
        x = y * y / N
        rN = sqrt_lower(N) if up else sqrt_upper(N)
        r1x = sqrt_lower(1 - x) if up else sqrt_upper(1 - x)
        inv = 1 / r1x
        return (y / rN) * (2 * inv + x * inv ** 3 - 2)
    return val(y_lo, False), val(y_hi, True)


s_hi = sqrt_upper(F(8))
g_s_lo, _ = G_bounds(s_lo, s_lo)
_, g_M_hi = G_bounds(M0, M0)
_, g_s_hi = G_bounds(s_hi, s_hi)
print("higher Taylor (l>=1) crude dimension costs, coefficient bound (2l+2) prod d:")
print("  seed-only part G(2sqrt2) <=", fmt(g_s_hi, 5), "(s_p -> 2sqrt2)")
print("  non-seed part G(M0)-G(s_p) <=", fmt(g_M_hi - g_s_lo, 5))
budget_dim = F(77414, 100000) - 2 * s_hi / sqrt_lower(N)
budget_pi1 = F(77414, 100000) - F(3, 4) * 2 * s_hi / sqrt_lower(N)
print("one-step non-seed budget (kappa* lower 0.77414 minus seed rate):",
      "dimension", fmt(budget_dim, 5), "; weighted alpha=1", fmt(budget_pi1, 5))
print("  => need rho*A(h) < budget*sqrt(N):  dimension", fmt(budget_dim * sqrt_lower(N), 4),
      "; weighted", fmt(budget_pi1 * sqrt_lower(N), 4), "(rho = per-simple ratio factor, crude 2 resp. 4)")
