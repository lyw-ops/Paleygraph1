"""Fully old rank-six refresh on two consecutive levels per 256, then unrestricted."""
from pathlib import Path
import runpy
from flint import acb,arb,arb_poly

x=runpy.run_path(str(Path(__file__).with_name("astra-nonlinear-68-check.py")))
p,s,t=x["p"],x["previous"],x["t"]
up,pars=p["upper"](acb(t))
a,b,c,d,z,w,v=pars
base=p["kern"]["dim"]+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+v)
ycap=arb(3)/10**8
caps=[arb(153)/10**6,arb(145)/10**6]
rows=p["lower"](p["lower_data"](),v)
c6=4*caps[0]**2+2*caps[1]**2
full=x["all_sibling_debit"](up,base,ycap,caps,c6)
prior=s["debit"](up,base,ycap,caps,c6+2*caps[1]**2,s["transports"]())
choices=[([a-b for a,b in zip(rows,cost)],err) for cost,err,_ in (prior,full)]
assert all(K[2][18]-err[2]>arb(1)/20 for K,err in choices)
h=[arb(0)]*28
for height in range(1,6001):
    kernel,errors=choices[(height-1)%256<2]
    side=[x/2 for x in h]
    b=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
    m=sum(b.coeffs(),arb(0)).upper()
    power=arb_poly([1])
    err=arb(0)
    out=[arb(0)]*28
    for r,row in enumerate(kernel):
        if r: power*=b
        prod=row*power
        err+=errors[r]*m**r
        for k in range(1,29):
            out[k-1]+=2*prod[18+28*r+k]
    h=[max(arb(0),(v-2*err).lower()) for v in out]
    if sum(k*v for k,v in enumerate(h,1))>21:
        x["record"]("consecutive_fully_old_signed_refresh_escape",height=height,
                    precision=192,period=256,active_one_based_residues=[1,2],
                    mass_threshold=21,shape=[9,18,28])
        break
else:
    raise ArithmeticError("scheduled lower iterate failed to cross")
