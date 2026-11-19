"""Interval check of one fixed weighted pinning rule on actual cold orbits."""

import argparse
import hashlib
import json
from pathlib import Path
import runpy

from flint import arb, ctx
import numpy as np

prior = runpy.run_path(str(Path(__file__).with_name("true-spill-63-check.py")))
transform = prior["transform"]
depth = 128
scale = 2**60


def certify(prime):
    signs = prior["paley_sign"](prime)
    sign = list(map(int, signs))
    n = len(sign)
    assert n == (prime - 1) // 2
    assert sign[0] == 0 and sign[:0:-1] == sign[1:]
    root = arb(n).sqrt()
    col = transform(sign, [arb(1)] + [arb(0)] * (n - 1))
    reflect = np.r_[0, np.arange(n - 1, 0, -1)]
    weight_types = [
        ("late_weight", [0] + [j**6 * (depth + 1 - j) for j in range(1, depth + 1)] + [0],
         arb(1) / 200, True),
        ("flat_prefix", [0] + [1] * depth + [0], arb(1) / 100, False),
    ]
    sources = [[arb(0)] * n for _ in weight_types]
    constants = [arb(0) for _ in weight_types]
    source_errors = [arb(0) for _ in weight_types]
    constant_errors = [arb(0) for _ in weight_types]
    state = [arb(0)] * n
    error = arb(0)
    digest = hashlib.sha256(np.zeros(n, dtype="<i8").tobytes())
    for j in range(depth + 1):
        phi = [(state[0]**2 + 4).sqrt()] + [abs(x) for x in state[1:]]
        phi_mean = sum(phi, arb(0)) / n
        for k, (_, w, _, _) in enumerate(weight_types):
            a, b = w[j] + w[j+1], w[j] - w[j+1]
            sources[k] = [x + a * z for x, z in zip(sources[k], phi)]
            constants[k] += b * phi_mean
            source_errors[k] += a * error
            constant_errors[k] += abs(b) * error / root
        if j == depth:
            break
        proposal = prior["kernel_action"](signs, np.array([float(x.mid()) for x in phi]))
        proposal = (proposal + proposal[reflect]) / 2
        ints = [round(float(x) * scale) for x in proposal]
        assert ints[1:] == ints[:0:-1]
        digest.update(np.asarray(ints, dtype="<i8").tobytes())
        new_state = [arb(x) / scale for x in ints]
        exact_step = transform(sign, phi)
        local = prior["upper_norm"]([x - y for x, y in zip(exact_step, new_state)])
        error = (error + local).upper()
        state = new_state

    record = dict(prime=prime, depth=depth, precision=ctx.prec,
                  orbit_prefix_sha256=digest.hexdigest(), state_error_upper=str(error))
    for k, (label, w, allowance, positive) in enumerate(weight_types):
        denom = 4 * sum(w)
        source, constant = sources[k], constants[k]
        source_error, scalar_error = source_errors[k], constant_errors[k]
        # The scaled row is sqrt(n) * [(I+sK)S + C] / denom.
        # All accumulated quantities here have had the weight denominator removed.
        row_radius = (root * (2 * source_error + scalar_error) / denom).upper()
        g_radius = (root * (source_error / root + scalar_error) / denom).upper()
        g = root * (sum(source, arb(0)) / n + constant) / denom + arb(0, g_radius)
        flipped = transform(sign, source)
        entries = []
        for side in (1, -1):
            diagonal = arb(n - 1 - side) / (2 * n)
            b = [1 - (side * x - arb(1)/n) / (2 * diagonal) for x in col[1:]]
            assert min(x.lower() for x in b) > arb(1)/2
            z = [root * (x + side * y + constant) / denom + arb(0, row_radius)
                 for x, y in zip(source, flipped)]
            mark = z[0] / root
            assert mark > 0
            shift = (1 + allowance) * mark - g
            repaired = [x + shift * f for x, f in zip(z[1:], b)]
            limit = min(x.lower() for x in repaired) if positive else min(x.upper() for x in repaired)
            if positive:
                assert limit > 0
            entries.append(dict(side=side, extremal_bound=str(limit)))
        if not positive:
            assert any(arb(x["extremal_bound"]) < 0 for x in entries)
        record[label] = entries
    print(json.dumps(record, sort_keys=True), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int, default=[9413, 153649])
    args = parser.parse_args()
    ctx.prec = 128
    for prime in args.primes:
        certify(prime)
