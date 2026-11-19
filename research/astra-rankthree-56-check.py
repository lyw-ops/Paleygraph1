"""Arb interval replay for arithmetic GL(3)^2 root collections."""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import runpy
from flint import arb, acb, arb_poly, ctx

old = runpy.run_path(str(Path(__file__).with_name("astra-rankthree-55-check.py")))
D = old["D"]
P = old["P"]
W = old["W"]
ctx.prec = 192
SEED = arb(arb(8).sqrt(), arb(1)/10**12)
old["domain"]["warm"].SEED=SEED
old["prev"]["warm"]["SEED"]=SEED


def pieri(a, b, dual):
    # Highest weights are (a,0,-b).  Last entry is the determinant power.
    if dual:
        if b:
            yield a+1,b-1,-1
        if a:
            yield a-1,b,0
        yield a,b+1,0
    else:
        if a:
            yield a-1,b+1,1
        if b:
            yield a,b-1,0
        yield a+1,b,0


@lru_cache(None)
def rank_powers(order):
    """Integer multiplicities in (4W)^ell. det U=m^-1, det V=m."""
    powers=[{(0,0,0,0,0):1}]
    for ell in range(order):
        new=Counter()
        for (a,b,c,d,m),v in powers[-1].items():
            for dual in (False,True):
                for u,vv,s in pieri(a,b,dual):
                    new[u,vv,c,d,m-s]+=v
                for u,vv,s in pieri(c,d,dual):
                    new[a,b,u,vv,m+s]+=v
        powers.append(dict(new))
    return powers


@lru_cache(None)
def fiber(a,b,first):
    """GL(3) Gelfand--Tsetlin patterns for highest weight (a,0,-b)."""
    table=Counter()
    for u in range(a+1):
        for v in range(-b,1):
            for x in range(v,u+1):
                y=u+v-x
                z=a-b-u-v
                wt=-x-y+3*z if first else -x
                table[wt]+=1
    return table


@lru_cache(None)
def pair_fiber(a,b,c,d):
    table=Counter()
    for x,v in fiber(a,b,True).items():
        for y,w in fiber(c,d,False).items():
            table[x+y]+=v*w
    return sorted(table.items())


def coefficients(t, da, db):
    modes = old["domain"]["laurent"](t,True)
    center=modes[0][2]
    correction=modes[2][2]*center**2/2+da
    alpha=center+correction
    apow=[alpha**h for h in range(D+1)]
    grouped={}
    for r in range(D+1):
        for k in range(D-r+1):
            g=defaultdict(lambda:acb(0))
            for h in range(D-r-k+1):
                if modes[r+h][k]==0:
                    continue
                v=modes[r+h][k]*apow[h]*comb(r+h,r)
                for key,mult in P[h].items():
                    g[key]+=v*mult
            grouped[r,k]=g
    beta=2*grouped[0,1][1,0]+db
    removed=grouped[0,2].copy()
    removed[0,0]=sum((modes[h][2]*apow[h]*P[h].get((0,0),0)
                       for h in range(1,D-1)),acb(0))-correction
    sub1=grouped[0,1].copy()
    sub1[1,0]=sub1[0,1]=-db/2
    amendments={1:sub1,2:removed}
    return alpha,beta,grouped,amendments


def make(t,L=3,A=2,E=5,J=5,lower=False,da=acb(0),db=acb(0)):
    """Explicit signed prefix, followed by a positive complement for upper certificates.
    Lower kernels retain only the prefix and need a separate omitted-tail debit."""
    alpha,beta,g,amendments=coefficients(t,da,db)
    pieces=rank_powers(L)
    bp=[(beta/4)**l for l in range(L+1)]
    # Raw full Legendre sectors and complementary source sectors, without ranks three.
    raw={}
    outside={}
    for (r,k),items in g.items():
        for typ,g0 in ((False,items),(True,amendments[k])) if r==0 and k in amendments else ((False,items),):
            row=defaultdict(lambda:arb(0))
            rem=defaultdict(lambda:arb(0))
            for (u,v),val in g0.items():
                price=abs(val).upper()*(v+1)/(2 if k else 1)
                if not price: continue
                for w in range(-2*u,2*u+1,4):
                    for s in ((-k,k) if k else (0,)):
                        row[w+s]+=price
                        if k>E or u+v>A:
                            rem[w+s]+=price
            raw[r,k,typ]=row
            outside[r,k,typ]=rem
    allrows=[]
    remrows=[]
    for r in range(D+1):
        n=2*(D-r)
        for table,store in ((raw,allrows),(outside,remrows)):
            vals=[arb(0)]*(2*n+1)
            for k in range(D-r+1):
                for i,val in table[r,k,r==0 and k in amendments].items():
                    vals[n+i]+=val
            store.append(arb_poly(vals))
    # r=0 is used with distinguished subtraction only when j=ell=0.
    Wpowers=[W**l for l in range(D+1)]
    out=[]
    endpoint=arb.lower if lower else arb.upper
    for j in range(D+1):
        n=3*(D-j)
        row=arb_poly()
        debit=arb_poly()
        if lower and j<=J:
            assert E>=D
            for l in range(L+1,D-j+1):
                weighted=(allrows[j+l]*Wpowers[l]).left_shift(n-2*(D-j-l)-3*l)
                debit+=weighted*(comb(j+l,j)*abs(beta).upper()**l)
        if not lower:
            for l in range(D-j+1):
                source=(remrows if j<=J and l<=L else allrows)[j+l]
                row+=(source*Wpowers[l]).left_shift(n-2*(D-j-l)-3*l)*(comb(j+l,j)*abs(beta).upper()**l)
        if j<=J:
            for u in range(A+1):
                for v in range(A+1-u):
                    collected=defaultdict(lambda:acb(0))
                    for l in range(min(L,D-j)+1):
                        for k in range(min(E,D-j-l)+1):
                            items=amendments[k] if not j+l and k in amendments else g[j+l,k]
                            val=items.get((u,v),0)
                            if val==0: continue
                            coeff=val*comb(j+l,j)*bp[l]/(2 if k else 1)
                            for (a,b,c,d,m),mult in pieces[l].items():
                                x=coeff*mult
                                for e in ((m-k,m+k) if k else (m,)):
                                    collected[a,b,c,d,e]+=x
                    weights=defaultdict(lambda:arb(0))
                    for (a,b,c,d,e),value in collected.items():
                        price=endpoint(abs(value))*(v+1)
                        for w,mult in pair_fiber(a,b,c,d):
                            weights[w-e]+=price*mult
                    vals=[arb(0)]*(2*n+1)
                    for w,vv in weights.items():
                        for r in range(-2*u,2*u+1,4):
                            vals[n+w+r]+=vv
                    row+=arb_poly(vals)
        out.append([max(arb(0),(row[n+k]-debit[n+k]).lower())*(2 if k else 1)
                    if lower else row[n+k]*(2 if k else 1) for k in range(n+1)])
    return out,abs(alpha).upper(),abs(beta).upper()


def escape(num,den,L=4,A=3,N=24,shift=14,jmax=8,tune=0):
    floor=arb(num)/den
    offset=acb(arb(0,arb(tune)/10**6))
    lower,a,b=make(acb(floor),L,A,D,jmax,True,offset,offset)
    radius=arb(2)
    seed=old["prev"]["warm"]["SEED"]
    r=(seed+2*a+3*b+radius)**2/(4*floor)
    assert r<1
    c=arb(1)
    for ell in range(1,D//2+2):
        c*=(arb(3)/2-ell)/ell
    tail=2*floor.sqrt()*abs(c)*r**(D//2+1)/(1-r)
    kernels=[]
    for j in range(jmax+1):
        trial=[]
        for h in (1,2,4,8,16,24,32,48,64,80):
            rr=arb(h)/32
            ratio=(seed+2*a+3*b+rr)**2/(4*floor)
            assert ratio<1
            trial.append(2*floor.sqrt()*abs(c)*ratio**(D//2+1)/((1-ratio)*rr**j))
        error=min(trial+[tail/radius**j])
        side=[max(arb(0),(v/2-error).lower()) for v in lower[j][1:shift+1]]
        zero=max(arb(0),(lower[j][0]-error).lower())
        kernels.append(arb_poly(side[::-1]+[zero]+side))
    assert kernels[2][shift]>arb(1)/20
    h=[arb(0)]*N
    for height in range(1,5001):
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        power=arb_poly([1])
        out=[arb(0)]*N
        for j,ker in enumerate(kernels):
            if j: power*=base
            row=ker*power
            for k in range(1,N+1):
                out[k-1]+=2*row[shift+j*N+k]
        h=[v.lower() for v in out]
        if sum(i*v for i,v in enumerate(h,1))>21:
            return dict(kind="full_arithmetic_character_map_escape",floor=f"{num}/{den}",
                        height=height,mass_lower=21,quadratic_zero_lower="1/20",
                        maximum_W_degree_enumerated=L,legendre_degree=A,packets=N,
                        shifts=shift,arities=jmax,seed_offset_radius_millionths=tune,precision=ctx.prec)
    raise AssertionError("lower recursion did not establish escape")


def envelope(first,last,div,width,L=4,A=3,E=7,J=6):
    max_w=None
    a=b=arb(0)
    for i in range(first,last):
        t=acb(old["prev"]["warm"]["slab"](i,div),arb(0,arb(1)/width))
        w,al,be=make(t,L,A,E,J)
        if max_w is None:
            max_w=w
        else:
            max_w=[[max(x,y) for x,y in zip(row,prior)] for row,prior in zip(w,max_w)]
        a,b=max(a,al),max(b,be)
    return max_w,a,b


CAPS = [2923298898502,1436923355088,610623934517,379628969765,158387575492,
        71167393853,33573757873,16401251273,8225160121,4210073832,2190535817,
        1155162323,616031080,331654497,180014565,98400918,54122644,29931793,
        16634050,9284397,5202495,2925571,1650482,933881,529841,301356,171796,
        98145,56180,32218,18508,10650,6137,3542,2047,1184,686,398,231,135,
        78,46,27,16,9,5]


def rectangle():
    first,last,div,width=32504,32544,2048,8192
    kernels,a,b=envelope(first,last,div,width)
    low=arb(first)/div
    high=abs(acb(arb(last)/div,arb(1)/width))
    h=[arb(x)/10**13 for x in CAPS]
    eps=arb(2)/10**6
    eta=arb(1)/5
    zero=sum(i*v for i,v in enumerate(h))+eps/eta+arb(1)/10**8
    side=[v/2 for v in h]
    base=arb_poly(side[::-1]+[zero]+side)
    norm=zero+sum(v*(eta*k).cosh() for k,v in enumerate(h,1))
    leak=arb(0)
    n=len(h)
    pooled=[arb(0)]*(D*n+3*D+1)
    power=arb_poly([1])
    for j,ker in enumerate(kernels):
        if j:
            power *= base
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
    total=SEED*eta.cosh()+a*(1+(2*eta).cosh())+b*(1+3*eta.cosh()/2+(3*eta).cosh()/2)+norm+eps
    r=total**2/(4*low)
    assert r<1
    c=arb(1)
    for ell in range(1,D//2+2):
        c*=(arb(3)/2-ell)/ell
    leak+=2*high.sqrt()*abs(c)*r**(D//2+1)/(1-r)
    full_cap=arb(466)/100
    assert leak<arb(17)/10**7<eps
    assert SEED+2*a+3*b+zero+sum(h)+eps<full_cap
    assert full_cap/(4*low-full_cap**2).sqrt()<arb(3)/4
    return dict(kind="arithmetic_rank_three_marked_rectangle",slabs=[first,last],
                division=div,imaginary_half_width="1/8192",packets=n,
                precision=ctx.prec,residual_cap="2/1000000",residual_output_upper="17/10000000",
                full_cap="466/100",maximum_W_degree_enumerated=4,legendre_degree=3,
                maximum_source_Jacobi_exponent=7,maximum_residual_arity_enumerated=6)


def ring_test():
    expected=Counter({0:1})
    seed=Counter({-3:1,-1:3,0:4,1:3,3:1})
    for degree,power in enumerate(rank_powers(8)):
        at_one=Counter()
        at_chi=Counter()
        for (a,b,c,d,e),mult in power.items():
            for w,v in pair_fiber(a,b,c,d):
                at_one[w-e]+=mult*v
            for w,v in pair_fiber(c,d,a,b):
                at_chi[w+e]+=mult*v
        assert at_one==at_chi==expected
        assert sum(at_one.values())==12**degree
        new=Counter()
        for i,u in expected.items():
            for j,v in seed.items():
                new[i+j]+=u*v
        expected=new
    count=rank_powers(3)[3]
    assert count[0,0,0,0,1]==2 and count[0,0,0,0,-1]==2
    return dict(kind="rank_three_Pieri_fiber_controls",max_degree=8,twists=["1","chi"],
                dimension_base=12,third_power_central_multiplicity_each_sign=2)


if __name__=="__main__":
    records=[ring_test(),rectangle(),escape(32502,2048,5,4,28,18,9),
             escape(1015,64,4,4,28,18,9,25),escape(63,4,4,4,28,18,9,500)]
    for record in records:
        print(json.dumps(record,sort_keys=True))
