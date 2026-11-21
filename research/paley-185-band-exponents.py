#!/usr/bin/env python3
r"""Round 185, call ordinary-prime-near-critical-band-autocorrelation: exponent ledger.

Exact rational arithmetic (fractions.Fraction), standard library only.

Checks the exponent algebra of the report
research/native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md:

  * Theorem 1 (simple form): sup_{lambda != 1} C(lambda) << p^{11/8 - 1/856}, from
      band term      11/8 - eps/4                    (Stevens-de Zeeuw, line role gain)
      heavy term     4*eta(eps), eta from Round 184 Prop. 3 / Round 182 display
      light term     4/3                              (tau_0 = c p^{-1/6})
    balanced at eps = 1/214.
  * Theorem 2 (refined form): leftover pieces of the heavy levels priced by incidence,
      band 11/8 - eps/4, Phase 1  4/3 + 20 eps/3, Phase 2  4/3 + 8 eps/3 + 2 d/3,
      leftover 11/8 - 5 d/8;  eps = 1/166, any d in [1/415, ...] gives 11/8 - 1/664.
  * Corollary: sum_xi W^{3/2}, E(mu), one-match covariance.
  * Hypothesis check an << p^2 at tau_0 = p^{-1/6} (and tau_0 = p^{-1/7}).
  * Warren-Wheeler Theorems 3 and 4 at the scale relevant for max_xi W_xi.
Prints ALL OK at the end if every assertion holds.
"""
from fractions import Fraction as F

ok = True


def check(cond, msg):
    global ok
    print(("ok   " if cond else "FAIL ") + msg)
    ok = ok and bool(cond)


half = F(1, 2)
T = F(11, 8)           # Round 180 sup C exponent, the threshold eps = 3/8 of Round 184 Prop. 1


def eta(eps):
    """Round 184 Prop. 3: N(h_>=) << p^eta(eps) for the heavy part g >= p^-eps (0 <= eps <= 1/16)."""
    return max(F(1, 3) + F(5, 3) * eps, F(15, 44) + F(6, 11) * eps)


print("== Round 180 reproduction ==")
# C << G^{11/4} + G^2 + tau G^3 with G = p^{1/2}, tau = p^{-1/8}
check(F(11, 4) * half == T and F(3, 2) - F(1, 8) == T, "R180: G^{11/4} = tau G^3 = p^{11/8} at tau = p^{-1/8}")

print("== Hypothesis an << p^2 of Stevens-de Zeeuw Thm 4 ==")
for t0 in (F(1, 6), F(1, 7)):
    lev = half + t0                      # level-set size exponent G/tau_0
    check(3 * lev <= 2, f"tau_0 = p^-{t0}: level sizes p^{lev}, a*n <= p^{3*lev} <= p^2")
    check(F(3, 2) - t0 < T - F(1, 664), f"light term tau_0 G^3 = p^{F(3,2)-t0} < p^(11/8-1/664)")

print("== Theorem 1 (simple: heavy part by Round 184 Prop. 3) ==")
e1 = F(1, 214)
band = T - e1 / 4
heavy = 4 * eta(e1)
print(f"   eps = {e1}: band {band}, heavy 4*eta = {heavy}, branch values "
      f"{4*(F(1,3)+F(5,3)*e1)}, {4*(F(15,44)+F(6,11)*e1)}")
check(band == heavy, "band term = heavy term at eps = 1/214")
check(band == T - F(1, 856), "sup C exponent = 11/8 - 1/856")
check(eta(e1) == F(15, 44) + F(6, 11) * e1, "second branch of eta is active at eps = 1/214")
check(e1 < F(1, 192), "eps < 1/192 (heavy bound below 11/8)")
# optimality: the two sides are monotone in opposite directions
for e in (F(1, 300), F(1, 214), F(1, 150)):
    print(f"   eps = {e}: max(band, heavy) = {max(T - e/4, 4*eta(e))} = 11/8 - {T - max(T - e/4, 4*eta(e))}")

print("== Theorem 2 (refined: leftover pieces by incidence) ==")
e2 = F(1, 166)
d2 = F(1, 415)
terms = {
    'band (line role gain eps/4)': T - e2 / 4,
    'Phase 1 structured': F(4, 3) + F(20, 3) * e2,
    'Phase 2 structured': F(4, 3) + F(8, 3) * e2 + F(2, 3) * d2,
    'leftover (point role gain 5d/8)': T - F(5, 8) * d2,
    'light': F(4, 3),
}
for k, v in terms.items():
    print(f"   {k:34s} {v}  = 11/8 - {T - v}")
top = max(terms.values())
check(top == T - F(1, 664), "refined sup C exponent = 11/8 - 1/664")
check(terms['band (line role gain eps/4)'] == terms['Phase 1 structured'], "band = Phase 1 at eps = 1/166")
check(terms['leftover (point role gain 5d/8)'] == top, "leftover term equals the max at d = 1/415")
check(F(4, 3) + F(8, 3) * e2 + F(2, 3) * F(1, 2) > top, "(d cannot be taken huge; any d in [1/415, d_max] works)")
dmax = (top - F(4, 3) - F(8, 3) * e2) * F(3, 2)
print(f"   admissible d range: [1/415, {dmax}] (= [{float(F(1,415)):.5f}, {float(dmax):.5f}])")
check(dmax >= d2, "admissible d interval nonempty")
# leftover line role gain 3d/4 >= 5d/8 (point role), so point role is the binding one
check(F(3, 4) > F(5, 8), "line-role leftover gain 3d/4 exceeds point-role gain 5d/8")
# band point role gain 3eps/8 >= eps/4
check(F(3, 8) > F(1, 4), "band point-role gain 3eps/8 exceeds line-role gain eps/4")

print("== Corollary: sum W^{3/2}, E(mu), covariance ==")
for name, dl in (("simple", F(1, 856)), ("refined", F(1, 664))):
    supC = T - dl
    Xsq = 2 * F(34, 23)
    Em = max(Xsq, supC + 2)          # E^x(m) <= X^2 + sup C * M_1^2
    check(Xsq < supC + 2, f"{name}: X^2 = p^{Xsq} is below sup C*M_1^2 = p^{supC+2}")
    W32 = 1 + Em / 2
    check(W32 == F(43, 16) - dl / 2, f"{name}: sum W^(3/2) = p^(43/16 - {dl/2})")
    # Round 178: E(mu) << sum W^2/p + sum W^{3/2} + G log p * M_1^2
    Emu = max(Em - 1, W32, F(5, 2))
    check(Emu == W32, f"{name}: E(mu) = p^(43/16 - {dl/2})")
    cov = F(9, 8) + Emu / 4
    check(cov == F(115, 64) - dl / 8, f"{name}: one-match covariance p^(115/64 - {dl/8}) = p^{cov}")

print("== max_xi W_xi: Warren-Wheeler at the relevant scale ==")
# points U1 x U3 with |U1| = |U3| = N, transformations indexed by V1 x V3, |T| = N^2
N = F(1)   # exponents in units of log N
th3 = max(F(4, 5) + F(3, 5) + F(4, 5) * 2, F(6, 5) + F(7, 5) + F(1, 5) * 2, 2 * N)
check(th3 == 3, "WW Thm 3 with |A|=|B|=N, |T|=N^2 gives N^3: the trivial bound")
# Thm 4: |A|^{1/2}|B|^{7/10}|T|^{3/5}E(T)^{1/10}; E(T) >= |T|^2 = N^4
th4 = F(1, 2) + F(7, 10) + F(6, 5) + F(4, 10)
check(th4 == F(14, 5), "WW Thm 4 with the smallest possible E(T) = |T|^2 gives N^{14/5}")
check(th4 * half > T, "N^{14/5} at N = p^{1/2} is p^{7/5} > p^{11/8}: no gain at height 1")
# with all four roles at height a, mass sqrt p: a^4 (sqrt p / a)^{14/5} = p^{7/5} a^{6/5}
# below p^{11/8} only for a < p^{-1/48}; Round 184 heavy bound needs a >= p^{-1/192}
check((F(7, 5) - T) / F(6, 5) == F(1, 48), "Moebius route at height a: needs a < p^{-1/48}")
check(F(1, 48) > F(1, 192), "gap (p^{-1/48}, p^{-1/192}) not covered for max W even with ideal E(T)")

print("ALL OK" if ok else "SOME CHECK FAILED")
