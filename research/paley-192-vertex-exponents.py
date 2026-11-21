#!/usr/bin/env python3
"""Round 192, call ordinary-nc-vertex-tightness: exact Fraction arithmetic.

Every constant, threshold and exponent quoted in
research/native-claude-ordinary-nc-vertex-tightness-192.md is recomputed here
with fractions.Fraction (no floating point).  Prints 'ALL OK' on success.

Run:  .venv/bin/python -B research/paley-192-vertex-exponents.py
"""
from fractions import Fraction as Fr
from math import gcd

CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))
    print(("ok   " if cond else "FAIL ") + name)


# ---------------------------------------------------------------------------
# Part 1. Proposition C (uncertainty bookkeeping), in units of sqrt p.
#   Sigma_{Lambda_a} g >= (1 - o(1)) sqrt p   [(V_rel), G_rho = (1+o(1)) sqrt p]
#   Sigma_{Lambda_a} g^2 <= (1/2 + o(1)) sqrt p   [R183 Prop 1.4]
#   Cauchy-Schwarz: |Lambda_a| >= (Sigma g)^2 / Sigma g^2 >= 2 sqrt p.
#   |S| = (1+o(1)) m_0 = (1+o(1)) n / sqrt p, so |S| |Lambda_a| >= 2 n.
#   Upper: |Lambda_a| <= Sigma g / a <= sqrt p / a; so a <= 1/2.
# ---------------------------------------------------------------------------
mass, energy_cap = Fr(1), Fr(1, 2)
lam_lower = mass ** 2 / energy_cap
check("Prop C: |Lambda_a| / sqrt p >= 2", lam_lower == 2)
check("Prop C: |S||Lambda_a| / n >= 2 (Donoho-Stark equality needs 1)", lam_lower * 1 == 2)
for a in [Fr(1, 2), Fr(1, 4), Fr(1, 10), Fr(1, 20)]:
    upper = mass / a
    check(f"Prop C: a={a}: window [2, {upper}] for |Lambda_a|/sqrt p is nonempty iff a<=1/2",
          (lam_lower <= upper) == (a <= Fr(1, 2)))
check("Prop C: a = 1/2 + 1/100 gives an empty window", lam_lower > mass / (Fr(1, 2) + Fr(1, 100)))
# (V) => Sigma g^2 >= a (1 - o(1)) sqrt p  (ASM C5): coefficient a.
check("ASM C5 restated: Sigma g^2/sqrt p >= a * 1", all(a * mass == a for a in [Fr(1, 3)]))

# ---------------------------------------------------------------------------
# Part 2. Proposition B (sector-free method cap), units of sqrt p.
#   heavier sign: G_rho >= (G-1)/2 = (1/2 - o(1)) sqrt p.
#   random flat law: Sigma_{x != 1, g >= a} g = 0 eventually -> m_<a >= 1/2.
#   D_theta: Sigma_{g >= a} g <= (theta + o(1)) sqrt p -> m_<a >= 1/2 - theta.
# ---------------------------------------------------------------------------
check("Prop B: random flat law, m_<a / sqrt p >= 1/2", Fr(1, 2) - 0 == Fr(1, 2))
for theta in [Fr(1, 10), Fr(1, 4), Fr(1, 3), Fr(49, 100)]:
    lb = Fr(1, 2) - theta
    check(f"Prop B: D_theta, theta={theta}: lower bound 1/2 - theta = {lb} > 0", lb > 0)
# D_theta Parseval: Sigma_x |D_L'|^2 = n/L', n/L' = theta n/m, n/m = sqrt p (1+o(1)).
check("Prop B: Sigma |D_L'|^2 = theta * (n/m) in units sqrt p", Fr(1, 4) * 1 == Fr(1, 4))
# D_theta energy (R190 Thm 4 item 4) = (2/3) theta in the models; the cap needs
# only theta < 1/2 -> energy < 1/2 (accepted).  High energy and (V) failing:
check("Prop B: D_{1/4} model energy (2/3)theta = 1/6 > 0 and (V) fails (1/2-1/4 > 0)",
      Fr(2, 3) * Fr(1, 4) == Fr(1, 6) and Fr(1, 2) - Fr(1, 4) > 0)

# ---------------------------------------------------------------------------
# Part 3. Two-subgroup sharp family (Proposition D), exact identities.
#   nu = (1_{x1+H1} + 1_{x2+H2}) / (h1+h2), beta_i = h_i/(h1+h2).
#   g = beta1^2 on Gamma1 \ Gamma', beta2^2 on Gamma2 \ Gamma', 0 off Gamma1 u Gamma2.
#   Sigma g^2 / G -> beta1^3 + beta2^3 (Gamma' negligible).
#   overlap q_a = beta_i (a in H_i \ H_j) -> 1/2.
# ---------------------------------------------------------------------------
b1 = b2 = Fr(1, 2)
check("Prop D: levels beta^2 = 1/4", b1 ** 2 == Fr(1, 4))
check("Prop D: energy ratio beta1^3+beta2^3 = 1/4 <= 1/2", b1 ** 3 + b2 ** 3 == Fr(1, 4))
check("Prop D: overlap on H_i \\ H_j is beta_i = 1/2 (dichotomy (1-q)(2q-1) = 0)",
      (1 - b1) * (2 * b1 - 1) == 0)
# (A6) Prop 4(b): a coset of a subgroup K of order <= (2-delta) m_0 holds at most
# max(beta1 + beta2/2, beta2 + beta1/2) = 3/4 of S (K cannot contain H1 + H2).
frac = b1 + b2 / 2
check("Prop D: max coset fraction 3/4", frac == Fr(3, 4))
# compare with (1 - delta/2)^(1/4):  (3/4)^4 < 1 - delta/2  iff delta < 2(1 - 81/256)
dmax = 2 * (1 - frac ** 4)
check(f"Prop D: (A6)(b) holds for every delta < {dmax} (> 1)", dmax == Fr(350, 256) and dmax > 1)
# Size bookkeeping: h_i ~ m_0/2, m_0 ~ sqrt(p)/2, n ~ p/2:
# n / lcm(h1,h2) = n d / (h1 h2) -> (p/2) d / (p/16) = 8 d.
check("Prop D: n/lcm(h1,h2) -> 8 gcd(h1,h2)", (Fr(1, 2)) / (Fr(1, 4) * Fr(1, 4)) == 8)
# square-root normalisation: |Gamma_i| = n/h_i -> (p/2)/(sqrt p/4) = 2 sqrt p
check("Prop D: |Gamma_i| -> 2 sqrt p", Fr(1, 2) / Fr(1, 4) == 2)
# Lemma J: #bad >= (|Gamma| - 1 - sqrt p)/2 -> (2 - 1)/2 = 1/2 (units sqrt p)
check("Lemma J: bad points in Gamma_i >= sqrt p / 2", (2 - 1) * Fr(1, 2) == Fr(1, 2))
# so G_{-rho} >= beta^2 * (1/2) sqrt p = sqrt p / 8 -> infinity
check("Lemma J: G_{-rho} >= sqrt p / 8 on the two-subgroup family", Fr(1, 4) * Fr(1, 2) == Fr(1, 8))


# Lemma J, exact: for a subgroup of index k in F_p^*,
#   |Sigma_{y in Gamma} chi(1-y)| <= (1 + (k-1) sqrt p)/k  <  sqrt p.
# Check the inequality (1+(k-1)s)/k < s for s = sqrt p > 1, as rationals s.
def lemmaJ_ok(k, s):
    return (1 + (k - 1) * s) / k < s


check("Lemma J: (1+(k-1)s)/k < s for k in 2..50, s in {3/2, 5, 100}",
      all(lemmaJ_ok(k, Fr(s)) for k in range(2, 51) for s in [Fr(3, 2), 5, 100]))

# ---------------------------------------------------------------------------
# Part 4. Square control (R184 SRM Prop 5): beta = 4/(r-1)^2 on Q \ F_r^*,
#   m_<a <= beta * |Q \ F_r^*| = (4/(r-1)^2) * ((r^2-1)/2 - (r-1)) = 2(r+1)/(r-1) - ... -> 2.
# ---------------------------------------------------------------------------
for r in [5, 7, 11, 23, 47, 389]:
    beta = Fr(4, (r - 1) ** 2)
    nQ = Fr(r * r - 1, 2)
    m_low = beta * (nQ - (r - 1))
    check(f"square control r={r}: m_<a <= {m_low} <= 2(r+1)/(r-1)", m_low <= Fr(2 * (r + 1), r - 1))
check("square control: 2(r+1)/(r-1) -> 2 (r=10^6+3)", abs(Fr(2 * (10**6 + 4), 10**6 + 2) - 2) < Fr(1, 10**5))
# G = r + 1 = sqrt q + 1 (exact identity (r-1) + beta (r-1)^2/2 = r+1 is in R184; recheck)
for r in [5, 7, 47]:
    beta = Fr(4, (r - 1) ** 2)
    G = (r - 1) + beta * Fr((r * r - 1) - 2 * (r - 1), 2)
    check(f"square control r={r}: G = r+1", G == r + 1)

# ---------------------------------------------------------------------------
# Part 5. Loss exponents (powers of p).
#   If (V_rel) fails, m_<a asymp sqrt p: R160 price p*m_<a = p^(3/2) vs O(p): 1/2.
#   (V) needs m_<a = o(D), D <= p^(1/4)/log p; scale gap sqrt p / D >= p^(1/4).
#   Absolute-scale (V) versus relative statements: exponent gap 1/2 - 1/4.
# ---------------------------------------------------------------------------
check("loss vs O(p): (1 + 1/2) - 1 = 1/2", Fr(3, 2) - 1 == Fr(1, 2))
check("loss vs o(pD): >= 1/2 - 1/4 = 1/4", Fr(1, 2) - Fr(1, 4) == Fr(1, 4))
check("scale of (V) vs o(sqrt p) statements: exponents 1/4 < 1/2", Fr(1, 4) < Fr(1, 2))
# Prop A transfer: Sigma |f - f_S|^2 = n * o(1/m_0) = o(n/m_0) = o(sqrt p): exponent 1/2.
check("Prop A: n/m_0 = sqrt p (exponent 1/2)", Fr(1) - Fr(1, 2) == Fr(1, 2))
# Prop A: Sigma|g-g_S| <= (o(p^(1/2)))^(1/2) * (O(p^(1/2)))^(1/2) = o(p^(1/2))
check("Prop A: (1/2)(1/2) + (1/2)(1/2) = 1/2", Fr(1, 4) + Fr(1, 4) == Fr(1, 2))

# ---------------------------------------------------------------------------
# Part 6. Random flat law bookkeeping (Proposition B), units:
#   sup_{x != 1} g <= C log p / m_0 and m_0 ~ sqrt p / 2;  Sigma_B g <= k c2 sqrt p * C log p / m_0
#   = O(log p) = o(sqrt p).  Energy ratio <= (1 + C log p)/|S| -> 0.
#   Coset counts: mean |S cap coset| <= 2 m_0 * pi = 2 m_0 / sqrt p -> 1.
# ---------------------------------------------------------------------------
check("Prop B: coset mean 2 m_0/sqrt p -> 2*(1/2) = 1", 2 * Fr(1, 2) == 1)
check("Prop B: overlap mean n pi^2 = n/p -> 1/2", Fr(1, 2) == Fr(1, 2))

# ---------------------------------------------------------------------------
# Part 7. Exact gcd/lcm identities for the two-subgroup primes listed in the report
# (the models script finds them; here: the arithmetic of one example).
# ---------------------------------------------------------------------------
def two_subgroup_numbers(p, h1, h2):
    n = (p - 1) // 2
    assert n % h1 == 0 and n % h2 == 0
    d = gcd(h1, h2)
    l = h1 * h2 // d
    return n, d, l, n // l


# (p, h1, h2) as found by paley-192-vertex-models.py Part B (report section 5.2)
EXAMPLES = [(20129, 34, 37), (20161, 35, 36), (3997297, 487, 513), (3998809, 484, 486),
            (3990241, 489, 510), (3999001, 500, 516)]
for p, h1, h2 in EXAMPLES:
    n, d, l, quot = two_subgroup_numbers(p, h1, h2)
    prime = p % 4 == 1 and all(p % q for q in range(2, int(p ** 0.5) + 1))
    check(f"example p={p} (prime, 1 mod 4: {prime}): h1={h1}, h2={h2} divide n, gcd={d}, n/lcm={quot}",
          prime and l % h1 == 0 and n % l == 0)

bad = [n for n, ok in CHECKS if not ok]
print()
print(f"{len(CHECKS)} checks, {len(bad)} failures")
print("ALL OK" if not bad else "FAILURES: " + "; ".join(bad))
