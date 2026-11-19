"""Outward checks of a uniform second-mean bound and true Picard mean deficits."""

import argparse
import hashlib
import json
from pathlib import Path
import runpy

import numpy as np
from flint import arb, ctx

helper = runpy.run_path(str(Path(__file__).with_name("true-spill-63-check.py")))
transform = helper["transform"]
upper_norm = helper["upper_norm"]
kernel_action = helper["kernel_action"]
paley_sign = helper["paley_sign"]
square_field_sign = helper["square_field_sign"]


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def compact_mean():
    r = arb(2).sqrt()
    m = 2 * r / arb.pi()
    a = 1 / (arb.pi() * r)
    b = a / 24
    upper_coefficient = arb(1) / 200
    lower_coefficient = arb(1) / 500

    upper_at_r = m + 2*a + 4*b + 8*upper_coefficient
    upper_first_at_r = r * (2*a + 8*b + 24*upper_coefficient)
    upper_second_at_r = 2*a + 24*b + 120*upper_coefficient
    margin_inside = upper_at_r-r
    margin_outside = margin_inside - (1-upper_first_at_r).max(arb(0))**2 / (2*upper_second_at_r)
    assert margin_inside > 0 and margin_outside > arb(1)/100
    lower_at_r = m + 2*a + 4*b - 8*lower_coefficient
    linear_max = 8*a/5 * (2*a/(15*lower_coefficient)).sqrt().sqrt()
    cubic_root = (4*b/(5*lower_coefficient)).sqrt()
    cubic_max = 8*b/5 * cubic_root**3
    assert r-lower_at_r > 0 and linear_max+cubic_max < 1

    variance = 1-m*m
    fourth = 3*variance**2 - (2*m/3)**4/8
    sixth_cap = 15*variance**3
    base = m+a*variance+b*fourth
    lower = base-lower_coefficient*sixth_cap
    upper = base+upper_coefficient*sixth_cap
    p2_lower = (1-m)**2+(1-upper)**2
    p2_upper = (1-m)**2+(1-lower)**2
    assert lower > arb(94360)/100000 and upper < arb(94433)/100000
    assert p2_lower > arb(13037)/10**6 and p2_upper < arb(13118)/10**6
    emit(kind="common_second_mean_and_first_two_squared_mean_deficits",
         precision=ctx.prec, sixth_moment_upper=str(sixth_cap.upper()),
         mean2_lower=str(lower.lower()), mean2_upper=str(upper.upper()),
         squared_deficit_lower=str(p2_lower.lower()), squared_deficit_upper=str(p2_upper.upper()))


def exact_fixed_reference():
    face = runpy.run_path(str(Path(__file__).with_name("astra-face-54-check.py")))
    plus, minus = face["faces"]()
    root = arb(face["n"]).sqrt()
    return [root * (p[0]-m) for p, m in zip(plus, minus)]


def prefix(order, square_root, depths, reference=None):
    signs = square_field_sign(square_root) if square_root else paley_sign(order)
    sign = list(map(int, signs))
    n = len(sign)
    assert sign[0] == 0 and sign[1:] == sign[:0:-1]
    assert sum(sign) == -1 and n == (order-1)//2
    root = arb(n).sqrt()
    scale = 2**60
    reflect = np.r_[0, np.arange(n-1, 0, -1)]
    state = [arb(0)] * n
    error = arb(0)
    p_sum = arb(0)
    digest = hashlib.sha256(np.zeros(n, dtype="<i8").tobytes())
    old = {}
    for t in range(max(depths)+1):
        phi = [(state[0]**2+4).sqrt()] + [abs(v) for v in state[1:]]
        g = sum(phi, arb(0))/(2*root)+arb(0, (error/2).upper())
        image = transform(sign, phi)
        if t:
            p_sum += abs(1-g)**2
        if t in depths:
            center_norm = upper_norm(image)
            energy_upper = (center_norm+error)**2
            energy_lower = max(arb(0), (sum(abs(x).lower()**2 for x in image).sqrt()-error).lower())**2
            record = dict(kind="true_zero_floor_mean_deficits_and_next_energy",
                          field=order, square_root=square_root, depth=t,
                          precision=ctx.prec, prefix_sha256=digest.hexdigest(),
                          state_error_upper=str(error), mean=str(g), p_sum=str(p_sum),
                          next_energy_lower=str(energy_lower.lower()),
                          next_energy_upper=str(energy_upper.upper()))
            if t == 16:
                old[t] = p_sum
            if order == 9413 and t == 512:
                assert arb(1154)/10**5 < p_sum < arb(1155)/10**5
                assert p_sum-old[16] < arb(1)/10**4
                assert energy_upper < 6
            if order == 9409 and t == 512:
                assert arb(1165)/1000 < p_sum < arb(1166)/1000
                assert energy_lower > 96
            if reference is not None and t == max(depths):
                tail = ((upper_norm([a-b for a,b in zip(image,reference)])+error)**2/4).upper()
                assert p_sum > arb(972)/10**5 and p_sum+tail < arb(103)/10**4
                record.update(tail_bound_after_depth=str(tail),
                              infinite_deficit_upper=str((p_sum+tail).upper()),
                              reference="actual_complementary_optima")
            emit(**record)
        if t < max(depths):
            next_state = kernel_action(signs, np.array([float(v.mid()) for v in phi]))
            next_state = (next_state+next_state[reflect])/2
            points = [round(float(v)*scale) for v in next_state]
            assert points[1:] == points[:0:-1]
            state = [arb(v)/scale for v in points]
            error = (error+upper_norm([a-b for a,b in zip(image,state)])).upper()
            digest.update(np.asarray(points, dtype="<i8").tobytes())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", choices=("all","compact","prime","square","tail"), default="all")
    args = parser.parse_args()
    ctx.prec = 128
    if args.part in ("all","compact"):
        compact_mean()
    if args.part in ("all","prime"):
        prefix(9413, None, (2,16,64,128,256,512))
    if args.part in ("all","square"):
        prefix(9409, 97, (2,16,64,128,256,512))
    if args.part in ("all","tail"):
        prefix(97, None, (512,), exact_fixed_reference())
