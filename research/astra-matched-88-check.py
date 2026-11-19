"""Reconstruct actual optima and replay matched fiber moments with Arb balls."""
from math import isqrt
import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_mat, ctx
from theta import prime_field_generator


base = Path(__file__).resolve().parent
prior = runpy.run_path(str(base / "endpoint-direction-45-check.py"))
ctx.prec = 384


def units(x):
    v = x * 10**9
    return [int(v.lower().floor().unique_fmpz()), int(v.upper().ceil().unique_fmpz())]


def equal(x, y):
    z = acb(x-y)
    assert z.is_finite() and z.real.contains(0) and z.imag.contains(0), (x,y)


def squared(z):
    return (z*z.conjugate()).real


def positions(w):
    return [z*len(w) for z in acb.dft(w, inverse=True)]


def convolution(q, r):
    n = len(q)
    return [sum(q[i]*r[(j-i) % n] for i in range(n)) for j in range(n)]


def add_odd(row, side, pivot, d):
    # A supported, forbidden-frequency-null odd perturbation keeps the mark.
    n = len(row)
    ids = [i for i in range(1, n//2) if row[i] > 0]
    forbidden = [k for k in range(1, n//2) if d[k] == -side]
    cols = [i for i in ids if i != pivot]
    assert pivot in ids and len(cols) == len(forbidden)
    sine = [(arb(2*k)/n).sin_pi() for k in range(n)]
    mat = arb_mat([[sine[i*k % n] for i in cols] for k in forbidden])
    direction = list(mat.solve(arb_mat([[-sine[pivot*k % n]] for k in forbidden])))
    vals = [arb(1)] + direction
    tiny = min(row[i].lower()/(2*(1+abs(v).upper()))
               for i,v in zip([pivot]+cols, vals))
    assert tiny > 0
    for i,v in zip([pivot]+cols, vals):
        row[i] += tiny*v
        row[-i] -= tiny*v
    assert all(x > 0 or x.is_zero() for x in row)
    assert row[pivot] > row[-pivot]
    return tiny


def audit(p, pivot=None):
    signs = prior["paley_sign"](p)
    d = list(map(int, signs))
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None
    n = len(d)
    row = {s: [v/arb(n).sqrt() for v in pair[s]] for s in (1,-1)}
    odd = None
    if pivot is not None:
        side = 1 if row[1][0] > row[-1][0] else -1
        odd = {"side": side, "pivot": pivot, "size": units(add_odd(row[side],side,pivot,d))}
    q,r = row[1],row[-1]
    F,R = positions(q),positions(r)
    for W,s in ((F,1),(R,-1)):
        for x in range(1,n):
            if d[x]!=s:
                equal(W[x],0)
    if odd:
        assert any(abs(z.imag)>0 for z in (F if odd["side"]==1 else R))
    q_corr = convolution(q, [q[-i % n] for i in range(n)])
    r_corr = convolution(r, [r[-i % n] for i in range(n)])
    cube = convolution(q_corr,q)
    r2 = convolution(r,r)
    configs = [
        ("linear", q,r, F,R),
        ("real_parts", [(q[i]+q[-i % n])/2 for i in range(n)],
         [(r[i]+r[-i % n])/2 for i in range(n)],
         [acb(z.real) for z in F], [acb(z.real) for z in R]),
        ("cubic_square", cube,r2, [z*squared(z) for z in F], [z*z for z in R]),
        ("signed_cubics", cube,convolution(r_corr,r),
         [z*squared(z) for z in F], [z*squared(z) for z in R]),
        ("absolute_fourths",convolution(q_corr,q_corr),convolution(r_corr,r_corr),
         [acb(squared(z)*squared(z)) for z in F], [acb(squared(z)*squared(z)) for z in R]),
    ]
    g = prime_field_generator(p)
    field = [pow(g,2*i,p) for i in range(n)]
    logs = {z:i for i,z in enumerate(field)}
    probes = [logs[k*k % p] for k in (2,3,5,7) if k<=isqrt(p)]
    kernel = acb.dft([arb(probes.count(t))/len(probes) for t in range(n)])
    rows = []
    for name,u,v,U,V in configs:
        mass = [n*x*y for x,y in zip(u,v)]
        equal(sum(mass),1)
        spec = acb.dft(mass)
        if name in ("linear","real_parts"):
            equal(mass[0],1)
            assert all(m.is_zero() for m in mass[1:])
        for w,Z in ((u,U),(v,V)):
            for z,target in zip(positions(w),Z):
                equal(z,target)
        covariances=[]
        raw_cross=[]
        cutoff = arb(1)/8
        head_witnesses = []
        for W in (F,R):
            assert all(abs(z) < cutoff or abs(z) > cutoff for z in W)
        for t in range(n):
            matched = [x for x in range(n) if d[x]==1 and d[(x+t)%n]==-1]
            cross = sum((U[x]*V[(x+t)%n].conjugate() for x in matched), acb(0))
            equal(cross+V[t].conjugate()+U[-t % n]-int(t==0), spec[t])
            raw_cross.append(cross)
            heads = [x for x in matched if abs(F[x]) > cutoff and abs(R[(x+t)%n]) > cutoff]
            if name == "signed_cubics":
                assert all(not (F[x]*R[(x+t)%n].conjugate()).real.contains(0) for x in heads)
                heads = [x for x in heads if (F[x]*R[(x+t)%n].conjugate()).real > 0]
            head_witnesses.append(len(heads))
            if matched:
                first = sum(U[x] for x in matched)
                second = sum(V[(x+t)%n] for x in matched)
                cov = cross - first*second.conjugate()/len(matched)
            else:
                cov = acb(0)
            covariances.append(cov)
            if name=="linear":
                budget = sum(squared(F[x]*R[(x+t)%n]) for x in matched)
                assert budget < 1
        ratios = [(j-k)%n for j in probes for k in probes]
        ext_expected = sum((squared(kernel[i])*mass[i] for i in range(1,n)),arb(0))
        equal(sum(spec[t]-mass[0] for t in ratios)/len(ratios),ext_expected)
        measured = sum(covariances[t].real for t in ratios)/len(ratios)
        measured_cross = sum(raw_cross[t].real for t in ratios)/len(ratios)
        axes = sum(V[t].real+U[-t % n].real-int(t==0) for t in ratios)/len(ratios)
        equal(measured_cross+axes, mass[0]+ext_expected)
        record = dict(filters=name,root_overlap=units(mass[0]),
                         ratio_covariance_real=units(measured),
                         ratio_exterior_transform=units(ext_expected))
        if name in ("signed_cubics","absolute_fourths"):
            record.update(raw_ratio_cross=units(measured_cross),ratio_axes=units(axes),
                          threshold="1/8",
                          witnessed_ordered_ratios=sum(head_witnesses[t]>0 for t in ratios),
                          max_witnesses_per_ratio=max(head_witnesses[t] for t in ratios))
        rows.append(record)
    threshold = arb(1)/8
    images = []
    for W,s in ((F,1),(R,-1)):
        values = set()
        for x in range(1,n):
            if d[x] == s and abs(W[x]) > threshold:
                val = (1-2*field[x])**2 % p
                if val:
                    values.add(logs[val])
        images.append(values)
    example = None
    for t in range(n):
        # Both deletions depend on the actual shift; the second image is inverted.
        first = {(t+z)%n for z in images[0]}
        second = {(-2*t-z)%n for z in images[1]}
        forbidden = first | second
        matched = [x for x in range(n) if d[x]==1 and d[(x+t)%n]==-1]
        removed = [x for x in matched if x in forbidden or (-t-x)%n in forbidden]
        price = sum((R[(x+t)%n].real-F[x].real for x in removed),arb(0))
        charged = sum((abs(F[x])+abs(R[(x+t)%n]) for x in removed),arb(0))
        majorant = sum((abs(F[z])+abs(R[(t+z)%n])+abs(F[(-t-z)%n])+abs(R[-z % n])
                        for z in forbidden),arb(0))
        assert abs(price) < charged or (abs(price)-charged).contains(0)
        assert charged < majorant or (charged-majorant).contains(0)
        if field[t]==4:
            example = dict(removed=len(removed),matched=len(matched),
                           signed_toll=units(price/arb(p).sqrt()),
                           absolute_toll=units(charged/arb(p).sqrt()))
    assert example is not None
    return dict(prime=p,precision_bits=ctx.prec,units="1e-9",odd_perturbation=odd,
                probed_prime_shifts=len(probes),all_fibers_per_filter=n,rows=rows,
                adaptive_image_deletion_h4=example)


if __name__ == "__main__":
    for p,pivot in ((53,None),(257,48),(409,95)):
        print(json.dumps(audit(p,pivot),sort_keys=True),flush=True)
