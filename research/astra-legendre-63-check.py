"""Signed Sp8 recentering with full old multiplication; outward-rounded replay."""
from pathlib import Path
from math import comb
import json
import runpy
from flint import arb, acb, arb_poly, ctx

prev = runpy.run_path(str(Path(__file__).with_name('astra-primitive-62-check.py')))
kern = prev['kern']
D, N, J, S = 28, 28, 9, 18
R = arb_poly([2, 0, 4, 0, 2])
AB = arb_poly([2, 0, 0, 0, 2])
unit2 = arb_poly([1]).left_shift(4)
unit3 = 3*R.left_shift(4)


def lower(pr):
    t=prev['t0']
    params=prev['lower_kernels'].__globals__
    params['J'],params['S']=J+3,S+6
    try:
        low=prev['lower_kernels']()
    finally:
        params['J'],params['S']=J,S
    upper,a,b,c,d=prev['retuned_rows'](acb(t))
    M=kern['dim']+2*a+3*b+4*c+arb(23)*d/4
    z=pr['z'].union(prefix(acb(t))[0].real)
    # Count the entire omitted degree tail in the translated coordinates.
    # For the separately debited old high kernels bound their analytic tail at radius 2.
    rad=arb(2)
    ratio=(M+rad)**2/(4*t)
    binom=arb(1)
    for ell in range(1,16):binom*=(arb(3)/2-ell)/ell
    tail=2*t.sqrt()*abs(binom)*ratio**15/(1-ratio)
    def up(r):
        row=upper[r]; side=[v/2 for v in row[1:]]
        return arb_poly(side[::-1]+[row[0]]+side),len(side)
    kernels=[]
    for j in range(J+1):
        row=[arb(0) for k in range(-S,S+1)]
        err=arb(0)
        for h in range(4):
            rank=j+h; mult=comb(rank,j)*z**h
            dim=2*h
            field=R**h
            returning=(unit2 if h==2 else unit3 if h==3 else arb_poly())
            pos=(low[rank]*(field-returning))*mult.lower()
            U,center=up(rank)
            debit=U*returning*mult.upper()
            err+=sum(returning.coeffs(),arb(0))*mult.upper()*tail/rad**rank
            for k in range(-S,S+1):
                row[k+S]+=pos[S+6+dim+k]-debit[center+dim+k]
        if j==0:
            for k in range(-2,3):row[S+k]-=AB[2+k]*z.upper()
        mass=8*z.upper()
        for h in range(4,D-j+1):
            err+=comb(j+h,j)*mass**h*sum(upper[j+h],arb(0))
        rt=mass/rad*(1+arb(j)/5)
        assert rt<1
        err+=tail/rad**j*comb(j+4,j)*(mass/rad)**4/(1-rt)
        kernels.append(arb_poly([max(arb(0),(v-err).lower()) for v in row]))
    return kernels


def escape(pr, cross_record):
    rows=lower(pr)
    t=prev['t0']; upper_rows,pars=upper(acb(t))
    a,b,c,d,z=pars
    mass=kern['dim']+2*a+3*b+4*c+arb(23)*d/4+8*z
    radius=2; ratio=(mass+radius)**2/(4*t);assert ratio<1
    binomial=arb(1)
    for ell in range(1,16):binomial*=(arb(3)/2-ell)/ell
    tail=2*t.sqrt()*abs(binomial)*ratio**15/(1-ratio)
    cross=arb(cross_record['dual_pair_return_times_1e15'][1])/10**15
    ra=arb(cross_record['new_RA_times_1e12'][1])/10**12
    assert 48*ra<arb(2)/1000
    debit=[]; uniform=[]
    for r in range(J+1):
        j=r+2; scale=cross*comb(j,r); U=upper_rows[j]
        def atom(k):return U[abs(k)]/(2 if k else 1) if abs(k)<len(U) else arb(0)
        off=max([arb(0)]+[atom(k) for k in range(S+1,len(U))])
        debit.append(arb_poly([(2*scale*atom(k)).upper() for k in range(-S,S+1)]))
        uniform.append((2*scale*(off+tail/radius**j)).upper())
        if r==2:assert rows[2][S]-scale*(atom(0)+tail/radius**j)>arb(1)/20
    def height(pair):
        h=[arb(0)]*N
        for iteration in range(1,5001):
            grouped=pair and iteration%2==0
            side=[v/2 for v in h]
            b=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
            total=sum(b.coeffs(),arb(0)).upper()
            out=[arb(0)]*N; power=arb_poly([1]);extra=arb(0)
            for j,row in enumerate(rows):
                if j:power*=b
                step=power*row
                if grouped:
                    step-=power*debit[j]
                    extra+=uniform[j]*total**j
                for k in range(1,N+1):out[k-1]+=2*step[S+j*N+k]
            h=[max(arb(0),(v-2*extra).lower()) for v in out]
            if sum(k*v for k,v in enumerate(h,1))>21:return iteration
        raise ArithmeticError('did not cross 21')
    return dict(kind='fully_collected_Sp8_center_and_dual_pair_escape',floor='2031/128',degree=D,
                arities=J,shifts=S,packets=N,unary_center_only_height=height(False),
                center_and_dual_pair_height=height(True),mass_lower=21,
                transported_tag_dimension_upper='0.002',surviving_quadratic='1/20',precision=ctx.prec)


def prefix(t):
    # These entire individual coefficients are already charged as separate labels
    # at rank-three degree <=4, no rank-four, rank-five, or Sp8 child.
    a,b,g,amend=kern['p3']['coefficients'](t,acb(prev['da']),acb(prev['db']))
    def coef(j,u,v):
        out=acb(0)
        for h,parts in enumerate(kern['p3']['rank_powers'](4)):
            for (a1,b1,a2,b2,e),mult in parts.items():
                if a1 or b1 or a2 or b2:continue
                k=abs(e)
                d=amend[k] if j+h==0 and k in amend else g[j+h,k]
                out+=d.get((u,v),0)*comb(j+h,j)*(b/4)**h*mult/(2 if k else 1)
        return out
    return coef(0,1,1),coef(1,1,0),coef(3,1,0)


def upper(t):
    old,*abcd=prev['retuned_rows'](t)
    c0,c1,c3=prefix(t)
    z=c0
    # Exact old amendment on the charged partial AB sector. All complementary
    # old contributions and their original positive charges stay present.
    old[0][2]-=4*abs(c0).lower()
    first=z*c1; third=3*z**3*c3
    saved=(2*(abs(first)*abs(third)-(first*third.conjugate()).real) /
           (abs(first)+abs(third)+abs(first+third))).lower()
    assert saved>0
    fields=[R**h for h in range(D+1)]
    pol=[]
    for arr in old:
        side=[v/2 for v in arr[1:]]
        pol.append(arb_poly(side[::-1]+[arr[0]]+side))
    rows=[]
    for j in range(D+1):
        n=5*(D-j); row=arb_poly()
        for h in range(D-j+1):
            row+=(pol[j+h]*fields[h]).left_shift(3*h)*comb(j+h,j)*abs(z).upper()**h
        if j==0:
            # Standard R times independently charged old A+B.
            cost=R*arb_poly([1,0,2,0,1]); row-=cost.left_shift(n-4)*saved
        rows.append([(row[n+k]*(2 if k else 1)).upper() for k in range(n+1)])
    return rows,abcd+[abs(z).upper()]


def envelope(first,last,sub=1,width=2**20):
    rows=None; abcd=[arb(0)]*5
    for j in range(first*sub,last*sub):
        t=acb(arb(2*j+1,1)/(2*sub*65536),arb(0,1)/width)
        r,pars=upper(t)
        rows=r if rows is None else [[max(x,y) for x,y in zip(a,b)] for a,b in zip(rows,r)]
        abcd=[max(x,y) for x,y in zip(pars,abcd)]
    return rows,abcd


def validate(first,last,width,rows,abcd,caps):
    # The inherited tail and coordinate routine takes the old scalar seed
    # masses. Four copies of the Y allocation have exactly the Sp8 weight measure.
    a,b,c,d,z=abcd
    # The generic scalar a Y has boundary measure 1 + cosh(2 eta).
    # Four times that norm equals the Sp8 norm 4 + 4 cosh(2 eta).
    assert R[2]==4 and R[4]==R[0]==2
    return kern['validate'](first,last,width,rows,a+4*z,b,c,d,caps)

def moments(limit):
    from collections import Counter
    rows=[{(0,0,0,0):1}]
    for step in range(limit):
        new=Counter()
        for shape,m in rows[-1].items():
            for i in range(4):
                for sign in (-1,1):
                    child=list(shape);child[i]+=sign
                    if child[-1]>=0 and child==sorted(child,reverse=True):new[tuple(child)]+=m
        rows.append(new)
    return [row.get((0,0,0,0),0) for row in rows]


def arithmetic():
    t=prev['t0']; degree=24
    old=prev['old']; a,b,c,d=prev['coefficients'](); s=kern['dim']
    z=prefix(acb(t))[0].real
    table=[{2*i-k:comb(k,i)*(s/2)**k for i in range(k+1)} for k in range(degree+1)]
    for l,r,scale,perverse in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
        factors=[(len(old['WEIGHTS'][i]),old['DETS'][i]) for i in range(l,r)]
        raw=old['scalar_powers'](factors,degree,perverse)
        table=old['add_inputs'](table,[{e:v*scale**j for e,v in row.items()} for j,row in enumerate(raw)])
    mu=moments(degree+1);assert mu[:7]==[1,0,1,0,3,0,15]
    def select(e,u,v,j,rep,center):
        tab=old['add_inputs'](table,[{0:a**k*kern['p3']['P'][k].get((u,v),0)} for k in range(degree+1)])
        mag=s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*abs(center)
        ratio=mag**2/(4*t); out=arb(0);bn=arb(1)
        for ell in range(1,degree//2+1):
            bn*=(arb(3)/2-ell)/ell
            n=2*ell-j
            if n<0:continue
            total=sum(comb(n,h)*center**h*mu[h+rep]*tab[n-h].get(e,0) for h in range(n+1))
            out+=2*t.sqrt()*bn*comb(2*ell,j)*total/(4*t)**ell
        ell=degree//2+1;bn*=(arb(3)/2-ell)/ell
        rt=ratio*comb(2*ell+2,j)/comb(2*ell,j); assert rt<1
        tail=2*t.sqrt()*abs(bn)*ratio**ell*comb(2*ell,j)/(mag**j*(1-rt))
        return out+arb(0,tail.upper())
    lin=select(0,1,0,1,0,arb(0));cub=select(0,1,0,3,0,arb(0))
    # For the small RA coefficient project the complete translated series.
    ra=select(0,1,0,0,1,z)
    u=select(2,0,0,0,0,z)-a/2
    h2=select(2,0,0,2,0,z)
    cross=2*ra**2; saving=-2*cross*h2
    assert z>0 and lin>0 and cub<0 and ra>0 and h2<0 and 0<saving/2<u
    weights=(-2,-2,0,0,0,0,2,2)
    before=(tuple(sorted(w+v for w in weights for v in (-2,2))),tuple(sorted(weights*2)))
    after=old['activation'](before);assert all(len(row)==24 for row in after) and after[0]!=after[1]
    def bounds(val,factor):
        return [int((val*factor).lower().floor().unique_fmpz()),int((val*factor).upper().ceil().unique_fmpz())]
    return dict(kind='non_Jacobi_Sp8_Legendre_dual_return',floor='2031/128',precision=ctx.prec,
        prefixed_AB_times_1e12=bounds(z,10**12),old_A_unary_times_1e12=bounds(lin,10**12),
        old_A_cubic_times_1e12=bounds(cub,10**12),new_RA_times_1e12=bounds(ra,10**12),
        new_m2_times_1e12=bounds(u,10**12),new_binary_m2_times_1e9=bounds(h2,10**9),
        dual_pair_return_times_1e15=bounds(cross,10**15),saving_per_Jacobi_sign_times_1e15=bounds(saving,10**15),
        rank=24,unit_multiplicities_AA_AB_BB=[0,1,0],cross_unit_phase=1,
        preactivation_sum_absolute_weights=[sum(map(abs,row)) for row in before])


def exact_feedback():
    sample=runpy.run_path(str(Path(__file__).with_name('astra-prime-phase-32-check.py')))
    conv=sample['cycconv']; qs=[]
    for p,k in ((5,1),(3,2),(13,1),(17,1),(5,2),(7,2),(97,1)):
        _,ell,*_=sample['data'](p,k);q=p**k
        n=[l*v for l,v in zip(ell,conv(ell,ell))];a=n[::2];b=n[1::2]
        ee=conv(a,a);oo=conv(b,b)
        old=conv(n,[v*(-1)**i for i,v in enumerate(n)])
        assert not any(old[1::2])
        grouped=[ee[j]-oo[j-1] for j in range(len(ee))]
        assert grouped==old[::2]
        rho=[ell[2*j]*g for j,g in enumerate(grouped)]
        assert rho==[l*v for l,v in zip(ell[::2],old[::2])] and any(rho)
        qs.append(q)
    return dict(kind='all_lift_AB_positive_Sp8_feedback',exact_cyclic_rings=qs,
                denominator='q^2',exceptional_column_coefficient=0,sign=1)

CAPS=[24297000000001,10415562221176,5512038497022,3096740233595,1465007912826,711500249757,
      335642085172,163959125581,82221421009,42083535617,21895490964,11545935057,6157018303,
      3314632695,1799031821,983358830,540845896,299094852,166209514,92766941,51979593,29228965,
      16489042,9329482,5292897,3010299,1716024,980304,561121,321775,184839,106349,61281,35362,
      20433,11821,6847,3971,2305,1340,779,454,265,155,90,53,31,18,11,6]


def rectangle():
    first,last,sub,width=1040021,1040023,8,2**20
    rows,pars=envelope(first,last,sub,width)
    leak,full=validate(first,last,width,rows,pars,CAPS)
    cap=arb(4654)/1000
    assert leak<arb(414)/10**9<arb(6)/10**7 and full<cap
    assert cap/(4*arb(first)/65536-cap**2).sqrt()<arb(3)/4
    return dict(kind='actual_fifth_center_Sp8_marked_rectangle',real_endpoints=[first,last],
                denominator=65536,imaginary_half_width='1/1048576',slabs=(last-first)*sub,
                precision=ctx.prec,core_excess_upper='414e-9',residual_budget='6e-7',
                coordinate_upper='4.654',mark_bound='3/sqrt(n)')


if __name__=='__main__':
    rec=arithmetic()
    for result in (exact_feedback(),rec,escape(prev['projected'](),rec),rectangle()):
        print(json.dumps(result,sort_keys=True),flush=True)
