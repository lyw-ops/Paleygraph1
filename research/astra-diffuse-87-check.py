"""Arb replay of the two diffuse signed prices and a distinct-center test."""
import json
from math import comb
from pathlib import Path
import runpy

from flint import acb, arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
from theta import prime_field_generator

ctx.prec = 384


def units(x):
    scaled = x * 10**9
    return [int(scaled.lower().floor().unique_fmpz()),
            int(scaled.upper().ceil().unique_fmpz())]


def total(values):
    return sum(values, arb(0))


def certify_equal(x, y):
    diff = x-y
    assert diff.is_finite() and diff.contains(0), (x, y)


def integer_power(x, exponent):
    # Repeated multiplication also encloses inputs straddling zero.
    result = arb(1)
    for _ in range(exponent):
        result *= x
    return result


def distinct_centers(mask, k, q, r, n, p, root, expected):
    f = [z.real*n/root for z in acb.dft(mask, inverse=True)]
    fk = [v*w for v, w in zip(f, k)]
    avg = total(fk)/n
    axes = root*(q[0]*(total(w*v for w, v in zip(r, fk))-avg)
                 - r[0]*(total(w*v for w, v in zip(q, fk))-avg))
    boundary = axes + p*q[0]*r[0]*total(v*w for v, w in zip(fk, k))/n
    fhat = acb.dft(f)
    centered = arb(0)
    for t in range(1, n):
        phat = acb.dft([k[z]*k[(z-t) % n] for z in range(n)])
        corr = [z.real/n for z in acb.dft([c*v.conjugate() for c,v in zip(fhat,phat)],
                                           inverse=True)]
        certify_equal(corr[0], corr[-t])
        for i in range(1, n):
            j = (i+t) % n
            if j:
                centered += p*q[i]*r[j]*(corr[i]+(corr[0]+corr[-t])/(n-2))
    certify_equal(expected, n*boundary/(n-2)-centered)
    return dict(boundary=units(boundary), centered=units(centered))


def audit(p):
    sign = prior["paley_sign"](p)
    pair, error = prior["solve_prime_pair"](sign)
    assert error is None, error
    d = list(map(int, sign))
    n = len(d)
    root = arb(p).sqrt()
    q, r = ([v/arb(n).sqrt() for v in pair[side]] for side in (1, -1))
    F, R = ([z.real*n for z in acb.dft(w, inverse=True)] for w in (q, r))
    k = [z.real*n/root for z in acb.dft(d, inverse=True)]
    transforms = [[z.real for z in acb.dft([v*u for v, u in zip(w, k)])] for w in (q, r)]
    primitive = prime_field_generator(p)
    field = [pow(primitive, 2*i, p) for i in range(n)]
    logs = {v:x for x,v in enumerate(field)}
    ds = [d[x] for x in range(n)]
    all_x = list(range(1, n))
    weights = [0]+[1-F[x]-R[x] for x in all_x]
    full = total(d[x]*weights[x] for x in all_x)/root
    prices = [total(W[x] for x in all_x)/root for W in (F, R)]
    for t in range(n):
        for W, spec in zip((F,R), transforms):
            certify_equal(total(ds[(x+t)%n]*W[x] for x in range(n))/root, spec[t])
    for spec, w in zip(transforms, (q,r)):
        certify_equal(total(v*v for v in spec)/n,
                      total((v*z)*(v*z) for v,z in zip(k,w)))
    # Bernstein probability for Bin(5,z) <= 2, evaluated independently in
    # its probability basis and using positive cyclic convolution powers.
    j, stop = 5, 2
    coeff = [sum(comb(j,m)*comb(j-m,k-m)*(-1)**(k-m)
                 for m in range(min(stop,k)+1)) for k in range(j+1)]
    assert sum(abs(c) for c in coeff) <= 3**j
    bernstein_records = []
    for W, w in zip((F,R), (q,r)):
        tapered = [v*total(comb(j,m)*integer_power(v*v,m)*integer_power(1-v*v,j-m)
                           for m in range(stop+1)) for v in W]
        signed_law = [arb(0) for _ in range(n)]
        autocorrelation = [total(w[i]*w[(i+t)%n] for i in range(n)) for t in range(n)]
        for m,c in enumerate(coeff):
            if not c:
                continue
            law = [v.real/n for v in acb.dft([integer_power(value,2*m+1) for value in W])]
            if m:
                certify_equal(total(law), 1)
                assert all(v < w[0] or (v-w[0]).contains(0) for v in law)
                assert all(v > 0 or v.contains(0) for v in law)
            for i in range(n):
                signed_law[i] += c*law[i]
        cube = [v.real/n for v in acb.dft([value*value*value for value in W])]
        for i,v in enumerate(cube):
            certify_equal(v, total(autocorrelation[t]*w[(i-t)%n] for t in range(n)))
        shifted = acb.dft([v*u for v,u in zip(k,signed_law)])
        for t,z in enumerate(shifted):
            certify_equal(z.real, total(ds[(x+t)%n]*v for x,v in enumerate(tapered))/root)
        bernstein_records.append(units(total(tapered[1:])/root))
    cutoffs = ((1,5),(1,20),(1,100))
    records = []
    for num, den in cutoffs:
        cut = arb(num)/den
        assert all(abs(W[x])<cut or abs(W[x])>cut for W in (F,R) for x in all_x)
        kept = [x for x in all_x if abs(F[x])<cut and abs(R[x])<cut]
        keep_set = set(kept)
        part = total(d[x]*weights[x] for x in kept)/root
        removed = [x for x in all_x if x not in keep_set]
        tail = [v-1 if x in keep_set else arb(-1) for x,v in enumerate(weights)]
        rhs = total(v*v for v in tail)/n
        lhs = arb(0)
        for t in range(n):
            shifted = total(ds[(x+t)%n]*tail[x] for x in range(n))/root
            lhs += (shifted*shifted)/n
            mod = total(d[x]*weights[x]*(1+d[x]*ds[(t+x)%n])/2 for x in kept)/root
            certify_equal(2*mod-part, shifted-1/root)
            if t == field.index(4) and den == 20:
                mask = [arb(d[x])*(1+d[x]*ds[(t+x)%n])/2 if x in keep_set else arb(0)
                        for x in range(n)]
                example = distinct_centers(mask, k, q, r, n, p, root, mod)
                example["marked"] = units(mod)
        assert lhs.upper() < rhs.lower()
        records.append(dict(cut=f"{num}/{den}", kept=len(kept), removed=len(removed),
                            residual=units(part), shifted_rms=units(lhs.sqrt())))
    cut = arb(1)/20
    heads = [[x for x in all_x if d[x]==s and abs(W[x])>cut] for s,W in ((1,F),(-1,R))]
    take = min(map(len,heads))
    images = [{logs[y] for x in head[:take] if (y := (1-2*field[x])**2 % p)}
              for head in heads]
    blocked = set.union(*images)
    rem = total(d[x]*weights[x] for x in all_x if x not in blocked)/root
    direct_all = []
    hfour = None
    for t in range(n):
        plus = [x for x in all_x if d[x]==1 and ds[(x+t)%n]==-1]
        mates = [(-(t+x))%n for x in plus]
        assert all(d[y]==-1 and ds[(t+y)%n]==1 for y in mates)
        assert len(plus)*2 == sum(d[x]*ds[(t+x)%n]==-1 for x in all_x)
        paired = [(x,y) for x,y in zip(plus,mates) if x not in blocked and y not in blocked]
        route = total(R[(t+x)%n]-F[x] for x,y in paired)/root
        orient = total(weights[x]-weights[y] for x,y in paired)/root
        certify_equal(route, orient)
        direct_all.append(abs(2*route-rem))
        if field[t]==4:
            bset = {z for xy in paired for z in xy}
            mask = [arb(d[x]) if x in bset else arb(0) for x in range(n)]
            hfour = distinct_centers(mask,k,q,r,n,p,root,route)
            hfour.update(marked=units(route),pairs=len(paired))
    paired_record = dict(equal_input_counts=take,image_counts=list(map(len,images)),
                         remainder=units(rem),h4=hfour,
                         all_shifts_mean_absolute_twice_error=units(total(direct_all)/n))
    t = field.index(4)
    direction = [arb(1+d[x]*ds[(t+x)%n])/2 for x in range(n)]
    half_prices = [total(direction[x]*W[x] for x in all_x)/root for W in (F,R)]
    for side, half, price, spec in zip((1,-1),half_prices,prices,transforms):
        certify_equal(2*half-price,side*(spec[t]-arb(d[t])/root))
    return dict(prime=p,bits=ctx.prec,units="1e-9",full=units(full),
                full_prices=[units(v) for v in prices],h4_agreement_prices=[units(v) for v in half_prices],
                bernstein_5_2_prices=bernstein_records,paired_disagreement=paired_record,all_shifted_transforms=2*n,thresholds=records,h4_agreement_below_1_over_20=example)


def square(u):
    d = list(map(int,prior["square_field_sign"](u)))
    n = len(d)
    step = (u+1)//2
    h = step
    F = [int(x % step == 0) for x in range(n)]
    R = [arb(1) if x == 0 else arb(2)*int(d[x] == -1)/(u+1) for x in range(n)]
    total_c = arb(0)
    part = arb(0)
    for x in range(1,n):
        v = d[x]*(1-F[x]-R[x])/u
        total_c += v
        part += v*(1+d[x]*d[(x+h)%n])/2
    col = sum(d[(x+h)%n]*F[x] for x in range(1,n))
    assert col == u-3
    return dict(square=u*u,subfield_shift_exponent=h,full=units(total_c),
                agreement=units(part),twice_agreement_minus_full=units(2*part-total_c),
                normalized_plus_translation=f"{col}/{u}")


if __name__ == "__main__":
    for p in (53,101,257,409,769):
        print(json.dumps(audit(p), sort_keys=True), flush=True)
    for u in (11,19,43):
        print(json.dumps(square(u), sort_keys=True), flush=True)
