"""Arb192 proof of the signed fourth-seed rectangle and full character-map obstruction."""
from pathlib import Path
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
import runpy
import json
from flint import acb, arb, arb_poly, ctx

prior=runpy.run_path(str(Path(__file__).with_name('astra-rankfour-57-check.py')))
p3=prior['p3']
D,F,dim=prior['D'],prior['F'],prior['SEED']
G=arb_poly([arb(1)/16,0,arb(5)/16,arb(1)/4,arb(9)/8,arb(9)/4,
            arb(9)/8,arb(1)/4,arb(5)/16,0,arb(1)/16])

def linear_scalar(groups,beta):
    scalar=acb(0)
    for l,parts in enumerate(p3['rank_powers'](4)):
        for k in range(8):
            value=groups[1+l,k].get((0,0),0)
            for (*labels,m),mult in parts.items():
                if any(labels): continue
                hit=sum(e==1 for e in ((m-k,m+k) if k else (m,)))
                scalar+=hit*value*(1+l)*(beta/4)**l*mult/(2 if k else 1)
    return scalar

def make(t,da=-7,db=-6,gfrac=998):
    da,db=arb(da)/100000,arb(db)/100000
    frac=arb(gfrac)/1000
    old,a,b,c=prior['make'](t,4,3,7,6,3,da,db,frac)
    alpha,beta,groups,amend=p3['coefficients'](t,acb(da),acb(db))
    gamma=frac*beta*groups[1,1][0,0]
    scalar=linear_scalar(groups,beta)
    delta=-2*gamma*scalar
    for k in range(6):
        # remove the entire h=1, r=1, e=+/-1 charge since both are
        # represented by the new distinguished input delta F5.
        weight=F[4+k-1]+F[4+k+1]
        old[0][k]-=(abs(gamma*scalar)*weight*(2 if k else 1)).lower()
    kernels=[]
    power=[G**i for i in range(D+1)]
    for j in range(D+1):
        n=5*(D-j)
        row=arb_poly()
        for h in range(D+1-j):
            ko=old[j+h]
            side=[v/2 for v in ko[1:]]
            ort=arb_poly(side[::-1]+[ko[0]]+side)
            row+=(ort*power[h]).left_shift(n-len(side)-5*h)*comb(h+j,j)*abs(delta).upper()**h
        kernels.append([(row[n+k]*(2 if k else 1)).upper() for k in range(n+1)])
    return kernels,a,b,c,abs(delta).upper()

def envelope(first,last,step=1,width=2**20):
    pooled=None; caps=[arb(0)]*4
    for i in range(first,last,step):
        mid=(arb(i)+arb(step)/2)/65536
        t=acb(arb(mid,arb(step)/(2*65536)),arb(0,arb(1)/width))
        rows,*parts=make(t)
        pooled=rows if pooled is None else [[max(a,b) for a,b in zip(x,y)] for x,y in zip(pooled,rows)]
        caps=[max(a,b.upper()) for a,b in zip(caps,parts)]
    return pooled,*caps

def validate(first,last,width,rows,a,b,c,d,caps):
    eta=arb(1)/5; eps=arb(6)/10**7; h=[arb(v)/10**14 for v in caps]
    zero=sum(i*v for i,v in enumerate(h))+eps/eta+arb(1)/10**8
    core=arb_poly([v/2 for v in reversed(h)]+[zero]+[v/2 for v in h])
    norm=zero+sum(v*(eta*k).cosh() for k,v in enumerate(h,1)); n=len(h)
    leak=arb(0); pooled=[arb(0)]*(D*n+5*D+1); power=arb_poly([1])
    for j,ker in enumerate(rows):
        if j: power*=core
        side=[v/2 for v in ker[1:]]; row=power*arb_poly(side[::-1]+[ker[0]]+side)
        center=j*n+len(side)
        for i in range(1,len(row)-center): pooled[i]+=2*row[center+i]
        if j: leak+=sum(v*(eta*k).cosh() for k,v in enumerate(ker))*j*(norm+eps)**(j-1)*eps
    for k,v in enumerate(pooled[1:],1): leak+=max(arb(0),(v-(h[k-1] if k<=n else arb(0))).upper())*(eta*k).cosh()
    def cn(poly,k):return sum(poly[k+i]*(2 if i else 1)*(eta*i).cosh() for i in range(k+1))
    total=prior['SEED']*eta.cosh()+a*(1+(2*eta).cosh())+b*(1+3*eta.cosh()/2+(3*eta).cosh()/2)+c*cn(F,4)+d*cn(G,5)+norm+eps
    low=arb(first)/65536; high=abs(acb(arb(last)/65536,arb(1)/width)); ratio=total**2/(4*low)
    assert ratio<1
    binom=arb(1)
    for ell in range(1,D//2+2): binom*=(arb(3)/2-ell)/ell
    leak+=2*high.sqrt()*abs(binom)*ratio**(D//2+1)/(1-ratio)
    full=prior['SEED']+2*a+3*b+4*c+arb(23)/4*d+zero+sum(h)+eps
    return leak,full

def cut(poly, n):
    return arb_poly([max(arb(0),poly[i].lower()) for i in range(2*n+1)])
def new_kernels(t,jmax=9,shift=18,dfrac=1):
    alpha,beta,g,amend=p3['coefficients'](acb(t),acb(-arb(7)/100000),acb(-arb(6)/100000))
    scalar=linear_scalar(g,beta)
    low,upper,a,b,c=prior['make'](acb(t),4,4,D,jmax+4,-1,-arb(7)/100000,-arb(6)/100000,arb(499)/500,True)
    d=abs(2*c*scalar*dfrac)
    C=abs(c)
    FP=[F**h for h in range(D+1)]
    a2=arb_poly([arb(1)/8]).left_shift(8)
    labels=defaultdict(list)
    for (lab,e),v in prior['four_powers'](2).items(): labels[lab].append((e,v))
    q2=Counter()
    for lab,ev in labels.items():
        if lab==prior['ZERO'] or len(ev)>1: continue
        (e,v),=ev
        for w,h in prior['four_fiber'](lab).items(): q2[w-e]+=h*v
    q2=arb_poly([arb(q2[i])/64 for i in range(-8,9)])
    # Every linear rank-four standard has its own derived label up to its
    # paired arithmetic determinant normalization. In arity zero, remove
    # |delta| times C1 F from this sector after signed subtraction.
    oldlow=[]; oldup=[]
    removed=F*arb_poly([arb(1)/2,0,arb(1)/2])*d
    for j in range(D+1):
        n=4*(D-j); lo=arb_poly(); hi=arb_poly()
        for h in range(D-j+1):
            r=j+h
            price=comb(r,j)*C**h
            full=upper[r]*FP[h]*price.upper()
            off=n-3*(D-r)-4*h
            hi+=full.left_shift(off)
            if h<=1: piece=low[r]*FP[h]*price.lower()
            elif h==2: piece=(low[r]*q2*price.lower()-upper[r]*a2*price.upper())
            else: piece=-full
            lo+=piece.left_shift(off)
        if not j:
            lo-=removed.left_shift(n-5)
            hi+=removed.left_shift(n-5)
        oldlow.append(cut(lo,n));oldup.append(hi)
    # All eight SL factors have rank >=5. At degree two every nontrivial
    # label has a unique determinant shift; sixteen scalar copies normalize
    # to 1/16. At degree >=3 debit the entire positive measure.
    gp=[G**i for i in range(D+1)]
    unit=arb_poly([arb(1)/16]).left_shift(10)
    q2=gp[2]-unit
    kernels=[]
    for j in range(jmax+1):
        n=5*(D-j); row=arb_poly()
        for h in range(D-j+1):
            r=j+h
            price=comb(r,j)*d**h
            if h<2: piece=oldlow[r]*gp[h]*price.lower()
            elif h==2: piece=oldlow[r]*q2*price.lower()-oldup[r]*unit*price.upper()
            else: piece=-oldup[r]*gp[h]*price.upper()
            row+=piece.left_shift(n-4*(D-r)-5*h)
        binom=arb(1)
        for ell in range(1,D//2+2): binom*=(arb(3)/2-ell)/ell
        errors=[]
        for v in (1,2,4,8,16,24,32,48,64,80):
            radius=arb(v)/32
            ratio=(dim+2*abs(a)+3*abs(b)+4*C+arb(23)/4*d+radius)**2/(4*t)
            assert ratio<1
            errors.append(2*t.sqrt()*abs(binom)*ratio**(D//2+1)/((1-ratio)*radius**j))
        error=min(errors)
        side=[max(arb(0),(row[n+k]-error).lower()) for k in range(1,shift+1)]
        zero=max(arb(0),(row[n]-error).lower())
        kernels.append(arb_poly(side[::-1]+[zero]+side))
    return kernels
def escape(t,nt=28,shift=18,dfrac=1):
    kernels=new_kernels(t,shift=shift,dfrac=dfrac)
    assert kernels[2][shift]>arb(1)/20
    h=[arb(0)]*nt
    for height in range(1,3001):
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        power=arb_poly([1]);out=[arb(0)]*nt
        for j,ker in enumerate(kernels):
            if j: power*=base
            row=ker*power
            for k in range(1,nt+1): out[k-1]+=2*row[shift+j*nt+k]
        h=[v.lower() for v in out]
        if sum(i*v for i,v in enumerate(h,1))>21: return height
    return None

@lru_cache(None)
def standard_powers(rank,degree):
    if not degree:
        return {(0,)*rank:1}
    out=Counter()
    for part,v in standard_powers(rank,degree-1).items():
        for i in range(rank):
            if i and part[i]==part[i-1]:
                continue
            row=list(part)
            row[i]+=1
            out[tuple(row)]+=v
    return out

def single_scalars(rank,exponent,degree):
    terms=Counter()
    for s in range(degree+1):
        t=degree-s
        for a,x in standard_powers(rank,s).items():
            for b,y in standard_powers(rank,t).items():
                v=a[-1]-b[-1]
                if all(i-j==v for i,j in zip(a,b)):
                    e=v*exponent
                    terms[e]+=comb(degree,s)*x*y*(-1 if e%2 else 1)
    return terms

def controls():
    families=[(6,0),(6,0),(5,1),(5,-1),(5,-1),(5,1),(7,-3),(7,3)]
    moments=[Counter({0:1})]+[Counter() for _ in range(6)]
    for rank,exponent in families:
        new=[Counter() for _ in range(7)]
        for j in range(7):
            for h in range(j+1):
                for e,x in single_scalars(rank,exponent,h).items():
                    for k,y in moments[j-h].items():
                        new[j][e+k]+=comb(j,h)*x*y
        moments=new
    assert moments==[{0:1},{},{0:16},{},{0:768},{-1:-4,1:-4},{0:61444}]
    weights=((-3,-3,1,1,1,3),(0,)*6,(-1,-1,0,0,1),(-1,-1,-1,2,2),
             (-1,-1,-1,-1,5),(-1,0,0,0,0),(0,0,0,0,0,0,3),(-3,-2,-2,1,1,1,1))
    zero=tuple((0,)*r for r,e in families)
    powers=[Counter({(zero,0):1})]
    for degree in (1,2):
        out=Counter()
        for (factors,e),mult in powers[-1].items():
            for i,part in enumerate(factors):
                for sign in (-1,1):
                    for j in range(len(part)):
                        row=list(part)
                        row[j]+=sign
                        if row!=sorted(row,reverse=True):
                            continue
                        shift=row[-1]
                        shape=tuple(k-shift for k in row)
                        out[(factors[:i]+(shape,)+factors[i+1:],e+shift*families[i][1])]+=mult
        assert len({lab for lab,e in out})==len(out)
        for twist in (0,1):
            combined=Counter()
            for (factors,e),mult in out.items():
                fiber=Counter({e*(1 if twist else -1):mult})
                for i,part in enumerate(factors):
                    if not any(part):
                        continue
                    expanded=Counter()
                    for u,v in prior['gt'](part,weights[i^twist]).items():
                        for k,h in fiber.items():
                            expanded[u+k]+=v*h
                    fiber=expanded
                combined.update(fiber)
            target=(16*G)**degree
            assert all(target[5*degree+k]==v for k,v in combined.items())
            assert sum(combined.values())==92**degree
        powers.append(out)
    assert not ({lab for lab,e in powers[1]} & {lab for lab,e in powers[2]})
    assert powers[2][zero,0]==16
    for k in range(1,6):
        assert G[5+k]==(F[4+k-1]+F[4+k+1])/2
    assert G[5]==sum((k-1)*2*G[5+k] for k in range(1,6))
    sources=[((-4,),(4,)),((-4,0,4),(0,0,0)),((-2,-2,2,2),(-2,-2,2,2))]
    signatures=[]
    for weights in sources:
        rank=sum(abs(v) for row in weights for v in row)//2
        diam=[]
        for i in (0,1):
            row=[v for v in weights[i] if v<0]+[v for v in weights[1-i] if v>0]
            row+=[0]*(rank-len(row))
            diam.append(max(row)-min(row))
        signatures.append([rank,sorted(diam)])
    assert signatures==[[4,[0,8]],[4,[4,4]],[8,[4,4]]]
    return dict(kind="signed_determinant_scalar_and_two_node_controls",
                moments=[dict(m) for m in moments],coordinates="positive Jacobi and perverse F5",
                two_node_dimension_diameters=signatures,new_label_counts=[len(p) for p in powers])

CAPS=[24148848481238, 11036242364221, 5481617025439, 3078938246431, 1455069682665,
      705929189778, 332515575261, 162188150279, 81211064249, 41503828216, 21561330009,
      11352571725, 6044763980, 3249283752, 1760897327, 961058584, 527781019, 291428034,
      161703803, 90115476, 50417426, 28307579, 15945059, 9008023, 5102777, 2897770,
      1649372, 940800, 537692, 307872, 176584, 101445, 58367, 33629, 19402, 11208, 6482,
      3753, 2176, 1263, 733, 427, 248, 145, 85, 49, 29, 17, 10, 5]
def rectangle():
    first,last,width=1040034,1040054,2**20
    rows,*data=envelope(first,last,2,width)
    leak,full=validate(first,last,width,rows,*data,CAPS)
    full_cap=arb(4648)/1000
    assert leak<arb(395)/10**9<arb(6)/10**7 and full<full_cap
    assert full_cap/(4*arb(first)/65536-full_cap**2).sqrt()<arb(3)/4
    return dict(kind="fourth_distinguished_actual_rectangle",division=65536,endpoints=[first,last],
                slabs=10,imaginary_half_width="1/1048576",precision=ctx.prec,
                residual_cap="6/10000000",residual_output_upper="395/1000000000",full_cap="4648/1000")
def lower_record(num,den,tolerance):
    height=escape(arb(num)/den,dfrac=arb(1,arb(1)/tolerance))
    assert height is not None
    return dict(kind="full_fourth_seed_root_escape",floor=f"{num}/{den}",phase="arbitrary",
                relative_modulus_radius=f"1/{tolerance}",height=height,arities=9,shifts=18,
                packets=28,precision=ctx.prec,mass_lower=21,quadratic_zero_lower="1/20")
if __name__=='__main__':
    for record in (controls,rectangle,lambda:lower_record(2031,128,10000),
                   lambda:lower_record(1015,64,1000)):
        print(json.dumps(record(),sort_keys=True),flush=True)
