"""Certify a centered Taylor bound for the four successive positive trials."""
import json
from pathlib import Path
import runpy

from flint import arb, ctx

rank_four = runpy.run_path(str(Path(__file__).with_name("rank-four-positive-55-check.py")))
nested = rank_four["nested"]
histogram = nested["histogram"]
warm = nested["warm"]
SEED = nested["SEED"]
Z_RADIUS = nested["Z_RADIUS"]
activation = rank_four["activation"]
fourth_rms = rank_four["fourth_rms"]


def expansion_constants(t):
    at_zero = activation(t, arb(0))
    at_center = (4 * t + 6).sqrt()
    at_boundary = (4 * t + 8).sqrt()
    coefficient = 1 / at_center
    linear_rms = 4 / (at_zero * at_center * (at_zero + at_center))
    quadratic_max = 1 / (4 * t.sqrt())
    quadratic_min = 2 * t / at_boundary**3
    quadratic_variation = (quadratic_max - quadratic_min) / 2
    cubic_cap = 12 / (25 * arb(5).sqrt() * t)
    activation_variance = 1 - (t / (t + 2)).sqrt()
    return (coefficient, linear_rms, quadratic_max, quadratic_variation,
            cubic_cap, activation_variance)


def second_projection(t, b, variance, tail, first_shift, truncation):
    coef, linear_rms, a_max, a_var, m3, activation_variance = expansion_constants(t)
    centered_square_rms = (2 * variance**2 - b**4 / 8).sqrt()
    square_rms = (3 * variance**2 - b**4 / 8).sqrt()
    odd_variance = b*b * linear_rms**2 / 2 + activation_variance * tail**2
    even_rms = a_max * centered_square_rms + a_var * variance
    remainder = m3 * first_shift * square_rms / 6
    return 2 * b * coef, ((odd_variance + even_rms**2).sqrt() + remainder + truncation).upper()


def third_projection(t, b, variance, tail, lam, eps, first, first_shift, second_shift, truncation):
    coef, linear_rms, a_max, a_var, m3, _ = expansion_constants(t)
    midpoint = first + (second_shift + lam * Z_RADIUS) / 2
    replacement = midpoint * eps / activation(t, midpoint)
    linear = lam * linear_rms / arb(2).sqrt()
    quadratic = a_max * (b*b*lam*lam + lam**4 / 2).sqrt()
    quadratic += lam*lam * a_var / 2 + 2 * lam * a_max * Z_RADIUS * tail
    gz2 = b * (arb(3) / 8).sqrt() + Z_RADIUS**2 * tail
    g2z = b*b * arb(5).sqrt() / 4 + (first_shift + 2*b) * Z_RADIUS * tail
    g2z = min(g2z.upper(), (Z_RADIUS * (3*variance**2 - b**4/8).sqrt()).upper())
    z3 = Z_RADIUS * (arb(3) / 4).sqrt()
    remainder = m3 * lam * (g2z + lam * gz2 + lam*lam * z3 / 3) / 2
    return 2 * lam * coef, (replacement + linear + quadratic + remainder + truncation).upper()


def trial(t):
    center, order = arb(12), 8
    modes = histogram["centered_modes"](t, center, order)
    envelope = [[abs(value).upper() for value in row] for row in modes]
    variance = sum(entry**2 for entry in envelope[0][1:]) / 2
    tail = (sum(entry**2 for entry in envelope[0][4:]) / 2).sqrt()
    b = modes[0][2]
    assert b > 0
    radii = [arb(0)] * (histogram["N"] + 2)
    former_error = arb(0)
    for step in range(1, 5):
        core = sum(k * value for k, value in enumerate(radii[:-2], 1))
        radius = (SEED + core + radii[-2]).upper()
        radii, _, _ = histogram["histogram_step"](envelope, radii, arb(1))
        total = sum(k * value for k, value in enumerate(radii[:-2], 1)) + radii[-2]
        shift = (total - core).upper()
        err = nested["remainder"](t, center, order, radius)
        if step == 1:
            first_shift = shift
        elif step == 2:
            first, second_shift = radius, shift
            lam, eps = second_projection(t, b, variance, tail, first_shift, former_error + err)
        elif step == 3:
            second, third_shift = radius, shift
            nu, error = third_projection(t, b, variance, tail, lam, eps, first,
                                         first_shift, second_shift, former_error + err)
        elif step == 4:
            rms = fourth_rms(t, b, tail, lam, eps, nu, error,
                             second, third_shift, former_error + err)
        former_error = err
    pair_radius = 2 * radius + shift
    ideal = t - pair_radius * shift / 4
    truncation = (2 * activation(t, radius) + err) * err / 4
    product = ideal - truncation
    assert product > 0 and 2 * t.sqrt() > err
    distance = rms * pair_radius / (4 * (t.sqrt() + ideal.sqrt()))
    distance += truncation / (ideal.sqrt() + product.sqrt())
    norm = (t.sqrt() + distance).upper()
    return (distance * norm / (1 + norm*norm).sqrt()).upper(), product.lower()


def certify(first, last, div, mark_cap, product_cap):
    for k in range(first, last):
        mark, product = trial(warm.slab(k, div))
        assert mark < mark_cap and product > product_cap, (k, mark, product)
    print(json.dumps(dict(kind="centered_taylor_positive_prime_trial", slabs=[first, last],
                          divisions=div, polynomial_center=12, degree=16, steps=4,
                          absolute_mark_limit=str(mark_cap), bulk_product_lower=str(product_cap)),
                     sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    certify(207 * 64, 27 * 512, 2048, arb(1699) / 100000, arb(147) / 100)
    certify(25 * 128, 207 * 16, 512, arb(232) / 10000, arb(33) / 100)
