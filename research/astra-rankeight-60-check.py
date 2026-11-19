"""Exact weight obstructions and Arb disjoint-pair signed-return obstruction."""
from collections import Counter
import json
from pathlib import Path
from itertools import product
import runpy

from flint import arb, acb, arb_poly, ctx, fmpz_poly

last = runpy.run_path(str(Path(__file__).with_name("astra-crossnode-59-check.py")))
kern = last["previous"]
weights = last["WEIGHTS"]
gt = last["gt"]


def divides(spectrum):
    low = min(spectrum)
    count = Counter(v - low for v in spectrum)
    poly = fmpz_poly([count[j] for j in range(max(count)+1)])
    target = fmpz_poly([2, 0, 4, 0, 2])
    # All shifts of an additional factor differ by integers, since all its
    # weights can be added to one fixed first weight in the product.
    quotient, remainder = divmod(target, poly)
    return not remainder and all(n >= 0 for n in quotient.coeffs())


def independence():
    pairs = []
    for i in (0,1):
        for degree in (1,3,7):
            pairs.append((f"SL2-{i}-sym{degree}", [sorted(gt((degree,0),weights[i^k]).elements()) for k in (0,1)]))
    for i in (2,3):
        pairs.append((f"SL3-{i}-adjoint", [sorted(gt((2,1,0),weights[i^k]).elements()) for k in (0,1)]))
    for i in range(4,8):
        pairs.append((f"SL4-{i}", [weights[i^k] for k in (0,1)]))
    pairs.extend([("new-Sp4-0", [(-4,0,0,4), (0,0,0,0)]),
                  ("new-Sp4-1", [(0,0,0,0), (-4,0,0,4)]),
                  ("new-SL4", [(-4,0,0,0), (0,0,0,4)])])
    out = {}
    for key,rows in pairs:
        fails = [i for i,r in enumerate(rows) if not divides(r)]
        assert fails
        assert fails == [i for i,r in enumerate(rows) if not divides([-v for v in r])]
        out[key] = fails
    # Both full twists of N * N^chi have the same lists before and after T.
    inputs = [tuple(sorted(i+j for i in weights[0] for j in weights[1]))]*2
    after = last["activation"](inputs)
    assert after[0] == after[1] == (-2,-2,0,0,0,0,2,2)
    return dict(kind="rank_eight_shared_simple_factor_exclusions", input=inputs[0],
                output=after[0], rejected_full_twists=out)


def tensor_alternative():
    # Integer adjoint exponents 2a,2b,2c can also be read from
    # differences of the integer weights in the triple standard.
    target = [-2,-2,0,0,0,0,2,2]
    solutions = set()
    for abc in product(range(5),repeat=3):
        vals = sorted(sum(v*w for v,w in zip(abc,signs)) for signs in product((-1,1),repeat=3))
        if vals==[2*x for x in target]:
            solutions.add(tuple(sorted(abc)))
    assert solutions=={(0,2,2)}
    possible_other = [(0,0,0),(-2,0,2)]
    ranks = [sum(map(abs,row))//2 for row in possible_other]
    assert max(ranks)<3
    return dict(kind="tensor_SL2_cube_conductor_obstruction", adjoint_highest_weights=[0,2,2],
                inactive_factor_ranks=ranks, convolution_dimension=3, rank_lower_by_drop=3,
                Haar_quadratic_moment=1, Haar_fourth_moment=3)


def norm_one(p,d):
    finite = runpy.run_path(str(Path(__file__).with_name("astra-prime-phase-32-check.py")))
    u=p**d
    field,ell,_,_ = finite["data"](p,2*d)
    conv=finite["cycconv"]
    q=field.q
    n=[a*b for a,b in zip(ell,conv(ell,ell))]
    nchi=[(-1)**i*x for i,x in enumerate(n)]
    source=conv(n,nchi)
    assert all(source[i]==0 for i in range(1,q-1,2))
    sym=conv(n,n)
    sym=[v+2*(q+1)-(q*q if i==0 else 0) for i,v in enumerate(sym)]
    B=[j*(u-1) for j in range(u+1)]
    weighted_source=sum((-1)**j*source[i] for j,i in enumerate(B))
    sympull=sum(sym[2*i%(q-1)] for i in B)
    symregular=sum(sym[i] for i in B)
    assert weighted_source==q*q+sympull-symregular
    assert all(ell[i]==-(-1)**j for j,i in enumerate(B) if i)
    total=sum(ell[i]*source[i] for i in B)
    assert total==-weighted_source+source[0]
    return dict(kind="finite_norm_one_sign_identity",base=u,extension=q,
                denominator=q*q,rank_eight_sum_numerator=total,
                sym_pullback_sum_numerator=sympull,sym_sum_numerator=symregular,
                removed_identity_numerator=source[0])


def escape():
    t = arb(2031)/128
    size, shift = 28, 18
    lower = kern["new_kernels"](t,shift=shift)
    upper,a,b,c,d = kern["make"](acb(t))
    M = kern["dim"]+2*a+3*b+4*c+arb(23)*d/4
    # Full arity tails at radius 1, and the coefficientwise geometric tail.
    ratio = (M+1)**2/(4*t)
    coeff = arb(1)
    for r in range(1,16):
        coeff *= (arb(3)/2-r)/r
    tail = 2*t.sqrt()*abs(coeff)*ratio**15/(1-ratio)
    assert ratio<1
    def cap(j,k):
        k = abs(k)
        return (upper[j][k]/(2 if k else 1) if k<len(upper[j]) else 0) + tail
    def nonleading(k):
        return cap(1,k)-(arb(169624)/10**6 if abs(k)==1 else 0)
    assert all(nonleading(k)>=0 for k in range(-2,size+3))
    u = arb(30611)/10**9
    a4,b4,c8 = [arb(x)/10**9 for x in (900251,850223,1700513)]
    unit = 2*a4**2 + 2*b4**2 + c8**2
    Z = 8*(a4+b4+c8)
    assert Z<arb(28)/1000
    # For degree >=4, debit the entire tagged mass, irrespective of the
    # particular old constituents and their shifts, separately at every bin.
    # The unsigned total preactivation coefficients of arity j have upper
    # bound 2 sqrt(t) times [x^j] sum |binomial(1/2,r)| ((M+x)^2/(4t))^r.
    # Nonnegative tails after small degrees can use a Cauchy bound at radius 1.
    allj = 2*t.sqrt()/(1-ratio)
    rem = arb(0)
    for j in range(4,9,2):
        rem += Z**j*(sum(upper[j])+tail)
    rem += Z**10*allj/(1-Z)
    assert rem < arb(1)/10**9
    debit = [4*u*(nonleading(k)+(nonleading(k-2)+nonleading(k+2))/2)
             +2*unit*cap(2,k)+2*rem for k in range(size+1)]
    assert lower[2][shift] > arb(1)/20
    h = [arb(0)] * size
    for height in range(1,8501):
        side = [v/2 for v in h]
        base = arb_poly(side[::-1]+[sum(j*v for j,v in enumerate(h))]+side)
        power = arb_poly([1])
        out = [arb(0)]*size
        for j, row in enumerate(lower):
            if j:
                power *= base
            conv = row*power
            for k in range(1,size+1):
                out[k-1] += 2*conv[shift+j*size+k]
        h = [max(arb(0),(v-2*debit[k+1]*(height%2==0)).lower()) for k,v in enumerate(out)]
        if sum(i*v for i,v in enumerate(h,1))>21:
            return dict(kind="all_pure_tag_old_returns_escape",floor="2031/128",height=height,
                        rank_four_and_eight_sources=3, unlimited_even_return_degrees=True,
                        full_C2_unary=True, full_old_outer_multipliers=True, packets=size,
                        arities=len(lower)-1, shifts=shift, mass_lower=21, precision=ctx.prec,
                        size_four_or_more_mass_upper="1e-9")
    raise AssertionError("no certified escape")


if __name__=="__main__":
    for test in (independence,tensor_alternative,lambda:norm_one(5,1),lambda:norm_one(3,2),
                 lambda:norm_one(13,1),lambda:norm_one(5,2),escape):
        print(json.dumps(test(),sort_keys=True),flush=True)
