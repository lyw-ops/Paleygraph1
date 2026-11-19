"""Selected-factor exterior competitor and unary original-price envelopes."""
from math import comb
from pathlib import Path
import runpy
from flint import ctx
from flint import arb, arb_poly, acb

here=Path(__file__).parent
q=runpy.run_path(str(here/"astra-unary-69-check.py"))
p,old,t,project=q["p"],q["old"],q["t"],q["project"]
D=28
scalar,marked,base=q["tables"]()
up,pars=p["upper"](acb(t))
runpy.run_path(str(here/"astra-unary-69-base.py"))["configure"](p)
rows=p["lower"](p["lower_data"](),pars[-1])
caps=[arb(153)/10**6,arb(145)/10**6]
c6=4*caps[0]**2+2*caps[1]**2
costs,errors,g=old["all_sibling_debit"](up,base,arb(3)/10**8,caps,c6,True)
amp=arb(144291005,24500)/10**12
u=abs(p["prev"]["coefficients"]()[2])/8
# A+Adual+Achi+Achi_dual from the fixed boundary lists.
T=arb_poly([3,2,6,2,3])*u
W=arb_poly([1,0,3,4,3,0,1])
assert sum(T.coeffs(),arb(0)).overlaps(16*u)

def core(row):
    side=[x/2 for x in row[1:]]
    return arb_poly(side[::-1]+[row[0]]+side)

def radius5(pol,rad):
    return pol.left_shift(5-rad)

T=radius5(T,2)
W=radius5(W,3)
tp=[T**h for h in range(D+1)]
# Bounds for the complementary polynomial H_j(V-T), j>=1.
U=[core(row) for row in up]
Q=[sum((comb(j+h,j)*U[j+h]*tp[h] for h in range(D-j+1)),arb_poly()) for j in range(D+1)]
# T^h on exactly the two exterior outputs via scalar and marked Pieri.
alg=p["prev"]["old"]
one=alg["scalar_powers"]([(4,-2)],D,False)
mt=alg["add_inputs"](one,old["linear"]["marked_factors"](D))
E=[]
for h,row in enumerate(mt):
    coeff=[arb(0)]*(10*h+1)
    for e,k in row.items():
        for wt in range(-5,6):
            if W[5+wt] and k:
                coeff[5*h+wt-e] += abs(k)*u**h*W[5+wt]
    E.append(arb_poly(coeff))
# Tail from all Taylor degrees above 28. Every projected price is bounded
# by the positive dimension majorant; the derivative translates use actual V0.
bn=arb(1)
for k in range(1,16):
    bn*=(arb(3)/2-k)/k
# Direct sector needs at least two T factors; unaries on nontrivial factors need one.
for r in range(10):
    nontrivial_input=sum((comb(r+1+h,h)*Q[r+1+h]*tp[h] for h in range(1,D-r)),arb_poly())
    direct=sum((comb(r+h,h)*Q[r+h]*E[h] for h in range(2,D-r+1)),arb_poly())
    charge=2*(direct+(r+1)*caps[1]*nontrivial_input*W)
    center=5*(D-r)
    # On explicitly resolved labels the T-trivial unary is known exactly from
    # its scalar preimage. It consumes at most the smaller direct price when
    # the signs differ. Subtract the certified unused direct charge.
    credit=[arb(0)]*37
    for e in range(-12,13):
        d=project(marked,base,r,e)
        v=-(r+1)*amp*project(scalar,base,r+1,e)
        refund=max(arb(0),(abs(d)+abs(d+v)-abs(v)).lower())
        for wt in range(-5,6):
            if abs(wt-e)<=18:
                credit[18+wt-e]+=refund*W[5+wt]
    # Choose two distinguished T slots for the direct, or one for the unary.
    def tail_derivative(j):
        k=15
        rt=base**2/(4*t)
        ratio=rt*comb(2*k+2,j)/comb(2*k,j)
        assert ratio<1
        return 2*t.sqrt()*abs(bn)*rt**k*comb(2*k,j)/base**j/(1-ratio)
    an=tail_derivative(r+2)*((16*u)**2*comb(r+2,2)
                              +12*caps[1]*(r+1)*(r+2)*16*u)
    outside=max([arb(0)]+[charge[center+k].upper() for k in range(19,center+1)])
    costs[r]+=arb_poly([charge[center+k].upper() for k in range(-18,19)])-arb_poly(credit)
    errors[r]+=outside+2*an.upper()

if __name__=="__main__":
    # The first update has zero incoming tags. All subtracted net envelopes
    # are nonnegative after restoring the blanket error, even at that update.
    assert all((row[k]+err)>=0 for row,err in zip(costs,errors) for k in range(37))
    height,binary=old["previous"]["escape"](rows,costs,errors)
    old["record"]("full_old_every_level_zero_start_escape",floor="2031/128",
                  precision=ctx.prec,height=height,mass_threshold=21,
                  binary_times_1e9=q["scaled"](binary,10**9),
                  total_tags_times_1e9=q["scaled"](g,10**9),
                  shape=[9,18,28])
