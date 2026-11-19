"""Optional floating cap selection, separate from the proof replay."""
from pathlib import Path
import runpy
import sys
import numpy as np

q = runpy.run_path(str(Path(__file__).with_name('astra-legendre-63-check.py')))
fit = runpy.run_path(str(Path(__file__).with_name('astra-mixed-61-probe.py')))['fit']
if __name__=='__main__':
    first,last,sub,width=map(int,sys.argv[1:5])
    rows,pars=q['envelope'](first,last,sub,width)
    start=np.array(q['prev']['CAPS'])*1e-14
    start[1]-=4*float(pars[-1])
    h,res=fit(rows,prev=start,first=.24297)
    caps=[max(1,int(x*1e14+1)) for x in h]
    leak,cap=q['validate'](first,last,width,rows,pars,caps)
    print(first,last,sub,width,res,float(leak),float(cap),caps)
