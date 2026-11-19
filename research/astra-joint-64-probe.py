"""Floating fitting for the certified dyadic slabs; prints caps and outward margins."""
from pathlib import Path
import runpy,sys
from flint import arb,acb
import numpy as np
q=runpy.run_path(str(Path(__file__).with_name('astra-joint-64-check.py')))
fit=runpy.run_path(str(Path(__file__).with_name('astra-mixed-61-probe.py')))['fit']
if __name__=='__main__':
    start,end,den,slices,width=map(int,sys.argv[1:6])
    eps=float(sys.argv[6])
    first=float(sys.argv[7])
    rows,pars=q['envelope'](start,end,den,slices,width)
    h,res=fit(rows,prev=np.array(q['old']['CAPS'])*1e-14,first=first,eps=eps*2.8/5)
    caps=[max(1,int(x*1e14+1)) for x in h]
    leak,cap=q['cap_invariant'](arb(start)/den,arb(end)/den,width,rows,pars,caps,arb(str(eps)))
    print(start,end,den,slices,width,eps,first,float(res),float(leak),float(cap),caps,flush=True)
