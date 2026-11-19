"""All-reserve interval test via convolution of the marked threshold masses."""
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import comb
from pathlib import Path

from flint import arb, arb_poly, ctx

spec=spec_from_file_location("compact_integrals", Path(__file__).with_name("astra-prime-repair-38.py"))
integrals=module_from_spec(spec)
spec.loader.exec_module(integrals)


def mesh_index(x, offset, denominator):
    idx=round(float((x+offset)*denominator))
    assert abs(arb(idx)/denominator-offset-x)<arb('.500001')/denominator
    return idx


def certify():
    ctx.prec=128
    tau=arb(1)/5
    g=integrals.mean_fourier(0,tau)/2
    c2=2*integrals.mean_fourier(2,tau)
    b=c2/(4*g)
    k=12
    hmax=arb(4**k)/comb(2*k,k)
    c=[2*(-1)**m*arb(comb(2*k,k-m))/comb(2*k,k) for m in range(1,k+1)]
    h1,h2=c[:2]
    tail=(4*(1+tau)-4*g*g-c2*c2/2).sqrt()/(4*g)
    error_path=tail*sum(a*a for a in c[1:]).sqrt()
    den=16384
    nx=524288
    bins=16384
    xmass=[0]*(5*den+1)
    xW=[arb(0)]*len(xmass)
    base=arb(0)
    sq2=arb(2).sqrt()
    for j in range(nx):
        x=(arb.pi()*(2*j+1)/(2*nx)).cos()
        A=arb(1)/2+(tau+2*x*x).sqrt()/(2*g)+sq2*x/g
        h=hmax*((1-x)/2)**k
        i=mesh_index(A,2,den)
        xmass[i]+=1
        xW[i]+=h-1-h1*x
        base+=A*h
    base/=nx
    smass=[arb(0)]*(2*den+1)
    sW=[arb(0)]*len(smass)
    for j,p in enumerate(integrals.semicircle_midpoints(bins)):
        s=arb(2*(j+1))/bins-2
        i=mesh_index(b*s,1,den)
        smass[i]+=p
        sW[i]+=p*h2*s
    # At threshold level t/den-3 the signed pushforward atom carries
    # W(x)+h2*s, averaged over the two independent discrete laws.
    mass=(arb_poly(xW)*arb_poly(smass)+arb_poly(xmass)*arb_poly(sW)).coeffs()
    slope=arb(0)
    value=base
    # All knot values, endpoints 0 and 4 inclusive. Between knots this
    # finite sum is affine. Arrays beyond the last mass are zero.
    max_box=None
    for j in range(7*den+1):
        if j>=3*den:
            max_box=value if max_box is None else max_box.max(value)
        if j<len(mass):
            slope+=mass[j]/nx
        value+=slope/den
    # Bounds valid simultaneously for 0<=delta<=4. In this range
    # D<5.4; |G_x|<420 and |G_s|<16. See the derivative argument.
    error_quad=420*arb.pi()/(2*nx)+arb(32)/bins
    error_snap=14*arb('1.000002')/den
    upper=max_box+error_quad+error_snap+error_path
    assert upper < -arb('.001')
    print(json.dumps(dict(kind="arb_first_reflection_all_nonnegative_thresholds",
                          tau="1/5",precision=ctx.prec,theta_bins=nx,
                          semicircle_bins=bins,threshold_denominator=den,
                          largest_grid_pairing=str(max_box),quadrature_error=str(error_quad),
                          snapping_error=str(error_snap),path_L2_error=str(error_path),
                          upper=str(upper),both_sectors=True),sort_keys=True))


if __name__=="__main__":
    certify()
