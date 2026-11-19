"""Certify simultaneous generic-rank and Mellin second-moment radii."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json

from flint import arb

spec = spec_from_file_location("warm51", Path(__file__).with_name("astra-warm-51-check.py"))
warm = module_from_spec(spec)
spec.loader.exec_module(warm)


def polynomial_cost(coefficients, b, c, rho):
    mass = [b**j for j in range(len(coefficients))]
    rank = arb(0)
    second = arb(0)
    coarse = arb(0)
    for j, row in enumerate(coefficients):
        variance = j*c*mass[j-1] if j else arb(0)
        for k, coefficient in enumerate(row):
            if coefficient == 0 or j+k == 0:
                continue
            weight = abs(coefficient) * rho**(k+1)
            energy = k*k*mass[j]+variance
            cap = min(((k+j)*mass[j]).upper(), (mass[j]*energy).sqrt().upper())
            if k:
                cap = min(cap, (k*mass[j]+variance/(4*k)).upper())
            rank += weight*cap
            second += weight*energy
            coarse += abs(coefficient)*(arb(1)/2)**(k+1)*(j+k)*mass[j]
    return rank, second, coarse


def cost(floor, b, c, rho):
    rank, second, coarse = polynomial_cost(warm.laurent(floor), b, c, rho)
    # All omitted even Taylor powers have Laurent l1 coefficient mass <= one
    # before the seed and feedback radii are inserted.
    ratio = (warm.SEED*rho+b)**2/(4*floor)
    assert ratio < 1
    ell = warm.CUTOFF+1
    geom = 1/(1-ratio)
    first = ell*geom+ratio*geom**2
    square = ell*ell*geom+(2*ell+1)*ratio*geom**2+2*ratio**2*geom**3
    tail = 2*floor.sqrt()*rho*ratio**ell
    return (rank+tail*2*first, second+tail*(4*square+2*first*c/b),
            coarse+tail*2*first)


def certify(low, high, div, b, c, rho, bounds):
    worst = [arb(0)]*3
    for index in range(low,high):
        floor = warm.slab(index,div)
        for i, val in enumerate(cost(floor,b,c,rho)):
            worst[i] = max(worst[i], val.upper())
    assert all(x < y for x,y in zip(worst,bounds)), str(worst)
    assert bounds[0] < b and bounds[1] < c and bounds[2] < b
    return dict(kind="mellin_second_moment_ball", divisions=div, indices=[low,high],
                b_thousandths=int((b*1000).unique_fmpz()),
                c_thousandths=int((c*1000).unique_fmpz()),
                rho_millionths=int((rho*1000000).unique_fmpz()),
                cap_thousandths=[int((x*1000).unique_fmpz()) for x in bounds])



def prefix(first, last, div, prime):
    worst = arb(0)
    for index in range(first,last):
        floor = warm.slab(index,div)
        coefficients = warm.laurent(floor)
        b = c = old_error = arb(0)
        seed_variance = sum(x*x for x in coefficients[0][1:])/2
        for step in range(4):
            v = (warm.SEED+b).upper()
            b,c,_ = polynomial_cost(coefficients,b,c,arb(1))
            b,c = b.upper(),c.upper()
            next_v = (warm.SEED+b).upper()
            error = warm.activation_error(floor,v,True)
            if step == 0:
                if prime:
                    difference = seed_variance.sqrt().upper()
                else:
                    difference = ((4*floor+warm.SEED**2).sqrt()-2*floor.sqrt())/2+error
            else:
                difference = difference*v/(4*floor+v*v).sqrt()+error+old_error
            difference = difference.upper()
            old_error = error
        height = 2*floor.sqrt()
        assert next_v < height-error
        lower = ((height-error)**2-next_v**2)/4
        ratio = (v+next_v)/((height**2+v*v-next_v**2).sqrt()+height)
        trunc = (2*(4*floor+v*v).sqrt()+error)*error/(4*(lower.sqrt()+(floor-next_v**2/4).sqrt()))
        distance = (difference*ratio/2+trunc).upper()
        norm = (floor.sqrt()+distance).upper()
        worst = max(worst,(distance*norm/(1+norm**2).sqrt()).upper())
    assert worst < arb(17)/1000, str(worst)
    return dict(kind="positive_four_step_prefix", family="primes" if prime else "primes_and_squares",
                divisions=div, indices=[first,last], actual_mark_limsup_upper="17/1000")


if __name__ == "__main__":
    for low, high, div, b, c, rho, caps, exponent in (
        (2320,2336,128,1740,3700,1000200,[1739,3688,523],28000),
        (1168,1216,64,1700,3620,1001000,[1698,3598,506],5600),
        (304,394,16,1650,3490,1005000,[1631,3439,479],1200),
    ):
        radius = arb(rho)/1000000
        assert radius**exponent > 256
        record = certify(low, high, div, arb(b)/1000, arb(c)/1000, radius,
                         [arb(x)/1000 for x in caps])
        print(json.dumps(dict(record, power_denominator=exponent), sort_keys=True))

    for row in (prefix(564,640,64,True), prefix(632,704,64,False)):
        print(json.dumps(row,sort_keys=True))
