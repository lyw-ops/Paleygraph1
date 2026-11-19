"""Enclose the three-step positive predictor with prime joint moments."""
import json
from math import comb

from flint import arb, ctx

ctx.prec = 192
DEGREE = 28
SEED = arb(8).sqrt()


def activation_modes(floor):
    modes = [[arb(0) for _ in range(DEGREE + 1)] for _ in range(DEGREE + 1)]
    weight = 2 * floor.sqrt()
    for ell in range(1, DEGREE // 2 + 1):
        weight *= (arb(3) / 2 - ell) / (4 * floor * ell)
        for j in range(2 * ell + 1):
            powers = 2 * ell - j
            common = weight * comb(2 * ell, j) * (SEED / 2) ** powers
            for i in range(powers // 2 + 1):
                k = powers - 2 * i
                modes[j][k] += common * comb(powers, i) * (2 if k else 1)
    return modes


def polynomial(coefficients, value):
    total = arb(0)
    for coefficient in reversed(coefficients):
        total = total * value + coefficient
    return total


def remainder(floor, radius):
    ratio = radius * radius / (4 * floor)
    assert ratio < 1
    first = DEGREE // 2 + 1
    coefficient = arb(1)
    for ell in range(1, first + 1):
        coefficient *= (arb(3) / 2 - ell) / ell
    return (2 * floor.sqrt() * abs(coefficient) * ratio**first).upper()


def powers(mass, second):
    for count in range(DEGREE + 1):
        moment = count * second * mass ** (count - 1) if count else arb(0)
        yield count, mass ** count, moment


def mixed_powers(current, previous, increment):
    a, c = current
    b, d = previous
    delta, energy = increment
    a_powers = [a ** k for k in range(DEGREE)]
    b_powers = [b ** k for k in range(DEGREE)]
    for count in range(1, DEGREE + 1):
        mass = second = arb(0)
        for older in range(count):
            newer = count - 1 - older
            common = a_powers[newer] * b_powers[older]
            mass += delta * common
            second += energy * common
            if newer:
                second += delta * newer * c * a_powers[newer - 1] * b_powers[older]
            if older:
                second += delta * older * d * a_powers[newer] * b_powers[older - 1]
        yield count, mass, second


def moment_step(modes, moments):
    rank = second = arb(0)
    for j, mass, variance in moments:
        for k, value in enumerate(modes[j]):
            if not value or j + k == 0:
                continue
            energy = k * k * mass + variance
            bound = min(((k + j) * mass).upper(), (mass * energy).sqrt().upper())
            if k:
                bound = min(bound, (k * mass + variance / (4 * k)).upper())
            rank += abs(value) * bound
            second += abs(value) * energy
    return rank.upper(), second.upper()


def local_bounds(floor, steps, use_moments):
    modes = activation_modes(floor)
    coefficients = [sum((j + k) * abs(value) for k, value in enumerate(row))
                    for j, row in enumerate(modes)]
    v = sum(value * value for value in modes[0][1:]) / 2
    tilted_second_moment = 4 + 3 * v / 4

    b = arb(0)
    previous_error = arb(0)
    current = previous = increment_moments = (arb(0), arb(0))
    for step in range(1, steps + 1):
        bulk_radius = (SEED + b).upper()
        previous_b = b
        if use_moments:
            next_moments = moment_step(modes, powers(*current))
            if step == 1:
                increment_moments = next_moments
            else:
                increment_moments = moment_step(
                    modes, mixed_powers(current, previous, increment_moments))
            previous, current = current, next_moments
            b = current[0]
        else:
            b = polynomial(coefficients, b)
        err = remainder(floor, bulk_radius)
        if step == 1:
            rms = v.sqrt()
        elif step == 2:
            tilted_radius = (SEED + previous_b / 2) ** 2
            tilted_fraction = tilted_second_moment / (4 * floor + tilted_second_moment)
            tilted_fraction -= 32 * floor / (4 * floor + tilted_radius) ** 3
            rms = (v * tilted_fraction).sqrt()
            rms += previous_error + err
        else:
            rms *= bulk_radius / (4 * floor + bulk_radius * bulk_radius).sqrt()
            rms += previous_error + err
        rms = rms.upper()
        previous_error = err

    increment = increment_moments[0] if use_moments else (b - previous_b).upper()
    assert increment > 0
    pair_radius = 2 * bulk_radius + increment
    ideal_floor = floor - pair_radius * increment / 4
    activation_upper = (4 * floor + bulk_radius * bulk_radius).sqrt()
    truncation = (2 * activation_upper + err) * err / 4
    product_floor = ideal_floor - truncation
    assert product_floor > 0 and 2 * floor.sqrt() > err
    distance = rms * pair_radius / (4 * (floor.sqrt() + ideal_floor.sqrt()))
    distance += truncation / (product_floor.sqrt() + ideal_floor.sqrt())
    distance = distance.upper()
    cap = (floor.sqrt() + distance).upper()
    mark = (distance * cap / (1 + cap * cap).sqrt()).upper()
    return mark, product_floor.lower()


def verify(start, stop, divisions, mark_limit, product_limit, steps, use_moments=False):
    for k in range(start, stop):
        floor = arb(arb(2 * k + 1) / (2 * divisions), arb(1) / (2 * divisions))
        mark_upper, product_lower = local_bounds(floor, steps, use_moments)
        assert mark_upper < mark_limit, (k, mark_upper)
        assert product_lower > product_limit, (k, product_lower)
    print(json.dumps(dict(kind="prime_joint_increment_bound", steps=steps,
                          mellin_second_moment=use_moments,
                          polynomial_degree=DEGREE, slabs=stop - start,
                          interval=[str(arb(start) / divisions), str(arb(stop) / divisions)],
                          limiting_bulk_product_lower=str(product_limit),
                          limiting_abs_mark_upper=str(mark_limit)), sort_keys=True))


if __name__ == "__main__":
    verify(35 * 64, 10 * 256, 256, arb(169) / 10000, arb(4), 3)
    verify(17 * 128, 35 * 64, 256, arb(184) / 10000, arb(4), 3)
    verify(9 * 256, 10 * 256, 256, arb(169) / 10000, arb(33) / 10, 4)
    verify(63 * 32, 9 * 256, 256, arb(169) / 10000, arb(1), 4, use_moments=True)
