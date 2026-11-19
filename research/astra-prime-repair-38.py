"""Interval check of the one-reflection signed Paley incidence integral."""
from math import comb
import json

from flint import acb, arb, arb_poly, ctx


def mean_fourier(degree, tau):
    def integrand(theta, analytic):
        value = 2 * (tau + 2*theta.cos()**2).sqrt(analytic=analytic)
        return value * (degree*theta).cos()
    return acb.integral(integrand, 0, arb.pi()).real / arb.pi()


def semicircle_midpoints(size):
    # Half the trace of Haar SU(2) has density 2 sqrt(1-u^2)/pi.
    cdf = []
    for j in range(size+1):
        u = arb(2*j)/size-1
        cdf.append((u*(1-u*u).sqrt()+u.asin())/arb.pi()+arb(1)/2)
    masses = arb_poly([r-l for l,r in zip(cdf, cdf[1:])])
    sums = (masses*masses).coeffs()
    assert len(sums) == 2*size-1 and sum(sums).contains(1)
    return sums


def depth_two_interval():
    # Bounds uniform on each closed floor interval. See the Laplace
    # representation in the note for monotonicity of path amplitudes.
    theta_bins, bins = 1024, 512
    weights = semicircle_midpoints(bins)
    coords = [arb(2*(j+1))/bins-2 for j in range(len(weights))]
    cosines = [(arb(2).sqrt()*(arb.pi()*(2*j+1)/(2*theta_bins)).cos())
               for j in range(theta_bins)]
    for left,right in [(0,5),(5,8),(8,10)]:
        lo,hi=arb(left)/100,arb(right)/100
        if left:
            first_lo=mean_fourier(0,lo)/2
            c2=2*mean_fourier(2,lo)
        else:
            first_lo=2*arb(2).sqrt()/arb.pi()
            c2=4*first_lo/3
        first_hi=mean_fourier(0,hi)/2
        tail_variance=1+lo-first_lo**2-c2**2/8
        assert tail_variance>0 and c2>0
        shift=[c2*s/2 for s in coords]
        offset=hi+tail_variance
        grid=sum(sum(w*(offset+(x+v)**2).sqrt() for w,v in zip(weights,shift))
                 for x in cosines)/theta_bins
        grid_error=arb(2).sqrt()*arb.pi()/(2*theta_bins)+c2/bins
        g_upper=(first_hi+grid+grid_error)/2
        assert g_upper < arb('.998')
        print(json.dumps(dict(kind="arb_two_step_true_mean_uniform_floor_upper",
                              precision=ctx.prec, lower_floor=f"{left}/100",
                              upper_floor=f"{right}/100", theta_bins=theta_bins,
                              semicircle_bins=bins,first_mean_ceiling=str(first_hi),
                              second_mean_midpoint_upper_model=str(grid),
                              second_mean_grid_error=str(grid_error),
                              two_step_average_upper=str(g_upper)),sort_keys=True))


def main():
    ctx.prec = 128
    tau, delta, k = arb(1)/5, arb(1)/500, 12
    g = mean_fourier(0, tau)/2
    c2 = 2*mean_fourier(2, tau)
    b = c2/(4*g)
    assert 1 < g and g < arb('1.05') and 0 < b and b < arb('.3')
    hmax = arb(4**k)/comb(2*k,k)
    coeff = [2*(-1)**m*arb(comb(2*k,k-m))/comb(2*k,k) for m in range(1,k+1)]
    h1,h2 = coeff[:2]
    assert hmax < 7 and abs(h1)<2 and abs(h2)<2
    test_norm = sum(a*a for a in coeff[1:]).sqrt()
    tail = (4*(1+tau)-4*g*g-c2*c2/2).sqrt()/(4*g)
    error_path = tail * test_norm

    # Midpoint quantization of the two independent semicircle variables.
    bins = 1024
    weights = semicircle_midpoints(bins)
    coords = [arb(2*(j+1))/bins-2 for j in range(len(weights))]
    moments = [[arb(0)] for _ in range(3)]
    for s,p in zip(coords, weights):
        for j,moment in enumerate(moments):
            moment.append(moment[-1] + p*s**j)
    # The integrand G=A*h+D*(h-1-h1*x+h2*s). Bound its derivatives
    # by the Lipschitz product rule, valid across the positive-part kink.
    # A=.5+f/(4*g)+sqrt(2)*x/g, |A|<3, |A'|<2.2,
    # |delta-A-b*s|<4, |h'|<= k*hmax/2<42.
    # |h-1-h1*x+h2*s|<14, so |G_x|<350 and |G_s|<13.
    Nx = 131072
    # A tighter S estimate uses the SAME off-mark field: A >= .5 -
    # sqrt(2)/g+sqrt(tau)/(2*g) > -.7, hence D<1.31.
    assert arb('.5')-arb(2).sqrt()/g+tau.sqrt()/(2*g) > arb('-.7')
    # So |G_s| <= .3*14+1.31*2 <7. Both scalar midpoint errors <=1/bins.
    error_grid = arb(350)*arb.pi()/(2*Nx)+arb(14)/bins
    total = arb(0)
    for j in range(Nx):
        theta = arb.pi()*(2*j+1)/(2*Nx)
        x = theta.cos()
        A = arb(1)/2+(tau+2*x*x).sqrt()/(2*g)+arb(2).sqrt()*x/g
        h = hmax*((1-x)/2)**k
        W = h-1-h1*x
        cut = (delta-A)/b
        # coords[j] < cut. Use a float only as a proposed integer, and
        # certify both sides with Arb. Strictness never failed in this run.
        count = min(len(coords),max(0,int((float(cut)+2)*bins/2)))
        assert count == 0 or coords[count-1] < cut
        assert count == len(coords) or coords[count] > cut
        m0,m1,m2 = [v[count] for v in moments]
        total += A*h + (delta-A)*(W*m0+h2*m1)-b*(W*m1+h2*m2)
    mid = total/Nx
    upper = mid + error_grid + error_path
    assert upper < -arb('.019')
    print(json.dumps(dict(kind="arb_one_reflection_limiting_incidence_upper",
                          precision=ctx.prec, floor="1/5", time=1,
                          threshold="1/500", test_degree=k,
                          theta_bins=Nx, semicircle_bins=bins,
                          g1=str(g),chebyshev_f2=str(c2),
                          midpoint_integral=str(mid),grid_error=str(error_grid),
                          omitted_path_error=str(error_path), upper=str(upper),
                          scope="limsup on every eligible prime and square, both sectors"),
                     sort_keys=True))


if __name__=="__main__":
    main()
    depth_two_interval()
