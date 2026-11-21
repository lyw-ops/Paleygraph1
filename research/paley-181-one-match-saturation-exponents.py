#!/usr/bin/env python3
"""Round 181: exact exponent bookkeeping (Fractions) for the abstract
fibre-statistics configuration that saturates every proved inequality used by
fibre-mass / sup / energy / rich-line arguments at the Round 180 value.
All quantities are powers of p (constants ignored); this checks the algebra of
the exponents only.  It is not a construction of an actual mu or level set.
"""
from fractions import Fraction as F

eps_star, eps1, kappa = F(1, 1280), F(1, 840), F(3, 418)
N = F(1, 2)            # |U| = p^(1/2) (top level, G ~ sqrt p)
M1 = F(1)              # M_1 ~ p
slopes = F(5, 8)       # |R|: slopes carrying mass (a multiplicative subgroup)
Ca = F(11, 8)          # C(a) for a in R
row = F(3, 8)          # m(r) = p^(3/8) on R  (row-mass model)
delta = F(11, 16)      # Delta value on rich (a,c)
per_slope = F(11, 16)  # number of c per slope with Delta = delta
t = F(19, 64)          # richness m'(a,c) on those (a,c)
R = slopes + per_slope  # number of rich generic h

checks = {
    'row model: M1 = |R| m(r)': (slopes + row, M1, '=='),
    'row model: m(r) <= G': (row, F(1, 2), '<='),
    'row model: C(a) = m^2 |R| for a in R': (2 * row + slopes, Ca, '=='),
    'C(a) <= p^(11/8) (Round 180)': (Ca, F(11, 8), '<='),
    'C(1) = sum m^2 <= p^(3/2-kappa) (Round 177)': (2 * row + slopes, F(3, 2) - kappa, '<='),
    'E^x(m) = sum_a C(a)^2 <= p^(27/8)': (slopes + 2 * Ca, F(27, 8), '<='),
    'sum_xi W^(3/2) <= p^(43/16)': (slopes + F(3, 2) * Ca, F(43, 16), '<='),
    'fibre mass: per_slope*delta = C(a)': (per_slope + delta, Ca, '=='),
    'total mass sum_h Delta = M1^2': (slopes + Ca, 2 * M1, '=='),
    'generic sup Delta <= p^(1-eps*-eps1) (Round 176)': (delta, 1 - eps_star - eps1, '<='),
    'E(mu) = R delta^2 <= p^(43/16) (Round 180)': (R + 2 * delta, F(43, 16), '<='),
    'transverse: per-c mass ~ (R/p) delta <= p^(3/2-kappa/2)': (R - 1 + delta, F(3, 2) - kappa / 2, '<='),
    "U side: rich lines R <= N^5/t^4 (Rudnev-Shkredov (22))": (R, 5 * N - 4 * t, '<='),
    "U side: per-slope richness mass per_slope*t <= N^2": (per_slope + t, 2 * N, '<='),
    "U side: generic m' <= p^(1/2-eps*) (Rounds 174/176)": (t, F(1, 2) - eps_star, '<='),
}
ok = True
for name, (lhs, rhs, op) in checks.items():
    good = (lhs == rhs) if op == '==' else (lhs <= rhs)
    ok &= good
    print(f"{'OK ' if good else 'BAD'} {name}: {lhs} {op} {rhs}")
value = R + delta + t
print('value exponent sum Delta m\' =', value, '(Round 180 RS-route value 147/64 =', F(147, 64), ')')
print('implied one-match covariance exponent value - 1/2 =', value - F(1, 2), '(115/64 =', F(115, 64), ')')
# conditional slope-dispersion criterion: generic <= 2 M1 G (K Lambda)^(1/2)
K = F(11, 8)
gen = M1 + N + K / 2
print('slope-dispersion criterion: generic exponent', gen, '-> covariance', gen + F(1, 2) - 1)
assert ok and value == F(147, 64)
