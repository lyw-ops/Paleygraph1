"""Interval bridge for the large-floor expansion of the seed's 30th residual."""
import json
import runpy
from fractions import Fraction
from math import comb
from pathlib import Path

from flint import acb, arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-fourth-75-check.py")))
hist = prior["hist"]
seed = prior["warm"].SEED
ctx.prec = 160


def kernel(z):
    degree = 28
    rows = [[acb(0) for _ in range(degree+1)] for _ in range(degree+1)]
    coefficient = z/2
    for ell in range(1, degree//2+1):
        if ell > 1:
            coefficient *= z*z*(arb(3)/2-ell)/ell
        for j in range(2*ell+1):
            power = 2*ell-j
            scale = coefficient*comb(2*ell,j)*(seed/2)**power
            for v in range(power//2+1):
                k = power-2*v
                rows[j][k] += scale*comb(power,v)*(2 if k else 1)
    return rows


def bridge():
    half = arb(1)/2**16
    cap = arb(5)
    # Include a neighborhood of zero and extend past z=1/8 (t=16).
    envelope = None
    for i in range(-1, 513):
        z = acb(arb(2*i+1,1)/8192, arb(0,half))
        new = [[abs(v).upper() for v in row] for row in kernel(z)]
        envelope = new if envelope is None else [
            [max(x,y) for x,y in zip(old,add)] for old,add in zip(envelope,new)]
    radius = abs(acb(arb(513)/4096,half)).upper()
    assert radius*cap < arb(63)/100
    caps = [arb(0)]*(hist["N"]+2)
    caps[0] = arb(1)/10**12
    for depth in range(1,31):
        output, mass, moment = hist["histogram_step"](envelope,caps,arb(1))
        # All absolute Taylor powers (including their weighted costs) increase
        # with |z|. Evaluate at radius, where 2 sqrt(t) = 1/radius.
        equivalent_floor = 1/(4*radius**2)
        tail = hist["taylor_tail"](equivalent_floor,equivalent_floor,mass,moment,arb(1))
        output[-2] += tail[0]
        output[-1] += tail[1]
        output[0] += arb(1)/10**5
        caps = [v.upper() for v in output]
        size = seed + sum(k*v for k,v in enumerate(caps[:-2],1)) + caps[-2]
        assert size < cap, (depth, size)
    # Sum of raw pretransport coefficients of G_z, with |x| cap 5.
    # For each word the bad-lift correction has price <=2 sqrt(q)/n.
    assert (1-(1-(radius*cap)**2).sqrt())/radius < 2
    assert 4*arb(3)/2/10**7 < arb(1)/10**5
    print(json.dumps(dict(kind="unmarked_proxy_uniform_analytic_bridge",bits=ctx.prec,
                          parameter="z=1/(2 sqrt(t))", slabs=514,
                          real_bounds=["-1/4096","513/4096"], imaginary_half_width="1/65536",
                          depth=30, all_site_modulus_upper=5, prime_n_min=10**14),
                     sort_keys=True))


def finite_newton():
    f = Fraction
    lower = f(2031,128)-f(1,2**17)
    cap, feedback = f(4768,1000), f(194,100)
    assert (cap-feedback)**2 < f(8)-f(1,10**10)
    complex_lip, real_lip = f(53755,10**5), f(51355,10**5)
    for imag, lip, exponent, step in [
            (feedback,complex_lip,321,f(1,2)), (0,real_lip,345,f(3,5))]:
        assert cap**2 < lip**2*(4*lower-2*imag**2+cap**2)
        assert (4*lip**600)**2*10**exponent < (step*(1-lip))**2
    assert f(2,5)*4*real_lip**599 < f(71,10**175)
    assert cap+f(3,5)+f(1,2) < f(59,10)
    print(json.dumps(dict(kind="actual_600_exact_newton_finite_bounds",
                          n_min=10**30,complex_n_max_exponent=321,real_n_max_exponent=345,
                          complex_counting_fourth_upper="1/2",real_counting_fourth_upper="3/5",
                          real_mark_limsup_upper="71e-175"),sort_keys=True))


if __name__ == "__main__":
    finite_newton()
    bridge()
