"""Arb192 replay for the retuned four inputs and the transported rank-twelve pair."""
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly, ctx

old = runpy.run_path(str(Path(__file__).with_name("astra-crossnode-59-check.py")))
kern = old["previous"]
four = kern["prior"]
D = kern["D"]
F, G = kern["F"], kern["G"]
t0 = arb(2031)/128
da, db = -arb(9)/10**6, -arb(3)/10**6
gfrac = arb(499)/500
N, S, J = 28, 18, 9


def coefficients():
    a,b,g,_=kern["p3"]["coefficients"](acb(t0),acb(da),acb(db))
    c=gfrac*b*g[1,1][0,0]
    d=-2*c*kern["linear_scalar"](g,b)
    return [v.real for v in (a,b,c,d)]


def projected():
    degree=24
    a,b,c,d=coefficients()
    s=kern["dim"]
    table=[{2*i-k:comb(k,i)*(s/2)**k for i in range(k+1)} for k in range(degree+1)]
    for l,r,scale,perverse in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
        factors=[(len(old["WEIGHTS"][i]),old["DETS"][i]) for i in range(l,r)]
        raw=old["scalar_powers"](factors,degree,perverse)
        table=old["add_inputs"](table,[{e:v*scale**j for e,v in row.items()}
                                       for j,row in enumerate(raw)])
    targets=[("u",2,0,0,0,a/2),("v",4,0,0,0,0),("w",0,2,0,0,0),
             ("z",0,1,1,0,0),("rank_two",1,1,0,0,b/4),
             ("linear",1,0,0,1,0),("square",2,0,0,2,0)]
    M=s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4
    ratio=M**2/(4*t0)
    result={}
    for name,e,u,v,j,amend in targets:
        row=old["add_inputs"](table,[{0:a**k*kern["p3"]["P"][k].get((u,v),0)}
                                     for k in range(degree+1)])
        value=-amend
        binom=arb(1)
        for ell in range(1,degree//2+1):
            binom*=(arb(3)/2-ell)/ell
            value+=2*t0.sqrt()*binom*comb(2*ell,j)/(4*t0)**ell*row[2*ell-j].get(e,0)
        ell=degree//2+1
        binom*=(arb(3)/2-ell)/ell
        rat=ratio*comb(2*ell+2,j)/comb(2*ell,j)
        assert rat<1
        tail=2*t0.sqrt()*abs(binom)*ratio**ell*comb(2*ell,j)/(M**j*(1-rat))
        result[name]=value+arb(0,tail.upper())
        if name=="linear":
            poly=defaultdict(lambda:arb(0))
            binom=arb(1)
            for ell in range(1,degree//2+1):
                binom*=(arb(3)/2-ell)/ell
                mult=2*t0.sqrt()*binom*(2*ell)/(4*t0)**ell
                for exponent,coeff in row[2*ell-1].items():
                    if exponent%2: poly[exponent]+=mult*coeff
            # Bessel's inequality controls all arity-one Jacobi shifts at once.
            norm=sum(v*v for v in poly.values()).sqrt()+arb(0,tail.upper())
            result["jacobi_square_sum"]=norm**2
    return result


def billionths(x):
    return [int((x.lower()*10**9).floor().unique_fmpz()),
            int((x.upper()*10**9).ceil().unique_fmpz())]


def arithmetic(pr):
    single=(-2,-2,0,0,0,0,2,2)
    lifted=[old["activation"](old["outer"]((single,single),sign)) for sign in (-1,1)]
    assert lifted[0]==lifted[1][::-1] and lifted[0]!=lifted[1]
    assert all(len(v)==12 for pair in lifted for v in pair)
    ret=2*(pr["linear"]*pr["z"])**2
    price=ret*pr["square"]
    allprice=pr["z"]**2*pr["jacobi_square_sum"]*pr["square"]
    assert 0<-allprice<pr["u"]
    assert pr["jacobi_square_sum"]>2*pr["linear"]**2
    assert 0<-price<pr["u"]<arb(7)/10**8 and abs(pr["rank_two"])<arb(2)/10**8
    return dict(kind="arithmetic_self_dual_propagated_pair",floor="2031/128",
                offsets=["-9/1000000","-3/1000000"],precision=ctx.prec,
                root_coefficients_billionths={k:billionths(v) for k,v in pr.items()},
                two_twists=[sorted(Counter(row).items()) for row in lifted[1]],
                rank=12,square_unit_multiplicities=[1,0,1],square_unit_phase=1,
                signed_return_times_1e12=billionths(1000*price),
                saving_per_sign_times_1e12=billionths(-2000*price),
                all_odd_saving_per_sign_times_1e15=billionths(-2*10**6*allprice),
                bilinear_form="symmetric",all_odd_quadratic_phase=1)


def retuned_rows(t):
    return kern["make"](t,da*10**5,db*10**5,998)


def lower_kernels():
    # Degree-28 lower proof, using exactly these offsets on both translated levels.
    lo,up,a,b,c=four["make"](acb(t0),4,4,D,J+4,-1,da,db,gfrac,True)
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
                else:
                    part=-charge
                off=n-oldrank*(D-r)-rank*h
                ll+=part.left_shift(off)
                uu+=charge.left_shift(off)
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


def debits(pr,low):
    rows,a,b,c,d=retuned_rows(acb(t0))
    U,V,W,Z=[abs(pr[key]).upper() for key in ("u","v","w","z")]
    C=2*V**2+2*W**2+Z**2
    tag=8*(V+W+Z)
    square=(Z**2*pr["jacobi_square_sum"]).upper()
    assert tag<arb(28)/1000
    # Rank of the h-shift is bounded by 8*(1+abs(h)). Every old seed
    # contributes at most five to an extreme boundary weight.
    M=kern["dim"]+2*a+3*b+4*c+arb(23)*d/4
    ratio0=M**2/(4*t0)
    binom=arb(1)
    for ell in range(1,16): binom*=(arb(3)/2-ell)/ell
    rt=ratio0*arb(16)/15*arb(156)/146
    assert rt<1
    weighted_tail=2*t0.sqrt()*abs(binom)*ratio0**15*30*146/(M*(1-rt))
    odd_tag=8*Z*(weighted_tail+sum((k+1)*x for k,x in enumerate(rows[1])))
    assert odd_tag<arb(14)/1000
    rad=arb(2)
    ratio=(kern["dim"]+2*a+3*b+4*c+arb(23)*d/4+rad)**2/(4*t0)
    assert ratio<1
    binom=arb(1)
    for ell in range(1,16): binom*=(arb(3)/2-ell)/ell
    tail=2*t0.sqrt()*abs(binom)*ratio**15/(1-ratio)
    def rem(j): return tail/rad**j
    def atom(j,k):
        k=abs(k)
        return rows[j][k]/(2 if k else 1) if k<len(rows[j]) else 0
    def full(k): return atom(1,k)+rem(1)
    # Include both leading Jacobi shifts without using any sign protection.
    unary=[4*U*(full(k)+(full(k-2)+full(k+2))/2) for k in range(N+1)]
    loss={2:[],3:[]}
    uniform={2:[],3:[]}
    for stage in (2,3):
        for r in range(J+1):
            c2=comb(r+2,r)*(C if stage==2 else square)
            c4=comb(r+4,r) if stage==2 else 0
            def small(k):
                return (c2*atom(r+2,k)+c4*(3*C**2*atom(r+4,k)
                          +W**4*(atom(r+4,k-4)+atom(r+4,k+4))))
            err=c2*rem(r+2)+c4*(3*C**2+2*W**4)*rem(r+4)
            if stage==2:
                err+=sum(comb(r+h,r)*tag**h*sum(rows[r+h]) for h in range(6,len(rows)-r,2))
                rt=tag/rad*(1+arb(r)/7)
                assert rt<1
                err+=rem(r)*comb(r+6,r)*(tag/rad)**6/(1-rt)
            if r==2: assert low[2][S]-small(0)-err>arb(1)/20
            off=max([arb(0)]+[arb(small(k)).upper() for k in range(S+1,len(rows[r+2])+5)])
            uniform[stage].append((2*(err+off)).upper())
            loss[stage].append(arb_poly([(2*small(k)).upper() for k in range(-S,S+1)]))
    return loss,uniform,unary,U


def escape(pr):
    low=lower_kernels()
    loss,uniform,unary,U=debits(pr,low)
    oldtag=arb_poly([U,0,2*U,0,U]).left_shift(N-2)
    h=[arb(0)]*N
    for height in range(1,6001):
        stage=(height-1)%3+1
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        upperbase=base+oldtag if stage==2 else base
        total=sum(upperbase.coeffs(),arb(0)).upper()
        out=[arb(0)]*N
        power=arb_poly([1]); upperpower=arb_poly([1]); common=arb(0)
        for r,ker in enumerate(low):
            if r:
                power*=base
                if stage>1: upperpower*=upperbase
            step=ker*power
            if stage>1:
                step-=loss[stage][r]*upperpower
                common+=uniform[stage][r]*total**r
            for k in range(1,N+1): out[k-1]+=2*step[S+r*N+k]
        h=[max(arb(0),(v-2*(common+(unary[k] if stage==2 else 0))).lower())
           for k,v in enumerate(out,1)]
        if sum(k*v for k,v in enumerate(h,1))>21:
            return dict(kind="retuned_signed_three_level_escape",floor="2031/128",
                        precision=ctx.prec,height=height,packets=N,shifts=S,arities=J,
                        transported_quadratic_unit="z^2*sum_odd(a_h^2)",mass_lower=21,
                        surviving_quadratic="1/20",discarded_tag_upper="0.028")
    raise ArithmeticError("no certified escape")


CAPS=[
 24249014555425,11075868485129,5501866217515,3091355312594,1462075177303,709873987043,
 334728942211,163441610524,81926015941,41913951485,21797684953,11489308848,6124127083,
 3295474748,1787846156,976814174,537009568,296842383,164885050,91987119,51519898,
 28957686,16328794,9234735,5236831,2977097,1696348,968636,554197,317664,182397,
 104897,60418,34849,20127,11639,6739,3906,2267,1317,766,446,260,152,89,52,30,18,10,6]


def rectangle():
    first,last,sub=1040022,1040028,3
    rows=None
    parts=[arb(0)]*4
    for j in range(first*sub,last*sub):
        t=acb(arb(2*j+1,1)/(2*sub*65536),arb(0,1)/2**20)
        rr,*pp=retuned_rows(t)
        rows=rr if rows is None else [[max(x,y) for x,y in zip(a,b)] for a,b in zip(rows,rr)]
        parts=[max(x,y) for x,y in zip(parts,pp)]
    leak,full=kern["validate"](first,last,2**20,rows,*parts,CAPS)
    cap=arb(4652)/1000
    assert leak<arb(396)/10**9<arb(6)/10**7 and full<cap
    assert cap/(4*arb(first)/65536-cap**2).sqrt()<arb(3)/4
    return dict(kind="retuned_actual_common_rectangle",precision=ctx.prec,
                real_endpoints=[first,last],denominator=65536,imaginary_half_width="1/1048576",
                slabs=sub*(last-first),core_excess_upper="396e-9",coordinate_upper="4.652",
                residual_budget="6e-7",mark_bound="3/sqrt(n)")


def gauss_test():
    finite=runpy.run_path(str(Path(__file__).with_name("astra-prime-phase-32-check.py")))
    bases=[]
    for p,d in ((5,1),(3,2),(13,1),(17,1),(5,2)):
        u=p**d
        _,ell,_,_=finite["data"](p,2*d)
        test=[0]*len(ell)
        for j in range(u+1):
            test[j*(u-1)]=(-1)**j
        for sign in (-1,1):
            jacobi=[-x*(-1 if i%2 and sign<0 else 1) for i,x in enumerate(ell)]
            assert finite["cycconv"](jacobi,test)==[u*x for x in test]
        bases.append(u)
    return dict(kind="twisted_norm_one_Jacobi_convolution_identity",bases=bases,
                norm_one_character="quadratic",perverse_Jacobi_eigenvalues=[1,1])


if __name__=="__main__":
    pr=projected()
    for record in (gauss_test,lambda: arithmetic(pr),lambda: escape(pr),rectangle):
        print(json.dumps(record(),sort_keys=True),flush=True)
