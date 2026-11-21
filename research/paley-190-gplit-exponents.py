#!/usr/bin/env python3
"""Round 190 literature call (cand:gp-shifted-energy): exponent bookkeeping in exact Fractions.

Checks the arithmetic used in research/native-claude-ordinary-gp-shifted-energy-literature-190.md
for MPRRS (arXiv:1702.01003v5) Theorem 37 applied to a symmetric geometric progression I,
|I| = N ~ p^(1/2), |II| < 2|I|.  Pure arithmetic; no mathematical claim beyond the quoted statements.
"""
from fractions import Fraction as F

ok = True


def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok &= bool(cond)


half = F(1, 2)
# Theorem 37 output exponent in |A| and its distance from 5/2.
e37 = F(32, 13)
check("32/13 = 5/2 - 1/26", e37 == F(5, 2) - F(1, 26))
# In p at |A| = p^(1/2).
ep = e37 * half
check("p-exponent 16/13 = 5/4 - 1/52", ep == F(16, 13) == F(5, 4) - F(1, 52))
# Round 189 notation: X(1_I) = O(|I|^(5/2 - 2 delta)).
delta = (F(5, 2) - e37) / 2
check("delta = 1/52", delta == F(1, 52))
# Size hypothesis |A| <= p^(13/23) M^(10/23), M >= 1: suffices N <= p^(13/23); N = p^(1/2).
check("1/2 < 13/23", half < F(13, 23))
# Internal constraints of the proof at M = O(1):
# Lemma 33 use: M|A|^2|B| <= p^2 for |B| <= |A|^(20/13) (M=O(1)) -> |A|^(46/13) <= p^2.
check("46/13 * 1/2 <= 2", F(46, 13) * half <= 2)
# Lemma 32 use: |AA| <= p^(2/3) (|AA| ~ 2N ~ p^(1/2)).
check("1/2 < 2/3", half < F(2, 3))
# Theorem 34 exponents: D1^(6/13) D2^(2/13) with D1 = M^5, D2 = M^(3/2) gives M^(33/13).
check("M exponent 5*6/13 + 3/2*2/13 = 33/13", 5 * F(6, 13) + F(3, 2) * F(2, 13) == F(33, 13))
# Comparison with project thresholds (T_0 / X exponents in p; covariance = 1/2 + that).
t_743 = F(31, 24)   # beating 43/24
t_74 = F(5, 4)      # below 7/4
check("16/13 < 5/4 (Thm 37 is below the Round 189 sector value)", ep < t_74)
check("16/13 < 31/24", ep < t_743)
check("covariance translation 1/2 + 16/13 = 45/26 = 7/4 - 1/52", half + ep == F(45, 26) == F(7, 4) - F(1, 52))
check("1/2 + 5/4 = 7/4", half + t_74 == F(7, 4))
check("1/2 + 31/24 = 43/24", half + t_743 == F(43, 24))
# F_{r^2} control: |A| = r - 1 ~ p (characteristic r); hypothesis |A| <= p^(13/23) M^(10/23) fails.
check("F_{r^2}: exponent 1 > 13/23 (+10/23 * 0 since M ~ 1)", F(1) > F(13, 23))
# Rudnev-Shkredov-Stevens Thm 11 exponent 3 - 1/5 is weaker than 5/2.
check("14/5 > 5/2", F(14, 5) > F(5, 2))
# Pointwise route: sup_lambda r(lambda) <= N^(1-c) gives E <= N^(3-c), weaker than 5/2 unless c > 1/2.
check("3 - c < 5/2 iff c > 1/2 (c = 1/2 boundary)", F(3) - half == F(5, 2))
# MSS subgroup bound |G|^2 log|G| for |G| < p^(1/2) log p: exponent 2 in |G|.
print("ALL OK" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
