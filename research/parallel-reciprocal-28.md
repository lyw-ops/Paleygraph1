# Reciprocal stationary sources: a positive test and an autocorrelation dichotomy

Round 28, 2026-11-18. Ordinary theta / ETH Problem 26.

**Result.** The full positive stationary pair gives a positive definite
weighted compression with a source at the mark. Its source test has exact
value `1/sqrt(E_sigma)`, where `E_sigma` is the centered squared norm of the
actual spectrum. This is a test on the full sector, with weights supplied by
the actual opposite spectrum; it uses neither a guessed support nor an
exterior diagonal. A large norm forces a specific negative signed Paley
correlation in a test with a prescribed nonzero marked value. At the larger
natural energy scale, autocorrelation instead gives an explicit witness of
bounded energy and fixed mass margin in the relaxed defect program.

There is **no uniform prime bound** on the new source test here. The theorem
is a finite quantitative reduction/dichotomy, rather than a proof that
stationary norms stay bounded. The square stationary family fails the
source bound and gives the explicit autocorrelation witness. Thus the
algebra below cannot itself establish the prime conclusion.

## 1. Actual pair and the reciprocal weights

Let `q=1 mod 4`, `n=(q-1)/2`, `P=I-J`, and

\[
 P_\sigma=(P+\sigma K)/2,\qquad V_\sigma=\operatorname{im}P_\sigma,
 \qquad U_\sigma=\mathbb R\mathbf1+V_\sigma.
\]

We work with the **actual** positive stationary pair

\[
 A=A_\sigma=(\Phi(v)+\sigma v)/2,\quad B=A_{-\sigma},\quad
 AB=w,
 \quad w_0=1,\quad w_i=c=\tau/n\quad(i\ne0).
\]

Assume `0<tau<n`, and both sectors are nonempty. Write

\[
 W=1+(n-1)c,\quad a=\sqrt{W/n},\quad
 \sum A=\sum B=na,\quad A_0B_0=1,
 \quad x=A-a\mathbf1\in V_\sigma,
 \quad E=\|x\|^2=\|A\|^2-W>0.
 \tag{1}
\]

The two centered components are orthogonal, so
`E_++E_-=||v||^2`. In particular a bulk squared norm of `v` at least
`2R` forces `E_sigma>=R` for one sign. Also
`||A_(sigma,bulk)||^2=E_sigma+W-A_(sigma,0)^2`. The stationary point cap
`A_(sigma,0)<=a(1+sqrt(q))` keeps the last marked term bounded at fixed
floor, so this formulation covers the actual bulk norm regime in the
question.

All norms and convolutions below use counting measure, with no hidden
factor of `n`. Let

\[
 d_i=\frac{c}{aA_i},\qquad
 T=P_\sigma\operatorname{diag}(d)P_\sigma\big|_{V_\sigma},
 \qquad e_\sigma=P_\sigma e_0,\qquad b=\frac{1-c}{A_0}.
 \tag{2}
\]

The operator `T` is positive definite. Most importantly, the diagonal is
not an arbitrary positive weight: exactly

\[
 d=B/a-(b/a)e_0,\qquad
 P_\sigma d=-(b/a)e_\sigma,
 \qquad d_iA_i=c/a.
 \tag{3}
\]

For the two signs the diagonals also satisfy

\[
 d_{+,i}d_{-,i}=\tau/W\quad(i\ne0),\qquad
 d_{+,0}d_{-,0}=\tau^2/(nW),
 \quad \sum_i d_i=n-b/a.
 \tag{4}
\]

The anomalous product at the mark must be retained. Replacing (2)--(4)
by an arbitrary sector vector and a freely chosen weight loses the
stationary constraint.

The translation argument in [translation.md](translation.md) gives
`A_i<=A_0`, `B_i<=B_0`. Consequently

\[
 T\succeq d_* I_{V_\sigma},\qquad d_*=c/(aA_0)>0.
 \tag{5}
\]

This lower bound tends to zero with field size and is not a useful prime
gap by itself.

## 2. Exact positive source theorem

With no further hypothesis,

\[
 \boxed{\quad Tx=b e_\sigma,\qquad
 Q:=\langle x,Tx\rangle=(1-c)(1-a/A_0)<1.\quad}
 \tag{6}
\]

Indeed, `d x=c/a-a d`; project and use (3). Pairing with `x` proves the
second equality. It also proves `A_0>a` and `E>0`, since the source is
nonzero. This is a positive source equation, unlike the indefinite
half-angle equation in [stationary-secant.md](stationary-secant.md).

Let `mu_sigma` be the spectral measure of **T** at `e_sigma`. Then

\[
 \boxed{\begin{aligned}
 \int\lambda^{-1}\,d\mu_\sigma
     &=\frac{A_0(A_0-a)}{1-c},\\
 \int\lambda^{-2}\,d\mu_\sigma
     &=\frac{A_0^2E}{(1-c)^2}.
 \end{aligned}}                                           \tag{7}
\]

The first inverse moment is bounded by the stationary point cap; the
second is exactly the norm being investigated. Small unweighted
eigenvalues alone are insufficient: the source measure matters.

There is also an exact finite convex test:

\[
 \boxed{\quad
 \epsilon_\sigma=
 \min_{\substack{h\in V_\sigma\\h_0=A_0/(1-c)}}\|Th\|_2
 =E^{-1/2}.
 \quad}                                                    \tag{8}
\]

For every admissible `h`,
`1=b h_0=<Tx,h>=<x,Th><=sqrt(E)||Th||`. Equality is attained by the
explicit signed vector

\[
 h_*=T^{-1}x/E.
 \tag{9}
\]

Indeed `<b e_sigma,h_*>=<x,x>/E=1` and `Th_*=x/E`. This test includes
every spectral band. No support threshold, spectral gap, or declaration
of a small residual to be exactly zero is required. The test vector is
not claimed to be nonnegative. It obeys the finite bound

\[
 \|h_*\|\le\frac{aA_0}{c\sqrt E}.
 \tag{10}
\]

Thus a proposed prime inequality `||Th||>=eta` for all the marked tests
in (8) is explicitly violated whenever the actual `E>eta^(-2)`. Its
weight must be the actual `d`, with (3)--(4), rather than a prescribed
diagonal. Establishing such an inequality on primes remains open.

### The forced signed correlation

Put `z=d h_*`. Since `P_sigma=(P+sigma K)/2`, equations (8)--(9) give

\[
 \boxed{\quad
 \sigma\langle z,Kz\rangle=-\|Pz\|^2+2/E,
 \qquad (h_*)_0=A_0/(1-c).
 \quad}                                                    \tag{11}
\]

More generally the last term is `2||Th||^2` for any test `h`. A large
actual norm therefore produces a small **absolute** signed-correlation
deficit in a reciprocal weighted, marked test. This is an explicit
arithmetic target, not a claim that it has already been estimated at
prime order. Calling it a relative near-equality additionally requires
`E||Pz||^2 -> infinity`; that hypothesis is not used or inferred here.

One equivalent source-only formulation, valid for all `h in V_sigma`, is

\[
 b^2h_0^2\le E\,\|P_\sigma(dh)\|^2,
 \tag{12}
\]

with optimal constant `E`. A full operator gap for `T` is substantially
stronger than (12). The numerical comparison below distinguishes them.

## 3. Broad soft modes with an explicit amplitude threshold

The source equation also gives a quantitative extraction statement. Set
`Lambda=2Q/E` and `x_low=1_(0,Lambda](T) x`. Then

\[
 \|x_{\rm low}\|^2\ge E/2.
 \tag{13}
\]

Proof: the squared norm above `Lambda` is at most
`<x,Tx>/Lambda=E/2`. This argument retains the entire first moment in (7).
Let `y=x_low/||x_low||`. For each `0<theta<1`, put

\[
 H_\theta=\left\{i:A_i>
       \frac{\theta cE}{2aQ}\right\}.
\]

Since `y in V_sigma`, its quadratic form is just `sum d_i y_i^2`.
It follows that

\[
 \boxed{\quad
 \|y_{H_\theta^c}\|^2\le\theta,
 \qquad |H_\theta|\le\frac{2nWQ}{\theta\tau E}.
 \quad}                                                    \tag{14}
\]

The strict inequality in the definition of `H_theta` is immaterial for
the bound. The vector is generated from the actual source, not selected
from a compression because it has a small eigenvalue. Indeed
`(y)_0=<x_low,T x_low>/(b||x_low||)>0`. Its size need not be bounded below
uniformly in `q`. The vector `y` is signed; a nonnegative-cone compression
estimate cannot be applied to it without another argument.

This gives the correct **broad** width `O_tau(n/E)` when
`1<<E<<sqrt(n)`. It does not put a broad instability into a bounded union
of critical cosets. At `E` of order `sqrt(n)` it reaches the critical
cardinality scale, with an unspecified constant; existing sharp critical
coset theorems cannot simply be applied to that constant.

## 4. An explicit low-energy witness at the natural energy scale

The following additional branch is useful precisely when the source norm
is a sufficiently large fraction of its maximum natural scale. Let

\[
 N=\|A\|^2=E+W,\qquad C=A*A,
 \qquad Z_i=C_i/N.
 \tag{15}
\]

Stationary spectra are even. Hence `C_0=N`, `C>=0`, and
`C in U_sigma`, because convolution squares the inverse Fourier
coefficients and does not enlarge their support. In particular `Z` is
an exactly feasible anchored witness, with

\[
 \boxed{\quad
 Z_0=1,\qquad
 \nu(Z):=\frac{\sum Z}{\sqrt n}=\frac{\sqrt n W}{N},\qquad
 e_2(Z):=\frac{\|Z_{\rm off}\|^2}{\sqrt n}
 \le\nu(Z)-n^{-1/2}.
 \quad}                                                    \tag{16}
\]

The last bound is Young's inequality
`||A*A||_2 <= ||A||_1 ||A||_2`, followed by subtraction of the marked
square. No unknown optimizer is used in (15).

Fix `0<delta<1`. If

\[
 E+W\ge \frac{W\sqrt n}{1-\delta},
 \tag{17}
\]

then `nu(Z)<=1-delta` and `e_2(Z)<=1-delta`. Thus the ordinary normalized
relaxed defect of [pinned-penalty-24.md](pinned-penalty-24.md), with mark
one and mean `1+epsilon`, satisfies for `epsilon<delta/(1-delta)`

\[
 D_q(1,1+\epsilon)^2
 \ge\frac{[\delta-\epsilon(1-\delta)]^2}{1-\delta}.
 \tag{18}
\]

For the weighted defect use
`C_q=max_(i!=0) M_i h_i/sqrt(n)` from the pinned repair geometry.
Its energy obeys `e_w(Z)<=C_q e_2(Z)`, so divide the right side of (18)
by `C_q`. Existing repair formulas give `C_q=O(1)` (in fact tending to
`1/sqrt(2)`). This is a bounded-energy, fixed-margin witness of the
precise relaxed obstruction class, not just a high-norm reference row.

The finite dichotomy is now explicit. For any actual `E>=R` and fixed
`delta`, either (17) holds and (15)--(18) give the low-energy witness, or
(17) fails and (8)--(11) still give a marked reciprocal source test with
`||Th_*||<=R^(-1/2)`, together with the broad extraction (13)--(14).
The two branches can overlap as phenomena; (17) is a specified rule for
selecting the witness branch.

The autocorrelation branch alone does **not** cover `E=o(sqrt(n))`, even
when `E` diverges. This is a limitation of this construction, not an
exclusion of low-energy witnesses arising by another method.

## 5. Exact square control and why the source matters

There is an exact ordered-limit check on the **actual** stationary family.
At each fixed `q=r^2`, `r` odd prime, let `tau` decrease to zero first.
The theta bracket and compactness imply that every limit of the actual
plus spectrum is an optimal plus spectrum of mass `sqrt(n)`. The
[square uniqueness result](square-endpoint-uniqueness.md) identifies it as

\[
 A_+^0=\frac{r-1}{\sqrt n}\mathbf1_I,
 \quad |I|=(r+1)/2,
 \quad \|A_+^0\|^2=r-1.
 \tag{19}
\]

Consequently, at each such fixed square,

\[
 E_+\longrightarrow r-2,\quad
 \epsilon_+\longrightarrow(r-2)^{-1/2},\quad
 Z\longrightarrow\mathbf1_I.
 \tag{20}
\]

After this limit let `r` grow. The witness has
`nu(Z) -> 1/sqrt(2)` and `e_2(Z) -> 1/sqrt(2)`. Both branches have the
expected square obstruction: the source minimum goes to zero, while
autocorrelation recovers the subfield witness exactly. By contrast the
least-norm minus endpoint in the same note has squared norm
`2r/(r+1)`, so that endpoint's centered energy tends to one. This last
comparison does not identify the positive-floor stationary minus limit.
These statements do not
exchange the floor and field limits or assume a uniform stationary
support at positive floors.

Every displayed algebraic identity also holds on squares. A universal
proof of a positive lower bound in (8), using only `K^2=I-J`, would be
false. Prime-specific work must use the actual reciprocal weights and
their Paley arithmetic. Likewise the prime Fejer examples in
[square-order-control.md](square-order-control.md) provide no
counterexample to the exact source theorem: an arbitrary feasible Fejer
spectrum does not supply the opposite reciprocal sector and the marked
source identities (3)--(4).

## 6. Reproducible diagnostic and a change in the estimate to attack

Replay, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-reciprocal-28.py --inverse-n-floor --dense-max 5000 \
  > research/parallel-reciprocal-28.jsonl
```

The script solves the original smoothing equation and constructs both
spectra stably using `large=(u+abs(v))/2`, `small=w/large`. It checks the
actual reciprocal product, means, sectors, (4), (6), and (16). At these
orders it also constructs an independent dense cosine basis for the
inversion-even sector, diagonalizes `T`, checks both inverse moments,
exhibits (9), and tests (11), (13). Source Krylov spaces of dimensions
1, 4, 8, 16, 32 produce additional explicit marked test vectors. They
only give upper bounds on the source minimum; they are not declared
optimal unless compared to the independent dense formula.

All these computations are **floating point**. Neither the stationary
points nor their closeness to exact solutions are interval certified in
this replay. The theorem is proved algebraically above; the data are
normalization checks and finite diagnostics, not prime asymptotic
evidence.

The saved run contains 36 field/floor/sign rows. The largest stationary
residual is below `2.0e-12`, the largest positive-source equation error
below `4.0e-12`, and the largest relative second-inverse-moment discrepancy
below `5.2e-10`. The largest signed test identity discrepancy is below
`3.1e-10`. The diagnostic distinguishes the smallest eigenvalue of
`T` from the eigenvalue at which half the **actual source solution's
squared norm** has accumulated. A small eigenvalue need not carry much
of this source energy.

Some plus-sign rows, rounded to the displayed precision:

| Order | Floor | `E` | `lambda_min(T)` | Source-energy median eigenvalue | Exact source minimum | Autocorrelation mass `nu` |
|---:|---:|---:|---:|---:|---:|---:|
| `31^2` | `.005` | `28.5893` | `.0168601` | `.0168601` | `.187024` | `.744002` |
| `1009` | `.005` | `2.49790` | `.00387316` | `.423822` | `.632721` | `6.44096` |
| `61^2` | `.005` | `58.1817` | `.00872768` | `.00872768` | `.131101` | `.732313` |
| `4001` | `.005` | `2.75488` | `.00395905` | `.386168` | `.602489` | `11.9538` |
| `97^2` | `1/n` | `94.9413` | `.00527798` | `.00527798` | `.102630` | `.715022` |
| `9413` | `1/n` | `2.77568` | `.000254980` | `.390665` | `.600227` | `18.1718` |

At the last prime the full gap is **smaller** than at its square control,
while the root-specific source minimum is much larger. The global gap
therefore gives a misleading ranking of these finite cases. Dimension-32
source Krylov tests are within `3.14%` of the dense source minimum in all
36 rows; in the displayed square cases they agree to rounding precision.
This provides small, explicit numerical test vectors as well as the
dense inverse computation.

At `97^2`, floor `1/n`, autocorrelation has ordinary off-mark energy
`.699854` and mass `.715022`. Its numerical lower bound on the ordinary
relaxed defect squared at mean `1.01` is `.110292`. At `9413` the same
autocorrelation construction has mass greater than 18 and gives no
positive-margin witness. This is an actual test of the different branches,
not an assumption that every large norm is already at the threshold (17).

The practical target suggested by this reduction is (12), or the signed
weighted projection test (11), on the full actual reciprocal pair.
Replacing it by a uniform smallest-eigenvalue gap discards useful source
information. A proof of this prime estimate is still missing; neither
the old broad reserve penalty nor a rich-correlation estimate for an
arbitrary feasible profile supplies it.

Only files with prefix `research/parallel-reciprocal-28` were written.
No shared README/ledger edits, commits, or pushes were made.
