"""Find an upper-half-disk Loewner obstruction from finitely many real stationary jets."""
from fractions import Fraction as Q
import argparse
import json
from pathlib import Path
import runpy
import numpy as np
from flint import arb
lib=runpy.run_path(str(Path(__file__).with_name("astra-strip-45-check.py")))
rat=lib["rat"]
def certificate(p,square):
    sign=lib["square_field_sign"](p) if square else lib["paley_sign"](p)
    n=len(sign)
    grid=[Q(1,32)*Q(5,4)**i for i in range(30)]
    data=[]
    for x in grid:
        jet,_,_,_,m=lib["disks"](sign,x,Q(1,16),9,20 if square else 8)
        c=rat(Q(n-1,n)); t=rat(x); W=1+c*t
        data.append([(W.log()/2+side*m,c/(2*W)-side*jet.first_center/t) for side in (1,-1)])
    for r in map(Q,["1/2","3/5","2/3","3/4","4/5","17/20","9/10","19/20"]):
        for center in grid:
            if center*(1-r)/(1+r)<Q(1,32) or center*(1+r)/(1-r)>2048:
                continue
            ids=[i for i,x in enumerate(grid) if abs((x-center)/(x+center))<r*Q(9,10)]
            if len(ids)<3:
                continue
            us=[]; dus=[]
            for i in ids:
                x=grid[i]
                z=(x-center)/(x+center)/r
                us.append(rat(((1+z)/(1-z))**2))
                dus.append(rat(4*(1+z)/(1-z)**3*2*center/(x+center)**2/r))
            for j,side in enumerate((1,-1)):
                f=[data[i][j][0] for i in ids]
                diag=[data[i][j][1]/dv for i,dv in zip(ids,dus)]
                mat=[[diag[k] if k==l else (f[k]-f[l])/(us[k]-us[l]) for l in range(len(ids))] for k in range(len(ids))]
                M=np.array([[float(v) for v in row] for row in mat])
                scale=np.sqrt(np.abs(M.diagonal()))
                _,ev=np.linalg.eigh(M/scale[:,None]/scale[None,:])
                weights=np.rint(ev[:,0]/scale*2**25).astype("int64").tolist()
                val=sum((wi*wj*mat[k][l] for k,wi in enumerate(weights) for l,wj in enumerate(weights)),arb(0))
                if val<0:
                    print(json.dumps(dict(kind="physical_sector_loewner_obstruction",order=2*n+1,side=side,radius=str(r),center=str(center),angle_upper=(2*rat(r).atan()).upper().str(12),grid_indices=ids,integer_weights=weights,quadratic_form=val.str(11)),sort_keys=True),flush=True)
                    return
    print(json.dumps(dict(kind="loewner_scan_inconclusive",order=2*n+1)),flush=True)
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--prime",type=int,required=True)
    p.add_argument("--square",action="store_true")
    args=p.parse_args()
    certificate(args.prime,args.square)
