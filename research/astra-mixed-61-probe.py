"""Floating diagnostics for fitting a one-step packet cap. The Arb replay verifies the chosen cap."""
import runpy
from pathlib import Path
import numpy as np
from scipy.optimize import root
from flint import arb
q=runpy.run_path(str(Path(__file__).with_name("astra-ranknext-58-check.py")))
def fit(rows,n=50,eps=6e-7,prev=None,first=None):
    d=16
    size=2048
    mats=[]
    for row in rows[:d]:
        v=np.array([float(x) for x in row])
        arr=np.zeros(size)
        arr[0]=v[0]
        if len(v)>1:
            arr[1:len(v)]=v[1:]/2
            arr[1-len(v):]=v[:0:-1]/2
        mats.append(np.fft.rfft(arr).real)
    mats=np.array(mats)
    idx=np.arange(n)
    D=np.cos(2*np.pi*np.arange(size//2+1)[:,None]*(idx+1)/size)+idx
    def fun(h,jac=False):
        b=np.r_[sum(h*idx)+5*eps+1e-8,h/2,np.zeros(size-2*n-1),h[::-1]/2]
        z=np.fft.rfft(b).real
        if jac:
            der=(d-1)*mats[-1]
            for j in range(d-2,0,-1):
                der=der*z+j*mats[j]
            return 2*np.fft.irfft(der[:,None]*D,axis=0)[1:n+1]*(1+1e-7)-np.eye(n)
        g=mats[-1]
        for val in mats[-2::-1]:
            g=g*z+val
        return 2*np.fft.irfft(g)[1:n+1]*(1+1e-7)-h
    if prev is None: prev=np.array(q['CAPS'])*1e-14
    if first is not None:
        def full(v): return np.r_[first,v]
        sol=root(lambda v:fun(full(v))[1:],prev[1:],jac=lambda v:fun(full(v),True)[1:,1:],tol=2e-13)
        h=full(sol.x)
        return h,fun(h)[0]
    sol=root(fun,prev,jac=lambda h:fun(h,True),tol=2e-13)
    return sol.x,np.max(abs(fun(sol.x)))
if __name__=='__main__':
    import sys
    for i in map(int,sys.argv[1:]):
        rows,*data=q['envelope'](i,i+2,2,2**20)
        h,res=fit(rows)
        caps=[max(0,int(x*1e14+1)) for x in h]
        z,v=q['validate'](i,i+2,2**20,rows,*data,caps)
        print(i,res,z,v,caps,flush=True)
