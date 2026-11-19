"""Arb interval proof with the third distinguished field and GL4 determinant collection."""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import runpy
from flint import acb, arb, arb_poly, ctx

p3 = runpy.run_path(str(Path(__file__).with_name("astra-rankthree-56-check.py")))
D, W, SEED = (p3[k] for k in ("D","W","SEED"))
F = arb_poly([arb(1)/8,0,arb(1)/2,arb(1)/2,arb(7)/4,arb(1)/2,arb(1)/2,0,arb(1)/8])
WEIGHTS = ((-2,-2,1,1),(0,0,0,2),(0,0,0,0),(-2,-1,-1,4))
DETS = (2,-2,0,0)
ZERO = ((0,0,0,0),)*4

@lru_cache(None)
def four_powers(degree):
    if not degree:
        return {(ZERO,0):1}
    out=Counter()
    for (factors,e),mult in four_powers(degree-1).items():
        for i,part in enumerate(factors):
            for s in (-1,1):
                for row in range(4):
                    a=list(part)
                    a[row]+=s
                    if a!=sorted(a,reverse=True):
                        continue
                    shift=a[3]
                    shape=tuple(t-shift for t in a)
                    result=factors[:i]+(shape,)+factors[i+1:]
                    out[result,e+DETS[i]*shift]+=mult
    return out

@lru_cache(None)
def gt(shape,weights):
    if len(shape)==1:
        return {shape[0]*weights[0]:1}
    from itertools import product
    out=Counter()
    for child in product(*(range(lo,hi+1) for lo,hi in zip(shape[1:],shape[:-1]))):
        shift=(sum(shape)-sum(child))*weights[-1]
        for k,v in gt(child,weights[:-1]).items():
            out[k+shift]+=v
    return out

@lru_cache(None)
def four_fiber(shapes,twist=0):
    fiber=Counter({0:1})
    for i,s in enumerate(shapes):
        row=gt(s,WEIGHTS[i^twist])
        out=Counter()
        for k,v in fiber.items():
            for l,w in row.items():
                out[k+l]+=v*w
        fiber=out
    return fiber

def four_control():
    model=Counter({-4:1,-2:4,-1:4,0:14,1:4,2:4,4:1})
    expected=Counter({0:1})
    for h in range(5):
        for twist in (0,1):
            out=Counter()
            for (shapes,e),mult in four_powers(h).items():
                for k,v in four_fiber(shapes,twist).items():
                    out[k+e*(1 if twist else -1)]+=mult*v
            assert out==expected
        nex=Counter()
        for k,v in expected.items():
            for l,w in model.items():
                nex[k+l]+=v*w
        expected=nex
    assert {e:v for (f,e),v in four_powers(4).items() if f==ZERO}=={-2:2,0:196,2:2}
    return dict(kind="rank_four_Pieri_and_boundary",degrees=[0,1,2,3,4],twists=[1,"chi"],
                quadratic_unit=four_powers(2)[ZERO,0],quartic_scalars=[2,196,2],dimension_base=32)

def make(t,L=3,A=2,E=5,J=4,central=3,da=0,db=0,gfrac=1,lower=False):
    alpha,beta,g,amendments=p3["coefficients"](t,acb(da),acb(db))
    gamma=gfrac*beta*g[1,1][0,0]
    pieces=p3["rank_powers"](L)
    raw=[]
    rem=[]
    for r in range(D+1):
        n=2*(D-r)
        vals=[arb(0)]*(2*n+1)
        odds=[arb(0)]*(2*n+1)
        for k in range(D-r+1):
            items=amendments[k] if r==0 and k in amendments else g[r,k]
            for (u,v),value in items.items():
                price=abs(value).upper()*(v+1)/(2 if k else 1)
                for w in range(-2*u,2*u+1,4):
                    for e in ((-k,k) if k else (0,)):
                        vals[n+w+e]+=price
                        if k>E or u+v>A:
                            odds[n+w+e]+=price
        raw.append(arb_poly(vals))
        rem.append(arb_poly(odds))
    wp=[W**i for i in range(D+1)]
    bp=[(beta/4)**i for i in range(L+1)]
    older=[]
    older_low=[]
    extracted=[]
    for r in range(D+1):
        n=3*(D-r)
        row=arb_poly()
        for l in range(D-r+1):
            source=rem if r<=J and l<=L else raw
            row+=(source[r+l]*wp[l]).left_shift(n-2*(D-r-l)-3*l)*(comb(r+l,r)*abs(beta).upper()**l)
        positive_complement=row
        core_lower=arb_poly()
        scalars={}
        if r<=J:
            for u in range(A+1):
                for v in range(A+1-u):
                    collected=defaultdict(lambda:acb(0))
                    for l in range(min(L,D-r)+1):
                        for k in range(min(E,D-r-l)+1):
                            items=amendments[k] if r+l==0 and k in amendments else g[r+l,k]
                            val=items.get((u,v),0)
                            if (r,l,k,u,v)==(0,1,1,0,0):
                                val=val*(1-gfrac)
                            if val==0: continue
                            x=val*comb(r+l,r)*bp[l]/(2 if k else 1)
                            for (a,b,c,d,m),mult in pieces[l].items():
                                for e in ((m-k,m+k) if k else (m,)):
                                    collected[a,b,c,d,e]+=x*mult
                    vals=[arb(0)]*(2*n+1)
                    lows=[arb(0)]*(2*n+1) if lower else []
                    for (a,b,c,d,e),value in collected.items():
                        if (u,v,a,b,c,d)==(0,)*6 and abs(e)<=central:
                            scalars[e]=value
                            continue
                        price=abs(value).upper()*(v+1)
                        floor=abs(value).lower()*(v+1) if lower else None
                        for w,mult in p3["pair_fiber"](a,b,c,d):
                            for i in range(-2*u,2*u+1,4):
                                vals[n+w+i-e]+=price*mult
                                if lower:
                                    lows[n+w+i-e]+=floor*mult
                    row+=arb_poly(vals)
                    if lower:
                        core_lower+=arb_poly(lows)
        older.append(row)
        if lower:
            assert central < 0
            older_low.append(arb_poly([max(arb(0),(core_lower[i]-positive_complement[i]).lower()) for i in range(2*n+1)]))
        extracted.append(scalars)
    if lower:
        return older_low,older,alpha,beta,gamma
    # On the extracted older scalar characters, pool every degree-two GL4
    # summand and the degree-four arithmetic lines with degree zero.
    fp=[F**h for h in range(D+1)]
    quartic=arb_poly([arb(2)/4096,0,arb(196)/4096,0,arb(2)/4096]).left_shift(14)
    kernels=[]
    for j in range(D+1):
        n=4*(D-j)
        row=arb_poly()
        pooled=defaultdict(lambda:acb(0))
        for h in range(D-j+1):
            r=j+h
            mult=comb(r,j)*gamma**h
            row+=(older[r]*fp[h]).left_shift(n-3*(D-r)-4*h)*abs(mult).upper()
            for e,value in extracted[r].items():
                x=mult*value
                if h in (0,2,4):
                    for (shape,shift),v in (four_powers(h).items() if h<=2 else
                                           [((ZERO,-2),2),((ZERO,0),196),((ZERO,2),2)]):
                        pooled[shape,e+shift]+=x*v/(8**h)
                if h not in (0,2):
                    factor=fp[h]-quartic if h==4 else fp[h]
                    row+=factor.left_shift(n-4*h-e)*abs(x).upper()
        vals=[arb(0)]*(2*n+1)
        for (shape,e),x in pooled.items():
            for k,v in four_fiber(shape).items():
                vals[n+k-e]+=abs(x).upper()*v
        row+=arb_poly(vals)
        kernels.append([row[n+k]*(2 if k else 1) for k in range(n+1)])
    return kernels,*[abs(x).upper() for x in (alpha,beta,gamma)]

def envelope(first,last,div,width):
    result=None
    caps=[arb(0)]*3
    for i in range(first,last):
        t=acb(p3["old"]["prev"]["warm"]["slab"](i,div),arb(0,arb(1)/width))
        kernels,*abc=make(t,4,3,7,6,3,-arb(7)/100000,-arb(6)/100000,arb(499)/500)
        if result is None:
            result=kernels
        else:
            result=[[max(v,w) for v,w in zip(a,b)] for a,b in zip(result,kernels)]
        caps=[max(v,w) for v,w in zip(caps,abc)]
    return result,*caps

def rectangle(first,last,caps,max_leak):
    div,width=65536,65536
    kernels,a,b,c=envelope(first,last,div,width)
    return validate(first,last,div,width,kernels,a,b,c,caps,max_leak)

def validate(first,last,div,width,kernels,a,b,c,caps,max_leak):
    low=arb(first)/div
    high=abs(acb(arb(last)/div,arb(1)/width))
    h=[arb(v)/10**14 for v in caps]
    eps=arb(6)/10**7
    eta=arb(1)/5
    zero=sum(i*v for i,v in enumerate(h))+eps/eta+arb(1)/10**8
    base=arb_poly([v/2 for v in reversed(h)]+[zero]+[v/2 for v in h])
    norm=zero+sum(v*(eta*k).cosh() for k,v in enumerate(h,1))
    leak=arb(0)
    n=len(h)
    pooled=[arb(0)]*(D*n+4*D+1)
    power=arb_poly([1])
    for j,ker in enumerate(kernels):
        if j: power*=base
        side=[v/2 for v in ker[1:]]
        row=power*arb_poly(side[::-1]+[ker[0]]+side)
        center=j*n+len(side)
        for i in range(1,len(row)-center):
            pooled[i]+=2*row[center+i]
        if j:
            leak+=sum(v*(eta*k).cosh() for k,v in enumerate(ker))*j*(norm+eps)**(j-1)*eps
    for k,v in enumerate(pooled[1:],1):
        cap=h[k-1] if k<=n else arb(0)
        leak+=max(arb(0),(v-cap).upper())*(eta*k).cosh()
    f_norm=arb(7)/4+eta.cosh()+(2*eta).cosh()+(4*eta).cosh()/4
    total=SEED*eta.cosh()+a*(1+(2*eta).cosh())+b*(1+3*eta.cosh()/2+(3*eta).cosh()/2)+c*f_norm+norm+eps
    ratio=total**2/(4*low)
    assert ratio<1
    binom=arb(1)
    for ell in range(1,D//2+2):
        binom*=(arb(3)/2-ell)/ell
    leak+=2*high.sqrt()*abs(binom)*ratio**(D//2+1)/(1-ratio)
    full=SEED+2*a+3*b+4*c+zero+sum(h)+eps
    if not max_leak:
        return float(leak),float(full),float(ratio)
    full_cap=arb(468)/100
    assert leak < arb(max_leak)/10**9 < eps
    assert full < full_cap
    assert full_cap/(4*low-full_cap**2).sqrt()<arb(3)/4
    return dict(kind="arithmetic_rank_four_marked_rectangle",slabs=[first,last],
                division=div,imaginary_half_width="1/65536",packets=n,
                precision=ctx.prec,residual_cap="6/10000000",residual_output_upper=f"{max_leak}/1000000000",
                full_cap="468/100",older_collection=[4,3,7,6],rank_four_scalar_source_exponent=3)

CAPS=[26132485019342,11447876150297,6042341373196,3062320231738,1564454747207,
      700924557441,329711040386,160601827412,80307348130,40986050007,21263294745,
      11180360127,5944932592,3191250376,1727080563,941311722,516228735,284658615,
      157731218,87781110,49044068,27498725,15468202,8726639,4936599,2799554,
      1591282,906419,517332,295807,169431,97202,55849,32134,18514,10680,6169,
      3567,2065,1197,694,403,234,137,80,47,27,16,9,5]

def escape(num,den,nt=28,shift=18,J=9,L=4):
    t=arb(num)/den
    low,upper,a,b,c=make(acb(t),L,4,D,J+2,-1,-arb(7)/100000,-arb(6)/100000,arb(499)/500,True)
    fp=[F**h for h in range(D+1)]
    # Keep precisely the nontrivial degree-two SU4^4 labels whose determinant
    # exponent has a unique value in this degree.
    quadratic=defaultdict(list)
    for (shape,e),v in four_powers(2).items():
        quadratic[shape].append((e,v))
    kept=Counter()
    for shape,parts in quadratic.items():
        if shape!=ZERO and len(parts)==1:
            e,v=parts[0]
            for w,m in four_fiber(shape).items():
                kept[w-e]+=v*m
    q2=arb_poly([arb(kept[i])/64 for i in range(-8,9)])
    atom=arb_poly([arb(1)/8]).left_shift(8)
    absc=abs(c)
    kernels=[]
    for j in range(J+1):
        n=4*(D-j)
        row=arb_poly()
        for h in range(D-j+1):
            r=j+h
            price=comb(r,j)*absc**h
            if h<2:
                source=low[r]*fp[h]*price.lower()
            elif h==2:
                source=low[r]*q2*price.lower()-upper[r]*atom*price.upper()
            else:
                source= -upper[r]*fp[h]*price.upper()
            row+=source.left_shift(n-3*(D-r)-4*h)
        binom=arb(1)
        for ell in range(1,D//2+2):
            binom*=(arb(3)/2-ell)/ell
        errors=[]
        for h in (1,2,4,8,16,24,32,48,64,80):
            radius=arb(h)/32
            ratio=(SEED+2*abs(a)+3*abs(b)+4*absc+radius)**2/(4*t)
            assert ratio<1
            errors.append(2*t.sqrt()*abs(binom)*ratio**(D//2+1)/((1-ratio)*radius**j))
        error=min(errors)
        side=[max(arb(0),(row[n+k]-error).lower()) for k in range(1,shift+1)]
        zero=max(arb(0),(row[n]-error).lower())
        kernels.append(arb_poly(side[::-1]+[zero]+side))
    assert kernels[2][shift]>arb(1)/20
    h=[arb(0)]*nt
    for height in range(1,4001):
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        power=arb_poly([1])
        out=[arb(0)]*nt
        for j,ker in enumerate(kernels):
            if j: power*=base
            row=ker*power
            for k in range(1,nt+1):
                out[k-1]+=2*row[shift+j*nt+k]
        h=[v.lower() for v in out]
        if sum(i*v for i,v in enumerate(h,1))>21:
            return dict(kind="full_GL4_arithmetic_map_escape",floor=f"{num}/{den}",height=height,
                        arities=J,shifts=shift,packets=nt,maximum_W_degree=L,legendre_degree=4,
                        quadratic_zero_lower="1/20",mass_lower=21,precision=ctx.prec)
    raise AssertionError("finite lower recursion did not escape")

if __name__=="__main__":
    for result in (four_control(),rectangle(1040052,1040130,CAPS,400),
                   escape(2031,128),escape(1015,64)):
        print(json.dumps(result,sort_keys=True))
