"""Arb replay of the two dual symmetric-square centers alongside the mixed Sp8 center."""
from pathlib import Path
from math import comb
import json
import runpy
from flint import acb, arb, arb_poly, ctx

old=runpy.run_path(str(Path(__file__).with_name('astra-legendre-63-check.py')))
prev,kern=old['prev'],old['kern']
D=28
field=arb_poly([1,0,0,0,6,0,0,0,1])
source=arb_poly([1,0,0,0,4,0,0,0,1])
powers=[field**i for i in range(D+1)]

def coefficient(t,j,u,v):
    a,b,g,amend=kern['p3']['coefficients'](t,acb(prev['da']),acb(prev['db']))
    out=acb(0)
    for h,parts in enumerate(kern['p3']['rank_powers'](4)):
        for (a1,b1,a2,b2,e),mult in parts.items():
            if a1 or b1 or a2 or b2:continue
            k=abs(e)
            d=amend[k] if j+h==0 and k in amend else g[j+h,k]
            out+=d.get((u,v),0)*comb(j+h,j)*(b/4)**h*mult/(2 if k else 1)
    return out

def upper(t):
    oldrows,pars=mixed_rows(t)
    w=coefficient(t,0,2,0)
    assert w.real>0 and w.overlaps(coefficient(t,0,0,2))
    # Both selected character charges in the h_R=0 term.
    for k in (0,4):
        oldrows[0][k]-=source[4+k]*(2 if k else 1)*abs(w).lower()
    pol=[]
    for arr in oldrows:
        side=[v/2 for v in arr[1:]]
        pol.append(arb_poly(side[::-1]+[arr[0]]+side))
    # Standard and dual each return six times at cubic order with zero
    # determinant shift. The mixed R^2 Q term returns three times.
    c1=coefficient(t,1,1,0)
    c3=coefficient(t,3,1,0)
    z=old['prefix'](t)[0]
    x=w*c1
    y=(6*w**3+3*z**2*w)*c3
    saved=(2*(abs(x)*abs(y)-(x*y.conjugate()).real)/(abs(x)+abs(y)+abs(x+y))).lower()
    assert saved>0
    rows=[]
    for j in range(D+1):
        n=5*(D-j); row=arb_poly()
        for h in range(D-j+1):
            row+=(pol[j+h]*powers[h]).left_shift(h)*comb(j+h,j)*abs(w).upper()**h
        if j==0:
            cost=field*arb_poly([1,0,2,0,1])
            row-=cost.left_shift(n-6)*saved
        rows.append([(row[n+k]*(2 if k else 1)).upper() for k in range(n+1)])
    return rows,pars+[abs(w).upper()]

def feedback():
    sample=runpy.run_path(str(Path(__file__).with_name('astra-prime-phase-32-check.py')))
    conv=sample['cycconv']; fields=[]
    for p,k in ((5,1),(3,2),(13,1),(17,1),(5,2),(7,2),(97,1)):
        _,ell,*_=sample['data'](p,k);q=p**k;n=(q-1)//2
        leg=[l*v for l,v in zip(ell,conv(ell,ell))]
        other=[(-1)**i*v for i,v in enumerate(leg)]
        aa=conv(leg,leg);bb=conv(other,other)
        assert sum(leg)**2==4
        # Inverse transforms on the full group: both raw squares are even
        # after summing their two lifts; each Chebyshev constant is a unit.
        incoming=[x+y-2*q*q*(i==0) for i,(x,y) in enumerate(zip(aa,bb))]
        assert not any(incoming[1::2])
        compact=[l*(v+2*(q+1)) for l,v in zip(ell,aa)]
        pair=[v*(1+(-1)**i) for i,v in enumerate(compact)]
        diff=[v-l*u for v,l,u in zip(pair,ell,incoming)]
        assert diff[::2]==[4*(q+1)*l for l in ell[::2]]
        assert not any(diff[1::2]) and n==(q-1)//2
        fields.append(q)
    return dict(kind='exact_dual_symmetric_square_compact_feedback',fields=fields,
                D_pair_minus_K_source='4*n*(q+1)/q^2 K e0',raw_denominator='q^2',
                first_trivial_lift_trace_correction='2-2/q^2')

def lower():
    t=prev['t0'];jmax,strip=9,18
    # Build the five-center lower kernels at all source arities/shifts needed below.
    glob=old['lower'].__globals__
    jold,sold=glob['J'],glob['S']
    glob['J'],glob['S']=jmax+2,strip+8
    try:
        lo=old['lower'](prev['projected']())
    finally:
        glob['J'],glob['S']=jold,sold
    upper,pars=old['upper'](acb(t))
    w=coefficient(acb(t),0,2,0).real
    assert w>0
    a,b,c,d,z=pars
    M=kern['dim']+2*a+3*b+4*c+arb(23)*d/4+8*z
    rad=2; rt=(M+rad)**2/(4*t);bn=arb(1)
    for ell in range(1,16):bn*=(arb(3)/2-ell)/ell
    tail=2*t.sqrt()*abs(bn)*rt**15/(1-rt)
    assert rt<1
    # At degree two only the two unit contractions and the two
    # determinant-shifted exterior squares have repeated SL4 labels.
    repeated=arb_poly([3,0,0,0,8,0,0,0,3]).left_shift(4)
    assert sum(repeated.coeffs())==14
    rows=[]
    for j in range(jmax+1):
        vals=[arb(0) for k in range(-strip,strip+1)]
        err=arb(0)
        for h in range(3):
            r=j+h; mult=comb(r,j)*w**h; dim=4*h
            rem=repeated if h==2 else arb_poly()
            pos=(lo[r]*(powers[h]-rem))*mult.lower()
            u=upper[r]; side=[v/2 for v in u[1:]]; size=len(side)
            debit=arb_poly(side[::-1]+[u[0]]+side)*rem*mult.upper()
            err+=sum(rem.coeffs(),arb(0))*mult.upper()*tail/rad**r
            for k in range(-strip,strip+1):
                vals[strip+k]+=pos[strip+8+dim+k]-debit[size+dim+k]
        if j==0:
            for k in range(-4,5):vals[strip+k]-=source[4+k]*w.upper()
        mass=8*w.upper()
        for h in range(3,D-j+1):
            err+=comb(j+h,j)*mass**h*sum(upper[j+h],arb(0))
        ratio=mass/rad*(1+arb(j)/4);assert ratio<1
        err+=tail/rad**j*comb(j+3,j)*(mass/rad)**3/(1-ratio)
        rows.append(arb_poly([max(arb(0),(v-err).lower()) for v in vals]))
    return rows

def escape():
    rows=lower();n=28;strip=18
    assert rows[2][strip]>arb(1)/20
    h=[arb(0)]*n
    for height in range(1,6001):
        side=[v/2 for v in h]
        b=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        out=[arb(0)]*n;power=arb_poly([1])
        for j,row in enumerate(rows):
            if j:power*=b
            step=power*row
            for k in range(1,n+1):out[k-1]+=2*step[strip+j*n+k]
        h=[max(arb(0),v.lower()) for v in out]
        if sum(k*v for k,v in enumerate(h,1))>21:
            return dict(kind='fully_collected_joint_center_escape',height=height,mass_lower=21,
                    surviving_binary_zero_lower='1/20',floor='2031/128',D=D,J=9,S=18,N=28,precision=ctx.prec)
    raise ArithmeticError('no certified escape')

def cap_invariant(floor,ceiling,width,rows,pars,caps,eps=arb(3)/10**7):
    eta=arb(1)/5; h=[arb(v)/10**14 for v in caps]; n=len(h)
    # Positive packet k contributes k-1 to the zero atom; bound its ratio
    # to cosh(k/5) sharply. Convexity proves the estimate beyond k=10.
    assert all(k-1<arb(14)/5*(eta*k).cosh() for k in range(11))
    assert arb(14)/5*eta*(10*eta).sinh()>1
    zero=sum(i*v for i,v in enumerate(h))+arb(14)/5*eps+arb(1)/10**8
    core=arb_poly([v/2 for v in reversed(h)]+[zero]+[v/2 for v in h])
    norm=zero+sum(v*(eta*k).cosh() for k,v in enumerate(h,1))
    leak=arb(0); pooled=[arb(0)]*(D*n+5*D+1); power=arb_poly([1])
    for j,ker in enumerate(rows):
        if j:power*=core
        side=[v/2 for v in ker[1:]]
        row=power*arb_poly(side[::-1]+[ker[0]]+side);center=j*n+len(side)
        for k in range(1,len(row)-center):pooled[k]+=2*row[center+k]
        if j:leak+=sum(v*(eta*k).cosh() for k,v in enumerate(ker))*j*(norm+eps)**(j-1)*eps
    for k,v in enumerate(pooled[1:],1):
        leak+=max(arb(0),(v-(h[k-1] if k<=n else arb(0))).upper())*(eta*k).cosh()
    def cn(poly,r):return sum(poly[r+i]*(2 if i else 1)*(eta*i).cosh() for i in range(r+1))
    a,b,c,d,z,w=pars
    total=kern['dim']*eta.cosh()+a*(1+(2*eta).cosh())+b*(1+3*eta.cosh()/2+(3*eta).cosh()/2)
    total+=c*cn(kern['F'],4)+d*cn(kern['G'],5)+z*cn(old['R'],2)+w*cn(field,4)+norm+eps
    ratio=total**2/(4*floor);assert ratio<1
    bn=arb(1)
    for ell in range(1,16):bn*=(arb(3)/2-ell)/ell
    high=abs(acb(ceiling,arb(1)/width))
    leak+=2*high.sqrt()*abs(bn)*ratio**15/(1-ratio)
    full=kern['dim']+2*a+3*b+4*c+arb(23)*d/4+8*(z+w)+zero+sum(h)+eps
    return leak,full

def expanded_four(t):
    # Enlarge only the explicit GL3^2 character prefix of the preceding rank-four
    # certificate. Its distinguished amplitudes and upper tail have identical formulas.
    a0,b0=prev['da'],prev['db']
    f=arb(499)/500
    rows,a,b,c=kern['prior']['make'](t,4,5,9,8,5,a0,b0,f)
    alpha,beta,groups,amend=kern['p3']['coefficients'](t,acb(a0),acb(b0))
    gamma=f*beta*groups[1,1][0,0];v=gamma*kern['linear_scalar'](groups,beta)
    delta=-2*v
    F,G=kern['F'],kern['G']; gp=[G**i for i in range(D+1)]
    for k in range(6):
        rows[0][k]-=(abs(v)*(F[4+k-1]+F[4+k+1])*(2 if k else 1)).lower()
    result=[]
    for j in range(D+1):
        n=5*(D-j);p=arb_poly()
        for h in range(D-j+1):
            row=rows[j+h];side=[v/2 for v in row[1:]]
            term=arb_poly(side[::-1]+[row[0]]+side)*gp[h]
            p+=term.left_shift(n-len(side)-5*h)*(comb(j+h,j)*abs(delta).upper()**h)
        result.append([(p[n+k]*(2 if k else 1)).upper() for k in range(n+1)])
    return result,a,b,c,abs(delta).upper()

def mixed_rows(t):
    rows,*abcd=expanded_four(t)
    z,c1,c3=old['prefix'](t)
    rows[0][2]-=4*abs(z).lower()
    x,y=z*c1,3*z**3*c3
    saved=(2*(abs(x)*abs(y)-(x*y.conjugate()).real)/(abs(x)+abs(y)+abs(x+y))).lower()
    assert saved>0
    pol=[]
    for row in rows:
        side=[v/2 for v in row[1:]]
        pol.append(arb_poly(side[::-1]+[row[0]]+side))
    R=old['R']; rp=[R**i for i in range(D+1)]
    out=[]
    for j in range(D+1):
        n=5*(D-j);p=arb_poly()
        for h in range(D-j+1):
            p+=(pol[j+h]*rp[h]).left_shift(3*h)*(comb(j+h,j)*abs(z).upper()**h)
        if j==0:p-=(R*arb_poly([1,0,2,0,1])).left_shift(n-4)*saved
        out.append([(p[n+k]*(2 if k else 1)).upper() for k in range(n+1)])
    return out,abcd+[abs(z).upper()]

def signed():
    degree=28;t=prev['t0'];algebra=prev['old']
    a,b,c,d=prev['coefficients']();s=kern['dim']
    z=old['prefix'](acb(t))[0].real;w=coefficient(acb(t),0,2,0).real
    def join(tab,raw,scale):
        return algebra['add_inputs'](tab,[{e:v*scale**j for e,v in row.items()} for j,row in enumerate(raw)])
    tab=[{2*i-k:comb(k,i)*(s/2)**k for i in range(k+1)} for k in range(degree+1)]
    for l,r,scale,perverse in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
        factors=[(len(algebra['WEIGHTS'][i]),algebra['DETS'][i]) for i in range(l,r)]
        tab=join(tab,algebra['scalar_powers'](factors,degree,perverse),scale)
    mu=old['moments'](degree)
    tab=join(tab,[{0:v} for v in mu],z)
    leg=kern['p3']['P']
    def legendre(u,v):return join(tab,[{0:leg[k].get((u,v),0)} for k in range(degree+1)],a)
    dual=algebra['scalar_powers']([(4,4)],degree,True)
    assert dual[2]=={0:2} and dual[4]=={-4:1,0:12,4:1}
    base=s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*abs(z)
    def project(tab,e,j,mag):
        out=arb(0);bn=arb(1)
        for ell in range(1,degree//2+1):
            bn*=(arb(3)/2-ell)/ell
            if 2*ell>=j:
                out+=2*t.sqrt()*bn*comb(2*ell,j)/(4*t)**ell*tab[2*ell-j].get(e,0)
        ell=degree//2+1;bn*=(arb(3)/2-ell)/ell
        ratio=mag**2/(4*t)
        rt=ratio*comb(2*ell+2,j)/comb(2*ell,j);assert rt<1
        tail=2*t.sqrt()*abs(bn)*ratio**ell*comb(2*ell,j)/(mag**j*(1-rt))
        return out+arb(0,tail.upper())
    nosym=legendre(0,0);full=join(nosym,dual,w)
    u5=project(nosym,2,0,base)-a/2
    u7=project(full,2,0,base+8*abs(w))-a/2
    h2=project(nosym,2,2,base)
    quadratic=2*w**2*h2
    assert 0<u7<u5 and quadratic<0
    # Signed direct residuals on the two individual quadratic inputs.
    residual=project(join(legendre(2,0),dual,w),0,0,base+8*abs(w))-w
    def integers(v,n):
        return [int((v*n).lower().floor().unique_fmpz()),int((v*n).upper().ceil().unique_fmpz())]
    return dict(kind='signed_joint_center_Jacobi_projection',floor='2031/128',degree=degree,precision=ctx.prec,
                prefixed_dual_center_times_1e12=integers(w,10**12),
                old_m2_times_1e12=integers(u5,10**12),joint_m2_times_1e12=integers(u7,10**12),
                exact_binary_correction_times_1e12=integers(quadratic,10**12),
                joint_Sym2_residual_times_1e12=integers(residual,10**12),
                quartic_arithmetic_lines_at_shifts_minus4_0_4=[1,12,1])

CAPS=[24295000000001,10414734859664,5511623180378,2926420689778,1464888486660,
      711433544575,335604507754,163937543008,82209016605,42076315901,21891296601,
      11543486472,6155586448,3313793553,1798539235,983069185,540675332,298994277,
      166150137,92731848,51958833,29216672,16481757,9325161,5290333,3008777,
      1715119,979767,560801,321584,184725,106281,61241,35338,20419,11813,6842,
      3968,2303,1339,779,454,264,154,90,53,31,18,11,6]

def envelope(first,last,den,slices,width):
    rows=None;pars=[arb(0)]*6
    for i in range(first*slices,last*slices):
        t=acb(arb(2*i+1,1)/(den*slices*2),arb(0,1)/width)
        r,p=upper(t)
        rows=r if rows is None else [[max(x,y) for x,y in zip(a,b)] for a,b in zip(rows,r)]
        pars=[max(x,y) for x,y in zip(pars,p)]
    return rows,pars

def rectangle():
    first,last,den,slices,width=1040019,1040022,65536,8,2**20
    rows,pars=envelope(first,last,den,slices,width)
    floor=arb(first)/den
    leak,cap=cap_invariant(floor,arb(last)/den,width,rows,pars,CAPS)
    coord=arb(4654)/1000
    assert leak<arb(207)/10**9<arb(3)/10**7 and cap<coord
    assert coord/(4*floor-coord**2).sqrt()<arb(3)/4
    return dict(kind='physical_joint_center_rectangle',real_endpoints=[first,last],
                denominator=den,slabs=slices*(last-first),imaginary_half_width='1/1048576',
                precision=ctx.prec,core_excess_upper='207e-9',residual_budget='3e-7',
                coordinate_upper='4.654',mark_bound='3/sqrt(n)')

if __name__=='__main__':
    for check in (feedback,signed,escape,rectangle):
        print(json.dumps(check(),sort_keys=True),flush=True)
