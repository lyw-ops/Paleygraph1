# Linear-depth positive completion of the prescribed average

Throughout use $q=2n+1$, $0<\tau<n$, $c=\tau/n$, $w_0=1$,
$w_i=c$ off the mark, and $W=1+(n-1)c$. The operator and ordinary
theta signs are those of [the exact mark budget](averaged-mark-35.md).
The unit of time is one application of the undamped zero-start Picard
map. All deterministic theorems below apply to eligible primes and
square orders. The prime arithmetic needed for ETH26 remains open.

For each fixed positive floor, one pinned reflection completes both
prescribed rows at **every** integer depth above an explicit
$O_\tau(n)$ threshold. This improves the
[round-36 bound](parallel-audit-36.md) of $O_\tau(n^{5/4})$, with the
same mean and mark at the same depth. A separate averaging argument gives
strict positivity with no repair at an explicitly selectable linear
depth, or for a prescribed mixture of neighboring prefixes. Every
unmodified uniform prefix is itself strictly positive beyond an
$O_\tau(n\log n)$ threshold.
At the earlier $p=7340033$ saved input, a second sparse reflection
certifies both marks at depth 128. The finite result concerns the saved
Fourier input; the uniform theorems concern the exact orbit.

## 1. The reciprocal rows charge large endpoint errors quadratically

Write $v_0=0$, $\phi_t=\sqrt{v_t^2+4w}$,
$v_{t+1}=K\phi_t$, $\mu_t=\mathbb E\phi_t/2$, $M=T^{-1}\sum_{t=1}^T\mu_t$,
and $A_{\sigma,t}=(\phi_t+\sigma v_t)/2$.
Let $X_{\sigma,T}=M1+T^{-1}\sum_{t=1}^TP_\sigma A_{\sigma,t}$ and
$z_\sigma=X_{\sigma,T}/M$. The [endpoint identity](parallel-audit-36.md) is

\[
 z_\sigma=U_\sigma+e_\sigma,\qquad
 U_\sigma=\frac{1}{TM}\sum_{t=1}^T A_{\sigma,t}>0,\qquad
 e_\sigma=\frac{\sigma P_{-\sigma}(v_{T+1}-v_1)}{2TM}.
\]

Write $h_\sigma^2=\mathbb E e_\sigma^2$. Each $U_\sigma$ has mean
one, and Cauchy–Schwarz in time gives $U_+U_-\ge w/M^2\ge r=c/M^2$.
In particular $\mathbb E(1/U_\sigma)\le1/r$. For any $\kappa>0$,
set $d_0=0$, $d_i=(2\kappa-z_\sigma(i))_+$ elsewhere. Then

\[
 \boxed{\mathbb E d\le\frac{9\kappa^2}{4r}
                         +\frac{h_\sigma^2}{4\kappa}.}                 \tag{1}
\]

Indeed $2\kappa-U-e=(3\kappa-U)+(-e-\kappa)$.
For $u>0$, $u(3\kappa-u)_+\le9\kappa^2/4$; for real $x$,
$(x-\kappa)_+\le x^2/(4\kappa)$. Sum the two pointwise bounds
and take means. Omitting the marked coordinate can only help. The
previous direct Lipschitz estimate charged $h_\sigma$ itself.
The new bound still uses absolute spatial spill, but an endpoint
perturbation smaller than the reserve creates no second deficit.

## 2. An all-depth theorem at the original mean and marks

Let $s=\min(1,\tau)$, $H_0=n\mu_0^2=[1+(n-1)\sqrt c]^2/n$,
and $R=2\sqrt W\,q^{1/4}$. For $n\ge16$ set

\[
 \kappa=\frac{s}{54W\sqrt n},\qquad
 T\ge\frac{54\sqrt3\,W R}{s\sqrt{H_0}}\,n^{3/4}.                      \tag{2}
\]

For both signs the explicit output $z_\sigma+2L_\sigma d$ has
bulk entries at least $3\kappa/2$ and marked entry exceeding
$\kappa$. Here $L_\sigma=P_\sigma-(P_\sigma e_0)(P_\sigma e_0)^T/(P_\sigma)_{00}$ is the
[round-34 pinned projector](astra-conic-primal-34.md). Means remain
one, the appropriate sector and even symmetry are preserved, and
the marked values are exactly those of $z_\sigma$.

The stationary diameter estimate used in round 36 gives
$h_\sigma\le R/(T\sqrt{H_0})$: the stationary solution has
$\|v^*\|_2\le R$, Picard is nonexpansive, and both $v_{T+1}$
and $v_1$ lie within $R$ of $v^*$. Also $M\ge\mu_0$.
Thus (2) implies $h_\sigma\le\kappa/(\sqrt3\,n^{1/4})$.
The exact time mean budget yields $nM^2\le B_{n,T}\le2W$, so
$r\ge\tau/(2W)\ge27\sqrt n\,\kappa$.
The round-34 bulk spill inequality and its round-36 simplification
give $\|(2L_\sigma-I)d\|_{\infty,\mathrm{bulk}}\le \Gamma\|d\|_1\le3\sqrt n\,\mathbb E d$. Each term of (1)
contributes at most $\kappa/4$ to this last bound. The clipped
bulk $z_\sigma+d$ already exceeds or equals $2\kappa$.

At the mark, $U_+(0)U_-(0)\ge1/M^2$ and both normalized positive
raw rows sum to $n$. Therefore $U_\sigma(0)\ge1/(nM^2)\ge1/(2W)$.
The coordinate error there is at most
$\sqrt n\,h_\sigma\le s/(54\sqrt3\,Wn^{1/4})$.
This leaves more than $\kappa$, and pinning preserves that entry.
Since $H_0\ge\tau/2$ for $n\ge16$, the right side of (2) is
$O_\tau(n)$. Nothing assumes the stationary energy is field-uniform.

### Limitation of the absolute-spill argument

Evenness, mean one, a large marked product, raw bulk reciprocity
as an inequality, and an endpoint RMS of order $n^{-3/4}$ are
consistent with failure of the absolute-spill sufficient test at
**every** reserve. For an even integer $m\ge8$ let $n=m^2$, choose
an even set $S$ of $m$ unmarked coordinates, and put $N=n-m-1$.
Choose two raw rows with $U_0=V_0=m$. On $S$ set
$U=1/m,V=m/2$; elsewhere off the mark set
$U=1,V=(n/2-m)/N\ge1/3$. Both rows have mean one and $UV\ge1/3$.
Set $e_0=0,e|_S=-2/m,e|_{S^c\setminus\{0\}}=2/N$.
This has mean zero and $\mathbb E e^2=(4/m+4/N)/n=O(n^{-3/2})$.
On $S$, $U+e=-1/m$. For every positive reserve, the Paley
absolute coefficient $\Gamma=2b+2b^2/a>1/m$, with
$b=(1+\sqrt{2n+1})/(2n)$ and $a=(n-1-\sigma)/(2n)>0$, gives
$\Gamma\|d\|_1\ge\Gamma m(2\kappa+1/m)>2\kappa$.
Thus the usual uniform reserve comparison fails even if the
reserve may be chosen after seeing these rows. This is a scalar
relaxation example. It asserts neither actual Fourier feasibility
nor failure of any signed correction, Picard orbit, or prime.

## 3. Linear-depth positivity without a reflection at selected lengths

Set $a=\sqrt{W/n}$ and $D=2\sqrt q\,a$. The coherence bound and
positivity give $\|v_j\|_\infty\le2\sqrt q\,\mu_{j-1}$ for $j\ge1$.
The energy identity summed from $0$ gives
$T^{-1}\sum_{j=0}^{T-1}\mu_j^2\le a^2$.
It follows that the coordinatewise time averages of $|v_j|$
over $j=1,\ldots,T$, and over $j=0,\ldots,T-1$, are at most
$D$ at every coordinate. For the second interval, use $v_0=0$
and the length-$(T-1)$ bound if $T>1$.

For either time interval, $A_{-\sigma,j}(i)\le |v_j(i)|+\sqrt{w_i}$
and $A_{\sigma,j}(i)A_{-\sigma,j}(i)=w_i$. The average desired
raw row is therefore at least
$w_i/(D+\sqrt{w_i})\ge c/(D+\sqrt c)=:f$.
This coordinatewise lower bound for **averages** is independent of
the largest individual orbit coordinate. In the
[round-36 unrepaired decomposition](astra-averaged-positive-36.md)
the scalar term is nonnegative, and the two raw averages have
coefficients $1/2$. Consequently, for every uniform prefix,
\[
 \min_i X_{\sigma,T}(i)\ge f-
 \frac{2\sqrt q(\mu_{T-1}+\mu_T+\mu_0)}{4T}.                       \tag{3}
\]

For every integer $L>5D/(4f)$, choose $T\in[L,2L-1]$
minimizing $\mu_{T-1}+\mu_T$ (either tie rule works).
The block average of these sums is at most $4a$ by the prefix
energy inequality up to $2L$. Also $\mu_0\le a$.
Inequality (3) gives **both** unmodified rows a strictly positive
margin $f-5D/(4L)$. Alternatively take the uniform mixture
of $X_{\sigma,T}$ over that whole deterministic block. Applying
(3) before averaging gives the identical margin. Its mean has
squared budget at most $(W+1/L)/n$, by the individual prefix
budgets and convexity. The mixture has its own weighted marks.
The selected length retains its original marks and its sharper
original mean budget. Both constructions cost $O_\tau(n)$ Picard
steps. They do not establish direct positivity at **every**
unweighted linear-depth prefix. Section 2 covers every such prefix
with one reflection beyond (2).

### Every unmodified uniform prefix at \(O_\tau(n\log n)\)

Put \(g_j=\sqrt n\,\mu_j\). Discarding the constant mode in an update
gives a simultaneous family of inequalities in time. For every integer
\(k\ge1\) and \(J\ge1\),
\[
 \begin{split}
 4\sum_{j=0}^{J-1}(g_{j+k}-g_j)^2
 &\le \|v_k\|_2^2-\|v_{J+k}-v_J\|_2^2\\
 &\le E_k\le4Wk .                                                   \tag{4}
 \end{split}
\]
Indeed the squared norm of the difference of two updated states is
the squared norm of the two activation vectors' difference minus
its squared constant component \(4(g_{j+k}-g_j)^2\). The
activation is pointwise 1-Lipschitz. Telescope over \(j\) and use
\(E_k=4Wk-4\sum_{j<k}g_j^2\). No hypothesis is imposed on how
large \(J\) or the shift \(k\) can be.

For any contiguous block \(I\) of length \(b\), write \(\bar g_I\)
for its mean. The variance double-sum and (4) give
\[
 \frac1b\sum_{j\in I}(g_j-\bar g_I)^2
 =\frac{1}{b^2}\sum_{k=1}^{b-1}
    \sum_{j,j+k\in I}(g_{j+k}-g_j)^2
 \le\frac{W}{b^2}\sum_{k=1}^{b-1}k\le W/2.                         \tag{5}
\]
This bounded time variance is uniform in both the location and the
length of the block. If \(I'\) is one half of a dyadic block \(I\),
Cauchy–Schwarz gives \(|\bar g_{I'}-\bar g_I|\le\sqrt W\).
Take \(j_*=\lceil\log_2(4\sqrt q)\rceil\), \(b=2^{j_*}\).
For every \(t\), apply these estimates to blocks starting at
\(t\) of lengths \(1,2,4,\ldots,b\). The energy identity over
\([t,t+b)\) gives
\(\bar g_{[t,t+b)}^2\le W+E_t/(4b)\le W+R^2/b\le2W\),
since \(E_t\le4R^2\) and \(R^2=4W\sqrt q\). Therefore
\[
    \sup_{t\ge0}g_t\le\sqrt W\,(\sqrt2+j_*).
\]
Using this in (3) proves **direct** positivity of every original
uniform prefix at every integer
\[
             T>\frac{3D(\sqrt2+j_*)}{4f}=O_\tau(n\log n).           \tag{6}
\]
The earlier direct threshold for these same rows was
\(O_\tau(n^{3/2})\). For comparison, using only the one-step bound
\(\|v_{t+1}-v_t\|_2\le2\) would give \(E_t-E_{t+1}\le8R\) and
\(g_t^2\le W+2R\), which gives \(O_\tau(n^{9/8})\) in (3).
The logarithmic bound uses all time shifts. It makes no claim that
the logarithmic factor is necessary on the actual orbit.

## 4. The earlier large-prime failure admits an exact second repair

For the [saved input](endpoint-stress-36-p7340033-t128-input.json.gz)
with $p=7340033,T=128,\tau=1/20$, the original reflection clipped
to $2/1000$. Its minus coordinate $2136334$ was negative. The
[Arb128 replay](astra-completion-37.py) uses exactly that input,
verifies the integer minus coefficients and support, and reconstructs
its first pinned reflection $y$. This time use $d'_0=0$,
$d'_i=(1/5000-y_i)_+$ on the bulk. All branch comparisons are
strict, exactly ten coordinates are active, and
\[
 \|d'\|_1<0.001341091,\qquad \Gamma<0.000739030.
\]
The interval multiplication with unrounded quantities proves
$y+2L_-d'>0.0001990088944$ on the whole bulk. This second
application requires no further DFT for certification. Its mean,
sector, evenness and marked entry are exact by the projector
identities. Combine this minus row with the previously certified
first plus row on the same input, whose bulk minimum exceeds
$0.0001331280709$. The two marks give
\[
 0.9766958449849362<
 \vartheta(\overline H_{7340033})/\sqrt{3670016}
 <1.0228533015085074.
\]
The [record](astra-completion-37-certified.jsonl) gives the exact
rational unnormalized endpoints and the input digest. It uses
[the round-36 plus certificate](endpoint-stress-36-negative-certified.jsonl)
with exact digest and mark checks. This section gives no exact-orbit
budget for a rounded input and no asymptotic prime estimate.

Recompute the finite record with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B research/astra-completion-37.py

## 5. Which quantifiers are still missing

At fixed $\tau,T$ with $\tau+1/T<1$, the fixed-depth marked
limit and budget force the normalized minus mark divided by
$\sqrt n$ to exceed $1/\sqrt2$ by a positive amount for all
sufficiently large squares. Since their exact minus optimum is
$(\sqrt q+1)/2$, such a completion is then impossible. At a fixed
positive floor the new unconditional thresholds grow linearly in
the dimension, so they impose no constraint on that fixed-depth
square contradiction. At any field-dependent depths satisfying (2),
an actual prime marked Cesàro estimate of the kind in round 35
would give the ordinary theta squeeze at that floor. One would then
need a sequence of such fixed floors tending to zero. The proved
[short arithmetic window](parallel-depth-window-30.md) does not
reach the new thresholds. Neither the finite second repair nor the
scalar relaxation example settles the intervening prime estimates.

The [small independent checker](astra-completion-37-check.py) constructs
two dense actual Paley kernels from the prime and square sign arrays.
It evolves 26 steps at 320 bits for fields 37 and 49, checks (1), (3),
and the time-shift and block-variance bounds, and checks three rational
scalar-relaxation sizes. Its [five records](astra-completion-37-checks.jsonl)
are reproducible with

    .venv/bin/python -B research/astra-completion-37-check.py
