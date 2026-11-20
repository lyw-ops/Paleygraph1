"""Exact/outward constants for the Kantorovich (small price-ball) form of the
price route at V_602.  Recursion (Rounds 174/177):
   u_{j+1} <= p0 + k0*u_j + c(M0+u)*u_j^2,  while u_j <= u,
with c(M) = (2/sqrt N)(1+x/2)(1-x)^(-5/2), x=M^2/N, N=4(2031/128-2^-17).
If (1-k0)^2 > 4 c p0 the smaller fixed point u_- = ((1-k0)-sqrt(disc))/(2c) is an
invariant bound for u_j from u_0=0.  We report the largest admissible k0 for each
trial ball radius u (needs u_- <= u), using decimal arithmetic at 60 digits with
directed rounding (c rounded up, thresholds rounded down)."""
from decimal import Decimal as D, getcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
getcontext().prec = 60
N = D(4) * (D(2031) / D(128) - D(1) / D(2**17))
M0 = D("4.823")

def c_of(M):
    getcontext().rounding = ROUND_CEILING
    x = M * M / N
    val = (D(2) / N.sqrt()) * (1 + x / 2) * (1 - x) ** D("-2.5")
    getcontext().rounding = ROUND_CEILING
    return val * (1 + D("1e-40"))  # outward pad

def kmax(p0, c):
    getcontext().rounding = ROUND_FLOOR
    return (1 - 2 * (c * p0).sqrt()) * (1 - D("1e-40"))

# sanity: Round 177 value at M=4.823+3/8 should be < 1.22
print("c(5.198) =", c_of(D("5.198")))
print("c(4.873) =", c_of(D("4.873")), "(Round 174: <1)")
for p0 in [D("0.01272"), D("0.001"), D("1e-6"), D("1e-12")]:
    best = None
    for k in range(1, 400):
        u = D(k) / D(1000)
        c = c_of(M0 + u)
        k0 = kmax(p0, c)
        um = (p0 / c).sqrt()   # u_- at the threshold
        if um <= u:
            best = (u, c, k0, um); break
    u, c, k0, um = best
    print(f"p0={p0}: ball u={u}, c<={float(c):.6f}, need k0 < {float(k0):.6f}, u_-~{float(um):.5f}")
# Compare: Round 180 polydisk-secant form at rho=3/8, eta->0, secant rate k0+2c(3/8)
c38 = c_of(D("5.198")); p0 = D("0.01272")
print("Round180 polydisk form at 3/8 with crude secant k0+2c*3/8: need k0 <",
      float(1 - p0 / D("0.375") - 2 * c38 * D("0.375")))
# optimised polydisk form: (1-k0)^2 > 8 c p0
print("optimised polydisk-secant form: need k0 <", float(1 - (8 * c_of(M0 + D("0.08")) * p0).sqrt()))
# inherited rates
print("inherited unsigned frozen rate 1.066; seed-linear Fourier-algebra rate bound s/(2|sqrt t|) * 2:",
      float(D(2) * D(2).sqrt() / (N / 4).sqrt()))
print("seed-linear L2 rate s/(2 sqrt 2 |sqrt t|):", float(D(2) * D(2).sqrt() / (D(2) * D(2).sqrt() * (N / 4).sqrt()) ))
