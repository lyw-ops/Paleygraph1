"""Enclose the fixed-mark squared defect and the scaled smoothed tail."""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy

import numpy as np


RESEARCH = Path(__file__).resolve().parent
SOFT = runpy.run_path(str(RESEARCH / 'soft-tail-21.py'))
ANCHOR = SOFT['ANCHOR']
R17 = SOFT['R17']


def descend(sign, side, mark, mean, steps):
    pinned, padding, kappa, column, caps, _ = SOFT['geometry'](sign, side)
    raw = mean + (mark*sqrt(len(sign))-mean)*column/kappa
    weight = caps/padding[1:]**2
    step_size = 1/float(weight.max())
    previous, trial, momentum = raw.copy(), raw.copy(), 1.
    best_value, best_row, best_step = np.inf, raw.copy(), 0
    start_value = None
    for step in range(steps + 1):
        defect = np.maximum(-trial[1:], 0.)
        weighted = defect*weight
        if step in (0, 16, 64, 256, steps):
            value = float(weighted @ defect)
            if step == 0:
                start_value = value
            if value < best_value:
                best_value, best_row, best_step = value, trial.copy(), step
        if step == steps:
            break
        updated = trial + step_size*pinned(np.r_[0., weighted])
        next_momentum = (1 + sqrt(1 + 4*momentum**2))/2
        trial = updated + ((momentum-1)/next_momentum)*(updated-previous)
        previous, momentum = updated, next_momentum

    defect = np.maximum(-best_row[1:], 0.)
    w = np.r_[0., defect*weight]
    gamma = -float(column @ w)/kappa
    candidate = None
    if gamma > 0:
        candidate = w - pinned(w)
        candidate[0] += gamma
        finish = ANCHOR['anchored_tools'](sign, -side)[-1]
        candidate += finish(-candidate)[0]
        candidate /= candidate.sum()
    record = dict(iteration=best_step, start_weighted_squared=start_value,
                  trial_weighted_squared=best_value,
                  trial_defect_over_n14=float(np.linalg.norm(defect))/len(sign)**.25)
    return record, best_row-raw, -best_row[1:]/padding[1:], caps, candidate


def ball(value, arb):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def certify(sign, side, mark, mean, correction, candidate, square_root, penalties, thresholds):
    from flint import acb, arb, ctx

    ctx.prec = 128
    n = len(sign)
    root_n = arb(n).sqrt()
    marked = ball(mark, arb)*root_n
    mean = ball(mean, arb)
    allowed = sign == -side
    kappa = arb(int(np.count_nonzero(allowed)))/n
    omega = (1 + arb(2*n+1).sqrt())/(2*n)
    eta = (1 - omega/kappa)/(omega + omega**2/kappa)
    column = [value.real for value in acb.dft([int(keep) for keep in allowed], inverse=True)]
    padding = [1 - value/kappa for value in column[1:]]
    caps = [1/(1 + eta*(kappa+value)) for value in column[1:]]

    scale = 10**13
    coefficients = np.fft.rfft(correction).real
    integers = [round(float(coefficients[min(j, n-j)])*scale) if keep else 0
                for j, keep in enumerate(allowed)]
    direction = [value.real/scale for value in acb.dft(integers, inverse=True)]
    root_gain = (marked-mean-direction[0])/kappa
    row = [mean + root_gain*basis + delta for basis, delta in zip(column[1:], direction[1:])]
    scores = [(-value/pad).upper() for value, pad in zip(row, padding)]
    defect_upper = (sum(max(arb(0), (-value).upper())**2 for value in row)/root_n).sqrt().upper()
    weighted_upper = sum(cap*max(arb(0), score)**2 for cap, score in zip(caps, scores)).upper()
    record = dict(certified_defect_over_n14_upper=str(defect_upper),
                  certified_weighted_squared_upper=str(weighted_upper))

    # This dual keeps the original affine seed and charges the correction radius.
    level = arb(1)/4
    seed_count = sum((-mean-(marked-mean)*basis/kappa)/pad > level
                     for basis, pad in zip(column[1:], padding))
    max_inverse_cap = 1 + eta*(kappa+omega)
    min_padding = 1 - omega/kappa
    if seed_count > max_inverse_cap:
        radius_lower = level - max_inverse_cap/(2*seed_count)
        radius_lower -= root_n.sqrt()/(min_padding*arb(seed_count).sqrt())
        record['canonical_radius_lower_at_penalty_one'] = str(max(arb(0), radius_lower.lower()))
        record['canonical_radius_tail_count'] = seed_count

    dual = None
    if square_root and side == 1:
        h = (square_root+1)//2
        dual_mark = arb(1)/h
        bulk = range(square_root-2, n-1, square_root-1)
        dual_cost = (sum(padding[j]**2/caps[j] for j in bulk)/h**2).upper()
        euclidean_cost = (root_n*(h-1)/h**2).upper()
        dual = dual_mark, dual_cost, euclidean_cost
    elif candidate is not None:
        dual_mark, dual_row = SOFT['rounded_mass_one'](sign, side, candidate)
        dual_cost = sum((value*pad)**2/cap for value, pad, cap in zip(dual_row, padding, caps)).upper()
        euclidean_cost = (root_n*sum(value**2 for value in dual_row)).upper()
        dual = dual_mark, dual_cost, euclidean_cost

    margin = arb(0)
    dual_cost = arb(1)
    if dual is not None:
        dual_mark, dual_cost, euclidean_cost = dual
        margin = max(arb(0), (marked*dual_mark-mean).lower())
        if margin > 0:
            lower = (margin**2/dual_cost).lower()
            if lower > weighted_upper:
                raise RuntimeError('the dual interval exceeded the primal upper bound')
            record.update(certified_weighted_squared_lower=str(lower),
                          certified_defect_over_n14_lower=str((margin/euclidean_cost.sqrt()).lower()),
                          dual_mass_threshold_lower=str((margin/dual_cost).lower()))

    record['scaled_tail'] = []
    for penalty, threshold in zip(penalties, thresholds):
        penalty_ball = ball(penalty, arb)
        threshold_ball = ball(threshold, arb)
        upper = penalty_ball*threshold_ball
        for cap, score in zip(caps, scores):
            excess = (score-threshold_ball).upper()
            if excess > 0:
                term = penalty_ball*(excess-penalty_ball/2) if excess >= penalty_ball else excess**2/2
                upper += cap*term
        upper = min(upper.upper(), (weighted_upper/2).upper())
        lower = arb(0)
        if margin > 0:
            mass = min(arb(1), (margin/(dual_cost*penalty_ball)).lower())
            lower = (penalty_ball*mass*(margin-penalty_ball*mass*dual_cost/2)).lower()
            if lower > upper:
                raise RuntimeError('the scaled-tail bounds are inconsistent')
        record['scaled_tail'].append(dict(penalty=str(penalty), lower=str(lower), upper=str(upper)))
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', nargs='*', type=int)
    parser.add_argument('--square-roots', nargs='+', type=int, default=[])
    parser.add_argument('--mark', type=Fraction, default=Fraction(1))
    parser.add_argument('--mean', type=Fraction, default=Fraction(1))
    parser.add_argument('--steps', type=int, default=512)
    parser.add_argument('--penalties', nargs='+', type=Fraction,
                        default=list(map(Fraction, ('1/100', '1/10', '1', '10'))))
    parser.add_argument('--certify-max-order', type=int, default=0)
    parser.add_argument('--endpoint-dual', action='store_true',
                        help='try the separate dense theta solve for the dual row')
    args = parser.parse_args()
    if min(args.mark, args.mean, *args.penalties) <= 0 or args.steps < 0:
        parser.error('use positive marks, means and penalties and a nonnegative depth')
    cases = [(p, None, R17['paley_sign']) for p in args.primes]
    cases += [(h*h, h, R17['square_field_sign']) for h in args.square_roots]
    for order, square_root, maker in sorted(cases):
        sign = maker(order if square_root is None else square_root)
        for side in (1, -1):
            result, correction, scores, caps, candidate = descend(
                sign, side, float(args.mark), float(args.mean), args.steps)
            if args.endpoint_dual and square_root is None:
                from theta import optimize

                _, endpoint = optimize(sign, side)
                candidate = endpoint/endpoint.sum()
                result['dual_candidate'] = 'endpoint'
            thresholds = [SOFT['hinge_envelope'](scores, caps, float(value))[0] for value in args.penalties]
            if order <= args.certify_max_order:
                result.update(certify(sign, side, args.mark, args.mean, correction, candidate,
                                      square_root, args.penalties, thresholds))
            print(json.dumps(dict(order=order, square_root=square_root, witness_sign=side,
                                  mark=str(args.mark), mean=str(args.mean)) | result), flush=True)


if __name__ == '__main__':
    main()
