"""Replay positional pair fibers and the quadratic transport of genuine endpoint heads."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
from theta import prime_field_generator

ctx.prec = 384


def dot(left, right):
    return sum((a*b for a, b in zip(left, right)), arb(0))


def units(value):
    scaled = 10**9*value
    return [int(scaled.lower().floor().unique_fmpz()),
            int(scaled.upper().ceil().unique_fmpz())]


def large_set(row, threshold):
    assert all(abs(value) > threshold or abs(value) < threshold for value in row)
    return {x for x in range(1, len(row)) if abs(row[x]) > threshold}


def audit(p):
    signs = prior["paley_sign"](p)
    n = len(signs)
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None, error
    signs = list(map(int,signs))
    side = 1 if pair[1][0] > pair[-1][0] else -1
    q, r = ([value/arb(n).sqrt() for value in pair[t]] for t in (side, -side))
    a, b = q[0], r[0]
    root = arb(p).sqrt()
    primitive = prime_field_generator(p)
    field = [pow(primitive, 2*x, p) for x in range(n)]
    logs = {value: x for x, value in enumerate(field)}
    mapped = [logs.get(pow(1-2*y, 2, p)) for y in field]
    for x in range(1,n):
        assert mapped[x] is None or signs[mapped[x]] == signs[x]
    minus = {x for x in range(1,n) if signs[x] == -1}
    assert {mapped[x] for x in minus} == minus
    F, R = ([value.real for value in acb.dft(row, inverse=True)]
            for row in (q, r))
    F, R = ([n*value for value in row] for row in (F, R))
    k = [value.real*n/root for value in acb.dft(signs, inverse=True)]
    U, V = ([(n*value-1)/root for value in row] for row in (q, r))
    conditional = []
    for t in range(n):
        masses = [n*q[i]*r[(i+t)%n] for i in range(n)]
        assert (sum(masses)-1).contains(0)
        conditional.append([n*z for z in acb.dft(masses, inverse=True)])
    for x in range(1,n):
        coeff = [F[(x-v)%n]*R[v] for v in range(n)]
        theta = acb.dft(coeff)
        for t in range(n):
            assert (conditional[t][x]-theta[t]).contains(0)
        allowed = [v for v in range(n) if signs[v]==-side and signs[(x-v)%n]==side]
        assert (4*len(allowed) ==
                n-2-sum(signs[v]*signs[(x-v)%n] for v in range(n)))
        assert (sum(coeff[v] for v in allowed)-(1-F[x]-R[x])).contains(0)
        assert sum(c*c for c in coeff) < 1 or (sum(c*c for c in coeff)-1).contains(0)
    pair_fields = []
    for t in range(1, n):
        product = [k[z]*k[(z-t)%n] for z in range(n)]
        pair_fields.append(acb.dft(product))
    records = []
    for headside, row in ((side, F), (-side, R)):
        cut = arb(1)/20
        head = large_set(row, cut)
        image = {mapped[x] for x in head if mapped[x] is not None}
        assert all(signs[y] == headside for y in image)
        collisions = sum(logs.get((1-field[x])%p) in head for x in head
                         if mapped[x] is not None)
        assert len(head)-sum(mapped[x] is None for x in head)-collisions//2==len(image)
        mult = [arb(signs[x])*(int(x in image)+int((-x)%n in image))/2 for x in range(n)]
        f = [value.real*n/root for value in acb.dft(mult, inverse=True)]
        marked = p*sum(w*u*v for w,u,v in zip(f,U,V))/n
        price = sum((row[x] for x in image),arb(0))
        assert (marked-headside*(len(image)-price)/root).contains(0)
        head_cubic = headside*(len(head)-sum((row[x] for x in head),arb(0)))/root
        head_price = sum((row[x] for x in head),arb(0))
        assert ((marked-head_cubic)*root-headside*head_price
                -headside*(len(image)-len(head)-price)).contains(0)
        fk = [u*v for u,v in zip(f,k)]
        mean = sum(fk)/n
        axes = side*root*(a*(dot(r,fk)-mean)-b*(dot(q,fk)-mean))
        triple = p*a*b*dot(fk,k)/n
        boundary = axes+triple
        fspec = acb.dft(f)
        centered, flat = arb(0), arb(0)
        for t, pairhat in enumerate(pair_fields,1):
            # inverse FFT gives sum_z f(z) k(z-i) k(z-i-t) at coordinate i.
            C = [s.real/n for s in acb.dft([w*v.conjugate() for w,v in
                                               zip(fspec,pairhat)],inverse=True)]
            assert (C[0]-C[-t]).contains(0)
            correction = (C[0]+C[-t])/(n-2)
            assert (sum(v for i,v in enumerate(C) if i not in (0,n-t))
                    +(n-2)*correction).contains(0)
            for i in range(1,n):
                j = (i+t)%n
                if j:
                    centered += p*q[i]*r[j]*(C[i]+correction)
            flat -= p*(arb(1)/n-a*r[t]-b*q[-t])*correction
        assert (flat+2*boundary/(n-2)).contains(0)
        assert (marked+centered-n*boundary/(n-2)).contains(0)
        records.append(dict(head_side=headside,head=len(head),image=len(image),
                            negative_input=sum(row[x]<0 for x in head),
                            negative_image=sum(row[x]<0 for x in image),
                            double_head=len(image & head),distinct_pair_collisions=collisions//2,
                            invalid_input=sum(mapped[x] is None for x in head),
                            image_count_price=units(headside*arb(len(image))/root),
                            image_endpoint_signed_price=units(headside*price/root),
                            input_endpoint_signed_price=units(headside*head_price/root),
                            image_endpoint_absolute_cost=units(sum((abs(row[x]) for x in image),arb(0))/root),
                            image_cubic=units(marked),image_boundary=units(boundary),
                            image_centered_distinct_sum=units(centered)))
    return dict(prime=p,bits=ctx.prec,units="1e-9",threshold="1/20",side=side,
                outputs=n-1,conditional_coefficients=n*(n-1),records=records)


if __name__=="__main__":
    for prime in (53,101,257,409,769):
        print(json.dumps(audit(prime),sort_keys=True),flush=True)
