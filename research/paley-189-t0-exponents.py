#!/usr/bin/env python3
"""Round 189 (ordinary-prime-intercept-fibre-t0): exact exponent arithmetic
(Fractions) for every exponent statement in the report. Exponents are powers
of p; N = |S| = p^(1/2) for level sets of size ~ sqrt p.

Run: .venv/bin/python -B research/paley-189-t0-exponents.py   (prints ALL OK)
"""
from fractions import Fraction as F

ok = True


def check(label, value, expected):
    global ok
    good = value == expected
    ok &= good
    print(f"{'ok  ' if good else 'FAIL'} {label}: {value}" + ("" if good else f" (expected {expected})"))


half = F(1, 2)
eX = F(4, 3)          # Round 187: X <= p^(4/3+o(1))
target_75 = F(7, 4)
target_4324 = F(43, 24)


def cov_from_T0(eT):  # Theorem A uniform branch, W <= G = p^(1/2)
    return max(F(3, 2), half + eT)


# 0. Theorem A thresholds
check("T_0 threshold for < 7/4", target_75 - half, F(5, 4))
check("T_0 threshold for < 43/24", target_4324 - half, F(31, 24))
check("averaged T threshold for < 7/4 (w <= 1/4, no p factor)", target_75, F(7, 4))
check("today: cov from T_0 <= X = p^(4/3)", cov_from_T0(eX), F(11, 6))

# 1. half-structured Cauchy-Schwarz: T_0 - c <= (sum_{k!=1} A^2)^(1/2) X^(1/2)
def cs_split(eA, eX_=eX):
    return (eA + eX_) / 2

check("CS split with structured side at MPRRS N^(5/2)=p^(5/4)", cs_split(F(5, 4)), F(31, 24))
check("  -> covariance", cov_from_T0(cs_split(F(5, 4))), F(43, 24))
check("CS split: e_A needed for < 7/4 (e_X = 4/3)", 2 * F(5, 4) - eX, F(7, 6))
check("CS split: e_A needed for < 43/24 (e_X = 4/3)", 2 * F(31, 24) - eX, F(5, 4))
check("CS split with both sides at 4/3 (no coupling gain)", cs_split(eX), eX)

# 2. auditor's decoupled pricings (Round 188 audit 5.2), re-derived
check("(T3 G E^x)^(1/2), T3 = p, E^x = p^(4/3)", (1 + half + eX) / 2, F(17, 12))
check("  T3 needed for < 5/4", 2 * F(5, 4) - half - eX, F(2, 3))
d_for = lambda eT: 2 * eT - half - eX
check("(Gam2 D0 X)^(1/2): d for < 7/4", d_for(F(5, 4)), F(2, 3))
check("(Gam2 D0 X)^(1/2): d for < 43/24", d_for(F(31, 24)), F(3, 4))
check("light-triangle split tau X + (G/tau) D0, optimised = (G X D0)^(1/2): same thresholds", d_for(F(31, 24)), F(3, 4))

# 3. pointwise Delta(l,0) as a sum of r over <= N pencil slopes
check("pointwise CS (N X)^(1/2), X = p^(4/3)", (half + eX) / 2, F(11, 12))
check("pointwise CS (N X)^(1/2), X at floor p", (half + 1) / 2, F(3, 4))
# rich-slope counts t(h) <= N^a / h^b; Delta <= N H + N^a / H^(b-1); in N-exponents
def pencil(a, b):
    # minimise max(1 + eta, a - (b-1) eta): eta = (a-1)/b
    eta = F(a - 1, b)
    return 1 + eta
dSdZ = pencil(4, 4) * half   # Lemma M'-type count t(h) << N^4/h^4 (K ~ 1)
dST = pencil(3, 3) * half    # Szemeredi-Trotter strength t(h) << N^3/h^3
check("pencil rich-slope pricing of D0 with SdZ/Lemma M' counts (p-exponent)", dSdZ, F(7, 8))
check("pencil rich-slope pricing of D0 with ST-strength counts (p-exponent)", dST, F(5, 6))
check("  both exceed 3/4", (dSdZ > F(3, 4)) and (dST > F(3, 4)), True)

# 4. anharmonic cross sum I_cross = sum c(k) c(1-k): N^2 points, N^2 lines (not a pencil)
sdz_cross = (F(3, 4) + F(1, 2) + F(3, 4) * 2) * half   # a^(3/4) b^(1/2) n^(3/4), a=b=N, n=N^2
st_cross = (F(2, 3) * (2 + 2)) * half                   # (mn)^(2/3), m = n = N^2
check("SdZ bound for I_cross (p-exponent)", sdz_cross, F(11, 8))
check("ST-strength bound for I_cross (p-exponent)", st_cross, F(4, 3))
check("(X I_cross)^(1/2) with SdZ", (eX + sdz_cross) / 2, F(65, 48))
check("  I_cross needed in (X I_cross)^(1/2) for < 43/24", 2 * F(31, 24) - eX, F(5, 4))
check("SdZ hypotheses at a=b=N, n=N^2: a b^2 <= n^3 (N^3 <= N^6)", F(3) <= F(6), True)
check("  a n << p^2: a n = N^3 = p^(3/2) < p^2", F(3, 2) < 2, True)

# 5. Plancherel/Gamma form: T_0 <= (Gam_tot E_0)^(1/2), E_0 = sum Delta(l,0)^2 >= c^2 ~ p^2
check("(Gam_tot E_0)^(1/2) floor at Gam ~ sqrt p, E_0 ~ p^2", (half + 2) / 2, F(5, 4))

# 6. transfer: interval / GP laws
N = half
check("GP energy exponent at MPRRS Lemma 33 (|AA|^(3/2)|B|^(3/2)/|A|^(1/2), all ~N)", F(3, 2) * N + F(3, 2) * N - F(1, 2) * N, F(5, 4))
check("Lemma 33 hypothesis |A||AA||B| <= p^2: 3N = 3/2 <= 2", 3 * N <= 2, True)
check("Lemma 33 hypothesis max(|AA|,|B|) <= (|A||AA||B|)^(1/2): N <= 3N/2", N <= 3 * N / 2, True)
check("GP laws pose no obstruction at 31/24 (5/4 < 31/24)", F(5, 4) < F(31, 24), True)
check("7/4 via T_0 needs GP energy below N^(5/2): exponent in N", F(5, 4) / N, F(5, 2))

# 7. F_{r^2} control: subfield subgroup H = F_r^* of size r = q^(1/2): X ~ |H|^3
check("F_{r^2} control: T_0 = X ~ q^(3/2), Theorem A cov exponent", cov_from_T0(F(3, 2)), F(2))

print("ALL OK" if ok else "SOME FAILED")
