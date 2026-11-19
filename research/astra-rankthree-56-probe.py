"""Floating diagnostics for choosing core caps for the interval replay."""
import numpy as np
from pathlib import Path
import runpy
certificate=runpy.run_path(str(Path(__file__).with_name("astra-rankthree-56-check.py")))


def approx(w,eps=0.00006,n=46,height=4000,margin=1e-7):
    # Truncate high arities and tiny shifts to choose caps only.
    kernels=[np.array([float(a) for a in row[:30]]) for row in w[:15]]
    h=np.zeros(n)
    for i in range(height):
        zero=sum(np.arange(n)*h)+eps*5+1e-8
        b=np.r_[h[::-1]/2,zero,h/2]
        g=np.array([1.])
        out=np.zeros(n)
        for j,ker in enumerate(kernels):
            tmp=np.convolve(g,np.r_[ker[:0:-1]/2,ker[0],ker[1:]/2])
            p=len(tmp)//2
            take=min(n,len(tmp)-p-1)
            out[:take]+=2*tmp[p+1:p+1+take]
            if j+1<len(kernels):
                g=np.convolve(g,b)
                p=len(g)//2
                r=min(p,n+40)
                g=g[p-r:p+r+1]
        out*=1+margin
        if np.abs(out-h).max()<2e-14: break
        h=out
        if h.sum()>10: break
    return h,i,sum(np.arange(1,n+1)*h)


if __name__=="__main__":
    w,_,_=certificate["envelope"](32504,32544,2048,8192)
    h,_,_=approx(w,eps=0.000002,height=4500)
    print([int(v*10**13+1) for v in h])
