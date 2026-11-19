"""Directed cross-list unit collision, using the nine-center moment tables."""
from math import comb
from pathlib import Path
import json
import runpy
from flint import arb, acb, ctx

ctx.prec = 192
r = runpy.run_path(str(Path(__file__).with_name("astra-joint-65-check.py")))
prev, kern, old, joint = (r[k] for k in ("prev", "kern", "old", "joint"))
alg = prev["old"]
t = prev["t0"]
a,b,c,d = prev["coefficients"]()
s = kern["dim"]
z = old["prefix"](acb(t))[0].real
w = joint["coefficient"](acb(t),0,2,0).real
v = r["selected"](acb(t)).real
M = s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*(abs(z)+abs(w)+abs(v))
D = 28
tab = [{2*i-k:comb(k,i)*(s/2)**k for i in range(k+1)} for k in range(D+1)]
def join(base, moments, scale):
    return alg["add_inputs"](base,[{e:x*scale**k for e,x in row.items()} for k,row in enumerate(moments)])
for l,h,x,p in ((2,4,b/4,False),(4,8,c/8,False),(8,16,d/16,True)):
    tab = join(tab,alg["scalar_powers"]([(len(alg["WEIGHTS"][i]),alg["DETS"][i]) for i in range(l,h)],D,p),x)
tab = join(tab,[{0:k} for k in old["moments"](D)],z)
tab = join(tab,alg["scalar_powers"]([(4,4)],D,True),w)
mu = r["symplectic_moments"](2,D)
tab = join(tab,[{0:sum(comb(j,k)*mu[k]*mu[j-k] for k in range(j+1))} for j in range(D+1)],v)
def project(j,e,u,h):
    T = join(tab,[{0:kern["p3"]["P"][k].get((u,h),0)} for k in range(D+1)],a)
    B = arb(1)
    out = arb(0)
    for k in range(1,16):
        B *= (arb(3)/2-k)/k
        term = 2*t.sqrt()*B*comb(2*k,j)/(4*t)**k
        if k<15:
            out += term*T[2*k-j].get(e,0)
    ratio = M**2/(4*t)*arb(comb(32,j))/comb(30,j)
    assert ratio<1
    return out+arb(0,(abs(term)*M**(30-j)/(1-ratio)).upper())

def band(x,lo,hi,scale):
    assert lo < x*scale < hi,(x,lo,hi,scale)
    return [lo,hi,scale]

u = project(0,2,0,0)-a/2
# At the next vertex the first regenerated tags have joint L2 at most E.
E = (4*arb('0.000153')**2+4*arb('0.000145')**2+arb('0.00000003')**2).sqrt()
def unary(e, tags=True):
    error = arb(2).sqrt()*E/(2*t.sqrt()) if tags else arb(0)
    return project(1,e,1,0)+project(1,e,0,1)+arb(0,error.upper())
# Regenerated m^2 arity-zero source: use rounds 65,66,68, including small Y.
# Safer elementary bound for Y than a sup norm: the known unary plus its remainder.
# At the first nonzero tag level the three per-pair amplitudes are the direct ones.
u2 = u + arb('0.000000000000049539', '0.000000000000000352') + arb('-0.0000000004515','0.0000000000435') + arb('-0.000000000010921','0.000000000002246')
neg = u*unary(2)
C = unary(0)
# H2=f''/2 >0 pointwise and E[(A+B)^2]=2.
radius = M+arb('0.008345')
Qlo = 4*t/(4*t+radius**2)**(arb(3)/2)
Qhi = 1/(2*t.sqrt())
# 2 H2 = f''; integrate the positive square.
binarylo,binaryhi = Qlo*u2**2,Qhi*u2**2
single = neg*C
def enclosure(x,n):
    return r["scaled"](x,n)
# Norm of (A+B)^2 is sqrt(10) and Taylor coefficient H2 has slope <= F3/2.
Q2 = (2*project(2,2,0,0)+project(2,2,2,0)+project(2,2,0,2)+2*project(2,2,1,1)
      +arb(0,(arb(10).sqrt()*E*3/(8*t)).upper()))
two2 = u2**2*Q2
one2 = neg*unary(2)
assert single < -binaryhi and one2 > -two2 > 0
# Uniform source at all later levels using the L2 norm of Y and the full slope.
uniform = u + arb(0,arb('0.427311')*arb('3e-8')) + arb('-0.0000000004515','0.0000000000435') + arb('-0.000000000010921','0.000000000002246')
assert 0 < uniform < arb('7e-8')
assert uniform*unary(2)**2 > arb('7e-8')**2*abs(Q2)
# This pays the original separate constituents before binary tensor collection.
# Each H2 projection is bounded by 1/(4 sqrt(t)) via orthogonality.
assert 2*arb('7e-8')**2*6/(4*t.sqrt()) < arb('4e-15')
print(json.dumps(dict(first_source=band(u,48,49,10**9),next_source=band(u2,47,49,10**9),
                      negative_source=band(neg,-7,-5,10**11),single_unit=band(single,-3,-1,10**12),
                      loss_unit_1e18=[enclosure(2*binarylo,10**18)[0],enclosure(2*binaryhi,10**18)[1]],
                      single_m2_1e18=enclosure(one2,10**18),binary_m2_1e18=enclosure(two2,10**18),
                      loss_m2_1e18=enclosure(-2*two2,10**18), full_binary_m2_kernel_1e6=enclosure(Q2,10**6)),sort_keys=True))
