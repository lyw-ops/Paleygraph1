"""Two-vertex signature, signed matrix-coefficient, and escape certificates."""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from flint import arb, acb, arb_poly, ctx
from pathlib import Path
import json
import runpy

previous = runpy.run_path(str(Path(__file__).with_name('astra-ranknext-58-check.py')))
gt = previous['prior']['gt']
WEIGHTS = (
    (-2, 2), (0, 0), (-1, -1, 3), (-1, 0, 0),
    (-2, -2, 1, 1), (0, 0, 0, 2), (0, 0, 0, 0), (-2, -1, -1, 4),
    (-3, -3, 1, 1, 1, 3), (0,)*6,
    (-1, -1, 0, 0, 1), (-1, -1, -1, 2, 2),
    (-1, -1, -1, -1, 5), (-1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 3), (-3, -2, -2, 1, 1, 1, 1),
)
DETS = (0, 0, -1, 1, 2, -2, 0, 0, 0, 0, 1, -1, -1, 1, -3, 3)
EMPTY = ((0,),)*len(WEIGHTS)

@lru_cache(None)
def fiber(shapes, twist):
    a = Counter({0:1})
    for i, p in enumerate(shapes):
        if p==(0,):
            continue
        weights = WEIGHTS[i^twist]
        b = gt(p+(0,)*(len(weights)-len(p)), weights)
        c = Counter()
        for u, v in a.items():
            for w, x in b.items():
                c[u+w] += x*v
        a = c
    return tuple(sorted(a.elements()))

def twists(shapes, e):
    return tuple(tuple(w + (e if twist else -e) for w in fiber(shapes,twist)) for twist in (0, 1))

def activation(two):
    rank = sum(abs(w) for row in two for w in row)//2
    rows = []
    for twist in (0,1):
        row = [w for w in two[twist] if w<0] + [w for w in two[1-twist] if w>0]
        assert len(row)<=rank
        rows.append(tuple(sorted(row+[0]*(rank-len(row)))))
    return tuple(rows)

def outer(two, sign):
    return tuple(tuple(w + (sign if twist else -sign) for w in row) for twist,row in enumerate(two))

def label(kind):
    if kind=='C4':
        return EMPTY,4
    if kind=='sym':
        return ((2,),)+EMPTY[1:],0
    if kind=='AB':
        return ((1,),(1,))+EMPTY[2:],0

def small_shapes():
    # Weyl's dimension formula leaves precisely these ways of making 4 and 8.
    result = defaultdict(set)
    for degree in (4, 8):
        for a in range(degree):
            for b in range(degree):
                if (a+1)*(b+1)==degree:
                    result[degree].add(((a,),(b,))+EMPTY[2:])
    for i in range(4,8):
        for p in ((1,), (1,1,1)):
            s = EMPTY[:i]+(p,)+EMPTY[i+1:]
            result[4].add(s)
            for a in (0,1):
                result[8].add(s[:a]+((1,),)+s[a+1:])
    for i in (2,3):
        result[8].add(EMPTY[:i]+((2,1),)+EMPTY[i+1:])
    return result

def signature_control():
    shapes = small_shapes()
    assert [len(shapes[i]) for i in (4,8)]==[11,22]
    out = []
    for kind in ('C4','sym','AB'):
        s,e = label(kind)
        rows = activation(twists(s,e))
        rank = len(rows[0])
        norm = lambda h: sum(abs(w) for row in outer(rows,h) for w in row)
        # Convexity of the absolute sum implies a unique integer minimizer.
        assert norm(-1)>norm(0)==2*rank<norm(1)
        # A free Jacobi twist of an old constituent absorbs any outer m shift.
        for candidate in shapes[rank]:
            left = fiber(candidate,0)
            assert len(left)==rank
            diff = sum(left)-sum(rows[0])
            if diff%rank==0:
                assert twists(candidate,diff//rank)!=rows
        out.append(dict(target=kind,rank=rank,unit_shift_norms=[norm(h) for h in (-1,0,1)]))
    return dict(kind="all_Jacobi_two_vertex_rigidity",old_labels_by_dimension=[11,22],rows=out)


def scalar_powers(families,degree,perverse):
    tab = [Counter({0:1})]+[Counter() for i in range(degree)]
    for d,e in families:
        vals = [previous['single_scalars'](d,e,k) for k in range(degree+1)]
        new = [Counter() for k in range(degree+1)]
        for k in range(degree+1):
            for j in range(k+1):
                for u,x in vals[j].items():
                    sign = -1 if not perverse and u%2 else 1
                    for v,y in tab[k-j].items():
                        new[k][u+v] += comb(k,j)*sign*x*y
        tab = new
    return tab

def add_inputs(old,new):
    n = len(old)-1
    out = [defaultdict(lambda: arb(0)) for _ in range(n+1)]
    for k in range(n+1):
        for j in range(k+1):
            for u,x in new[j].items():
                for v,y in old[k-j].items():
                    out[k][u+v] += comb(k,j)*x*y
    return out

def signed_coefficients():
    degree=24
    t=arb(2031)/128
    a,b,g,unused=previous['p3']['coefficients'](acb(t),acb(-arb(7)/100000),acb(-arb(6)/100000))
    c=arb(499)/500*b*g[1,1][0,0]
    d=-2*c*previous['linear_scalar'](g,b)
    a,b,c,d=[x.real for x in (a,b,c,d)]
    s=previous['dim']
    table=[{2*i-k:comb(k,i)*(s/2)**k for i in range(k+1)} for k in range(degree+1)]
    for first,last,prefactor,perverse in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
        factors=[(len(WEIGHTS[i]),DETS[i]) for i in range(first,last)]
        raw=scalar_powers(factors,degree,perverse)
        weighted=[{e:v*prefactor**k for e,v in row.items()} for k,row in enumerate(raw)]
        table=add_inputs(table,weighted)
    mass = s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4
    ratio=mass**2/(4*t)
    assert ratio<1
    result={}
    targets = [(4,0,0,0,'C4'), (0,2,0,0,'sym'), (0,1,1,0,'AB'),
               (1,0,0,1,'outer_m'), (2,0,0,0,'inner_m2'),
               (1,1,0,0,'direct_mA'), (2,1,0,1,'outer_m2A')]
    for k,u,v,j,name in targets:
        leg=previous['p3']['P']
        row=add_inputs(table,[{0:a**i*leg[i].get((u,v),0)} for i in range(degree+1)])
        coeff=arb(0)
        binom=arb(1)
        for ell in range(1,degree//2+1):
            binom *= (arb(3)/2-ell)/ell
            coeff += 2*t.sqrt()*binom/(4*t)**ell*comb(2*ell,j)*row[2*ell-j].get(k,0)
        ell=degree//2+1
        binom *= (arb(3)/2-ell)/ell
        lead=2*t.sqrt()*abs(binom)*ratio**ell
        if j==0:
            tail=lead/(1-ratio)
        else:
            tail=2*lead/mass*(ell/(1-ratio)+ratio/(1-ratio)**2)
        if name=='inner_m2':
            coeff-=a/2
        elif name=='direct_mA':
            coeff-=b/4
        result[name]=coeff+arb(0,tail.upper())
    return result

def coefficient_record():
    coeffs = signed_coefficients()
    bounds = {'C4':(-900251,-900249),'sym':(850221,850223),'AB':(1700511,1700513),
              'outer_m':(169624600,169624620),'inner_m2':(30609,30611),
              'direct_mA':(14262,14264),'outer_m2A':(-620412,-620408)}
    for key,(lo,hi) in bounds.items():
        assert lo < 10**9*coeffs[key] < hi
    u, d = coeffs['inner_m2'], coeffs['outer_m2A']
    assert 0<u*(1+2*d)
    reduction = -4*u*d
    assert arb(75)/10**9 < reduction < arb(77)/10**9
    return dict(kind='signed_arithmetic_paths',floor='2031/128',precision=ctx.prec,
                taylor_degree=24,intervals_billionths=bounds,
                contraction_saving_per_sign_billionths=[75,77])

def escape_test(whole=False):
    shift=18
    size=28
    kernels=previous['new_kernels'](arb(2031)/128,shift=shift)
    cost=arb(8)/10**8
    debits=[arb(0)]*(size+1)
    debits[2]=cost
    if whole:
        t=arb(2031)/128
        rows,a,b,c,d=previous['make'](acb(t))
        vals=rows[1]
        radius=arb(1)
        mass=previous['dim']+2*a+3*b+4*c+arb(23)/4*d+radius
        ratio=mass**2/(4*t)
        binom=arb(1)
        for j in range(1,16):
            binom*=(arb(3)/2-j)/j
        assert ratio<1
        tail=2*t.sqrt()*abs(binom)*ratio**15/((1-ratio)*radius)
        def at(w):
            return vals[abs(w)]/(2 if w else 1)+tail-(arb(169624)/10**6 if abs(w)==1 else 0)
        assert all(at(w)>=0 for w in range(-2,size+3))
        debits=[4*arb(30611)/10**9*(at(k)+(at(k-2)+at(k+2))/2) for k in range(size+1)]
    # Combine the two signs, and subtract once at each grouped parent.
    assert kernels[2][shift]>arb(1)/20
    h=[arb(0)]*size
    for height in range(1,5001):
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(j*v for j,v in enumerate(h))]+side)
        power=arb_poly([1])
        out=[arb(0)]*size
        for j,ker in enumerate(kernels):
            if j: power*=base
            row=ker*power
            for k in range(1,size+1): out[k-1]+=2*row[shift+j*size+k]
        h=[max(arb(0),(v-2*debits[i+1]*(height%2==0)).lower()) for i,v in enumerate(out)]
        if sum(i*v for i,v in enumerate(h,1))>21:
            return dict(kind='two_vertex_signed_escape',floor='2031/128',height=height,
                        all_unary_channels=whole,quadratic_zero_lower='1/20',
                        packets=size,arities=len(kernels)-1,shifts=shift,mass_lower=21)
    raise AssertionError('missing escape')

if __name__=='__main__':
    for calculate in (signature_control, coefficient_record, escape_test, lambda: escape_test(True)):
        print(json.dumps(calculate(),sort_keys=True),flush=True)
