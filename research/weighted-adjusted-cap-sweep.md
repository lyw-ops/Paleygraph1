# A prime-sample sweep of the stationary-weighted adjusted overshoot

Use the physical weights \(t_i=t\) in the bulk and \(t_0=n=(p-1)/2\). For each sampled prime, the calculation solves the actual capped equation \(U=K\Phi_t(C_M(U))\) and the true stationary equation \(Y=K\Phi_t(Y)\) by floating-point iteration. It then evaluates the two sides of [Round 117, equation (2)](weighted-adjusted-cap-117.md) with \(f_\epsilon=(\Phi_t(Y)+\epsilon Y)/2\) and means over all \(n\) coordinates. The sweep records the contribution \(W_\epsilon/(d_\epsilon-\ell_\epsilon)\), where

\[
 W_\epsilon=\mathbb E_n(f_\epsilon S_\epsilon),\qquad
 S_\epsilon=(\epsilon KT_\epsilon-(a-\epsilon U)_+)_+,\qquad
 T_\epsilon=(a-\epsilon U)_-,\qquad a=\Phi_t(C_M(U)).
\]

The code checks the capped mean identity, both stationary means, the opposite-sector pairing and the finite marked bound. The capped residual divided by one minus the global contraction factor gives a max-norm error estimate, evaluated in floating point. At \(p=401,t=0.002,M=3\), a separate dense cosine-sum matrix and two dense fixed-point iterations give normalized excesses \(0.0579566113025\) and \(0.0649067433241\), both within \(2\times10^{-12}\) of the FFT computation. The sweep is a numerical diagnostic.

## Sample results

The [112 signed rows](weighted-adjusted-cap-sweep.jsonl) use previously studied primes. The \(M=10\) sweep covers nine primes at all four floors, with \(1000033\) and \(7340033\) added at the two warmer floors. Both signs have zero spill and zero adjusted overshoot at every measured \((p,t)\). The largest computed amplitude is \(8.293828\) at \((7340033,0.01)\). Subtracting the floating-point residual-based error estimates leaves a minimum distance of \(1.7061716\) from the cap over these samples. Eight bulk peaks in the sweep agree with the earlier [smoothing data](../data/smoothing-norms.csv) to within \(3.0\times10^{-8}\).

The \(M=6\) stress test uses the same four primes at every floor. The last two columns give the sample maximum of \(W_\epsilon/(d_\epsilon-\ell_\epsilon)\) for each sign.

| \(t\) | \(M=10\) prime count | \(M=10\) largest \(\|U\|_\infty\) | \(M=6\), \(+\) | \(M=6\), \(-\) |
| ---: | ---: | ---: | ---: | ---: |
| 0.05 | 11 | 7.981896 | \(1.4630\times10^{-4}\) | \(5.0443\times10^{-5}\) |
| 0.01 | 11 | 8.293828 | \(2.1892\times10^{-3}\) | \(2.2235\times10^{-3}\) |
| 0.002 | 9 | 7.939101 | \(3.8877\times10^{-3}\) | \(4.0305\times10^{-3}\) |
| 0.0005 | 9 | 7.994081 | \(4.3718\times10^{-3}\) | \(4.4744\times10^{-3}\) |

The larger sign varies by prime. At \(t=0.0005\), both signwise maxima occur at \(p=151337\), where about 90 percent of the stationary-weighted positive transport survives subtraction of the actual slack. The stress test exercises both signs and the active branch. The \(M=10\) zeros leave the through-primes behavior of that branch undetermined and the samples do not identify a power of \(t\).

## Replay

Run the following with the repository's NumPy and SciPy dependencies. Output is JSON Lines, with residuals, support sizes, the weighted positive transport before subtracting slack, and the two terms in the marked denominator. The saved runs include a tighter initial stationary tolerance and a cold-point retry at the current tolerance. Check agreement at numerical precision.

```sh
.venv/bin/python -B research/weighted-adjusted-cap-sweep.py 13 401 9413 10009 37253 50021 151337 153649 200009
.venv/bin/python -B research/weighted-adjusted-cap-sweep.py 1000033 7340033 --floors 0.05 0.01
.venv/bin/python -B research/weighted-adjusted-cap-sweep.py 9413 37253 151337 200009 --caps 6
```

## Reduction for the double limit

At the stipulated positive marked denominator, \(S_{\epsilon,0}=0\). On the bulk, \(0\le f_\epsilon-(\epsilon Y)_+\le\sqrt t\) by the radical formula. Also \(S_\epsilon\le(\epsilon KT_\epsilon)_+\). The transported row has mean zero, \(K\) contracts the normalized second norm, and \(T_\epsilon^2\le (U^2-M^2)_+\) coordinatewise. Consequently

\[
 \mathbb E_n S_\epsilon\le\tfrac12\|KT_\epsilon\|_{1,n}
 \le\tfrac12\sqrt\alpha\le 1,\qquad
 0\le W_\epsilon-\mathbb E_n[(\epsilon Y)_+S_\epsilon]\le\sqrt t.
\]

This uses the actual cap-defect budget \(\alpha\le4(1-t/n)\) and requires no decay rate in \(p\). For \(M=10\), [Round 108](projected-cap-completion-108.md) gives \(\liminf_p(d_\epsilon-\ell_\epsilon)\ge 2-2\sqrt2/10\) at each fixed \(t\). Thus the remaining sufficient target is

\[
 \lim_{t\downarrow0}\limsup_{p\to\infty}\max_{\epsilon=\pm1}
 \mathbb E_n[(\epsilon Y)_+ (\epsilon KT_\epsilon-(a-\epsilon U)_+)_+]=0,
\]

where a sequence of fixed positive floors tending to zero suffices. A quantitative target is an upper bounded by \(C\sqrt t\) after taking the prime limsup. The easy \(\sqrt t\) contribution is proved by the decomposition above. The same power for the aligned term is a possible proof target.
