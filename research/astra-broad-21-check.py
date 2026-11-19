"""Normalization checks for the Round 21 inequalities; not certificates."""
from pathlib import Path
import runpy
import sys
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from quadratic_theta import damped_trials
from theta import paley_sign, optimize
from square_control import square_field_sign

anchored_tools = runpy.run_path(str(ROOT / 'research/anchored-repair-20.py'))['anchored_tools']

def check(q, sign):
    n = len(sign)
    s = 1 / 16
    _, _, plus, minus, residual = next(damped_trials(sign, [s], tolerance=1e-13, rounds=80))
    for side, x, y in [(1, plus, minus), (-1, minus, plus)]:
        P, _, M, _, _, _ = anchored_tools(sign, side)
        c = y.sum() / np.sqrt(n)
        H = y.mean() + P(y)
        row = np.sqrt(n) * H + (1-c)*M
        X, V = np.sqrt(n)*x, np.sqrt(n)*y
        A = s/(1-s*s)
        b = s*c/(1+s)+(1-c)*M
        error = np.max(np.abs(-row[1:]-(A*X-V/(1-s*s)-b)[1:]))
        _, spectrum = optimize(sign, side)
        W = spectrum/spectrum[0]
        assert W.min() > -1e-10 and W.max() < 1+1e-10
        S, B = W.sum(), W[1:]@W[1:]
        k = np.fft.fft(sign).real/np.sqrt(q)
        delta1 = (W@(1-side*k))/S
        delta2 = ((W*W)@(1-side*k))/(1+B)
        root_error = abs(delta1-(1+1/np.sqrt(q)-n/(np.sqrt(q)*S)))
        assert root_error < 1e-10
        assert delta2 <= S*delta1/(1+B)+1e-10
        m = (S-1)**2/B
        signed_dual = (row[0]-S)/np.sqrt(B)
        pair_error = abs(signed_dual + W[1:]@row[1:]/np.sqrt(B))
        margins = []
        for t in np.linspace(0, 2*b[1:].min()/A, 17):
            beta = b[1:].min()-A*t
            rhs = A*np.linalg.norm(np.maximum(X[1:]-t, 0))-beta*np.sqrt(m)
            margins.append(rhs-signed_dual)
        assert error < 1e-9 and pair_error < 1e-8 and min(margins)>-1e-8
        print(json.dumps(dict(q=q, side=side, reference_residual=float(residual),
              identity_error=float(error), pairing_error=float(pair_error),
              rooted_identity_error=float(root_error),
              min_bound_margin=float(min(margins)), signed_dual=float(signed_dual))))

for q in (101, 401):
    check(q, paley_sign(q))
for r in (7, 19):
    check(r*r, square_field_sign(r))
    # In the cyclic Q coordinates the subfield group has order r-1.
    n=(r*r-1)//2
    g=np.zeros(n)
    g[np.arange(r-1)*(r+1)//2]=1
    g[0]=0
    corr=np.fft.ifft(np.abs(np.fft.fft(g))**2).real
    indices=np.arange(1,r-1)*(r+1)//2
    assert np.max(np.abs(corr[indices]-(r-3))) < 1e-10
    assert abs(corr[0]-(r-2)) < 1e-10
    t=(r-3)/2
    rich=t*t*np.count_nonzero(corr[1:]>t)/(r-2)**2
    assert abs(rich-(r-3)**2/(4*(r-2))) < 1e-10
    print(json.dumps(dict(square_root=r, rich_lower=float(rich))))
