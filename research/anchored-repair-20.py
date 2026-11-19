"""Repair a Fourier row while keeping its marked coordinate fixed."""

import argparse
from fractions import Fraction
import json
from math import isfinite, sqrt
from pathlib import Path
import runpy

import numpy as np


RESEARCH = Path(__file__).resolve().parent
R17 = runpy.run_path(str(RESEARCH / 'parallel-repair-17.py'))


def anchored_tools(sign, side):
    n = len(sign)
    project, kappa, _, _, _ = R17['sector_tools'](sign, side)
    omega = (1 + sqrt(2*n + 1))/(2*n)
    if kappa <= omega:
        raise ValueError('the universal off-diagonal bound must be below the projector diagonal')
    unit = np.zeros(n)
    unit[0] = 1
    column = project(unit)
    padding = 1 - column/kappa
    padding[0] = 0
    eta = (1 - omega/kappa)/(omega + omega**2/kappa)
    height = padding[1:] * (1 + eta*(kappa + column[1:]))
    capacities = padding[1:] / height
    if capacities.sum() <= 1:
        raise ValueError('insufficient bulk kernel capacity for threshold optimization')

    def anchored_project(array):
        projected = project(array)
        projected -= (projected[0]/kappa) * column
        return projected

    def finish(residual):
        scores = residual[1:] / padding[1:]
        order = np.argsort(-scores, kind='stable')
        t = scores[order[np.searchsorted(np.cumsum(capacities[order]), 1)]]
        weights = np.zeros(n)
        weights[1:] = np.maximum(residual[1:] - t*padding[1:], 0) / height
        correction = (t + weights.sum()) * padding + eta * anchored_project(weights)
        if abs(correction[0]) > 5e-10 or np.min(correction[1:] - residual[1:]) < -5e-9:
            raise RuntimeError('the anchor-preserving finish failed its pointwise test')
        return correction, float(t)

    return project, anchored_project, padding, kappa, column, finish


def trials(sign, side, raw, depth, target_ratios):
    n = len(raw)
    root_n = sqrt(n)
    _, project_anchored, padding, kappa, column, finish = anchored_tools(sign, side)
    opposite_finish = anchored_tools(sign, -side)[-1]
    c, anchor = float(raw.mean()), float(raw[0])
    targets = [(f'ratio_{ratio:g}', anchor/(root_n*ratio)) for ratio in target_ratios]
    if not targets:
        targets = [('reserve', 1.), ('large_ratio', .94*anchor/root_n)]
    for label, mean in targets:
        adjustment = (mean - c) * padding
        depths = sorted({0, min(4, depth), min(16, depth), depth})
        for step in range(depths[-1] + 1):
            row = raw + adjustment
            defect = np.maximum(-row, 0)
            defect[0] = 0
            projected = project_anchored(defect)
            gamma = -float(column @ defect)/kappa
            dual_mass = (defect.sum() + gamma)/n
            dual_margin = gamma * anchor - n * dual_mass * mean
            deviation = float(defect @ defect) + float(projected @ row) - dual_margin
            if abs(deviation) > 5e-9*max(1., abs(dual_margin), np.linalg.norm(defect)**2):
                raise RuntimeError('the signed defect identity failed')
            if step in depths:
                correction, t = finish(-row)
                full_correction = adjustment + correction
                primal_lower = anchor/(root_n * (row + correction).mean())
                record = dict(target=label, depth=step, target_mean=mean, target_ratio=anchor/(root_n*mean),
                              raw_mark=anchor/root_n, defect_norm=float(np.linalg.norm(defect)),
                              projected_norm=float(np.linalg.norm(projected)), gamma=gamma,
                              dual_margin=float(dual_margin), signed_work=float(projected @ row), finish_cutoff=t,
                              finish_mass=float(correction.mean()), primal_lower=float(primal_lower))
                dual_row = None
                if gamma > 0:
                    dual_row = defect - projected
                    dual_row[0] += gamma
                    correction, _ = opposite_finish(-dual_row)
                    dual_row += correction
                    record['primal_upper'] = float(root_n * dual_row.mean()/gamma)
                    if record['primal_upper'] < primal_lower - 2e-9:
                        raise RuntimeError('complementary positive rows failed to pair')
                yield record, full_correction, dual_row
            adjustment += 1.9*projected


def certify_anchor(sign, side, balls, candidate):
    """Round an exact-zero-anchored correction and pad its bulk with M."""
    from flint import acb, arb

    vector, phi0, error = balls
    n = len(sign)
    root_n = arb(n).sqrt()
    allowed = sign == -side
    kappa = arb(int(np.count_nonzero(allowed)))/n
    lower_padding = 1 - (1 + arb(2*n + 1).sqrt())/(2*n*kappa)
    if not lower_padding > 0:
        raise RuntimeError('could not certify the padding floor')
    y = [max(arb(0), -side*value) for value in vector]
    y[0] = (phi0 - side*vector[0])/2
    transformed = acb.dft(y)
    raw_hat = [entry if keep else acb(0) for entry, keep in zip(transformed, allowed)]
    raw_hat[0] = transformed[0]
    raw = [entry.real for entry in acb.dft(raw_hat, inverse=True)]
    scale = 10**14
    coefficients = np.fft.fft(candidate / sqrt(n)).real
    integers = [round(scale*value) if keep else 0 for value, keep in zip(coefficients, allowed)]
    for i in range(1, n // 2 + 1):
        integers[-i] = integers[i]
    integers[0] = -sum(integers)
    repair = [entry.real/scale for entry in acb.dft(integers, inverse=True)]
    slack = min((g+h-error).lower() for g, h in zip(repair[1:], raw[1:]))
    pad_units = max(0, int(((-slack/lower_padding)*scale).upper().ceil().unique_fmpz()))
    mass = (transformed[0].real + arb(integers[0])/scale)/root_n + root_n*arb(pad_units)/scale
    positive_anchor = raw[0] - error
    if not positive_anchor > 0 or not mass-error > 0:
        raise RuntimeError('the interval proof missed positivity at the mark or of the mass')
    return dict(anchor_lower=str(positive_anchor.lower()), mass_upper=str((mass+error).upper()),
                primal_lower_certified=str((positive_anchor/(mass+error)).lower()),
                anchor_repair_sum=0, padding_units=pad_units, padding_denominator=scale)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes', nargs='*', type=int, default=[401, 9413, 37253, 153649, 1000033])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[19, 97, 193, 389])
    parser.add_argument('--width', type=float, default=1/16)
    parser.add_argument('--moving', action='store_true')
    parser.add_argument('--depth', type=int, default=64)
    parser.add_argument('--certify-max-order', type=int, default=0)
    parser.add_argument('--target-ratios', nargs='+', type=float, default=[],
                        help='replace the default means with the means for these target ratios')
    args = parser.parse_args()
    if args.depth < 0 or not 0 < args.width < 1:
        parser.error('depth must be nonnegative and width must lie in (0,1)')
    if any(not isfinite(ratio) or ratio <= 0 for ratio in args.target_ratios):
        parser.error('target ratios must be positive and finite')
    cases = [(p, p, None, R17['paley_sign']) for p in args.primes]
    cases += [(ell*ell, ell, ell, R17['square_field_sign']) for ell in args.square_roots]
    if args.certify_max_order:
        reference = runpy.run_path(str(RESEARCH / 'parallel-defect-16.py'))
        from flint import arb, ctx
        from smoothing import certify_spectrum
    for order, characteristic, square_root, maker in sorted(cases):
        sign = maker(characteristic)
        n = len(sign)
        widths = [args.width]
        if args.moving:
            widths = sorted(set(widths + [order**(-1/4)]), reverse=True)
        for width, _, plus, minus, residual in R17['damped_trials'](sign, widths, 1e-11, 48):
            balls = reference['reference_balls'](sign, width, plus, minus) if order <= args.certify_max_order else None
            for side, y in ((1, minus), (-1, plus)):
                raw = sqrt(n) * np.fft.ifft((sign != side)*np.fft.fft(y)).real
                candidates = list(trials(sign, side, raw, args.depth, args.target_ratios))
                if balls is not None:
                    best_primal = max(candidates, key=lambda entry: entry[0]['primal_lower'])
                    best_dual = min(candidates, key=lambda entry: entry[0].get('primal_upper', np.inf))
                    best_primal[0].update(certify_anchor(sign, side, balls, best_primal[1]))
                    if best_dual[2] is not None:
                        theta = certify_spectrum(sign, side, best_dual[2])
                        ctx.prec = 128
                        normalized_upper = arb(n).sqrt() * theta.denominator / theta.numerator
                        best_dual[0].update(primal_upper_certified=str(normalized_upper.upper()),
                                            opposite_theta_lower_exact=str(theta))
                for record, _, _ in candidates:
                    print(json.dumps(dict(order=order, square_root=square_root, side=side, width=width,
                                          width_exact=str(Fraction(width)), reference_residual=residual) | record), flush=True)


if __name__ == '__main__':
    main()
