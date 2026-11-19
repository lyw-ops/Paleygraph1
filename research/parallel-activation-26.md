# Actual-increment activation loss and two-step transfer out of the mark

Round 26, 2026-11-18. This gives a new deterministic two-step contraction
theorem, an explicit conditional route to the critical residual scale, and
prime/square actual-orbit diagnostics. **The prime-uniform weighted estimate
is not proved.** In particular, a bound in the fixed-depth limiting process
alone does not control the growing-depth exceptional mass.

The starting points are [the mixed-moment criterion](parallel-random-circulant-25.md),
[the scalar-space obstruction](scalar-seed-25.md), and
[the bounded exact-mark dynamics](astra-dynamics-24.md). The latter already
separates optimization error from the arithmetic existence of a good repair.
Here the directions are consecutive increments of the actual smoothing
orbit, not arbitrary directions and not a projection onto the scalar seed
space. No new endpoint theta bound through all primes is claimed.

## 1. Exact normalization and increment identities

Let `q=2n+1`, `K=K^T`, `K^2=I-J`, `J=11^T/n`. Use the full heterogeneous
activation, so the source at the mark is never silently replaced by its
limit:

\[
 V_t=\sqrt n\,v_t,\quad c_0=4n,\quad c_i=4\tau\ (i\ne0),\qquad
 V_{t+1}=K\Psi(V_t),\quad \Psi_i(x)=\sqrt{x_i^2+c_i},\quad V_0=0.
 \tag{1}
\]

Put `X=V_t`, `Y=V_{t+1}`, `D=Y-X`, and

\[
 u_i=\sqrt{X_i^2+c_i},\quad z_i=\sqrt{Y_i^2+c_i},\quad
 d_i=\frac{X_i+Y_i}{u_i+z_i},\quad H_i=d_iD_i.
\]

These definitions include `D_i=0`, with no division by the increment.
Exactly,

\[
 H=\Psi(Y)-\Psi(X),\qquad D_{t+1}=KH,
\]

\[
 \boxed{\ \|D_t\|^2-\|D_{t+1}\|^2
 =\sum_i(1-d_i^2)D_i^2+\frac{(\sum_i H_i)^2}{n}.\ }
 \tag{2}
\]

The last term is the **true mean reserve**, including the root contribution
to `sum H`; it need not be replaced by a bulk mean or dropped. On writing
`X_i=sqrt(c_i)sinh a_i`, `Y_i=sqrt(c_i)sinh b_i`, the coordinate loss is

\[
 D_i^2-H_i^2=2c_i[\cosh(b_i-a_i)-1]. \tag{3}
\]

Thus the root loss, after division by `n`, is exactly
`8[cosh(b_0-a_0)-1]`, at least `4(b_0-a_0)^2`. This retains the actual root,
including at depths depending on the field.

There is also a useful exact harmonic form. Set

\[
 Q_i=\frac{u_i z_i+X_iY_i+c_i}{2}\ge c_i.
\]

Rationalizing `u_i z_i-X_iY_i-c_i` gives

\[
 \boxed{\ 1-d_i^2=c_i/Q_i.\ } \tag{4}
\]

In particular it is the `D_i^2`-weighted harmonic mean of `Q_i`, not the
ordinary bulk RMS of `X`, which measures the loss. The inequality

\[
 Q_i\le c_i+(X_i^2+Y_i^2)/2
\]

recovers a moment bound, but (4) can be substantially sharper.

For the averaged orbit `V_{t+1}=(1-h)V_t+h K Psi(V_t)`, `0<h<=1`, consecutive
increments instead obey `D_{t+1}=(1-h)D_t+h KH`. The exact identity is

\[
 \|D_t\|^2-\|D_{t+1}\|^2
 =h\left[\sum_i(1-d_i^2)D_i^2+\frac{(\sum_iH_i)^2}{n}\right]
  +h(1-h)\|D_t-KH\|^2. \tag{5}
\]

All three terms are nonnegative. The two-step theorem below concerns the
unaveraged orbit (1); the averaged diagnostics also check (5).

### Independent integer check of the marked-to-bulk constants

For the actual Paley signs, `s(0)=0`, `s(a)^2=1` off zero and `sum s=-1`.
Consequently, without evaluating a numerical Fourier transform,

\[
 K_{00}=-1/n,\qquad
 \sum_i|K_{0i}|^2=\frac{\sum_a s(a)^2}{n}=\frac{n-1}{n},\qquad
 r_n^2:=\sum_{i\ne0}|K_{0i}|^2=1-1/n-1/n^2. \tag{6}
\]

The first equality uses the `1/n` Fourier convolution convention; the second
uses Parseval. The [integer audit](parallel-activation-26-integer.jsonl)
checks the sign counts and rational quantities independently at six prime
and four square orders. For example `q=61`, `n=30` gives `K_00=-1/30` and
`r_n^2=869/900`; `q=49`, `n=24` gives `-1/24` and `551/576`. At the smallest
prime `q=5`, `n=2`, the off-root squared row norm is `1/4`, not `1-1/n`.
Changing the sign of `K` only changes the sign of `K_00`, so every estimate
below applies to both masks.

The same integer/rational audit also checks the trace, determinant
`-rho/n^2`, and determinant of `I-B`, calling the smaller matrix in (14)
`B`, at four rational values of `rho` per field. The last determinant is exactly
`1-1/n^2+rho/n`, positive. This checks the marked-to-bulk matrix constants
independently of the floating trajectory code.

## 2. A one-step bound retaining both the root and the mean reserve

Let `B={i!=0}`, `E_t=||D_t||^2`, and suppose `||D_{t,B}||>0`. Define the
actual endpoint-weighted amplitude

\[
 A_t=\max\left\{
 \frac{\sum_B D_i^2X_i^2}{\sum_BD_i^2},
 \frac{\sum_B D_i^2Y_i^2}{\sum_BD_i^2}\right\}.
 \tag{7}
\]

The weighted second moment of `(1-s)X+sY` is convex in `s`, so (7) is
exactly its maximum on the segment. Weighted Cauchy--Schwarz, either using
(4) or integrating the derivative of `sqrt(x^2+4tau)`, gives

\[
 \|H_B\|^2\le\rho_t\|D_B\|^2,\qquad
 \rho_t=\frac{A_t}{A_t+4\tau}. \tag{8}
\]

If `D_B=0`, (8) is vacuous and any chosen `rho_t` in `[0,1)` works. Put

\[
 \beta_t=D_0^2/E_t,\quad
 m_t=\frac{(\sum_iH_i)^2}{nE_t},\quad a_t=d_0^2.
\]

Then the root- and mean-preserving rate is

\[
 \boxed{\quad E_{t+1}/E_t
 \le\rho_t(1-\beta_t)+a_t\beta_t-m_t.\quad} \tag{9}
\]

The exact equality has `sum_B H_i^2/E_t` in place of the first term.
In particular the root is not assigned the bulk smoothing weight `tau`.
No claim that `beta_t=o(1)` uniformly in depth is used.

### A weaker, directly testable small-ball condition

Let

\[
 F_t(R)=\frac{\sum_B D_i^2\mathbf1_{\max(|X_i|,|Y_i|)>R}}
                  {\sum_BD_i^2}.
\]

On the complementary set the activation derivative squared is at most
`R^2/(R^2+4tau)`. Thus (8) can instead use

\[
 \rho_t(R)=1-\frac{4\tau}{R^2+4\tau}[1-F_t(R)]. \tag{10}
\]

A positive, depth-uniform fraction of increment energy at bounded amplitude
therefore suffices. **A bounded weighted second moment is not necessary**:
the remaining small fraction can have an arbitrarily large contribution to
`A_t`. At `R=b sqrt(tau)`, a weighted small-ball mass at least
`c sqrt(tau)` gives a loss at least `4c sqrt(tau)/(b^2+4)`. This is a
deterministic actual-orbit criterion, not an assertion of such a small-ball
estimate for arithmetic fields.

The replay records separately the coordinate fraction above each cutoff,
the `D^2` energy fraction there, and

\[
 T_t(R)=\frac{\sum_BD_i^2\max(X_i^2,Y_i^2)
                       \mathbf1_{\max(|X_i|,|Y_i|)>R}}
                   {\sum_BD_i^2}. \tag{11}
\]

This prevents a small exceptional set with a large moment contribution from
being reported as harmless bulk behavior. `T_t(0)` is a conservative
amplitude envelope; (7) is the maximum of two weighted sums, rather than
the sum of coordinatewise maxima.

## 3. Two-step contraction without a root-amplitude hypothesis

**Theorem.** Suppose (8) holds with the same `0<=rho<1` at two consecutive
steps `t,t+1`. Let

\[
 k=1/n,\quad r^2=1-1/n-1/n^2,\quad
 b=k^2-\rho(1/n+k^2),\quad
 \lambda_n(\rho)=\frac{b+\sqrt{b^2+4\rho k^2}}2,
\]

\[
 \mathcal Q_n(\rho)=\rho+(1-\rho)\lambda_n(\rho).
\]

Then, putting `M_t=(sum H_t)^2/n` without normalization,

\[
 \boxed{\quad
 E_{t+2}\le\mathcal Q_n(\rho)E_t-\rho M_t-M_{t+1}.
 \quad} \tag{12}
\]

For every `n>=2`,

\[
 \lambda_n(\rho)\le n^{-2}+\sqrt\rho/n\le3/4,
 \qquad
 \mathcal Q_n(\rho)\le1-(1-\rho)/4<1. \tag{13}
\]

For large fields `Q_n(rho)=rho+O((1-rho)/n)`. Thus the field-limit rate
essentially costs **one bulk contraction every two iterations**. Root
saturation cannot by itself cause an arbitrarily slow source-generated
orbit under a uniform actual bulk contraction.

**Proof.** Write `H=(h_0,h_B)`, and `D'=KH`. From (9), with the next root
secant bounded by one,

\[
 E_{t+2}\le\rho E_{t+1}+(1-\rho)|D'_0|^2-M_{t+1}.
\]

Use `E_{t+1}=h_0^2+||h_B||^2-M_t`, and the exact row norm (6):

\[
 |D'_0|\le k|h_0|+r\|h_B\|,
 \qquad |h_0|\le|D_0|,\quad \|h_B\|\le\sqrt\rho\|D_B\|.
\]

The resulting quadratic upper bound, as a function of
`(|D_0|,||D_B||)`, has matrix

\[
 C=\rho I+(1-\rho)
 \begin{pmatrix}k^2&kr\sqrt\rho\\
                 kr\sqrt\rho&-\rho(1-r^2)\end{pmatrix}. \tag{14}
\]

The smaller matrix has trace `b` and determinant `-rho k^2`; hence its top
eigenvalue is exactly `lambda_n(rho)`. This proves (12). Its top eigenvalue
is at most `k^2+kr sqrt(rho)`, for example by the maximum row-sum bound
after increasing the negative diagonal to zero. This proves (13).
For `n>=3` it is also useful to keep

\[
 \mathcal Q_n(\rho)\le1-(1-2/n)(1-\rho). \tag{15}
\]

The off-root damping and the root-to-bulk transfer are both used in (14).
Replacing this argument by `||K||<=1` would leave the root undamped.

## 4. Quantitative depth, trial norm, mark, and the critical residual

The following bookkeeping is in the **unscaled** `v` norm used by the
residual certificate. Let `d_t=v_{t+1}-v_t`. Initially

\[
 \|d_0\|=2|1-\sqrt{\tau/n}|\sqrt{(n-1)/n}\le2
\]

when `n>=tau`, as eventually holds at a fixed floor. Put
`B_{q,j}=max(A_{q,2j},A_{q,2j+1})`,
`rho_{q,j}=B_{q,j}/(B_{q,j}+4tau)`, and

\[
 S_{q,J}=\sum_{j<J}-\log\mathcal Q_n(\rho_{q,j}).
\]

Nonexpansiveness makes the step norms nonincreasing. Iterating (12), while
optionally retaining its nonnegative mean-reserve improvement, gives

\[
 \boxed{\quad
 \|r_{2J}\|=\|d_{2J}\|\le2e^{-S_{q,J}/2},\qquad
 \|v_{2J}\|\le4\sum_{j<J}e^{-S_{q,j}/2}=:N_{q,J}.
 \quad} \tag{16}
\]

One may replace `Q_n(rho_j)` in this product by the sharper observed upper
factor `Q_n(rho_j)-(rho_j M_{2j}+M_{2j+1})/E_{2j}` whenever the increments
are nonzero. The two mean terms include the root throughout. Merely
observing such factors numerically is not a proof of their future rate.

The existing [smoothing certificate](smoothing.md) gives

\[
 \left|\log\frac{\theta_+}{\sqrt n}
       -\operatorname{arsinh}(v_{2J,0}/2)\right|
 \le\tfrac12\log W+
 \sqrt{(N_{q,J}+\sqrt W\,q^{1/4})\,2e^{-S_{q,J}/2}},
 \quad W=1+(n-1)\tau/n. \tag{17}
\]

Thus the explicit sufficient residual condition is

\[
 S_{q,J}-2\log(N_{q,J}+\sqrt W\,q^{1/4})\longrightarrow+\infty.
 \tag{18}
\]

When `N_{q,J}=O(1)`, or even `o(q^(1/4))`, this is
`S_{q,J} >= (1/2)log q+omega(1)`. It gives
`||r_{2J}||=o(q^(-1/4))`, with the square root in (17) accounted for.

### Bounded amplitude

If `A_{q,t}<=A` throughout the needed horizon, set `rho=A/(A+4tau)`.
Taking

\[
 T(q)=2\left\lceil
 \frac{(1/2+\epsilon)\log q}{-\log\mathcal Q_n(\rho)}
 \right\rceil \tag{19}
\]

gives residual at most `2q^(-1/4-epsilon/2)` and trial norm at most
`4/(1-sqrt(Q_n(rho)))`, uniformly bounded as `q->infinity`.
Asymptotically the depth is

\[
 T(q)\sim\frac{(1+2\epsilon)\log q}{\log(1+4\tau/A)}.
\]

For example `tau=.05`, `A=6` gives a coefficient about `30.50` multiplying
`(1+2epsilon)log q`. This is a conditional rate, not a certified bound
`A<=6`: the measured early amplitudes can exceed six.

### Amplitude growing sublinearly with depth

Suppose for fixed `tau` there are `C<infinity`, `0<=alpha<1`, independent of
the field, with

\[
 A_{q,t}\le C(t+1)^\alpha\qquad(0\le t\le T(q)). \tag{20}
\]

Using (15), for `n>=3` one has the explicit bound

\[
 S_{q,J}\ge(1-2/n)\frac{4\tau}{(C+4\tau)2^\alpha}
       \frac{(J+1)^{1-\alpha}-1}{1-\alpha}. \tag{21}
\]

Here `B_{q,j}<=C(2j+2)^alpha`, and
`sum_{k=1}^J k^(-alpha)>=((J+1)^(1-alpha)-1)/(1-alpha)`.
Thus a horizon

\[
 T(q)=O_{\tau,C,\alpha,\epsilon}
             ((\log q)^{1/(1-\alpha)}) \tag{22}
\]

can make the right side of (21) at least `(1/2+epsilon)log q`. The bound on
the trial norm in (16) is then uniform, because the scalar envelope is a
summable stretched exponential. More generally the needed envelope
condition is `sum_J exp(-S_J/2)<infinity`; sublinear power growth is one
sufficient example. A linear growth claim with an arbitrary constant is
not covered by this summability assertion.

### Why fixed-depth marked cancellation suffices *under (20)*

No quantitative arithmetic estimate out to the polylogarithmic depth is
needed once (20) is available uniformly on that whole horizon. Let `b_t`
be the summable, field-independent upper envelope for `||d_t||` obtained
from (21). For every fixed `L` and `T(q)>=L`,

\[
 |v_{T(q),0}|\le|v_{L,0}|+\sum_{t=L}^{T(q)-1}b_t
 \le|v_{L,0}|+\sum_{t\ge L}b_t. \tag{23}
\]

First send `q->infinity` through primes at this **fixed** `L`, using the
[fixed-depth parity input](iteration-parity.md); then send `L->infinity`.
The right side tends to zero. This preserves the field-first order and
proves the needed growing-depth marker vanishes. Combining (17)--(23) and
then sending fixed floors `tau->0` would prove Problem 26.

The exact additional input is therefore a bound such as (20), with the
same constants for every sufficiently large prime and **every depth up to
(22)**, or the corresponding weighted small-ball/product condition.
The prime threshold cannot be allowed to increase arbitrarily with depth.
A statement merely of the form `limsup_p A_{p,t}<=a_t` for each fixed `t`
does not provide (20). It allows a large exceptional increment at a depth
which escapes every fixed-depth test.

For a field-dependent amplitude envelope `A_{q,t}<=a_q`, (16)--(18) still
apply: typically `N=O(a_q/tau)` and the needed depth is of order
`(a_q/tau)log q` when `a_q=o(q^(1/4))`. But if `a_q->infinity`, the
summable field-independent tail used in (23) is no longer supplied by this
bound. One then needs, separately, `v_{T(q),0}=o(1)`, for example a genuine
depth-uniform marked arithmetic estimate. A polylogarithmic norm bound
alone does not prove that estimate.

## 5. Square-order obstruction and the order of limits

For `q=r^2`, the exact square theta is `theta_+=r-1`. At each fixed
`0<tau<1`, the stationary bracket implies

\[
 \liminf_{r\to\infty}\operatorname{arsinh}(v_0^*/2)
 \ge\tfrac12\log[2/(1+\tau)]>0. \tag{24}
\]

Nevertheless fixed-depth marked cancellation holds on square orders as
well; see [the square control](square-order-control.md).

**Consequence of the theorem and that fixed-depth input.** No uniform
bound (20) can hold across all sufficiently large square orders up to a
horizon (22) chosen with sufficient constant to satisfy (18). Otherwise
(23) and the same residual certificate would give a normalized square
theta tending to one after `tau->0`, and already contradict (24) at any
fixed `tau<1`. In particular, for every `C`, `alpha<1`, `tau in (0,1)` and
square-order cutoff, there is a larger square and a depth with
`A_{q,t}>C(t+1)^alpha`. This all-depth impossibility is a theorem, conditional
only on the inherited fixed-depth parity input; it is not inferred from
the finite plots.

Fixed-word limits do not distinguish the prime and square families in the
way needed here. Even a bounded `A_t` in a field-first limiting process
would leave the growing-depth exceptional-mass gap. The arithmetic input
in (20) must concern actual prime trajectories on the stated entire
horizon. Bounds for arbitrary directions, scalar-only projected repairs,
or only dispersed sampled primes do not supply it.

## 6. Actual prime and square trajectories

The [replay](parallel-activation-26.py) initializes the exact source
increment and evolves it with `D_next=K(d D)` (or its averaged version),
so late increments are not obtained by subtracting two nearly equal FFT
outputs. It independently recomputes the original recurrence at recorded
checkpoints to measure numerical drift. These are floating-point
trajectories, **not interval certificates or uniform estimates**.

At `tau=.05`, the [primary records](parallel-activation-26-picard.jsonl)
give the following rounded values. RMS is that of the scaled bulk field;
the high-amplitude columns use the maximum of the two endpoint amplitudes.

| Order | Depth | Bulk RMS | Weighted `A_t` | Squared increment ratio | `D^2` fraction above 16 | Weighted moment contribution above 16 |
|---:|---:|---:|---:|---:|---:|---:|
| 9413 | 64 | 2.293 | 5.183 | .82246 | 0 | 0 |
| 153649 | 64 | 2.309 | 5.406 | .83100 | 0 | 0 |
| 1000033 | 64 | 2.313 | 5.305 | .82985 | 0 | 0 |
| 97² | 64 | 5.053 | 2212.5 | .99031 | .95727 | 2212.39 |
| 389² | 64 | 3.352 | 2699.5 | .99831 | .98762 | 2699.45 |
| 389² | 255 | 9.463 | 33784.96 | .99765 | .98949 | 33784.93 |

At `389²`, depth 64, only `.2564%` of bulk coordinates exceed 16, but they
carry `98.76%` of the increment energy and essentially the whole weighted
amplitude. Bulk RMS `3.352` alone misses this effect. This is a delayed
exceptional arithmetic trajectory, rather than a test on arbitrary vectors.

The sampled prime increments do **not** exhibit a blanket tendency to
avoid large coordinates. At `1000033`, `tau=.05`, depth 255, `6.216%` of
coordinates exceed four and they carry `6.208%` of increment energy; their
weighted moment contribution is `1.31249`, about a quarter of the full
amplitude. A claim of strong anti-correlation is not supported by this
measurement. The observed boundedness is compatible with increment energy
remaining distributed through the field.

The [smaller-floor records](parallel-activation-26-small-floor.jsonl) give,
at the million-order prime and the indicated late depths:

| `tau` | Depth | `A_t` | Squared ratio | Increment energy fraction with both endpoints `<=2 sqrt(tau)` |
|---:|---:|---:|---:|---:|
| .05 | 255 | 5.35970 | .830995 | .11446 |
| .01 | 511 | 5.54379 | .921460 | .05075 |
| .001 | 511 | 5.63193 | .974244 | .01705 |

These small-ball fractions are roughly proportional to `sqrt(tau)` on this
small set of runs. They motivate (10); they do not prove a density limit,
an independence assertion, or a uniform prime small-ball theorem.

The [averaged controls](parallel-activation-26-averaged.jsonl) use `h=1/2`.
The identities and applicable two-step bounds are checked at every
processed step, and the one-step moment bound at recorded checkpoints.
The independent sign-count audit (6) is
exact; all FFT, moment and orbit checks remain floating point.

The [near-square prime stress inputs](parallel-activation-26-stress.jsonl)
`1008001` and `151337` do not change the finite-data picture. At `tau=.001`,
depth 511, their respective amplitudes are `5.62871`, `5.63949`, and squared
ratios are `.974202`, `.974212`. At `tau=.05`, depth 128, the respective
amplitudes are `5.32585`, `5.40588`. These selected primes, including the
near-square inputs, support further testing of the hypothesis; they do
not establish it for arbitrary primes or depths.

Across the 24 primary, smaller-floor, averaged and stress trajectories,
the largest relative increment-identity error was `1.24e-15`, the largest
direct-recurrence RMS drift at a recorded checkpoint was `1.93e-14`, and
no one-step moment or applicable two-step bound failed its stated
floating tolerance. These numbers verify the implementation's algebraic
consistency; they do not enclose its distance from an exact arithmetic
trajectory. The exact sign-count/Parseval and rational matrix audit is
separate from those numerical checks.

## 7. Mean and mark in an endpoint repair

The `M_t` in (12) is the loss of the constant Fourier component. It should
not be confused with the available **repair mean**. For a reciprocal source
with actual root `a`, mean coefficient `c`, and a correction `G` of root
`g_0` and mean coefficient `b`, the exact endpoint comparison remains

\[
 \frac{\theta}{\sqrt n}\ge\frac{a+g_0}{c+b}. \tag{25}
\]

Thus a target quotient at least one requires `b<=a+g_0-c`, not an
unjustified replacement by `1-c`. Root-preserving corrections set `g_0=0`.
This is the same reserve/root accounting as
[the explicit repair formula](parallel-repair-17.md) and
[the moving-width transport](astra-transport-22.md). The increment theorem
does not turn the scalar seed's vanishing bulk defect into endpoint
feasibility, nor remove the arithmetic radius/mean requirement in
`astra-dynamics-24`. Its direct endpoint application is the full residual
certificate (17), with actual root and actual `W` retained.

## Replay commands

All new outputs have the prefix `research/parallel-activation-26`. The
integer audit can be rerun without floating transforms:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-activation-26.py --integer-audit \
  --primes 5 13 61 9413 153649 1000033 --square-roots 7 11 97 389 \
  > research/parallel-activation-26-integer.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-activation-26.py --steps 256 \
  > research/parallel-activation-26-picard.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-activation-26.py --tau .01 .001 --steps 512 \
  --checkpoints 0 1 2 4 8 16 32 64 128 256 511 \
  > research/parallel-activation-26-small-floor.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-activation-26.py --tau .05 --relaxation .5 --steps 512 \
  --checkpoints 0 1 2 4 8 16 32 64 128 256 511 \
  > research/parallel-activation-26-averaged.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-activation-26.py --primes 1008001 151337 --square-roots \
  --tau .05 .001 --steps 512 --checkpoints 0 1 2 4 8 16 32 64 128 256 511 \
  > research/parallel-activation-26-stress.jsonl
```
