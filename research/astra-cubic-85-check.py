"""Verify individual cubic output frequencies and displacement centering with Arb."""
import json
from math import isqrt
from pathlib import Path
import runpy

from flint import acb, arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 384


def units(x):
    scaled = 10**9 * x
    return [int(scaled.lower().floor().unique_fmpz()),
            int(scaled.upper().ceil().unique_fmpz())]


def dot(x, y):
    return sum((u*v for u, v in zip(x, y)), arb(0))


def audit(p):
    signs = prior["paley_sign"](p)
    n = len(signs)
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None, error
    signs = list(map(int, signs))
    side = 1 if pair[1][0] > pair[-1][0] else -1
    q, r = ([v/arb(n).sqrt() for v in pair[t]] for t in (side, -side))
    a, b = q[0], r[0]
    root = arb(p).sqrt()
    k = [z.real*n/root for z in acb.dft(signs, inverse=True)]
    F, H = ([z.real for z in acb.dft(row)] for row in (q, r))
    U, V = ([(n*v-1)/root for v in row] for row in (q, r))
    spectral = [p*z.real/n for z in acb.dft([u*v for u,v in zip(U,V)])]
    assert all((spectral[x]-(1-F[x]-H[x])).contains(0) for x in range(1,n))
    for t in range(n):
        assert (n*dot(q, r[t:]+r[:t])-1).contains(0)
    k2 = [x*x for x in k]
    kernel_square_mean = sum(k2)/n
    axis = side*root*(a*(dot(r,k2)-kernel_square_mean)-b*(dot(q,k2)-kernel_square_mean))
    triple = p*a*b*dot(k,k2)/n
    boundary = axis+triple
    A = [dot(k2,k[-t:]+k[:-t])/n for t in range(n)]
    fiber_sum = arb(0)
    for t in range(1,n):
        # Sum C(i,i+t) over the distinct fiber independently by FFT convolution.
        product = [k[i]*k[(i-t)%n] for i in range(n)]
        col = acb.dft([u*v.conjugate() for u,v in zip(acb.dft(k),acb.dft(product))], inverse=True)
        assert (col[0].real/n-A[t]).contains(0)
        assert (col[-t].real/n-A[t]).contains(0)
        assert (sum(z.real for i,z in enumerate(col) if i not in (0,n-t))/n+2*A[t]).contains(0)
        weight = arb(1)/n-a*r[t]-b*q[-t]
        fiber_sum += p*weight*(-2*A[t])/(n-2)
    assert (fiber_sum+2*boundary/(n-2)).contains(0)

    # Annihilate the heaviest unmarked coset for every nontrivial subgroup.
    phases = [acb(arb(2*j)/n).exp_pi_i() for j in range(n)]
    coset_tests = 0
    for row, sector in ((q,side),(r,-side)):
        for size in range(2,n+1):
            if n%size:
                continue
            residue = max(range(1,size),key=lambda j: float(sum(row[j::size]).mid()))
            step = min(range(1,size),key=lambda v: float(phases[(n//size*v*residue)%n].real.mid()))
            u = n//size*step
            phase = phases[(u*residue)%n]
            assert abs(1-phase)>1
            z = [(phases[(u*i)%n]-phase)*v for i,v in enumerate(row)]
            mask = [int(signs[j]==signs[(j+u)%n]==-sector) for j in range(n)]
            # The conjugate change of DFT direction uses z with the plus phase.
            transform = acb.dft(z,inverse=True)
            assert all(transform[j].contains(0) for j,yes in enumerate(mask) if yes)
            outside = 1-sum(row[residue::size])
            assert row[0]*(arb(n)/4-root-2) < 2*outside*(root+2)
            coset_tests += 1

    records = []
    for threshold in (arb(1)/20, arb(1)/4, arb(3)/4):
        peaks = [x for x in range(1,n) if abs(F[x])>threshold or abs(H[x])>threshold]
        assert all(max(abs(F[x]),abs(H[x]))<threshold for x in range(1,n) if x not in peaks)
        multipliers = [int(x in peaks)*sign for x,sign in enumerate(signs)]
        k_peak = [z.real*n/root for z in acb.dft(multipliers,inverse=True)]
        actual = p*dot(k_peak,[u*v for u,v in zip(U,V)])/n
        formula = sum((signs[x]*(1-F[x]-H[x])/root for x in peaks),arb(0))
        assert (actual-formula).contains(0)
        records.append(dict(threshold=units(threshold),selected=len(peaks),
                            negative_selected=sum((F[x]+H[x])<0 for x in peaks),
                            scaled_signed_cubic=units(actual)))
    powers = [x*x*x*x*x*x*x for x in F]
    seventh = sum(powers)/n
    overlap0 = n*seventh*b
    q7 = [z.real for z in acb.dft(powers,inverse=True)]
    assert all(z.lower()>=0 or z.contains(0) for z in q7)
    assert (overlap0+n*dot(q7[1:],r[1:])-1).contains(0)
    # Compare Kneser's product bound for several thresholds including nontrivial heads.
    tested = 0
    h = (1+isqrt(1+4*n))//2
    for f in [F,H]:
        for order in (1,2,3,4):
            threshold = arb(1)-arb(1)/(5*order**2)
            head = [i for i, v in enumerate(f) if abs(v)>threshold]
            assert all(abs(v)<threshold for i,v in enumerate(f) if i not in head)
            words = {0}
            for _ in range(order):
                words = {(u+v)%n for u in words for v in head}
            assert all(signs[(u-v)%n] == (side if f is F else -side)
                       for u in words for v in words if u != v)
            assert len(words)<=h
            if 2*h<order*len(head):
                assert all((u+v)%n in words for u in words for v in words)
            tested += 1
    return dict(prime=p,side=side,bits=ctx.prec,units="1e-9",fibers=n-1,
                marked_cubic_output_modes=n-1,thresholds=records,product_sets=tested,
                off_mark_coset_tests=coset_tests,
                displacement_flat_cubic=units(fiber_sum),seventh_overlap_at_root=units(overlap0),
                seventh_normalized_mark=units(seventh*arb(n).sqrt()))


if __name__=="__main__":
    for prime in (53,101,257,409,769):
        print(json.dumps(audit(prime),sort_keys=True),flush=True)
