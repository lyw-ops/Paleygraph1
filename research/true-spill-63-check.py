"""Outward checks of the pinned reflection on unrounded zero-floor Picard averages."""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, arb, ctx, fmpq

prior = runpy.run_path(str(Path(__file__).with_name("harmonic-orbit-27.py")))
upper_norm = prior["upper_norm"]
kernel_action = prior["kernel_action"]
paley_sign = prior["paley_sign"]
square_field_sign = prior["square_field_sign"]


def transform(sign, values):
    frequency = acb.dft(values)
    return [x.real for x in acb.dft(
        [x * weight for x, weight in zip(frequency, sign)], inverse=True
    )]


def positive_part(x):
    return x.max(arb(0))


def fixed_reserve(values, sign, side, ell, a, b, u):
    # values is T times the scaled raw row. u denotes T times the mean allowance.
    trial = [x + u * y for x, y in zip(values, b)]
    deficit = [arb(0)] + [positive_part(u / 4 - x) for x in trial[1:]]
    flipped = transform(sign, deficit)
    n = len(values)
    mean = sum(deficit, arb(0)) / n
    pin = 2 * sum((x * y for x, y in zip(ell, deficit)), arb(0)) / a
    spill = [side * x - mean - pin * y for x, y in zip(flipped, ell)]
    output = [x + d + r for x, d, r in zip(trial, deficit, spill)]
    return spill, output, deficit


def single_site_uniform_upper(values, col, side, ell, a, b, site, length):
    # A dyadic piecewise-affine upper envelope for the true chosen entry.
    all_sites = len(values)
    intercept = values[site].upper().fmpq()
    slope = b[site].upper().fmpq()
    stops = []
    for j in range(1, all_sites):
        weight = (int(site == j) - arb(1) / all_sites
                  + side * col[(site - j) % all_sites]
                  - 2 * ell[site] * ell[j] / a).upper().fmpq()
        hinge_height = (-values[j]).upper() if weight >= 0 else (-values[j]).lower()
        hinge_slope = (b[j] - arb(1) / 4).lower() if weight >= 0 else (b[j] - arb(1) / 4).upper()
        height, speed = hinge_height.fmpq(), hinge_slope.fmpq()
        assert speed > 0
        if height <= 0 or weight == 0:
            continue
        intercept_change, slope_change = weight * height, weight * speed
        intercept += intercept_change
        slope -= slope_change
        knot = height / speed
        if knot < length:
            stops.append((knot, intercept_change, slope_change))
    bound = intercept
    for knot, intercept_change, slope_change in sorted(stops):
        bound = max(bound, intercept + slope * knot)
        intercept -= intercept_change
        slope += slope_change
    return arb(max(bound, intercept + slope * length)).upper()


def budget(order, n, square_root, depth, side, values, sign, col, mean, error, orbit_digest):
    a = arb(n - 1 - side) / (2 * n)
    ell = [(int(i == 0) - arb(1) / n + side * x) / 2 for i, x in enumerate(col)]
    assert (ell[0] - a).contains(0)
    ell[0] = a
    b = [1 - x / a for x in ell]
    assert min(x.lower() for x in b[1:]) > arb(1) / 2

    u = arb(4) / 3 if order == 9413 else arb(3) / 2
    spill, output, deficit = fixed_reserve(values, sign, side, ell, a, b, u)
    spill_margin = min((x + u / 4).lower() for x in spill[1:])
    signed_minimum = min(x.lower() for x in output[1:])
    info = dict(order=order, square_root=square_root, depth=depth, side=side,
                floor=0, precision=ctx.prec, orbit_prefix_sha256=orbit_digest,
                state_error_upper=str(error), success_mean_coefficient=str(u),
                signed_spill_margin_times_depth_lower=str(spill_margin),
                repaired_bulk_minimum_times_depth_lower=str(signed_minimum))

    if not square_root:
        assert spill_margin > arb(1) / 40
        assert signed_minimum > arb(1) / 40 and values[0] > 0
        assert (output[0] - values[0]).contains(0)
        assert (sum(output, arb(0)) / n - (depth * mean + u)).contains(0)
        alpha = values[0] / (depth * mean + u) / arb(n).sqrt()
        absolute_charge = (
            (1 + arb(order).sqrt()) / n
            + (1 + arb(order).sqrt())**2 / (2 * n**2 * a)
        ) * sum(deficit, arb(0))
        assert absolute_charge > u / 4
        info.update(absolute_spill_envelope_times_depth_lower=str(absolute_charge.lower()),
                    normalized_theta_lower=str(alpha.lower()))
    elif side == -1:
        # At square order the exact minus theta is (sqrt(q)+1)/2.
        # The input keeps the full marked value while its mean may increase.
        needed = values[0] / depth * 2 / (square_root + 1) - mean
        assert needed > arb(1) / 8 and spill_margin < -arb(1) and output[0] > 0
        info.update(mean_increment_lower_for_any_completion=str(needed.lower()))
    else:
        assert spill_margin > 0
    length = fmpq(1) if not square_root else fmpq(3, 2)
    if not square_root or side == -1:
        _, trial_at_endpoint, _ = fixed_reserve(values, sign, side, ell, a, b, arb(length))
        witness = min(range(1, n), key=lambda j: trial_at_endpoint[j].upper())
        upper = single_site_uniform_upper(values, col, side, ell, a, b, witness, length)
        assert upper < -arb(1) / 10, (order, depth, side, witness, upper)
        info.update(failure_mean_coefficient_interval=["0", str(length)],
                    fixed_witness_coordinate=witness,
                    uniform_repaired_witness_times_depth_upper=str(upper))
    print(json.dumps(info, sort_keys=True), flush=True)


def certify(order, square_root, depths):
    signs = square_field_sign(square_root) if square_root else paley_sign(order)
    sign = list(map(int, signs))
    n = len(sign)
    assert sign[0] == 0 and sign[1:] == sign[:0:-1]
    assert n == (order - 1) // 2 and sum(sign) == -1
    root = arb(n).sqrt()
    scale = 2**60
    root_delta = [arb(1)] + [arb(0)] * (n - 1)
    col = transform(sign, root_delta)
    state = [arb(0)] * n
    error = arb(0)
    total_error = arb(0)
    total = [arb(0)] * n
    phi0 = [arb(2)] + [arb(0)] * (n - 1)
    digest = hashlib.sha256(np.zeros(n, dtype="<i8").tobytes())
    reflect = np.r_[0, np.arange(n - 1, 0, -1)]
    for time in range(max(depths) + 1):
        phi = [(state[0]**2 + 4).sqrt()] + [abs(x) for x in state[1:]]
        if time > 0:
            total = [x + y for x, y in zip(total, phi)]
            total_error = (total_error + error).upper()
        if time in depths:
            # T*X = source + sigma*K(source) + scalar*1.
            trapezoid = [(2*x + y - z) / 4 for x, y, z in zip(total, phi0, phi)]
            k_trapezoid = transform(sign, trapezoid)
            scalar = (sum(phi, arb(0)) - 2) / (4 * n)
            true_error = (root * (total_error + error / 4)).upper()
            mean = sum(total, arb(0)) * root / (2 * n * time)
            mean += arb(0, (total_error / (2 * time)).upper())
            for side in (1, -1):
                values = [root * (x + side * y + scalar) + arb(0, true_error)
                          for x, y in zip(trapezoid, k_trapezoid)]
                budget(order, n, square_root, time, side, values, sign, col,
                       mean, error, digest.hexdigest())
        if time < max(depths):
            proposal = kernel_action(signs, np.array([float(x.mid()) for x in phi]))
            proposal = (proposal + proposal[reflect]) / 2
            proposed = [round(float(x) * scale) for x in proposal]
            assert proposed[1:] == proposed[:0:-1]
            digest.update(np.asarray(proposed, dtype="<i8").tobytes())
            new_state = [arb(x) / scale for x in proposed]
            exact_step = transform(sign, phi)
            error = (error + upper_norm([x - y for x, y in zip(exact_step, new_state)])).upper()
            state = new_state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", choices=("all", "prime", "larger", "square"), default="all")
    args = parser.parse_args()
    ctx.prec = 128
    cases = [
        ("prime", 9413, None, (32, 64, 128)),
        ("larger", 153649, None, (32, 64, 128)),
        ("square", 9409, 97, (32, 64, 128)),
    ]
    for label, order, square_root, depths in cases:
        if args.part in ("all", label):
            certify(order, square_root, depths)


if __name__ == "__main__":
    main()
