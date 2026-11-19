"""Outward check of two actual delayed cold-orbit profiles and their common mix."""

import hashlib
import json
from pathlib import Path
import runpy

from flint import arb, ctx
import numpy as np

prior = runpy.run_path(str(Path(__file__).with_name("true-spill-63-check.py")))
transform = prior["transform"]


def main():
    ctx.prec = 128
    prime = 9413
    windows = [(44, 76), (84, 124)]
    last = windows[-1][1]
    signs = prior["paley_sign"](prime)
    sign = list(map(int, signs))
    n = len(sign)
    assert n == (prime - 1) // 2
    root = arb(n).sqrt()
    scale = 2**60
    state = [arb(0)] * n
    reflection = np.r_[0, np.arange(n - 1, 0, -1)]
    orbit_hash = hashlib.sha256(np.zeros(n, dtype="<i8").tobytes())
    error = arb(0)
    source = [[arb(0)] * n for _ in windows]
    source_error = [arb(0) for _ in windows]
    scalar = [arb(0) for _ in windows]
    scalar_error = [arb(0) for _ in windows]
    for j in range(last + 1):
        phi = [(state[0]**2 + 4).sqrt()] + [abs(x) for x in state[1:]]
        for k, (a, b) in enumerate(windows):
            w = int(a <= j <= b)
            following = int(a <= j + 1 <= b)
            if w or following:
                source[k] = [x + (w + following) * z for x, z in zip(source[k], phi)]
                source_error[k] += (w + following) * error
            if w != following:
                scalar[k] += (w - following) * sum(phi, arb(0)) / n
                scalar_error[k] += error / root
        if j == last:
            break
        proposal = prior["kernel_action"](signs, np.array([float(x.mid()) for x in phi]))
        proposal = (proposal + proposal[reflection]) / 2
        integers = [round(float(x) * scale) for x in proposal]
        orbit_hash.update(np.asarray(integers, dtype="<i8").tobytes())
        next_state = [arb(x) / scale for x in integers]
        exact_step = transform(sign, phi)
        error = (error + prior["upper_norm"]([x - y for x, y in zip(exact_step, next_state)])).upper()
        state = next_state

    col = transform(sign, [arb(1)] + [arb(0)] * (n - 1))
    repaired = []
    for k, (a, b) in enumerate(windows):
        denominator = 4 * (b - a + 1)
        mean_radius = (root * (source_error[k] / root + scalar_error[k]) / denominator).upper()
        mean = root * (sum(source[k], arb(0)) / n + scalar[k]) / denominator + arb(0, mean_radius)
        row_radius = (root * (2 * source_error[k] + scalar_error[k]) / denominator).upper()
        flipped = transform(sign, source[k])
        profiles = []
        for side in (1, -1):
            a0 = arb(n - 1 - side) / (2 * n)
            pin = [1 - (side * x - arb(1) / n) / (2 * a0) for x in col[1:]]
            assert min(x.lower() for x in pin) > arb(1) / 2
            row = [root * (x + side * y + scalar[k]) / denominator + arb(0, row_radius)
                   for x, y in zip(source[k], flipped)]
            mark = row[0] / root
            assert mark > 0
            shift = (1 + arb(1) / 200) * mark - mean
            profiles.append([x + shift * w for x, w in zip(row[1:], pin)])
        repaired.append(profiles)

    def entry(side, i, numerator, denominator=1000):
        first = repaired[0][side][i - 1]
        second = repaired[1][side][i - 1]
        return ((denominator - numerator) * first + numerator * second) / denominator

    inner_minima = [min(entry(s, i, u).lower()
                        for s in range(2) for i in range(1, n))
                    for u in (668, 968)]
    assert min(inner_minima) > 0
    left = entry(1, 1295, 667)
    right = entry(1, 1720, 969)
    assert left < 0 and right < 0
    assert entry(1, 1295, 1000) > entry(1, 1295, 0)
    assert entry(1, 1720, 1000) < entry(1, 1720, 0)
    print(json.dumps(dict(prime=prime, windows=windows, precision=ctx.prec, epsilon="1/200",
                          inner_interval_times_1000=[668, 968],
                          outer_interval_times_1000=[667, 969],
                          inner_minima=list(map(str, inner_minima)),
                          upper_negative_witnesses=[str(left.upper()), str(right.upper())],
                          negative_sites=[[-1, 1295], [-1, 1720]],
                          orbit_prefix_sha256=orbit_hash.hexdigest()), sort_keys=True))


if __name__ == "__main__":
    main()
