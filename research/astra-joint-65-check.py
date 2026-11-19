"""Collect the two Sp4 outputs of the fourth Jacobi mode in the joint seed."""
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly, ctx

joint = runpy.run_path(str(Path(__file__).with_name("astra-joint-64-check.py")))
prev, kern, old = (joint[k] for k in ("prev", "kern", "old"))
D = joint["D"]
field = joint["field"]  # The two independent symplectic standards have this same boundary sum.


def selected(t):
    a, b, g, amend = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    c = arb(499)/500*b*g[1,1][0,0]
    shapes = kern["p3"]["rank_powers"](4)
    def scalar(j, e):
        if abs(e)>5:
            return acb(0)
        out = acb(0)
        for h, parts in enumerate(shapes):
            for (a1,b1,a2,b2,shift), mult in parts.items():
                if a1 or b1 or a2 or b2:
                    continue
                k = abs(e-shift)
                if k>9:
                    continue
                row = amend[k] if j+h==0 and k in amend else g[j+h,k]
                out += row.get((0,0),0)*comb(j+h,j)*(b/4)**h*mult/(2 if k else 1)
        return out
    def at(e):
        return (scalar(0,e)+c**2*scalar(2,e)/8+
                c**4*(196*scalar(4,e)+2*scalar(4,e+2)+2*scalar(4,e-2))/4096)
    v=at(4)
    assert v.real<0 and v.overlaps(at(-4))
    return v


def upper(t):
    rows, pars = joint["upper"](t)
    v = selected(t)
    rows[0][4] -= 2*abs(v).lower()
    base=[]
    for row in rows:
        side=[x/2 for x in row[1:]]
        base.append(arb_poly(side[::-1]+[row[0]]+side))
    result=[]
    for j in range(D+1):
        center=5*(D-j)
        row=arb_poly()
        for h in range(D-j+1):
            row+=(base[j+h]*joint["powers"][h]).left_shift(h)*comb(j+h,j)*abs(v).upper()**h
        result.append([(row[center+k]*(2 if k else 1)).upper() for k in range(center+1)])
    return result, pars+[abs(v).upper()]


def lower_data():
    t = prev["t0"]
    low = joint["lower"]()
    upper, pars = joint["upper"](acb(t))
    a,b,c,d,z,w=pars
    mass = kern["dim"]+2*a+3*b+4*c+arb(23)*d/4+8*(z+w)
    radius = arb(2)
    ratio = (mass+radius)**2/(4*t)
    assert ratio<1
    binom = arb(1)
    for ell in range(1,16):
        binom *= (arb(3)/2-ell)/ell
    tail = 2*t.sqrt()*abs(binom)*ratio**15/(1-ratio)
    return low,upper,tail


def lower(data,magnitude):
    low,upper,tail = data
    up=[]
    for row in upper:
        side=[v/2 for v in row[1:]]
        up.append((arb_poly(side[::-1]+[row[0]]+side),len(side)))
    radius=arb(2)
    rows=[]
    strip, jmax=18,9
    for j in range(jmax+1):
        values=[arb(0)]*(2*strip+1)
        err=arb(0)
        for h in range(3):
            r=j+h
            mult=comb(r,j)*magnitude**h
            retn=arb_poly([2]).left_shift(8) if h==2 else arb_poly()
            oldlo=low[r] if r<len(low) else arb_poly()
            pos=oldlo*(joint["powers"][h]-retn)*mult.lower()
            u,center=up[r]
            debit=u*retn*mult.upper()
            for k in range(-strip,strip+1):
                values[strip+k]+=pos[strip+4*h+k]-debit[center+4*h+k]
            if h==2:
                err+=2*mult.upper()*tail/radius**r
        if j==0:
            for k in (-4,4):
                values[strip+k]-=magnitude.upper()
        size=8*magnitude.upper()
        for h in range(3,D-j+1):
            err+=comb(j+h,j)*size**h*sum(upper[j+h],arb(0))
        ratio=size/radius*(1+arb(j)/4)
        assert ratio<1
        err+=tail/radius**j*comb(j+3,j)*(size/radius)**3/(1-ratio)
        rows.append(arb_poly([max(arb(0),(v-err).lower()) for v in values]))
    return rows


def escape(rows):
    n,strip=28,18
    assert rows[2][strip]>arb(1)/20
    h=[arb(0)]*n
    for height in range(1,8001):
        side=[v/2 for v in h]
        b=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        out=[arb(0)]*n
        power=arb_poly([1])
        for j,row in enumerate(rows):
            if j:
                power*=b
            step=power*row
            for k in range(1,n+1):
                out[k-1]+=2*step[strip+j*n+k]
        h=[max(arb(0),v.lower()) for v in out]
        if sum(k*v for k,v in enumerate(h,1))>21:
            return height
    raise ArithmeticError("surviving lower recursion did not cross 21")


def symplectic_moments(rank,limit):
    from collections import Counter
    zero=(0,)*rank
    row={zero:1}
    moments=[1]
    for j in range(limit):
        new=Counter()
        for shape,value in row.items():
            for i in range(rank):
                for direction in (-1,1):
                    child=list(shape)
                    child[i]+=direction
                    if child[-1]>=0 and child==sorted(child,reverse=True):
                        new[tuple(child)]+=value
        row=new
        moments.append(row.get(zero,0))
    return moments


def dual_sectors(limit):
    """Multiplicities on D and Ddual in (D+Ddual)^j, keyed by Jacobi exponent."""
    from collections import Counter
    states={(0,0,0,0):1}
    rows=[[],[]]
    for k in range(limit+1):
        left,right={},{}
        for shape,val in states.items():
            l=shape[-1]
            part=tuple(a-l for a in shape)
            if part==(1,0,0,0):
                left[4*l]=val
            if part==(1,1,1,0):
                right[4*(l+1)]=val
        rows[0].append(left)
        rows[1].append(right)
        if k==limit:
            break
        nxt=Counter()
        for shape,val in states.items():
            for i in range(4):
                for step in (-1,1):
                    child=list(shape)
                    child[i]+=step
                    if child==sorted(child,reverse=True):
                        nxt[tuple(child)]+=val
        states=nxt
    assert rows[0][3]=={-4:1,0:6} and rows[1][3]=={4:1,0:6}
    return rows


def projection_data():
    algebra=prev["old"]
    a,b,c,d=prev["coefficients"]()
    t=prev["t0"]
    s=kern["dim"]
    z=old["prefix"](acb(t))[0].real
    w=joint["coefficient"](acb(t),0,2,0).real
    v=selected(acb(t)).real
    def join(table,factor,scale):
        return algebra["add_inputs"](table,[{e:x*scale**j for e,x in row.items()}
                                             for j,row in enumerate(factor)])
    table=[{2*i-j:comb(j,i)*(s/2)**j for i in range(j+1)} for j in range(D+1)]
    for l,r,scale,perverse in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
        factors=[(len(algebra["WEIGHTS"][i]),algebra["DETS"][i]) for i in range(l,r)]
        table=join(table,algebra["scalar_powers"](factors,D,perverse),scale)
    prior=table
    r_mom=[{0:k} for k in old["moments"](D+1)]
    q_mom=algebra["scalar_powers"]([(4,4)],D+1,True)
    table=join(join(table,r_mom,z),q_mom,w)
    base=s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*(abs(z)+abs(w))
    mu=symplectic_moments(2,D+1)
    assert mu[:7]==[1,0,1,0,3,0,14]
    both=[sum(comb(j,k)*mu[k]*mu[j-k] for k in range(j+1)) for j in range(D+2)]
    assert both[:7]==[1,0,2,0,12,0,118]
    u_mom=[{0:k} for k in both]
    with_pair=join(table,u_mom,v)
    def project(j,e,u,ell,pair):
        tab=join(with_pair if pair else table,
                 [{0:kern["p3"]["P"][k].get((u,ell),0)} for k in range(D+1)],a)
        M=base+8*abs(v) if pair else base
        return evaluate(tab,j,e,M)
    def evaluate(tab,j,e,M,amplitude=1):
        out=arb(0)
        bn=arb(1)
        for k in range(1,D//2+1):
            bn*=(arb(3)/2-k)/k
            if 2*k>=j:
                out+=2*t.sqrt()*bn*comb(2*k,j)/(4*t)**k*tab[2*k-j].get(e,0)
        k=D//2+1
        bn*=(arb(3)/2-k)/k
        rt=M**2/(4*t)
        ratio=rt*comb(2*k+2,j)/comb(2*k,j)
        assert ratio<1
        return out+arb(0,(amplitude*2*t.sqrt()*abs(bn)*rt**k*comb(2*k,j)/(M**j*(1-ratio))).upper())
    # Full post-amendment coefficients for the five arity-zero residual leaves.
    tags = (project(0,4,0,0,True)-v,project(0,0,2,0,True)-w,project(0,0,1,1,True)-z)
    assert tags[1].overlaps(project(0,0,0,2,True)-w)
    assert tags[0].overlaps(project(0,-4,0,0,True)-v)
    seven=project(0,2,0,0,False)-a/2
    nine=project(0,2,0,0,True)-a/2
    binary=2*v**2*project(2,2,0,0,False)
    assert 0<nine<seven and binary<0
    # A marked X in a moment E[X^k X] uses E[X^(k+1)], including
    # determinant lines for the D pair. This measures the outer unary on each tag.
    scalar_leg=[{0:kern["p3"]["P"][k].get((0,0),0)} for k in range(D+1)]
    prior=join(prior,scalar_leg,a)
    unaries=[]
    first_u=None
    full=base+8*abs(v)
    for marked in range(3):
        tab=prior
        for i,(mom,scale) in enumerate(((u_mom,v),(q_mom,w),(r_mom,z))):
            tab=join(tab,mom[1:] if i==marked else mom,scale)
        unaries.append(evaluate(tab,1,2,full,8)*tags[marked])
        if marked==0:
            first_u=evaluate(tab,0,1,full,8)/2
    # Resolve the two arithmetic standards even on a nonzero Jacobi label.
    other=join(join(prior,u_mom,v),r_mom,z)
    leading=[evaluate(join(other,mom,w),0,1,full) for mom in dual_sectors(D)]
    assert first_u<0 and all(x>0 for x in leading)
    m=8*sum(abs(x) for x in tags)
    paired_return=sum(unaries)+arb(0,(m**2/(4*t.sqrt())).upper())
    assert paired_return>0
    return v, seven, nine, binary, tags, unaries, paired_return, [first_u]+leading


def pair_debit(up,pars,tags):
    radius=arb(2)
    t=prev["t0"]
    a,b,c,d,z,w,v=pars
    M=kern["dim"]+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+v)
    rt=(M+radius)**2/(4*t)
    assert rt<1
    binom=arb(1)
    for k in range(1,16):
        binom*=(arb(3)/2-k)/k
    tail=2*t.sqrt()*abs(binom)*rt**15/(1-rt)
    U=[]
    for row in up:
        side=[x/2 for x in row[1:]]
        U.append(arb_poly(side[::-1]+[row[0]]+side))
    vv,ww,zz=(abs(x).upper() for x in tags)
    tag=(vv+ww)*field+zz*old["R"].left_shift(2)
    size=8*(vv+ww+zz)
    assert size<arb(5)/10**8
    powers=[tag**h for h in range(D+1)]
    debit=[]
    errors=[]
    for r in range(10):
        center=5*(D-r)
        total=arb_poly()
        for h in range(1,D-r+1):
            total+=(U[r+h]*powers[h]).left_shift(h)*comb(r+h,r)
        outside=max([arb(0)]+[total[center+k].upper() for k in range(19,center+1)])
        ratio=size/radius*(1+arb(r)/2)
        assert ratio<1
        analytic=tail/radius**r*(r+1)*size/radius/(1-ratio)
        errors.append((2*(outside+analytic)).upper())
        debit.append(arb_poly([(2*total[center+k]).upper() for k in range(-18,19)]))
    return debit,errors


def pair_escape(rows,debit,errors):
    n,strip=28,18
    assert rows[2][strip]-debit[2][strip]-errors[2]>arb(1)/20
    h=[arb(0)]*n
    for height in range(1,8001):
        side=[v/2 for v in h]
        b=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        size=sum(b.coeffs(),arb(0)).upper()
        out=[arb(0)]*n
        power=arb_poly([1])
        extra=arb(0)
        for r,row in enumerate(rows):
            if r:
                power*=b
            if height%2==0:
                step=power*(row-debit[r])
                extra+=errors[r]*size**r
            else:
                step=power*row
            for k in range(1,n+1):
                out[k-1]+=2*step[strip+r*n+k]
        h=[max(arb(0),(v-2*extra).lower()) for v in out]
        if sum(k*v for k,v in enumerate(h,1))>21:
            return height
    raise ArithmeticError("paired map did not cross 21")


def feedback():
    sample=runpy.run_path(str(Path(__file__).with_name("astra-prime-phase-32-check.py")))
    fields=[]
    for p,k in ((5,1),(3,2),(13,1),(17,1),(5,2),(7,2),(97,1)):
        _,ell,*_=sample["data"](p,k)
        conv=sample["cycconv"]
        q=p**k
        n=(q-1)//2
        base=ell[::2]
        q2=conv(base,base)
        q4=conv(q2,q2)
        f2=conv(ell,ell)
        f4=conv(f2,f2)
        for i in range(n):
            raw=8*q4[i]-8*q*q2[i]+q*q*(i==0)
            assert n*(raw-f4[2*i])==q*q-8*q+7
        fields.append(q)
    return dict(kind="exact_fourth_Jacobi_compact_feedback",fields=fields,
                K2C4_minus_two_Sp4="2*(1-8/q+7/q^2) K e0",identity_stalk=0)


def scaled(x,n):
    return [int((x*n).lower().floor().unique_fmpz()),
            int((x*n).upper().ceil().unique_fmpz())]


def run():
    print(json.dumps(feedback(),sort_keys=True),flush=True)
    v,seven,nine,binary,tags,unaries,total,leading=projection_data()
    assert all(x>0 for x in unaries)
    print(json.dumps(dict(kind="signed_nine_center_and_paired_Jacobi_coefficients",
        floor="2031/128",degree=D,precision=ctx.prec,center_times_1e12=scaled(v,10**12),
        m2_seven_times_1e12=scaled(seven,10**12),m2_nine_times_1e12=scaled(nine,10**12),
        new_binary_m2_times_1e12=scaled(binary,10**12),
        tags_v_w_z_times_1e12=[scaled(x,10**12) for x in tags],
        unary_return_v_w_z_times_1e18=[scaled(x,10**18) for x in unaries],
        full_paired_return_times_1e18=scaled(total,10**18),
        first_mU_mD_mDdual_times_1e12=[scaled(x,10**12) for x in leading],
        shifted_cubic_standard_dual=[[-4,1],[4,1]]),sort_keys=True),flush=True)
    data=lower_data()
    rows=lower(data,abs(v))
    band=lower(data,arb(1,arb(1)/1000)*abs(v))
    print(json.dumps(dict(kind="full_one_vertex_symplectic_pair_escape",floor="2031/128",
        exact_height=escape(rows),annulus_height=escape(band),relative_modulus=["999/1000","1001/1000"],
        mass_lower=21,binary_zero_lower="1/20",shape=[9,18,28]),sort_keys=True),flush=True)
    up,pars=upper(acb(prev["t0"]))
    debit,errors=pair_debit(up,pars,tags)
    print(json.dumps(dict(kind="unrestricted_tag_degree_five_leaf_pair_escape",floor="2031/128",
        height=pair_escape(rows,debit,errors),mass_lower=21,binary_zero_lower="1/20",
        tagged_mass_upper="5e-8",shape=[9,18,28]),sort_keys=True),flush=True)


if __name__=="__main__":
    run()
