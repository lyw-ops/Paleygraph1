"""Strengthen the two original translated lower kernels on proved disjoint cubic and quartic sectors."""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from flint import arb, arb_poly, acb


def configure(p):
    global four,D,J,S,da,db,gfrac,t0,coefficients,F,G,kern,novel,pre
    obj=p["prev"]
    four,D,da,db,gfrac,t0,coefficients,F,G,kern=[obj[k] for k in
        ("four","D","da","db","gfrac","t0","coefficients","F","G","kern")]
    novel={}
    for rank,lo,hi,den in ((4,4,8,8),(5,8,16,16)):
        weights=obj["old"]["WEIGHTS"][lo:hi]
        dets=obj["old"]["DETS"][lo:hi]
        zero=tuple((0,)*len(w) for w in weights)
        current={(zero,0):1}
        seen={zero}
        @lru_cache(None)
        def fiber(factors):
            result={0:1}
            for shape,wt in zip(factors,weights):
                if not any(shape):
                    continue
                next_row=Counter()
                for w,m in four["gt"](shape,wt).items():
                    for v,n in result.items():
                        next_row[w+v]+=m*n
                result=next_row
            return result
        for h in range(1,5 if rank==4 else 4):
            nxt=Counter()
            for (fs,e),mult in current.items():
                for i,f in enumerate(fs):
                    for j in range(len(f)):
                        for step in (-1,1):
                            raw=list(f)
                            raw[j]+=step
                            if raw!=sorted(raw,reverse=True):
                                continue
                            l=raw[-1]
                            fs2=fs[:i]+(tuple(x-l for x in raw),)+fs[i+1:]
                            nxt[fs2,e+l*dets[i]]+=mult
            current=nxt
            by=defaultdict(list)
            for (fs,e),mult in current.items():
                by[fs].append((e,mult))
            if h>=3:
                counts=Counter()
                for fs,terms in by.items():
                    if fs in seen or len(terms)!=1:
                        continue
                    (e,mult),=terms
                    for w,m in fiber(fs).items():
                        counts[w-e]+=m*mult
                novel[rank,h]=arb_poly([arb(counts[i])/den**h for i in range(-rank*h,rank*h+1)])
                assert all(x>=0 for x in ((F if rank==4 else G)**h-novel[rank,h]).coeffs())
            seen.update(by)
    a,b,c,d=coefficients()
    alg=obj["old"]
    s=kern["dim"]
    tab=[{2*i-j:comb(j,i)*(s/2)**j for i in range(j+1)} for j in range(D+1)]
    for factor,scale in ((alg["scalar_powers"]([(3,-1),(3,1)],D,False),b/4),
                         ([{0:kern["p3"]["P"][j].get((0,0),0)} for j in range(D+1)],a)):
        tab=alg["add_inputs"](tab,[{e:x*scale**j for e,x in row.items()} for j,row in enumerate(factor)])
    @lru_cache(None)
    def pre(j,e):
        bn,ans=arb(1),arb(0)
        for k in range(1,D//2+1):
            bn*= (arb(3)/2-k)/k
            if 2*k>=j:
                ans+=2*t0.sqrt()*bn*comb(2*k,j)/(4*t0)**k*tab[2*k-j].get(e,0)
        return ans
    # Previous wrappers change J,S temporarily on the function they call.
    J,S=obj["J"],obj["S"]
    obj["lower_kernels"]=lower_kernels
    p["joint"]["old"]["lower"].__globals__["prev"]["lower_kernels"]=lower_kernels

def lower_kernels():
    # Degree-28 lower proof, using exactly these offsets on both translated levels.
    lo,up,a,b,c=four["make"](acb(t0),5,6,D,J+4,-1,da,db,gfrac,True)
    d=abs(coefficients()[3])
    C=abs(c)
    unit4=arb_poly([arb(1)/8]).left_shift(8)
    labels=defaultdict(list)
    for (lab,e),v in four["four_powers"](2).items():
        labels[lab].append((e,v))
    counts=Counter()
    for lab,shifts in labels.items():
        if lab==four["ZERO"] or len(shifts)!=1:
            continue
        (e,v),=shifts
        for w,h in four["four_fiber"](lab).items():
            counts[w-e]+=h*v
    keep4=arb_poly([arb(counts[w])/64 for w in range(-8,9)])
    removed=F*arb_poly([arb(1)/2,0,arb(1)/2])*d
    def translate(lo,up,field,rank,oldrank,scale,keep,unit,amend,last):
        low=[]; high=[]; powers=[field**i for i in range(D+1)]
        for j in range(last+1):
            n=rank*(D-j)
            ll=arb_poly(); uu=arb_poly()
            for h in range(D-j+1):
                r=j+h
                mult=comb(r,j)*scale**h
                charge=up[r]*powers[h]*mult.upper()
                if h<=1:
                    part=lo[r]*powers[h]*mult.lower()
                elif h==2:
                    part=lo[r]*keep*mult.lower()-up[r]*unit*mult.upper()
                elif (rank,h) in novel:
                    new=novel[rank,h]
                    part=lo[r]*new*mult.lower()-up[r]*(powers[h]-new)*mult.upper()
                else:
                    part=-charge
                off=n-oldrank*(D-r)-rank*h
                ll+=part.left_shift(off)
                uu+=charge.left_shift(off)
            if rank==4 and j+2<=D:
                combined=[arb(0)]*(2*n+1)
                for e in range(-min(12,n-3),min(12,n-3)+1):
                    val=(pre(j+2,e-1)+pre(j+2,e+1))*comb(j+2,j)*(C/8)**2
                    for wt,nwt in ((-3,1),(-1,3),(0,4),(1,3),(3,1)):
                        combined[n+wt-e]+=abs(val).lower()*nwt
                ll+=arb_poly(combined)
            if j==0 and amend is not None:
                ll-=amend.left_shift(n-5)
                uu+=amend.left_shift(n-5)
            low.append(kern["cut"](ll,n))
            high.append(uu)
        return low,high
    lo,up=translate(lo,up,F,4,3,C,keep4,unit4,removed,D)
    unit5=arb_poly([arb(1)/16]).left_shift(10)
    lo,_=translate(lo,up,G,5,4,d,G**2-unit5,unit5,None,J)
    M=kern["dim"]+2*abs(a)+3*abs(b)+4*C+arb(23)*d/4
    binom=arb(1)
    for ell in range(1,16): binom*=(arb(3)/2-ell)/ell
    errors=[]
    for k in (1,2,4,8,16,24,32,48,64,80):
        R=arb(k)/32
        ratio=(M+R)**2/(4*t0)
        assert ratio<1
        errors.append([2*t0.sqrt()*abs(binom)*ratio**15/((1-ratio)*R**j) for j in range(J+1)])
    return [arb_poly([max(arb(0),(row[5*(D-j)+k]-min(v[j] for v in errors)).lower())
                      for k in range(-S,S+1)]) for j,row in enumerate(lo)]


