"""Actual reciprocal supports: moving-width raw rescaling and pinned descent.
All numbers are floating-point diagnostics; the accompanying note proves bounds.
"""
import json
import sys
import runpy
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
A = runpy.run_path(str(ROOT/'anchored-repair-20.py'))
from quadratic_theta import damped_trials
from theta import paley_sign
from square_control import square_field_sign

for q, root in [(401,None),(9413,None),(37253,None),(97**2,97),(193**2,193)]:
    sign = paley_sign(q) if root is None else square_field_sign(root)
    n = len(sign)
    widths = [C/np.sqrt(n) for C in [4.,1.,.25]]
    for r, _, plus, minus, residual in damped_trials(sign,widths,1e-12,64):
        for side,x,y in [(1,plus,minus),(-1,minus,plus)]:
            project,L,pad,kappa,col,_ = A['anchored_tools'](sign,side)
            H = y.mean()+project(y)
            c = np.sqrt(n)*y.mean()
            ar = H[0]
            # A sufficient sign margin for a true zero y_i follows from
            # ||z-z*||_2 <= residual/(1-(1-r)/(1+r)).
            error = residual*(1+r)/(2*r)
            zeros = (x > 2*error)
            zeros[0] = False
            for a in [.98,1.]:
                t = a/ar
                row = t*np.sqrt(n)*H+(1-t*c)*pad
                defect = np.linalg.norm(np.minimum(row[1:],0))
                floor = (t*c-1)*pad[zeros]-t*r*c/(1+r)
                support_lower = np.linalg.norm(np.maximum(floor,0))
                assert support_lower <= defect+1e-7
                assert abs(row[0]/np.sqrt(n)-a)<1e-10
                assert abs(row.mean()-1)<1e-10
                initial=defect
                for _ in range(512):
                    e=np.maximum(-row,0);e[0]=0
                    row += 1.9*L(e)
                final=np.linalg.norm(np.minimum(row[1:],0))
                m=y[0]**2
                upper=(np.sqrt(n*r/(1-r)) if m>=r+(1-r)*a*a else None)
                if upper is not None:
                    # Descent is an upper trial; it need not reach this
                    # theoretically guaranteed minimum in finite steps.
                    pass
                square_lower=max(a*np.sqrt(n)-(root+1)/2,0)/np.sqrt((root-1)/2) if root and side==1 else 0
                assert final >= square_lower-1e-7
                print(json.dumps(dict(q=q,side=side,C=r*np.sqrt(n),r=r,a=a,c=c,
                    raw_mark=ar,free_mark=ar/c,M=m,residual=residual,zero_count=int(zeros.sum()),
                    raw_defect=initial,support_lower=support_lower,descent_defect=final,
                    square_lower=square_lower,scalar_bound=upper,
                    raw_scaled=initial/n**.25,descent_scaled=final/n**.25)),flush=True)
