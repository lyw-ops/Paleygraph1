"""Check the convolution resolvent at thresholds from the clipped repair."""

import argparse
import json
from math import sqrt
from pathlib import Path
import runpy

from flint import arb, ctx
import numpy as np
from scipy.optimize import brentq


RESEARCH = Path(__file__).resolve().parent
RATIO = runpy.run_path(str(RESEARCH / 'parallel-ratio-18.py'))
from quadratic_theta import damped_trials
from smoothing import certify_spectrum
from square_control import square_field_sign
from theta import paley_sign


def resolvent(raw, affine, residue, threshold):
    n = len(raw)
    shadow = raw + affine + threshold
    scaled_mean = sqrt(n) * shadow.mean()
    if scaled_mean <= 0:
        return None
    excess = np.maximum(residue - threshold, 0)
    excess[0] = 0
    shadow_transform = np.fft.rfft(shadow).real
    excess_transform = np.fft.rfft(excess).real
    gaps = excess_transform[0] - excess_transform

    def margin(target):
        spectrum = shadow_transform / (gaps + target * scaled_mean)
        return (spectrum[0] + spectrum[-1] + 2 * spectrum[1:-1].sum()) / n - 1

    lower, upper = 1e-6, 2.0
    if margin(lower) <= 0 or margin(upper) >= 0:
        return None
    ratio = brentq(margin, lower, upper, xtol=5e-14)
    row = np.fft.irfft(shadow_transform / (gaps + ratio * scaled_mean), n)
    if abs(row[0] - 1) > 2e-9 or row.min() < -2e-9:
        raise RuntimeError('the resolvent failed its pointwise test')
    return ratio, row, float(excess_transform[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes', nargs='*', type=int, default=[401, 9413, 37253, 153649, 1000033])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[19, 97, 193, 389])
    parser.add_argument('--certify-max-order', type=int, default=0)
    args = parser.parse_args()
    repairs = runpy.run_path(str(RESEARCH / 'parallel-repair-17.py'))
    cases = [(p, p, None, paley_sign) for p in args.primes]
    cases += [(h * h, h, h, square_field_sign) for h in args.square_roots]
    for order, characteristic, square_root, maker in sorted(cases):
        sign = maker(characteristic)
        n = len(sign)
        for width, _, plus, minus, residual in damped_trials(sign, [1/16, order**(-1/4)], 1e-11, 48):
            for side, y in ((1, minus), (-1, plus)):
                raw = sqrt(n) * np.fft.ifft((sign != side) * np.fft.fft(y)).real
                rows = []
                competing_ratio = 0.0
                tested = 0
                for signed in (False, True):
                    floor = -raw.copy() if signed else np.maximum(-raw, 0)
                    floor[0] = 0
                    trials = list(RATIO['candidates'](sign, side, raw, floor, 4, 3, repairs))
                    competing_ratio = max(competing_ratio, *(trial[6] for trial in trials))
                    residue = trials[0][7]
                    affine = floor - residue
                    thresholds = sorted({0.0, *(trial[2] for trial in trials)})
                    tested += len(thresholds)
                    for threshold in thresholds:
                        result = resolvent(raw, affine, residue, threshold)
                        if result is not None:
                            ratio, row, excess_mass = result
                            rows.append((ratio, row, excess_mass, threshold, signed))
                record = dict(order=order, square_root=square_root, side=side, width=width,
                              thresholds_tested=tested, roots_found=len(rows),
                              translated_ratio=competing_ratio, reference_residual=residual)
                if rows:
                    ratio, row, excess_mass, threshold, signed = max(rows, key=lambda trial: trial[0])
                    record.update(resolvent_ratio=ratio, threshold=threshold, signed=signed,
                                  excess_mass=excess_mass, row_minimum=float(row.min()))
                    if order <= args.certify_max_order:
                        theta = certify_spectrum(sign, -side, row)
                        ctx.prec = 128
                        normalized = arb(theta.numerator) / theta.denominator / arb(n).sqrt()
                        record.update(theta_lower_exact=str(theta), endpoint_lower=str(normalized.lower()))
                print(json.dumps(record), flush=True)


if __name__ == '__main__':
    main()
