"""Certify an invariant for the pooled Jordan-weight distribution."""
import importlib.util
import json
from math import comb
from pathlib import Path

from flint import arb, arb_poly, ctx

spec = importlib.util.spec_from_file_location("warm51", Path(__file__).with_name("astra-warm-51-check.py"))
warm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(warm)
ctx.prec = 160
N = 16
DEGREE = 2 * warm.CUTOFF
RHO = arb(10003) / 10000
CAPS = [3190382711,3432668322,811485794,272135872,102438357,41533235,
        17675127,7787798,3522035,1625539,762536,362454,174097,84165,
        40457,17941,18568977,47733168]


def coefficient_envelope(start, stop, divisions):
    modes = [[arb(0) for _ in range(DEGREE+1)] for _ in range(DEGREE+1)]
    for index in range(start,stop):
        for j,row in enumerate(warm.laurent(warm.slab(index,divisions))):
            for k,value in enumerate(row):
                modes[j][k] = max(modes[j][k],abs(value).upper())
    return modes


def histogram_step(modes, caps, rho):
    hist = caps[:-2]
    u, v = caps[-2:]
    b = sum(k*h for k,h in enumerate(hist,1))
    c = sum(k*k*h for k,h in enumerate(hist,1))
    zero = b-sum(hist)
    sides = [h/2 for h in hist]
    base = arb_poly(sides[::-1]+[zero]+sides)
    power = arb_poly([1])
    core_b, core_c = arb(1), arb(0)
    remainder_b = remainder_c = arb(0)
    result = [arb(0) for _ in caps]
    for j,row in enumerate(modes):
        if j:
            remainder_b,remainder_c = (
                remainder_b*(b+u)+core_b*u,
                remainder_c*(b+u)+remainder_b*(c+v)+core_c*u+core_b*v)
            core_b,core_c = core_b*b, core_c*b+core_b*c
            power *= base
        weighted = [row[k]*rho**(k+1) for k in range(len(modes)-j)]
        side = [a/2 for a in weighted[1:]]
        offset = j*N+len(side)
        pooled = power * arb_poly(side[::-1]+[weighted[0]]+side)
        for i in range(offset+1,len(pooled)):
            k = i-offset
            packet = 2*pooled[i]
            if k <= N:
                result[k-1] += packet
            else:
                result[-2] += k*packet
                result[-1] += k*k*packet
        for k,weight in enumerate(weighted):
            if weight == 0:
                continue
            energy = k*k*remainder_b+remainder_c
            cap = min(((j+k)*remainder_b).upper(),(remainder_b*energy).sqrt().upper())
            if k:
                cap = min(cap,(k*remainder_b+remainder_c/(4*k)).upper())
            result[-2] += weight*cap
            result[-1] += weight*energy
    return result,b+u,c+v


def taylor_tail(low, high, mass, energy, rho):
    ratio = (warm.SEED*rho+mass)**2/(4*low)
    assert ratio < 1
    ell = warm.CUTOFF+1
    choose = arb(1)
    for i in range(1,ell+1):
        choose *= (arb(3)/2-i)/i
    geom = 1/(1-ratio)
    first = ell*geom+ratio*geom**2
    square = ell**2*geom+(2*ell+1)*ratio*geom**2+2*ratio**2*geom**3
    scale = 2*high.sqrt()*rho*abs(choose)*ratio**ell
    return scale*2*first, scale*(4*square+2*first*energy/mass)


def certify():
    divisions = 128
    start,stop = 2112,2320
    low,high = arb(start)/divisions,arb(stop)/divisions
    modes = coefficient_envelope(start,stop,divisions)
    caps = [arb(v)/10**10 for v in CAPS]
    output,mass,energy = histogram_step(modes,caps,RHO)
    tail1,tail2 = taylor_tail(low,high,mass,energy,RHO)
    output[-2] += tail1
    output[-1] += tail2
    assert all(a < arb(999)*b/1000 for a,b in zip(output,caps)), [float(a/b) for a,b in zip(output,caps)]
    coarse = sum((j+k)*val*(arb(1)/2)**(k+1)*mass**j
                 for j,row in enumerate(modes) for k,val in enumerate(row)) + tail1
    assert mass < arb(147)/100 and energy < arb(4) and coarse < mass
    assert RHO**18500 > 256
    print(json.dumps(dict(kind="packet_histogram_invariant",divisions=divisions,
                          slab_indices=[start,stop],cutoff=N,polynomial_degree=DEGREE,
                          cap_units="1e-10",caps=CAPS,rho="10003/10000",
                          rank_upper="147/100",second_moment_upper="4",
                          component_ratio_upper="999/1000",power_denominator=18500),sort_keys=True))



def centered_modes(floor, center, order):
    degree = 2*order
    power = [arb(0) for _ in range(order+1)]
    weight = (4*floor+center).sqrt()
    for ell in range(1,order+1):
        weight *= (arb(3)/2-ell)/((4*floor+center)*ell)
        for i in range(1,ell+1):
            power[i] += weight*comb(ell,i)*(-center)**(ell-i)
    modes = [[arb(0) for _ in range(degree+1)] for _ in range(degree+1)]
    for i,weight in enumerate(power):
        for j in range(2*i+1):
            p = 2*i-j
            common = weight*comb(2*i,j)*(warm.SEED/2)**p
            for e in range(p//2+1):
                k = p-2*e
                modes[j][k] += common*comb(p,e)*(2 if k else 1)
    return modes


def finite_trial(floor,center,order,depth):
    modes = centered_modes(floor,center,order)
    envelope = [[abs(v).upper() for v in row] for row in modes]
    variance = sum(v**2 for v in envelope[0][1:])/2
    choose = arb(1)
    for i in range(1,order+2):
        choose *= (arb(3)/2-i)/i
    x = [arb(0) for _ in range(N+2)]
    previous_err = arb(0)
    for j in range(1,depth+1):
        old = x
        core_mass = sum(k*v for k,v in enumerate(old[:-2],1))
        radius = (warm.SEED+core_mass+old[-2]).upper()
        x,_,_ = histogram_step(envelope,old,arb(1))
        rank = sum(k*v for k,v in enumerate(x[:-2],1))+x[-2]
        delta = (rank-core_mass).upper()
        ratio = max(center,abs(radius**2-center).upper())/(4*floor+center)
        assert ratio < 1
        err = ((4*floor+center).sqrt()*abs(choose)*ratio**(order+1)/(1-ratio)).upper()
        if j == 1:
            rms = variance.sqrt()
        elif j == 2:
            m = 4+3*variance/4
            cap = (warm.SEED+(core_mass+old[-2])/2).upper()
            rms = (variance*(m/(4*floor+m)-32*floor/(4*floor+cap**2)**3)).sqrt()+previous_err+err
        else:
            rms = rms*radius/(4*floor+radius**2).sqrt()+previous_err+err
        rms = rms.upper()
        previous_err = err
    pair = 2*radius+delta
    ideal = floor-pair*delta/4
    truncation = (2*(4*floor+radius**2).sqrt()+err)*err/4
    product = ideal-truncation
    assert product > 0 and 2*floor.sqrt() > err
    distance = rms*pair/(4*(floor.sqrt()+ideal.sqrt()))+truncation/(ideal.sqrt()+product.sqrt())
    distance = distance.upper()
    norm = (floor.sqrt()+distance).upper()
    return (distance*norm/(1+norm**2).sqrt()).upper(),product.lower()


def certify_trial(start,stop,divisions,center,order,mark_cap,product_cap):
    for k in range(start, stop):
        mark,product = finite_trial(warm.slab(k,divisions),arb(center),order,4)
        assert mark < arb(mark_cap)/10000 and product > arb(product_cap)/10,(k,mark,product)
    print(json.dumps(dict(kind="positive_centered_prime_trial",divisions=divisions,
                          slab_indices=[start,stop],center=center,polynomial_degree=2*order,
                          iterations=4,packet_cutoff=N,limsup_mark=f"{mark_cap}/10000",
                          limiting_bulk_product_lower=f"{product_cap}/10"),sort_keys=True))


def obstruction():
    floor = arb(127)/8
    radius = arb(2)
    tail_ratio = (warm.SEED+radius)**2/(4*floor)
    assert tail_ratio < 1
    omitted = 2*floor.sqrt()*tail_ratio**(warm.CUTOFF+1)/(1-tail_ratio)
    modes = [[max(arb(0),(abs(a)-omitted/radius**j).lower()) for a in row]
             for j,row in enumerate(warm.laurent(floor))]
    assert modes[2][0] > arb(1)/20
    x = [arb(0) for _ in range(N+2)]
    for height in range(1,251):
        output,_,_ = histogram_step(modes,x,arb(1))
        x = [max(arb(0),v.lower()) for v in output[:-2]]+[arb(0),arb(0)]
        if sum(k*v for k,v in enumerate(x[:-2],1)) > 21:
            print(json.dumps(dict(kind="positive_histogram_divergence",floor="127/8",
                                  retained_weights=N,height=height,rho=1,
                                  mass_lower=21,quadratic_mode_lower="1/20"),sort_keys=True))
            return
    raise AssertionError("lower histogram did not cross the escape barrier")


if __name__ == "__main__":
    certify()
    certify_trial(15*128,63*32,256,12,8,169,47)
    certify_trial(7*256,15*128,256,12,8,222,33)
    obstruction()
