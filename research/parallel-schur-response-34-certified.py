"""Arb finite actual-Paley HR certificates using a continuous threshold cover.

Run with -B. Only stdout is written. All acceptances use Arb comparisons;
floating point selects rational centers and proposed interval lengths only.
"""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from flint import acb, arb, ctx, fmpq
from poisson_weights import weighted_iterate
from theta import paley_sign


def exact_float(x):
    return arb(fmpq(*float(x).as_integer_ratio()))


def upper(x):
    return str(x.upper())


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def even_transform(sign, x, side=None):
    n = len(sign)
    f = acb.dft([acb(z) for z in x])
    mult = sign if side is None else [int(s == -side) for s in sign]
    return [(z/n).real for z in acb.dft([mult[j]*f[j] for j in range(n)])]


def certify(prime, tau_string, radius_string, target_string, max_steps):
    started = time.monotonic()
    signs = paley_sign(prime).astype(int).tolist()
    n = len(signs)
    assert signs[0] == 0 and sum(signs) == -1
    assert all(signs[j] == signs[-j % n] for j in range(n))
    tau, radius, target = arb(tau_string), arb(radius_string), arb(target_string)
    c = tau/n
    W = 1+(n-1)*c
    a, na = (W/n).sqrt(), (n*W).sqrt()
    weights = [arb(1)]+[c]*(n-1)
    vector, _, raw_residual = weighted_iterate(
        np.array(signs), np.array([float(w) for w in weights]),
        tolerance=1e-14, rounds=128)
    vector = (vector+vector[(-np.arange(n)) % n])/2
    center = [exact_float(z) for z in vector]
    phi = [(z*z+4*w).sqrt() for z, w in zip(center, weights)]
    applied = even_transform(signs, phi)
    epsilon = sum(((z-v)**2 for z, v in zip(applied, center)), arb(0)).sqrt()
    lipschitz = max(((abs(z)+radius)/((abs(z)+radius)**2+4*w).sqrt()).upper()
                    for z, w in zip(center, weights))
    margin = (1-lipschitz)*radius-epsilon
    assert lipschitz < 1 and margin > 0, (prime, epsilon, lipschitz, margin)
    emit(dict(kind="rigorous_stationary_enclosure", p=prime, n=n,
              tau=tau_string, bits=ctx.prec, radius_l2=radius_string,
              residual_norm_upper=upper(epsilon), L_upper=upper(lipschitz),
              banach_margin_lower=str(margin.lower()), certified=True))

    for side in (1, -1):
        calc_A = [(ph+side*z)/2 for ph, z in zip(phi, center)]
        Ahat = [exact_float(float(z.mid())) for z in calc_A]
        rounding_l2 = sum(((z-v)**2 for z, v in zip(calc_A, Ahat)), arb(0)).sqrt()
        rA = (radius+rounding_l2).upper()
        assert all(Ahat[j] == Ahat[-j % n] for j in range(n))
        assert all(z-rA > 0 for z in Ahat)
        d_up = [(c/(a*(z-rA))).upper() for z in Ahat]
        dmax = max(d_up)
        mass_error = ((n-1)*rA*rA).sqrt()
        norm_error = dmax.sqrt()*rA
        maximum_A = max((z+rA).upper() for z in Ahat[1:])
        left = arb(0)
        intervals = 0
        maximum_cover_ratio = arb(0)
        maximum_anchor_ratio = arb(0)
        minimum_interval_width = None

        while True:
            assert left.is_exact(), "threshold anchors must be exact dyadic rationals"
            # Every t >= left obeys h_t <= (maximum_A-left)_+ pointwise.
            terminal_ratio = na*dmax*max(maximum_A-left, arb(0))
            if terminal_ratio < target:
                break
            assert intervals < max_steps, (prime, side, intervals, left)
            hhat = [arb(0)]+[max(z-left, arb(0)) for z in Ahat[1:]]
            zhat = even_transform(signs, hhat, side=side)
            H_upper = (sum((d*z*z for d, z in zip(d_up, zhat)), arb(0)).sqrt()
                       + norm_error).upper()
            mass_lower = (sum(hhat, arb(0))-mass_error).lower()
            gap = target*mass_lower-na*H_upper*H_upper
            assert gap > 0, (prime, side, left, gap)
            anchor_ratio = (na*H_upper*H_upper/mass_lower).upper()
            maximum_anchor_ratio = max(maximum_anchor_ratio, anchor_ratio)
            # Certified upper bound on the exact active count at the left anchor.
            active = sum(not (z+rA <= left) for z in Ahat[1:])
            assert active > 0
            L = (dmax*active).sqrt()
            # Float proposes an exact rational step. Arb verifies the whole interval.
            aa = float(na*L*L)
            bb = float(2*na*H_upper*L+target*active)
            gg = float(gap)
            proposed = 0.8*2*gg/(bb+sqrt(bb*bb+4*aa*gg))
            step = exact_float(proposed)
            assert step > 0
            while True:
                denominator = target*(mass_lower-active*step)
                numerator = na*(H_upper+L*step)**2
                if denominator > 0 and numerator < denominator:
                    break
                step /= 2
            ratio = (numerator/(mass_lower-active*step)).upper()
            maximum_cover_ratio = max(maximum_cover_ratio, ratio)
            minimum_interval_width = (step if minimum_interval_width is None
                                      else min(minimum_interval_width, step))
            left += step
            intervals += 1

        emit(dict(kind="rigorous_continuous_all_threshold_HR", p=prime, n=n,
                  tau=tau_string, side=side, C=target_string,
                  certified_intervals=intervals,
                  maximum_cover_ratio_upper=upper(maximum_cover_ratio),
                  all_threshold_ratio_upper=upper(max(maximum_cover_ratio, terminal_ratio)),
                  maximum_anchor_ratio_upper=upper(maximum_anchor_ratio),
                  terminal_ratio_upper=upper(terminal_ratio),
                  terminal_normalized_threshold_upper=upper(left/a),
                  coordinate_and_l2_radius_upper=upper(rA),
                  certified_dmax_upper=upper(dmax),
                  minimum_physical_interval_width_lower=str(minimum_interval_width.lower()),
                  all_R_ge_zero_certified=True,
                  scope="finite exact stationary pair; no prime-uniform assertion"))
    emit(dict(kind="finite_prime_completed", p=prime, tau=tau_string,
              elapsed_seconds=round(time.monotonic()-started, 3)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="+", default=[4001, 10009])
    parser.add_argument("--tau", default="0.01")
    parser.add_argument("--radius", default="1e-8")
    parser.add_argument("--C", default="1")
    parser.add_argument("--bits", type=int, default=128)
    parser.add_argument("--max-steps", type=int, default=10000)
    args = parser.parse_args()
    ctx.prec = args.bits
    for p in args.primes:
        certify(p, args.tau, args.radius, args.C, args.max_steps)
    emit(dict(kind="all_checks_passed", primes=args.primes, tau=args.tau,
              arithmetic="Arb outward-rounded balls; exact Paley multipliers",
              all_thresholds=True))
