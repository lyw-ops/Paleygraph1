"""Certify the Jacobi-Laurent radius and four positive Picard steps."""
import json
from math import comb

from flint import arb, ctx

ctx.prec = 160
CUTOFF = 14
SEED = arb("2.82845", "0.00003")  # contains sqrt(8) and all eventual s_q
RHO = arb(1001) / 1000


def laurent(floor):
    """Taylor polynomial in the activation, expressed in cos(k theta) y^j."""
    size = 2 * CUTOFF + 1
    coefs = [[arb(0) for _ in range(size)] for _ in range(size)]
    scale = 2 * floor.sqrt()
    ratio = 1 / (4 * floor)
    weight = scale
    for ell in range(1, CUTOFF + 1):
        weight *= (arb(3) / 2 - ell) * ratio / ell
        arity = 2 * ell
        for j in range(arity + 1):
            seeds = arity - j
            common = weight * comb(arity, j) * (SEED / 2) ** seeds
            for v in range(seeds // 2 + 1):
                k = seeds - 2 * v
                coefs[j][k] += common * comb(seeds, v) * (2 if k else 1)
    return coefs


def coefficients(coefs, rho):
    return [sum((j+k) * abs(c) * rho**(1+k) for k, c in enumerate(row))
            for j, row in enumerate(coefs)]


def polynomial(coefs, value):
    result = arb(0)
    for c in reversed(coefs):
        result = result * value + c
    return result


def slab(index, divisions):
    return arb(arb(2*index+1)/(2*divisions), arb(1)/(2*divisions))


def activation_error(floor, bound, sharp):
    ratio = bound**2 / (4 * floor)
    assert ratio < 1
    if sharp:
        # Alternating Taylor terms with decreasing magnitudes on [0,1].
        coefficient = arb(1)
        for ell in range(1,CUTOFF+2):
            coefficient *= (arb(3)/2-ell)/ell
        return (2*floor.sqrt()*abs(coefficient)*ratio**(CUTOFF+1)).upper()
    return (2*floor.sqrt()*ratio**(CUTOFF+1)/(1-ratio)).upper()


def decay(first, last, divisions, radius, rho, cost_upper, rate):
    worst = arb(0)
    for index in range(first, last):
        floor = slab(index, divisions)
        low = polynomial(coefficients(laurent(floor), rho), radius)
        r = (rho*SEED+radius)**2/(4*floor)
        # Sum of 2*l*r^l. The first omitted term has l=CUTOFF+1.
        l = CUTOFF+1
        tail = 4*floor.sqrt()*rho*r**l*(l/(1-r)+r/(1-r)**2)
        worst = max(worst, (low+tail).upper())
    assert worst < cost_upper < radius
    assert (SEED+radius).upper() < arb(46)/10
    assert rho**rate > 8
    return dict(kind="laurent_decay", slab_indices=[first,last], divisions=divisions,
                cutoff=CUTOFF, rate_exponent=f"1/{rate}",
                cost_upper_millionths=int((cost_upper*1000000).unique_fmpz()))


def tolerance(first, prime, sharp=False):
    worst = arb(0)
    for index in range(first*8, 25*8):
        floor = slab(index, 8)
        coefs = coefficients(laurent(floor), arb(1))
        b = arb(0)
        old_err = arb(0)
        for j in range(1,5):
            v = (SEED+b).upper()
            b = polynomial(coefs, b).upper()
            next_v = (SEED+b).upper()
            err = activation_error(floor, v, sharp)
            if j == 1:
                sd = (arb(8001)/1000).sqrt() if prime else SEED.upper()**2/2
                diff = sd/(4*floor.sqrt()) + err
            else:
                diff = diff*v/(4*floor+v**2).sqrt()+old_err+err
            diff = diff.upper()
            old_err = err
        hmax = (4*floor+v*v).sqrt()
        bulk_min = ((2*floor.sqrt()-err)**2-next_v**2)/4
        assert bulk_min > 0 and 2*floor.sqrt() > err
        mag = ((v+next_v)*diff+(2*hmax+err)*err)/4
        bound = (mag/(floor.sqrt()+bulk_min.sqrt())).upper()
        if sharp:
            c = 2*floor.sqrt()
            assert next_v < c
            ratio = (v+next_v)/((c*c+v*v-next_v**2).sqrt()+c)
            trunc = (2*hmax+err)*err/(4*(bulk_min.sqrt()+(floor-next_v**2/4).sqrt()))
            distance = (diff*ratio/2+trunc).upper()
            bulk_norm = (floor.sqrt()+distance).upper()
            bound = (distance*bulk_norm/(1+bulk_norm**2).sqrt()).upper()
        worst = max(worst, bound)
    if sharp:
        ceiling = 170
    else:
        ceiling = 154 if prime else 146
    assert worst < arb(ceiling)/10000, str(worst)
    return dict(kind="four_picard_steps_sharp" if sharp else "four_picard_steps", family="primes" if prime else "primes_and_squares",
                floor=[first,25], slabs=(25-first)*8, cutoff=CUTOFF,
                actual_log_mark_limsup_upper=f"{ceiling}/10000")


if __name__ == "__main__":
    assert SEED.contains(arb(8).sqrt())
    for row in (
        decay(197*8, 25*64, 64, arb(174)/100, arb(10001)/10000, arb(17399)/10000, 21000),
        decay(25*16, 28*16, 16, arb(177)/100, RHO, arb(1766)/1000, 2100),
        tolerance(11, True), tolerance(12, False),
        tolerance(10, True, True), tolerance(11, False, True),
    ):
        print(json.dumps(row, sort_keys=True))
