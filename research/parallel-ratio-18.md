# Optimizing the endpoint ratio of a translated repair

The [four-step repair](parallel-repair-17.md) finishes an affine projection by minimizing the mean of a positive Fourier correction. The endpoint estimate depends on both the mean and the marked coordinate. Optimizing them together gives a weighted residual estimate in which the leftover marked-coordinate defect has zero price at the current kernel ratio. A feasible repaired row can also serve as the kernel for another finish.

## Exact ratio and weighted threshold

Use scaled coordinates $X=\sqrt n H$, where $H$ is the projected opposite spectrum at reference width $s$, and $\overline X=c$. The projection shadow $A$ has mean $b$ and belongs to the same Fourier space as $H$. Pick a floor $F$ with $F_0=0$ and $F_i\ge-X_i$ off the mark. The positive floor is $F_i=(-X_i)_+$ and the signed floor is $F_i=-X_i$ off the mark. In both cases a correction $G\ge F$ in the same Fourier space gives a nonnegative final row with a positive mark, since $X_0>0$.

Let $R$ be a nonnegative kernel in the opposite Fourier space, normalized by $R_0=\max_i R_i=1$. Write $h=1/\overline R$ and $\rho=h/\sqrt n$. For any threshold $t$ put

$$u_i(t)=(F_i-A_i-t)_+,\qquad G(t)=A+t\mathbf1+R*u(t),\qquad Y(t)=X+G(t).$$

Each translate of $R$ is nonnegative, and its unshifted coefficient at the origin is one. This gives $G(t)\ge F$ directly. The normalized endpoint lower bound supplied by this row is $Y_0(t)/(\sqrt n\,\overline{Y(t)})$. For any proposed lower bound $\tau\ge\rho$ its numerator after subtracting the required mean contribution is

$$
Y_0(t)-\tau\sqrt n\,\overline{Y(t)}
=X_0+A_0-\tau\sqrt n(c+b)
 -(\tau\sqrt n-1)t-\sum_i(\tau/\rho-R_{-i})u_i(t).\tag{1}
$$

The weights $w_i=\tau/\rho-R_{-i}$ are nonnegative. Minimizing the last two costs over $t\in\mathbb R$ is exactly

$$\sup_{0\le v_i\le w_i,\ \sum_i v_i=\tau\sqrt n-1}\sum_i v_i(F_i-A_i).\tag{2}$$

This follows by filling the per-coordinate capacities in decreasing order of the signed residual. The capacity is feasible since $\sum_i w_i=(n/h)(\tau\sqrt n-1)$ and $h\le n$. At the base ratio $\tau=\rho$, the weight at the mark is zero. Thus the test for a strict improvement over this kernel uses only the weighted **bulk** tail and the starting margin $X_0+A_0-h(c+b)$. The marked value $A_0$ in this starting margin is still needed. For a target above the current ratio, the coefficient of the remaining marked violation is exactly $\tau/\rho-1$.

The ordinary ratio $Y_0(t)/(\sqrt n\,\overline{Y(t)})$ is a quotient of affine functions on each interval between two consecutive residual values. Its denominator is positive, so it is monotone or constant on each such interval. When $h<n$, its limits at both ends of the real axis are $1/\sqrt n$. When $h=n$, the left tail is constant. Hence every best bound above the constant-row value is attained at a residual breakpoint. One sort and three prefix sums evaluate all these ratios.

The construction spends $u_0(t)$ at the root even if some of the other translates have already filled its constraint. One can remove the smaller of $u_0(t)$ and the slack $G_0(t)-F_0$ from that coefficient. At every other coordinate the self-translate still ensures feasibility. Removing that much of $R$ leaves (1) invariant at $\tau=\rho$. It increases the final ratio if the row initially had ratio greater than $\rho$. The replay chooses the best ordinary breakpoint first and trims the root coefficient there when this can help. This last operation does not optimize the threshold again in the larger family with trimming.

A previously feasible row can be translated to its peak and averaged with its inverse as a new even kernel. Both operations preserve the sector and mean, and the average preserves the selected peak, so rescaling makes its marked entry one. The replay reuses the highest numerical candidate and interval-certifies the selected rows. Selecting new kernels this way has no general uniform iteration count guarantee.

## Solve for the kernel at a fixed threshold

Fix $t$ and put $V=X+A+t\mathbf1$, $v=\overline V$. Take $u_i=(F_i-A_i-t)_+$ for $i\ne0$ and $u_0=0$. More generally we only need $u\ge0$, $u_0=0$ and $V_i+u_i\ge0$ for $i\ne0$. Write $U=\sum_i u_i$ and $C_uY=u*Y$. If $v>0$, a proposed normalized lower bound $\tau>0$ determines

$$Q=U+\tau\sqrt n\,v,\qquad Y(Q)=(QI-C_u)^{-1}V.\tag{3}$$

This inverse preserves the Fourier sector and $\overline{Y(Q)}=v/(Q-U)$. If $Y_0(Q)\ge1$ then every entry is nonnegative. Indeed, a negative minimum $\gamma$ would occur off the mark, at $i$ say. There

$$Q\gamma\ge V_i+u_iY_0(Q)+(U-u_i)\gamma\ge(U-u_i)\gamma,$$

contrary to $Q>U$. Thus the scalar test $Y_0(Q)\ge1$ certifies the ordinary normalized endpoint bound $\tau Y_0(Q)\ge\tau$. The test imposes no marked constraint on $V$ or on its correction from $X$. In the inversion-even case it uses only a real Fourier sum,

$$Y_0(Q)=\frac1n\sum_{j=0}^{n-1}\frac{\widehat V_j}{\tau\sqrt n\,v+U-\widehat u_j}.\tag{4}$$

At a root $Y_0(Q)=1$, the row is its own normalized convolution kernel: $QY=V+u*Y$. If the support of $u$ generates the cyclic group, this root exists since the constant eigenvalue $U$ is simple, $Y_0(Q)\to+\infty$ as $Q\downarrow U$ and $Y_0(Q)\to0$ as $Q\to\infty$. The proof also works when the support generates a proper subgroup with positive mean of $V$ on the coset containing the mark.

The criterion has a monotone form with exclusively nonnegative feedback terms. Let $B$ be the off-mark principal block of $C_u$, $W=V+u$, $K_Q=(QI-C_u)^{-1}e_0$, and let $\perp$ mean restriction to the off-mark coordinates. Prescribe $Z_0=1$ and $Z_\perp=(QI-B)^{-1}W_\perp$. Then $(QI-C_u)Z=V+\chi(Q)e_0$, where

$$\chi(Q)=Q-V_0-\sum_{k\ge0}\frac{\langle(u_{-i})_{i\ne0},B^kW_\perp\rangle}{Q^{k+1}}.\tag{5}$$

Since $1=Y_0(Q)+\chi(Q)K_Q(0)$ and $K_Q(0)>0$, the test (4) is equivalent to $\chi(Q)\le0$. The sum converges and is nonnegative and decreasing in $Q>U$. Hence $\chi$ is strictly increasing, the root when it exists is unique, and keeping any initial segment of the sum gives a sufficient test. With the signed floor, $W_i=(V_i)_+$ off the mark. For even $V,u$ the $k=0$ coefficient is then zero and the $k=1$ coefficient is $\sum_{i\ne0}(u*u)_i(V_i)_+$. This term tests whether a two-step sum of defects reaches the positive portion of the row. If all defects lie in a subgroup and the off-mark $W$ vanishes there, every coefficient is zero. Conversely the entire feedback is at most $U\|W_\perp\|_\infty/(Q-U)$, by bounding each power by the off-mark row-sum bound $U$. Thus when $U=O(\sqrt n)$, $v$ and $\tau$ are bounded below, and $\|W_\perp\|_\infty=o(\sqrt n)$, the feedback can change the scalar margin by at most $o(\sqrt n)$.

## Square upper bound and a field-first criterion

On the plus side at square order, the subfield spectrum gives $Y_0\le (\sqrt q+1)\overline Y/2$ for each nonnegative opposite-sector row $Y$. This follows by summing $Y$ on the square annihilator coset, immediately from orthogonality and positivity. The resulting ceiling $(\sqrt q+1)/(2\sqrt n)$ applies to every kernel and every finish. When a kernel already attains this ratio, (1) cannot give a positive margin at its base ratio.

At prime order one may try target ratios tending to one and take $s$ small after the field limit. Formula (2) isolates the tail quantity to bound at an actual affine shadow. A positive lower bound on the scaled margin divided by $\sqrt n$ certifies a quantitative gain when the completed mean stays bounded. The exact root cancellation removes one obstacle to controlling this expression. The bulk residual estimate at a sequence of targets approaching one remains to be proved.

## Reproducible comparison

The [translated-repair replay](parallel-ratio-18.py) starts from the same affine mean $3(1-c)/4$ and four clipped projections as the previous positive repair. It also runs the same update with the signed floor. It compares the mean-minimizing threshold with three ratio finishes with kernel reuse. The [288 numerical candidates](parallel-ratio-18.csv) yield [134 interval rows](parallel-ratio-18-certified.jsonl) by certifying the mean-minimizing finish and the best numerical candidate at each setting. Interval verification rounds each selected correction in its Fourier sector and covers the error to the actual reference solve with a rational constant when needed. Certified widths use the exact binary rationals in the corresponding run.

The [resolvent replay](resolvent-repair-18.py) uses the same shadows and tries zero and all distinct thresholds from the translated candidates. All 260 scalar solves returned a numerical root. At each order, width and sign it selects the best numerical resolvent across both floors, then rounds and interval-checks its Fourier row directly. This yields [36 exact rational theta lower bounds](resolvent-repair-18-certified.jsonl). The path to each candidate uses a numerical reference solve, but its final certificate only requires a nonnegative spectrum in the specified Fourier sector. On the side $\sigma=-$, that sector supplies the lower bound on $\vartheta(\overline H)/\sqrt n$.

| Order and sign | Width | Minimum-mean finish | Best translated finish | Best resolvent |
|---|---:|---:|---:|---:|
| $1000033,+$ | $1/16$ | $0.94563799$ | $0.94714586$ | $0.94714591$ |
| $1000033,-$ | $1/16$ | $0.94753762$ | $0.94898763$ | $0.94898767$ |
| $1000033,-$ | $p^{-1/4}$ | $0.97099780$ | $0.97198247$ | $0.97198248$ |
| $389^2,+$ | $1/16$ | $0.70892686$ | $0.70892686$ | $0.70892687$ |

These are normalized certified lowers, rounded down for display. The translated finishes improve the certified bound by more than $10^{-9}$ in 56 of 72 settings, including all 40 prime settings. The resolvent increases the translated bound by more than $10^{-9}$ in 31 of its 36 settings. The largest additional increase is about $5.38\cdot 10^{-7}$, on the minus side of order $19^2$. Thus for the thresholds tried, the scalar solve explains and slightly improves the reused kernel without materially changing the finite bounds. A separate dense replay of (5) checked it against the full inverse on 90 even test systems.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-ratio-18.py --primes 401 9413 37253 153649 1000033 \
  > research/parallel-ratio-18.csv
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-ratio-18.py --primes 401 9413 37253 153649 1000033 \
  --certify-max-order 1000033 > research/parallel-ratio-18-certified.jsonl
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/resolvent-repair-18.py --certify-max-order 1000033 \
  > research/resolvent-repair-18-certified.jsonl
```

The [bulk-tail analysis](parallel-tail-18.md) breaks the missing prime estimate into the starting load, peak transfer and new excess from the background. The [low-layer analysis](astra-low-layer-18.md) rules out a separate shortcut based on small discarded energy alone. A uniform prime estimate for (4) or (5) at target ratios approaching one remains open.
