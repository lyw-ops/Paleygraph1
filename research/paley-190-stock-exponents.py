#!/usr/bin/env python3
"""Round 190 stocktake: exact exponent bookkeeping for the ordinary obligation map.

Exact Fractions only. Every input exponent is copied from an accepted record
(cited in the comments); nothing here proves an estimate. Lines marked
"bookkeeping" substitute an accepted bound into an accepted inequality; they are
not accepted statements. Exponents are of p, with G = sum g asymp sqrt p and
o(1) / log factors dropped (marked where the source carries them).

Run: python3 research/paley-190-stock-exponents.py
"""
from fractions import Fraction as F

half = F(1, 2)

# ---- normalisations -------------------------------------------------------
G = half                      # G = sum g = O(sqrt p) (R166 l.7; R183 Prop 1.2: G=(1+o(1))sqrt p on (NC))
W = half                      # W = sum_t w(t): G - Gamma_tot >= (1/2-o(1))sqrt p on (NC) (R188 l.79, l.241)
COV_TARGET = F(3, 2)          # covariance / full diagonal target (R166 l.46; R172 l.7)
FM_TARGET = F(1)              # first-moment target for the fixed moderate block (R162 l.30; R164 l.54)

def cs_first_moment(cov_exp):
    """Cauchy-Schwarz M_w <= W^(1/2) D^(1/2) (R180 l.54-56)."""
    return W / 2 + cov_exp / 2

def cov_equivalent(fm_exp):
    """Covariance exponent whose C-S image is fm_exp."""
    return 2 * (fm_exp - W / 2)

assert cs_first_moment(COV_TARGET) == FM_TARGET, "C-S converts p^(3/2) to p exactly"

# ---- accepted current exponents --------------------------------------------
one_match = F(43, 24)          # R187 acc. l.272 (with (log p)^(4/3)); unchanged R188 l.279, R189 l.290
theoremA_uncond = F(11, 6)     # R188 acc. l.275: Theorem A with X << p^(4/3+o(1))
full_diag = F(9, 4)            # R179 acc. l.248; R179 note l.5
D01_recorded = F(2399, 1280)   # R180 acc. l.253; R180 note l.60
DJ_recorded = F(15, 8)         # R180 note l.76 (per generic class)
Mw = F(4, 3)                   # R187 acc. l.272 Cor 4 (with (log p)^(32/3))
X = F(4, 3)                    # same
Rstar = half - F(1, 1280)      # R173 note l.40 / R180 note l.42
zero_katz = F(5, 2)            # implicit: R168 l.7 Katz r m/sqrt p, R167 l.44 prefactor p^3/m, ||l||_1<=2

assert D01_recorded == F(15, 8) - F(1, 1280)
assert D01_recorded == Rstar + F(11, 8)          # 4 R_* M_w with M_w = 11/8 (R180 l.56-60)
assert F(11, 8) == cs_first_moment(full_diag)    # R180's M_w comes from C-S on the diagonal

# Katz bookkeeping for zero match: prefactor p^3/m ~ p^2, |l|_1 <= 2, correlation <= 4m/sqrt p ~ p^(1/2)
assert F(2) + half == zero_katz

# ---- bookkeeping substitutions (NOT accepted statements) -------------------
D01_book = Rstar + Mw                            # 4 R_* M_w with R187's M_w
DJ_book = G + Mw                                 # 2 G M_w per generic class (R180 l.76)
zero_sub_upper = full_diag                       # zero = D - one - (>=2) + O(p^(3/2)), one >= -O(p^(3/2))
zero_sub_lower = one_match                       # zero >= -one - O(p^(3/2)) since D >= 0
assert D01_book == F(11, 6) - F(1, 1280) == F(7037, 3840)
assert DJ_book == F(11, 6)

# ---- gaps ---------------------------------------------------------------
rows = [
    # name, current, target, normalisation ('cov' or 'fm')
    ("one-match covariance", one_match, COV_TARGET, "cov"),
    ("zero match (Katz-implied, not recorded)", zero_katz, COV_TARGET, "cov"),
    ("zero match (bookkeeping subtraction)", zero_sub_upper, COV_TARGET, "cov"),
    ("full diagonal D", full_diag, COV_TARGET, "cov"),
    ("generic J sum D_gen (via D_gen <= D)", full_diag, COV_TARGET, "cov"),
    ("D_0 + D_1 recorded", D01_recorded, COV_TARGET, "cov"),
    ("D_0 + D_1 bookkeeping", D01_book, COV_TARGET, "cov"),
    ("first mass M_w (direct)", Mw, FM_TARGET, "fm"),
    ("slope-row moment X (one-match / M_w use)", X, FM_TARGET, "fm"),
]
print(f"{'piece':46s} {'current':>10s} {'target':>7s} {'gap':>10s} {'cov-equiv gap':>14s} {'fm-equiv gap':>13s}")
for name, cur, tgt, norm in rows:
    gap = cur - tgt
    if norm == "cov":
        cov_gap, fm_gap = gap, gap / 2
    else:
        cov_gap, fm_gap = cov_equivalent(cur) - COV_TARGET, gap
    print(f"{name:46s} {str(cur):>10s} {str(tgt):>7s} {str(gap):>10s} {str(cov_gap):>14s} {str(fm_gap):>13s}")

# route bottlenecks (max gap of the pieces each route needs), fm-equivalent
routes = {
    "split (>=2 paid, one, zero)": max(one_match, zero_sub_upper) - COV_TARGET,
    "full diagonal D": full_diag - COV_TARGET,
    "J split (D_0+D_1, D_gen)": max(D01_book, full_diag) - COV_TARGET,
    "first mass M_w": cov_equivalent(Mw) - COV_TARGET,
}
print("\nroute bottlenecks (covariance-equivalent gap, first-moment-equivalent gap):")
for k, v in sorted(routes.items(), key=lambda kv: kv[1]):
    print(f"  {k:32s} {str(v):>6s}  {str(v/2):>6s}")

# M_w direct beats M_w from the diagonal by
print("\nM_w from C-S on D:", cs_first_moment(full_diag), " M_w direct:", Mw,
      " difference:", cs_first_moment(full_diag) - Mw)

# Theorem A at the current X, against 43/24
print("Theorem A at X = p^(4/3):", COV_TARGET + (X - 1), " minus 43/24:", COV_TARGET + (X - 1) - one_match)

# Round 179 majorant floor: terms p G^2 and G^6/p of sum_h m(h)^3 (R179 l.43, l.51)
print("R179 majorant terms p*G^2, G^(9/2), G^6/p:", 1 + 2 * G, F(9, 2) * G, 6 * G - 1)
assert 1 + 2 * G == 2 and 6 * G - 1 == 2 and F(9, 2) * G == full_diag

# headroom thresholds that the accepted records state (for comparison only)
print("one-match below 43/24 iff X-epsilon <", F(7, 24), "(R188 l.275)")
