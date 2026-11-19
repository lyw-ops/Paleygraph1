"""Certify pinned square defects and the corresponding one-sided width range."""

from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy

from flint import acb, arb, ctx
import numpy as np


RESEARCH = Path(__file__).resolve().parent
ANCHOR = runpy.run_path(str(RESEARCH / 'anchored-repair-20.py'))


def find_correction(sign, root, mark):
    """Search the affine slice with a flat subfield bulk."""
    _, pinned, _, kappa, column, _ = ANCHOR['anchored_tools'](sign, 1)
    n = len(sign)
    h = (root + 1) // 2
    bulk = np.arange(root - 1, n, root - 1)
    exterior = np.arange(n) % (root - 1) != 0
    eigenvalue = kappa * h / (h - 1)
    baseline = 1 + (float(mark) * sqrt(n) - 1) * column / kappa

    def flatten(row):
        local = np.zeros(n)
        local[bulk] = row[bulk] - row[bulk].mean()
        return row - pinned(local) / eigenvalue

    previous = baseline.copy()
    row = baseline.copy()
    momentum = 1.
    for step in range(1501):
        if row[exterior].min() > .001:
            return row - baseline, step
        violation = np.zeros(n)
        violation[exterior] = np.maximum(.003 - row[exterior], 0)
        updated = row + flatten(pinned(violation))
        next_momentum = (1 + sqrt(1 + 4 * momentum**2)) / 2
        row = updated + (momentum - 1) / next_momentum * (updated - previous)
        previous, momentum = updated, next_momentum
    raise RuntimeError("the flattened trial did not reach the exterior floor")


def certify(sign, root, mark, correction, depth):
    """Reconstruct the pinned flattened row from exact Fourier coefficients."""
    ctx.prec = 128
    n = len(sign)
    root_n = arb(n).sqrt()
    h = (root + 1) // 2
    bulk = list(range(root - 1, n, root - 1))
    allowed = sign == -1
    kappa = arb(int(np.count_nonzero(allowed))) / n
    assert kappa == arb(1) / 2
    eigenvalue = kappa * h / (h - 1)
    column = [value.real for value in acb.dft([int(keep) for keep in allowed], inverse=True)]

    def pin(row):
        return [value - row[0] * basis / kappa for value, basis in zip(row, column)]

    quantum = 10**13
    coefficients = np.fft.fft(correction).real
    rounded = [round(quantum * value) if keep else 0 for value, keep in zip(coefficients, allowed)]
    for i in range(1, n // 2 + 1):
        rounded[-i] = rounded[i]
    direction = pin([value.real / quantum for value in acb.dft(rounded, inverse=True)])
    target = (arb(mark.numerator) / mark.denominator) * root_n
    row = [1 + (target - 1) * basis / kappa + value for basis, value in zip(column, direction)]

    local = [arb(0) for _ in range(n)]
    center = sum(row[i] for i in bulk) / (h - 1)
    for i in bulk:
        local[i] = row[i] - center
    masked = [value if keep else acb(0) for value, keep in zip(acb.dft(local), allowed)]
    shape = pin([value.real for value in acb.dft(masked, inverse=True)])
    row = [value - delta / eigenvalue for value, delta in zip(row, shape)]
    exterior_slack = min(row[i].lower() for i in range(n) if i % (root - 1))
    assert exterior_slack > 0 and target > h

    negative_level = (target - h) / (h - 1)
    defect = negative_level * arb(h - 1).sqrt()
    width = h * negative_level / (n + h * negative_level)
    return dict(
        order=root**2, square_root=root, target_mark=str(mark), target_mean=1,
        proposal_depth=depth, exterior_slack_lower=str(exterior_slack),
        exact_defect_enclosure=str(defect), saturation_width_lower=str(width.lower()),
        saturation_scale_lower=str((root_n * width).lower()),
    )


def main():
    root = 389
    sign = ANCHOR['R17']['square_field_sign'](root)
    for mark in (Fraction(49, 50), Fraction(1)):
        correction, depth = find_correction(sign, root, mark)
        print(json.dumps(certify(sign, root, mark, correction, depth)), flush=True)


if __name__ == '__main__':
    main()
