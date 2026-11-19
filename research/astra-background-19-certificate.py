"""Arb certificate: first Picard cost cap misses actual prime initial tail."""
import json,runpy,sys
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H.parent))
R=runpy.run_path(str(H/'parallel-repair-17.py'))
Q=runpy.run_path(str(H/'parallel-defect-16.py'))
ctx.prec=128
p=9413;sign=R['paley_sign'](p);n=len(sign);s=arb(1)/64;beta=s/(1-s*s);root=arb(n).sqrt()
_,_,xp,ym,res=next(R['damped_trials'](sign,[1/64],1e-12,64))
v,phi0,error=Q['reference_balls'](sign,1/64,xp,ym)
lam=acb.dft([int(a) for a in sign])
for side in [1,-1]:
    x=[max(arb(0),side*z) for z in v];y=[max(arb(0),-side*z) for z in v]
    x[0]=(phi0+side*v[0])/2;y[0]=(phi0-side*v[0])/2;c=sum(y)/root
    P,kap,omega,(height,_),_=R['sector_tools'](sign,side)
    approx_y=ym if side==1 else xp
    D=np.sqrt(n)*np.maximum(-approx_y.mean()-P(approx_y),0)
    m=int(np.ceil(height));indices=np.argpartition(D,-m)[-m:]
    j=1+int(np.argmax(side*np.fft.fft(sign).real[1:]))
    omega_lower=(1+side*lam[j].real)/(2*n)
    hb=1+(arb(int(np.count_nonzero(sign==-side)))/n)/omega_lower
    assert hb<m
    # Each selected positive part exceeds its un-clipped argument, so no interval max needed.
    selected=sum(beta*(root*x[int(i)]-(1-s)*c-(root+1-s)*error) for i in indices)/m
    assert 0 not in indices
    U=2*s/(1+s)**2*(arb(p)/n).sqrt()
    raw=acb.dft([z if a in [0,-side] else acb(0) for z,a in zip(acb.dft(y),sign)],inverse=True)
    assert raw[0].real-error>0
    gap=selected-U
    assert gap>0
    print(json.dumps(dict(prime=p,side=side,width='1/64',recipient_count=m,height_upper=str(hb.upper()),stationary_error_l2_upper=str(error),actual_selected_average_lower=str(selected.lower()),first_picard_uniform_upper=str(U.upper()),actual_minus_reference_tail_lower=str(gap.lower()),positive_projected_mark_lower=str((raw[0].real-error).lower()))))
