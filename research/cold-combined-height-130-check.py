"""Outward Arb bounds for the genuine height-601 cold predictor on Q."""
import json
from fractions import Fraction
from pathlib import Path
import runpy

from flint import acb, arb, arb_poly, ctx


source = Path(__file__).resolve().parent
old = runpy.run_path(str(source / "astra-predictor-76-check.py"))
ctx.prec = 192
fields = old["fields"]
N, KEEP = old["N"], old["KEEP"]
symmetric, tilt, eps = old["symmetric"], old["tilt"], old["eps"]
floor, half = arb(2031) / 128, arb(1) / 2**17
t = acb(arb(floor, half), arb(0, half))
rows, pars = fields["upper"](t)
rows = [[x.upper() for x in row] for row in rows]
assert all(x < 1 for x in pars)
assert all(x >= 0 for row in rows for x in row)
folded = [symmetric(row, KEEP) for row in rows]
norms = [sum(x * w for x, w in zip(row, tilt)) for row in rows]
seed = fields["kern"]["dim"]
a, b, c, d, z, w, v = pars


def tilted(poly, radius):
    return sum(poly[radius + i] * (2 if i else 1) * tilt[i]
               for i in range(radius + 1))


center_mass = seed + 2*a + 3*b + 4*c + (arb(23)/4)*d + 8*(z+w+v)
center_norm = seed*tilt[1] + a*(1+tilt[2]) + b*(1+3*tilt[1]/2+3*tilt[3]/2)
center_norm += c*tilted(fields["kern"]["F"], 4) + d*tilted(fields["kern"]["G"], 5)
center_norm += z*tilted(fields["old"]["R"], 2) + (v+w)*tilted(fields["field"], 4)
assert center_mass < arb(377)/100
tol = arb(1)/10**12
assert (8+arb(4)/10**30).sqrt() < seed.upper()
assert (arb(3)/2)*(34+11+16)/10**15 < tol
bn = arb(1)
for i in range(1, 16):
    bn *= (arb(3)/2-i)/i

# The rational trial prices of Round 82, with linear extension.
scaled = [0, 100000000, 252200485, 426274040, 611406156, 802387069, 996550741,
          1192477542, 1389393325, 1586868991, 1784663875, 1982641789,
          2180725131, 2378869432, 2577049092, 2775249319, 2973461537,
          3171680760, 3369904083, 3568129809, 3766356945, 3964584907,
          4162813351, 4361042071, 4559270933]
prices = [arb(k)/10**8 for k in scaled]
slope = prices[-1] - prices[-2]
assert all(k <= x <= 2*k for k, x in enumerate(prices)) and 1 < slope < 2


def price(k):
    k = abs(k)
    if k < len(prices):
        return prices[k]
    return prices[-1] + (k + 1 - len(prices))*slope


def residual(h):
    zero = sum(i*x for i, x in enumerate(h)) + (arb(14)/5)*eps + arb(1)/10**8
    return symmetric([zero]+h, N), zero + sum(x*w for x, w in zip(h, tilt[1:])) + eps


def retained(core, order):
    power = arb_poly([0]*KEEP + [1])
    result = arb_poly()
    for j in range(order, len(folded)):
        if j > order:
            step = power * core
            power = arb_poly([step[i+N] for i in range(2*KEEP+1)])
        term = folded[j] * power
        result += arb_poly([(j if order else 1)*term[i+2*KEEP] for i in range(N+1)])
    return [result[k]*(2 if k else 1) for k in range(N+1)]


def tail_ratio(norm):
    radius = center_norm + norm
    ratio = radius**2 / (4*(floor-half))
    assert 0 < ratio < 1
    return radius, ratio


def derivative_rate(h):
    core, norm = residual(h)
    mu = retained(core, 1)
    radius, ratio = tail_ratio(norm)
    tail = (4*abs(t).sqrt()*abs(bn)*ratio**15/radius
            * (15/(1-ratio) + ratio/(1-ratio)**2))
    leak = sum(j*norms[j]*norm**(j-1) for j in range(1, len(norms)))
    leak += tail - sum(x*w for x, w in zip(mu, tilt))
    assert leak >= 0
    moment = sum(x*price(i) for i, x in enumerate(mu))
    bounds = [moment/slope + sum(mu)]
    for k in range(1, N+len(prices)+1):
        image = (k-1)*moment + sum(
            x*(price(k+i)+price(k-i))/2 for i, x in enumerate(mu))
        bounds.append(image/price(k))
    return max(bound.upper() for bound in bounds) + 10*leak, leak


h = [arb(0)] * N
max_cap = max_leak = arb(0)
for step in range(1, 602):
    core, norm = residual(h)
    mu = retained(core, 0)
    _, ratio = tail_ratio(norm)
    leak = old["polynomial"](norms, norm) - sum(x*w for x, w in zip(mu, tilt))
    leak += 2*abs(t).sqrt()*abs(bn)*(ratio**15)/(1-ratio)
    assert 0 <= leak < eps, step
    h = [x.upper() for x in mu[1:]]
    h[0] += tol
    cap = center_mass + sum(k*x for k, x in enumerate(h, 1)) + 4*eps
    assert cap < arb(48)/10, step
    max_cap, max_leak = max(max_cap, cap.upper()), max(max_leak, leak.upper())
    if step >= 600:
        rate, derivative_leak = derivative_rate(h)
        bound = "1.046434" if step == 600 else "1.047425"
        assert rate + tol < arb(bound)
        assert arb(bound)*(1+arb(2)/5000) < arb("1.048")
        print(json.dumps({
            "kind": "physical_packet_operator", "height": step, "bits": ctx.prec,
            "physical_base_rate_ceiling": bound, "geometric_base_rate": str(rate),
            "omitted_tilted_derivative_mass": str(derivative_leak),
            "translated_eventual_rate_ceiling": "1.048",
            "prefix_cap_upper": str(max_cap), "prefix_leak_upper": str(max_leak),
        }, sort_keys=True))

rate = Fraction("1.048")
assert rate**467 * Fraction("0.5145")**33 < 1
assert rate**467 * Fraction("0.514")**33 < 1
print(json.dumps({"kind": "rational_geometric_split", "exponent": "0.467",
                  "packet_rate": "1.048", "counting_rates": ["0.514", "0.5145"],
                  "comparison": "rate**467 * counting_rate**33 < 1"}, sort_keys=True))
