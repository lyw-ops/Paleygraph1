"""Check the lower escape barrier for a signed Jacobi and Legendre expansion."""
from collections import defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import arb, arb_poly, ctx

warm = runpy.run_path(str(Path(__file__).with_name("astra-warm-51-check.py")))
ctx.prec = 192
D = 2 * warm["CUTOFF"]
N = 24


def legendre_powers():
    """Multiplicities in ((tr A + tr B)/2)^h for two SL(2) factors."""
    powers = [{(0, 0): arb(1)}]
    for _ in range(D):
        row = defaultdict(lambda: arb(0))
        for (a, b), weight in powers[-1].items():
            for key in ((a+1,b), (a-1,b), (a,b+1), (a,b-1)):
                if min(key) >= 0:
                    row[key] += weight/2
        powers.append(row)
    return powers


def grouped_kernel(modes, alpha, powers, j, remove_first=False):
    kernel = [arb(0) for _ in range(4*D+1)]
    for k in range(D-j+1):
        grouped = defaultdict(lambda: arb(0))
        for h in range(D-j-k+1):
            if remove_first and (j,k,h) == (0,2,0):
                continue
            factor = modes[j+h][k] * comb(j+h,j) * alpha**h
            if factor == 0:
                continue
            for key, coefficient in powers[h].items():
                grouped[key] += factor*coefficient
        if (j,k) == (0,2) and not remove_first:
            grouped[0,0] -= alpha
        for (a,b), value in grouped.items():
            for weight in range(-2*a,2*a+1,4):
                cost = abs(value)*(b+1)/2
                kernel[2*D+weight+k] += cost
                kernel[2*D+weight-k] += cost
    return kernel


def escape(natural=True):
    floor = arb(127)/8
    alpha = arb(arb(487)/2000,arb(1)/1000000)
    modes = warm["laurent"](floor)
    if natural:
        alpha = modes[0][2]
    powers = legendre_powers()
    radius = arb(2)
    r = ((warm["SEED"]+2*alpha+radius)**2/(4*floor)).upper()
    assert r < 1
    coefficient = arb(1)
    for ell in range(1,D//2+2):
        coefficient *= (arb(3)/2-ell)/ell
    tail = (2*floor.sqrt()*abs(coefficient)*r**(D//2+1)/(1-r)).upper()
    lower = []
    # Keep a fixed subset of shifts and arities. Every discarded cost is positive.
    shift = 14
    for j in range(9):
        kernel = grouped_kernel(modes,alpha,powers,j,natural)
        lower.append(arb_poly([max(arb(0),(kernel[2*D+k]-tail/radius**j).lower())
                               for k in range(-shift,shift+1)]))
    assert lower[2][shift] > arb(1)/20
    h = [arb(0)]*N
    for height in range(1,1501):
        half = [v/2 for v in h]
        base = arb_poly(half[::-1]+[sum(i*v for i,v in enumerate(h))]+half)
        power = arb_poly([1])
        out = [arb(0)]*N
        for j, kernel in enumerate(lower):
            if j:
                power *= base
            row = power*kernel
            for k in range(1,N+1):
                out[k-1] += 2*row[j*N+shift+k]
        h = [max(arb(0),v.lower()) for v in out]
        if sum(k*v for k,v in enumerate(h,1)) > 21:
            print(json.dumps(dict(kind="signed_legendre_histogram_escape", floor="127/8",
                                  alpha=("degree28_c02" if natural else "487/2000 +/- 1/1000000"), precision=ctx.prec,
                                  retained_packets=N, max_shift=shift,max_arity=8,
                                  height=height, mass_lower=21, quadratic_zero_lower="1/20"),
                             sort_keys=True))
            return
    raise AssertionError("escape barrier was not reached")


def rectangle(fixed_zero=False):
    from flint import acb
    old = runpy.run_path(str(Path(__file__).with_name("marked-domain-53-check.py")))
    histogram = old["histogram"]
    step = histogram["histogram_step"]
    step.__globals__["N"] = N
    caps = [337378560332,111002625388,85258166719,29217875428,11245088047,
            4661116663,2028034299,913590563,422440008,199348553,95618670,
            46481081,22848303,11337996,5672063,2857601,1448562,738295,
            378093,194424,100278,51715,26342,12268,206487397,529933695]
    caps = [arb(v)/10**12 for v in caps]
    powers = legendre_powers()
    width = arb(1)/1024
    first, last, div = 1040, 1057, 64
    if fixed_zero:
        first,last = 1026,1041
    envelope = [[arb(0) for _ in range(2*D+1)] for _ in range(2*D+1)]
    alpha_cap = arb(0)
    for ix in range(first,last):
        t = acb(warm["slab"](ix,div),arb(0,width))
        modes = old["laurent"](t,True)
        alpha = modes[0][2]
        alpha_cap = max(alpha_cap,abs(alpha).upper())
        for j in range(D+1):
            kernel = grouped_kernel(modes,alpha,powers,j,True)
            for k in range(2*(D-j)+1):
                value = (kernel[2*D+k]*(2 if k else 1)).upper()
                envelope[j][k] = max(envelope[j][k],value)
    if fixed_zero:
        zero_slice(envelope,alpha_cap,arb(first)/div,abs(acb(arb(last)/div,width)))
        return
    output,b,c = step(envelope,caps,arb(1))
    total_b, total_c = b+2*alpha_cap, c+4*alpha_cap
    low = arb(first)/div
    high = abs(acb(arb(last)/div,width))
    tail_b,tail_c = histogram["taylor_tail"](low,high,total_b,total_c,arb(1))
    output[-2] += tail_b
    output[-1] += tail_c
    ratios = [a/b for a,b in zip(output,caps)]
    assert max(ratios) < arb(9999)/10000, ([float(v) for v in ratios],float(tail_b),float(tail_c))
    assert warm["SEED"]+total_b < arb(46)/10
    print(json.dumps(dict(kind="signed_legendre_complex_rectangle", slab_indices=[first,last],
                          divisions=div,imaginary_half_width="1/1024", scaled_vector_cap="4.6",
                          cap_ratio="0.9999",retained_packets=N),sort_keys=True))


def zero_slice(envelope,alpha_cap,low,high):
    h = [374375598699,126259871616,93256675145,33226233693,13304900058,
         5737749776,2597609508,1217659942,585920131,287742466,143636848,
         72668096,37177129,19200865,9997589,5242421,2765988,1467361,782223,
         418803,225107,121424,65708,35663,19408,10588,5789,3171,1738,950,511,250]
    h = [arb(v)/10**12 for v in h]
    n = len(h)
    u = arb(530953)/10**6
    error = arb(34)/10**5
    eta = arb(1)/5
    half = [v/2 for v in h]
    base = arb_poly(half[::-1]+[u]+half)
    norm = u+sum(v*(eta*k).cosh() for k,v in enumerate(h,1))
    leak = arb(0)
    pooled = [arb(0)]*(D*n+2*D+1)
    power = arb_poly([1])
    for j in range(D+1):
        if j:
            power *= base
        w = envelope[j][:2*(D-j)+1]
        side = [v/2 for v in w[1:]]
        row = power*arb_poly(side[::-1]+[w[0]]+side)
        center = j*n+len(side)
        for k in range(1,len(row)-center):
            pooled[k] += 2*row[center+k]
        if j:
            leak += sum(v*(eta*k).cosh() for k,v in enumerate(w))*j*(norm+error)**(j-1)*error
    for k,v in enumerate(pooled[1:],1):
        cap = h[k-1] if k<=n else arb(0)
        leak += max(arb(0),(v-cap).upper())*(eta*k).cosh()
    # Bound all high Taylor terms before projecting to the nonzero weights.
    r = ((warm["SEED"]*eta.cosh()+alpha_cap*(1+(2*eta).cosh())+norm+error)**2/(4*low))
    assert r < 1
    coefficient = arb(1)
    for ell in range(1,D//2+2):
        coefficient *= (arb(3)/2-ell)/ell
    leak += 2*high.sqrt()*abs(coefficient)*r**(D//2+1)/(1-r)
    assert leak < error,(float(leak),float(error))
    assert sum(i*v for i,v in enumerate(h))+error/eta < u
    assert warm["SEED"]+2*alpha_cap+u+sum(h)+error < arb(46)/10
    print(json.dumps(dict(kind="frozen_zero_signed_legendre_rectangle",slab_indices=[1026,1041],
                          divisions=64,imaginary_half_width="1/1024",zero_cap="530953/1000000",
                          weighted_residual_cap="34/100000",eta="1/5",scaled_vector_cap="4.6"),
                     sort_keys=True))


if __name__ == "__main__":
    escape()
    escape(False)
    rectangle()
    rectangle(True)
