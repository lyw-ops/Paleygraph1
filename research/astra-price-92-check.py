"""Outward checks for affine signed quantiles and two independent dilations."""
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import runpy
import sys

from flint import acb, arb, ctx

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
old = runpy.run_path(str(here / "astra-matched-88-check.py"))
from theta import prime_field_generator

ctx.prec = 384
units, equal, prior = old["units"], old["equal"], old["prior"]


def ordered(scores):
    lows = sorted(v.lower() for v in scores)
    highs = sorted(v.upper() for v in scores)
    return [lo.union(hi) for lo, hi in zip(lows, highs)]


def partial(seq, frac):
    """Integral of the empirical quantile between zero and frac."""
    n = len(seq)
    whole, rem = divmod(frac.numerator * n, frac.denominator)
    total = sum(seq[:whole], arb(0))
    if rem:
        total += seq[whole] * rem / frac.denominator
    return total / n


def w1(left, right):
    m, n = len(left), len(right)
    i = j = prev = 0
    accum = arb(0)
    while i < m and j < n:
        edge = min((i + 1) * n, (j + 1) * m)
        accum += (edge - prev) * abs(left[i] - right[j])
        i += edge == (i + 1) * n
        j += edge == (j + 1) * m
        prev = edge
    assert (i, j, prev) == (m, n, m * n)
    return accum / (m * n)


def audit(p, pivot):
    signs = prior["paley_sign"](p)
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None
    n = len(signs)
    q, r = [[a / arb(n).sqrt() for a in pair[s]] for s in (1, -1)]
    if pivot is not None:
        old["add_odd"](r, -1, pivot, signs)
    F, R = [[a.real for a in old["positions"](row)] for row in (q, r)]
    plus = [i for i in range(1, n) if signs[i] == 1]
    minus = [i for i in range(1, n) if signs[i] == -1]
    for spec, row, sector in ((F, q, plus), (R, r, minus)):
        equal(sum(spec[i] for i in sector), n * row[0] - 1)
        assert all(v.is_zero() or v > 0 for v in row)
    equal(n * q[0] * r[0], 1)
    prod = ordered([R[j] - F[i] for i in plus for j in minus])
    median = prod[len(prod) // 2]
    mean = sum(prod) / len(prod)
    mad = sum(abs(x - median) for x in prod) / len(prod)
    lower, upper = partial(prod, Fraction(1, 2)), partial(prod[::-1], Fraction(1, 2))
    equal(2 * lower, mean - mad)
    equal(2 * upper, mean + mad)
    g = prime_field_generator(p)
    log = {pow(g, 2 * i, p): i for i in range(n)}
    units_g = [acb(0, arb.pi() * 2 * i / n).exp() for i in range(n)]
    root = arb(p).sqrt()
    cloud = sorted(range(1, n), key=lambda j: float(q[j] + q[-j]), reverse=True)[:6]
    weights = [(q[j] + q[-j])/2 for j in cloud]
    scale = sum(x*x for x in weights).sqrt()
    def phase(i):
        return sum(a * units_g[-i*j % n] for a,j in zip(weights,cloud)) / scale
    phases = [phase(i) for i in plus]
    phase_mean = sum(phases)/len(plus)
    correlation = sum(F[i]*(val-phase_mean) for i,val in zip(plus, phases))
    equal(correlation, n*scale-phase(0)-(n*q[0]-1)*phase_mean)
    cap = max(abs(val-phase_mean).upper() for val in phases)
    cloud_bound = abs(correlation)/(len(plus)*cap)
    assert cloud_bound > 0 and cloud_bound.upper() <= mad.upper()
    d = 3 if n % 3 == 0 else 2
    u, v = (11, 2) if p == 53 else (2, 3)
    base = [[] for _ in range(d)]
    for z in range(p):
        if all(t % p in log for t in (z,z+1,z+2)):
            base[log[(z+2) % p] % d].append((log[z], log[(z+1) % p]))
    a, b = log[u*u % p], log[v*v % p]
    bins, totals = [], [arb(0),arb(0),arb(0)]
    short_width = arb(0)
    full = arb(0)
    options = []
    for sites in base:
        scores = ordered([R[(y+b) % n]-F[(x+a) % n] for x,y in sites
                          if (x+a) % n in plus and (y+b) % n in minus])
        m = len(scores)
        full += sum(scores)/root
        options.append([sum(chosen,arb(0))/root for chosen in combinations(scores,m//2)])
        sampled = [((x+a)%n, (y+b)%n) for x,y in sites
                   if (x+a)%n in plus and (y+b)%n in minus]
        tests = [phase(x) for x,y in sampled]
        centered = [z-sum(tests)/m for z in tests]
        sample_prices = [R[y]-F[x] for x,y in sampled]
        median_sample = scores[m//2]
        cloud_cov = abs(sum(k*f for k,f in zip(centered,sample_prices)))/root
        width_lower = arb(0)
        for budget in (arb(1)/4, arb(1)/2, arb(1), arb(2)):
            excess = sum(abs(f-median_sample)*(abs(k)-budget).max(0)
                         for k,f in zip(centered,sample_prices))/root
            width_lower = width_lower.max((cloud_cov-excess)/budget)
        short_width += width_lower
        assert width_lower.lower() <= (sum(abs(f-median_sample) for f in sample_prices)/root).upper()
        dist = w1(scores,prod)
        frac = Fraction(m//2,m)
        l, h = partial(scores,frac), partial(scores[::-1],frac)
        for empirical, target in ((l,partial(prod,frac)),(h,partial(prod[::-1],frac))):
            assert abs(empirical-target).lower() <= dist.upper()
        l,h,dist = [z*m/root for z in (l,h,dist)]
        bins.append(dict(n=m, retained=m//2, raw=units(sum(scores)/root),
                         low=units(l), high=units(h), W1_at_price_scale=units(dist)))
        for k,val in enumerate((l,h,dist)):
            totals[k] += val

    # Every dilation at 53, and a nonlinear strict joint threshold away from ties.
    ortho = None
    if p == 53:
        threshold = arb(1)/31
        values = [[arb(0) for j in range(n)] for i in range(n)]
        for i in plus:
            for j in minus:
                score = R[j] - F[i]
                assert score > threshold or score < threshold
                if score > threshold:
                    values[i][j] = score
        bar = sum(sum(row) for row in values) / n**2
        sites = base[0]
        measured = []
        for a in range(n):
            for b in range(n):
                measured.append(sum(values[(x+a)%n][(y+b)%n]-bar for x,y in sites)/root)
        equal(sum(measured),0)
        rows = [acb.dft(row) for row in values]
        predicted = arb(0)
        for j in range(n):
            col = acb.dft([row[j] for row in rows])
            for i in range(n):
                if i or j:
                    kernel = sum(units_g[(i*x+j*y)%n] for x,y in sites)/root
                    predicted += abs(col[i]*kernel/n**2)**2
        observed = sum(t*t for t in measured)/n**2
        equal(observed,predicted)
        ortho = units(observed)
    nearest = ordered([abs(sum(choice)) for choice in product(*options)])[0]
    if p == 409:
        assert short_width > abs(full)
    return dict(prime=p, bits=ctx.prec, units="1e-9", probes=[u,v], index=d,
                product_pairs=len(prod), product_mean=units(mean), product_MAD=units(mad),
                product_half_price_per_site=[units(lower),units(upper)],
                six_mode_MAD_lower=units(cloud_bound), short_clipped_width_lower=units(short_width),
                realized_whole_price=units(full), nearest_floor_half_abs_price=units(nearest),
                whole_dilation_variance=ortho,
                bins=bins, summed_floor_half_range_and_W1=[units(a) for a in totals])


if __name__ == "__main__":
    for p,j in ((53,None),(257,48),(409,95)):
        print(json.dumps(audit(p,j),sort_keys=True),flush=True)
