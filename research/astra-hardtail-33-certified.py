"""Rigorous finite all-threshold HR checks using Arb and a Banach enclosure.

Only stdout is written. Run with -B. Decimal diagnostics are not used for
acceptance; every certification comparison uses Arb enclosures.
"""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from flint import arb,acb,ctx,fmpq
from theta import paley_sign
from poisson_weights import weighted_iterate

def exact_float(x):
 p,q=float(x).as_integer_ratio(); return arb(fmpq(p,q))
def up(x): return str(x.upper())
def fft_K(s,x):
 n=len(s); f=acb.dft([acb(z) for z in x])
 # DFT squared is n times inversion; x and s are even here.
 return [(z/n).real for z in acb.dft([s[j]*f[j] for j in range(n)])]
def project(s,side,x):
 k=fft_K(s,x); mean=sum(x,arb(0))/len(x)
 return [(xj-mean-side*kj)/2 for xj,kj in zip(x,k)]
def emit(x):print(json.dumps(x,sort_keys=True),flush=True)
def certify(p,tau_string,rad_string,witness_R=None):
 s=paley_sign(p).astype(int).tolist(); n=len(s)
 assert s[0]==0 and sum(s)==-1 and all(s[j]==s[-j%n] for j in range(n))
 tau=arb(tau_string);c=tau/n; W=1+(n-1)*c; a=(W/n).sqrt();rho=tau/W
 w=[arb(1)]+[c]*(n-1); rad=arb(rad_string)
 wf=np.array([float(x) for x in w]); v,_,rawres=weighted_iterate(np.array(s),wf,tolerance=1e-14,rounds=128)
 # Make the chosen approximate vector exactly even, with rational entries.
 v=(v+v[(-np.arange(n))%n])/2;v0=[exact_float(x) for x in v]
 phi=[(x*x+4*wi).sqrt() for x,wi in zip(v0,w)]
 kv=fft_K(s,phi);eps=sum(((ki-vi)**2 for ki,vi in zip(kv,v0)),arb(0)).sqrt()
 bounds=[(abs(x)+rad)/((abs(x)+rad)**2+4*wi).sqrt() for x,wi in zip(v0,w)]
 L=max(b.upper() for b in bounds)
 assert L<1 and eps<(1-L)*rad, ('Banach ball failed',p,eps,L,rad)
 emit({'kind':'rigorous_stationary_enclosure','p':p,'n':n,'tau':tau_string,'precision_bits':ctx.prec,
       'radius_l2':rad_string,'residual_norm_upper':up(eps),'L_upper':up(L),
       'banach_margin_lower':str(((1-L)*rad-eps).lower()),'certified':True})
 for side in [1,-1]:
  calcA=[(ph+side*x)/2 for ph,x in zip(phi,v0)]
  centers=[exact_float(float(z.mid())) for z in calcA]
  centererr=max(abs(z-x).upper() for z,x in zip(calcA,centers))
  rA=rad+centererr
  assert all(centers[i]==centers[-i%n] for i in range(n))
  assert all(x-rA>0 for x in centers)
  # Uniform coordinate bounds follow from the proved l2 distance and |A'|<=1.
  du=[(c/(a*(x-rA))).upper() for x in centers]
  dmax=max(du)
  if witness_R is not None:
   R=arb(witness_R); exact_t=a*R; t=exact_float(float(exact_t.mid()))
   err=rA+abs(exact_t-t).upper()
   h=[arb(0)]+[max(x-t,arb(0)) for x in centers[1:]]
   z=project(s,side,h);mass=sum(h,arb(0))
   dl=[(c/(a*(x+rA))).lower() for x in centers]
   nominal=sum((di*zi**2 for di,zi in zip(dl,z)),arb(0)).sqrt()
   norm_lower=(nominal-err*(n*dmax).sqrt()).lower()
   assert norm_lower>0
   ratio_lower=(norm_lower**2*n*a/(mass+n*err)).lower()
   assert ratio_lower>1, ('C=1 counterexample not certified',ratio_lower)
   emit({'kind':'rigorous_actual_hot_C1_counterexample','p':p,'side':side,
         'tau':tau_string,'R':witness_R,'ratio_lower':str(ratio_lower),
         'certified_ratio_exceeds_one':True,
         'scope':'does not contradict HR with a tau-dependent constant'})
   continue
  # Every possible exact hinge knot is included: inversion pairs coincide exactly.
  knots=[None]+list(range(1,n//2+1))
  max_ratio=arb(0); worst=None; fallback=0
  for j in knots:
   t=arb(0) if j is None else centers[j]
   h=[arb(0)]
   for i in range(1,n):
    dif=centers[i]-t
    if dif>0:h.append(dif)
    elif dif<0 or dif.is_zero():h.append(arb(0))
    else: raise AssertionError('rational difference comparison unclear')
   # t=A_j varies by at most rA, hence h differs by at most 2*rA per coordinate.
   err=rA if j is None else 2*rA
   mass=sum(h,arb(0)); ml=mass-n*err;mu=mass+n*err
   if ml>0:
    z=project(s,side,h)
    norm=sum((di*zi**2 for di,zi in zip(du,z)),arb(0)).sqrt()
    upper=((norm+err*(n*dmax).sqrt())**2*n*a/ml).upper()
   else:
    # For any nonnegative h: ||D^.5 P h||<=sqrt(dmax)*||h||_1.
    # This handles the terminal zero/near-zero tail without dividing by eta.
    upper=(n*a*dmax*mu).upper();fallback+=1
   assert upper<1,('HR C=1 not certified',p,side,j,upper)
   if upper>max_ratio:max_ratio=upper;worst=j
  emit({'kind':'rigorous_all_threshold_HR','p':p,'n':n,'side':side,'tau':tau_string,
        'C':1,'knots_checked':len(knots),'terminal_mass_bound_count':fallback,
        'maximum_certified_ratio_upper':up(max_ratio),'worst_knot_index':worst,
        'coordinate_enclosure_radius_upper':up(rA),'all_R_ge_zero_certified':True,
        'scope':'one exact stationary pair; no prime-uniform conclusion'})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--primes',nargs='+',type=int,default=[101,401,1009]);ap.add_argument('--tau',default='0.05');ap.add_argument('--radius',default='1e-9');ap.add_argument('--bits',type=int,default=128);ap.add_argument('--witness-R',default=None);args=ap.parse_args();ctx.prec=args.bits
 for p in args.primes:certify(p,args.tau,args.radius,args.witness_R)
 emit({'kind':'all_checks_passed','primes':args.primes,'tau':args.tau,'arithmetic':'Arb outward-rounded balls plus exact integer multipliers'})
