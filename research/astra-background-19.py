"""Actual Picard references and localized errors; floating diagnostics only."""
import argparse,csv,runpy,sys
from pathlib import Path
import numpy as np
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H.parent))
from smoothing import kernel_action
R=runpy.run_path(str(H/'parallel-repair-17.py'))

def pair(v):
    u=np.abs(v); u[0]=np.hypot(v[0],2)
    return (u+v)/2,(u-v)/2

def orbit(D,b,P,alpha,k=4):
    r=D-b
    for _ in range(k):r=r-alpha*P(np.maximum(r,0))
    return r

def injection(r,limit,P,alpha,T):
    C=np.minimum(np.maximum(r,0),limit); C[0]=max(r[0],0)
    f=C-alpha*P(C)+np.minimum(r,0)-limit
    return float(np.maximum(f[T],0).sum()),C,f

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--primes',type=int,nargs='*',default=[9413,37253,153649]);ap.add_argument('--roots',type=int,nargs='*',default=[97,193,389]);ap.add_argument('--width',type=float,default=1/64);a=ap.parse_args();writer=None
    for q,ell,fn in [(p,None,R['paley_sign']) for p in a.primes]+[(r*r,r,R['square_field_sign']) for r in a.roots]:
        sign=fn(ell or q);n=len(sign);s=a.width;d=(1-s)/(1+s)
        _,_,xp,ym,res=next(R['damped_trials'](sign,[s],1e-12,64));vstar=xp-ym
        v=np.zeros(n)
        for t in range(129):
            if t in [0,1,2,4,8,16,32,64,128]:
                xt,yt=pair(v)
                for side,x,y,xx,yy in [(1,xp,ym,xt,yt),(-1,ym,xp,yt,xt)]:
                    P,kap,om,(h,_),_=R['sector_tools'](sign,side);alpha=min(2,1/(kap+om));c=np.sqrt(n)*y.mean();ct=np.sqrt(n)*yy.mean();B=1-c;b=.75*B
                    D=np.sqrt(n)*np.maximum(-y.mean()-P(y),0)
                    Dt=s/(1-s*s)*np.maximum(np.sqrt(n)*xx-(1-s)*ct,0);Dt[0]=0
                    Dproj=np.sqrt(n)*np.maximum(-yy.mean()-P(yy),0)
                    rr=orbit(D,b,P,alpha);rt=orbit(Dt,b,P,alpha)
                    m=int(np.ceil(h));T=np.argpartition(rr,-m)[-m:];U=np.argpartition(D,-m)[-m:]
                    r3=orbit(D,b,P,alpha,3); rt3=orbit(Dt,b,P,alpha,3)
                    target=rr>B/5;target[0]=False
                    inj,C,f=injection(r3,B/5,P,alpha,target)
                    injt,Ct,ft=injection(rt3,B/5,P,alpha,target)
                    injection_error=np.abs(f-ft)[target].sum()/h
                    if abs(inj-injt)/h>injection_error+1e-9:raise RuntimeError("injection stability")
                    err=np.linalg.norm(v-vstar);costerr=np.linalg.norm(D-Dt)
                    row=dict(order=q,root=ell,side=side,width=s,picard_depth=t,stationary_residual=res,height=h,injection_actual=inj/h,injection_reference_on_actual_target=injt/h,injection_error_bound=injection_error,recipient_count=int(target.sum()),reference_l2=err,cost_error_l2=costerr,cost_error_rms=costerr/np.sqrt(n),cost_error_top_recipients=np.abs(D-Dt)[T].sum()/h,cost_error_initial_recipients=np.abs(D-Dt)[U].sum()/h,projection_cost_error_l2=np.linalg.norm(D-Dproj),initial_tail=R['cap'](D-b,h)[0],initial_ref_tail=R['cap'](Dt-b,h)[0],repair_tail=R['cap'](rr,h)[0],repair_ref_tail=R['cap'](rt,h)[0],repair_error_recipients=np.abs(rr-rt)[T].sum()/h,tail_l2_bound=(1+alpha*4)*costerr/np.sqrt(h),complement_bound=2*s*np.sqrt(n)/(1-s*s)*err)
                    # same affine mean isolates D replacement; no artificial reference budget
                    if costerr>row['complement_bound']+1e-8 or abs(row['repair_tail']-row['repair_ref_tail'])>row['tail_l2_bound']+1e-8:raise RuntimeError(row)
                    if ell and side==1:
                        I=np.arange(n)%(ell-1)==0
                        row.update(subfield_initial=float(D[I].mean()),subfield_ref=float(Dt[I].mean()))
                    else:row.update(subfield_initial='',subfield_ref='')
                    if writer is None:writer=csv.DictWriter(sys.stdout,row.keys());writer.writeheader()
                    writer.writerow(row)
                sys.stdout.flush()
            if t<128:
                total=np.abs(v);total[0]=np.hypot(v[0],2);v=d*kernel_action(sign,total)
if __name__=='__main__':main()
