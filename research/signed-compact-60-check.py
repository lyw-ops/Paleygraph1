"""Arb enclosure with exact Jacobi/rank-three coefficient collection."""
from collections import defaultdict
from functools import lru_cache
import json
from math import comb
from pathlib import Path
import runpy

from flint import arb, ctx, fmpq

prior = runpy.run_path(str(Path(__file__).with_name("compact-variance-59-check.py")))
spectrum = prior["spectrum56"]
degree = prior["degree"]
BASE = (("1","13/15","17/30"),
        ("-0.003","0.018","0.02","0.00875","-0.004","0.006","0.006"))
LOWER = (("99/100","163/200","463/1000"),
         ("0","0.0295","0.0287","0.0089","-0.00865","0.00727","0.00727"))


def legendre_coefficients(modes, b, beta):
    powers = prior["powers"](b,degree)
    symbols = spectrum["P"]
    for r in range(degree+1):
        for k in range(degree-r+1):
            values = defaultdict(lambda: arb(0))
            for h in range(degree-r-k+1):
                c = modes[r+h][k]*comb(r+h,r)*powers[h]
                if c:
                    for uv,m in symbols[h].items():
                        values[uv] += c*m
            if (r,k) == (0,2):
                values[0,0] -= b
            elif (r,k) == (0,1):
                values[1,0] -= beta/2
                values[0,1] -= beta/2
            yield r,k,values


@lru_cache(None)
def remaining_rank_four(h):
    return prior["remaining_packet"](0,h)


@lru_cache(None)
def signed_mass(u, h, a, b, c, d, e):
    packet = remaining_rank_four(h)
    weights = spectrum["pair_fiber"](a,b,c,d)
    return sum(value*sum(mult*sum(abs(i-4*h+w+j-e) for j in range(-2*u,2*u+1,4))
                         for w,mult in weights)
               for i,value in enumerate(packet))


def signed_radius(modes, b, beta, gamma, cutoffs=(4,3,4,8), *, upper=True):
    endpoint = arb.upper if upper else arb.lower
    l_cap,h_cap,legendre_cap,k_cap = cutoffs
    table = spectrum["rank_powers"](l_cap)
    bp,gp = prior["powers"](beta,degree),prior["powers"](gamma,degree)
    pooled = defaultdict(lambda: arb(0))
    outside = arb(0)
    for r,k,values in legendre_coefficients(modes,b,beta):
        if not values:
            continue
        for l in range(r+1):
            h = r-l
            coef = comb(r,l)*bp[l]*gp[h]
            for (u,v),value in values.items():
                a0 = coef*value
                if (l,h,k,u,v)==(1,0,1,0,0):
                    a0 -= gamma
                if a0 == 0:
                    continue
                if l>l_cap or h>h_cap or u+v>legendre_cap or k>k_cap:
                    outside += endpoint(abs(a0))*(v+1)*prior["shifted_mass"](l,h,k,u)
                    continue
                cosine = a0/(2 if k else 1)/4**l
                for (a,b3,c,d,e),mult in table[l].items():
                    for shift in ((-k,k) if k else (0,)):
                        pooled[u,v,h,a,b3,c,d,e+shift] += cosine*mult
    collected = sum(endpoint(abs(a0))*(v+1)*signed_mass(u,h,a,b3,c,d,e)
                    for (u,v,h,a,b3,c,d,e),a0 in pooled.items())
    return endpoint(outside+collected)


def projected_covariances(t, b, lam, nu):
    p = prior["activation_poly"](t)
    variance,*three = prior["exact_variance"](p,b,lam,nu)
    rt2 = arb(2).sqrt()
    values = tuple(prior["powers"](a,2*degree) for a in (rt2,b/2,lam/(2*rt2),nu/4))
    def scalar(extra):
        return sum(c*x for c,x in zip(p,prior["mean_powers"](degree,extra,values)))
    moment0 = scalar((0,0,0,0))
    moment2 = scalar((2,0,0,0))
    y = moment2/2-moment0-b/2
    fourth = scalar((4,0,0,0))/2-2*moment2+moment0
    quadratic = sum(c*x for c,x in zip(p,quadratic_means(values,False)))
    cross = sum(c*x for c,x in zip(p,quadratic_means(values,True)))
    return variance,(y,*three,fourth,quadratic,cross)


@lru_cache(None)
def weighted_quadratic_terms(cross):
    # The symmetric square average is (A^2+B^2)/2-1 for the two SU(2) traces.
    def catalan(k):
        return comb(k,k//2)//(k//2+1) if k%2==0 else 0
    pair = prior["raw_rows"](2*degree)[1]
    quotient = {}
    for j in range(0,degree+1,2):
        if cross:
            quadratic = sum(comb(j,k)*catalan(k+1)*catalan(j-k+1) for k in range(1,j,2))
        else:
            quadratic = sum(comb(j,k)*catalan(k+2)*catalan(j-k) for k in range(0,j+1,2))
            quadratic -= pair[j][0]
        quotient[j] = quadratic,pair[j][0]
    rows = []
    for terms in prior["contraction_terms"](degree,(0,0,0,0)):
        row = []
        for i,j,k,r,a in terms:
            factor,divisor = quotient[j]
            assert a%divisor==0
            weight = a//divisor*factor
            if weight:
                row.append((i,j,k,r,weight))
        rows.append(row)
    return rows


def quadratic_means(values, cross):
    return [sum(a*values[0][i]*values[1][j]*values[2][k]*values[3][r]
                for i,j,k,r,a in row)
            for row in weighted_quadratic_terms(cross)]


def projected_weight(b, lam, nu, coefficients):
    y,z,w,u,fourth,quadratic,cross = coefficients
    source = (2*b+y,2*lam+z,2*nu+w,u,fourth,quadratic,cross)
    moments = (arb(5)/8,arb(3)/4,arb(49)/64,arb(3)/4,arb(3)/4,arb(3)/4,arb(3))
    variances = (arb(1)/2,)*6+(arb(1),)
    square = 16*sum(a*a*v for a,v in zip(coefficients,variances))+source[1]*z*z
    square += sum(a*a*c*c*m for a,c,m in zip(source,coefficients,moments))
    for i in range(len(source)):
        for j in range(i):
            a,beta = source[i],source[j]
            c,d = coefficients[i],coefficients[j]
            square += (a*a*d*d+beta*beta*c*c+4*a*beta*c*d)*variances[i]*variances[j]
    radius = sum(abs(a)*r for a,r in zip(coefficients,(2,3*arb(2).sqrt(),8,23/arb(2).sqrt(),4,4,8)))
    return square.sqrt(),radius


def midpoint_residual(t, scales, projection):
    b,lam,nu = parameters(t,scales)[0]
    variance,covariances = projected_covariances(t,b,lam,nu)
    variances = (arb(1)/2,)*6+(arb(1),)
    variance += sum(a*a*v-2*a*c for a,c,v in zip(projection,covariances,variances))
    assert variance>0
    return variance.sqrt()


def parameters(t, scales):
    amplitudes,derivatives = prior["parameters"](t,scales[1:])
    return tuple(scales[0]*a for a in amplitudes),tuple(scales[0]*a for a in derivatives)


def trial(t, center, half_width, scales, projection):
    (b,lam,nu),derivatives = parameters(t,scales)
    beta,gamma = arb(2).sqrt()*lam,2*nu
    total = (arb(8).sqrt()+2*b+3*beta+4*gamma).upper()
    shift = signed_radius(prior["seed_modes"](prior["activation_poly"](t)),b,beta,gamma)
    error = prior["remainder"](t,arb(12),degree//2,total)
    rms = midpoint_residual(center,scales,projection).upper()
    rms += half_width*prior["derivative_bound"](t,total,derivatives)
    lead,lead_shift = projected_weight(b,lam,nu,projection)
    return *prior["split_transfer"](t,lead,lead_shift,rms,total,shift,error),shift


def trial_coefficients(profile):
    scales,projection = profile
    return tuple(arb(fmpq(x)) for x in scales),tuple(map(arb,projection))


def point_check():
    t = arb(19)/4
    scales,projection = trial_coefficients(BASE)
    mark,product,shift_upper = trial(t,t,arb(0),scales,projection)
    (b,lam,nu),_ = parameters(t,scales)
    modes = prior["seed_modes"](prior["activation_poly"](t))
    shift_lower = signed_radius(modes,b,arb(2).sqrt()*lam,2*nu,upper=False)
    assert arb("1.43706") < shift_lower <= shift_upper < arb("1.43707")
    assert shift_lower > arb("1.40323719")
    assert mark < arb("0.0148") and product > arb("0.969")
    print(json.dumps(dict(kind="rankthree_radius_and_extended_projection",floor="19/4",
                          signed_radius_bracket=["1.43706","1.43707"],
                          radius_threshold_for_old_projection="1.40323719",
                          new_mark_upper="0.0148",product_lower="0.969",precision=ctx.prec),sort_keys=True))


def certify(first, last, divisions, mark_cap, product_floor, profile):
    scales,projection = trial_coefficients(profile)
    width = arb(1)/(2*divisions)
    for k in range(first,last):
        center = arb(2*k+1)/(2*divisions)
        t = prior["warm"].slab(k,divisions)
        mark,product,_ = trial(t,center,width,scales,projection)
        assert mark < mark_cap and product > product_floor,(k,mark,product)
    print(json.dumps(dict(kind="signed_rankthree_and_extended_projection",slab_indices=[first,last],
                          divisions=divisions,mark_cap=str(mark_cap),product_floor=str(product_floor),
                          scales=profile[0],projection=profile[1],
                          precision=ctx.prec),sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    point_check()
    certify(35*256,143*64,2048,arb(19)/1000,arb(29)/100,LOWER)
    certify(143*128,144*128,4096,arb(1699)/100000,arb(58)/100,LOWER)
    certify(9*512,309*16,1024,arb(1699)/100000,arb(67)/100,LOWER)
