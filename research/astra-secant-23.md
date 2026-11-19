# Exact scaled-tail criterion and the broad/narrow secant obstruction

This note uses the conventions of [the one-sided quadratic](one-sided-quadratic-22.md)
and [the smoothed repair tail](soft-tail-21.md). It proves a necessary-and-sufficient
large-penalty criterion for ordinary theta. It does **not** prove the required
estimate through primes. It also identifies precisely what the one-sided secant
tests on any subsequential limiting family, and gives a quantitative square-order
obstruction without assuming a value for the square plus broad limit.

## 1. A uniform energy cap that is useful in both directions

Let

\[
\mathcal C_q=\{W\geq0:W\in U_\sigma,\ \sum_iW_i=1\},\qquad
z(W)=\sqrt nW_0,\quad e(W)=\sqrt n\|P_\sigma W\|_2^2,
\quad T_q=\max_{\mathcal C_q}z.
\]

Thus \(T_q=\theta_\sigma/\sqrt n\). The translated Jacobi point cap gives,
with an absolute constant \(C\),

\[
0\leq\sqrt nW_i\leq C\quad\hbox{for every }i,
\qquad 0\leq e(W)\leq\sqrt n\|W\|^2\leq C. \tag{1}
\]

The second assertion applies to **every** feasible mass-one row, not just a
theta optimizer. This upper energy bound prevents a positive endpoint margin
from disappearing from a suitably rescaled quadratic tail.

## 2. A necessary-and-sufficient large-penalty tail

Take the actual smoothed repair optimum \(\mathcal H_q(\lambda)\) in
[soft-tail-21, (3)](soft-tail-21.md), at mark \(a_s=\sqrt n\) and mean one.
Its exact dual, with \(W=uV\), is

\[
\mathcal H_q(\lambda)=
\max_{V\in\mathcal C_q,\ 0\leq u\leq1}
\left\{u(z(V)-1)-\frac\lambda2 u^2B_q(V)\right\},
\quad B_q(V)=\sum_{i\ne0}M_i h_iV_i^2. \tag{2}
\]

Since \(M_i h_i=O(\sqrt n)\), (1) gives \(B_q(V)\leq C_B\)
uniformly. Put \(\Delta_q=(T_q-1)_+\), and choose a fixed \(D\) bounding
all \(\Delta_q\). For \(\lambda\geq D/C_B\), testing an endpoint
optimizer at mass \(u=\Delta_q/(\lambda C_B)\) proves

\[
\boxed{\quad
\frac{\Delta_q^2}{2C_B\lambda}\leq\mathcal H_q(\lambda)
\leq\Delta_q.\quad} \tag{3}
\]

Consequently, on any field family,

\[
\boxed{\quad
\limsup_q\frac{\theta_\sigma}{\sqrt n}\leq1
\quad\Longleftrightarrow\quad
\lim_{\lambda\to\infty}\lambda\limsup_q\mathcal H_q(\lambda)=0.
\quad} \tag{4}
\]

For the forward implication the inner limsup is zero for **every** fixed
\(\lambda>0\). For the reverse implication, a subsequence with
\(\Delta_q\geq\delta>0\) makes the right side of (3), after multiplication
by \(\lambda\), at least \(\delta^2/(2C_B)\).
The outer limit exists in the extended nonnegative reals: for each fixed
\(V\), the optimized quantity
\(\lambda\max_{0\leq u\leq1}(u\delta-\lambda B u^2/2)\)
increases until it reaches \(\delta_+^2/(2B)\), and is then constant
(with the evident convention if \(B=0\)). Maxima and field limsups preserve
monotonicity.

Apply (4) on both signs and use endpoint reciprocity to obtain an exact
criterion for Problem 26. This closes the *logical* gap between the broad-tail
criterion and the endpoint: the needed hypothesis is **o(1/\lambda)**,
not merely decay of the unscaled smooth tail. It supplies no new arithmetic
estimate for that hypothesis.

The same theorem holds for the simpler dual penalty \(B_q(V)=e(V)\),
using (1) directly. More generally it holds for any nonnegative quadratic
penalty uniformly bounded on \(\mathcal C_q\).

### Square-order lower coefficient

At \(q=t^2\), take \(V=\mathbf1_I/h\), \(h=(t+1)/2\).
Then \(z(V)\to\sqrt2\), while the actual repair penalty satisfies
\(B_q(V)=h_I/h\to1\), by the explicit calculation in soft-tail-21.
Optimizing its mass in (2) gives

\[
\liminf_{\lambda\to\infty}\lambda\liminf_{t\to\infty}
\mathcal H_{t^2}(\lambda)
\ \geq\ \frac{(\sqrt2-1)^2}{2}=\frac32-\sqrt2>0. \tag{5}
\]

This is a lower bound, not an equality assertion for all square orders.
The two finite pinned certificates in square-pinned-22 are not extrapolated.

## 3. What broad/narrow mixing says about the secant

Here the penalty is \(e\) and

\[
F_q(R)=\max_{W\in\mathcal C_q}\frac{z(W)^2}{1+Re(W)}.
\tag{6}
\]

For precision about subsequences, set
\(S_q=\{(z(W),e(W)):W\in\mathcal C_q\}\subset[0,C]^2\).
Pass to any subsequence on which these compact nonempty sets converge in
Hausdorff distance to \(S\). Then

\[
f(R)=\lim_qF_q(R)=\max_{(z,e)\in S}\frac{z^2}{1+Re},\qquad
T=\lim_qT_q=\max_Sz,
\quad\beta=\max\{z:(z,0)\in S\}. \tag{7}
\]

There is always a zero-energy point, from the uniform row. Compactness gives
\(f(R)\downarrow\beta^2\) as \(R\to\infty\). This is the
subsequence's broad mark; different subsequences need not have the same one.

Choose a broad sequence \(A_q\) with \(z(A_q)\to\beta\),
\(e(A_q)\to0\), and a narrow sequence \(N_q\) with
\(z(N_q)\to T\), \(e(N_q)\to e_*\). Positivity and the sector
constraint survive convex mixing. Cauchy–Schwarz gives

\[
e((1-u)A_q+uN_q)\longrightarrow u^2e_*,\qquad
z((1-u)A_q+uN_q)\longrightarrow\beta+u(T-\beta). \tag{8}
\]

In particular, if \(T>\beta>0\), then \(e_*>0\), and optimizing
\(u\) yields, whenever \(R\geq(T-\beta)/(\beta e_*)\),

\[
\boxed{\quad f(R)\geq\beta^2+
\frac{(T-\beta)^2}{e_*R}.\quad} \tag{9}
\]

The maximizing weight is \(u=(T-\beta)/(\beta e_*R)\).
Thus the cross term in the **mark** is first order in the mixing weight,
whereas the Fourier penalty is second order. If \(\beta=0<T\), the
unmixed narrow row gives \(f(R)\geq T^2/(1+Re_*)\), with the same
asymptotic coefficient \(T^2/e_*\).

Define \(D_f(R)=R(f(R/2)-f(R))\). Telescoping gives

\[
R(f(R)-\beta^2)=\sum_{k\geq1}2^{-k}D_f(2^kR).
\]

Hence (9), including the \(\beta=0\) case, proves

\[
\boxed{\quad
\limsup_{R\to\infty}D_f(R)\geq\frac{(T-\beta)^2}{e_*}
\geq\frac{(T-\beta)^2}{C}\quad(T>\beta).
\quad} \tag{10}
\]

Conversely, if \(T=\beta\), (7) gives \(f(R)=T^2\) for every
\(R>0\). Therefore, for each such limiting family,

\[
\boxed{\quad D_f(R)\longrightarrow0
\quad\Longleftrightarrow\quad T=\beta.\quad} \tag{11}
\]

This is an exact interpretation of the secant: it tests whether the endpoint
mark can already be reached at zero limiting energy. It is not intrinsically
a threshold-one test. The theorem does not assert that every prime limit
has \(\beta=T\), nor that ordinary theta convergence alone proves that
additional dispersion property.

The order of limits matters. For every limiting family,
\(f(R/2)-f(R)\leq\limsup_q(F_q(R/2)-F_q(R))\), so its obstruction
passes to the original field-first secant criterion. No exchange of a field
limsup with subtraction is used.

In fact the original vanishing secant condition is equivalent to
\(T=\beta\) for **every** Hausdorff limiting family. Necessity follows
from (10). For sufficiency, every such \(f\) is constant, so at each fixed
\(R>0\) the field limsup of \(F_q(R/2)-F_q(R)\) is already zero:
otherwise a subsequence with a positive drop has a Hausdorff-convergent
further subsequence, contradicting constancy. Thus the apparent large-
\(R\) rate condition actually forces all fixed-scale drops to vanish.

### Artificial Fourier cone: theta is correct but the secant fails

There is a clean obstruction to declaring the secant *necessary* using
only Fourier support, positivity, translation symmetry, the point cap and
endpoint reciprocity. Take the group \(G=\mathbb Z_m^2\), \(n=m^2\),
and a subgroup \(H\) of size \(m\). Let \(U_+\) consist of functions
constant on the cosets of \(H\); it is an exact Fourier subspace. Let
\(U_-=\operatorname{im}J\oplus U_+^\perp\).

In \(U_+\), a mass-one nonnegative row has \(W_0\leq1/m\), with
equality for the uniform row on \(H\). In \(U_-\), every coset has
mass \(1/m\), so again \(W_0\leq1/m\), and equality is attained
by concentrating the mass of the root coset at zero. Thus **both** endpoint
theta values are exactly \(m=\sqrt n\), and both sectors obey the
translated point cap with constant one.

For the plus sector let \(x\) be the mass on the root coset. The minimum
energy at that mark is attained by distributing the remaining mass equally
over the other cosets:

\[
z=x,\qquad e_{\min}(x)=\frac m{m-1}(x-1/m)^2,\qquad 0\leq x\leq1.
\]

For \(0<R\leq m\), the quotient in (6) is increasing in \(x\), hence

\[
F_m(R)=\frac1{1+R(1-1/m)},\quad
f(R)=\frac1{1+R},\quad \beta=0,\quad T=1,\quad
\lim_{R\to\infty}R[f(R/2)-f(R)]=1. \tag{11a}
\]

So the broad bound holds and ordinary theta has exactly the desired value,
yet the secant fails. This is an artificial Fourier-cone example, **not**
a Paley example: its ranks are unbalanced,
\(\kappa_+=(m-1)/m^2\to0\) and \(\kappa_-\to1\).
It does not disprove necessity under the additional Paley balanced-rank
and arithmetic hypotheses. It identifies precisely an extra dispersion
fact that a proof of necessity there would have to supply.

### An unconditional square dichotomy

On square plus, \(T=\sqrt2\). Its known subfield optimizer has
\(e_*\to\sqrt2\), so that value can replace \(C\) in (10).
If the global broad bound in one-sided-quadratic-22 is at most one, then
every limiting family above has \(\beta\leq1\). Consequently

\[
\boxed{\quad
\limsup_{R\to\infty} R\limsup_{t\to\infty}
[F_{t^2}(R/2)-F_{t^2}(R)]
\geq\frac{(\sqrt2-1)^2}{\sqrt2}
=\frac3{\sqrt2}-2>0.
\quad} \tag{12}
\]

Thus either the square broad limit is greater than one, or its secant
fails by at least this positive limsup coefficient. This conclusion does
not require identifying the unknown square plus broad mark. Mixing with
the explicit broad row of mark \(1/\sqrt2\) alone would **not** prove
(12): its baseline might be smaller than the actual broad limit. The
compact-limit argument is what permits mixing at the correct baseline.

## 4. An exact all-width constrained-energy dual

There is also a finite-dimensional way to keep the mean constraint instead
of bounding it by the total objective. Define, for \(c>1/\sqrt n\),

\[
G_q(c)=\min_{b\geq0,\ b_0=1,\ \sum b/\sqrt n\leq c}
\sqrt n\|P_\sigma b\|^2.
\]

Then

\[
\boxed{\quad G_q(c)=\sup_{R\geq0}R(F_q(R)-c^2).\quad} \tag{13}
\]

At \(R=0\) the expression means zero. Indeed \(RF_q(R)\) is the
infimum of \(\sqrt n\|P_\sigma b\|^2+R(\sum b)^2/n\).
Apply convex Lagrange duality to the constraint \((\sum b)^2/n\leq c^2\).
Relative Slater holds: take anchor one and sufficiently small positive bulk
entries. The primal feasible set is compact. These facts justify equality,
including when the optimal multiplier is zero.

Using the explicit mark/mean repair of one-sided-quadratic-22 gives

\[
\frac{d_q(a,1)^2}{\sqrt n}
\leq a^2\left(1+\frac{\kappa_\sigma}{\kappa_{-\sigma}}\right)
G_q(1/a). \tag{14}
\]

Conversely, if a pinned row has negative-part norm \(d\), its positive
part, divided by \(a\sqrt n\), gives

\[
G_q\left(\frac{1+d/\sqrt n}{a}\right)
\leq\frac{d^2}{a^2\sqrt n}. \tag{15}
\]

The slight mean slack in (15) must not be silently discarded.
For both signs, the following are equivalent: Problem 26;
\(G_p(1/a)\to0\) for every fixed \(0<a<1\); and vanishing normalized
pinned defect for every such \(a\). For the forward implication of the
\(G\) statement, complementary endpoint theta tends to one, so an exact
nonnegative opposite-sector anchored optimizer already has mass below
\(\sqrt n/a\), and \(G=0\) eventually. The reverse follows from (14)
and the pinned-row pairing argument in one-sided-quadratic-22.

Equation (13) keeps a supremum over **all widths before the field limit**.
Replacing it by a tail supremum or moving that supremum outside the field
limit is not justified here. In contrast, (4) is a genuine necessary-and-
sufficient field-first large-penalty criterion, using the smooth margin
objective rather than the one-sided quadratic secant.

## Verification and scope

The proofs above are finite-dimensional convexity, the existing translated
Jacobi cap, and the established square subfield trial. No new character-sum
estimate or all-prime bound is claimed. The companion
`astra-secant-23-check.py` checks the mixing optimizer algebra and compares
(13) with dense constrained quadratic minimization on small actual prime
and square Fourier sectors. Its output is numerical verification of the
formulas, not interval certification or evidence for an asymptotic rate.

Replay:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-secant-23-check.py > research/astra-secant-23-check.json
```

The run checked 81 mixing identities, 9 artificial-cone quotients, and 24
constrained dual values on both signs at orders 25, 29, 49 and 61.
The largest constrained-dual discrepancy was below \(9\cdot10^{-13}\).
Eight of the 24 cases use the endpoint LP to verify a zero-energy feasible
row and hence a dual maximum of zero at \(R=0\); the other sixteen
numerically optimize the positive dual multiplier.
