"""Certify exact saturation of the pinned square defect at mean one."""

from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy

from flint import acb, arb, ctx
import numpy as np


RESEARCH = Path(__file__).resolve().parent
ANCHOR = runpy.run_path(str(RESEARCH / 'anchored-repair-20.py'))
REFERENCE = runpy.run_path(str(RESEARCH / 'parallel-defect-16.py'))
R17 = ANCHOR['R17']


def check(root=389):
    sign = R17['square_field_sign'](root)
    n = len(sign)
    size = (root + 1)//2
    h_minus_one = size - 1
    locations = list(range(root - 1, n, root - 1))
    exterior = np.arange(n) % (root - 1) != 0
    allowed = sign == -1
    _, pinned, padding, kappa, _, _ = ANCHOR['anchored_tools'](sign, 1)
    assert kappa == .5
    block_eigenvalue = kappa + kappa/h_minus_one

    def unshape(row):
        local = np.zeros(n)
        local[locations] = row[locations] - row[locations].mean()
        return row - pinned(local)/block_eigenvalue

    for width, _, plus, minus, _ in R17['damped_trials'](sign, [1/16, 1/64], 1e-11, 48):
        raw = sqrt(n) * np.fft.ifft((sign != 1)*np.fft.fft(minus)).real
        row = unshape(raw + (1 - raw.mean()) * padding)
        weights = np.zeros(n)
        for _ in range(20):
            step = np.zeros(n)
            step[exterior] = 1.8*np.maximum(1/250 - row[exterior], 0)
            weights += step
            row += unshape(pinned(step))

        seed, phi0, error = REFERENCE['reference_balls'](sign, width, plus, minus)
        ctx.prec = 128
        root_n = arb(n).sqrt()
        kappa_ball = arb(1)/2
        eigenvalue = kappa_ball * size/h_minus_one
        column = [value.real for value in acb.dft([int(keep) for keep in allowed], inverse=True)]
        M = [1 - value/kappa_ball for value in column]

        def project(array, include_constant=False):
            transformed = acb.dft(array)
            selected = [value if keep else acb(0) for value, keep in zip(transformed, allowed)]
            if include_constant:
                selected[0] = transformed[0]
            return [value.real for value in acb.dft(selected, inverse=True)]

        def pin(array):
            projected = project(array)
            return [value - projected[0]*basis/kappa_ball for value, basis in zip(projected, column)]

        def flatten_subfield(array):
            local = [arb(0) for _ in range(n)]
            center = sum(array[i] for i in locations)/h_minus_one
            for i in locations:
                local[i] = array[i] - center
            correction = pin(local)
            return [value - delta/eigenvalue for value, delta in zip(array, correction)]

        y = [max(arb(0), -value) for value in seed]
        y[0] = (phi0 - seed[0])/2
        X = [root_n * value for value in project(y, include_constant=True)]
        c = sum(y)/root_n
        balanced = [value + (1-c)*pad for value, pad in zip(X, M)]
        scale = 10**12
        added = pin([arb(round(scale*value))/scale for value in weights])
        certified_row = flatten_subfield([value + delta for value, delta in zip(balanced, added)])
        row_error = (1+1/eigenvalue) * (root_n + arb(n+2).sqrt()) * error
        exterior_lower = min((certified_row[i] - row_error).lower() for i in range(n) if exterior[i])
        anchor = X[0]
        if not (exterior_lower > 0 and anchor - root_n*error > size):
            raise RuntimeError('could not certify exact square defect saturation')
        defect = (anchor - size)/arb(h_minus_one).sqrt()
        anchor_error = root_n*error/arb(h_minus_one).sqrt()
        enclosure = (defect-anchor_error).lower().union((defect+anchor_error).upper())
        print(json.dumps(dict(order=root**2, square_root=root, width=str(Fraction(width)), target_mean=1,
                              subfield_size=size, exact_defect_norm_enclosure=str(enclosure),
                              exterior_slack_lower=str(exterior_lower), reference_propagation_upper=str(row_error.upper()))),
              flush=True)


if __name__ == '__main__':
    check()
