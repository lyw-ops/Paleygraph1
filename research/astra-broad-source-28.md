# Fixed forcing and exact mass do not make approximate reciprocity coercive

Round 28, 2026-11-18. Ordinary theta / ETH Problem 26.

**No bound on the actual broad prime source is proved here.** There is a
new obstruction to weakening its reciprocal equation: even after keeping
the prescribed forcing, nonnegative source, exact stationary source mass,
and exact stationary source value at the root, an **unnormalized total
absolute quadratic-reciprocity error tending to zero** does not bound the
source norm or its distance from the true source. This happens at every
sufficiently large prime, using the established logarithmic Fejer runs.

More precisely, for each fixed `tau>0`, there are even sources `g_p>=0`
with `v_p=f_p+K_p g_p` such that

\[
\begin{gathered}
\sum g_p=2\sqrt{nW}-\sum a,\qquad (g_p)_0=(g_p^*)_0,\\
\sum_i\left|v_{p,i}^2-g_{p,i}^2-2a_i g_{p,i}\right|\longrightarrow0,\\
\|\Phi(v_p)-a-g_p\|_2\longrightarrow0,\qquad
\|g_p\|_2,\ \|g_p-g_p^*\|_2\longrightarrow\infty.
\tag{1}
\end{gathered}
\]

Here `g_p^*` is the exact stationary source at the *same fixed floor*.
Also `(v_p)_0-(v_p^*)_0 -> 0`, and the scaled sources have vanishing
normalized `L1` distance. Consequently this construction preserves uniform
integrability if the actual sources have it. That last statement is
conditional; actual-prime uniform integrability is not established.

These are constructed static profiles, **not Picard iterates from zero**.
The source is not exactly `Phi(v_p)-a`. The two complementary Fourier rows
need not both be nonnegative, although their negative-part norms tend to
zero. Neither exact reciprocity nor the actual trajectory has been
refuted. In particular, (1) gives no counterexample to Problem 26.

The new feature relative to [the original Fejer obstruction](square-order-control.md)
and the [moving-width QP perturbations](astra-sampling-14.md) is the
simultaneous preservation of the **undamped, fixed-positive-floor** source
equation, its exact mass, and its root source. The proof measures total
absolute product error, not just a coordinate maximum. It also gives a
diverging distance from the true stationary point, regardless of whether
that point's own norm is bounded.

## 1. Setup and the scalar cancellation

Write

\[
\begin{gathered}
n=(q-1)/2,\quad w_0=1,\quad w_i=\tau/n\ (i\ne0),\quad W=\sum w_i,\\
a_i=2\sqrt{w_i},\quad b=2\sqrt{\tau/n},\quad
a=b\mathbf1+(2-b)e_0,\quad f=Ka,\\
K^T=K,\quad K^2=I-J,\quad K\mathbf1=0,\quad
|K_{ij}|\le\sqrt q/n.
\end{gathered}
\tag{2}
\]

Let `u*=Phi(v*)=a+g*`, `v*=Ku*` denote the exact solution from
[smoothing](smoothing.md). Put

\[
M=\sum u^*=2\sqrt{nW},\qquad G=M-\sum a=\sum g^*.
\tag{3}
\]

Every nonnegative source `g` of mass `G`, with `u=a+g` and `v=Ku`, obeys

\[
\sum_i(u_i^2-v_i^2-a_i^2)
=\frac{(\sum u)^2}{n}-4W=0.
\tag{4}
\]

Thus the **signed total** reciprocal equation is automatic after imposing
the correct mass. It cannot control `||g||`. The root forcing cancels in
the equivalent expansion of `||f+Kg||^2`: its cross term is
`2(2-b)(g_0-G/n)`, cancelling the root term in `2<a,g>`.

The stationary bounds used below require no prime asymptotics:

\[
\|v^*\|_1\le M,\quad \|v^*\|_\infty\le(\sqrt q/n)M,
\quad \|u^*\|_\infty=O_\tau(1).
\tag{5}
\]

The last follows from `u_i*^2=v_i*^2+a_i^2` and, eventually, `n>=tau`.
Moreover

\[
G/\sqrt n\longrightarrow
\gamma_\tau:=2(\sqrt{1+\tau}-\sqrt\tau)>0.
\tag{6}
\]

## 2. A root-preserving injection lemma

Suppose `h>=0` is real and even and satisfies

\[
\sum h=n,\qquad Kh=h-\mathbf1,\qquad
\|h\|_\infty\le H,\qquad \langle h,u^*\rangle\le M.
\tag{7}
\]

Assume `H=O(sqrt(n))`, with a fixed implied constant, and `n` sufficiently
large. Define

\[
c=\frac{G-g_0^*}{n-h_0},\quad
g^H_0=g_0^*,\quad g^H_i=ch_i\ (i\ne0),\quad
g_\delta=(1-\delta)g^*+\delta g^H\quad(0<\delta<1).
\tag{8}
\]

Then `c>0`, `c asymp_tau n^(-1/2)`, and `g_delta` is nonnegative and even,
has mass exactly `G`, and has root exactly `g_0*`. Put `u_delta=a+g_delta`
and `v_delta=K u_delta=f+K g_delta`. With constants also allowed to depend
on the bound for `H/sqrt(n)`,

\[
\boxed{\quad
\|u_\delta^2-v_\delta^2-a^2\|_1\le C_\tau\delta,
\qquad
\|\Phi(v_\delta)-u_\delta\|_2\le\sqrt{C_\tau\delta}.
\quad}
\tag{9}
\]

All squares here and below are coordinatewise. There are also the lower
bounds

\[
\begin{split}
\|g_\delta\|_2^2&\ge
\delta^2c^2(\|h\|_2^2-h_0^2),\\
\|g_\delta-g^*\|_2^2&\ge
\delta^2\{c^2(\|h\|_2^2-h_0^2)-2cM\}.
\end{split}
\tag{10}
\]

The state also satisfies

\[
|(v_\delta)_0-v_0^*|=O_\tau(\delta),\qquad
\|v_\delta-K\Phi(v_\delta)\|_2\le\sqrt{C_\tau\delta}.
\tag{11}
\]

**Proof, including finite computable constants.** Write

\[
e=a+(g_0^*-ch_0)e_0=b\mathbf1+D e_0,\quad z=Ke=DKe_0.
\]

Thus `u^H=e+ch`, `v^H=z+c(h-1)`. Both are the exact linear combinations
used in (8). Define

\[
\begin{gathered}
Q^H=(u^H)^2-(v^H)^2-a^2,\\
B=u^*e-v^*z-a^2+cv^*,\\
C_1=\|B\|_1+c\langle h,u^*-v^*\rangle,\qquad C_2=\|Q^H\|_1.
\end{gathered}
\tag{12}
\]

The second summand of `C1` is nonnegative. Exact expansion gives

\[
Q_\delta=
2\delta(1-\delta)\{B+ch(u^*-v^*)\}+\delta^2Q^H,
\quad
\|Q_\delta\|_1\le2\delta(1-\delta)C_1+\delta^2C_2.
\tag{13}
\]

These constants do not conceal `||g*||_2`. Indeed `c=O_tau(n^(-1/2))`,
`cH=O_tau(1)`, `|D|=O_tau(1)`, `||z||_infty<=|D|sqrt(q)/n`, and
`||z||_2<=|D|`. Using `u*-v*<=2u*` and (7),

\[
C_1\le bM+|D|u_0^*+
|D|\frac{\sqrt q}{n}M+4W+3cM=O_\tau(1).
\tag{14}
\]

For the other constant, expand the seed defect:

\[
Q^H=e^2-z^2-a^2+2ch(e-z+c\mathbf1)+2cz-c^2\mathbf1.
\]

Consequently

\[
\begin{split}
C_2\le{}&|e_0^2-4|+D^2
+2c\{bn+|D|H+|D|\sqrt q+cn\}\\
&+2c\sqrt n|D|+nc^2=O_\tau(1).
\end{split}
\tag{15}
\]

This proves the first part of (9). For nonnegative numbers `s,t`,
`(s-t)^2<=|s^2-t^2|`; apply this with `s=Phi_i(v_delta)` and
`t=(u_delta)_i`. The second part follows without dividing by the small
bulk floor. Contraction of `K` gives the last claim in (11).

For (10), retain the off-root coordinates. Positivity gives the first
bound. For the second, expand the squared distance and use
`<h_off,g*_off><=<h,u*><=M`; the remaining `||g*_off||^2` is nonnegative.
Finally `v_0^H=-D/n+c(h_0-1)=O_tau(1)` since `K_00=-1/n`.
This proves the root estimate. All statements are exact finite-dimensional
ones. No assumption on stationarity of an approximate numerical solve is
part of this proof. ∎

The root pin in (8) matters: simply using `c h` would preserve mass but
change `g_0`. It is also why the rank-one correction in `e` must be kept
in (12)--(15).

## 3. Prime Fejer profiles meeting the pairing condition

Here is the arithmetic input, recalled with its proof to specify its
scope. For every sufficiently large prime `p=1 mod 4`, set
`L=floor(log_2(p)/4)`. There is `t` in the nonzero squares, of order
greater than `2L`, with

\[
\chi(1-t^j)=1\qquad(1\le j\le L).
\tag{16}
\]

Expand the indicator of `chi(t)=1` and the `L` requirements in (16),
discarding zeros. Each nonconstant character product is the quadratic
character of
`t^epsilon product_(j in S)(1-t^j)`. If `S` is nonempty, a primitive root
of unity of order `max S` is a simple zero belonging to no smaller selected
factor; here `p>L`. If `S` is empty, the only nonconstant product is `t`.
Thus no such polynomial is a constant times a square. Its degree is at
most `1+L(L+1)/2`. The quadratic Weil bound gives

\[
\#\{t\text{ meeting all requirements}\}
=p/2^{L+1}+O(L^2\sqrt p+L^2).
\tag{17}
\]

Removing the `O(L^2)` elements with order at most `2L` leaves a positive
count for all sufficiently large primes. This is the same run lemma as in
[quadratic-fourth](quadratic-fourth.md), not a new character-sum estimate.
The only imported arithmetic estimate is the standard quadratic Weil
bound; an accessible statement is Theorem 1 of
[Alon--Goldreich--Hastad--Peralta, §4](https://web.math.princeton.edu/~nalon/PDFS/aghp4.pdf).
No conjectural equidistribution input is used here.

For frequency `i` let

\[
F_i=\frac1{L+1}\left|\sum_{j=0}^L i(t)^j\right|^2.
\]

Then `F>=0`, `sum F=n`, `KF=F-1`, `max F=L+1`, and exactly

\[
\frac{\|F\|^2}{n}
=1+2\sum_{j=1}^L(1-j/(L+1))^2
=\frac{2(L+1)^2+1}{3(L+1)}.
\tag{18}
\]

Translations commute with `K`. For each frequency shift `s`, set
`h^(s)=(T_s F+T_(-s)F)/2`, which is even. Its two summands are nonnegative,
so `||h^(s)||^2 >= ||F||^2/2 >= n(L+1)/3`. The mean of `h^(s)` over all
shifts is `1`. Hence at least one shift has
`<h^(s),u*><=sum u*=M`. This is the required pairing condition (7), not
an independence assumption about the actual solution.

Use that shift and (8) with `delta=L^(-1/4)`. Since `H=L+1=o(sqrt(n))`,
(9)--(10) give

\[
\begin{gathered}
\|Q_\delta\|_1=O_\tau(L^{-1/4}),\qquad
\|\Phi(v_\delta)-a-g_\delta\|_2=O_\tau(L^{-1/8}),\\
\|g_\delta\|_2,\ \|g_\delta-g^*\|_2
\ge c_\tau L^{1/4}\quad\text{eventually}.
\tag{19}
\end{gathered}
\]

This proves (1) through **all sufficiently large primes**, not just a
Dirichlet subsequence. The injected component has effective support of
order `n/L`, well above the critical `sqrt(n)` scale. Its off-root height
in the unscaled coordinates is `O_tau(L/sqrt(n))`; this is a dispersed norm
obstruction, not an individual large-coordinate obstruction.

## 4. What is retained, what is lost, and the UI target

Equation (4) holds exactly for these candidates, so the small absolute
defect in (19) has exactly cancelling signed total. They also have exact
complementary Fourier subspaces: for
`X_delta=(u_delta+v_delta)/2`, `Y_delta=(u_delta-v_delta)/2`, the forbidden
projections vanish and both sums equal `M/2`. However, positivity of both
rows is **not** asserted. Their failure of positivity is small only in
the following sense:

\[
\|(X_\delta)_-\|_2^2+\|(Y_\delta)_-\|_2^2
\le\tfrac14\|(Q_\delta)_-\|_1
\le\tfrac14\|Q_\delta\|_1.
\tag{20}
\]

Indeed a negative row occurs only when `|v_delta|>u_delta`, and the square
of its negative part is at most `(v_delta^2-u_delta^2)_+/4`.
Relative pointwise reciprocity, such as `max |Q_i|/a_i^2 -> 0`, is **not**
proved. Bulk weights of order `1/n` make that a much stronger condition.
The small absolute errors in (19)--(20) cannot be silently upgraded to it.

For the uniform probability measure on frequencies, put
`Z*=sqrt(n)g*`, `Z_delta=sqrt(n)g_delta`. Exact positivity and common mass
give the dimension-free comparison

\[
\mathbb E|Z_\delta-Z^*|
=\frac{\|g_\delta-g^*\|_1}{\sqrt n}
\le2\delta G/\sqrt n=O_\tau(\delta).
\tag{21}
\]

Thus the two families are uniformly integrable simultaneously as
`delta->0`. This is the usual stability of UI under an `L1` perturbation
tending to zero, and it remains valid for these varying finite probability
spaces. It does **not** assume or prove UI of the actual family.

More generally, for any fixed `1<r<2`, if the actual `Z*` have bounded
`L^r` norms, choose `delta=L^(-alpha)` with
`1-1/r<alpha<1/2`. Since `E h^r <= H^(r-1)` and the pinned root contributes
`O_tau(n^(r/2-1))`,

\[
\|Z_\delta-Z^*\|_{L^r}=o(1),
\qquad \|g_\delta-g^*\|_2\gtrsim_\tau L^{1/2-\alpha}\to\infty.
\tag{22}
\]

Likewise, a uniform actual entropy moment `E[Z* log(1+Z*)]` remains
uniformly bounded under this perturbation: convexity charges at most
`O_tau(delta log(1+L))` for the off-root seed, and its root contribution
is `O_tau(log(n)/sqrt(n))`. These observations explain why UI or a moment
below two could be a materially weaker actual-source target. They do not
settle whether any such target alone transfers fixed-depth marked parity;
no interchange of a truncation cutoff, time horizon, and field limit is
made here.

## 5. The signed transformed-residual tail escapes this obstruction

The proposed root/mass tail certificate asks for a different quantity.
For the trial `z=v_delta`, let `r=z-K Phi(z)` and `beta=-Kr`. Writing
`epsilon=Phi(v_delta)-u_delta`, the exact forcing equation gives

\[
r=-K\epsilon,\qquad \beta=(I-J)\epsilon.
\tag{23}
\]

In fact these examples have the much stronger **one-sided** estimate

\[
\epsilon_i\le
\delta\left(\frac{|D|\sqrt q}{n}+c\right)
=O_\tau(\delta/\sqrt n)\qquad(i\ne0).
\tag{24}
\]

To prove it, coordinatewise convexity gives
`epsilon<=delta[Phi(v^H)-u^H]`. On the bulk put `t=ch_i>=0` and
`k=(Ke)_i-c`. The triangle inequality in `R^2` gives

\[
\sqrt{(t+k)^2+b^2}-t-b
\le\sqrt{k^2+b^2}-b\le |k|.
\]

Use `|(Ke)_i|<=|D|sqrt(q)/n`. This uses nonnegativity of the injected
profile, not its norm. For centering, the Lipschitz property of `Phi`
and the common positive mass imply

\[
\begin{split}
\|\epsilon\|_1
&\le\delta\{\|v^H-v^*\|_1+\|u^H-u^*\|_1\}\\
&\le\delta\{\sqrt n|D|+2cn+3M\}=O_\tau(\delta\sqrt n).
\end{split}
\tag{25}
\]

Also `|epsilon_0|<=delta |v_0^H-v_0*|=O_tau(delta)`, since `u_delta,0=u_0*`.
Consequently, for every real `0<=k<=C sqrt(n)`, with fractional top sums
defined by linear interpolation,

\[
\boxed{\qquad
|\beta_0|=O_\tau(\delta),\quad
\max_{i\ne0}\beta_i=O_\tau(\delta/\sqrt n),\quad
\operatorname{Top}_{k}(\beta_{\rm bulk})
\le O_{\tau,C}(\delta).
\qquad}
\tag{26}
\]

The maximum-coordinate claim is an upper bound, not an absolute-value
bound. This distinction matters: the source defects can have larger
negative coordinates, which do not increase a positive-mass support
function.

For completeness, let `s=u_0*`, `d=s-b`, `B=M-nb`. The stationary
translation inequalities `X_i*<=X_0*`, `Y_i*<=Y_0*`
from [the exact translate budget](translation.md) imply
`b<=u_i*<=s` on the bulk. At fixed `s`, maximizing `<beta,u*>` subject
only to these coordinate bounds and the correct mass gives exactly

\[
d\left[\beta_0+
\operatorname{Top}_{B/d-1}(\beta_{\rm bulk})\right].
\tag{27}
\]

Here `sum beta=0` removes the baseline `b`, the root consumes one unit of
capacity `d`, and the remaining mass fills the largest bulk entries.
The bounds (5) give `2<=s<=C_tau`; hence `d` stays bounded above and
away from zero, and the top index is `O_tau(sqrt(n))`. Equation (26)
bounds (27) uniformly by `O_tau(delta)`, including its maximization
over the allowed root interval. The other scalar term is small too:

\[
2\sqrt W\frac{\sum\Phi(v_\delta)}{\sqrt n}-4W
=\frac{M}{n}\sum\epsilon=O_\tau(\delta).
\tag{28}
\]

Thus the complete scalar tail upper bound is `O_tau(delta)` on these
norm-divergent profiles. This is compatible with their marker being
close to the true marker. The obstruction in (1) **does not refute the
signed-tail relaxation**; that relaxation avoids the failed Euclidean
coercivity target.

For an actual Picard trial `z=v_t`, `t>=1`, there is an equally simple
identification, without reference to a stationary norm:

\[
\beta_t=(I-J)\{\Phi(v_t)-\Phi(v_{t-1})\}
=(I-J)(g_t-g_{t-1}).
\tag{29}
\]

It follows from `K v_t=(I-J)Phi(v_(t-1))`. What remains unproved is a
prime estimate on the top `O(sqrt(n))` **positive** centered activation
increment in (29), at the necessary growing horizon, together with its
scalar mass term. Bounds (24)--(26) were proved for the constructed chord
from the stationary point; they are not bounds for the actual trajectory.

## 6. Square controls and replay

The injection lemma is field-independent. In a square field `q=r^2`, let
`I` be the frequency annihilator of `F_r^*` and put

\[
h=(r-1)\mathbf1_I,\quad |I|=(r+1)/2.
\]

The exact subfield identity gives `Kh=h-1`, `sum h=n`,
`||h||^2/n=r-1`, and `max h=r-1=O(sqrt(n))`. An even translated average
again gives (7) and retains at least half the squared norm. The removal
of the root in (10) costs `c^2h_0^2=O_tau(1)`, while the full term is of
order `r`. The same construction therefore works on the square control,
for example with `delta=r^(-1/4)`. Nothing in the argument supplies the
false square-field actual-source bound. The prime Fejer construction is
broader and has a much smaller height than this subfield construction.

Replay:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-broad-source-28-check.py \
  > research/astra-broad-source-28-check.jsonl
```

The script checks prime orders `97,9413,153649` and square orders `49,9409`
at `tau=.05`, with four perturbation sizes per profile. It uses integer
sign masks and order/run tests, and checks both Fejer and square subfield
profiles. Small-field direct geometric sums independently check the
Fejer Fourier formula. The stationary solves and subsequent vector
computations are **floating point, not interval certificates**. The
measured base defect is retained in the expansion, so a converged
numerical base is never treated as an exact point in these checks.

All 28 perturbation checks passed. The five base residual norms are below
`2.001e-12`. The numerical base source norms at `9413,153649,97^2` are
about `1.9620,1.9766,9.0237`, respectively. The finite `C1,C2` from (12)
are bounded by `7.332,14.251` in the seven tested profiles. These small
finite degrees do not exhibit or certify an asymptotic divergence; that
conclusion is the theorem (17)--(19), not an extrapolation of the replay.
The replay also checks (23)--(24). Across these trials, the centered bulk
upper bound times `sqrt(n)/delta` is below `4.256`; the top
`ceil(sqrt(n))` sum divided by `delta` is below `4.272`. These are finite
diagnostics of the one-sided estimate, not actual-orbit tail certificates.

The remaining task is still a prime estimate for **actual** sources or
the actual growing-depth orbit. A proof that replaces their exact local
reciprocity by a qualitative total absolute defect, while retaining only
the constraints in (1), cannot supply uniform Euclidean coercivity.
An actual UI/entropy estimate would escape the need for that strong norm
bound, but its sufficiency and prime arithmetic input both require proof.
