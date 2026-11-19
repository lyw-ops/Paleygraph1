"""Enclose the initial active set in two prime cases beyond the support barrier."""

from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy

from flint import acb, arb, ctx
import numpy as np


RESEARCH = Path(__file__).resolve().parent
REPAIR = runpy.run_path(str(RESEARCH / 'parallel-repair-17.py'))
REF = runpy.run_path(str(RESEARCH / 'parallel-defect-16.py'))


def positive_part(ball):
    return max(arb(0), ball.lower()).union(max(arb(0), ball.upper()))


def check(prime=153649, width=1/16):
    sign = REPAIR['paley_sign'](prime)
    n = len(sign)
    _, _, plus, minus, _ = next(REPAIR['damped_trials'](sign, [width], 1e-11, 48))
    vector, marked_activation, error = REF['reference_balls'](sign, width, plus, minus)
    ctx.prec = 128
    jacobi = acb.dft([int(value) for value in sign])
    root_n, root_q = arb(n).sqrt(), arb(prime).sqrt()
    selected_size = 2000
    for side, numeric_y in ((1, minus), (-1, plus)):
        project, numeric_kappa, numeric_omega, (height, _), _ = REPAIR['sector_tools'](sign, side)
        numeric_alpha = min(2, 1/(numeric_kappa + numeric_omega))
        numeric_raw = sqrt(n) * np.fft.ifft((sign != side) * np.fft.fft(numeric_y)).real
        numeric_cost = np.maximum(-numeric_raw, 0)
        numeric_shadow = np.full(n, .75 * (1 - numeric_raw.mean()))
        for _ in range(4):
            numeric_shadow += numeric_alpha * project(np.maximum(numeric_cost - numeric_shadow, 0))
        numeric_residue = numeric_cost - numeric_shadow
        cutoff = Fraction(.5 * REPAIR['cap'](numeric_residue, height)[1])
        cutoff_ball = arb(cutoff.numerator) / cutoff.denominator
        indices = np.argpartition(numeric_residue[1:], -selected_size)[-selected_size:] + 1

        allowed = sign == -side
        kappa = arb(int(np.count_nonzero(allowed))) / n
        signed_jacobi = [side * value.real for value in jacobi[1:]]
        maximum = max(value.lower() for value in signed_jacobi).union(max(value.upper() for value in signed_jacobi))
        reciprocal = 1 / (kappa + (1 + maximum)/(2*n))
        alpha = min(arb(2), reciprocal.lower()).union(min(arb(2), reciprocal.upper()))

        def projection(vector, include_constant=False):
            transformed = acb.dft(vector)
            kept = [entry if keep else acb(0) for entry, keep in zip(transformed, allowed)]
            if include_constant:
                kept[0] = transformed[0]
            return [entry.real for entry in acb.dft(kept, inverse=True)]

        y = [positive_part(-side * value) for value in vector]
        y[0] = (marked_activation - side * vector[0]) / 2
        cost = [positive_part(-root_n * value) for value in projection(y, include_constant=True)]
        mass = sum(y) / root_n
        shadow = [3*(1-mass)/4 for _ in range(n)]
        for _ in range(4):
            step = projection([positive_part(item - value) for item, value in zip(cost, shadow)])
            shadow = [value + alpha * increment for value, increment in zip(shadow, step)]

        # Subtract the respective means before comparing the updates. Each
        # centered shadow sees the effective floor D-b, and changing that
        # floor costs at most (1+3/4)*sqrt(n)*error in Euclidean norm.
        residual_error = arb(7)/4 * (1 + 4*alpha) * root_n * error
        margin = min((cost[i] - shadow[i] - cutoff_ball - residual_error).lower() for i in indices)
        m = arb(selected_size)
        radius_bound = alpha/4 * ((1-1/arb(n)) * m/root_q - (2+1/(2*root_q)) * (1-m/n))
        if not (margin > 0 and radius_bound > 1):
            raise RuntimeError('did not certify the support obstruction')
        print(json.dumps(dict(prime=prime, side=side, width=str(Fraction(width)), cutoff=str(cutoff),
                              minimum_support=selected_size, cutoff_margin_lower=str(margin),
                              radius_lower=str(radius_bound.lower()), residual_error_upper=str(residual_error.upper()))))


if __name__ == '__main__':
    check()
