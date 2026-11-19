# Complex structure of the actual central path: a hot domain and two obstructions

Round 35. **The cold common-domain and growth obligations remain open for
growing primes.** This note gives four rigorous structural results, without
another small-field elimination or floating branch tracking:

1. The inherited mixed-product Mellin norm gives a nonvanishing holomorphic
   actual reciprocal pair on the **uniform hot complex region**
   `Re tau > 0, 1024 < |tau| < n`, with `|m(tau)| <= 4/sqrt(n)`.
2. A general weighted-barrier theorem gives an explicit cold local complex
   disk. For the full actual Paley tangent space, its isotropic Hessian-ball
   certificate necessarily has width of order `n^(-1/2)` at fixed floor.
   This is a limitation of that certificate, not a singularity theorem.
3. At the **actual prime 13**, the marked spectrum, marked logarithm, and
   normalized marked spectrum cannot be Pick functions in either direction.
   Exact five-term jets give negative 3-by-3 Pick determinants. Thus a
   Stieltjes/complete-Bernstein representation of these particular quantities
   cannot supply the missing continuation theorem.
4. If square-family marked logarithms do extend over a common cold–hot
   domain, their imaginary parts must grow at least polynomially somewhere
   in that domain. Bounded-sector or positive-real continuations therefore
   cannot hold uniformly for that family. This sharpens the existing
   extension-versus-growth obstruction to a **phase-growth obstruction**.

Inputs read: [round 33](complex-floor-33.md),
[round 34](complex-branches-34.md),
[independent audit, Sections 1–5](parallel-audit-34.md), and
[round-34 acceptance](repair-response-34-acceptance.json).
The finite prime-17 and square-25 half-plane theorems are retained, not
strengthened to a growing-field statement. The hot theorem below uses the
arithmetic mixed-product inequality already proved in
[large-smoothing](large-smoothing.md); it is not a new audit of its sheaf proof.

## 1. A uniform actual hot complex domain

Write `q=2n+1`, and retain the complexified rank-squared Mellin norm
`||.||_N` from large-smoothing. The precise inputs needed here are

\[
 \|f\|_\infty\le\|f\|_{\mathcal N},\quad
 \|x\|_{\mathcal N}\le\sqrt{2+1/n},\quad K\mathbf1=0,
 \qquad
 \left\|K\prod_{j=1}^{m}f_j\right\|_{\mathcal N}
 \le 2m^2\prod_j\|f_j\|_{\mathcal N}\quad(m\ge2\text{ even}).       \tag{1}
\]

Here the `f_j` belong to the negative-type span, and `n>=1024`.
The mixed version of (1), not just its diagonal specialization, follows
from the multilinear expansion and absolute coefficients in that note.
The same proof permits complex coefficients. This finite-dimensional
complex normed space is complete.

**Theorem 1.** For each actual field order with `n>1024`, put

\[
 \Omega_n=\{\tau:\Re\tau>0,\ 1024<|\tau|<n\}.
\]

The actual real stationary pair on `(1024,n)` extends to a holomorphic,
coordinatewise nonzero reciprocal pair on `Omega_n`. Its marked logarithm,
with the actual real normalization, satisfies

\[
                 |m_q(\tau)|\le4/\sqrt n.                        \tag{2}
\]

In particular, any fixed bounded domain compactly contained in
`{Re tau>0, |tau|>1024}` is a common domain with this bound for all sufficiently
large fields, both primes and squares.

**Proof.** Write `V=sqrt(n) v`. The exact scaled fixed-point map is

\[
 \mathcal T_\tau(V)=b_\tau(V_0)x+K\sqrt{V^2+4\tau},\qquad
 b_\tau(z)=\sqrt{4+z^2/n}-n^{-1/2}\sqrt{z^2+4\tau}.                \tag{3}
\]

All square roots here use their binomial series about the indicated
nonzero constant, with the holomorphic square root of `tau` positive on
the positive real axis. On `||V||_N<=R=6`, set `s=|tau|` and
`z=R^2/(4s)=9/s`. The series converge absolutely since `s>1024`.
Because `|sqrt(tau/n)|<1` and its argument lies between `-pi/4` and `pi/4`,

\[
 |2(1-\sqrt{\tau/n})|\le2.
\]

The correction and derivative estimates for the scalar term are

\[
\begin{split}
 |b_\tau(V_0)|&\le2+\epsilon(n,s),\\
 \epsilon(n,s)&=
 \frac{R^2}{n(2+\sqrt{4-R^2/n})}
 +\frac{R^2}{\sqrt n(2\sqrt s+\sqrt{4s-R^2})},\\
 |b_\tau'(V_0)|&\le
 \beta(n,s)=\frac{R}{n\sqrt{4-R^2/n}}
                 +\frac{R}{\sqrt n\sqrt{4s-R^2}}.                 \tag{4}
\end{split}
\]

These follow by rationalizing the two square-root differences. Factoring
out `2 sqrt(tau)` reduces the complex estimate to
`Re sqrt(1+w) >= sqrt(1-|w|)` for `|w|<1`.

For `c_l=|binom(1/2,l)|`, define

\[
 S_2(z)=\sum_{l\ge1}(2l)^2c_lz^l
       =\frac{z(2-z)}{(1-z)^{3/2}},\qquad
 S_3(z)=\sum_{l\ge1}(2l)^3c_lz^l
       =\frac{z(4-2z+z^2)}{(1-z)^{5/2}}.                         \tag{5}
\]

By (1), the nonlinear term in (3) has norm at most `4 sqrt(s) S_2(z)`.
Expand the difference of two powers into its `2l` mixed products to get
Lipschitz constant at most `4 sqrt(s) S_3(z)/R`. Thus the entire map has
image bound and Lipschitz constant

\[
\begin{split}
 B&=(2+\epsilon(n,s))\sqrt{2+1/n}+4\sqrt s S_2(9/s),\\
 L&=\beta(n,s)\sqrt{2+1/n}+(4\sqrt s/6)S_3(9/s).                 \tag{6}
\end{split}
\]

Every term is decreasing in `n,s>=1024`. For the sums, this follows
termwise from their positive coefficients and powers `s^(1/2-l)`.
At `n=s=1024`, rigorous Arb evaluation gives

\[
       B<5.13<6,\qquad L<0.78<1.                               \tag{7}
\]

The iterates from zero converge uniformly, with a uniform geometric
rate, to a holomorphic fixed point on `Omega_n`. On the real interval,
the roots in (3) are the positive real roots, and the known uniqueness
of the real fixed point identifies it with the actual stationary path.
The coordinate formulas

\[
 A_i=(\sqrt{v_i^2+4w_i}+v_i)/2,\qquad
 B_i=(\sqrt{v_i^2+4w_i}-v_i)/2
\]

are holomorphic and satisfy `A_i B_i=w_i`, where `w_0=1` and
`w_i=tau/n` otherwise. Thus no coordinate vanishes. The mean and sector
identities hold by the identity theorem. Finally

\[
 m_q=\operatorname{arsinh}(V_0/(2\sqrt n)),\qquad
 |m_q|\le\frac{3}{\sqrt n\sqrt{1-9/n}}<\frac4{\sqrt n},
\]

using the analytic branch near zero. This proves the theorem.

This domain does not reach any fixed cold floor below 1024. It supplies
both obligations only within the hot region, and gives no propagation
across its missing disk. No Picard convergence assertion in a cold
complex domain has been made.

## 2. A quantitative local theorem for any positive weighted barrier

Let an affine real spectral space be parametrized near its positive
stationary row `u*` by `u=u*+B xi`, where `B` has full column rank `d`.
At a real floor `a>0`, the weights are `w_0=1`, `w_i=a/n` otherwise.
The objective is `sum w_i log u_i`. Define

\[
 H=\sum_i w_i\frac{B_i^TB_i}{(u_i^*)^2},\qquad
 v_i=H^{-1/2}B_i^T/u_i^*,\qquad
 L_* =\max_i\|v_i\|_2,\quad M=\max\{1,L_*\}.                    \tag{8}
\]

The transpose convention in (8) makes each `v_i` a real column vector.
The complex continuation uses the bilinear `v_i^T z`, and the bounds
use the ordinary Hermitian Euclidean norm. Stationarity and normalization
give

\[
 \sum_i w_i v_i=0,\quad \sum_i w_i v_iv_i^T=I,
 \quad\|v_0\|_2\le1.                                          \tag{9}
\]

**Theorem 2.** The actual stationary row has a unique continuation in
the ball `||z||_2<=1/(8M)` for

\[
       |\tau-a|<a/(32M),\qquad z=H^{1/2}\xi.                    \tag{10}
\]

The continuation is holomorphic and all spectral coordinates are nonzero.
In particular the guaranteed disk

\[
       |\tau-a|<\frac{a}{32\sqrt{\max\{1,n/a\}}}               \tag{11}
\]

always works. This theorem applies to either actual normalized Paley
sector, at every positive floor.

**Proof.** Put `delta=(tau-a)/a`, `e_0=0`, `e_i=1` otherwise, and use
the fixed-point map

\[
 \Psi_\delta(z)=z+
     \sum_i\frac{w_i(1+\delta e_i)v_i}{1+v_i^Tz}.               \tag{12}
\]

Its value at zero is `-delta v_0`. On the stated ball,
`|v_i^Tz|<=1/8`. The matrix with columns `sqrt(w_i)v_i` is a coisometry
by (9); consequently sandwiching a diagonal complex multiplier between
it and its transpose has operator norm at most the largest multiplier.
It follows that

\[
 \|D\Psi_\delta(z)\|
 \le (1+|\delta|)(1-1/8)^{-2}-1
 \le17/49.                                                    \tag{13}
\]

For clarity, the first inequality follows by splitting
`1-(1+delta e_i)/(1+v_i^Tz)^2` into the unperturbed difference and
the `delta` term, and summing the absolute binomial series.
The center displacement is at most one quarter of the ball radius.
Thus the self-map ratio is at most `1/4+17/49=117/196<1`.
Banach iteration gives uniqueness in this ball and holomorphic dependence.
All relative coordinates remain within `1/8` of one. Positive real
parameters give the actual row by strict concavity and uniqueness.
The projection bound `w_i ||v_i||^2<=1` gives
`M<=sqrt(max{1,n/a})`, proving (11).

For Paley, multiply the normalized row by `sqrt(W(tau)/n)` to recover
the actual row. `W=1+(n-1)tau/n` has no zero in (10). The opposite row
is `w_i/A_i`, so the full reciprocal pair and its marked logarithm also
continue on this disk.

### The isotropic local certificate necessarily loses dimension

Let `ell_i=w_i ||v_i||^2`. They are the diagonal entries of a rank-`d`
orthogonal projection. Thus

\[
 \sum_i\ell_i=d,\quad \ell_0\le1,\qquad
 L_*^2\ge\frac{n(d-1)}{a(n-1)}.                                \tag{14}
\]

The full even plus Paley tangent space has `d=floor(n/4)`:
the plus multiplier has `n/2-1` positions, inverse pairs contribute
one dimension each, and the self-inverse nonzero position contributes
one exactly when `n` is divisible by four. Hence at fixed `a`, (14)
and the upper bound in Theorem 2 show `M=Theta_a(sqrt(n))`.
The radius specified in (10) is therefore `Theta_a(n^(-1/2))`.

This lower bound holds at the actual stationary point without knowing
its coordinates. It explains why a direct full-Hessian isotropic-ball
argument cannot yield a common cold tube. A direction-sensitive method,
a genuine symmetry reduction, or a different norm could do better.
In particular (14) is **not** a bound on the distance to an actual
singularity, and does not rule out a half-plane continuation theorem.

## 3. An exact actual-prime obstruction to Pick/Stieltjes structure

A Pick function here means a holomorphic map from the whole upper
half-plane into its closure, with the specified real analytic germ on
the positive axis. The corresponding negative class reverses the sign.
This condition is different from being holomorphic on the right
half-plane, or having positive real part there.

For such a function `f`, real analytic at `a`, write
`f(a+h)=sum c_j h^j`. A necessary condition is

\[
                 (c_{i+j+1})_{0\le i,j<k}\succeq0
                 \quad\text{for every }k.                    \tag{15}
\]

Here is the kernel justification, to specify exactly the criterion
being used. The upper-half-plane Pick kernel
`(f(z)-overline(f(w)))/(z-overline(w))` is positive semidefinite.
Cayley transformation reduces this to the Schur kernel
`(1-s(z)overline(s(w)))/(1-z overline(w))` in the unit disk: multiplication
by `s` is a contraction on the Hardy space since `|s|<=1`, so `I-M_s M_s*`
is positive. Real analytic continuation across `a` permits derivatives
and limits of the kernel at `a`. Its power-series coefficients are
exactly `c_{i+j+1}`; derivative evaluation, or finite differences followed
by a limit, proves (15). No claim that local positivity of the imaginary
part on a small half-disk alone implies (15) is used.

Use the already accepted actual prime-13 cubic, with `tau=6+h` and
the physical root `x(0)=0`:

\[
 (6+5\tau)x^3+(\tau-6)x^2-(24+8\tau)x+24-4\tau=0.
\]

Its `x` derivative at the base point is `-72`, so its Taylor jet is
uniquely determined without following any other algebraic branch.
The three quantities tested are

\[
 m=\tfrac12\log(1+5h/36)+\log(1+x),\quad
 A_0=\sqrt{1+5h/36}(1+x),\quad -u_0=-1-x.                       \tag{16}
\]

For the third quantity the constant is irrelevant to every test.
Their exact coefficients `c_1,...,c_5` are

| Quantity | `c1` | `c2` | `c3` | `c4` | `c5` |
|---|---|---|---|---|---|
| `m` | `1/72` | `-1/5184` | `1/279936` | `-17/13436928` | `29/67184640` |
| `A_0` | `1/72` | `-1/10368` | `1/746496` | `-29/23887872` | `6407/15479341056` |
| `-u_0` | `1/18` | `-1/162` | `17/23328` | `-37/419904` | `1/93312` |

All three have positive `c1` and positive leading 2-by-2 determinant,
but their 3-by-3 determinants are respectively

\[
 -\frac{26639}{1754956051230228480},\qquad
 -\frac{54271}{3327916660110655488},\qquad
 -\frac1{12694994583552}.                                      \tag{17}
\]

Thus none is Pick. Their positive derivatives exclude the negative
Pick class. Equivalently, `m`, `A_0`, and `u_0` each fail both classes.
The replay also supplies exact rational vectors with negative quadratic
forms, not just determinant signs.

This rules out a Stieltjes representation of any of these quantities
(Stieltjes functions are in the negative Pick class), and a complete
Bernstein representation of `A_0` or `u_0` (those are Pick functions).
It also rules out adding a real constant to repair these representations.
It does not exclude arbitrary parameter changes, other spectral
observables, positive-real structure on a different domain, or the
already proved right-half-plane holomorphy of the prime-13 marked log.
The obstruction is on the **actual** branch: it only uses its uniquely
determined jet at the positive equal-weight point.

## 4. A phase-growth obstruction for the actual square family

The round-33 obstruction can be strengthened when one tries to obtain
growth from a sector condition. Fix a connected bounded domain `D`
containing the real interval `[a,T+1]`, with `0<a<1`, `T>1024`.
Suppose the actual `m_q` has a single-valued holomorphic extension on `D`.
Choose a regular connected `D_0` compactly contained in `D` and containing
that interval. Let `omega` be the harmonic measure of `E=[T,T+1]` at `a`
in `D_0` slit along `E`.

**Phase lemma.** With a constant depending only on these fixed domains,

\[
 \sup_{D_0}|m_q|\le C(1+B_q),\qquad
                   B_q=\sup_D|\Im m_q|.                        \tag{18}
\]

If `B_q` is infinite the assertion is vacuous. Otherwise apply the
positive-real-function disk estimate to
`F=B_q+i(m_q-m_q(T))`. Its real part is nonnegative and `F(T)=B_q`.
For a disk centered at a point `z_0`, Cayley transformation gives

\[
 |F(z)-i\Im F(z_0)|
 \le\frac{1+r}{1-r}\Re F(z_0),\quad |z-z_0|\le rR.
\]

A finite chain of overlapping disks in `D`, followed by a finite cover
of the compact closure of `D_0`, gives `|F|<=C B_q` there. The value
`m_q(T)` is bounded, indeed `O(q^(-1/2))`, by the actual hot theorem.
This proves (18). If `B_q=0`, the open mapping theorem makes `m_q`
constant and (18) follows directly.

For squares `q=r^2`, the actual theta value gives, eventually, any
fixed positive lower bound `delta` smaller than
`(1/2)log(2/(1+a))` for `m_q(a)`. The hot interval gives
`sup_E |m_q|<=6/sqrt(q)`. The two-constants argument on `D_0` now yields

\[
 \delta\le(6q^{-1/2})^\omega
                   [C(1+B_q)]^{1-\omega},
 \quad\text{hence}\quad
 1+B_q\ge c q^{\omega/[2(1-\omega)]}.                          \tag{19}
\]

Consequently a common square-family extension would require polynomially
large **unwrapped argument** of `A_{q,0}=exp(m_q)` somewhere in `D`.
This is a lower bound on the analytic logarithm's imaginary part, not
merely a statement about the principal argument modulo `2pi`.

In particular a common extension with `Re A_{q,0}>0`, or with its image
in any fixed sector admitting a bounded-argument logarithm, is impossible
for all sufficiently large squares. Its logarithm normalized on the
real axis would have bounded imaginary part, contradicting (19).
More generally, `B_p=p^{o(1)}` on such a common prime domain would,
by (18), discharge the growth obligation on `D_0` and yield the cold
marked decay. This is a sufficient **prime** condition, not an established
prime property.

The conclusion remains a disjunction for squares: either the required
single-valued extension fails, or its unwrapped phase is large. It does
not locate a branch point of any fixed field and does not contradict
the accepted square-25 half-plane theorem.

## 5. Replay, route comparison, and remaining scope

Run from the repository root:

```sh
.venv/bin/python -B research/parallel-complex-structure-35.py \
  > research/parallel-complex-structure-35-certified.jsonl
```

Seven records: three exact actual-prime Pick obstructions, the exact
physical-jet identity, one Arb hot-contraction bound, exact cold-ball
constants, and a success summary. The proof of the uniform statements
is in Sections 1, 2, and 4; the finite records check their explicit
constants and the exact obstruction. They are not Lean kernel proofs.

| Route considered | Result | What it does not provide |
|---|---|---|
| Complex Picard in the inherited Mellin norm | Actual uniform hot domain, contraction, and small marked log | Any common cold–hot domain |
| Full-Hessian isotropic barrier continuation | Explicit cold disks with nonzero reciprocal coordinates | Uniform width: trace forces this certificate's scale to shrink |
| Pick/Stieltjes/complete-Bernstein marked representation | Excluded on actual prime 13 by exact jets | Does not exclude plain right-half-plane holomorphy |
| Positive-real/bounded-phase growth control | Sufficient on a prime common domain; impossible uniformly for squares | Neither prime hypothesis has been proved |
| Searching larger-field eliminants or floating branch tracks | Not used | No claim of an actual right-half-plane branch point |

The new positive uniform domain remains hot. The prime target still needs
a common domain reaching every chosen cold floor, and controlled complex
growth there. Fixed-field extension, real analyticity, real derivative
bounds, and this explicit shrinking local disk do not discharge those
obligations. No README, ledger, other research prefix, commit, push, or
external message is part of this work.
