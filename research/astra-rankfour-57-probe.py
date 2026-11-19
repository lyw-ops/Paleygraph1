"""Floating cap generation only. The proof uses the fixed tables in the checker."""
from pathlib import Path
import runpy
import sys
m=runpy.run_path(str(Path(__file__).with_name("astra-rankfour-57-check.py")))
old=runpy.run_path(str(Path(__file__).with_name("astra-rankthree-56-probe.py")))
if __name__=="__main__":
    first,last=map(int,sys.argv[1:3])
    w,*abc=m["envelope"](first,last,65536,65536)
    h,i,mass=old["approx"](w,eps=.0000006,n=50,height=13500,margin=1.e-7)
    print(i,mass,flush=True)
    if mass < 2:
        caps=[int(v*10**14+1) for v in h]
        print(caps,flush=True)
        print(m["validate"](first,last,65536,65536,w,*abc,caps,0),flush=True)
