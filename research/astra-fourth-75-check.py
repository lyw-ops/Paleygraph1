"""Arb enclosures for the exact marked complex Picard iterates."""
import json
from fractions import Fraction
from math import comb
import runpy
from pathlib import Path

from flint import acb, arb, ctx

source = Path(__file__).resolve().parent
domain = runpy.run_path(str(source / "marked-domain-53-check.py"))
hist = domain["histogram"]
warm = domain["warm"]
ctx.prec = 160
center = arb(2031) / 128


def rational_fourth():
    # The first two even powers are retained without sign cancellation.
    f = Fraction
    scale, seed, height = f(81,10), f(283,100), f(312,5)
    caps = [(56,116),(96,214),(135,321),(182,473)]
    b = c = f(0)
    for mass_cap, moment_cap in caps:
        mass = moment = f(1,10**5)  # mark and all lift errors in Q_1
        for ell, binomial in [(1,f(1,2)),(2,f(1,8))]:
            for j in range(2*ell+1):
                degree = 2*ell-j
                a = b**j
                variance = j*c*b**(j-1) if j else 0
                for v in range(degree//2+1):
                    k = degree-2*v
                    factor = scale*binomial/height**ell * comb(2*ell,j)
                    factor *= (seed/2)**degree * comb(degree,v) * (2 if k else 1)
                    price = (k+j)*a
                    if k:
                        price = min(price,k*a+variance/f(4*k))
                    mass += factor*price
                    moment += factor*(k*k*a+variance)
        ratio = (seed+b)**2/height
        assert ratio < 1
        geometric = 1/(1-ratio)
        first = 3*geometric + ratio*geometric**2
        second = 9*geometric + 7*ratio*geometric**2 + 2*ratio**2*geometric**3
        tail = scale*ratio**3/16
        mass += tail*2*first
        moment += tail*(4*second + 2*first*(c/b if b else 0))
        b,c = f(mass_cap,100),f(moment_cap,100)
        assert mass < b and moment < c
    assert seed+b == f(465,100)
    return dict(kind="ordinary_two_moment_rational_fourth_bound", disk_radius="1/4",
                input_n_min=10**14, price_pairs_hundredths=caps, fourth_upper="4.65")


def envelope(width, partitions):
    size = 2 * warm.CUTOFF + 1
    modes = [[arb(0) for _ in range(size)] for _ in range(size)]
    half = width / partitions
    # The negative imaginary half follows by complex conjugation.
    for u in range(partitions):
        real = arb(center - width + (2*u+1)*half, half)
        for v in range(partitions//2):
            imag = arb((2*v+1)*half, half)
            coeffs = domain["laurent"](acb(real, imag), True)
            for j, row in enumerate(coeffs):
                for k, value in enumerate(row):
                    modes[j][k] = max(modes[j][k], abs(value).upper())
    return modes


def physical_prefix(width_den, partitions, steps, fourth_millis, final_millis,
                    n_exponent, real_increment_units, real_scale):
    width = arb(1) / width_den
    modes = envelope(width, partitions)
    # An upper input for zero avoids a zero denominator in the tail bound.
    caps = [arb(0)] * (hist["N"] + 2)
    caps[0] = arb(1) / 10**12
    low = center - width
    high = center + 2*width
    seed = arb(2829) / 1000
    assert warm.SEED.upper() < seed
    assert warm.SEED.lower() < arb(8).sqrt()
    assert (8 + arb(4)/10**14).sqrt() < warm.SEED.upper()
    correction = arb(1) / 10**5
    # Per node, the coefficient sum is at most 2 sqrt(high) times
    # (2 - sqrt(1-r)), with r bounded using the full input radius five.
    assert 25/(4*low) < 1 and 4*high.sqrt() < 17
    assert (4*high+25).sqrt()+arb(25)/(2*10**7) < 11
    assert arb(3)/2*(2*17+11)/10**7 < correction
    complex_delta = real_delta = arb(0)
    for depth in range(1, steps+1):
        output, mass, energy = hist["histogram_step"](modes, caps, arb(1))
        remainder = hist["taylor_tail"](low, high, mass, energy, arb(1))
        output[-2] += remainder[0]
        output[-1] += remainder[1]
        output[0] += correction
        caps = [x.upper() for x in output]
        feedback = sum(k*v for k,v in enumerate(caps[:-2],1)) + caps[-2]
        radius = seed + feedback
        assert radius < 5
        if depth == 4:
            assert radius < arb(fourth_millis)/1000
        if depth == 1:
            complex_delta = real_delta = feedback
        if depth == steps:
            assert radius < arb(final_millis) / 1000
            assert complex_delta * arb(10**n_exponent).sqrt() < arb(1)/4
            assert real_delta < arb(real_increment_units) / (10**real_scale)
            break
        # For the next increment the segment must include both adjacent inputs.
        # Take running maxima to avoid relying on monotonicity of rounded caps.
        if depth == 1:
            hull_feedback = feedback
        else:
            hull_feedback = max(hull_feedback, feedback)
        hull = seed + hull_feedback
        complex_delta *= hull/(4*low - 2*hull_feedback**2 + hull**2).sqrt()
        real_delta *= hull/(4*low+hull**2).sqrt()
    # For the final segment also allow a counting ball of radius one half.
    assert feedback < arb(22)/10
    assert hull_feedback < arb(22)/10
    # A segment from V_(j-1) to V_j has imaginary part at most 2.2,
    # and adding the counting ball about V_j raises this to 2.7.
    assert arb(55)/10/(4*low-2*(arb(27)/10)**2+(arb(55)/10)**2).sqrt() < arb(2)/3
    return dict(kind="actual_marked_picard_prefix_and_finite_disk_closure",
                disk_radius=f"1/{width_den}", complex_box_partitions=partitions,
                precision_bits=ctx.prec, steps=steps, all_site_cap=5,
                fourth_millis_upper=fourth_millis, final_millis_upper=final_millis,
                stationary_n_range=[10**14,10**n_exponent],
                final_real_normalized_increment_upper=f"{real_increment_units}e-{real_scale}")


# Frozen from numerical fits. Only these integers are used by the invariant proof.
WIDE_CAPS = [
    24295000000001,10414747497833,5511630198111,2746410827462,1464891024787,
    711435013316,335605337015,163938015791,82209288052,42076472618,21891387480,
    11543539363,6155617323,3313811623,1798549833,983075412,540678997,298996437,
    166151412,92732602,51959279,29216936,16481914,9325254,5290388,3008809,
    1715139,979778,560808,321588,184728,106283,61242,35339,20419,11813,6843,
    3968,2304,1339,779,454,265,154,90,53,31,18,11,6,
]
LEFT_CAPS = [
    24295000000001,10414747184163,5511632121200,2746412275992,1464891943980,
    711435569969,335605654491,163938196725,82209391471,42076531908,21891421574,
    11543559024,6155628689,3313818210,1798553659,983077639,540680295,298997195,
    166151856,92732861,51959431,29217025,16481966,9325285,5290406,3008820,1715145,
    979782,560810,321590,184729,106283,61242,35339,20419,11813,6843,3968,2304,
    1339,779,454,265,154,90,53,31,18,11,6,
]


def stationary_rectangle(kernel, first, width_den, caps, leak_billionths):
    # Horizontal units are 1/2^20; take adjoining closed slabs.
    last = 16640308
    rows = None
    pars = [arb(0)]*7
    for i in range(first, last):
        t = acb(arb(2*i+1,1)/2**21, arb(0,1)/width_den)
        new, current = kernel["upper"](t)
        rows = new if rows is None else [
            [max(x,y) for x,y in zip(old,add)] for old,add in zip(rows,new)
        ]
        pars = [max(x,y) for x,y in zip(pars,current)]
    a,b,c,d,z,w,v = pars
    eps = arb(1)/10**7
    lower = arb(first)/2**20
    leak, coord = kernel["joint"]["cap_invariant"](
        lower, arb(last)/2**20, width_den, rows, [a,b,c,d,z,w+v], caps, eps)
    assert leak < arb(leak_billionths)/10**9 < eps
    assert coord < arb(4654)/1000
    assert coord/(4*lower-coord**2).sqrt() < arb(3)/4
    return dict(kind="physical_nine_center_stationary_rectangle", precision_bits=ctx.prec,
                real_numerators=[first,last], denominator=2**20, slabs=last-first,
                imaginary_half_width=f"1/{width_den}", weighted_excess_billionths_upper=leak_billionths,
                residual_budget="1e-7", coordinate_upper="4.654", mark_upper="3/sqrt(n)")


if __name__ == "__main__":
    print(json.dumps(rational_fourth(),sort_keys=True),flush=True)
    for params in [(4,8,30,3938,4960,16,4,10), (128,2,64,3911,4977,36,14,21)]:
        print(json.dumps(physical_prefix(*params),sort_keys=True),flush=True)
    kernel = runpy.run_path(str(source / "astra-joint-65-check.py"))
    ctx.prec = 192
    for params in [(16640296,1024,WIDE_CAPS,81), (16640292,2048,LEFT_CAPS,98)]:
        print(json.dumps(stationary_rectangle(kernel,*params),sort_keys=True),flush=True)
