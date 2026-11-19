"""Replay the mass- and root-preserving source construction of Round 28.

Finite-field masks and run/order tests are exact integers. Stationary solves,
Fourier transforms, and inequality checks are floating-point diagnostics, not
interval certificates. All output goes to stdout; no other files are modified.
"""

import argparse
import json
from math import gcd, sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import kernel_action, smoothing
from square_control import square_field_sign
from theta import paley_sign


def norm(x):
    return float(np.linalg.norm(x))


def longest_run(sign, maximum=128):
    n = len(sign)
    candidates = np.arange(1, n, dtype=np.int64)
    orders = n // np.gcd(candidates, n)
    best = None
    for length in range(1, maximum + 1):
        keep = (sign[(length*candidates) % n] == 1) & (orders > 2*length)
        candidates, orders = candidates[keep], orders[keep]
        if not len(candidates):
            break
        best = length, int(candidates[0])
    if best is None:
        raise ValueError('no plus run of order greater than two')
    return best


def fejer(sign):
    n = len(sign)
    length, step = longest_run(sign)
    modes = np.zeros(n)
    modes[0] = 1
    for j in range(1, length+1):
        assert sign[(j*step) % n] == 1
        assert sign[(-j*step) % n] == 1
        modes[(j*step) % n] = 1-j/(length+1)
        modes[(-j*step) % n] = 1-j/(length+1)
    h = n*np.fft.ifft(modes).real
    exact_norm_squared_over_n = (2*(length+1)**2+1)/(3*(length+1))
    assert abs(np.dot(h, h)/n-exact_norm_squared_over_n) < 1e-10
    if n < 200:
        roots = np.exp(2j*np.pi*step*np.arange(n)/n)
        independent = abs(sum(roots**j for j in range(length+1)))**2/(length+1)
        assert norm(h-independent) < 1e-10
    return h, dict(profile='fejer', degree=length, step=step,
                   step_order=n//gcd(step, n), height_bound=length+1)


def choose_even_translate(h, u):
    # Each translate has mean one. Thus the minimum pairing is <= sum(u).
    correlations = np.fft.ifft(np.fft.fft(u)*np.conj(np.fft.fft(h))).real
    even_correlations = (correlations+correlations[(-np.arange(len(h))) % len(h)])/2
    shift = int(np.argmin(even_correlations))
    translated = (np.roll(h, shift)+np.roll(h, -shift))/2
    assert np.dot(translated, u) <= u.sum()+1e-8
    return translated, shift


def check_case(order, root, tau, tolerance, maximum):
    sign = paley_sign(order) if root is None else square_field_sign(root)
    n = len(sign)
    a = np.full(n, 2*sqrt(tau/n))
    a[0] = 2
    a2 = a*a
    W = float(a2.sum()/4)
    M = 2*sqrt(n*W)
    G = M-a.sum()
    f = kernel_action(sign, a)
    vp, metrics = smoothing(sign, tau, tolerance, maximum)
    u = np.sqrt(vp*vp+a2)
    g = vp*vp/(u+a)
    # Enforce the linear equation in the diagnostic base; retain its measured
    # nonlinear defect instead of labelling a numerical solve an exact point.
    v = kernel_action(sign, u)
    q_base = u*u-v*v-a2
    assert norm(v-vp) <= 2*tolerance
    base_mass_error = float(u.sum()-M)
    profiles = [fejer(sign)]
    if root is not None:
        h = np.zeros(n)
        h[::root-1] = root-1
        profiles.append((h, dict(profile='square_subfield', height_bound=root-1,
                                  subgroup_size=(root+1)//2)))
    results = []
    for raw, info in profiles:
        h, shift = choose_even_translate(raw, u)
        H = info['height_bound']
        assert h.min() > -1e-10
        assert norm(kernel_action(sign, h)-(h-1)) < 1e-8
        assert h.max() <= H+1e-10
        c = (G-g[0])/(n-h[0])
        assert c > 0
        seed = c*h
        seed[0] = g[0]
        e = a.copy()
        e[0] += g[0]-c*h[0]
        z = kernel_action(sign, e)
        U = a+seed
        V = kernel_action(sign, U)
        q_seed = U*U-V*V-a2
        B = u*e-v*z-a2+c*v
        cross = B+c*h*(u-v)
        C1 = float(np.abs(B).sum()+c*np.dot(h, u-v))
        C2 = float(np.abs(q_seed).sum())
        lower_distance2 = c*c*(np.dot(h, h)-h[0]**2)-2*c*M
        rows = []
        for delta in (.5, .25, .125, .0625):
            candidate = (1-delta)*g+delta*seed
            uu = a+candidate
            vv = kernel_action(sign, uu)
            q = uu*uu-vv*vv-a2
            q_formula = ((1-delta)**2*q_base+delta**2*q_seed
                         +2*delta*(1-delta)*cross)
            source_residual = np.sqrt(vv*vv+a2)-uu
            transformed = source_residual-source_residual.mean()
            sorted_bulk = np.sort(transformed[1:])[::-1]
            top_indices = [min(n-1, int(np.ceil(scale*sqrt(n)))) for scale in (1, 2)]
            seed_column_scale = float(abs(e[0]-a[1]))
            bulk_upper = delta*(seed_column_scale*sqrt(order)/n+c)
            base_coordinate_error = float(np.max(abs(v-vp)))
            assert np.max(source_residual[1:]) <= (
                bulk_upper+(1-delta)*base_coordinate_error+1e-9)
            assert norm(transformed+kernel_action(
                sign, vv-kernel_action(sign, np.sqrt(vv*vv+a2)))) < 1e-9
            forced_error = norm(vv-f-kernel_action(sign, candidate))
            mass_error = float(candidate.sum()-G)
            reciprocity_l1 = float(np.abs(q).sum())
            bound = ((1-delta)**2*np.abs(q_base).sum()
                     +2*delta*(1-delta)*C1+delta**2*C2)
            distance = norm(candidate-g)
            x, y = (uu+vv)/2, (uu-vv)/2
            negative_energy = float(np.dot(np.minimum(x, 0), np.minimum(x, 0))
                                    +np.dot(np.minimum(y, 0), np.minimum(y, 0)))
            assert norm(q-q_formula) < 1e-8
            assert forced_error < 1e-9
            assert candidate.min() > -1e-10
            assert candidate[0] == g[0]
            assert reciprocity_l1 <= bound+1e-8
            assert norm(source_residual)**2 <= reciprocity_l1+1e-9
            assert distance**2 >= delta**2*lower_distance2-1e-8
            assert negative_energy <= reciprocity_l1/4+1e-9
            # The exact identity uses the actually computed mass, avoiding a
            # false exact-stationarity assertion about the numerical base.
            assert abs(q.sum()-(uu.sum()**2/n-a2.sum())) < 1e-8
            rows.append(dict(delta=delta, source_norm=norm(candidate),
                             source_distance=distance, distance_lower_squared=
                             max(0., delta**2*lower_distance2),
                             source_residual=norm(source_residual),
                             reciprocity_l1=reciprocity_l1, defect_upper=bound,
                             forced_equation_error=forced_error,
                             exact_mass_target_error=mass_error,
                             quadratic_defect_sum=float(q.sum()),
                             root_source_error=float(candidate[0]-g[0]),
                             root_state_change=float(vv[0]-v[0]),
                             opposite_row_negative_energy=negative_energy,
                             minimum_row_entry=float(min(x.min(), y.min())),
                             max_relative_product_error=float(np.max(abs(q)/a2)),
                             centered_bulk_upper_scaled_over_delta=
                             float(sqrt(n)*transformed[1:].max()/delta),
                             centered_root_over_delta=float(transformed[0]/delta),
                             mass_scalar_over_delta=float((
                                 2*sqrt(W/n)*np.sqrt(vv*vv+a2).sum()-4*W)/delta),
                             signed_top_sums=[dict(count=k,
                                 top_over_delta=float(sorted_bulk[:k].sum()/delta))
                                 for k in top_indices]))
        results.append(dict(**info, shift=shift, paired_mean=float(np.dot(h, u)/M),
                            h_root=float(h[0]), c=c, c_height=c*H,
                            C1=C1, C2=C2, rows=rows))
    return dict(kind='floating_diagnostic', order=order, square_root=root, tau=tau,
                steps=metrics[-1], base_residual=norm(v-vp),
                base_source_norm=norm(g), base_root=float(v[0]),
                base_mass_error=base_mass_error,
                base_reciprocity_l1=float(np.abs(q_base).sum()), profiles=results)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', nargs='*', type=int, default=[97, 9413, 153649])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[7, 97])
    parser.add_argument('--tau', type=float, default=.05)
    parser.add_argument('--tolerance', type=float, default=2e-12)
    parser.add_argument('--max-steps', type=int, default=20000)
    args = parser.parse_args()
    if args.tau <= 0 or args.tolerance <= 0:
        parser.error('tau and tolerance must be positive')
    for q, r in [(p, None) for p in args.primes]+[(r*r, r) for r in args.square_roots]:
        print(json.dumps(check_case(q, r, args.tau, args.tolerance, args.max_steps)), flush=True)


if __name__ == '__main__':
    main()
