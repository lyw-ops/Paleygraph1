# Exact time telescopes, scalar reserve, and a square-order source-tail obstruction

Round 29, 2026-11-18. Ordinary Lovász theta / ETH Problem 26.

**No prime-uniform estimate is proved.** The useful outcome is an exact
reduction and a quantitative obstruction at the requested `top O(sqrt n)`
scale, on actual zero-start trajectories. Positive decreasing time weights
do not create extra pointwise cancellation: their transformed residual is
the centered image of a nonnegative combination of actual activations.
The scalar reserve is real and sometimes large, but even after retaining it
exactly the square controls force a positive discrepancy. In fact their
terminal, geometrically averaged source has top-`O(sqrt n)` mass growing
at least linearly in fixed depth in the field-first limit; see (21).

This is **not** a new prime criterion claimed to be strictly weaker than
all previous norm/amplitude criteria. Section 7 gives a terminal-source
criterion weaker than the older terminal sup-amplitude test; no implication
relative to the increment-weighted criterion of round 26 is claimed. The
finite support certificate below is an application of the accepted source-tail relaxation to an exact time
identity. The new information is the nonnegative-source reduction, the
weight restriction, and the explicit actual-source lower bound. Arbitrary
static Fejér profiles are not used as surrogate orbits.

## 1. Setup and exact identities

Let `q=2n+1`, `P=I-J`, `K=K^T`, `K1=0`, `K^2=P`, and use the actual Paley
multiplier. Set

\[
w_0=1,\quad w_i=\tau/n\ (i\ne0),\quad
W=1+(n-1)\tau/n,\quad a_i=2\sqrt{w_i},
\quad \Phi_i(x)=\sqrt{x_i^2+4w_i}.
\]

Throughout, `0<tau<1`, and the actual trajectory is

\[
z_0=0,\qquad z_{t+1}=(1-\rho)z_t+\rho K\Phi(z_t),
\qquad 0<\rho\le1. \tag{1}
\]

The relaxation `rho` is unrelated to the bulk floor `tau/n`. Define

\[
u_t=\Phi(z_t),\quad g_t=u_t-a\ge0,\quad
r_t=z_t-Ku_t,\quad b_t=-Kr_t=Pu_t-Kz_t,
\quad E_t=\|z_t\|^2,\quad S_t=\sum_i u_{t,i}/\sqrt n.
\]

All vectors `z_t` have mean zero. For the exact stationary pair put
`u*=Phi(v*)`, `v*=Ku*`, `M=sum u*=2sqrt(nW)`. The mass follows directly
from `||u*||^2-||v*||^2=4W` and `K^2=P`.

With `gamma_i=asinh(v_i*/(2sqrt(w_i)))` and
`eta_(t,i)=asinh(z_(t,i)/(2sqrt(w_i)))`, the exact discrepancy is

\[
\begin{split}
\Delta_t
&=\langle u^*,u_t\rangle-\langle v^*,z_t\rangle-4W\\
&=4\sum_iw_i\{\cosh(\gamma_i-\eta_{t,i})-1\}\\
&=2\sqrt W S_t-4W+\langle b_t,u^*\rangle\ge0. \tag{2}
\end{split}
\]

This is the normalization of [source-tail-28](source-tail-28.md), not the
possibly differently normalized `D_t` in older notes.

The squared norm of `Ku_t` is `E_t+4W-S_t^2`. Expanding the relaxed update gives

\[
E_{t+1}=E_t+\rho(4W-S_t^2)
             -\rho(1-\rho)\|r_t\|^2.
\]

Consequently the scalar contribution is **exactly**

\[
\boxed{
2\sqrt W S_t-4W
=\frac{E_t-E_{t+1}}{2\rho}-R_t,
\quad
R_t=\frac{1-\rho}{2}\|r_t\|^2+
                 \frac12(S_t-2\sqrt W)^2\ge0.}
\tag{3}
\]

Both terms in `R_t` matter. The second contains the full activation mass,
including the mark. Formula (3) is not an estimate on the bulk mean alone.

## 2. Arbitrary nonnegative time weights: boundary and interior terms

Choose any nonnegative weights `lambda_t`, summing to one, on `L<=t<=R`.
They may depend on the field and on the observed trajectory. Let
`bar b=sum lambda_t b_t`, `bar Delta=sum lambda_t Delta_t`. Then

\[
\begin{split}
\bar b={1\over\rho}K\bigg[
 \lambda_R z_{R+1}-\lambda_Lz_L+
 \sum_{s=L+1}^R(\lambda_{s-1}-\lambda_s)z_s\bigg],\\
Q_\lambda={1\over2\rho}\bigg[
 \lambda_LE_L-\lambda_RE_{R+1}+
 \sum_{s=L+1}^R(\lambda_s-\lambda_{s-1})E_s\bigg],\\
\boxed{\quad\bar\Delta=Q_\lambda-\sum_t\lambda_tR_t
                            +\langle\bar b,u^*\rangle.\quad}
\tag{4}
\end{split}
\]

Proof: `b_t=K(z_(t+1)-z_t)/rho`, then summation by parts and (3).
For uniform weights on `0<=t<T`, this simplifies to

\[
\bar b={Kz_T\over\rho T},\qquad
\bar\Delta=-{E_T\over2\rho T}
            -{1\over T}\sum_{t<T}R_t
            +{\langle z_T,v^*\rangle\over\rho T}. \tag{5}
\]

Thus the negative endpoint energy is an actual reserve. Bounding only the
last pairing loses it. For a later window, the positive starting energy
`E_L/(2rho(R-L+1))` must be restored. For increasing weights there are
positive interior energy terms in (4); using just a terminal energy term
would be wrong.

As a useful equivalent check, (5) equals

\[
\frac{\|v^*\|^2-\|z_T-v^*\|^2}{2\rho T}
                         -\frac1T\sum_{t<T}R_t.
\]

This equality is not a usable field-uniform bound unless the resulting
pairing or norm is controlled. In particular it does not prove Problem 26.

## 3. What time averaging can actually cancel

For unaveraged Picard, `rho=1`, at times `t>=1`,

\[
b_t=P(g_t-g_{t-1}),\qquad
{1\over T}\sum_{t=1}^T b_t={P g_T\over T}. \tag{6}
\]

There is no signed raw endpoint source: `g_T>=0`. Centering is essential,
and can have either sign at individual coordinates. More generally,
if `lambda_1>=...>=lambda_T>=0`,

\[
\sum_{t=1}^T\lambda_tb_t
=P\left[\lambda_Tg_T+
       \sum_{t=1}^{T-1}(\lambda_t-\lambda_{t+1})g_t\right]. \tag{7}
\]

The bracket is a nonnegative combination of actual sources. This statement
concerns the prefix starting at zero. A window starting later has a negative
initial-source boundary term, and is not covered by its positivity claim.

For the general relaxed iteration, expand the *actual* recurrence:

\[
z_t=\rho K\sum_{j<t}(1-\rho)^{t-1-j}u_j.
\]

For weights on `0<=t<T`, this gives the exact formula

\[
\begin{split}
\bar b&=PH_\lambda,\qquad H_\lambda=\sum_{j<T}\kappa_ju_j,\\
\kappa_j&=\lambda_j-\rho\sum_{t=j+1}^{T-1}
                   \lambda_t(1-\rho)^{t-1-j},\\
\sum_j\kappa_j&=\sum_{t<T}\lambda_t(1-\rho)^t. \tag{8}
\end{split}
\]

If the weights are nonincreasing, then

\[
\kappa_j\ge\lambda_j(1-\rho)^{T-1-j}\ge0. \tag{9}
\]

Indeed replace every later `lambda_t` by `lambda_j` in the geometric sum.
For uniform weights define the terminal activation and source

\[
\widehat u_T=\rho\sum_{j<T}(1-\rho)^{T-1-j}u_j,
\quad \beta_T=1-(1-\rho)^T,
\quad \widehat g_T=\widehat u_T-\beta_Ta\ge0.
\]

Then

\[
\boxed{\quad \bar b={P\widehat u_T\over\rho T}.\quad} \tag{10}
\]

At `rho=1`, `hat u_T=u_(T-1)`. These are recent geometric averages, not
ordinary averages of all past sources. The initial activation is retained.
In particular dropping its root value `a_0=2` changes the formula.

Increasing weights can have negative `kappa_j`; (8) describes precisely
where a genuine raw-source cancellation might be obtained. It would have
to be estimated jointly with the interior energy terms in (4).

There is a second elementary restriction on decreasing weights. Extend
`lambda_T=0`, with original indices `0,...,T-1`, and set
`alpha_k=k(lambda_(k-1)-lambda_k)`, `1<=k<=T`. Then `alpha_k>=0`,
`sum alpha_k=1`, and, for **any** scalar sequence `d_t`,

\[
\sum_{t<T}\lambda_td_t
=\sum_{k=1}^T\alpha_k\left({1\over k}\sum_{t<k}d_t\right). \tag{11}
\]

Thus decreasing weights cannot make the *exact* discrepancy smaller than
the best uniform prefix discrepancy. This does not say a convex relaxed
support bound cannot improve under mixing: that would interchange a
maximum over unknown stationary data with an average.

## 4. A finite, observable bound with all reserve and root terms

For completeness the time reduction can be enclosed without knowing `u*`.
Write `a=2sqrt(tau/n)` now for the constant bulk baseline, `h=tau/n`,
`B=M-na`, and `s=u_0*`. The positive stationary rows
`A=(u*+v*)/2`, `Brow=(u*-v*)/2` have means `sqrt(W/n)`, pointwise products
`w_i`, and `A_i<=A_0`, `Brow_i<=Brow_0`. To recall the latter proof,
`sum w_i log(A_(i+j)/A_i) <= sum Brow_i(A_(i+j)-A_i)=0` by
complementary Fourier support; constant bulk weights cancel, leaving
`(1-h)log(A_j/A_0)<=0`. The other row is identical.

Let

\[
C=(1+\sqrt q)\sqrt{W/n},\quad
s_{\max}=\min(C+C^{-1},B+a),\quad
m(s)={1+h\over2}s+{1-h\over2}\sqrt{s^2-4}.
\]

The entry bound on `K` gives `A_0,Brow_0<=C`. Since their product is one,
`2<=s<=s_max`; the bulk bounds are `a<=u_i*<=m(s)`. For any **real**
threshold `x`, put `U_x=sum_(i!=0)(bar b_i-x)_+`. Exactly as in the accepted
source-tail certificate,

\[
\mathcal H_x(\bar b)=\max_{2\le s\le s_{\max}}
\{(s-a)(\bar b_0-x)+(m(s)-a)U_x+xB\}
\ge\langle\bar b,u^*\rangle. \tag{12}
\]

The expression is `Ls+J sqrt(s^2-4)+constant`, with `J>=0`, so endpoints
and the possible critical point give its explicit maximum. All signs of
`x`, the root cost, and the mass term are retained. Therefore

\[
D_\lambda=Q_\lambda-\sum_t\lambda_tR_t+
                                    \mathcal H_x(\bar b)\ge\bar\Delta\ge0.
\tag{13}
\]

For the averaged root angle `bar eta=sum lambda_t asinh(z_(t,0)/2)`,
Jensen in (2) gives

\[
|\gamma_0-\bar\eta|\le\operatorname{arcosh}(1+D_\lambda/4). \tag{14}
\]

Consequently ordinary theta obeys

\[
\frac{\exp(\bar\eta-\operatorname{arcosh}(1+D_\lambda/4))}{\sqrt W}
\le\frac{\theta_+}{\sqrt n}\le
\sqrt W\exp(\bar\eta+\operatorname{arcosh}(1+D_\lambda/4)). \tag{15}
\]

To justify the last step, `sqrt(n/W)A` is a feasible theta spectrum and
`sqrt(n/W)Brow` is feasible for the complementary theta problem. Their
root product is `n/W`; the complementary theta product is `n`. Hence
`e^(gamma_0)/sqrt W <= theta_+/sqrt n <= sqrt W e^(gamma_0)`.
For a small discrepancy the radius is of order `sqrt(D_lambda/2)`, not
`D_lambda`. A merely bounded positive budget is insufficient.

## 5. A strict square control, including arbitrary positive weights

For `q=r^2`, the exact ordinary theta is `theta_+=r-1`. For reference,
`F_r^times` is a clique of size `r-1`; the complementary Fourier row
`1_{1}+2 1_{s=-1}/(r+1)` is nonnegative in Fourier space by the Jacobi
bound, giving the matching complementary value `(r+1)/2`. This uses the
square field itself, and imports no prime coset assumption.

The stationary bracket in (15) implies

\[
\gamma_0\ge\ell_{q,\tau}:=
\log\frac{r-1}{\sqrt{nW}}.
\]

For **any** nonnegative normalized weights on **any** finite time set,
including field-dependent weights and horizons, Jensen in (2) proves the
finite inequality

\[
\boxed{\quad
\bar\Delta\ge4\{\cosh((\ell_{q,\tau}-\bar\eta)_+)-1\}.
\quad} \tag{16}
\]

It follows that every valid signed-tail upper enclosure must satisfy

\[
\mathcal H_x(\bar b)\ge
4\{\cosh((\ell_{q,\tau}-\bar\eta)_+)-1\}
                              -Q_\lambda+\sum_t\lambda_tR_t. \tag{17}
\]

This explicitly includes the scalar cancellation. It is not a lower bound
on an unsigned residual. If a square-order growing-window marker average
is `o(1)`, the right side of (16) tends to

\[
c_\tau=4\left[\cosh\left({1\over2}\log{2\over1+\tau}\right)-1\right]>0.
\tag{18}
\]

This is an unconditional implication from that marker hypothesis. For any
**fixed** horizon, marker cancellation follows from the inherited
[fixed-depth parity proof draft](iteration-parity.md), as discussed in
[square-order-control](square-order-control.md). Under that draft, (18)
holds uniformly over all choices of weights on that fixed horizon. No
uniform assertion for growing horizons follows from the fixed-depth draft.

### A quantitative obstruction on the actual terminal source tail

Here is a consequence specifically at the desired top-`O(sqrt n)` scale.
Use uniform weights on `0,...,T-1`, and `hat u_T,hat g_T` from (10). Let

\[
k_n={B\over 2-a}-1,\qquad C_n=C+C^{-1}.
\]

For sufficiently large `n`, `0<=k_n<=n-1`; fractional top sums use linear
interpolation. The common bound `u_i*<=s` is weaker than (12), but convenient
for a necessary estimate. Removing the baseline `a`, the root uses mass
`s-a`, and the bulk uses `B-(s-a)` with cap `s-a`. Since `s>=2`, its capacity
index `B/(s-a)-1` is at most `k_n`. Positivity of `hat u_T` then gives

\[
\begin{split}
\langle P\widehat u_T,u^*\rangle
&=\langle\widehat u_T,u^*-a\mathbf1\rangle
                   -B\,\overline{\widehat u_T}\\
&\le C_n\{\widehat u_{T,0}+
                         \operatorname{Top}_{k_n}(\widehat u_{T,\rm bulk})\}.
\end{split}
\]

The discarded term is nonpositive. Combining this with (5), (10), and (16)
yields the finite actual-orbit lower bound

\[
\boxed{
\operatorname{Top}_{k_n}(\widehat g_{T,\rm bulk})\ge
{\rho T\over C_n}\left[
4\{\cosh((\ell_{q,\tau}-\bar\eta)_+)-1\}
+{E_T\over2\rho T}+{1\over T}\sum_{t<T}R_t
\right]
-\widehat u_{T,0}-k_n\beta_Ta.}
\tag{19}
\]

All terms are actual trajectory quantities. A negative right side is simply
uninformative. Equation (19) is a necessary lower bound, not a certificate
that a square trajectory has converged.

At fixed `T`, take the square-order field-first limit, invoking only the
inherited fixed-depth marker cancellation. Then

\[
\begin{gathered}
\widehat u_{T,0}\to2\beta_T,\quad
k_na\to d_\tau:=2\sqrt\tau(\sqrt{1+\tau}-\sqrt\tau),\\
C_n\to C_\tau:=\sqrt{2(1+\tau)}+1/\sqrt{2(1+\tau)}.
\tag{20}
\end{gathered}
\]

Dropping only the nonnegative energy and dissipation from (19) proves

\[
\boxed{
\liminf_{r\to\infty}
\operatorname{Top}_{k_n}(\widehat g_{T,\rm bulk})
\ge {\rho c_\tau\over C_\tau}T-\beta_T(2+d_\tau).
} \tag{21}
\]

Thus a proposed `o(T)` field-first bound for this top-tail quantity is
false on square controls. It is stronger information than merely forcing
one large scaled coordinate: it specifies growth of the aggregate mass
of the largest `O(sqrt n)` coordinates of a **true** terminal source.
At `tau=.05`, the weaker bound (21) is
`0.0978868 rho T - 2.358258 beta_T`, with the displayed coefficient of `T`
rounded downward and the constant rounded upward.
The lower bound concerns each fixed `T` followed by `r->infinity`; it does
not assert that (21) holds uniformly when `T=T(r)`. At any fixed square
order, late trajectories can converge and their markers can approach the
nonzero stationary marker, so (16) then need not remain positive.

## 6. Minimal replay and numerical checks

The standalone [script](astra-source-window-29.py) writes only JSON lines
to stdout. Its rational audit checks 36 combinations of horizon,
relaxation, and uniform/increasing/decreasing weights, including the exact
coefficient identity (8), positivity (9), prefix mixture (11), and the
energy summation by parts. It also checks (7) using rational test data.
An independent rational `q=9` Paley matrix also checks `K^2=P`, the
transformed residual, and the exact energy update at three relaxations
using a rational activation pair with the prescribed heterogeneous weights.
These checks are independent of FFTs and stationary solutions.

The floating replay starts the specified actual recurrence at zero, with
no Newton proposal and no stationary solve. The saved
[72 diagnostics](astra-source-window-29-check.jsonl) cover primes `61,9413`,
squares `7^2,97^2`, both relaxations `1,1/2`, depths `8,32,128`, and three
weight choices. The largest activation-telescope error is `2.94e-16`,
weighted scalar-identity error `1.74e-15`, and individual energy-identity
error `1.36e-14`. These are numerical consistency checks, **not interval
certificates or enclosures of an exact Picard prefix**.

For `tau=.05`, `rho=1`, `T=128`, selected floating quantities are:

| Order | Weights | Scalar | Source support upper bound | Full discrepancy upper bound |
|---:|---|---:|---:|---:|
| 9413 | uniform | -0.030317 | 0.072591 | 0.042274 |
| 9413 | decreasing | -0.059975 | 0.141850 | 0.081875 |
| 9413 | increasing | -0.000659 | 0.004275 | 0.003616 |
| 97² | uniform | -0.270688 | 0.651044 | 0.380356 |
| 97² | decreasing | -0.251433 | 0.773201 | 0.521768 |
| 97² | increasing | -0.289944 | 0.539215 | 0.249272 |

“Increasing/decreasing” means weights proportional to `t+1` or `T-t`,
respectively. Increasing weights help the listed prime calculation, but
also help the square, and this is not an asymptotic discriminator. All
square rows satisfy the finite necessary bounds (16) and (19). Root means,
terminal source top sums, and corresponding lower bounds are in the JSONL.

An additional [18 larger-field diagnostics](astra-source-window-29-larger.jsonl)
compare `153649` and `389^2` at `rho=1`. The observed terminal source top sums
(capacities about `221.22` and `219.53`) at depths `8,32,64` are respectively
`4.408,4.383,4.391` for the prime and `5.943,18.987,36.054` for the square.
The finite lower bounds (19) at the square are `0.275,2.801,6.556`. These
are floating diagnostics and selected finite orders, not a growth theorem
for primes.

Reproduce from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-source-window-29.py --exact-only

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-source-window-29.py \
  > research/astra-source-window-29-check.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-source-window-29.py --primes 153649 --square-roots 389 \
  --steps 8 32 64 --relaxation 1 \
  > research/astra-source-window-29-larger.jsonl
```

The existing accepted Arb certificates are not modified or recounted here.

## 7. A terminal-source criterion and its precise scope

The same common-cap proof, now on primes, gives the sufficient bound

\[
0\le\bar\Delta\le {C_n\over\rho T}
\{\widehat u_{T,0}+\beta_Tak_n+
               \operatorname{Top}_{k_n}(\widehat g_{T,\rm bulk})\}.
\tag{22}
\]

Here we discarded the **nonpositive** scalar in (5). The sharper signed
certificate (13) can do better. In particular, assume the inherited
fixed-depth marker cancellation, and for each fixed floor in a sequence
`tending to zero` assume the actual-prime source condition

\[
\liminf_{T\to\infty}{1\over T}
\limsup_{p\to\infty}
\operatorname{Top}_{k_n}(\widehat g_{T,\rm bulk})=0.
\tag{23}
\]

Then Problem 26 follows: (20), (22), and (14) first take the prime limit
at each fixed `T`; use a sequence of `T` supplied by (23); the root error
vanishes, leaving only `sqrt(1+tau)` in (15); finally send the floor to
zero. This is a valid field-first criterion, requiring no illicit
uniformity for a field-dependent horizon. The top sum is computed solely
from actual finite trajectories; its universal prime limit is unproved.

This criterion is weaker than the old **terminal sup-amplitude** condition
in [iteration-parity](iteration-parity.md#a-criterion-involving-only-the-iterates).
Indeed `g_(t,i)<=|z_(t,i)|` and

\[
\operatorname{Top}_{k_n}(\widehat g_{T,\rm bulk})
\le k_n\rho\sum_{j<T}(1-\rho)^{T-1-j}
                          \max_{i\ne0}|z_{j,i}|,\quad
k_n/\sqrt n\to\sqrt{1+\tau}-\sqrt\tau.
\tag{24}
\]

If the field-first scaled maximum is finite at every fixed depth and
`o(j)` as `j` grows, the geometric convolution on the right is `o(T)`
(split at a fixed index, then use the geometric tail). Finiteness of those
fixed-depth maxima is the separate inherited
[uniform fixed-depth draft](uniform-fixed-depth.md); it is not a consequence
of marked cancellation alone.
For `rho=1`, use the same statement for the Picard version and the single
terminal index `T-1`.

The functional weakening is strict: on even mean-zero trial profiles with
root zero, put value `1` at two opposite nonroot indices and
`-2/(n-3)` on the other nonroot indices. Their true activation sources
`Phi(z)-a` have bounded top-`k_n` mass (indeed total mass `2+o(1)`), while
`sqrt(n) max_bulk |z_i|` diverges. These are **static profiles**, used only
to show the two observable tests differ. They are not a counterexample to
any assertion about actual prime trajectories, and do not establish a
strict logical separation within that restricted family. No comparison
with round 26's *increment-weighted* amplitude criterion is proved.

Thus (23) is an explicit source-tail target, not an established prime
bound. Its relevance beyond renaming the single-trial residual condition
is that (10) derives it from the true time recurrence, and (21) proves
quantitatively that it fails on actual square controls.

## 8. Remaining prime gap

The exact algebra alone leaves two possible directions. A later window or
increasing weights can produce signed raw-source differences; proving their
positive centered top tail small requires an actual prime estimate, jointly
with the positive starting/interior energy in (4). Alternatively a prefix
bound on the nonnegative terminal source can work, but (21) shows precisely
what square arithmetic must violate. Neither estimate follows from
nonexpansiveness, residual decay, fixed-depth parity, positivity, or the
exact scalar reserve.

For a prime theorem one still needs compatible `bar eta->0` and
`D_lambda->0`, with all quantities evaluated on the same weights and
horizon, and then the justified floor limit. Static approximate profiles
from [astra-broad-source-28 §5](astra-broad-source-28.md#5-the-signed-transformed-residual-tail-escapes-this-obstruction)
separate tail and norm criteria but do not supply this orbit estimate.
The exact stationary pair is used only for the proved comparison; no
numerical stationary point is assumed exact, and no prime is assigned a
square-field subfield coset.
