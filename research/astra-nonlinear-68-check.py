"""Uniform old-exterior refresh and a supersolution for its fully debited lower test."""
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly, ctx

root = Path(__file__).parent
previous = runpy.run_path(str(root / "astra-shifted-66-check.py"))
linear = runpy.run_path(str(root / "astra-rank-six-67-linear.py"))
p = previous["prior"]
t = previous["t"]
scaled = p["scaled"]


def character_projections():
    """Direct mZ, first-return m² and the scalar unary m, including determinants."""
    degree = p["D"]
    old = p["prev"]["old"]
    a, b, c, d = p["prev"]["coefficients"]()
    z = p["old"]["prefix"](acb(t))[0].real
    w = p["joint"]["coefficient"](acb(t), 0, 2, 0).real
    v = p["selected"](acb(t)).real
    s = p["kern"]["dim"]

    def join(table, factor, scale):
        return old["add_inputs"](table, [{e: x*scale**j for e,x in row.items()}
                                          for j,row in enumerate(factor)])

    table = [{2*i-j: comb(j,i)*(s/2)**j for i in range(j+1)} for j in range(degree+1)]
    for lo, hi, scale, perverse in ((2,4,b/4,False),(5,8,c/8,False),(8,16,d/16,True)):
        factors = [(len(old["WEIGHTS"][i]),old["DETS"][i]) for i in range(lo,hi)]
        table = join(table,old["scalar_powers"](factors,degree,perverse),scale)
    table = join(table,[{0:p["kern"]["p3"]["P"][j].get((0,0),0)} for j in range(degree+1)],a)
    table = join(table,[{0:k} for k in p["old"]["moments"](degree)],z)
    table = join(table,old["scalar_powers"]([(4,4)],degree,True),w)
    mu = p["symplectic_moments"](2,degree)
    table = join(table,[{0:sum(comb(j,k)*mu[k]*mu[j-k] for k in range(j+1))}
                        for j in range(degree+1)],v)
    marked = join(table,linear["marked_factors"](degree),c/8)
    scalar = join(table,old["scalar_powers"]([(4,2)],degree,False),c/8)
    extent = s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*(abs(v)+abs(w)+abs(z))
    rt = extent**2/(4*t)

    def coefficient(moments,arity,exponent):
        bn, acc = arb(1), arb(0)
        for k in range(1,degree//2+1):
            bn *= (arb(3)/2-k)/k
            acc += (2*t.sqrt()*bn*comb(2*k,arity)/(4*t)**k
                    *moments[2*k-arity].get(exponent,0))
        k += 1
        bn *= (arb(3)/2-k)/k
        ratio = rt*comb(2*k+2,arity)/comb(2*k,arity)
        tail = 2*t.sqrt()*abs(bn)*rt**k*comb(2*k,arity)/(extent**arity*(1-ratio))
        return acc+arb(0,tail.upper())

    return extent, abs(c)/8, coefficient(marked,0,1), coefficient(marked,1,2), coefficient(scalar,1,1)


def refresh():
    base, u, direct_mz, unary_z, unary_m = character_projections()
    v, _, _, _, small_direct, _, _, large = p["projection_data"]()
    ycap = arb(3)/10**8
    cap_u, cap_d = arb(153)/10**6, arb(145)/10**6
    cmax = 4*(cap_u**2+cap_d**2)
    c6 = 4*cap_u**2+2*cap_d**2
    slope = (base+arb(128).sqrt()*ycap)/((base+arb(128).sqrt()*ycap)**2+4*t).sqrt()
    f2, f3, f4 = 1/(2*t.sqrt()), 3/(4*t), 3/(8*t*t.sqrt())
    norm_small = (2*small_direct[0]**2+2*small_direct[1]**2+small_direct[2]**2).sqrt()
    # The surviving linear bias needs two copies of the selected A-sector.
    bias = f3/2*arb(52).sqrt()*u**2*arb(2).sqrt()*cap_d
    drift = slope*ycap+cmax*f2/2+bias
    assert norm_small+drift < ycap
    assert abs(large[0])+drift < cap_u
    assert max(abs(v).upper() for v in large[1:])+drift < cap_d
    extent = base+arb(128).sqrt()*ycap+28*(cap_u+cap_d)
    lipschitz = extent/(4*t+extent**2).sqrt()
    assert lipschitz < arb(428)/1000
    amp = large[1]+arb(0, (drift+abs(large[1]-large[2])).upper())
    assert amp>0
    # Compare to the same tags with the rank-six pair resampled independently
    # conditional on m. Every other large character uses its actual arithmetic law.
    main = -2*amp*unary_z
    # Difference caused by old Y in the linear projection: the constant in T has
    # zero conditional pairing with Z+Zchi. Bound the remaining difference by f'''.
    eu = 2*u                         # conditional L2 of T
    ez = arb(2).sqrt()*cap_d
    linear_y = f3*eu*arb(128).sqrt()*ycap*ez
    linear_six = f3*c6*ez/2
    # Conditional parity kills the term linear in T in the covariance of f''.
    max_t = 16*u
    quadratic = f4/2*max_t**2*(2*cap_d**2)  # two copies, Taylor and f''/2
    cubic = f3/3*(12*cap_d)*(2*cap_d**2)
    err = linear_y+linear_six+quadratic+cubic
    new_minus_old = main+arb(0,err.upper())
    assert new_minus_old<0
    # Resampling-free sign on a non-Jacobi old output. Here f differs by admitting W
    # while all other tags are held fixed in both expressions.
    # E[(Z+Zchi)Z | m] = 1. Subtract T, then replace its scalar unary by H_1's.
    compare_unary = f2*(max_t*(arb(2).sqrt()+1)
                         +arb(2).sqrt()*(arb(128).sqrt()*ycap+c6.sqrt()))
    # |Z|<=6, E[(Z+Zchi)^2 | m]=2 gives a direct bound on the quadratic remainder.
    m_z_change = -amp*unary_m+arb(0,(amp*compare_unary+6*f2*amp**2).upper())
    assert direct_mz<0 and m_z_change<0
    # With the six and Y admitted but W withheld, the same coefficient differs
    # from its bare value only via the selected A block; use conditional orthogonality.
    # A mixed difference of f (in T vs the other tags) vanishes through degree one in T.
    # d/dY of its T remainder: f''' T^2/2. For fluctuations in the six, d²/dX²
    # of its T remainder: f'''' T²/2. E[T² |Z|] <= sqrt(E[T^4] E[Z²]).
    disturbance = (f3/2*arb(128).sqrt()*ycap+f4*c6/4)*arb(52).sqrt()*u**2
    direct_with_others = direct_mz+arb(0,disturbance.upper())
    assert direct_with_others<0
    record("full_old_rank_six_refresh", floor="2031/128",precision=ctx.prec,
           direct_mZ_times_1e12=scaled(direct_mz,10**12),
           same_inputs_without_W_mZ_times_1e12=scaled(direct_with_others,10**12),
           mZ_full_W_change_times_1e12=scaled(m_z_change,10**12),
           scalar_unary_m_times_1e9=scaled(unary_m,10**9),
           linear_rank_six_m2_times_1e18=scaled(main,10**18),
           m2_nonlinear_error_times_1e18=scaled(err,10**18),
           m2_full_minus_independently_resampled_times_1e18=scaled(new_minus_old,10**18),
           direct_to_regenerated_drift_times_1e12=scaled(drift,10**12),
           refresh_Lipschitz_times_1e6=scaled(lipschitz,10**6))
    return abs(v),base,ycap,[cap_u,cap_d],c6


def all_sibling_debit(up,base,ycap,limits,c6, projected_unary=False):
    # Treat the old W and the five old tags as a single full signed block.
    # The six independent objects have no linear Jacobi return.
    # At degree two their only Jacobi contractions are the actual dual pairs.
    D = p["D"]
    outs = previous["transports"]()
    oldrow = arb_poly([0,2,0,2,0,16,0,2,0,2,0])*ycap
    zz = [arb(0)]*11
    six = [arb(0)]*11
    for (name,sgn),sides in outs.items():
        coeff = limits[0 if name.startswith("U") else 1]
        active = zz if len(sides[0])==6 else six
        for wt in sides[0]:
            active[5+wt] += coeff
    assert all(x.overlaps(y) for a in (zz,six) for x,y in zip(a,a[::-1]))
    five = oldrow
    oldrow += arb_poly(zz)
    sixrow = arb_poly(six)
    s = sum(oldrow.coeffs(),arb(0)).upper()
    g = (s+sum(six,arb(0))).upper()
    assert g < arb(8345)/10**6
    old_powers = [oldrow**h for h in range(D+1)]
    six_powers = [sixrow**h for h in range(D+1)]
    blocks = [arb_poly()]
    for h in range(1,D+1):
        row = old_powers[h]
        if h>=2:
            row += old_powers[h-2].left_shift(10)*comb(h,2)*c6
        for k in range(3,h+1):
            row += old_powers[h-k]*six_powers[k]*comb(h,k)
        blocks.append(five if projected_unary and h==1 else row)
    U = []
    for row in up:
        side = [x/2 for x in row[1:]]
        U.append(arb_poly(side[::-1]+[row[0]]+side))
    rho = (base+2)**2/(4*t)
    bn = arb(1)
    for k in range(1,16):
        bn *= (arb(3)/2-k)/k
    tail = 2*t.sqrt()*abs(bn)*rho**15/(1-rho)
    u=abs(p["prev"]["coefficients"]()[2])/8
    enlarged=base+2
    f3_abs=3*(4*t)*enlarged/(4*t-enlarged**2)**(arb(5)/2)
    one_tag=f3_abs/2*arb(52).sqrt()*u**2*arb(2).sqrt()*limits[1]
    firstsize=sum(five.coeffs(),arb(0)) if projected_unary else s
    costs,errors = [],[]
    for r in range(10):
        mid=5*(D-r)
        pol = arb_poly()
        for h in range(1,D-r+1):
            pol += U[r+h]*blocks[h]*comb(r+h,r)
        off = max([arb(0)]+[pol[mid+k].upper() for k in range(19,mid+1)])
        analytic = tail/2**r*((r+1)*firstsize/2+comb(r+2,r)*(s**2+c6)/4+
                               comb(r+3,r)*(g/2)**3/(1-(g/2)*(1+arb(r)/4)))
        if projected_unary:
            analytic += one_tag/2**r
        costs.append(arb_poly([(2*pol[mid+k]).upper() for k in range(-18,19)]))
        errors.append((2*(off+analytic)).upper())
    return costs,errors,g


def record(kind,**fields):
    print(json.dumps(dict(kind=kind,**fields),sort_keys=True),flush=True)


if __name__=="__main__":
    v,base,ycap,limits,c6=refresh()
    up,_=p["upper"](acb(t))
    rows=p["lower"](p["lower_data"](),v)
    costs,errors,g=all_sibling_debit(up,base,ycap,limits,c6)
    kernel=[a-b for a,b in zip(rows,costs)]
    binary=kernel[2][18]-errors[2]
    assert binary>arb(1)/20
    # Proof-sized rational envelope for the positive-part polynomial upper map.
    # Starting with very slightly overweight fixed-point coordinates leaves a strict margin.
    import sys
    if "--fit" in sys.argv:
        import numpy as np
        h=np.zeros(28)
        pos=[np.maximum(0,np.array([float(row[k]) for k in range(37)])) for row in kernel]
        for _ in range(1500):
            b=np.r_[h[::-1]/2,np.dot(h,np.arange(28)),h/2]
            out=np.zeros(28)
            power=[1.]
            for r,row in enumerate(pos):
                if r: power=np.convolve(power,b)
                step=np.pad(np.convolve(power,row),(0,28))
                out+=2*step[19+28*r:47+28*r]
            h=out+1.e-12
        print([int(x) for x in np.ceil(h*10**17)])
        sys.exit(0)
    caps = [20810076017782396,8928416210113660,4771349705051824,2350593881266546,
            1255353470718631,597518575789842,272775655452156,128936760333082,62556282426880,
            30976522233354,15590058784819,7951855732757,4100901509025,2134740647861,
            1120280914166,592197669335,314984269985,168446961758,90517035484,48850892354,
            26466944957,14389846332,7847989616,4291174358,2349628540,1283625621,690004727,336434961]
    h=[arb(k)/10**17 for k in caps]
    b=arb_poly([x/2 for x in h[::-1]]+[sum(k*x for k,x in enumerate(h))]+[x/2 for x in h])
    m=sum(k*x for k,x in enumerate(h,1))
    assert m<1
    out=[arb(0)]*28
    for r,row in enumerate(kernel):
        positive=arb_poly([max(arb(0),row[k].upper()) for k in range(37)])
        prod=positive*b**r
        for k in range(1,29):
            out[k-1]+=2*prod[18+28*r+k]
    assert all(x<y for x,y in zip(out,h))
    record("full_triangle_debit_supersolution",precision=ctx.prec,shape=[9,18,28],
           comparison_cap_mass_times_1e9=scaled(m,10**9),
           binary_zero_lower_times_1e6=scaled(binary,10**6),tag_mass_times_1e6=scaled(g,10**6),
           least_coordinate_slack_times_1e18=scaled(min(y-x for x,y in zip(out,h)),10**18))
    costs2,errors2,g2=all_sibling_debit(up,base,ycap,limits,c6,projected_unary=True)
    height,binary2=previous["escape"](rows,costs2,errors2)
    record("all_levels_all_nonlinear_all_old_trivial_selected_unary_escape",height=height,
           mass_threshold=21,shape=[9,18,28],precision=ctx.prec,
           paid_binary_times_1e6=scaled(binary2,10**6))
