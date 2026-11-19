"""Certify a positive four-step trial using the rank-three feedback law."""
import json
from pathlib import Path
import runpy

from flint import arb, ctx

histogram = runpy.run_path(str(Path(__file__).with_name("astra-histogram-53-check.py")))
warm = histogram["warm"]
PACKETS = histogram["N"]
SEED = arb(8).sqrt()
Z_RADIUS = 3 * arb(2).sqrt()


def remainder(floor, center, order, radius):
    ratio = max(center, abs(radius**2 - center).upper()) / (4 * floor + center)
    assert ratio < 1
    coefficient = arb(1)
    for k in range(1, order + 2):
        coefficient *= (arb(3) / 2 - k) / k
    return ((4 * floor + center).sqrt() * abs(coefficient)
            * ratio**(order + 1) / (1 - ratio)).upper()


def first_projection_error(floor, radius, quadratic, variance, tail, truncation):
    low = 1 / ((4 * floor + radius**2).sqrt() + (4 * floor + SEED**2).sqrt())
    high = 1 / (4 * floor.sqrt())
    reciprocal = (low + high) / 2
    fourth_saving = quadratic.lower()**4 / 8
    mixed_norm = (16 * variance + 3 * variance**2 - fourth_saving).sqrt()
    error = (high - low) * mixed_norm / 2
    error += reciprocal * (4 * tail + (2 * variance**2 - fourth_saving).sqrt())
    return 4 * quadratic * reciprocal, (error + truncation).upper()


def nested_rms(floor, first_radius, second_shift, quadratic, amplitude, error, tail):
    small_b, small_amplitude = quadratic.lower(), amplitude.lower()
    assert small_b > 0 and small_amplitude > 0
    variance_lower = 8 + 8 * small_b**2 + 3 * small_b**4 / 8
    variance_lower += (2 + small_b**2) * small_amplitude
    variance_lower += (arb(23) / 4 + 3 * small_b**2 / 4) * small_amplitude**2
    quadratic, amplitude = quadratic.upper(), amplitude.upper()
    base = SEED + 2 * quadratic
    bound = (base + amplitude * Z_RADIUS / 2)**2
    tilted_mean = 4 + quadratic**2 / 2 + amplitude / 2 + 3 * amplitude**2 / 8
    tilted_fraction = tilted_mean / (4 * floor + tilted_mean)
    tilted_fraction -= 4 * floor * variance_lower / (4 * floor + bound)**3
    assert tilted_fraction > 0
    midpoint = first_radius + second_shift / 2
    return (amplitude * (tilted_fraction / 2).sqrt()
            + midpoint * error / (4 * floor + midpoint**2).sqrt()
            + amplitude * Z_RADIUS * (tail + error / 2) / (2 * floor.sqrt()))


def trial(floor):
    center = arb(12)
    order = 8
    modes = histogram["centered_modes"](floor, center, order)
    assert modes[0][2] > 0
    envelope = [[abs(value).upper() for value in row] for row in modes]
    seed_modes = envelope[0]
    variance = sum(value**2 for value in seed_modes[1:]) / 2
    tail = (sum(value**2 for value in seed_modes[4:]) / 2).sqrt()
    quadratic = modes[0][2]
    radii = [arb(0)] * (PACKETS + 2)
    previous_error = arb(0)
    for step in range(1, 5):
        core = sum(k * value for k, value in enumerate(radii[:-2], 1))
        radius = (SEED + core + radii[-2]).upper()
        radii, _, _ = histogram["histogram_step"](envelope, radii, arb(1))
        total = sum(k * value for k, value in enumerate(radii[:-2], 1)) + radii[-2]
        shift = (total - core).upper()
        err = remainder(floor, center, order, radius)
        if step == 2:
            first_radius, second_shift = radius, shift
            amplitude, error = first_projection_error(
                floor, radius, quadratic, variance, tail, previous_error + err)
        elif step == 3:
            rms = nested_rms(floor, first_radius, second_shift,
                             quadratic, amplitude, error, tail)
            rms = (rms + previous_error + err).upper()
        elif step == 4:
            rms = rms * radius / (4 * floor + radius**2).sqrt() + previous_error + err
            rms = rms.upper()
        previous_error = err

    pair = 2 * radius + shift
    ideal = floor - pair * shift / 4
    truncation = (2 * (4 * floor + radius**2).sqrt() + err) * err / 4
    product = ideal - truncation
    assert product > 0 and 2 * floor.sqrt() > err
    distance = rms * pair / (4 * (floor.sqrt() + ideal.sqrt()))
    distance += truncation / (ideal.sqrt() + product.sqrt())
    distance = distance.upper()
    norm = (floor.sqrt() + distance).upper()
    return (distance * norm / (1 + norm**2).sqrt()).upper(), product.lower()


def certify(first, last, divisions, mark_cap, product_cap):
    for k in range(first, last):
        mark, product = trial(warm.slab(k, divisions))
        assert mark < mark_cap and product > product_cap, (k, mark, product)
    print(json.dumps(dict(kind="nested_positive_prime_trial", slabs=[first, last],
                          divisions=divisions, center=12, degree=16, steps=4,
                          absolute_mark_limit=str(mark_cap),
                          bulk_product_lower=str(product_cap)), sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    certify(223 * 32, 15 * 512, 1024, arb(1699) / 100000, arb(33) / 10)
    certify(27 * 128, 223 * 16, 512, arb(202) / 10000, arb(25) / 10)
