"""Actual-Paley signed/weighted-operator diagnostics; not certificates."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from poisson_weights import weighted_iterate
from theta import paley_sign
from square_control import square_field_sign
from smoothing import kernel_action

def emit(x):print(json.dumps(x,sort_keys=True),flush=True)
def analyze(q,char,tau):
 s=paley_sign(q) if q==char else square_field_sign(char);n=len(s);c=tau/n
 w=np.full(n,c);w[0]=1;W=w.sum();a=np.sqrt(W/n);rho=tau/W
 v,phi,res=weighted_iterate(s,w,tolerance=1e-13,rounds=128)
 assert res<1e-10
 high=(phi+abs(v))/2;low=w/high
 k=np.fft.ifft(s).real;idx=np.arange(n);K=k[(idx[:,None]-idx[None,:])%n]
 for side in [1,-1]:
  A=np.where(side*v>=0,high,low);B=w/A;d=c/(a*A);b=(1-c)/A[0]
  P=(np.eye(n)-1/n-side*K)/2;e=P[:,0];p0=P[0,0];sd=d.sum()
  m1=d@(e*e);linear=B[0]/a*(1-(1-c)*p0)-1
  lower=linear**2/(sd*d[0]);T=np.sqrt(d)[:,None]*P/np.sqrt(d)[None,:]
  fullnorm=np.linalg.norm(T,2)**2;bulknorm=np.linalg.norm(T[:,1:],2)**2
  hs=(T*T).sum();pred=n*p0+(1-c)/c*(p0-np.dot(e*e,A)/A[0])
  errors=[abs(e@d-linear),abs(sd-(n-b/a)),abs(hs-pred)/max(1,hs)]
  assert max(errors)<1e-8 and fullnorm+1e-9>=lower
  emit({'kind':'floating_actual_weighted_projection','q':q,'characteristic':char,'tau':tau,'side':side,
        'full_operator_norm_squared':fullnorm,'bulk_input_operator_norm_squared':bulknorm,
        'proved_mark_column_lower_evaluated':lower,'mark_column_ratio':m1/d[0],
        'rank_one_Fourier_norm_squared':d.mean()*np.mean(1/d),
        'HS_squared_per_dimension':hs/n,'identity_max_error':max(errors),
        'stationary_residual':res})
  # Direct signed triangle, with the exact mark subtraction retained.
  for R in [0.,2.,4.]:
   h=np.maximum(A-a*R,0);h[0]=0;eta=h.sum()/(n*a);z=P@h
   E=np.flatnonzero(s==-side);r=np.fft.fft(h)[E]/n;beta=np.fft.fft(B/a)/n
   diff=(E[:,None]-E[None,:])%n
   tri=n*np.vdot(r,(beta[diff]*(s[diff]==-side))@r).real
   diag=n*np.vdot(r,r).real;mark=b/a*abs(r.sum())**2;energy=d@(z*z)
   err=abs(energy-(diag+tri-mark));assert err<1e-8
   emit({'kind':'floating_signed_triangle','q':q,'side':side,'tau':tau,'R':R,
         'eta':eta,'H2':energy,'diagonal':diag,'signed_triangle':tri,'mark_subtraction':mark,
         'negative_beta_count':int(np.sum(beta[E].real < -1e-10)),
         'negative_r_count':int(np.sum(r.real < -1e-10)),
         'identity_error':err})
if __name__=='__main__':
 for q,ch in [(101,101),(401,401),(1009,1009),(361,19),(961,31)]:analyze(q,ch,.05)
 emit({'kind':'all_checks_passed','scope':'floating diagnostics only'})
