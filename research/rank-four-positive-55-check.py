"""Certify the fourth increment using independent rank-four derived groups."""
import json
from pathlib import Path
import runpy

from flint import arb, ctx

nested = runpy.run_path(str(Path(__file__).with_name("nested-positive-54-check.py")))
histogram = nested["histogram"]
warm = nested["warm"]
SEED = nested["SEED"]
Z_RADIUS = nested["Z_RADIUS"]


def activation(floor, x):
    return (4 * floor + x*x).sqrt()


def third_projection_error(floor, b, tail, lam, eps, first, second, shift, truncation):
    low = 1 / (activation(floor, first) + activation(floor, second))
    high = 1 / (4 * floor.sqrt())
    mean = (low + high) / 2
    midpoint = first + shift / 2
    gz = b / 2 + Z_RADIUS * tail
    ez = Z_RADIUS * eps
    numerator = 2 * arb(2).sqrt() + 2 * gz + lam * (arb(3) / 4).sqrt() + ez
    error = midpoint * eps / activation(floor, midpoint)
    error += (high - low) * lam * numerator / 2
    error += mean * lam * (2 * gz + lam / arb(2).sqrt() + ez)
    return (4 * lam * mean).upper(), (error + truncation).upper()


def fourth_rms(floor, b, tail, lam, eps, nu, error, second, shift, truncation):
    tilted_activation = 1 - (floor / (floor + 2)).sqrt()
    tilted_activation += (b*b + lam*lam) / (8 * floor)
    tilted_activation += 25 * nu*nu / (256 * floor)
    midpoint = second + shift / 2
    return (nu * (tilted_activation / 2).sqrt()
            + midpoint * error / activation(floor, midpoint)
            + 4 * nu * (tail + eps + error / 2) / floor.sqrt()
            + truncation).upper()


def trial(floor):
    center, order = arb(12), 8
    modes = histogram["centered_modes"](floor, center, order)
    envelope = [[abs(value).upper() for value in row] for row in modes]
    variance = sum(entry**2 for entry in envelope[0][1:]) / 2
    tail = (sum(entry**2 for entry in envelope[0][4:]) / 2).sqrt()
    quadratic = modes[0][2]
    assert quadratic > 0
    radii = [arb(0)] * (histogram["N"] + 2)
    former_error = arb(0)
    for step in range(1, 5):
        core = sum(k * value for k, value in enumerate(radii[:-2], 1))
        radius = (SEED + core + radii[-2]).upper()
        radii, _, _ = histogram["histogram_step"](envelope, radii, arb(1))
        total = sum(k * value for k, value in enumerate(radii[:-2], 1)) + radii[-2]
        shift = (total - core).upper()
        err = nested["remainder"](floor, center, order, radius)
        if step == 2:
            first, second_shift = radius, shift
            lam, eps = nested["first_projection_error"](
                floor, radius, quadratic, variance, tail, former_error + err)
        elif step == 3:
            second, third_shift = radius, shift
            b, lam = quadratic.upper(), lam.upper()
            nu, error = third_projection_error(
                floor, b, tail, lam, eps, first, second, second_shift, former_error + err)
        elif step == 4:
            rms = fourth_rms(floor, b, tail, lam, eps, nu, error,
                             second, third_shift, former_error + err)
        former_error = err
    pair_radius = 2 * radius + shift
    ideal = floor - pair_radius * shift / 4
    truncation = (2 * activation(floor, radius) + err) * err / 4
    product = ideal - truncation
    assert product > 0 and 2 * floor.sqrt() > err
    distance = rms * pair_radius / (4 * (floor.sqrt() + ideal.sqrt()))
    distance += truncation / (ideal.sqrt() + product.sqrt())
    norm = (floor.sqrt() + distance).upper()
    return (distance * norm / (1 + norm*norm).sqrt()).upper(), product.lower()


def certify(first, last, div, mark_cap, product_cap):
    for k in range(first, last):
        mark, product = trial(warm.slab(k, div))
        assert mark < mark_cap and product > product_cap, (k, mark, product)
    print(json.dumps(dict(kind="rank_four_positive_prime_trial", slabs=[first, last],
                          divisions=div, polynomial_center=12, degree=16, steps=4,
                          absolute_mark_limit=str(mark_cap),
                          bulk_product_lower=str(product_cap)), sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    certify(27 * 128, 7 * 512, 512, arb(1699) / 100000, arb(26) / 10)
    certify(13 * 256, 27 * 128, 512, arb(218) / 10000, arb(15) / 10)
