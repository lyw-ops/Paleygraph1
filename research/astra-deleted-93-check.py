"""Outward checks of true short-probe deletions, complementary prices and tails."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx
from theta import prime_field_generator

here = Path(__file__).resolve().parent
old = runpy.run_path(str(here / "astra-matched-88-check.py"))
prior, units, same = old["prior"], old["units"], old["equal"]
ctx.prec = 384


def positive(x):
    return x.max(0)


def ordered(values):
    lows = sorted((x.lower() for x in values), reverse=True)
    highs = sorted((x.upper() for x in values), reverse=True)
    return [left.union(right) for left, right in zip(lows, highs)]


def extrema(values):
    return min(x.lower() for x in values).union(min(x.upper() for x in values))


def stop_loss(values, t):
    return sum((positive(x - t) for x in values), arb(0))


def upper_quantile(values, mass, budget):
    """The sample points have identical mass. Return top integral and dual threshold."""
    if not values or not mass:
        return arb(0), arb(0)
    count = min(Fraction(len(values)), budget * len(values) / mass)
    whole, rem = divmod(count.numerator, count.denominator)
    t = positive(values[whole]) if whole < len(values) else arb(0)
    integral = sum((positive(x) for x in values[:whole]), arb(0)) + t * rem / count.denominator
    point_mass = arb(mass.numerator) / (mass.denominator * len(values))
    total = point_mass * integral
    same(total, budget * t + point_mass * stop_loss(values, t))
    return total, t


def audit(p, odd, pair, table):
    d = prior["paley_sign"](p)
    optima, err = prior["solve_prime_pair"](d)
    assert err is None
    n, root = len(d), arb(p).sqrt()
    q, r = [[a / arb(n).sqrt() for a in optima[side]] for side in (1, -1)]
    if odd is not None:
        old["add_odd"](r, -1, odd, d)
    same(q[0] * r[0] * n, 1)
    X, Y = [[z.real for z in old["positions"](row)] for row in (q, r)]
    plus = [j for j in range(1, n) if d[j] == 1]
    minus = [j for j in range(1, n) if d[j] == -1]
    for row, spec, sector in ((q, X, plus), (r, Y, minus)):
        same(sum(spec[j] for j in sector), n * row[0] - 1)
    # The three selected pairs have the larger mark in the minus row.
    gap = r[0] - q[0]
    assert gap > 0
    prod = [Y[j] - X[i] for i in plus for j in minus]
    size = len(prod)
    mean = sum(prod) / size
    K = len(table)
    assert len(set(table)) == K
    even = [(r[j] + r[-j]) / 2 for j in range(n)]
    response = sum(even[(j - k) % n] for j in table for k in table) / K**2 - q[0] / K
    omega = [acb(0, arb.pi() * 2 * i / n).exp() for i in range(n)]
    kernel = [abs(sum(omega[j * i % n] for j in table) / K)**2 for i in range(n)]
    same(sum(kernel), arb(n) / K)
    same(sum(k * y for k, y in zip(kernel, Y)) / n, response + q[0] / K)
    assert response > gap
    scale = gap / response
    same(scale * response, gap)

    index = 3 if n % 3 == 0 else 2
    mass = Fraction(p, 32 * index)
    target_mass = arb(mass.numerator) / mass.denominator
    g = prime_field_generator(p)
    log = {pow(g, 2 * j, p): j for j in range(n)}
    bins = [[] for _ in range(index)]
    weight, paid = arb(0), arb(0)
    u, v = pair
    for z in range(p):
        x, y = u * u * z % p, v * v * (z + 1) % p
        w = (z + 2) % p
        if x in log and log[x] in plus and y in log and log[y] in minus and w in log:
            score = Y[log[y]] - X[log[x]]
            bins[log[w] % index].append(score)
            weight += scale * kernel[log[y]]
            paid += scale * kernel[log[y]] * score / root
    intact = sum(sum(row) for row in bins) / root
    assert weight < scale * n / K
    all_deleted = [sum(picks) / root for picks in product(*[[arb(0)] + row for row in bins])]
    nearest = extrema([abs(intact - x) for x in all_deleted])
    tau = arb(1) / 10
    directions = []
    for orient in (-1, 1):
        prod_sorted = ordered([orient * x for x in prod])
        prod_extreme, prod_t = upper_quantile(prod_sorted, mass, 1)
        pred = index * prod_extreme / root
        actual, h_error = arb(0), arb(0)
        for row in bins:
            scores = ordered([orient * score for score in row])
            extreme, t = upper_quantile(scores, Fraction(len(scores)), 1)
            actual += extreme / root
            # Each truncated optimum is reached at one of these two thresholds.
            allowance = arb(0)
            for t0 in (tau.max(t), tau.max(prod_t)):
                diff = stop_loss(scores, t0) - target_mass * stop_loss(prod_sorted, t0) / size
                allowance = allowance.max(abs(diff))
            h_error += allowance / root
        same(actual, ordered([orient * price for price in all_deleted])[0])
        assert abs(actual - pred).upper() <= (h_error + index * tau / root).lower()
        # Jensen bound (4), using the same deletion budget in all bins.
        tail_bounds = []
        for T in (0, 1, 2, 4, 8, 16):
            # The optimum can use fewer than index sites. Take the nonnegative
            # part of the per-site allowance, which is needed for T=0.
            count_part = positive(2 * T - orient * root * mean) * index / p
            tail = sum(positive(orient * root * x - T) for x in prod) / size
            tail_bounds.append(count_part + (len(plus) + len(minus)) * tail / p)
        best_bound = extrema(tail_bounds)
        assert actual.upper() <= best_bound.lower()
        directions.append(dict(sign=orient, empirical_top=units(actual), product_top=units(pred),
                          hinge_discrepancy=units(h_error), jensen_upper=units(best_bound)))
    return dict(prime=p, bits=ctx.prec, units="1e-9", probes=pair, counts=[len(row) for row in bins],
                per_bin_delete_cap=1, product_pairs=size, gap=units(gap), difference_set=table,
                table_response=units(response), attenuation=units(scale), fractional_deleted_count=units(weight),
                fractional_deleted_price=units(paid), fractional_complement_price=units(intact-paid),
                intact_price=units(intact), ordinary_selections=len(all_deleted),
                nearest_ordinary_complement_abs=units(nearest), directions=directions)


def square_control(s):
    square = {a * a % s for a in range(1, s)}
    nr = next(a for a in range(2, s) if a not in square)

    def chi(a, b):
        norm = (a * a - nr * b * b) % s
        return 0 if not norm else 1 if norm in square else -1

    plus = subfield_plus = matches = 0
    for a in range(s):
        for b in range(s):
            if chi(a, b) == 1 and chi(1 - a, -b) == 1:
                plus += 1
                subfield_plus += b == 0
            if (chi(a, b) == chi(a + 1, b) == chi(a + 2, b) == 1
                    and chi(1 - 4 * a, -4 * b) == 1
                    and chi(1 - 9 * (a + 1), -9 * b) == -1):
                assert b != 0
                matches += 1
    assert plus == (s * s - 5) // 4 and subfield_plus == s - 2
    budget = s // 16
    actual_cost = Fraction(2, s + 1)
    product_high_mass = Fraction(s * s * subfield_plus, 32 * plus)
    assert matches >= budget and product_high_mass >= budget
    product_top = Fraction(budget, s) * (1 - actual_cost)
    return dict(square=s*s, exact=True, probes=[2, 3], matches=matches, budget=budget,
                strict_plus=plus, strict_subfield_plus=subfield_plus,
                actual_negative_top="0", product_negative_top=str(product_top))


if __name__ == "__main__":
    for row in [(53, None, (11, 2), [0, 3, 6, 9, 12, 15, 18, 21]),
                (257, 48, (2, 3), [0, 33, 79, 120, 41, 87, 60, 19]),
                (409, 95, (2, 3), [0, 33, 9, 42, 87, 96, 63, 150])]:
        print(json.dumps(audit(*row), sort_keys=True), flush=True)
    print(json.dumps(square_control(101), sort_keys=True), flush=True)
