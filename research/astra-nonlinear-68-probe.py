"""Floating diagnostic for the one-tag triangle debit. Not proof evidence."""
import numpy as np
import runpy
from pathlib import Path
from flint import acb, arb, arb_poly
from math import comb
s=runpy.run_path(str(Path(__file__).with_name("astra-shifted-66-check.py")))
p=s["prior"]
v=p["selected"](acb(s["t"])).real
lo=p["lower"](p["lower_data"](),abs(v))
up,pars=p["upper"](acb(s["t"]))
a,b,c,d,z,w,vabs=pars
base=p["kern"]["dim"]+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+vabs)
small=arb(3)/10**8
limits=[arb(153)/10**6,arb(145)/10**6]
var=4*sum(v**2 for v in limits)
debit,err,size=s["debit"](up,base,small,limits,var,s["transports"]())
toarr=lambda a: np.array([float(v) for v in a.coeffs()])
out=np.zeros((10,37))
for r in range(10):
    out[r]=toarr(lo[r]-debit[r])
errors=np.array([float(x) for x in err])
U=[]
for row in up:
    ss=[float(x/2) for x in row[1:]]
    U.append(np.array(ss[::-1]+[float(row[0])]+ss))
zz=np.array([1,0,0,0,3,0,3,0,0,0,1])*0.0
zz=np.array([1,0,3,4,3,0,1])*0.000145
# Sum the (-3,0^4,3) and (-1^3,1^3) boundaries.
add=np.zeros_like(out)
for r in range(10):
    pol=2*(r+1)*np.convolve(U[r+1],zz)
    mid=len(pol)//2
    add[r]=pol[mid-18:mid+19]
def iterate(kernel,errors,n=28,steps=8500,period=1,burst=1):
    h=np.zeros(n)
    for i in range(steps):
        side=h/2
        b=np.r_[side[::-1],np.dot(np.arange(n),h),side]
        bm=np.sum(b)
        acc=np.zeros(n)
        power=[1.]
        for r,row in enumerate(kernel if i%period<burst else out):
            if r: power=np.convolve(power,b)
            step=np.pad(np.convolve(row,power),(0,n))
            acc+=2*(step[18+r*n+1:18+r*n+1+n]-errors[r]*bm**r)
        new=np.maximum(acc,0)
        mass=np.dot(new,np.arange(1,n+1))
        if mass>21 or max(abs(h-new))<1e-15: return i+1,mass
        h=new
    return i+1,mass
if __name__=="__main__":
    for q in (100,160,200,240,256,280,300,320,400,512):
        print(q,iterate(out-add,errors,period=q,burst=2,steps=8000),flush=True)
