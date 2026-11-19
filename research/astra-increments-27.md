# A prime cone gap for the actual increment source

Round 27, 2026-11-18. Ordinary theta / ETH Problem 26.

**The uniform actual-prime amplitude or small-ball estimate from Round 26
is not proved.** The new result is a restricted arithmetic theorem for the
true smoothing dynamics. The existing prime gap for a *flat* vector on a
critical bounded coset union extends to the norm of the compression on
**every nonnegative vector** on that union. No flatness of the input or
sign of the output is assumed. This supplies:

1. a loss-or-leakage inequality for actual consecutive increments, and a
   fixed two-step loss when their high-amplitude set stays in such a union
   and their activation change has small minority-sign norm;
2. a bound on the actual cumulative activation source, which is exactly
   nonnegative and needs no minority-sign hypothesis.

The second bound prevents an arbitrarily large source from building up on
one critical coset union while its exterior source norm stays bounded.
Both statements hold at arbitrary depths, including depths depending on
the prime. They do not control broad sources, or the order-two alternation
between two disjoint critical cosets. The square subfield and norm-one
examples show exactly where these restrictions matter.

The starting arithmetic result is [Round 20, §3](parallel-rectangle-20.md),
which improves the nonalternating branch of
[Round 19](parallel-cap-19.md). The proof below recalls its arithmetic
inputs and its deduction, then proves the new extension and actual-orbit
statements. In particular, this is not another derivation of the
conditional rate in [Round 26](parallel-activation-26.md).

## 1. Exact normalization and a finite matrix lemma

Let `q = 1 mod 4`, `n = (q-1)/2`, `m0 = n/sqrt(q)`, and let `K` be the real
Paley convolution on `G = Q^`, with

\[
 K=K^T,\qquad K^2=I-J,\qquad K\mathbf1=0,\qquad
 |K_{ij}|\le m_0^{-1},\qquad J=\mathbf1\mathbf1^T/n.
 \tag{1}
\]

The entry bound follows by compressing the norm-one additive Paley
operator to the nonzero squares and diagonalizing multiplicatively; it
holds at square orders as well. For a nonempty coordinate set `U`, put

\[
 m=|U|,\quad C=P_UKP_U\big|_{\mathbb R^U},\quad
 u=\mathbf1_U/\sqrt m,\quad r=m/m_0,\quad a=\langle u,Cu\rangle,
 \quad c=\sqrt{(r^2+a^2)/2}.
 \tag{2}
\]

Here `P_U` is coordinate restriction/projection, not a Fourier-sector
projection. Define

\[
 \Gamma(r,a)=\min\left\{1,
 c-\frac1r+\sqrt{2-\frac{2c}{r}+\frac1{r^2}}\right\}.
 \tag{3}
\]

**Positive-cone compression lemma.** For every `w >= 0` supported in `U`,

\[
 \boxed{\quad \|P_UKw\|_2\le\Gamma(r,a)\|w\|_2.\quad}
 \tag{4}
\]

This is a norm bound on a cone, not the full operator norm of `C`.

**Proof.** The entry bound gives `||C||_F^2 <= r^2`. In the orthogonal
decomposition `R u + u^perp`, write

\[
 C=\begin{pmatrix}a&b^T\\b&D\end{pmatrix}.
\]

Symmetry is essential here: `a^2+2||b||^2+||D||_F^2 <= r^2`. Consequently

\[
 \|Cu\|^2=a^2+\|b\|^2\le(r^2+a^2)/2=c^2.                 \tag{5}
\]

Normalize `||w||=1` and set `x=<u,w>=||w||_1/sqrt(m)`, so `0<=x<=1`.
The entry bound and then `||C||<=1` separately give

\[
 \|Cw\|\le r x,\qquad
 \|Cw\|\le\|Cu\|+\|C(w-u)\|
              \le c+\sqrt{2(1-x)}.                         \tag{6}
\]

Also `|a|<=r`, hence `c<=r`. The first expression in (6) increases in `x`
and the second decreases. Their crossing in `[0,1]` has value

\[
 c-r^{-1}+\sqrt{2-2c/r+r^{-2}}.
\]

Combining this maximum of the smaller expression with `||C||<=1` proves
(3)--(4), including `c=r` by continuity. No optimization over arbitrary
weights is left in this lemma. ∎

For example, at the exactly critical size `r=1`, if `|a|<=1-delta<1`,
then

\[
 c\le\sqrt{[1+(1-\delta)^2]/2}<1,\qquad
 \Gamma\le c-1+\sqrt{3-2c}<1.                              \tag{7}
\]

The last strict inequality follows by squaring
`sqrt(3-2c)<2-c`; its difference is `(1-c)^2>0`.
Continuity gives the same strict gap when `r` lies in a sufficiently
small fixed neighborhood of one. This extension would be false without
nonnegativity: a rank-one symmetric matrix `zz^T` with a flat, balanced
sign vector `z` has critical entry bound and `a=0`, but full norm one.

## 2. Where the prime-specific gap enters

**Arithmetic input, in the form needed here.** For every fixed integer
`R0 >= 1`, there are `eta>0`, `delta>0` and `p0`, independent of the cosets,
such that for primes `p>=p0`, a union `U` of at most `R0` cosets of one
frequency subgroup satisfying `||U|/m0-1|<eta` obeys

\[
 |\langle u_U,K_pu_U\rangle|\le1-\delta.                  \tag{8}
\]

Here is the deduction from the standard arithmetic estimates used in
Round 20. It also identifies the imported results precisely.

Write `s(x)=chi(1-x)` on `Q` and
`k(j)=q^(-1/2) sum_(x in Q) s(x)j(x)`, so `K_ij=k(i-j)/m0`.
The smooth cap

\[
 P_{M,\rho}(z)=((1+\rho z)/2)^M
\]

has inverse multiplicative Fourier coefficients `A_M`. The Jacobi
equidistribution theorem and the disjoint-parameter hypergeometric bound
give

\[
 |A_M(1)|\ll M^{-1/2}+p^{-1/4},\quad
 \|A_M\|_2\ll M^{-1/4}+p^{-1/8},\quad
 |A_M(x)|\le\sqrt{M/(2p)}+4/(p-1)\quad(x\ne1).             \tag{9}
\]

These are the consequences of
[Xi, Theorem 1.1 and Lemma 2.2](https://arxiv.org/pdf/1809.04286)
proved with the lift and binomial expansion in Round 20, §1. The other
input is the prime-field rich-intersection estimate, for a multiplicative
subgroup `B` of order comparable to `sqrt(p)`,

\[
 Y=(1-B)\setminus\{0\},\qquad
 \#\{z\ne1:|Y\cap zY|\ge L\}\ll p/L^2.                  \tag{10}
\]

It follows from the subgroup line-incidence estimate in
[Macourt--Shkredov--Shparlinski, Lemma 2.1](https://arxiv.org/pdf/1701.06192):
the equation `1-x=z(1-y)` becomes `alpha x+beta y=1`; grouping
`(alpha,beta)` by their two `B`-cosets, a cell with `N` solutions has
exactly `N` such ratios and intersection `N-1`. The rich-cell estimate is
`#{N>=L} << b^2/L^3`, and summing `N` on these cells gives (10).
The size hypotheses in that line estimate hold above a fixed cutoff
because `b` is comparable to `sqrt(p)`; smaller `L` is trivial.

For any complex `g` supported in `Q intersect vY`, `|g|<=1`, and
`||g||^2` comparable to `sqrt(p)`, split its multiplicative correlations
at height `L`. Equations (9)--(10) give, with unitary Fourier transform,

\[
 \frac{\sum_jP_{M,\rho}(k(j))|\widehat g(j)|^2}{\|g\|^2}
 \ll M^{-1/2}+M^{-1/4}\sqrt{\log(2L)}+\sqrt M/L+o_p(1).
 \tag{11}
\]

The identity correlation is treated separately. For the other terms use
`sum_(r<=L) r^2 << p log(2L)` with the `l2` cap bound, and
`sum_(r>L) r << p/L` with its off-identity pointwise bound. Take `L=M`,
then choose a large fixed `M`. Since
`1-P_(M,rho)(z)<=M(1-rho z)/2`, (11) excludes a relative additive Paley
Rayleigh defect tending to zero for these `g`.

To prove (8) by contradiction, suppose `|U|/m0->1` and
`<u_U,K u_U>->sigma`. Its within-set signed deficit tends to zero.
Choose an anchor `j0 in U` with no larger row deficit and put

\[
 f(x)=m^{-1}\sum_{j\in U}(j-j_0)(x)\quad(x\in Q),
\]

extended by zero to the additive field. Then `|f|<=1`, `f(1)=1`,
`||f||^2=n/m ~ sqrt(p)`, and its support is in the annihilator `B` of the
common frequency subgroup. Since the number of cosets is bounded,
`|B|` is comparable to `sqrt(p)`. Diagonalizing the compression of the
additive Paley operator `T` to `Q` gives

\[
 \langle f,(I-\sigma T)f\rangle=o(\|f\|^2),\qquad
 \sum_{x\in Q}(1-\sigma s(x))|f(x)|^2=o(\|f\|^2).        \tag{12}
\]

The first uses the anchor row; the second is exactly
`(1-sigma <u_U,K u_U>)||f||^2`. Pick `d` with `chi(d)=sigma` and reflect
by `Rf(x)=f(1-dx)`. The additive operators satisfy `TR=sigma RT`.
Discarding the part off `Q` loses at most `1+o(||f||^2)`, by the second
part of (12). Thus `g=1_Q Rf` is supported in `Q intersect d^(-1)Y`,
has squared norm comparable to `sqrt(p)`, and has additive Rayleigh
defect `o(||g||^2)` for sign plus. This contradicts (11). A sequence
argument supplies fixed constants in (8), uniformly for both signs.

Combining (7)--(8), and shrinking `eta` if necessary, proves the new
arithmetic conclusion:

**Prime positive-cone gap.** For each fixed `R0`, there exist
`eta>0`, `gamma<1`, and `p0` such that

\[
 \boxed{\quad \|P_UK_pw\|\le\gamma\|w\|
 \quad\text{for every }w\ge0\text{ supported in }U.\quad}  \tag{13}
\]

The sets `U` are exactly those in (8), for all primes `p>=p0`.
This conclusion allows arbitrary nonnegative weights, not only the flat
test used to establish (8). It is a *same-support* assertion; it gives
no bound below one on `P_T K P_U` for disjoint critical sets `T,U`.

## 3. A restricted theorem for true consecutive increments

Use unscaled variables throughout this section, including the true mark:

\[
 w_0=1,\quad w_i=\tau/n\ (i\ne0),\quad
 \Phi_i(v)=\sqrt{v_i^2+4w_i},\quad v_0=0,\quad
 v_{t+1}=K\Phi(v_t).
 \tag{14}
\]

Let `d_t=v_(t+1)-v_t`, `h_t=Phi(v_(t+1))-Phi(v_t)`, and `E_t=||d_t||^2`.
Exactly,

\[
 d_{t+1}=Kh_t,\qquad h_{t,i}=s_{t,i}d_{t,i},\quad
 s_{t,i}=\frac{v_{t,i}+v_{t+1,i}}{\Phi_i(v_t)+\Phi_i(v_{t+1})},
\]
\[
 E_t-E_{t+1}=L_t+\frac{(\sum_i h_{t,i})^2}{n},\qquad
 L_t=\sum_i(1-s_{t,i}^2)d_{t,i}^2.                         \tag{15}
\]

The mark and its mean contribution have not been removed. For a set `U`
having cone constant `gamma`, define its actual minority-sign norm by

\[
 b_t(U)=\min\{\|(h_t)_+\|_{2,U},\|(h_t)_-\|_{2,U}\}.
\]

Decompose `h_(t,U)` into either `|h_(t,U)|` or its negative, plus an
error of norm `2 b_t(U)`. Applying (13) to the absolute value gives

\[
 \boxed{\quad
 \|d_{t+1}\|\le\gamma\|d_t\|+2b_t(U)
       +\|h_t\|_{2,U^c}+\|d_{t+1}\|_{2,U^c}.
 \quad}                                                   \tag{16}
\]

One may keep a sharper version with the square root of
`[gamma ||h_t||_(2,U)+2b_t(U)+||h_t||_(2,Uc)]^2
+||d_(t+1)||_(2,Uc)^2`. Equation (16) is simpler to use. Neither statement
assumes the increments are flat. Conversely, low total loss alone does
not prove the three error terms in (16) are small.

**Two-step saturation theorem.** Fix `tau>0`, `R<infinity`, and `R0`.
Use the constants in (13), and write

\[
 \Delta=1-\gamma,\qquad
 \kappa_R=\frac{4\tau}{R^2+4\tau},\qquad
 \varepsilon=\min\{\Delta/4,\ \kappa_R\Delta^2/64\}>0.
 \tag{17}
\]

At any depth `t`, suppose a critical union `U` of at most `R0` cosets
contains the mark and has both of the following properties:

\[
 \sqrt n\,|v_{s,i}|\le R
 \quad(i\notin U,\ s=t,t+1,t+2),\qquad
 b_t(U)\le\Delta\|d_t\|/8.                                \tag{18}
\]

Then, for all primes beyond the fixed threshold,

\[
 \boxed{\qquad E_{t+2}\le(1-\varepsilon)E_t.\qquad}        \tag{19}
\]

There is **no amplitude bound inside `U`**, including at the mark.
The set may be chosen anew for different two-step blocks; within each
block the same set must satisfy (18). The depth has no restriction.

**Proof.** The low amplitudes off `U` imply

\[
 \|d_t\|_{2,U^c}^2\le L_t/\kappa_R,\qquad
 \|d_{t+1}\|_{2,U^c}^2\le L_{t+1}/\kappa_R.
\]

Assume `E_t>0` and, toward a contradiction,
`E_(t+2)>(1-epsilon)E_t`. Equation (15) implies
`L_t,L_(t+1)<epsilon E_t` and
`||d_(t+1)||/||d_t||>sqrt(1-epsilon)>=1-epsilon`.
But (16), (18), and `||h_t||_(2,Uc)<=||d_t||_(2,Uc)` bound the same ratio
by

\[
 \gamma+\Delta/4+2\sqrt{\varepsilon/\kappa_R}
 \le1-\Delta/2<1-\varepsilon.
\]

This is a contradiction. If `E_t=0`, all later increments vanish. ∎

Unlike a global amplitude assumption, (18) permits the entire potentially
large part of the field on `U`. Its cost is a precise arithmetic support
hypothesis and a radial-sign condition on the **actual** activation
change. These hypotheses are not established for general prime orbits.

## 4. The cumulative actual source is nonnegative without a hypothesis

There is an exact source-generated quantity to which (13) applies
unconditionally whenever its restriction to `U` is considered:

\[
 g_t:=\Phi(v_t)-\Phi(0)=\sum_{s<t}h_s\ge0,
 \qquad
 g_{t,i}=\frac{v_{t,i}^2}{\Phi_i(v_t)+\Phi_i(0)}.
 \tag{20}
\]

This positivity uses the prescribed start `v_0=0`; it is not a property
of each `h_t`. Put `f=K Phi(0)`. The true recurrence becomes

\[
 v_{t+1}=f+Kg_t,\qquad
 g_{t+1}=\Phi(f+Kg_t)-\Phi(0),\qquad
 0\le g_{t+1}\le|f+Kg_t|.
 \tag{21}
\]

For fixed `U` with cone constant `gamma<1`, set
`z_t=||g_t||_(2,U)`, `e_t=||g_t||_(2,Uc)`, `F_U=||f||_(2,U)`. Then

\[
 \boxed{\quad z_{t+1}\le\gamma z_t+F_U+e_t,\qquad
 z_T\le\frac{1-\gamma^T}{1-\gamma}F_U
             +\sum_{t<T}\gamma^{T-1-t}e_t.\quad}          \tag{22}
\]

This follows directly from (21), the cone gap on `g_(t,U)`, and
`||K||<=1` on its exterior part. It includes all nonlinear feedback and
all marked terms. No exact stationary point or eigenvector is substituted
for the orbit.

When `n>=tau`, the forcing is exactly

\[
 f=2(1-\sqrt{\tau/n})Ke_0,\qquad
 F_U\le2\sqrt m/m_0=O(p^{-1/4})\quad(m\asymp m_0).        \tag{23}
\]

Thus, if the **exterior** cumulative source norm is at most `B` through
an arbitrary horizon, its part on `U` is at most

\[
 z_T\le\frac{B+O(p^{-1/4})}{1-\gamma}.                    \tag{24}
\]

The full source and iterate norms are then bounded independently of the
prime: use `||g_T||<=z_T+e_T` and `||v_(T+1)||<=2+||g_T||`.
More locally, whenever `z_(t+1)>=z_t`, (22) forces

\[
 e_t\ge(1-\gamma)z_t-F_U.                                \tag{25}
\]

An unbounded critical-coset component that is still growing therefore
requires an unbounded exterior source component. This is stronger than
assuming a bounded total norm in advance: it rules out a concentrated
instability on `U` from bounded exterior forcing. It does not bound the
exterior norm, and hence does not handle a broad instability.

## 5. Square checks and the order-two escape

At `q=r^2`, let `I` be the frequency annihilator of `F_r^*`, of size
`h=(r+1)/2`. Fourier multiplication gives exactly

\[
 K\mathbf1_I=\mathbf1_I-(h/n)\mathbf1,\qquad
 \|P_IK u_I\|=1-\frac1{r-1}\longrightarrow1.              \tag{26}
\]

Thus no uniform `gamma<1` in (13) can hold on squares, even for a single
coset and a positive flat input. The unscaled actual source does build
up on this set; the replay below measures it without choosing an
arbitrary initial vector.

The distinct order-two example must also be retained. Let
`B={x:x^(r+1)=1}`, `b=r+1`, let `H=B^perp`, `h=(r-1)/2`, and let `T` be
the order-two coset of `H`. With
`sigma=(-1)^((r+1)/2)`, the exact positional identity is

\[
 s(x)=\sigma d(x)\quad(x\in B\setminus\{1\}),\qquad
 d(x)=x^{(r+1)/2}\in\{1,-1\}.
\]

Consequently

\[
 K\mathbf1_H=\sigma(\mathbf1_T-(h/n)\mathbf1),\qquad
 K\mathbf1_T=\sigma(\mathbf1_H-(h/n)\mathbf1).             \tag{27}
\]

In particular `||P_T K u_H||=1-1/(r+1)->1`, although the input and output
are on different cosets. Their union has size asymptotic to **`2m0`**, so
it is outside the critical window of (13). A hypothetical prime twisted
pair would evade this theorem in exactly the same way. Neither positive
cumulative sources nor repeated application of (13) closes that gap.
The two-anchor cross-ratio estimates of
[Rounds 20--23](parallel-crossratio-21.md) remain relevant and unproved
at their required uniform strength. The projective change of variable
is already part of that earlier route; it is not a new estimate here.

## 6. Replay and what it does and does not certify

Run:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-increments-27-check.py \
  > research/astra-increments-27-check.jsonl
```

For a single frequency subgroup `U=H`, with positional annihilator of
size `b`, the flat Rayleigh value is the exact rational number
`a=b^(-1) sum_(x in B)s(x)`, and `r=sqrt(q)/b`. The checker encloses
(2)--(3) with 160-bit Arb, using integer finite-field signs. These are
rigorous finite constants for the proved matrix lemma. For example:

| Prime | `b` | Exact `a` | Cone bound from (3), rounded upward |
|---:|---:|---:|---:|
| 4177 | 72 | `-1/72` | `0.872316` |
| 40801 | 200 | `23/200` | `0.976436` |
| 252001 | 500 | `-57/500` | `0.970972` |

At `p=1153,b=32` and `p=10193,b=98`, this particular finite formula only
returns the trivial bound one. Those are not claimed as certified gaps.
The file also records an independent exact full compression norm for
single subgroups: its eigenvalues are the positional `B`-coset sign
means. This stronger finite calculation is not used to assert a uniform
prime theorem.

The checker independently constructs dense `K` at prime orders 61, 97
and square orders 49, 121; it tests (4)--(6) on 4,800 nonnegative vectors
and 48 supports. It verifies the positional norm-one twists with integer
signs and cross-checks (26)--(27) by FFT at roots 31, 97, 193.

There are also two **interval certificates of the actual first pair** in
(19), at `p=61,b=10` and `p=4177,b=72`. At `t=0` the source change is
nonnegative exactly, so the minority norm is zero. Arb encloses the
original recurrence through `v_3`; the off-support scaled endpoints are
bounded by the integers 4 and 5, respectively. Rational upward cone
bounds are `775430883/1000000000` and `436157729/500000000`. With the
corresponding exact rational epsilon from (17), both enclosures verify
`E_2 < (1-epsilon)E_0`. The enclosed energy ratios are about `.102226`
and `.125961`. These use the finite matrix bound, so do not require an
effective value of the asymptotic prime threshold or critical window.

The actual-orbit replay runs 257 steps at `tau=.05`, for the five primes
above and the three square orders. It evolves increments using the exact
secant recurrence, checks `sum h_s=g_t`, independently recomputes the
original recurrence, and tests (16) and (22) at every step. These orbit
computations are **floating point, not interval trajectory certificates**.
The maximum cumulative-source identity error is below `1.1e-14`, the
maximum recurrence discrepancy below `1.3e-14`, and no tested inequality
violates its stated tolerance.

Some actual-source measurements at depth 256, in unscaled norms:

| Order | `||g_U||` | `||g_(Uc)||` | `g` energy in `U` | Increment energy outside `U` |
|---:|---:|---:|---:|---:|
| 40801 | .13221 | 1.97091 | .00448 | .99505 |
| 252001 | .09340 | 1.97750 | .00223 | .99799 |
| 97² | 8.94915 | .98689 | .98798 | .06946 |
| 193² | 11.21357 | 1.04109 | .99145 | .02062 |

Here `U` is the root-containing frequency subgroup specified above for
primes, and the subfield annihilator for squares. At the last two square
rows `h_(t,U)` has no negative coordinates in the floating replay. No
analogous sign or coset concentration is inferred for arbitrary primes.
The tested prime increments are broad relative to these cosets, and the
right side of (16), divided by `||d_t||`, exceeds one. The data therefore
do **not** claim to verify the hypotheses of (19) in a useful prime
regime. Very small late residuals also make relative diagnostics
sensitive to numerical errors; the mathematical statements do not rely
on them.

## 7. Precisely what remains

The new unconditional prime statement is the cone gap (13); (16) and
(22) then apply to the true orbit with their displayed errors. A new
restricted actual-increment theorem is (19), under exactly (18).

There is still no proof that low activation loss forces the high set
into a bounded critical coset union, that the source minority-sign norm
is small there, or that the cumulative exterior norm in (22) stays
bounded. The sparse extraction and collision-size hypotheses in
[Round 26](astra-extraction-26.md) cannot simply be inserted as conclusions
about these increments. Broad supports and the disjoint order-two
alternation remain outside this result. None of the finite checks
supplies the missing uniform weighted amplitude estimate, and Problem
26 remains unresolved.

Only files with prefix `research/astra-increments-27` were written.
No shared campaign files, commits, or pushes were changed.
