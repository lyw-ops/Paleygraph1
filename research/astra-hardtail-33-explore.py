"""Exploratory floating probes; stdout only. Run with -B."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from poisson_weights import weighted_iterate
from smoothing import kernel_action

def probe(s,tau=.05):
 n=len(s); w=np.full(n,tau/n); w[0]=1; a=np.sqrt(w.mean())
 v,phi,res=weighted_iterate(s,w,tolerance=1e-11,rounds=64)
 hi=(phi+abs(v))/2; lo=w/hi
 best=(0,None,None)
 for side in [1,-1]:
  A=np.where(side*v>=0,hi,lo); u=A/a; d=(tau/n)/(a*A)
  for R in np.unique(np.r_[0,u[1:]]):
   h=a*np.maximum(u-R,0); h[0]=0; eta=h.sum()/(n*a)
   if eta<1e-15:continue
   z=(h-h.mean()-side*kernel_action(s,h))/2
   ratio=np.dot(d,z*z)/eta
   if ratio>best[0]:best=(float(ratio),side,float(R))
 return best,res
if __name__=='__main__':
 rng=np.random.default_rng(33)
 for n in [16,32,64,128,256]:
  best=(0,None,None); bad=0
  for j in range(100):
   s=np.zeros(n); x=rng.choice([-1,1],n//2); s[1:n//2+1]=x; s[n//2+1:]=x[-2::-1]
   row,res=probe(s)
   if res>1e-8: bad+=1;continue
   if row[0]>best[0]:best=row; witness=s.astype(int).tolist()
  print(json.dumps({'n':n,'best':best,'failed':bad,'sign':witness}),flush=True)
