"""Exact compact moments and interval bounds for the distinguished trial."""
from collections import Counter
from functools import lru_cache
import json
from math import comb
from pathlib import Path
import runpy

from flint import arb, arb_poly, ctx, fmpq

trial58 = runpy.run_path(str(Path(__file__).with_name("distinguished-positive-58-check.py")))
spectrum56 = runpy.run_path(str(Path(__file__).with_name("astra-rankthree-56-check.py")))
warm = trial58["warm"]
remainder = trial58["remainder"]
activation = trial58["activation"]
degree = 16


@lru_cache(None)
def standard_tensor(rank, power):
    if power == 0:
        return {(0,)*rank: 1}
    result = Counter()
    for part, mult in standard_tensor(rank,power-1).items():
        for row in range(rank):
            if row and part[row] == part[row-1]:
                continue
            shape = list(part)
            shape[row] += 1
            result[tuple(shape)] += mult
    return result


@lru_cache(None)
def derived_tensor(rank, power):
    return {tuple(a-part[-1] for a in part): (part[-1],mult)
            for part,mult in standard_tensor(rank,power).items()}


def one_trace(rank, exponent, max_power):
    out = []
    for ell in range(max_power+1):
        weights = Counter()
        for h in range(ell+1):
            multiplier = comb(ell,h)
            first = derived_tensor(rank,h)
            second = derived_tensor(rank,ell-h)
            for label, (i, x) in first.items():
                if label in second:
                    j,y = second[label]
                    weights[(i-j)*exponent] += multiplier*x*y
        out.append(dict(weights))
    return out


def combine_moments(first, second, max_power):
    out = []
    for ell in range(max_power+1):
        weights = Counter()
        for h in range(ell+1):
            coef = comb(ell,h)
            for i,x in first[h].items():
                for j,y in second[ell-h].items():
                    weights[i+j] += coef*x*y
        out.append(dict(weights))
    return out


@lru_cache(None)
def raw_rows(max_power):
    arc = [{k-2*j:comb(k,j) for j in range(k+1)} for k in range(max_power+1)]
    # Each SU(2) trace is real and has Catalan moments in even degree.
    legendre = [{0:comb(k,k//2)//(k//2+1)} if k%2==0 else {} for k in range(max_power+1)]
    pair = combine_moments(legendre,legendre,max_power)
    triple = combine_moments(one_trace(3,1,max_power),one_trace(3,-1,max_power),max_power)
    four = combine_moments(one_trace(4,2,max_power),one_trace(4,-2,max_power),max_power)
    unit = one_trace(4,0,max_power)
    four = combine_moments(combine_moments(four,unit,max_power),unit,max_power)
    return arc,pair,triple,four


@lru_cache(None)
def contraction_terms(max_even, extra):
    limit = max_even+sum(extra)
    arc, pair, triple, four = raw_rows(2*degree)
    join = {}
    for k in range(limit+1):
        for r in range(0,limit+1-k,2):
            result = Counter()
            for i,x in triple[k].items():
                for j,y in four[r].items():
                    result[i+j] += x*y
            join[k,r] = dict(result)
    ia, ib, ic, iw = extra
    rows = []
    for n in range(0,max_even+1,2):
        terms = []
        for i in range(n+1):
            for j in range(ib%2,n-i+1,2):
                y = pair[j+ib][0]
                for r in range(iw%2,n-i-j+1,2):
                    k = n-i-j-r
                    joint = join[k+ic,r+iw]
                    coefficient = sum(x*joint.get(-h,0) for h,x in arc[i+ia].items())
                    if coefficient:
                        orderings = comb(n,i)*comb(n-i,j)*comb(n-i-j,r)
                        terms.append((i,j,k,r,orderings*y*coefficient))
        rows.append(terms)
    return rows


def powers(x, max_power):
    row = [arb(1)]
    for _ in range(max_power):
        row.append(row[-1]*x)
    return row


def mean_powers(max_even, extra, values):
    return [sum(a*values[0][i]*values[1][j]*values[2][k]*values[3][r]
                for i,j,k,r,a in row)
            for row in contraction_terms(max_even, extra)]


def activation_poly(t, order=degree//2):
    total = 4*t+12
    p = arb_poly([-12,1])
    binomial = arb(1)
    power = arb_poly([total.sqrt()])
    out = arb_poly()
    for j in range(order+1):
        if j:
            power = power*p*(1/total)
            binomial = binomial*(arb(3)/2-j)/j
        out += binomial*power
    return out


@lru_cache(None)
def b_scalar_coefficients():
    choose = fmpq(1)
    out = []
    for ell in range(1,degree//2+1):
        choose *= (fmpq(3,2)-ell)/ell
        coefficient = sum(comb(ell,j)*(-12)**(ell-j)*2**(j+1)*comb(2*j,j-1)
                          for j in range(1,ell+1))
        out.append(choose*coefficient)
    return out


def parameters(t, scales):
    total = 4*t+12
    coeffs = b_scalar_coefficients()
    b = sum(arb(c)*total**(-i) for i,c in enumerate(coeffs,1))*total.sqrt()
    db = sum(arb(c)*(2-4*i)*total**(-i-1) for i,c in enumerate(coeffs,1))*total.sqrt()
    k = 1/(4*t+6).sqrt()
    dk = -2*k**3
    lam = 2*scales[0]*b*k
    dlam = 2*scales[0]*(db*k+b*dk)
    nu = 2*scales[1]*lam*k
    dnu = 2*scales[1]*(dlam*k+lam*dk)
    return (b,lam,nu),(db,dlam,dnu)


def exact_variance(p, b, lam, nu):
    rt2 = arb(2).sqrt()
    vals = tuple(powers(a,2*degree) for a in (rt2,b/2,lam/(2*rt2),nu/4))
    moments = mean_powers(2*degree,(0,0,0,0),vals)
    p_mean = sum(c*x for c,x in zip(p,moments))
    squared = p*p
    p2 = sum(c*x for c,x in zip(squared,moments))
    extra = ((2,0,0,0),(1,1,0,0),(1,0,1,0))
    cross = [sum(c*x for c,x in zip(p,mean_powers(degree,e,vals))) for e in extra]
    physical = (cross[0]/2,cross[1]/(2*rt2),cross[2]/4)
    p_times_subtraction = sum(a*c for a,c in zip((b,lam,nu),physical))
    subtraction_square = 3*b*b/2+(lam*lam+nu*nu)/2
    variance = p2 - 2*p_times_subtraction + subtraction_square - (p_mean-b)**2
    mixed = sum(c*x for c,x in zip(p,mean_powers(degree,(1,0,0,1),vals)))/(4*rt2)
    return variance, physical[1]-lam/2, physical[2]-nu/2, mixed


def split_transfer(t, lead, lead_shift, rms, total, shift, error):
    correction = (2*activation(t,total)+error)*error/4
    pair = 2*total+shift
    ideal = t-pair*shift/4
    product = ideal-correction
    lead_floor = t-(2*total+lead_shift)*lead_shift/4
    assert product>0 and lead_floor>0 and 2*t.sqrt()>error
    distance = lead/(4*(t.sqrt()+lead_floor.sqrt()))
    distance += (pair+lead_shift)*rms/(4*(ideal.sqrt()+lead_floor.sqrt()))
    distance += correction/(ideal.sqrt()+product.sqrt())
    norm = (t.sqrt()+distance).upper()
    return (distance*norm/(1+norm*norm).sqrt()).upper(),product.lower()


def leading_weight(b, lam, nu, projection):
    z,w,u = projection
    source = (2*lam+z,2*nu+w,u)
    moments = (arb(3)/4,arb(49)/64,arb(3)/4)
    square = (8+b*b)*sum(a*a for a in projection)+source[0]*z*z
    square += sum(a*a*c*c*m for a,c,m in zip(source,projection,moments))
    for i,j in ((0,1),(0,2),(1,2)):
        a,beta = source[i],source[j]
        c,d = projection[i],projection[j]
        square += (a*a*d*d+beta*beta*c*c+4*a*beta*c*d)/4
    radius = z*3*arb(2).sqrt()+8*w+u*23/arb(2).sqrt()
    return square.sqrt(),radius


def remainder_norm(t, scales, projection):
    p = activation_poly(t)
    b,lam,nu = parameters(t,scales)[0]
    var,*covariance = exact_variance(p,b,lam,nu)
    projected = var+sum(a*a/2-2*a*c for a,c in zip(projection,covariance))
    assert projected>0
    return projected.sqrt()


def derivative_bound(t, total, derivatives):
    """Bound the centered L2 derivative of the source, with fixed projection."""
    base = 4*t+12
    ratio = max(arb(12),abs(total*total-12).upper())/base
    choose = arb(1)
    t_part, v_part = arb(2),arb(0)
    for j in range(1,degree//2+1):
        choose *= (arb(3)/2-j)/j
        t_part += (4*j-2)*abs(choose)*ratio**j
        v_part += j*abs(choose)*ratio**(j-1)
    db, dl, dn = map(lambda a: abs(a).upper(), derivatives)
    speed = 2*db+3*arb(2).sqrt()*dl+8*dn
    return ((t_part+2*total*v_part*speed)/base.sqrt()
            +(db+dl+dn)/arb(2).sqrt()).upper()


def trial(t, center, half_width, scales, projection):
    p = activation_poly(t)
    (b,lam,nu),derivatives = parameters(t,scales)
    beta,gamma = arb(2).sqrt()*lam,2*nu
    total = (arb(8).sqrt()+2*b+3*beta+4*gamma).upper()
    shift = signed_difference(seed_modes(p),b,beta,gamma)
    defect = remainder(t,arb(12),degree//2,total)
    rms = remainder_norm(center,scales,projection).upper()
    rms += half_width*derivative_bound(t,total,derivatives)
    lead,lead_shift = leading_weight(b,lam,nu,projection)
    return split_transfer(t,lead,lead_shift,rms,total,shift,defect)


def moment_and_point_check():
    arc,pair,triple,four = raw_rows(2*degree)
    assert arc[2][0]==2 and arc[4][0]==6
    assert pair[4]=={0:10}
    assert triple[2]=={0:4} and triple[3]=={-1:2,1:2} and triple[4]=={0:48}
    assert four[2]=={0:8} and four[4]=={-2:2,0:196,2:2}
    t = arb(5)
    scales = arb(19)/20,arb(3)/4
    b,lam,nu = parameters(t,scales)[0]
    variance,*_ = exact_variance(activation_poly(t),b,lam,nu)
    assert arb(480948475)/10**12 < variance < arb(480948476)/10**12
    modes = trial58["histogram"]["centered_modes"](t,arb(12),degree//2)
    assert modes[0][2].contains(b)
    # Keep the previous envelope, to isolate the gain from the variance calculation.
    b_old = modes[0][2]
    lam_old = 2*scales[0]*b_old/(4*t+6).sqrt()
    nu_old = 2*scales[1]*lam_old/(4*t+6).sqrt()
    amps = b_old,arb(2).sqrt()*lam_old,2*nu_old
    total = (arb(8).sqrt()+2*amps[0]+3*amps[1]+4*amps[2]).upper()
    shift = trial58["difference_radius"](modes,amps)
    error = remainder(t,arb(12),degree//2,total)
    mark,product = split_transfer(t,arb(0),arb(0),variance.sqrt(),total,shift,error)
    assert mark < arb(1694)/100000 and product > arb(93)/100
    print(json.dumps(dict(kind="exact_compact_variance_point", floor="5", max_degree=32,
                          variance_bounds_1e12=[480948475,480948476],
                          mark_upper_with_round58_pointwise="0.01694",
                          product_lower="0.93", precision=ctx.prec),sort_keys=True))


def certify(first, last, divisions, cap, product_floor):
    scales = arb(9)/10,arb(13)/20
    projection = arb(1)/125,arb(1)/96,arb(3)/400
    half_width = arb(1)/(2*divisions)
    for k in range(first,last):
        center = arb(2*k+1)/(2*divisions)
        t = warm.slab(k,divisions)
        mark, product = trial(t,center,half_width,scales,projection)
        assert mark < cap and product > product_floor,(k,mark,product)
    print(json.dumps(dict(kind="compact_three_field_split_positive_trial",
                          slab_indices=[first,last], divisions=divisions,
                          mark_cap=str(cap), product_floor=str(product_floor),
                          scales=["9/10","13/20"], projection=["1/125","1/96","3/400"],
                          max_degree=32,precision=ctx.prec),sort_keys=True))


def pointwise_radius_target():
    t = arb(19)/4
    scales = arb(13)/15,arb(17)/30
    projection = arb(9)/500,arb(1)/50,arb(7)/800
    (b,lam,nu),_ = parameters(t,scales)
    beta,gamma = arb(2).sqrt()*lam,2*nu
    total = (arb(8).sqrt()+2*b+3*beta+4*gamma).upper()
    old = signed_difference(seed_modes(activation_poly(t)),b,beta,gamma)
    rms = remainder_norm(t,scales,projection)
    lead,shift = leading_weight(b,lam,nu,projection)
    error = remainder(t,arb(12),degree//2,total)
    lo,hi = arb("1.40323718"),arb("1.40323719")
    below,_ = split_transfer(t,lead,shift,rms,total,lo,error)
    above,_ = split_transfer(t,lead,shift,rms,total,hi,error)
    mark,product = split_transfer(t,lead,shift,rms,total,old,error)
    assert lo < hi < old < arb("1.44904434")
    assert below < arb(17)/1000 < above
    assert arb("0.01734731") < mark < arb("0.01734732") and product>arb("0.93359")
    print(json.dumps(dict(kind="precise_pointwise_radius_target",floor="19/4",
                          critical_radius_bracket=["1.40323718","1.40323719"],
                          current_radius_upper="1.44904434",
                          product_lower="0.93359", mark_bracket=["0.01734731","0.01734732"],
                          scales=["13/15","17/30"], projection=["9/500","1/50","7/800"],
                          precision=ctx.prec),sort_keys=True))


def seed_modes(p):
    modes = [[arb(0) for _ in range(degree+1)] for _ in range(degree+1)]
    ss = powers(arb(2).sqrt(),degree)
    for i in range(1,len(p)):
        for j in range(2*i+1):
            power = 2*i-j
            base = p[i]*comb(2*i,j)*ss[power]
            for e in range(power//2+1):
                k = power-2*e
                modes[j][k] += base*comb(power,e)*(2 if k else 1)
    return modes


@lru_cache(None)
def remaining_packet(l, h):
    w = trial58["field_poly"](trial58["SEED_FIELDS"][1])
    f = trial58["field_poly"](trial58["SEED_FIELDS"][2])
    return w**l*f**h


@lru_cache(None)
def shifted_mass(l, h, k, u):
    mid = 3*l+4*h
    return sum(val*sum(max(k,abs(i-mid+k0)) for k0 in range(-2*u,2*u+1,4))
               for i,val in enumerate(remaining_packet(l,h)))


def signed_difference(modes, b, beta, gamma):
    # Collect the two Legendre representation labels before taking absolute values.
    symbols = spectrum56["P"]
    bs = powers(b,degree)
    bp,gp = powers(beta,degree), powers(gamma,degree)
    shift = arb(0)
    for r in range(degree+1):
        for k in range(degree-r+1):
            values = {}
            for h in range(degree-r-k+1):
                c = modes[r+h][k]*comb(r+h,r)*bs[h]
                if c == 0:
                    continue
                for uv,m in symbols[h].items():
                    values[uv] = values.get(uv,arb(0)) + c*m
            if (r,k) == (0,2):
                values[0,0] -= b
            elif (r,k) == (0,1):
                values[1,0] -= beta/2
                values[0,1] -= beta/2
            for l in range(r+1):
                h = r-l
                coefficient = comb(r,l)*bp[l]*gp[h]
                for (u,v),a in values.items():
                    c = coefficient*a
                    if (l,h,k,u,v)==(1,0,1,0,0):
                        c -= gamma
                    price = abs(c).upper()*(v+1)
                    shift += price*shifted_mass(l,h,k,u)
    return shift.upper()


if __name__ == "__main__":
    ctx.prec = 192
    moment_and_point_check()
    certify(309*128,155*256,8192,arb(1699)/100000,arb(89)/100)
    certify(155*64,83*128,2048,arb(1699)/100000,arb(94)/100)
    certify(75*128,309*32,2048,arb(2)/100,arb(45)/100)
    certify(37*256,75*128,2048,arb(22)/1000,arb(24)/100)
    pointwise_radius_target()
