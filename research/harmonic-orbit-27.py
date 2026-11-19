"""Certify finite actual Picard prefixes using norm shadowing and Arb FFTs.

Floating point chooses rational trial points. Every local defect and every
claimed actual-orbit bound is enclosed independently with Arb.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from flint import acb, arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def rational_ball(value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def upper_norm(values):
    return sum((abs(x).upper()**2 for x in values), arb(0)).sqrt().upper()


def lower_norm(values):
    return sum((max(arb(0), abs(x).lower())**2 for x in values), arb(0)).sqrt().lower()


def certify_prefix(order, square_root, tau, steps, checkpoints, precision, root_budget=False):
    ctx.prec = precision
    sign = square_field_sign(square_root) if square_root else paley_sign(order)
    n = len(sign)
    assert n >= 3 and sign[0] == 0 and np.array_equal(sign[1:], sign[:0:-1])
    scale = 2**60
    c = [arb(4)]+[4*rational_ball(tau)/n]*(n-1)
    c_float = np.array([4.]+[4*float(tau)/n]*(n-1))
    point = [0]*n
    x = [arb(0)]*n
    phi_x = [z.sqrt() for z in c]
    error = arb(0)
    losses = []
    pair_product = arb(1)
    hash_state = hashlib.sha256(np.asarray(point, dtype='<i8').tobytes())
    maximum_local = arb(0)
    initial_increment = None
    root_secants = []
    one_step_product = arb(1)
    for t in range(steps):
        candidate_float = kernel_action(sign, np.sqrt(np.array(point, dtype=float)**2/scale**2+c_float))
        candidate_float = (candidate_float+candidate_float[np.r_[0, np.arange(n-1, 0, -1)]])/2
        proposed = [round(float(z)*scale) for z in candidate_float]
        assert proposed[1:] == proposed[:0:-1]
        assert max(map(abs, proposed)) < 2**63
        y = [arb(z)/scale for z in proposed]
        phi_y = [(z*z+cc).sqrt() for z, cc in zip(y, c)]
        transformed = acb.dft(phi_x)
        for i in range(n):
            transformed[i] *= int(sign[i])
        exact_step = [z.real for z in acb.dft(transformed, inverse=True)]
        if t == 0:
            initial_increment = upper_norm(exact_step)
        local = upper_norm([a-b for a, b in zip(exact_step, y)])
        new_error = (error+local).upper()
        d_error = (error+new_error).upper()
        maximum_local = max(maximum_local, local)
        delta = [b-a for a, b in zip(x, y)]
        bulk_norm_upper = upper_norm(delta[1:])
        bulk_norm_lower = lower_norm(delta[1:])
        full_norm_upper = upper_norm(delta)
        weighted_energy = arb(0)
        for i in range(1, n):
            # Q=(phi(x)phi(y)+xy+c)/2, and |partial_x Q| <= (phi(y)+|y|)/2.
            # The norm errors bound every coordinate perturbation.
            q_center = (phi_x[i]*phi_y[i]+x[i]*y[i]+c[i])/2
            q_upper = (q_center+((phi_y[i]+abs(y[i])+2*new_error)*error
                                   +(phi_x[i]+abs(x[i])+2*error)*new_error)/2).upper()
            weight = max(arb(0), min(arb(1), (c[i]/q_upper).lower()))
            weighted_energy += weight*delta[i]**2
        weighted_norm_lower = max(arb(0), weighted_energy.lower()).sqrt().lower()
        loss_numerator = max(arb(0), (weighted_norm_lower-d_error).lower())
        denominator = (bulk_norm_upper+d_error).upper()
        loss = ((loss_numerator/denominator)**2).lower() if denominator > 0 else arb(0)
        loss = max(arb(0), min(arb(1), loss))
        losses.append(loss)
        if t % 2:
            pair_loss = min(losses[-1], losses[-2])
            pair_factor = (1-(1-arb(2)/n)*pair_loss).upper()
            assert pair_factor > 0 and pair_factor <= 1
            pair_product = (pair_product*pair_factor).upper()
        record = dict(kind='step', order=order, square_root=square_root, n=n,
                      tau=str(tau), step=t, precision=precision,
                      local_defect_upper=str(local), actual_state_error_upper=str(error),
                      actual_bulk_loss_lower=str(loss))
        if root_budget or t in checkpoints:
            h_sum = sum((b-a for a, b in zip(phi_x, phi_y)), arb(0))
            mean_lower = max(arb(0), (abs(h_sum).lower()-arb(n).sqrt()*d_error).lower())
            mean_fraction = ((mean_lower/(arb(n).sqrt()*(full_norm_upper+d_error)))**2).lower()
            record['actual_mean_reserve_fraction_lower'] = str(mean_fraction)
        if root_budget:
            root_q = (phi_x[0]*phi_y[0]+x[0]*y[0]+c[0])/2
            root_q_upper = (root_q+((phi_y[0]+abs(y[0])+2*new_error)*error
                                      +(phi_x[0]+abs(x[0])+2*error)*new_error)/2).upper()
            root_loss_lower = max(arb(0), min(arb(1), (c[0]/root_q_upper).lower()))
            root_secant = (1-root_loss_lower).upper()
            root_secants.append(root_secant)
            full_factor = min(arb(1), (max((1-loss).upper(), root_secant)-mean_fraction).upper())
            assert full_factor > 0
            one_step_product = (one_step_product*full_factor).upper()
            record['actual_root_secant_squared_upper'] = str(root_secant)
            record['actual_full_energy_ratio_upper'] = str(full_factor)
        if t in checkpoints:
            lower_true_norm = max(arb(0), (bulk_norm_lower-d_error).lower())
            if lower_true_norm > 0:
                amplitude_bounds = []
                for field, field_error in ((x, error), (y, new_error)):
                    weighted = upper_norm([a*b for a, b in zip(field[1:], delta[1:])])
                    maximum = max(abs(z).upper() for z in field[1:])
                    product_upper = weighted+maximum*d_error+field_error*(bulk_norm_upper+d_error)
                    amplitude_bounds.append((n*(product_upper/lower_true_norm)**2).upper())
                amplitude = max(amplitude_bounds)
                record['actual_endpoint_amplitude_upper'] = str(amplitude)
                record['moment_loss_lower'] = str((4*rational_ball(tau)/(amplitude+4*rational_ball(tau))).lower())
            trial_residual = upper_norm([a-b for a, b in zip(exact_step, x)])
            record['actual_residual_upper'] = str((trial_residual+2*error).upper())
            record['actual_field_norm_upper'] = str((upper_norm(x)+error).upper())
            record['actual_root_abs_upper'] = str((abs(x[0])+error).upper())
        print(json.dumps(record), flush=True)
        hash_state.update(np.asarray(proposed, dtype='<i8').tobytes())
        point, x, phi_x, error = proposed, y, phi_y, new_error
    completed_pairs = steps//2
    log_budget = (-pair_product.log()).lower()
    audit = dict(kind='prefix_audit', order=order, square_root=square_root,
                          n=n, tau=str(tau), precision=precision, steps=steps,
                          rational_scale=scale, orbit_integer_sha256=hash_state.hexdigest(),
                          maximum_local_defect_upper=str(maximum_local),
                          actual_final_state_error_upper=str(error),
                          paired_time=2*completed_pairs,
                          initial_increment_norm_upper=str(initial_increment),
                          paired_product_upper=str(pair_product),
                          paired_residual_upper=str((initial_increment*pair_product.sqrt()).upper()),
                          pair_log_budget_lower=str(log_budget),
                          critical_budget_margin_lower=str((log_budget-arb(order).log()/2).lower()),
                          minimum_bulk_loss_lower=str(min(losses)))
    if root_budget:
        gamma = arb(n)/(n-2)
        for use_root in (False, True):
            u, v = arb(1), arb(1)
            for loss, a in zip(reversed(losses), reversed(root_secants)):
                rho = max(arb(1)/2, (1-loss).upper())
                u, v = ((a if use_root else 1)*v).upper(), (rho*max(u, v)).upper()
            factor = min(arb(1), ((gamma**steps)*max(u, v)).upper())
            label = 'root_path' if use_root else 'bulk_path'
            audit[label+'_product_upper'] = str(factor)
            audit[label+'_log_budget_lower'] = str((-factor.log()).lower())
            audit[label+'_residual_upper'] = str((initial_increment*factor.sqrt()).upper())
        audit['one_step_product_upper'] = str(one_step_product)
        audit['one_step_residual_upper'] = str((initial_increment*one_step_product.sqrt()).upper())
        audit['one_step_log_budget_lower'] = str((-one_step_product.log()).lower())
        audit['maximum_root_secant_squared_upper'] = str(max(root_secants))
        # Validate a field-specific invariant tail ball, if available.
        final_transform = acb.dft(phi_x)
        for i in range(n):
            final_transform[i] *= int(sign[i])
        final_step = [z.real for z in acb.dft(final_transform, inverse=True)]
        final_residual = upper_norm([a-b for a, b in zip(final_step, x)])
        audit['final_rational_trial_residual_upper'] = str(final_residual)
        for denominator in (100000, 10000, 2000, 1000, 500, 200, 100, 50, 20, 10):
            radius = arb(1)/denominator
            derivative = max(((abs(z).upper()+radius)/
                              ((abs(z).upper()+radius)**2+cc).sqrt()).upper()
                             for z, cc in zip(x, c))
            margin = ((1-derivative)*radius-final_residual).lower()
            if margin > 0 and error < radius:
                audit['invariant_tail_ball'] = dict(
                    radius=str(Fraction(1, denominator)),
                    contraction_upper=str(derivative), invariance_margin_lower=str(margin),
                    all_future_actual_norm_upper=str((upper_norm(x)+radius).upper()),
                    all_future_bulk_amplitude_upper=str(
                        (n*(max(abs(z).upper() for z in x[1:])+radius)**2).upper()),
                    fixed_point_root_abs_upper=str((abs(x[0])+radius).upper()))
                break
    print(json.dumps(audit), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', nargs='*', type=int)
    parser.add_argument('--square-roots', nargs='*', type=int, default=[])
    parser.add_argument('--tau', default='1/20')
    parser.add_argument('--steps', type=int, default=128)
    parser.add_argument('--precision', type=int, default=128)
    parser.add_argument('--root-budget', action='store_true',
                        help='also certify root secants, every mean reserve, and block products')
    parser.add_argument('--checkpoints', nargs='*', type=int, default=[0, 1, 2, 4, 8, 16, 32, 64, 96, 127])
    args = parser.parse_args()
    tau = Fraction(args.tau)
    if not 0 < tau < 1 or args.steps < 1 or args.precision < 64 or (not args.primes and not args.square_roots):
        parser.error('provide fields, a floor in (0,1), positive depth and precision at least 64')
    for p in args.primes:
        certify_prefix(p, None, tau, args.steps, set(args.checkpoints), args.precision, args.root_budget)
    for h in args.square_roots:
        certify_prefix(h*h, h, tau, args.steps, set(args.checkpoints), args.precision, args.root_budget)


if __name__ == '__main__':
    main()
