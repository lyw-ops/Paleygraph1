"""Floating cap search only. The certificate uses the frozen rational table."""
from pathlib import Path
import runpy
check=runpy.run_path(str(Path(__file__).with_name('astra-ranknext-58-check.py')))
approx=runpy.run_path(str(Path(__file__).with_name('astra-rankthree-56-probe.py')))['approx']
if __name__=='__main__':
    import sys
    first,last=map(int,sys.argv[1:3])
    rows,*data=check['envelope'](first,last,2)
    h,i,mass=approx(rows,eps=.0000006,n=50,height=15000,margin=1.e-7)
    print(i,mass)
    if mass<2:
        caps=[int(v*10**14+1) for v in h]
        print(caps)
        print(check['validate'](first,last,2**20,rows,*data,caps))
