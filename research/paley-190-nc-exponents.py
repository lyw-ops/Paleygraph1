#!/usr/bin/env python3
"""Round 190, call ordinary-nc-excludes-sector-laws: exact exponent arithmetic (Fractions).

Every exponent quoted in research/native-claude-ordinary-nc-excludes-sector-laws-190.md is
checked here. Exponents are powers of p. Prints ALL OK on success.
"""
from fractions import Fraction as F

ok = True


def check(name, cond):
    global ok
    print(("OK   " if cond else "FAIL ") + name)
    ok = ok and cond


# Thresholds (Round 188 Theorem A / Corollary B1, Round 189 Proposition 5)
cov_T0 = lambda e: F(1, 2) + e                 # covariance exponent 1/2 + e(T_0)
check("T_0 < p^(31/24) <=> covariance < 43/24", cov_T0(F(31, 24)) == F(43, 24))
check("T_0 < p^(5/4)  <=> covariance < 7/4", cov_T0(F(5, 4)) == F(7, 4))
check("T_0 = O(p)     <=> covariance 3/2 (target)", cov_T0(F(1)) == F(3, 2))


def cov_gamma(g):                                # Round 188 Cor. B1: min(1+2g, g+4/3, 43/24)
    return min(1 + 2 * g, g + F(4, 3), F(43, 24))


check("Gamma_tot = p^(11/24): covariance exactly 43/24 (threshold)", cov_gamma(F(11, 24)) == F(43, 24))
check("Gamma_tot = p^(5/12): covariance exactly 7/4 (threshold)", cov_gamma(F(5, 12)) == F(7, 4))
check("below 7/4 iff gamma < 5/12 (sampled)",
      all((cov_gamma(F(5, 12) - F(1, k)) < F(7, 4)) and cov_gamma(F(5, 12) + F(1, k)) >= F(7, 4) for k in range(13, 400)))
check("below 43/24 iff gamma < 11/24 (sampled)",
      all((cov_gamma(F(11, 24) - F(1, k)) < F(43, 24)) and cov_gamma(F(11, 24) + F(1, k)) >= F(43, 24) for k in range(25, 400)))
check("Gamma_tot asymp sqrt p (the (NC) cap 1/2 + o(1), Round 183 Prop. 1.4) gives 43/24 only",
      cov_gamma(F(1, 2)) == F(43, 24))
check("target needs gamma <= 1/4", cov_gamma(F(1, 4)) == F(3, 2))

# Heavy-triangle reduction (Round 189 Prop. 5): light part p^{-theta} X with X = p^{4/3}
theta = F(1, 24)
check("p^(-1/24) * p^(4/3) = p^(31/24)", -theta + F(4, 3) == F(31, 24))

# Sector reduction (Proposition 3 of the report): T_0^(-rho) <= G_{-rho} * c, c <= (sum g^2)^2
c_exp = 2 * F(1, 2)                              # (sum g^2)^2 <= (sqrt p / 2)^2 on (NC)
check("T_0^(-rho) <= (1+o(1)) c = O(p^1): exponent 1 < 5/4 < 31/24", c_exp == 1 and c_exp < F(5, 4) < F(31, 24))

# Diluted-interval family D_theta: |I| ~ theta sqrt p / 2, Gamma_tot ~ (2 theta/3) sqrt p
check("D_theta: |I|^(5/2) = p^(5/4) at |I| asymp sqrt p", F(5, 2) * F(1, 2) == F(5, 4))
check("D_theta: Gamma_tot exponent 1/2 > 11/24 > 5/12", F(1, 2) > F(11, 24) > F(5, 12))

# Quantitative GP-Sub with p^kappa points in the bad sector: tau <= p^(-kappa)
# obstruction T_0 >= tau^5 X(1_I), X(1_I) <= |I|^(5/2) = p^(5/4) (MPRRS): cap removed for delta < 5 kappa
for kappa in (F(1, 100), F(1, 24), F(1, 10)):
    lifted = F(5, 4) - 5 * kappa
    check(f"kappa={kappa}: obstruction lower bound p^(5/4-5kappa) = p^{lifted} < p^(5/4)", lifted < F(5, 4))
# heavy level threshold p^(-1/24-delta): at most G_{-rho} p^(1/24+delta) heavy points in T_{-rho}
check("heavy points in T_{-rho}: (1+o(1)) p^(1/24+delta), exponent 1/24 < 1/2", F(1, 24) < F(1, 2))

# Clique bounds: |I| <= sqrt p (elementary), <= (sqrt(2p-1)+1)/2 ~ p^(1/2)/sqrt 2 (Hanson-Petridis)
check("clique exponent 1/2 equals the family exponent 1/2 (no power gap)", F(1, 2) == F(1, 2))

print("ALL OK" if ok else "SOME CHECK FAILED")
