# Quadratic signed scatter and an obstruction to the first nested repair

Round 35, 2026-11-18. Ordinary theta, actual Paley fields.

**The all-prime good-proposal theorem remains open.** This round proves
two restricted arithmetic results, using only the first three nested
fields whose joint law was established in [round 32](joint-law-32.md).

* A root-reset square profile has a sharp, dimension-independent signed
  spill: for fixed real t, the spill of `(x-t)^2` tends to
  `3+t^2+2 sqrt(2)|t|`. There is an explicit finite-field upper formula.
  The absolute-coherence estimate for the same profile grows like sqrt(n).
* Adding the **first nonscalar nested direction** `L(xy)` to `L(x^2)`
  does not improve the attainable normalized mark. The exact limiting
  maximum in this three-parameter affine family is `mu/sqrt(2)`.
  This includes arbitrary field-dependent coefficients. When mu=1 and
  tau<1, every positive feasible pair in this family has a strictly
  positive limiting conic gap, explicitly (18) below.

The second assertion is an actual-Paley obstruction to a specified
construction, not an abstract counterexample. It extends the scalar
direction obstruction to a genuinely nested direction. It does **not**
exclude deep Picard proposals, general functions of the three fields,
or the nonlinear clipped reflection of round 34. The first assertion
is a signed-scatter estimate for a specified profile, **not** a proof
that the true clipping deficit has that profile.

## 1. Accepted starting point and arithmetic scope

The [round-34 acceptance record](repair-response-34-acceptance.json) and
[independent audit, section 6](parallel-audit-34.md) retain the exact
formula

\[
 R_\sigma d=\sigma Kd-(Ed)1-
       \frac{2\ell_\sigma}{a_\sigma}\langle\ell_\sigma,d\rangle,
 \qquad R_\sigma=2L_\sigma-I.                         \tag{1}
\]

Here q=2n+1, E is the empirical mean over n cyclic coordinates,
`P_sigma=(I-J+sigma K)/2`, `ell_sigma=P_sigma e_0`,
`a_sigma=(n-1-sigma)/(2n)`, and
`L_sigma=P_sigma-ell_sigma ell_sigma^T/a_sigma`. Assume a_sigma>0.
The real even setting and normalization are exactly those of
[round 34](astra-conic-primal-34.md). In particular L kills 1 and e_0.

The actual arithmetic fields used here are

\[
 x=\sqrt n K e_0,\qquad y=K(x^2),\qquad z=K(xy).        \tag{2}
\]

We use the established compact law

\[
 X=\sqrt2\operatorname{Re}J,\quad
 Y=(\operatorname{Tr}S+\operatorname{Tr}T)/2,\quad
 Z=(\operatorname{Re}\operatorname{Tr}U+
                       \operatorname{Re}\operatorname{Tr}V)/\sqrt2,
                                                               \tag{3}
\]

where J is Haar on the unit circle, S,T are independent Haar SU(2),
and conditional on J the independent U,V have determinants J^{-1},J.
The Y variable is independent of (X,Z). Both the **pointwise compact
membership with O(q^{-1/2}) aliases** and the **fixed-polynomial
equidistribution** in round 32 are needed. A weak law alone would not
give the upper bound in section 3.

No assertion is made about `K F(x,y,z)` for another F. We never replace
the law of a later clipped field by (3). All asymptotic assertions below
hold through all primes q=1 mod 4 and also through the square controls
covered by the same law. Consequently neither result distinguishes
the prime endpoint from the square endpoint.

## 2. Root pinning and exact low-degree identities

Write h=1-1/n. Directly from K^2=I-J and K1=0,

\[
 x_0=-1/\sqrt n,\quad Ex=0,\quad Ex^2=h,\quad
 Kx=\sqrt n e_0-1/\sqrt n,\quad
 E(xy)=(-1+2/n)/\sqrt n.                              \tag{4}
\]

The last equality follows by moving K from x^2 to x in E[x K(x^2)].
Also L_sigma x=0: P_sigma x=sigma sqrt(n) ell_sigma.
Thus R_sigma x=-x and R_sigma 1=-1 exactly.

Two marked evaluations must be controlled before discarding the pinning
term. Symmetry of K gives

\[
 y_0=\sqrt n\,E x^3,\qquad z_0=\sqrt n\,E(x^2y).       \tag{5}
\]

Both are O(1), uniformly through these fields. For y_0, apply round-32
equidistribution to x^3, whose compact mean is zero, and add the exact
marked x_0^3/n. For z_0, apply it to x^2 y, whose compact mean is zero
by independence and EY=0; the omitted contribution is x_0^2 y_0/n.
The errors for these two fixed polynomials are O(q^{-1/2}). This argument
does not assume any bound on later exceptional modes.

For i!=0,

\[
 \begin{split}
 (R_\sigma x^2)_i
 &=\sigma y_i-h-\frac{\ell_{\sigma,i}}{a_\sigma}
                      (2/n-1+\sigma y_0),                 \tag{6}\\
 (L_\sigma x^2)_i&=\tfrac12(x_i^2-1+\sigma y_i)+O(q^{-1/2}),\\
 (L_\sigma(xy))_i&=\tfrac12(x_i y_i+\sigma z_i)+O(q^{-1/2}). \tag{7}
 \end{split}
\]

The errors are uniform in the bulk. Indeed the mark of P(x^2) is
`(2/n-1+sigma y_0)/2`; the mark of P(xy) is
`(x_0 y_0-E(xy)+sigma z_0)/2`. Both are O(1), while
`|ell_i| <= b_n=(1+sqrt(q))/(2n)` off the mark and a_sigma tends to 1/2.
This verifies rather than assumes the harmlessness of root pinning.

## 3. A sharp signed-spill theorem for square profiles

Fix t in R and set

\[
 d_0=0,\qquad d_i=(x_i-t)^2\ (i\ne0),\qquad
 S_\sigma(d)=\max_{i\ne0}(-(R_\sigma d)_i)_+.
\]

Resetting the root changes Rf only at the root, because R e_0=-e_0.
Consequently (6) gives the **exact bulk formula**

\[
 (R_\sigma d)_i=
   \sigma y_i+2t x_i-(h+t^2)
   -\frac{\ell_{\sigma,i}}{a_\sigma}(2/n-1+\sigma y_0).
                                                               \tag{8}
\]

Here is a finite-field upper bound containing no unknown stationary
quantity. Set

\[
 M_x=\sqrt{q/n},\qquad M_y=q/n+M_x/\sqrt n.
\]

The Jacobi bound gives |x_i|<=M_x on the bulk. The exact rank-two alias
in round 32 gives |y_i|<=M_y there. Therefore

\[
 \boxed{S_\sigma(d)\le
 t^2+h+2|t|M_x+M_y+
  \frac{b_n}{a_\sigma}|2/n-1+\sigma y_0|.}              \tag{9}
\]

Every quantity on the right is explicitly computable from the field.
Equation (5) shows it is
`3+t^2+2 sqrt(2)|t|+O_t(q^{-1/2})`. This is a uniform upper bound,
not a fitted rate. It is sharp in the limit:

\[
 \boxed{S_\sigma(d)\longrightarrow
                3+t^2+2\sqrt2|t|.}                    \tag{10}
\]

To prove the lower bound, choose X=-sign(t)sqrt(2) (either endpoint
when t=0), and Y=-2 sigma. These coordinates occur in the compact
support because X and Y are independent. Every neighborhood of that
support point has positive Haar mass, so equidistribution supplies
bulk coordinates approaching the maximizing value in (8). This uses
only a fixed continuous function of x,y, never a new projected field.

This is a concrete removal of the absolute-coherence sqrt(n) loss:
`Ed -> 1+t^2`, whereas `Gamma ||d||_1` is of order sqrt(n). By
homogeneity, replacing d by c d for c>=0 multiplies (9)--(10) by c.
For example, any fixed c<kappa/3 gives `S_sigma(c x^2)<=kappa` for all
sufficiently large fields.

**How it can be used, and the unsupplied step.** For an actual clipping
deficit d_actual, a decomposition

\[
 d_{\rm actual}=c\,1_{i\ne0}(x-t)^2+e,\quad e_0=0,
\]

gives the rigorous bound

\[
 S_\sigma(d_{\rm actual})\le c\,\text{RHS}(9)
                                  +\Gamma_{n,\sigma}\|e\|_1. \tag{11}
\]

This follows from (1) and the round-34 entry bound, valid also for
signed e. Such a profile approximation has **not** been proved for a
Picard deficit. In fact a squared profile is nonzero on nearly all
bulk points, while a clipping deficit has a zero set tied to the
proposal's positive slack. A fixed relative L1 fitting error would
still cost sqrt(n). Thus (10) is useful arithmetic information about
a specified profile; it is not offered as a completion of the requested
construction, and (11) alone is not counted as new uniform progress.

## 4. The first nonscalar nested correction cannot improve the mark

Consider the following completely explicit affine-sector proposals:

\[
 H_{q,\sigma}(\mu,a,b,c)=
 \mu1+(a\sqrt n-\mu)\ell_\sigma/a_\sigma
             +bL_\sigma(x^2)+cL_\sigma(xy).              \tag{12}
\]

They have mean mu, mark a sqrt(n), and the correct sector exactly.
The new direction here is L(xy), not a scalar function of x. All
coefficients are real, mu>0, and a>=0. The coefficients a,b,c may
depend arbitrarily on the field.

Equations (4)--(7) identify the bulk with

\[
 F_\sigma(X,Y,Z)=\mu+\sigma aX+
       \tfrac b2(X^2-1+\sigma Y)+
       \tfrac c2(XY+\sigma Z),                           \tag{13}
\]

with a pointwise error `O(q^{-1/2})(mu+a+|b|+|c|)`.

At the adverse endpoint X=-sigma sqrt(2), choose Y=+2 or -2.
Conditional on J=-sigma, the following two values of sigma Z occur:

\[
                  -3\sqrt2,\qquad 3/\sqrt2.             \tag{14}
\]

These are **actual points of the compact group**, not independent
unconstrained coordinates. If sigma=+, J=-1: choose U=V=-I_3 for the
first value and U=V=exp(i pi/3) I_3 for the second. Their determinants
are both -1. If sigma=-, J=1: choose U=V=I_3 for the first value of
sigma Z and U=V=exp(2 pi i/3) I_3 for the second. S,T=+I_2 or -I_2
give Y=+2 or -2 independently. Thus the two determinant constraints
are explicitly respected at all four corners, for either sign.

Minimizing (13) over just these four support points gives

\[
 \begin{split}
 C(\mu,a,b,c)=\mu-\sqrt2a+b/2-|b-\sqrt2c|
       +\begin{cases}-3c/\sqrt2,&c\ge0,\\
                         3c/(2\sqrt2),&c<0.
         \end{cases}
 \end{split}                                                   \tag{15}
\]

Put r=sqrt(2)c and u=b-r. The negative of the last three terms is
`|u|-u/2+r` when r>=0, and `|u|-u/2-5r/4` when r<0. Hence it is at
least `|u|/2+|r|`, which is at least `(|b|+|c|)/2`. We conclude

\[
 \boxed{\min_{i\ne0}H_{q,\sigma,i}
 \le \mu-\sqrt2a-\tfrac12(|b|+|c|)
                 +o(1)(\mu+a+|b|+|c|).}                \tag{16}
\]

The o(1) is uniform over all coefficients, not a fixed-coefficient
subsequence assertion. To see this, choose a nearest actual triple to
each of the **finite set** of four compact corners. All four distances
tend to zero by equidistribution and positive mass in every open
neighborhood. Evaluating (13) there incurs a uniform coefficient-linear
error. Add the uniform alias/pinning error already established. Thus
diverging coefficients cannot escape (16).

In particular nonnegativity forces a and |b|+|c| bounded when mu is
fixed, and gives `limsup a<=mu/sqrt(2)`. This is sharp. The choice b=c=0
and

\[
 a_q=\frac\mu{\sqrt n}(1+a_\sigma/b_n)
\]

is nonnegative everywhere, by |ell_i|<=b_n off the mark, and tends to
mu/sqrt(2). Therefore the supremal normalized mark in (12) tends
**exactly** to mu/sqrt(2).

### The obstruction has positive density, not just one bad coordinate

Fix a>mu/sqrt(2), and put delta=sqrt(2)a-mu. Choose
`epsilon=min(1/12,delta/(4a))`. Let nu_epsilon>0 be the minimum Haar
probability of the four open coordinate boxes of radius epsilon about
the corners above. This is a specified finite compact-group integral;
no numerical lower value for it is claimed. In one such box the change
in F from its center is at most
`epsilon(a+3(|b|+|c|))`. Consequently F is at most
`-3 delta/4-(|b|+|c|)/4` on the adverse box selected by b,c.
For all sufficiently large q, the uniform finite-field error and the
positive mass of each box give, **simultaneously for every b,c**,

\[
 \boxed{\frac1n\|(H_{q,\sigma})_-\|_2^2
 \ge\frac{\nu_\epsilon}{2}
              \left(\frac\delta2+\frac{|b|+|c|}{8}\right)^2.} \tag{17}
\]

The root is positive and contributes no negative part. Formula (17)
prevents interpreting (16) as a small exceptional set removable for free.
Its field threshold is not made effective here.

## 5. Consequence for explicit conic proposals

Take a positive pair p,q, one from each sign of (12), with mu=1.
The coefficients are free and field-dependent. By (16), their marked
product h_q=p_0 q_0/n has limsup at most 1/2. Opposite sectors give
E(pq)=1 exactly. Separating the mark and using Cauchy--Schwarz on the
bulk in the actual conic objective yields

\[
 D(p,q)\ge
 (\sqrt{1/W}-\sqrt{h_q})^2+
 (\sqrt{1-1/W}-\sqrt{1-h_q})^2.
\]

For 0<tau<1 the target marked fraction tends to 1/(1+tau)>1/2.
The last expression is decreasing in h up to that target. Thus

\[
 \boxed{\liminf D(p,q)\ge
       2-\frac{\sqrt2(1+\sqrt\tau)}{\sqrt{1+\tau}}>0.}   \tag{18}
\]

This holds even without a prescribed kappa floor, so such positive
trials cannot have D=o(kappa). At tau=1/20 the right side is strictly
between `.31126218139110774388555` and `.31126218139110774388556`.
Those endpoints are interval-certified constants, not finite-field
lower certificates or a bound for unrestricted conic optimization.

A later nonlinear repair of (12) leaves this restricted family. Neither
(17) nor (18) bounds its D_clip or its repaired conic objective. Likewise,
the depth40/48 proposals of round 34 are not represented by (12).

## 6. Attempts, failure boundaries, and acceptance material

The requested direction was to bound both D_clip and signed spill for
the zero-Picard construction uniformly over primes. I did not obtain
that theorem. The following routes were examined:

1. Replacing signed scatter by entrywise coherence reproduces the
   sqrt(n) loss at positive deficit density. It cannot use the finite
   success at depth40 as a uniform argument.
2. Low-degree polynomial scatter is genuinely better: (8)--(10) are
   sharp actual-field bounds. However fitting an actual hinge by such
   a profile leaves a signed residual whose L1 error must be controlled
   at the scale in (11). No growing-depth or hinge approximation theorem
   was established, so this route stops before the needed hypothesis.
3. Enlarging scalar polynomial repairs by the first new field xy does
   not solve positivity. The determinant-correct compact corners give
   the quantitative obstruction (16)--(18). This is the new obstruction
   proved here; it is not inferred from the earlier scalar result.
4. Using the rank-three law for further clipped fields was rejected:
   (3) contains no such closure statement. No source UI, HR, exact
   stationary input, or exchange of field/depth/floor limits is used.

The core deliverables are an **ordinary mathematical proof**, three exact
rational/symbolic audit records, and 42 floating diagnostics (three fields,
two signs, seven fixed tests). The two Arb records enclose the gap constant
and the genuine small-field calculation in section 7.
The diagnostics check exact finite identities and the pinning error;
they do not establish the asymptotic results. Their fixed rational
inputs are recorded in [inputs.json](astra-signed-repair-35-inputs.json).
No finite optimization is run. No interval certificate of a Picard
trajectory or of an actual large-field positive proposal is claimed.

```sh
.venv/bin/python -B research/astra-signed-repair-35.py --exact \
  > research/astra-signed-repair-35-exact.jsonl
.venv/bin/python -B research/astra-signed-repair-35.py --constants \
  > research/astra-signed-repair-35-constants.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-signed-repair-35.py --primes 9413 153649 --square-roots 97 \
  > research/astra-signed-repair-35-diagnostics.jsonl
```

All writes have the authorized `research/astra-signed-repair-35` prefix.
No README, ledger, other-prefix file, commit, push, or external message
was changed. Awaiting main-line mathematical review, in particular the
uniform-coefficient corner transfer and the limited applicability of the
square-profile scatter theorem. ETH26, prime-uniform good proposals,
actual source UI, and the HR/marked comparison route remain open. The
direct root route discussed next does not logically require UI or HR.

## 7. Main-line steering: averaged proposals and the weaker root finish

During this work main proposed the averaged raw-sector construction,
which can use positivity and balanced marks directly, without proving
D=o(kappa). I retain this as a distinct, weaker target. Main is auditing
the direct theta finish; the following identities and diagnostics were
checked here independently.

For the genuine unaveraged Picard orbit v_0=0, v_{t+1}=K phi_t,
`phi_t=sqrt(v_t^2+4w)`, put `mu_t=E phi_t/2` and `C_t=n mu_t^2`.
There is the exact energy identity

\[
 \|v_{t+1}\|^2-\|v_t\|^2=4W-4C_t.                   \tag{19}
\]

It does **not** justify C_t<=W at every step. A genuine Arb evaluation
at p=13, tau=1/20, starting at v_0=0 proves
`.22369121<C_1-W<.22369122`. This refutes an all-field all-depth claim;
it does not refute any fixed-depth prime-limsup estimate.

One possible scalar selection is elementary: over any fixed window
T<=t<T+L, some C_t is at most `W(1+T/L)`, by telescoping (19) and
`||v_T||^2<=4WT`. This supplies no positivity for the selected candidate.
Main's averaging avoids selecting such a time. Its subsequent
[sharp-budget proof](averaged-mark-35.md) is now the governing direct
construction target. Put

\[
 M_T=T^{-1}\sum_{t=1}^T\mu_t,\quad
 A_{\sigma,t}=(\phi_t+\sigma v_t)/2,\quad
 X_{\sigma,T}=M_T1+T^{-1}\sum_{t=1}^T P_\sigma A_{\sigma,t}.
                                                               \tag{20}
\]

Cauchy--Schwarz and (19) give exactly, with c=tau/n,

\[
 nM_T^2\le B_{n,T}:=W+
       \frac{(1-\sqrt c)^2(1-1/n)}T
       \longrightarrow1+\tau+1/T.                      \tag{22}
\]

Indeed `v_1=2(1-sqrt(c))Ke_0`, hence
`||v_1||^2=4(1-sqrt(c))^2(1-1/n)`. This improves the earlier displayed
coarser budget W(1+1/T). The row X/M_T has mean one
and the correct sector. The following endpoint decomposition isolates
the sign problem without a stationary source:

\[
 X_{\sigma,T}=
 \frac{\mu_T-\mu_0}{2T}1+
 \frac1{2T}\sum_{t=1}^T(A_{\sigma,t}+A_{\sigma,t-1})+
 \frac\sigma{4T}(v_T+v_{T+1}-v_1).                    \tag{21}
\]

To prove it, expand P A, use `Kv_t=phi_{t-1}-2mu_{t-1}1`, then
telescope `sum(v_{t+1}-v_{t-1})`. The first term is nonnegative because
phi_T>=phi_0 pointwise. The middle term is strictly positive. Only the
displayed terminal increment combination can produce a negative entry.
Its L2 energy bound alone still gives no uniform coordinate positivity.

I tested the specified one-step reflection of X/M_T, with tau=1/20,
kappa=1/1000 and T=16,32,64,128. These are **floating diagnostics**:

| order | T | repaired minimum, + | repaired minimum, - |
|---:|---:|---:|---:|
| 9413 | 64 | -.005958 | -.005762 |
| 153649 | 64 | -.006305 | -.006773 |
| 1000033 | 64 | -.007038 | -.006569 |
| 9413 | 128 | .000681 | .000935 |
| 153649 | 128 | .000110 | .000478 |
| 1000033 | 128 | .0000474 | .000232 |
| 97^2 | 128 | .001753 | -.306838 |

At p=1000033,T=128 the signed spills are about .00195262 and .00176785;
the absolute bounds are .0331986 and .0327157. The rows appear positive,
but do not meet the prescribed .001 floor. Direct theta would need
positivity only. Neither statement is interval-certified here. The
smallest positive margin decreases across these tests, so it is
particularly inappropriate to extrapolate fixed-T uniform feasibility.
At T<=64 these specified trials fail even positivity at the tested primes.

There are 32 additional records in
[averaged.jsonl](astra-signed-repair-35-averaged.jsonl) and
[averaged-large.jsonl](astra-signed-repair-35-averaged-large.jsonl).
They were not promoted to exact Fourier witnesses or counted as uniform
progress. The new ordinary proofs remain (9)--(10) and (16)--(18);
the positivity of (20), or of its marked-preserving repair, is open.

The revised target is now explicit: prove a prime-uniform nonnegative
completion of (20) preserving mean, sector, and mark for a sequence
tau->0, T->infinity, with the prime limit first. Fixed-depth marked
cancellation gives X_{+,T}(0),X_{-,T}(0)->1. The root theta bracket and
(22) then squeeze theta_+/sqrt(n) between the limits
`(1+tau+1/T)^(-1/2)` and `(1+tau+1/T)^(1/2)`. **No bound on D_clip,
D/kappa, UI, or HR is an additional requirement for this route.**
All that positivity work remains unproved here.

The square negative control must also be strengthened in view of
[main's sections 5 and 7](averaged-mark-35.md): at fixed tau+1/T<1,
the averaged minus prescribed mark asymptotically exceeds the exact
square maximum. Thus **every** nonnegative completion preserving its
mean, sector, and mark is impossible at sufficiently large square
orders. The saved round-34 square depth48 input already has the exact
finite obstruction: its minus mark is 267.60440179976... while the
maximum is exactly 195. This excludes all such completions of that
saved row, not merely the one reflected trial. It does not establish
the obstruction for each separate finite averaged diagnostic above,
and it does not imply unrestricted conic infeasibility.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-signed-repair-35.py --averaged \
  --primes 9413 153649 --square-roots 97 \
  > research/astra-signed-repair-35-averaged.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-signed-repair-35.py --averaged --primes 1000033 \
  > research/astra-signed-repair-35-averaged-large.jsonl
```
