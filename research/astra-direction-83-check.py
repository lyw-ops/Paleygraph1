"""Arb lower certificates for three cold packet comparison obstructions."""
import json
import runpy
from pathlib import Path
from flint import acb, arb, arb_mat, arb_poly, ctx

source = Path(__file__).resolve().parent
fields = runpy.run_path(str(source / 'astra-joint-65-check.py'))
ctx.prec = 192
base = arb(2031)/128
half = arb(1)/2**17
square = acb(arb(base,half),arb(0,half))

def upper_kernels(t,lam):
    global n,degree,strip,kernels
    ctx.prec=192
    rows, _ = fields['upper'](t)
    ctx.prec=224
    n,degree,strip=36,10,36
    kernels=[]
    for j,row in enumerate(rows[:degree+1]):
        entries=[(x.lower()*(lam if j==0 else 1)).lower() for x in row[:strip+1]]
        assert all(x>=0 for x in entries) and len(entries)==strip+1
        sides=[x/2 for x in entries[1:]]
        kernels.append(arb_poly(sides[::-1]+[entries[0]]+sides))

def value_and_derivative(h):
    sides = [x/2 for x in h]
    packet = arb_poly(sides[::-1]+[sum(i*x for i,x in enumerate(h))]+sides)
    powers = [arb_poly([1])]
    for _ in range(degree):
        powers.append(powers[-1]*packet)
    value = [arb(0)]*n
    shift = [arb(0)]*(2*n+1)
    for j, kernel in enumerate(kernels):
        term = kernel*powers[j]; center = strip+j*n
        for k in range(1,n+1):
            value[k-1] += 2*term[center+k]
        if j:
            term = j*kernel*powers[j-1]; center -= n
            for k in range(2*n+1):
                shift[k] += term[center+k]
    mat = arb_mat([[2*(l-1)*shift[k]+shift[abs(k-l)]+shift[k+l]
                    for l in range(1,n+1)] for k in range(1,n+1)])
    return value, mat

def positive(v): return all(x>0 for x in v.entries())

def record(**values): print(json.dumps(values),flush=True)

def obstruct(kind,lam,discount=1):
    h=[arb(0)]*n
    for step in range(20):
        image, derivative = value_and_derivative(h)
        gap = arb_mat([[x-y] for x,y in zip(image,h)])
        assert all(y>=0 for y in gap.entries()) and gap[0,0]>0
        ident = arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
        delta = (ident-derivative).solve(gap)
        if positive(-delta):
            assert positive(gap)
            v = -delta
            factor = min((a/b).lower() for a,b in zip((derivative*v).entries(),v.entries()))
            assert factor>arb('1.000001')
            record(kind=kind,forcing_parameter=str(lam),kernel_multiplier=str(discount),
                   packets=n,arities=degree,strip=strip,newton_lower_steps=step,
                   first_packet_lower=str(h[0]),right_expansion_lower=str(factor),
                   minimum_tangent_defect=str(min(a.lower() for a in gap.entries())))
            break
        assert positive(delta)
        if not positive(gap):
            gauge=(ident-derivative).solve(arb_mat([[arb(1)/2**k] for k in range(n)]))
            assert positive(gauge)
        # (I-D) delta = gap > 0 certifies rho(D)<1. The true linear solve is
        # therefore dominated by any unknown x-h with (I-D)(x-h)>=gap.
        h=[((a+arb(19)/20*b)*2**140).lower().floor()/2**140 for a,b in zip(h,delta.entries())]
    else:
        raise AssertionError('no expanding tangent')

original=arb(998960)/10**6
upper_kernels(square,original)
obstruct('undivided_upper_square_no_supersolution', original)

# Nine-center actual complete one-vertex comparison at the central real floor.
# These are genuine lower polynomials after debiting possible cancellations
# by the R65 arithmetic projection, not the preceding upper-polynomial model.
ctx.prec=192
mag=abs(fields['selected'](acb(fields['prev']['t0'])))
rows=fields['lower'](fields['lower_data'](),mag)
ctx.prec=224
n,degree,strip=28,9,18
true_lambda=arb(9997521)/10**7
kernels=[]
for j,row in enumerate(rows):
    # Keep a symmetric lower measure even if finite-precision endpoint
    # extraction had different widths on two reflected atoms.
    atoms=[(min(row[strip+k].lower(),row[strip-k].lower())*(true_lambda if j==0 else 1)).lower() for k in range(strip+1)]
    assert all(x>=0 for x in atoms)
    kernels.append(arb_poly(atoms[:0:-1]+atoms))
obstruct('actual_one_vertex_model_no_supersolution_at_center',true_lambda)

# A second obstruction at lambda=1 grants the rule a discount on *all*
# its nonnegative arity contributions, before applying each vertex.
all_discount=arb(99999)/10**5
kernels=[]
for j,row in enumerate(rows):
    atoms=[(min(row[strip+k].lower(),row[strip-k].lower())*all_discount).lower() for k in range(strip+1)]
    kernels.append(arb_poly(atoms[:0:-1]+atoms))
obstruct('actual_one_vertex_parameter_one_uniform_kernel_discount',1,all_discount)
