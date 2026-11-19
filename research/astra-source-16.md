# Prime source propagation at the cubic width

**Result: an exact prime-only propagation theorem and a narrowed necessary
source obstruction; the required energy estimate remains open.** At
`r=p^(-1/3)`, the additive translates of the positional lift of **any
nonzero actual bulk cut**, or of its uncentered signed source, span the
entire mean-zero space on `F_p`. No smaller subspace invariant under
additive translation contains that source. The proof uses cyclotomic
disjointness at the prime `p`, including the cubic field introduced by
the width. It does not assert full spark for the multiplicative Fourier
matrix of order `(p-1)/2`.

The uncentered source also has a dual witness with **unit root contrast**,
small samples on the entire actual support, and a controlled global norm.
Failure of the desired energy bound forces this witness to have full
additive translation rank `p`. These are necessary conditions, not an
energy upper bound.

There is a quantitative obstruction to using the new rank statement alone:
for every fixed `k`, infinitely many genuine primes admit a real,
inversion-even, pure Paley-sector vector whose positional lift has full
mean-zero translation rank but an additive convolution eigenvalue
`O_k(p^(-k))`. Already a six-point rational construction has an eigenvalue
`O(p^(-2))`, much smaller than the `p^(-2/3)` source scale. Square controls
have exact missing additive modes, and nonnegative bulk controls can have
translation rank only `3(sqrt(q)-1)`.

Thus the new prime input excludes **exact additive decoupling** as an
explanation of a bad actual source. A quantitative estimate still has to
use its prescribed supported preimage and actual optimality. Generic
signed-sector membership, inversion symmetry, and cyclotomic rigidity do
not provide the needed conditioning.

Starting points were [round 15](astra-cuts-15.md) and the
[moving-width estimate](parallel-complexity-14.md). The public
[ETH statement](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/)
specifies prime orders. All statements about the requested sign below
mean the sign with larger **ordinary theta**, without identifying it from
the positive-width marker.

## 1. An uncentered dual source test with no fitted mean

Keep the actual normalized reciprocal pair from round 15:

\[
Q=J+rP+r^{-1}N,\quad y=Qx,\quad x,y\ge0,
\quad x_0=a,\quad y_0=a^{-1},\quad x_i y_i=0\ (i\ne0).
\]

Let `I={i!=0:x_i>0}`, let `E_I` extend by zero, and set

\[
\eta=\frac{r^2}{1-r^2},\qquad \beta=\frac r{1+r},\qquad
R=N+\beta J,\quad C=E_I^*RE_I,\quad f=-aE_I^*Re_0,
\quad v=x_I,\quad E=\|v\|^2.
\tag{1}
\]

Since `N,J` are orthogonal projections with orthogonal ranges,
`0<=R<=I`, `R²<=R`, and `0<=C<=I`. Actual complementarity gives

\[
(C+\eta I)v=f.
\tag{2}
\]

Suppose `E>0`. Define the signed preimage and its global potential by

\[
w=\frac{(C+\eta I)^{-1}v}{E},\qquad d=RE_Iw.
\tag{3}
\]

Then the following finite-width conditions hold simultaneously:

\[
\boxed{\begin{aligned}
-a d_0&=1,\\
\|d_I\|=\|Cw\|&\le E^{-1/2},\\
\eta\|w\|&\le E^{-1/2},\\
\sqrt\eta\,\|d\|&\le\frac1{2\sqrt E},\\
Pd&=0,\qquad d=RE_Iw.
\end{aligned}}
\tag{4}
\]

For the first identity, `-a d_0=f^T w=1` by (2). The next two estimates
use the contractions `C(C+eta I)^(-1)` and
`eta(C+eta I)^(-1)`. Finally,

\[
\|d\|^2\le w^TCw
=E^{-2}v^T(C+\eta I)^{-1}C(C+\eta I)^{-1}v
\le\frac1{4\eta E}.
\]

The last step is `t/(t+eta)²<=1/(4eta)`. Unlike the centered witness of
[round 13](astra-energy-13.md), (4) has a root-only contrast. Its cost is
the retained mean component `beta J`; one must not call `d` a pure
opposite-sector vector. The displayed supported-preimage condition is
also essential.

The associated finite convex test is equivalent to the total bulk energy,
including both inverse density and centered response:

\[
\epsilon_I=\inf_{f^Tw=1}\max\{\|Cw\|,\eta\|w\|\},\qquad
\boxed{\frac1{2\sqrt E}\le\epsilon_I\le\frac1{\sqrt E}.}
\tag{5}
\]

The upper bound uses (3). For every admissible `w`,
`1=v^TCw+eta v^Tw<=2 sqrt(E) max(||Cw||,eta||w||)`, proving the lower
bound. This is a second-order cone problem once the actual support and
source are specified. Its constraints allow signed `w`.

Write `L_p=log_2^* p`. By round 15, `A=||Px||²=E+O(1)` at the requested
width. Consequently failure of `A=o(L_p)` produces a subsequence with
`E>=epsilon L_p`, for a fixed `epsilon>0`, and (4) gives

\[
-ad_0=1,\qquad
\|d_I\|=O_\epsilon(L_p^{-1/2}),\qquad
\|w\|=O_\epsilon(p^{2/3}L_p^{-1/2}),\qquad
\|d\|=O_\epsilon(p^{1/3}L_p^{-1/2}).
\tag{6}
\]

These estimates by themselves also hold over squares. The next section
adds an arithmetic constraint that does not.

## 2. The cubic width preserves prime cyclotomic rigidity

Let `p=1 mod 4` be prime, `n=(p-1)/2`, and

\[
F=\mathbb Q(\zeta_n),\qquad
\mathbb E=F(p^{1/3}).
\]

**Field lemma.** The polynomial `Phi_p` remains irreducible over
$\mathbb E$, and $[\mathbb E(\zeta_p):\mathbb E]=p-1$.

Here is a direct degree proof. Coprimality of `n,p` gives
`[F(zeta_p):F]=p-1` by the cyclotomic degree formula. The polynomial
`X³-p` is irreducible over **every abelian extension of Q**: if a root
lay in such an extension, its degree-three field over `Q` would be
Galois, whereas `X³-p` is Eisenstein and has nonsquare discriminant
`-27p²`. In particular it remains irreducible over both `F` and the
abelian field `F(zeta_p)`. Taking degrees in the two towers proves the
claim. This argument avoids assuming that $\mathbb E/\mathbb Q$ itself
is Galois. The proof only uses `p` not dividing `n`, so it also applies
to the coefficient field needed in the square controls below.
The underlying cyclotomic and Galois facts are in
[Sharifi, Chapter 6](https://math.ucla.edu/~sharifi/notes/algebra-ch06.html).

Choose the multiplicative characters `eta_i` of `Q=F_p^{×2}`. For a
frequency vector `u` define its **unnormalized positional lift**, extended
by zero to the additive field, by

\[
\mathcal L u(t)=
\begin{cases}
\sum_i u_i\eta_i(t),&t\in Q,\\
0,&t\notin Q.
\end{cases}
\tag{7}
\]

For an additive function `g`, write
`hat g(xi)=sum_t g(t) exp(2 pi i xi t/p)`.

**Prime propagation theorem.** If `u!=0` has coefficients in $\mathbb E$,
then

\[
\widehat{\mathcal L u}(\xi)\ne0\quad(\xi\ne0),\qquad
\widehat{\mathcal L u}(0)=n u_0.
\tag{8}
\]

Consequently its additive convolution matrix, equivalently the span of
its additive translates, has rank

\[
\boxed{\operatorname{rank}_{\rm add}(\mathcal Lu)=
\begin{cases}p-1,&u_0=0,\\p,&u_0\ne0.\end{cases}}
\tag{9}
\]

The same conclusions hold after multiplying `u` by any nonzero common
scalar; the scalar need not belong to $\mathbb E$.

**Proof.** All coefficients of $g=\mathcal L u$ are in $\mathbb E$ and
`g(0)=0`. If an additive coefficient at nonzero `xi` vanished, the
polynomial `sum_{t=0}^{p-1} g(t) X^t` would vanish at the primitive
`p`th root `zeta_p^xi`. By the field lemma it is a scalar multiple of
`1+X+...+X^(p-1)`. Its constant coefficient is zero, so all its
coefficients vanish. Multiplicative Fourier inversion then gives `u=0`,
a contradiction. The zero-frequency formula is character orthogonality.
Diagonalizing additive convolution proves (9).

In particular, for `u_0=0`, the **only** complex relation among its `p`
additive translates has constant coefficients. Their sum is zero and
their span is the entire mean-zero space. No assertion about the size of
the nonzero eigenvalues is part of this theorem.

### Application to the actual source and actual high cut

The anchored actual minimizer `b=x/a` has entries in $\mathbb E$.
Indeed `Q(r)` has entries in $F(r)=\mathbb E$. On its actual positive bulk
support it obeys
`b_I=-Q_II(r)^(-1)Q_I0(r)`, with an invertible positive-definite principal
matrix. This argument is valid at support changes and needs no strict
inactive inequalities. Selecting any subset of its coordinates preserves
the coefficient field.

Therefore (9) applies to each nonzero `x_U`, for **any** bulk cut `U`,
including `U={i!=0:x_i>lambda/sqrt(n)}` from round 15. Its additive
translation rank is exactly `p-1`. It also applies to the uncentered
source `E_I f`, since `f/a` has coefficients in $\mathbb E$ and its root
coordinate is zero. More generally a nonzero residual
`E_I(f-Ch)` has rank `p-1` whenever `h/a` has coefficients in this field.
This covers rational trials after the common root normalization; the
primal source bound itself continues to allow arbitrary real trials.

For the witness (3), `a w` and `a d` have coefficients in $\mathbb E$:
write `E=a²||b_I||²` in that formula. Since `ad_0=-1`, the **global dual
potential has additive translation rank `p`**. A bad prime source must
thus satisfy (6), its prescribed preimage equation, and this full-rank
condition simultaneously. Exact lower-dimensional additive propagation
cannot carry it.

This is stronger than a generic support-count uncertainty statement,
but relies on the coefficient field of the actual algebraic-width solve.
It is not a new uniform bound on an arbitrary complex Fourier minor.

## 3. A prime obstruction to quantitative conditioning from rank

Full rank is still quantitatively inadequate, even with real signed
vectors, multiplicative inversion symmetry, and an exact Paley sector.
Here is an explicit construction using only six positional points.

Take `p=1 mod 24`, `p>17`. Each of
`2,3,4,2^(-1),3^(-1),4^(-1)` lies in `D_+`: quadratic reciprocity gives
`chi(2)=chi(3)=chi(-1)=1`, and
`chi(1-a^(-1))=chi(1-a)` for a square `a`. Define on `F_p`

\[
g_p=\frac1{\sqrt{1324}}\sum_{a=2,3,4} c_a
       (\delta_a+\delta_{a^{-1}}),\qquad
(c_2,c_3,c_4)=(-11,21,-10).
\tag{10}
\]

The six points are distinct at these primes, `||g_p||=1`, and `g_p` is
inversion-even, supported in `D_+`, and has sum zero. Its unitary
multiplicative inverse transform `u` is real, satisfies `P_+u=u`, and
has `u_0=0`. This is a signed-sector vector, not an actual QP optimizer or
a trial already supported on its adaptive mask.

The exact rational cancellations are

\[
\sum_a c_a=0,\qquad \sum_a c_a(a+a^{-1})=0.
\]

At the fixed additive frequency `xi=12`, multiplication of the modular
inverse by `12` gives the **ordinary integer** `12/a` modulo `p`. Thus

\[
\widehat g_p(12)=\frac1{\sqrt{1324}}\sum_a c_a
  \left(e^{2\pi i(12a)/p}+e^{2\pi i(12/a)/p}\right).
\tag{11}
\]

Using `|exp(it)-1-it|<=t²/2` and the two cancellations proves

\[
\boxed{0<|\widehat g_p(12)|\le\frac{C_2}{p^2},\qquad
C_2=\frac{2\pi^2}{\sqrt{1324}}
   \sum_a |c_a|\big((12a)^2+(12/a)^2\big)<31147.}
\tag{12}
\]

Strict positivity follows from (8), or directly from irreducibility of
`Phi_p` over `Q` before the scalar normalization. The additive convolution
operator with kernel `g_p` has rank `p-1` and smallest nonzero singular
value at most `C_2 p^(-2)`. Since `eta=(p^(2/3)-1)^(-1)`,
`|hat g_p(12)|/eta=O(p^(-4/3))`.

### Arbitrarily high polynomial loss

For every fixed integer `k>=1`, choose `k+1` distinct positive integers
`a_j>=2` and a nonzero rational solution of

\[
\sum_j c_j(a_j^m+a_j^{-m})=0\qquad(0\le m<k).
\tag{13}
\]

There is a one-dimensional kernel when `a_j=2,...,k+2`: the functions
`a^m+a^(-m)` are polynomials of degree `m` in `a+a^(-1)` (with a nonzero
leading coefficient), so these are Vandermonde rows at distinct points.
Let `ell=lcm(a_1,...,a_(k+1))`. Normalize
`g_p=sum_j c_j(delta_(a_j)+delta_(a_j^(-1)))` to unit norm. Along primes
in a fixed progression `p=1 mod M_k` all its positions belong to `D_+`.
For example take `M_k=8` times the product of the odd primes at most
`k+2`. There are infinitely many such primes by
[Dirichlet's theorem](https://kskedlaya.org/ant/chap-primes-in-ap.html).

At additive frequency `ell`, the exponents are the bounded integers
`ell a_j` and `ell/a_j`. Taylor expansion through order `k-1` and (13)
give

\[
0<|\widehat g_p(\ell)|\le C_k p^{-k}.
\tag{14}
\]

For all sufficiently large primes in the progression the positional
points are distinct. They still give a real, inversion-even pure-sector
frequency vector with zero mark and full mean-zero additive translation
rank. For each `k` the rational coefficients and paired integers were
fixed independently of `p`; no increasing rational precision is being
used. Hence **no fixed polynomial conditioning bound** follows from just
these properties on all prime signed-sector vectors. On the mean-zero
space the condition number of this additive convolution operator is at
least `p^k/C_k`, since Parseval also makes its largest singular value at
least one.

This does not contradict the desired source certificate. The additive
convolution operator in (12) is **not** the actual compression `C_I`.
There is no identification of its small additive mode with a small
eigenvalue, or large forcing overlap, of `C_I`. What fails is the proposed
intermediate step of obtaining useful quantitative source propagation
from cyclotomic nonvanishing and sector membership alone.

## 4. Square controls: exact trace-fiber cancellation

Let `q=ell²`, with `ell` an odd prime, and take the same width
`r=q^(-1/3)`. The field lemma still shows that `Phi_ell` is irreducible
over `Q(zeta_((q-1)/2),ell^(1/3))`. However an additive character now has
the form `exp(2 pi i Tr(xi t)/ell)`. An additive Fourier coefficient of a
function with coefficients in that field vanishes exactly when the
`ell` trace-fiber sums

\[
\sum_{t:\operatorname{Tr}(\xi t)=b}g(t),\qquad b\in\mathbb F_\ell,
\tag{15}
\]

are all equal. At primes each fiber is a singleton and the zero extension
outside `Q` makes this impossible for nonzero `g`. At squares these fibers
have `ell` points and permit exact cancellation.

Two explicit controls demonstrate the distinction.

* **An exact sector control.** For `ell>=7`, let
  `g=delta_2+delta_(2^(-1))-delta_3-delta_(3^(-1))` on the subfield
  `F_ell`, extended by zero. Its four distinct positions lie in
  `F_ell^×\{1} subset D_+` of the square field. It is rational,
  inversion-even, and has sum zero. Its additive Fourier coefficients
  vanish on exactly the `ell` characters trivial on the subfield.
  For the other characters nonvanishing follows from the prime
  polynomial argument over the base field. Its translation rank is
  **`q-ell`**, while its real multiplicative spectrum is in `ran P_+`
  and has zero root.
* **A nonnegative bulk control of much lower rank.** Put
  `B=F_ell^×`, choose `t in Q` generating `Q/B`, and set
  `g=1_B-(1/2)1_(tB)-(1/2)1_(t^(-1)B)`.
  For `ell>=5` the three cosets are distinct. Its inverse multiplicative
  transform is a positive scalar times
  `1_H(i)(1-Re eta_i(t))`, where `H=B^perp`; it is nonnegative, nonzero,
  and zero at the mark. Additively,
  `g=1_(F_ell)-(1/2)1_(tF_ell)-(1/2)1_(t^(-1)F_ell)` because the three
  coefficients sum to zero at field zero. Its transform is supported on
  three distinct annihilator lines, which meet only at zero. The
  zero-frequency value cancels, and the value on each other point of
  those lines is nonzero. The rank is exactly **`3(ell-1)`**.

The second control need not lie in one Paley sign sector. Neither control
is asserted to equal the actual square high cut or actual square source
at this width. They separately check the sector and nonnegative-cut
versions of the prime propagation theorem. The actual square failure of
the target at `q^(-1/3)` is already proved in
[round 15, Section 5](astra-cuts-15.md#5-square-controls-fail-the-target-at-this-exact-width).

## 5. Replay and what remains

[astra-source-16.py](astra-source-16.py) and its
[JSONL output](astra-source-16-results.jsonl) contain 22 numerical actual-QP
sign cases at seven primes through 2017 and four squares through `31²`,
all at `r=q^(-1/3)`. They check (2)--(5), and compute additive transforms
of the actual source, the cut at `x_i>1/sqrt(n)`, and the dual potential.
The largest identity discrepancy is below `3.2e-12`; the largest reported
QP residual is below `1.8e-11`. These are numerical support solves, not
interval support certificates. The replay uses the unitary version
`mathcal L/sqrt(n)` of (7); this common scalar does not affect rank.
The rank statements follow from the
proof, not a floating-point zero threshold. Both signs are retained.

The eight square-control rows independently reproduce the exact ranks.
For `q=49,121,361,961`, the pure-sector ranks are `42,110,342,930` and the
nonnegative bulk ranks are `18,30,54,90`.

Four separate 192-bit Arb evaluations verify the six-point construction,
including exact integer moment cancellations and exact Legendre signs.
At `p=1,000,033`, the unit-norm kernel's additive eigenvalue magnitude is
approximately `1.2530519194e-9`; its ratio to `eta` is approximately
`1.2529541812e-5`. The intervals and the rigorous Taylor upper bounds are
recorded in the JSONL. This small additive eigenvalue is a theorem-backed
method obstruction, not evidence of large actual QP energy.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-source-16.py \
  > research/astra-source-16-results.jsonl
```

For the desired estimate one still needs to prove, on the larger ordinary
theta side, either `E=o(log_2^*p)` or equivalently that the source constant
in (5) satisfies `epsilon_I sqrt(log_2^*p) -> infinity`. The prime result
here says its adverse witnesses must propagate in full additive dimension.
The explicit prime examples show why turning that into a norm estimate
requires a further argument using the **actual adaptive support and the
root source**, rather than a general additive rank or sector-conditioning
bound. No bound for the round-15 signed cut surplus is proved here.

Only this note, its unique script, and its JSONL were written. No README,
ledger, shared script, or remote was changed.
