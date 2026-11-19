"""Floating diagnostics for signed hinge descent; no interval certification."""
import json, runpy
from pathlib import Path
import numpy as np
R=runpy.run_path(str(Path(__file__).with_name('parallel-repair-17.py')))

def run(sign,side,raw,steps=128):
 n=len(sign); P,kappa,omega,(h,translate),_=R['sector_tools'](sign,side)
 alpha=min(2,1/(kappa+omega)); D=np.maximum(-raw,0); b=.75*(1-raw.mean())
 A=np.full(n,b)
 for _ in range(4): A+=alpha*P(np.maximum(D-A,0))
 _,cut,_=R['cap'](D-A,h); t=.5*cut; G=A+t; initial=G.copy()
 unit=np.zeros(n);unit[0]=1
 records=[]; sum_norm=0.; first_norm=None
 for k in range(steps+1):
  r=D-G;e=np.maximum(r,0);e[0]=0;v=P(e);ee=e@e
  if first_norm is None:first_norm=np.sqrt(ee)
  sum_norm+=np.sqrt(ee)
  if k in (0,1,4,16,32,128):
   duals=[]
   scale=e.max()
   if scale>1e-12:
    z=e/scale
    for lam in (0,.5,1,2):
     u=z+lam*unit; w=u-P(u);delta=max(0,-w.min());w+=delta
     duals.append(dict(mark_completion=lam,padding=delta,lower_mean=float(w@D/w.sum())))
   tail,ft,remaining=R['cap'](D-G,h)
   records.append(dict(step=k,support=int((e>1e-12).sum()),energy=float(ee),summability_ratio=float(sum_norm/first_norm) if first_norm else 0,rayleigh=float(v@v/ee) if ee else 0,
    mark_charge=float(max(r[0],0)/h),finish_mean=float(G.mean()+tail),dual=duals))
  if k==steps:break
  newG=G+alpha*v;rr=D-newG;en=np.maximum(rr,0);en[0]=0
  # Exact switching identity: Taylor remainder of squared hinge.
  beta=(en@en-ee+2*alpha*(v@v))/alpha**2
  # beta is weighted active-segment v^2, hence lies in [0, ||Pv||? = ||v||^2].
  tol=1e-8*max(1,ee)
  assert -tol<=beta<=v@v+tol
  # Fejer equality relative to initial state (not assumed feasible).
  lhs=np.sum((newG-initial)**2)-np.sum((G-initial)**2)
  rhs=-2*alpha*ee-2*alpha*np.dot(e,initial-D)+alpha**2*np.dot(v,v)
  assert abs(lhs-rhs)<tol
  if records and records[-1]['step']==k:
   records[-1].update(next_energy_ratio=float(en@en/ee) if ee else 0,secant_beta=float(beta/ee) if ee else 0,
    entered=int(((e<=0)&(en>0)).sum()),left=int(((e>0)&(en<=0)).sum()))
  G=newG
 return dict(alpha=alpha,height=h,mean=float(initial.mean()),cutoff=t,records=records)

if __name__=='__main__':
 for q,root in [(9413,None),(153649,None),(9409,97),(151321,389)]:
  sign=R['paley_sign'](q) if root is None else R['square_field_sign'](root)
  for width,_,plus,minus,residual in R['damped_trials'](sign,[1/64],1e-11,48):
   for side,y in [(1,minus),(-1,plus)]:
    raw=np.sqrt(len(sign))*np.fft.ifft((sign!=side)*np.fft.fft(y)).real
    print(json.dumps(dict(order=q,side=side,width=width,reference_residual=residual,**run(sign,side,raw))),flush=True)
