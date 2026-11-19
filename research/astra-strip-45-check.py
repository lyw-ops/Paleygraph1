"""Verified Fourier-supported primal and dual predictors on physical disk chains."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys
import numpy as np
from scipy.sparse.linalg import LinearOperator, gmres
from flint import acb, arb, arb_poly, ctx
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign

ctx.prec = 128

def rat(q):
    q = Fraction(q)
    return arb(q.numerator)/q.denominator

def approx(sign, x, R, deg, newton_steps):
    n = len(sign)
    def K(v):
        return np.fft.irfft(sign[:n//2+1]*np.fft.rfft(v), n)
    w = np.full(n, x/n)
    w[0] = 1.
    v = np.zeros(n)
    for _ in range(40):
        v = K(np.sqrt(v*v+4*w))
    def linear(rhs,d):
        op = LinearOperator((n,n),matvec=lambda u: u-d*K(u),dtype=float)
        ans, flag = gmres(op,rhs,atol=0.,rtol=2e-13,restart=120,maxiter=50)
        if flag:
            raise ValueError("numerical preprocessor",flag)
        return ans
    for _ in range(newton_steps):
        s = np.sqrt(v*v+4*w)
        resid = K(s)-v
        if np.linalg.norm(resid)<3e-15:
            break
        v += resid + K(linear((v/s)*resid,v/s))
    s = np.sqrt(v*v+4*w)
    vs,ss = [v], [s]
    for j in range(1,deg+1):
        src = np.zeros(n)
        if j==1:
            src[0]=-4*R
        for k in range(1,j):
            src += vs[k]*vs[j-k]-ss[k]*ss[j-k]
        sj = linear(src/(2*s),v/s)
        ss.append(sj)
        vs.append(K(sj))
    A=(np.array(ss)+vs)/2
    B=(np.array(ss)-vs)/2
    mu=np.mean(A,axis=1)
    # Normalize plus mean to one and transfer the scalar series to minus.
    U = np.empty_like(A)
    V = np.zeros_like(B)
    for j in range(deg+1):
        U[j]=(A[j]-sum(mu[k]*U[j-k] for k in range(1,j+1)))/mu[0]
        for k in range(j+1):
            V[j]+=mu[k]*B[j-k]
    return U,V

def projection(row,sign,side,mean):
    """Exact dyadic samples; bound pointwise change to exact Fourier support."""
    n=len(sign)
    half = [arb(float(t)) for t in row[:n//2+1]]
    full = half + half[-2:0:-1]
    fhat = acb.dft(full)
    error = sum((abs(fhat[i])*(1 if 2*i==n else 2) for i in range(1,n//2+1) if sign[i]!=side),arb(0))
    if mean is not None:
        error += abs(fhat[0]-mean*n)
    tol = arb(0,(error/n).upper())
    return [t+tol for t in half]

def disks(sign, x, R, N, newton_steps=8):
    n=len(sign)
    rr = rat(R)
    X = rat(x)
    U,V=approx(sign,float(x),float(R),N,newton_steps)
    us = [projection(row,sign,1,int(j==0)) for j,row in enumerate(U)]
    vs = [projection(row,sign,-1,None) for row in V]
    one=arb(1)
    bulk=X/n
    delta=one/64
    sup, errsq=arb(0),arb(0)
    for i,(u,v) in enumerate(zip(zip(*us),zip(*vs))):
        w = one if i==0 else bulk
        assert u[0]>0
        hi=sum((abs(uj) for uj in u[1:]),arb(0))/u[0]
        if not hi<1:
            raise ValueError("predictor coordinate",float(x),i,hi)
        sup=max(sup,hi.upper())
        target=arb_poly([w,-rr]) if i==0 else arb_poly([w])
        residual=target-arb_poly(list(u))*arb_poly(list(v))
        local=sum((abs(vv) for vv in residual.coeffs()),arb(0))/(w*(1-hi))
        errsq += (1 if 2*i in (0,n) else 2)*w*local.upper()**2
    error=errsq.nonnegative_part().sqrt()
    b=sup+delta
    lip=(1+rr)/(1-b)**2-1 if b<1 else arb(2)
    rad=delta*min(one,bulk).sqrt()
    if not (lip<1 and error<(1-lip)*rad):
        raise ValueError("disk",float(x),float(sup),float(lip),float(error),float(rad))
    logerr=error/((1-lip)*(1-b))
    # The physical log differs by log(1+h_0)-log(U_0(y)/U_0(0)).
    # Normalization adds (log(1-z/W)-log(1-z))/2 up to a constant.
    # Differentiate in v=log(x/t) after combination of the log derivatives.
    F=arb_poly([a[0] for a in us])
    W=1+(n-1)*bulk
    # y=z/R, dy/dv=-(1-R*y)/R.
    E=arb_poly([one,-rr])
    C=arb_poly([one,-rr/W])
    def D(p):
        return -E*p.derivative()*(1/rr)
    F1=D(F)
    F2=D(F1)
    F3=D(F2)
    G=F3*F**2-3*F1*F2*F+2*F1**3
    G0=E*(W-1)*(W-1-E)*(1/(2*W**3))
    num=G*C**3+G0*F**3
    den=(C*F)**3
    base=C*F
    qnum=D(num)*base-3*num*D(base)
    qden=base**4
    def signed(v):
        y=(1-v.exp())/rr
        return num(y)/den(y),qnum(y)/qden(y)
    # Enclose dm/d(log(x/t)) at the center via the verified log-disk.
    signed.first_center=F1[0]/F[0]+(1/W-1)/2+arb(0,(logerr/(1+rr).log()).upper())
    return signed,logerr,lip,error/((1-lip)*rad),arb(0,logerr.upper())+(us[0][0]*(W/n).sqrt()).log()

def run(p, R, U, N, theta, probe=None, square=False):
    sign=square_field_sign(p) if square else paley_sign(p)
    centers=[Fraction(1,32)]
    while centers[-1]<2048:
        centers.append(min(Fraction(2048),centers[-1]*U))
    if probe:
        centers=[Fraction(x) for x in probe]
    lip=fraction=arb(0)
    stats=[[arb(0) for _ in range(5)] for _ in range(2)]
    endpoints={}
    for j,x in enumerate(centers):
        cubic,de,l,rf,mark=disks(sign,x,R,N,20 if square else 8)
        if j in (0,len(centers)-1):
            endpoints[str(x)]=mark.str(13)
        if probe:
            print(x, "logerr",de,"lip",l,"rel_res",rf,"cubic",cubic(arb(0)),flush=True)
            continue
        left=-(rat(centers[j+1]/x)).log()/2 if j+1<len(centers) else arb(0)
        right=rat(x/centers[j-1]).log()/2 if j else arb(0)
        margin=(1+rat(R)).log()-max(abs(left).upper(),abs(right).upper())
        assert margin>0
        errs=[6*de/margin**3,24*de/margin**4]
        lip=max(lip,l.upper())
        fraction=max(fraction,rf.upper())
        step=(right-left)/32
        for k in range(32):
            mid=left+(k+arb(1)/2)*step
            wide=cubic(mid+arb(0,step.upper()/2))
            narrow=cubic(mid)
            for i,(q,exact,derr) in enumerate(zip(wide,narrow,errs)):
                val=abs(q+arb(0,derr.upper()))
                st=stats[i]
                st[0]+=step*max(arb(0),val.lower())
                st[1]+=step*val.upper()
                st[2]=max(st[2],abs(exact+arb(0,derr.upper())).lower())
                st[3]=max(st[3],val.upper())
                st[4]=max(st[4],derr.upper())
    if probe:
        return
    r=rat(U).sqrt()
    assert (r-1)**2+r*rat(theta)**2<rat(R)**2
    def show(value):
        return value.str(10)
    print(json.dumps(dict(kind="physical_fourier_predictor_chain",order=p*p if square else p,n=len(sign),x_first=str(centers[0]),x_last=str(centers[-1]),centers=len(centers),ratio=str(U),degree=N,disk=str(R),angular_width=str(theta),derivatives={str(i+3):dict(integral_lower=show(st[0].lower()),integral_upper=show(st[1].upper()),sup_lower=show(st[2].lower()),sup_upper=show(st[3].upper()),max_cauchy_error=show(st[4])) for i,st in enumerate(stats)},endpoint_marks=endpoints,max_lipschitz=show(lip),max_residual_fraction=show(fraction)),sort_keys=True),flush=True)
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--square",action="store_true",help="interpret --prime as the square-field characteristic")
    parser.add_argument("--prime",type=int,default=7681)
    parser.add_argument("--radius",type=Fraction,default=Fraction(1,12))
    parser.add_argument("--ratio",type=Fraction,default=Fraction(11,10))
    parser.add_argument("--degree",type=int,default=10)
    parser.add_argument("--angle",type=Fraction,default=Fraction(13,200))
    parser.add_argument("--probe",nargs="+")
    a=parser.parse_args()
    run(a.prime,a.radius,a.ratio,a.degree,a.angle,a.probe,a.square)
