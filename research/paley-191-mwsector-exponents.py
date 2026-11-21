#!/usr/bin/env python3
"""Round 191, call ordinary-first-mass-sector-obstruction: exact exponent arithmetic.

Every exponent and every rational constant quoted in
research/native-claude-ordinary-first-mass-sector-obstruction-191.md is checked here
with fractions.Fraction.  Standard library only.  Prints ALL OK.

Replay:  .venv/bin/python -B research/paley-191-mwsector-exponents.py
"""
from fractions import Fraction as F

ok = True


def check(name, cond):
    global ok
    print(("OK   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


half = F(1, 2)
E_gp = F(32, 13)          # MPRRS Theorem 37 exponent in |I|
M_wall = E_gp * half      # in p, at |I| ~ sqrt p

# 1. The wall in p-units and its relation to 5/2, 5/4.
check("32/13 = 5/2 - 1/26", E_gp == F(5, 2) - F(1, 26))
check("|I|^(32/13) = p^(16/13) at |I| ~ p^(1/2)", M_wall == F(16, 13))
check("16/13 = 5/4 - 1/52", M_wall == F(5, 4) - F(1, 52))

# 2. A bound M_w <= p^(16/13 - delta) translates to E <= |I|^(32/13 - 2 delta).
for d in (F(1, 100), F(1, 52), F(1, 13), F(3, 13)):
    check(f"(16/13 - {d}) * 2 = 32/13 - 2*{d}", (M_wall - d) * 2 == E_gp - 2 * d)

# 3. Covariance-equivalent threshold (Round 190 GPLIT/audit convention 1/2 + e).
check("1/2 + 16/13 = 45/26", half + M_wall == F(45, 26))
check("45/26 = 7/4 - 1/52", F(45, 26) == F(7, 4) - F(1, 52))

# 4. Gaps: target M_w = O(p) (exponent 1), wall 16/13, current bound 4/3 (Round 187).
check("wall - target = 3/13 (p-units)", M_wall - 1 == F(3, 13))
check("in |I|-units: 32/13 - 2 = 6/13", E_gp - 2 == F(6, 13))
check("current 4/3 - wall 16/13 = 4/39 > 0", F(4, 3) - M_wall == F(4, 39) and F(4, 39) > 0)
check("current 4/3 - target 1 = 1/3", F(4, 3) - 1 == F(1, 3))
check("unobstructed window (16/13, 4/3) has length 4/39 out of 1/3 = 4/13",
      (F(4, 3) - M_wall) / (F(4, 3) - 1) == F(4, 13))

# 5. Criterion 5.2 analogue: (GP-Sub_kappa) weakens the restriction bound by p^(-5 kappa).
for k in (F(1, 100), F(1, 52)):
    check(f"5*kappa removes the family for delta < 5 kappa: 16/13 - 5*{k} = {M_wall - 5 * k}",
          M_wall - 5 * k < M_wall)

# 6. Fejer second-moment identity used in Lemma 3: sum_{|t|<L}(1-|t|/L) t^2 = (L^3 - L)/6.
for L in range(1, 60):
    s = sum((1 - F(abs(t), L)) * t * t for t in range(-L + 1, L))
    if s != F(L ** 3 - L, 6):
        check(f"Fejer moment L={L}", False)
check("sum_{|t|<L} (1-|t|/L) t^2 = (L^3-L)/6 for 1 <= L < 60", True)
# then (2/L) * 4 * (L^3-L)/6 = (4/3)(L^2-1) and (2/L) * pi^2 * (L^3-L)/6 = (pi^2/3)(L^2-1)
for L in range(1, 60):
    assert F(2, L) * 4 * F(L ** 3 - L, 6) == F(4, 3) * (L * L - 1)
    assert F(2, L) * F(L ** 3 - L, 6) == F(1, 3) * (L * L - 1)
check("(2/L)*4*(L^3-L)/6 = (4/3)(L^2-1); (2/L)*(L^3-L)/6 = (L^2-1)/3", True)
check("(4/3)(L^2-1) >= L^2 for L >= 2",
      all(F(4, 3) * (L * L - 1) >= L * L for L in range(2, 1000)))

# 7. Window bookkeeping for the restriction (Theorem 2 / 4'): 4K' <= n/(2L) with K' = floor(n/(8L)).
for n in (500, 5004, 50002, 123456):
    for L in (2, 3, 7, 22, 50):
        K = n // (8 * L)
        assert 4 * K <= F(n, 2 * L)
check("K' = floor(n/(8L)) gives 4K' <= n/(2L)", True)

# 8. Lengths of I' (leading order): |I'| = 2K'+1 ~ n/(4L).
#    D_theta^eta: L' = (1-eta) m/theta, n/m ~ sqrt p  =>  |I'| ~ theta sqrt p / (4(1-eta)).
th, eta = F(1, 4), F(1, 2)
check("|I'|/sqrt p -> theta/(4(1-eta)) = 1/8 at theta=1/4, eta=1/2", th / (4 * (1 - eta)) == F(1, 8))
#    max overlap theta(1-eta) < 1/2 for theta < 1/2, eta in (0,1)
check("theta(1-eta) < 1/2 at theta=1/4, eta=1/2 (=1/8)", th * (1 - eta) == F(1, 8))
#    energy ratio of the S1 part (continuous Fejer model): (2/3) theta (1-eta)^... reported only as evidence

# 9. Plateau constants of the eta-mixture: a = (1-eta)^2 (4/pi^2), b = (1-eta)^2.
#    With eta = 1/2: b = 1/4, b(1-b) = 3/16; a = 1/pi^2 (not rational; checked in floating below).
b = (1 - eta) ** 2
check("b = (1-eta)^2 = 1/4, b(1-b) = 3/16", b == F(1, 4) and b * (1 - b) == F(3, 16))

import math
a = float((1 - eta) ** 2) * 4 / math.pi ** 2
w0 = min(a * (1 - a), float(b * (1 - b)))
c_eta = a ** 4 * w0
check(f"eta=1/2: a = 1/pi^2 = {a:.6f}, w0 = a(1-a) = (pi^2-1)/pi^4 = {w0:.6f}",
      abs(a - 1 / math.pi ** 2) < 1e-15 and abs(w0 - (math.pi ** 2 - 1) / math.pi ** 4) < 1e-15)
check(f"c(1/2) = a^4 w0 = (pi^2-1)/pi^12 = {c_eta:.4e}", abs(c_eta - (math.pi ** 2 - 1) / math.pi ** 12) < 1e-18)
# Round 189 constant for comparison: (4/pi^2)^5
check(f"Round 189 T_0 constant (4/pi^2)^5 = {(4 / math.pi ** 2) ** 5:.4e}", True)

# 10. Masked -> unmasked (Round 189 audit 2.4): E <= 16 (X + |I|^2).  With X <= C p^(16/13-delta)
#     and |I| >= c sqrt p: E <= 16 C c^(-(32/13 - 2 delta)) |I|^(32/13 - 2 delta) + 16|I|^2,
#     and 2 < 32/13 - 2 delta iff delta < 3/13.
check("2 < 32/13 - 2 delta  iff  delta < 3/13", F(32, 13) - 2 * F(3, 13) == 2)

print("ALL OK" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
