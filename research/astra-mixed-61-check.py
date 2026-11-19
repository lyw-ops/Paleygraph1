"""Signed old-sector regrouping with arbitrary residual siblings, at the limiting floor."""
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly, ctx

previous = runpy.run_path(str(Path(__file__).with_name("astra-rankeight-60-check.py")))
old = previous["last"]
kern = previous["kern"]
floor = arb(2031) / 128
U, V, W, Z = [arb(n)/10**9 for n in (30611, 900251, 850223, 1700513)]
C = 2*V**2 + 2*W**2 + Z**2
tag_mass = 8*(V+W+Z)
N, S, J = 28, 18, 9



def signed_saving():
    # Pure Jacobi m^1 coefficient of H_3=[y^3] sqrt(4t+(V+y)^2).
    # Conditional standard-power tables include the signs of determinant shifts.
    degree=20
    a,b,g,_=kern["p3"]["coefficients"](acb(floor),acb(-arb(7)/100000),acb(-arb(6)/100000))
    c=arb(499)/500*b*g[1,1][0,0]
    d=-2*c*kern["linear_scalar"](g,b)
    a,b,c,d=[x.real for x in (a,b,c,d)]
    seed=kern["dim"]
    table=[{2*i-k:comb(k,i)*(seed/2)**k for i in range(k+1)} for k in range(degree+1)]
    for i,j,scale,perverse in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
        fam=[(len(old["WEIGHTS"][k]),old["DETS"][k]) for k in range(i,j)]
        raw=old["scalar_powers"](fam,degree,perverse)
        table=old["add_inputs"](table,[{e:z*scale**k for e,z in row.items()}
                                       for k,row in enumerate(raw)])
    leg=kern["p3"]["P"]
    table=old["add_inputs"](table,[{0:a**k*leg[k].get((0,0),0)} for k in range(degree+1)])
    coeff=arb(1)
    result=arb(0)
    for ell in range(1,degree//2+1):
        coeff*=(arb(3)/2-ell)/ell
        if 2*ell>=3:
            result+=2*floor.sqrt()*coeff/(4*floor)**ell*comb(2*ell,3)*table[2*ell-3].get(1,0)
    # Bound the derivative tail termwise at its first omitted degree;
    # binomial(2l,3) ratios decrease with l and |binomial(1/2,l)| decreases.
    mass=seed+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4
    ell=degree//2+1
    coeff*=(arb(3)/2-ell)/ell
    ratio=mass**2/(4*floor)
    ratio_cap=ratio*comb(2*ell+2,3)/comb(2*ell,3)
    assert ratio_cap<1
    tail=2*floor.sqrt()*abs(coeff)*ratio**ell*comb(2*ell,3)/(mass**3*(1-ratio_cap))
    result+=arb(0,tail.upper())
    clo=(2*arb(900249)**2+2*arb(850221)**2+arb(1700511)**2)/10**18
    cup=C
    saving_lo=-6*result.upper()*clo
    saving_hi=-6*result.lower()*cup
    assert -arb(2)/100<result<0 and 3*cup*abs(result)<arb(169624)/10**6
    return dict(kind="opposite_signed_old_Jacobi_multiplier_with_residual_sibling",
                floor="2031/128",Taylor_degree=degree,shift=[-1,1],arity_pair=[1,3],
                cubic_multiplier_nano=[int((result.lower()*10**9).floor().unique_fmpz()),
                                      int((result.upper()*10**9).ceil().unique_fmpz())],
                saving_per_shift_femto=[int((saving_lo*10**15).floor().unique_fmpz()),
                                       int((saving_hi*10**15).ceil().unique_fmpz())],precision=ctx.prec)


def prepared():
    rows, a, b, c, d = kern["make"](acb(floor))
    low = kern["new_kernels"](floor, shift=S)
    M = kern["dim"] + 2*a + 3*b + 4*c + arb(23)*d/4
    radius = arb(2)
    ratio = (M+radius)**2/(4*floor)
    assert ratio<1
    coeff = arb(1)
    for i in range(1,16):
        coeff *= (arb(3)/2-i)/i
    tail = 2*floor.sqrt()*abs(coeff)*ratio**15/(1-ratio)
    def atom(j,k):
        k = abs(k)
        return (rows[j][k]/(2 if k else 1) if k<len(rows[j]) else 0)
    def rem(j):
        return tail/radius**j
    def upper(j,k):
        return atom(j,k)+rem(j)
    def nonleading(k):
        return upper(1,k)-(arb(169624)/10**6 if abs(k)==1 else 0)
    unary = [4*U*(nonleading(k)+(nonleading(k-2)+nonleading(k+2))/2)
             for k in range(N+1)]
    assert all(x>0 for x in unary)
    loss, uniform = [], []
    zero_projection_cap = None
    for r in range(J+1):
        p2=comb(r+2,2)*C
        p4=comb(r+4,4)
        # Full signed shifts on det(D) and det(D^dual) in the old projection.
        def small(k):
            return (p2*atom(r+2,k) +
                    p4*(3*C**2*atom(r+4,k) +
                        W**4*(atom(r+4,k-4)+atom(r+4,k+4))))
        # Large-arity tagged returns may contain arbitrary old shifts.
        big = sum(comb(r+h,r)*tag_mass**h*sum(rows[r+h])
                  for h in range(6,len(rows)-r,2))
        t_ratio=tag_mass/radius*(1+arb(r)/7)
        assert t_ratio<1
        big += rem(r)*comb(r+6,r)*(tag_mass/radius)**6/(1-t_ratio)
        series_tail=p2*rem(r+2) + p4*(3*C**2+2*W**4)*rem(r+4) + big
        # Off-strip atoms are charged by a uniform single-bin upper bound.
        offstrip=max([arb(0)]+[small(k) for k in range(S+1,len(rows[r+2])+5)])
        uniform.append((2*(series_tail+offstrip)).upper())
        loss.append(arb_poly([(2*small(k)).upper() for k in range(-S,S+1)]))
        if r==2:
            zero_projection_cap=small(0)+series_tail
    quadratic=(low[2][S]-zero_projection_cap).lower()
    assert quadratic>arb(1)/20 and tag_mass<arb(28)/1000
    return low,loss,uniform,unary,quadratic


def escape():
    low,loss,uniform,unary,quadratic=prepared()
    # An upper bound for the fixed C2 leaf u(A+B), at each of the two twists.
    old_tag=arb_poly([U,0,2*U,0,U]).left_shift(N-2)
    h=[arb(0)]*N
    for height in range(1,8501):
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(j*v for j,v in enumerate(h))]+side)
        power=arb_poly([1])
        out=[arb(0)]*N
        grouped=(height%2==0)
        if grouped:
            upper_base=base+old_tag
            upper_total=sum(upper_base.coeffs()).upper()
            upper_power=arb_poly([1])
            common=arb(0)
        for r,ker in enumerate(low):
            if r: power*=base
            step=ker*power
            if grouped:
                if r: upper_power*=upper_base
                step-=loss[r]*upper_power
                common+=uniform[r]*upper_total**r
            for k in range(1,N+1):
                out[k-1]+=2*step[S+r*N+k]
        if grouped:
            out=[v-2*(unary[k]+common) for k,v in enumerate(out,1)]
        h=[max(arb(0),v.lower()) for v in out]
        if sum(i*v for i,v in enumerate(h,1))>21:
            return dict(kind="arbitrary_residual_siblings_all_even_tag_returns_escape",
                        floor="2031/128",certified_height=height,packets=N,arities=J,
                        shift=S,precision=ctx.prec,quadratic_zero_lower="1/20",
                        discarded_tag_dimension_upper="0.028",mass_lower=21,
                        exact_quartic_old_shifts=[-4,0,4],
                        old_sibling_counts="all",tagged_return_degrees="all")
    raise ArithmeticError("escape not certified")


CAPS = [
    24244501591847,11076337879653,5501899402071,3089676327967,1460914329785,
    709168293193,334332832426,163217201937,81797966868,41840468156,21755319091,
    11464789038,6109889700,3287184812,1783007585,973984111,535351204,295869012,
    164312892,91650353,51321444,28840611,16259659,9193872,5212658,2962786,1687870,
    963610,551216,315894,181346,104273,60047,34628,19996,11561,6693,3879,2250,1307,
    760,442,258,150,88,51,30,18,10,5
]


def rectangle():
    first,last=1040026,1040036
    width=2**20
    rows,*parts=kern["envelope"](first,last,1,width)
    excess,full=kern["validate"](first,last,width,rows,*parts,CAPS)
    cap=arb(4651)/1000
    assert excess<arb(396)/10**9<arb(6)/10**7 and full<cap
    assert cap/(4*arb(first)/65536-cap**2).sqrt()<arb(3)/4
    return dict(kind="fourth_seed_refitted_actual_rectangle",endpoints=[first,last],
                denominator=65536,slabs=last-first,imaginary_half_width="1/1048576",
                frozen_caps=len(CAPS),precision=ctx.prec,coordinate_upper="4.651",
                core_excess_upper="396e-9",residual_budget="6e-7",mark_upper="3/sqrt(n)")


if __name__=="__main__":
    for test in (signed_saving,escape,rectangle):
        print(json.dumps(test(),sort_keys=True),flush=True)
