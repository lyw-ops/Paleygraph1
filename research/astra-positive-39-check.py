"""Interval certificate for two consecutive pinned reflections of the true T=1 proposal."""
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path

from flint import arb, ctx


spec = spec_from_file_location("first_repair", Path(__file__).with_name("astra-prime-repair-38.py"))
first_repair = module_from_spec(spec)
spec.loader.exec_module(first_repair)


def certify():
    ctx.prec = 128
    tau, cut = arb(7)/50, -arb(9)/20
    g = first_repair.mean_fourier(0, tau)/2
    b = first_repair.mean_fourier(2, tau)/(2*g)
    jacobi = arb(2).sqrt()/g
    tail = ((1+tau-g*g)/(2*g*g)-b*b).sqrt()
    assert 1 < g < arb('1.002') and b < arb('.26') and jacobi < arb('1.42')
    theta = cut.acos()
    pi = arb.pi()
    costs = [(pi-theta)/pi] + [-(k*theta).sin()/(k*pi) for k in range(1,4)]
    h0 = cut*costs[0]-costs[1]
    h1,h2 = [2*(cut*costs[j]-(costs[j-1]+costs[j+1])/2)/h0 for j in [1,2]]
    hsq = (cut**2*costs[0]-2*cut*costs[1]+(costs[0]+costs[2])/2)/h0**2
    test_norm = (2*(hsq-1)-h1**2).sqrt()
    assert 1/h0 < 8 and (cut+1)/h0 < 5 and abs(h1) < 2 and abs(h2) < arb('1.2')
    a0,a1,a2,a3 = [arb(j)/1000 for j in [40,-70,47,-55]]
    bins, nx = 16384, 65536
    masses = first_repair.semicircle_midpoints(bins)
    points = [arb(2*(j+1))/bins-2 for j in range(len(masses))]
    pref = [[arb(0)] for _ in range(3)]
    for y, mass in zip(points,masses):
        for j in range(3):
            pref[j].append(pref[j][-1] + mass*y**j)

    def index(v):
        i = min(len(points),max(0,int((float(v)+2)*bins/2)))
        assert not i or points[i-1] < v
        assert i == len(points) or v < points[i]
        return i

    def product(left,right,c,d,e,f):
        # Integrate (c+d*y)(e+f*y) on the selected midpoint range.
        return (c*e*(pref[0][right]-pref[0][left])
                +(c*f+d*e)*(pref[1][right]-pref[1][left])
                +d*f*(pref[2][right]-pref[2][left]))

    integral, residual = arb(0), arb(0)
    for j in range(nx):
        x = (pi*(2*j+1)/(2*nx)).cos()
        s = 2*x*x-1
        h = max(arb(0), cut-x)/h0
        H0 = h-1-h1*x
        z0 = 1+jacobi*x+b*s
        p0 = a0+a1*x+a2*s
        r0 = -a0-a1*x+a3*s
        split = index(-z0/b)
        integral += h*z0  # midpoint sum in y is centered exactly
        for left,right,d0,d1,u0,u1 in [(0,split,-z0,-b,r0,a2),
                                        (split,len(points),arb(0),arb(0),z0+r0,b+a2)]:
            stop = min(right,max(left,index(-u0/u1)))
            integral += product(left,right,(d0+p0)/2,(d1+a3)/2,H0,h2)
            integral += product(left,stop,-u0,-u1,H0,h2)
            residual += product(left,right,d0-p0,d1-a3,d0-p0,d1-a3)
    integral /= nx
    residual = (residual/nx).sqrt()
    # Pointwise Lipschitz bounds for the signed integrand and the residual.
    xerr, yerr = pi/(2*nx), arb(2)/bins
    integral_error = 130*xerr+8*yerr
    residual_error = 3*xerr+arb('.32')*yerr
    upper = integral+integral_error+(residual+residual_error+tail)*test_norm/2
    assert upper < -arb('.011')
    print(json.dumps(dict(kind="actual_two_reflections_incidence_upper",precision=ctx.prec,
                          tau="7/50",T=1,thresholds=[0,0],theta_bins=nx,
                          semicircle_bins=bins,g=str(g),b=str(b),tail=str(tail),
                          test_norm=str(test_norm),integral=str(integral),
                          integral_error=str(integral_error),residual=str(residual),
                          residual_error=str(residual_error),upper=str(upper)),
                     sort_keys=True))


if __name__ == "__main__":
    certify()
