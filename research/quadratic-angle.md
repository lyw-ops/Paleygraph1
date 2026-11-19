# Directional energy bounds from a reference gradient

The [capped gradient certificate](quadratic-gap.md) transports a feasible trial at a reference width $s$ to a target $r\le s$. That estimate first lower-bounds the target value, then divides its upper sector norm by the lower value. A direction-based argument instead bounds the normalized sector energy in one step. It also bounds the signed width derivative using the same single reference trial. The resulting bound is defined for every width ratio. This relaxation loses information when $s^2/r$ becomes large.

## Two inner products determine an angular constraint

Fix the sign $\sigma$ and write $Q_t=J+tP+t^{-1}N$ for the [quadratic metric](quadratic-theta.md), with $P=P_\sigma$ and $N=P_{-\sigma}$. Let $b_*$ be the nonnegative anchored minimizer at $r$, with value $M=b_*^TQ_rb_*$. Take a trial $b_0=1$, $0\le b\le1$ and use the same [capped mass set and linear deficit](quadratic-gap.md#a-capped-gradient-split). In particular, $b_*$ lies in the mass set using $U=b^TQ_rb$.

Let $D_s$ be an upper bound on $D(Q_s b)$ over that target mass set and set $c_s=b^TQ_s b-D_s$. Define

$$
B=Q_r^{1/2}b,\qquad V=Q_r^{-1/2}Q_s b,\qquad
u=Q_r^{1/2}b_*,\qquad v=u/\|u\|.
$$

First-order optimality at $b_*$ along $b-b_*$ and the reference deficit give

$$\langle B,u\rangle\ge\|u\|^2,\qquad \langle V,u\rangle\ge c_s.$$

For $c_s>0$ the two inner products are positive and

$$\langle B,v\rangle\langle V,v\rangle\ge c_s.\tag{1}$$

Write $a=(\|JB\|,\|PB\|,\|NB\|)$ and $h=(\|JV\|,\|PV\|,\|NV\|)=(a_0,(s/r)a_+, (r/s)a_-)$. With $z=(\|Jv\|,\|Pv\|,\|Nv\|)$ and $H=(ah^T+ha^T)/2$, the two Cauchy–Schwarz inequalities imply

$$ z\ge0,\quad \|z\|=1,\quad z^THz\ge c_s. \tag{2} $$

These are exactly the directions permitted by the two inner product inequalities when only the three sector lengths are retained. For nonzero reference components one can align with $B$ in each sector to attain both upper inner products simultaneously. Then choose $\|u\|$ between $c_s/(h^Tz)$ and $a^Tz$. A sector with zero reference component may be arbitrary, with a sector of dimension zero excluded if exact equivalence is desired. In particular, any diagonal matrix $W$ with the energy or derivative coefficients yields, for all $\lambda\ge0$,

$$ z^TWz\le\lambda_{\max}(W+\lambda H)-\lambda c_s.\tag{3} $$

Here the allowed energy is $z_+^2/r$. By reciprocal complementarity, $z_-^2/r$ is the opposite allowed energy, since $Nb_*=rNQ_rb_*$. Thus $d\log M_\sigma/d\log r=z_+^2-z_-^2$. This gives its two-sided enclosure from $(0,1,-1)$ and $(0,-1,1)$. If the available $c_s$ is nonpositive, $\lambda=0$ always gives the trivial bounds.

The infimum of (3) equals the exact optimum of the three-coordinate relaxation. To see this, lift to $Z\succeq0$, $\mathrm{tr}Z=1$, $\mathrm{tr}(HZ)\ge c_s$. Each extreme point has rank one. If its rank were $k\ge2$, the symmetric matrices supported on its image would have dimension $k(k+1)/2\ge3$, admitting a nonzero perturbation preserving both trace constraints. Sufficiently small perturbations in both directions preserve positive semidefiniteness. For rank one we can replace the three coordinates by their absolute values since $H$ is entrywise nonnegative and $W$ is diagonal. For $c_s<\lambda_{\max}(H)$ the concave, nonincreasing optimum as a function of the threshold $c_s$ has a supporting line with slope $-\lambda\le0$. Maximizing the resulting linear inequality over all trace-one positive semidefinite matrices gives equality with (3) at this $\lambda$. At the top threshold the infimum as $\lambda\to\infty$ gives equality by compactness. This exactness concerns the two-constraint relaxation. The original optimizer also has a fixed anchor and coordinatewise optimality conditions.

The eigenvalue upper bound can be enclosed without an interval eigensolver. For any positive numerical vector $w$, the largest eigenvalue of $F=W+\lambda H$ is at most $\max_i(Fw)_i/w_i$. Indeed $F$ has nonnegative off-diagonal entries, and after adding a scalar multiple of the identity, diagonal conjugation reduces the bound to the maximum row sum of a nonnegative matrix. The optional interval replay uses an approximate multiplier and approximate positive vector from a numerical minimization, then evaluates this inequality using Arb. The projection norms come from the reference trial only. The target solve in the comparison is floating point and supplies neither of these inputs.

## What happens at a long width ratio

The reference direction $z=h/\|h\|$ is always feasible in (2), since its product is $a^Th=b^TQ_s b\ge c_s$. Set $m=\|Jb\|$, $b_P=\|Pb\|$ and $b_N=\|Nb\|$. Substituting this direction gives a lower bound on the **best upper bound within the relaxation**.

$$
\frac1r\frac{(s^2/r)b_P^2}{m^2+(s^2/r)b_P^2+(r/s^2)b_N^2}. \tag{4}
$$

Thus for trials with $m,b_P\asymp1$ and $b_N=O(s)$ the best upper bound grows at least as fast as $(s/r)^2$ when $s^2/r$ is small. When $s^2/r\to\infty$ the relaxation is asymptotic to the trivial $1/r$ upper bound. Even exact optimization of the multiplier leaves this obstruction.

The long-ratio failure can persist with a prescribed positive target value. Assume also $b_N\gtrsim s$ and $c_s=O(1)$. Given any fixed proposed target norm $t>0$, set $\varepsilon=t\sqrt r/b_N$ and $z=(0,\sqrt{1-\varepsilon^2},\varepsilon)$. If $s^2/r\to\infty$ then $\varepsilon=o(1)$, $a^Tz\ge t$, and $h^Tz\ge (s/\sqrt r)b_P\sqrt{1-\varepsilon^2}\to\infty$. Choosing $\|u\|=t$ satisfies both relaxed inner product inequalities while the allowed energy still tends to $1/r$ in ratio. The direction argument uses only sector lengths and two inner products. Additional conditions involving individual coordinates or the anchor can exclude these directions.

## Interval comparison

The [92 interval rows](../data/quadratic-angle.csv) cover both signs at six primes through $153649$ and six prime squares through $389^2$. They use $r$ near $q^{-1/3}$ and reference widths $1.02r$, $1.5r$, $4r$, and $0.5$ where those widths lie in $[r,1]$. The interval statements use the exact binary rational widths in the script. The older unscaled split returns a positive lower value bound in 74 rows. The new certified energy bound improves the older floating-point split value in all 74 and gives a bound in the remaining 18. Sixteen certified derivative intervals exclude zero.

| Order and sign | Reference width | Numerical target energy | Previous split upper estimate | Directional interval upper bound |
|---|---:|---:|---:|---:|
| $401,+$ | $1.02r$ | 1.55217 | 1.63171 | 1.61300 |
| $9413,+$ | $4r$ | 2.31434 | 127.43531 | 16.86419 |
| $153649,+$ | $1.5r$ | 2.59969 | 7.40065 | 6.27634 |
| $153649,+$ | $0.5$ | 2.59969 |  | 53.45276 |
| $389^2,+$ | $1.5r$ | 3.79479 | 8.69022 | 7.41099 |

The last fixed-reference comparison at $153649$ has $1/r\approx53.56$, consistent with the loss in (4). The nearby square gives the same qualitative pattern. Successful finite-width transport by this method leaves the $o(\log_2^*p)$ estimate of [round 14](parallel-complexity-14.md#4-consequence-at-the-intermediate-width) open.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_angle.py 61 401 1997 9413 37253 153649 --square-characteristics 7 19 43 97 193 389 --width-factors 1.02 1.5 4 --reference-widths .5 --certify-max-order 153649
```
