# Small primal low layers need not screen the root

**Result: a sharp signed screening bound, a genuine-prime obstruction, and a
nonvanishing theorem for actual positive two-sector optimizers. No improved
all-prime energy estimate is proved.** The homogeneous low layer contributes a
signed amount `kappa_L` to the unit root contrast. It is also exactly the
high-to-low bulk current at the forcing boundary. A Schur estimate bounds it by
`(nu_L s_L)^(1/2)`, where `nu_L` is the root leverage through the low block and
`s_L` is the low response energy in that block. Actual primal positivity gives
an additional error bound and an explicit necessary angle condition. Small
**relative primal energy** alone does not make either bound small.

This failure is concrete. A 192-bit Arb certificate at the cubic width proves
that the actual prime `p=257,+` has a high cut retaining more than 99% of bulk
energy, while its low root contribution is below `-0.26`. At `p=29,-` the low
contribution is below `-1`, so the high contribution exceeds `2`. Thus this
signed decomposition is not a decomposition into fractions of a unit current.

More generally, even at fixed dimension and fixed width, actual positivity,
complementarity, both marks being maximal, and the two orthogonal sectors
**do not imply any uniform estimate**

\[
|\kappa_L|\le F(E_L/E),\qquad F(t)\longrightarrow0\quad(t\downarrow0).
\tag{A}
\]

An explicit six-coordinate family has `E_L/E -> 0` and
`kappa_L -> -9.6853279088...`. Its low block is one-dimensional, so it also
saturates the Schur bound. This is a theorem about the geometric assumptions;
the family is **not** a Paley family and does not have the Jacobi entry or
constant-diagonal conditions. It identifies a step that requires additional
arithmetic or additional control of the actual support.

The square comparison is not benign: at `389^2,+`, a numerical cut retaining
98.62% of energy has low root contribution about `-3.80`, even though only
8.35% of the response norm is low. The nearby prime `153649,+` has contribution
about `-4.16`. Norm concentration by itself does not separate these cases.

This follows [round 17](astra-preimage-17.md),
[round 16](astra-source-16.md), and [round 15](astra-cuts-15.md).
The [ETH statement](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/)
was checked on 2026-11-17 and concerns prime orders. Whenever the energy target
is mentioned below, the intended sign is the sign with larger **ordinary
theta**, not a sign inferred from a positive-width marker.

## 1. The root and the low harmonic layer

For a Paley field order `q`, put `n=(q-1)/2`. Use the actual normalized
reciprocal pair

\[
Q=J+rP+r^{-1}N,\qquad y=Qx,\qquad x,y\ge0,
\]

\[
x_0=a,\quad y_0=a^{-1},\quad x_i y_i=0\ (i\ne0),\qquad
\eta=\frac{r^2}{1-r^2},\quad\beta=\frac r{1+r},\quad R=N+\beta J.
\]

Here `P,N,J` are mutually orthogonal projections summing to the identity and
`J=11^T/n`. Write

\[
I=\{i\ne0:x_i>0\},\quad v=x_I,\quad C=R_{II},\quad
T=C+\eta I,\quad f=-aR_{I0},\quad Tv=f.
\]

For the actual high cut `U={i in I:v_i>tau}`, let `L=I\U`,
`E_U=||v_U||^2>0`, and `E_L=||v_L||^2`. The round-17 localized response is

\[
w=T^{-1}\frac{\mathbf1_Uv}{E_U},\qquad d=RE_Iw,\qquad -ad_0=1.
\tag{1}
\]

Coordinates on `I` are ordered as `U,L`. To avoid identifying a block with the
sector energy, use the notation

\[
T=\begin{pmatrix}A_U&B\\B^T&D\end{pmatrix},\quad
D=C_{LL}+\eta I,\quad S=A_U-BD^{-1}B^T.
\]

Both `D,S` are positive definite, and

\[
w_U=S^{-1}v_U/E_U,\qquad w_L=-D^{-1}B^Tw_U.
\tag{2}
\]

Define the two signed root contributions

\[
\boxed{\kappa_L=f_L^Tw_L=-a(RE_Lw_L)_0,\qquad
\kappa_U=f_U^Tw_U=1-\kappa_L.}
\tag{3}
\]

Deleting the low preimage changes the root contrast from `1` to `1-kappa_L`.
There is no positivity assertion for either term in (3).

For the round-17 mixed current, with `G_ij=-R_ij` off the diagonal,

\[
\mathcal F(U)=\sum_{i\in U,\ j\in\{0\}\cup L}
G_{ij}(x_jw_i-x_iw_j)=1.
\]

Its root part is `kappa_U`; therefore its bulk part is exactly `kappa_L`.
A negative `kappa_L` means that the signed bulk term cancels part of a root
term larger than one. This statement keeps the edge signs and makes no
positive-conductance or maximum-principle assumption.

## 2. A sharp Schur estimate with an actual-root ceiling

Set

\[
z=D^{-1}f_L,\qquad
\nu_L=f_L^TD^{-1}f_L,\qquad s_L=w_L^TDw_L.
\]

The low-block inner product gives the finite estimate

\[
\boxed{|\kappa_L|\le\sqrt{\nu_Ls_L}.}
\tag{4}
\]

If both factors are positive, define the signed correlation

\[
\rho_L=\frac{\langle D^{1/2}z,D^{1/2}w_L\rangle}
                   {\sqrt{\nu_Ls_L}}.
\]

Then `|rho_L|<=1`. In particular, to discard the low layer with root error at
most `delta`, one needs

\[
|\rho_L|\le\frac\delta{\sqrt{\nu_Ls_L}}.
\tag{5}
\]

A correlation tending to zero without this rate is insufficient when the
response energy grows. Alternatively, a small product `nu_L s_L` is sufficient.
Neither factor in this product is the discarded primal energy.

The actual rooted equation gives a useful finite upper bound on `nu_L`:

\[
\boxed{0\le\nu_L\le f^TT^{-1}f
=a^2(R_{00}+\eta)-\frac r{1-r^2}.}
\tag{6}
\]

For the inequality, extend a low trial by zero in the variational formula
`f^T T^{-1} f = max_h (2 f^T h-h^T T h)`. For the equality use `T^{-1}f=v`
and the root equation

\[
(Rx)_0+\eta a=\frac r{(1-r^2)a}.
\]

For Paley matrices `R_00=d_N+beta/n`, and the round-15 root bound shows that
the right side of (6) is `O(1)` at the cubic width. This bounds the root
leverage, but does not bound the growing `s_L`. The strict high-energy case
also gives

\[
f^TT^{-1}f-\nu_L=v_U^TSv_U>0.
\]

The coefficient one in (4) cannot be improved under the hypotheses used
here: equality holds whenever the two low vectors are proportional. The
actual positive family in Section 4 has a one-dimensional low layer and
realizes this equality while its primal low energy tends to zero.

## 3. What actual primal positivity adds

The actual positive primal vector relates the low root solve to the high
harmonic extension:

\[
f_L=B^Tv_U+Dv_L,\qquad
h_L:=D^{-1}B^Tv_U=z-v_L.
\]

Put

\[
\ell_L=v_L^TDv_L,\quad
\alpha_L=h_L^TDh_L,\quad
m_L=\langle D^{-1/2}B^Tv_U,D^{-1/2}B^Tw_U\rangle.
\]

Since `Dw_L=-B^Tw_U`,

\[
\kappa_L=-m_L+v_L^TDw_L.
\]

Cauchy--Schwarz and the triangle inequality yield the quantitative bounds

\[
\boxed{
\begin{aligned}
|\kappa_L+m_L|&\le\sqrt{\ell_Ls_L},\\
(|m_L|-\sqrt{\ell_Ls_L})_+
&\le |\kappa_L|\le |m_L|+\sqrt{\ell_Ls_L},\\
|\sqrt{\nu_L}-\sqrt{\alpha_L}|&\le\sqrt{\ell_L}.
\end{aligned}}
\tag{7}
\]

Here is where the **actual nonnegative low coordinates** give a priori control.
Since `0<=C<=I`, and since `0<v_i<=tau` on `L`,

\[
\boxed{\ell_L\le(1+\eta)E_L
\le(1+\eta)\tau\sum_{i\in L}v_i.}
\tag{8}
\]

At `tau=lambda/sqrt(n)`, the mass bound gives
`ell_L <= (1+eta)lambda`. The improved error term is therefore at most
`[(1+eta) E_L s_L]^(1/2)`. It is not controlled by `E_L/E` alone.

When `alpha_L s_L>0`, let

\[
\cos\theta_L=\frac{m_L}{\sqrt{\alpha_Ls_L}}.
\]

A necessary condition for `|kappa_L|<=delta` is

\[
\boxed{|\cos\theta_L|\le
\sqrt{\ell_L/\alpha_L}
+\frac\delta{\sqrt{\alpha_Ls_L}}.}
\tag{9}
\]

Equivalently, if `|cos theta_L|>=c` and `c sqrt(alpha_L)>sqrt(ell_L)`,
then

\[
\boxed{|\kappa_L|\ge
\sqrt{s_L}\bigl(c\sqrt{\alpha_L}-\sqrt{\ell_L}\bigr).}
\tag{10}
\]

This is a necessary obstruction to screening, with explicit tolerance. A
large harmonic response whose two high-to-low images remain aligned cannot
be removed merely because the actual low primal coordinates are small.
The matrices in (9) involve the prescribed root, the actual support, and the
actual high cut. They are not arbitrary sector vectors.

These estimates also explain why replacing the Schur complement by `A_U`
is not justified by the round-17 localization budget. That budget controls
`w^U-w^I`; it does not force the canonical response's contribution through
`L` to be small. The data below show substantial negative contributions from
the canonical response too.

## 4. No uniform screening from positivity and two sectors

The following construction proves the failure of (A), rather than merely
showing that a proposed proof of it has a loose step.

Fix `n=6`, `r=1/10`, and, for `epsilon>0` sufficiently small, set

\[
b=(1,1/2,1/4,\epsilon,0,0)^T,\quad
s=\mathbf1^Tb=7/4+\epsilon,\quad M=s^2/6.
\]

Let `z` be the smaller root, continuous near `epsilon=0`, of

\[
\frac{3r}{2}z^2-(rs+1+r^2)z
+r\bigl(\|b\|^2+s^2/2-2M\bigr)+(1+r^2)M=0,
\tag{11}
\]

and put

\[
q=(z,0,0,0,(s-z)/2,(s-z)/2)^T,
\qquad h=\frac r{1-r^2}\bigl(q-rb-(1-r)Jb\bigr).
\]

Equation (11) is exactly

\[
(1+r^2)(\langle b,q\rangle-M)
=r(\|b\|^2+\|q\|^2-2M).
\]

Consequently `h` has zero mean and `<h,b>=||h||^2`. Introduce two more
mutually orthogonal zero-mean vectors

\[
u=(0,1/4-\epsilon,\epsilon-1/2,1/4,0,0)^T,
\qquad t=(0,0,0,0,1,-1)^T.
\]

Both are orthogonal to `b,q,h`. Define

\[
N=\frac{hh^T}{\|h\|^2}+\frac{uu^T}{\|u\|^2}+\frac{tt^T}{2},
\qquad P=I-J-N.
\tag{12}
\]

These are orthogonal projections of ranks `3` and `2`, orthogonal to `J`,
and the definition of `h` gives exactly

\[
(J+rP+r^{-1}N)b=q.
\]

Now set `x=b/sqrt(z)`, `y=q/sqrt(z)`. Near zero, `z>0` and
`0<(s-z)/2<z`, so `x,y>=0`, both marks are maximal,
`x_0 y_0=1`, and their bulk supports are complementary. All coordinates of
`x_I`, `I={1,2,3}`, are strictly positive for `epsilon>0`; the inactive dual
coordinates `4,5` are strictly positive. These are actual unique anchored
optimizers: positive definiteness of `Q` and these KKT conditions suffice.
The reciprocal problem has `Q^{-1}=J+r^{-1}P+rN` and the same normalization.

The fixed actual threshold `tau=1/10` selects `U={1,2}`, `L={3}` for all
sufficiently small positive `epsilon`. Exactly,

\[
\frac{E_L}{E}=\frac{\epsilon^2}{5/16+\epsilon^2}\longrightarrow0.
\tag{13}
\]

The response (1), solved on `I={1,2,3}`, varies continuously down to zero:
its positive definite matrix has smallest eigenvalue at least the fixed
`eta`. At zero, the defining polynomial simplifies to

\[
480z^2-3792z+2233=0,
\qquad z=0.6408586209310024\ldots.
\]

The [Arb replay](astra-low-layer-18-certified.jsonl) encloses the exact
limiting root contribution in

\[
\boxed{-9.686<\lim_{\epsilon\downarrow0}\kappa_L<-9.685.}
\tag{14}
\]

For example, at `epsilon=10^(-6)`, `E_L/E<3.2e-12` but
`kappa_L<-9.68`. Continuity and (13)--(14) prove that no function in (A)
can hold uniformly over these actual pairs, even with fixed `n,r` and fixed
sector ranks. Because `L` has one coordinate, (4) is an equality in absolute
value. The canonical response has the same limiting low contribution:
its forcing differs from the localized forcing by `O(epsilon)` at fixed
`eta`.

At `epsilon=0` itself the coordinate `3` ceases to be active. The computation
in (14) is the limit of the positive-face solves with `epsilon>0`, **not** a
claim that this limiting zero coordinate belongs to the actual support.
The projectors vary with `epsilon`. They have nonconstant diagonals and are
not Jacobi/Fourier projectors, so this theorem does not refute a prime-only
screening assertion that uses those additional hypotheses.

## 5. Strict prime certificates at the requested width

The separate `--certificate` mode uses 192-bit Arb at the exact algebraic
width `r=p^(-1/3)`. It solves the active primal block, checks every strict
positive active coordinate and every strict positive inactive dual coordinate,
and checks the threshold. Thus the displayed supports are actual unique QP
supports, not supports inferred only from floating-point signs.

| Prime, sign | Scaled threshold `lambda` | `E_L/E` | `kappa_L` | `kappa_U` |
|---|---:|---:|---:|---:|
| `29,-` | 1 | 0.33307738 | -1.07316937 | 2.07316937 |
| `257,+` | 1/2 | 0.00908775 | -0.26441893 | 1.26441893 |

At `29,-`, `U={6,8}` and `L={1,2,12,13}`. At `257,+`,
`L={13,18,43,44,47,81,84,85,110,115}`. The complete supports and interval
values are in [the certificate JSONL](astra-low-layer-18-certified.jsonl).
The root bound (4) at the second example is `0.29446463...`, so its signed
correlation is about `-0.898` and the bound is fairly close to attained.

These certificates refute a nonnegative-current interpretation and, at
`p=257`, also refute the particular proposed estimate
`|kappa_L|<=sqrt(E_L/E_U)`. They do **not** refute every possible asymptotic
prime bound in terms of energy: the nonvanishing family of Section 4 is a
geometric counterexample, not an infinite sequence of primes. No claim about
the larger ordinary-theta sign is needed for these stated signed examples.

## 6. Square comparison and the subfield transfer

The numerical replay covers 32 sign/field cases, nine primes through
`153649` and seven squares through `389^2`, always at `r=q^(-1/3)`.
For `lambda=1`:

| Order, sign | `E_L/E` | `kappa_L` | Canonical low root contribution | `||w_L||/||w||` |
|---|---:|---:|---:|---:|
| `4001,+` | 0.02918 | -1.55451 | -1.17168 | 0.56364 |
| `9413,+` | 0.02465 | -1.36844 | -1.08371 | 0.55336 |
| `153649,+` | 0.01881 | -4.15531 | -3.47513 | 0.53279 |
| `153649,-` | 0.01792 | -3.54938 | -2.99100 | 0.51655 |
| `97^2,+` | 0.02127 | -1.79278 | -1.51492 | 0.15982 |
| `389^2,+` | 0.01375 | -3.80156 | -3.32813 | 0.08346 |

The canonical column uses `T^{-1}v/E` and the **same** low set. Thus the
cancellation is not created solely by changing the forcing in round 17.
At `153649,+`, `nu_L=0.05120...`, `s_L=2845.55...`, and
`rho_L=-0.34425...`; at `389^2,+`, these are `0.05798...`, `1541.57...`, and
`-0.40210...`. A moderately small correlation does not offset the large
response factor. These are finite observations, not asymptotic lower bounds.

There is an exact square mechanism. Let `q=ell^2`, take plus, and put
`H=(F_ell^times)^perp`, `k=|H|=(ell+1)/2`. The subfield calculation gives
`N 1_H=0`, so for any vector `z` supported on `L`,

\[
\boxed{-a(RE_Lz)_0
=a\sum_{i\in H\setminus\{0\}}(RE_Lz)_i
-\frac{a\beta k}{n}\sum_{i\in L}z_i.}
\tag{15}
\]

This does not assume the subfield lies in the high set. In the two square
plus rows displayed above, however, every bulk subfield coordinate is in
`U`, a checked finite fact. At `389^2,+`, with `z=w_L`, the two terms on the
right of (15) are about `-3.95589` and `+0.15433`. Thus the low response's
coupling to the high subfield, together with its mean correction, accounts
for its root contribution `-3.80156` even though its relative norm is small.

The identities and estimates (1)--(10) all hold over squares. The square
failure of the desired energy target at this exact moving width was already
proved in [round 15, Section 5](astra-cuts-15.md#5-square-controls-fail-the-target-at-this-exact-width).
The present comparison rules out using low-norm concentration as a proxy
for small signed current; it supplies no theorem separating the prime and
square currents.

## 7. Replay and remaining prime requirement

Files for this round are [the script](astra-low-layer-18.py),
[the 32 numerical rows](astra-low-layer-18-results.jsonl), and
[the five certificate rows](astra-low-layer-18-certified.jsonl).
The numerical replay verifies the root decomposition, harmonic equation,
Schur bound, actual-root leverage ceiling, positivity refinement, angle
bounds, three current levels per cut, and square transfer. Its largest
checked discrepancy is below `1.0e-11`; the largest input QP residual is
below `2.0e-11`. Those large-order supports are numerical, not interval
certificates. The five certificate rows comprise two strict prime cases and
three evaluations of the geometric family, including its limiting face.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-low-layer-18.py --large \
  > research/astra-low-layer-18-results.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-low-layer-18.py --certificate \
  > research/astra-low-layer-18-certified.jsonl
```

The remaining target is still `E=o(log_2^*p)` on the larger ordinary-theta
side. If one tries to reach it by removing the homogeneous low response,
this round specifies what needs proof: small `nu_L s_L`, or the signed
correlation rate (5), with the actual positive-primal obstruction (9) also
satisfied. Energy retention alone does not supply this. Even proving small
root deletion error would not automatically control the deleted low-block
residual or finish the energy estimate.

The new result is therefore a quantified obstruction to the screening step,
with exact prime certificates and a square control, rather than a reduction
of the all-prime exponent or a proof of Problem 26. No README, ledger, shared
script, or remote was edited.
