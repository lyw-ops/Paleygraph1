"""Actual Paley smoothing increments, including weighted saturation tails.

All trajectory outputs are floating-point diagnostics, not interval
certificates or asymptotic estimates.
"""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def scalar(value):
    return float(value)


def root_transfer_rate(n, rho):
    """Largest eigenvalue of the two-step upper comparison matrix."""
    k = 1/n
    trace = k*k-rho*(1/n+k*k)
    eigenvalue = (trace+sqrt(trace*trace+4*rho*k*k))/2
    return rho+(1-rho)*eigenvalue


def integer_normalization(order, square_root, sign):
    """Parseval and the marked coefficient using only exact sign counts."""
    n = len(sign)
    sign_sum = sum(map(int, sign))
    square_sum = sum(int(value)**2 for value in sign)
    if sign_sum != -1 or square_sum != n-1 or int(sign[0]) != 0:
        raise RuntimeError('exact Paley sign normalization failed')
    marked = Fraction(sign_sum, n)
    row_energy = Fraction(square_sum, n)
    bulk_row_energy = row_energy-marked**2
    if bulk_row_energy != Fraction(n*n-n-1, n*n):
        raise RuntimeError('marked-to-bulk normalization failed')
    matrix_audits = []
    for rho in (Fraction(0), Fraction(1, 2), Fraction(9, 10), Fraction(30, 31)):
        diagonal_0 = marked**2
        diagonal_1 = -rho*(1-bulk_row_energy)
        off_diagonal_squared = marked**2*bulk_row_energy*rho
        trace = diagonal_0+diagonal_1
        determinant = diagonal_0*diagonal_1-off_diagonal_squared
        determinant_of_complement = 1-trace+determinant
        if determinant != -rho/n**2 or determinant_of_complement != 1-Fraction(1,n*n)+rho/n:
            raise RuntimeError('exact comparison-matrix normalization failed')
        matrix_audits.append(dict(rho=str(rho), trace=str(trace),
                                  determinant=str(determinant),
                                  determinant_of_identity_minus_matrix=str(determinant_of_complement)))
    return dict(kind='integer_normalization', order=order, square_root=square_root,
                n=n, sign_sum=sign_sum, sign_square_sum=square_sum,
                marked_coefficient=str(marked), full_row_energy=str(row_energy),
                off_mark_row_energy=str(bulk_row_energy), matrix_audits=matrix_audits)


def trajectory(order, square_root, sign, tau, steps, checkpoints, cutoffs, relaxation):
    n = len(sign)
    c = np.full(n, 4*tau)
    c[0] = 4*n
    x = np.zeros(n)
    d = relaxation*kernel_action(sign, np.sqrt(c))
    initial_energy = scalar(d @ d/n)
    maximum_identity_error = 0.
    maximum_averaged_identity_error = 0.
    maximum_recurrence_error = 0.
    maximum_two_step_violation = 0.
    previous = None
    for step in range(steps):
        y = x+d
        u, v = np.sqrt(x*x+c), np.sqrt(y*y+c)
        secant = (x+y)/(u+v)
        h = secant*d
        kh = kernel_action(sign, h)
        next_d = (1-relaxation)*d+relaxation*kh
        energy = scalar(d @ d)
        if energy < 1e-27*n:
            break
        activation_loss = scalar((d*d*(1-secant*secant)).sum())
        mean_loss = scalar(h.sum()**2/n)
        bulk_e = scalar(d[1:] @ d[1:])
        endpoint_moments = [scalar((d[1:]**2*z[1:]**2).sum()/bulk_e)
                            for z in (x, y)]
        amplitude = max(endpoint_moments)
        two_step = None
        if relaxation == 1 and previous is not None:
            rho = max(previous['amplitude'], amplitude)/(max(previous['amplitude'], amplitude)+4*tau)
            two_step = dict(start_step=step-1,
                            amplitude=max(previous['amplitude'], amplitude),
                            ratio_upper=root_transfer_rate(n, rho)
                            -(rho*previous['mean_loss']+mean_loss)/previous['energy'],
                            observed_ratio=scalar(next_d @ next_d)/previous['energy'])
            violation = two_step['observed_ratio']-two_step['ratio_upper']
            maximum_two_step_violation = max(maximum_two_step_violation, violation)
            if violation > 3e-12:
                raise RuntimeError('two-step root transfer bound failed')
        identity_error = abs(scalar(kh @ kh)+activation_loss+mean_loss-energy)/energy
        maximum_identity_error = max(maximum_identity_error, identity_error)
        averaged_error = abs(scalar(next_d @ next_d)
                             +relaxation*(activation_loss+mean_loss)
                             +relaxation*(1-relaxation)*scalar(np.linalg.norm(d-kh)**2)
                             -energy)/energy
        maximum_averaged_identity_error = max(maximum_averaged_identity_error, averaged_error)
        if max(identity_error, averaged_error) > 3e-12:
            raise RuntimeError('increment identity failed')
        if step in checkpoints:
            bulk_mx = np.maximum(x[1:]**2, y[1:]**2)
            tails = []
            for cutoff in sorted(set(cutoffs+[2*sqrt(tau), 4*sqrt(tau)])):
                high = bulk_mx > cutoff**2
                tails.append(dict(cutoff=cutoff,
                                  bulk_coordinate_fraction=scalar(high.mean()),
                                  bulk_increment_energy_fraction=scalar((d[1:][high]**2).sum()/bulk_e),
                                  bulk_weighted_amplitude_contribution=scalar((d[1:][high]**2*bulk_mx[high]).sum()/bulk_e)))
            next_energy = scalar(next_d @ next_d)
            record = dict(kind='trajectory', order=order, square_root=square_root,
                          tau=tau, relaxation=relaxation, step=step,
                          increment_energy=energy/n, initial_increment_energy=initial_energy,
                          increment_energy_ratio=next_energy/energy,
                          field_norm=scalar(np.linalg.norm(x)/sqrt(n)),
                          root_unscaled=scalar(x[0]/sqrt(n)),
                          root_increment_energy_fraction=scalar(d[0]**2/energy),
                          root_secant_squared=scalar(secant[0]**2),
                          bulk_endpoint_amplitude=amplitude,
                          bulk_maximum_endpoint_amplitude=scalar((d[1:]**2*bulk_mx).sum()/bulk_e),
                          bulk_rms=scalar(np.linalg.norm(x[1:])/sqrt(n-1)),
                          bulk_max=scalar(np.sqrt(bulk_mx.max())),
                          bulk_activation_loss=scalar((d[1:]**2*(1-secant[1:]**2)).sum()/energy),
                          bulk_effective_harmonic_amplitude=4*tau*(bulk_e/scalar((d[1:]**2*(1-secant[1:]**2)).sum())-1),
                          root_activation_loss=scalar(d[0]**2*(1-secant[0]**2)/energy),
                          mean_reserve=mean_loss/energy,
                          picard_energy_ratio=scalar(kh @ kh/energy),
                          averaging_reserve=scalar(relaxation*(1-relaxation)*np.linalg.norm(d-kh)**2/energy),
                          identity_relative_error=identity_error,
                          tails=tails)
            if two_step is not None:
                record['two_step'] = two_step
            bulk_bound = (bulk_e/energy)*record['bulk_endpoint_amplitude']/(record['bulk_endpoint_amplitude']+4*tau)
            full_bound = bulk_bound+record['root_increment_energy_fraction']*record['root_secant_squared']-record['mean_reserve']
            record['conditional_picard_ratio_upper'] = full_bound
            if record['picard_energy_ratio'] > full_bound+2e-12:
                raise RuntimeError('weighted conditional rate failed')
            # Independently recompute a direct iterate to detect incremental drift.
            direct_y = (1-relaxation)*x+relaxation*kernel_action(sign, u)
            recurrence_error = scalar(np.linalg.norm(direct_y-y)/sqrt(n))
            maximum_recurrence_error = max(maximum_recurrence_error, recurrence_error)
            record['direct_recurrence_rms_error'] = recurrence_error
            print(json.dumps(record), flush=True)
        previous = dict(energy=energy, mean_loss=mean_loss, amplitude=amplitude)
        x, d = y, next_d
    print(json.dumps(dict(kind='audit', order=order, square_root=square_root,
                          tau=tau, relaxation=relaxation, completed_steps=step+1,
                          maximum_identity_relative_error=maximum_identity_error,
                          maximum_averaged_identity_relative_error=maximum_averaged_identity_error,
                          maximum_direct_recurrence_rms_error=maximum_recurrence_error,
                          maximum_two_step_violation=maximum_two_step_violation)), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes', nargs='*', type=int, default=[9413, 153649, 1000033])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[97, 389])
    parser.add_argument('--tau', nargs='+', type=float, default=[.05])
    parser.add_argument('--steps', type=int, default=256)
    parser.add_argument('--relaxation', type=float, default=1.)
    parser.add_argument('--checkpoints', nargs='*', type=int,
                        default=[0, 1, 2, 4, 8, 16, 32, 64, 128, 255])
    parser.add_argument('--cutoffs', nargs='+', type=float, default=[.5, 1, 2, 4, 8, 16, 32, 64])
    parser.add_argument('--integer-audit', action='store_true',
                        help='report exact integer/Parseval marked-to-bulk normalizations only')
    args = parser.parse_args()
    if min(args.tau) <= 0 or not 0 < args.relaxation <= 1 or args.steps < 1:
        parser.error('use positive floors, depth, and relaxation at most one')
    for p in args.primes:
        sign = paley_sign(p)
        if args.integer_audit:
            print(json.dumps(integer_normalization(p, None, sign)), flush=True)
            continue
        for tau in args.tau:
            trajectory(p, None, sign, tau, args.steps, set(args.checkpoints),
                       args.cutoffs, args.relaxation)
    for p in args.square_roots:
        sign = square_field_sign(p)
        if args.integer_audit:
            print(json.dumps(integer_normalization(p*p, p, sign)), flush=True)
            continue
        for tau in args.tau:
            trajectory(p*p, p, sign, tau, args.steps, set(args.checkpoints),
                       args.cutoffs, args.relaxation)


if __name__ == '__main__':
    main()
