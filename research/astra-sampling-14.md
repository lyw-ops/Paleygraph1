# Actual-support potentials and two quantitative barriers at p^(-1/3)

**Status: stronger necessary conditions and method barriers; no uniform prime
allowed-energy bound.** The current-support response in
[astra-energy-13.md](astra-energy-13.md) can be supplemented by a pure
opposite-sector potential whose **positive part is small everywhere**, and
whose level set is exactly the actual positive bulk support. Actual optimality
also imposes a weighted Jacobi identity on every cut of that support. These
conditions retain dispersed energy and all inactive inequalities.

Two obstructions clarify what an arithmetic proof still has to use. At
`r = p^(-1/3)`, the existing Hanson–Petridis scalar moment hierarchy is
automatically trivial whenever the actual common mass satisfies
`c^2 >= 1/(1+r(T_p-1)) ~ sqrt(2) p^(-1/6)`. Separately, the existing prime
Fejér perturbation can be made **maximal at the mark**, relatively near-optimal,
and have bulk projected-gradient residual `o(r)` **in maximum norm**, while its
allowed energy diverges. The latter sharpens the earlier qualitative-residual
obstruction; the Fejér construction itself was already in
[quadratic-fourth.md](quadratic-fourth.md#unbounded-allowed-energy-with-vanishing-residual).

The requested sign is the larger **ordinary-theta** sign. Every result below
holds for either sign, so applies to that sign without inferring it from the
positive-width marker. It suffices to prove
`A_sigma(p^(-1/3)) = o(log_2^* p)` by the
[weighted marked contraction](parallel-complexity-14.md#4-consequence-at-the-intermediate-width). The public
[ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/)
specifies prime orders; it was checked on 2026-11-17.

## 1. An actual potential with a global positive cap

Use the notation of [the reciprocal QP](quadratic-theta.md). At a fixed
`0 < r < 1`, put

\[
 N=P_{-\sigma},\quad P=P_\sigma,\quad
 Q=J+rP+r^{-1}N,\quad x=A_\sigma(r),\quad y=Qx,
 \qquad x_0=a,\quad y_0=a^{-1},\quad j^Tx=j^Ty=c.
\]

Thus `x,y >= 0`, `x_i y_i = 0` off zero, and `x^T y=1`. Translation
optimality gives `x_i <= a`, `y_i <= a^(-1)`. The Jacobi entry estimate gives
uniform upper and lower bounds on `a`. Let

\[
 I=\{i\ne0:x_i>0\},\quad m=|I|>0,\quad
 L=\sum_Ix_i,\quad \mu=L/m,\quad
 v=x_I-\mu\mathbf1_I,\quad D=\|v\|^2,
\]

\[
 A=\|Px\|^2,\qquad B=\|Ny\|^2,\qquad
 \eta=\frac{r^2}{1-r^2},\qquad
 t=\frac{(1-r)c}{r\sqrt n},\qquad
 H=D+(1-r^2)B.
 \tag{1}
\]

Suppose `H>0`. Define

\[
 \boxed{d=\frac{x-r^{-1}y+t\mathbf1}{H}
              =-\frac{Nx}{\eta H}\in\operatorname{ran}N.}
 \tag{2}
\]

The second equality follows directly from
`Q=rI+(r^(-1)-r)N+(1-r)J`. All coordinates, including the inactive ones,
are retained in (2). On the bulk it gives

\[
 \begin{array}{ll}
 d_i=(x_i+t)/H>t/H,&i\in I,\\
 d_i=(t-y_i/r)/H\le t/H,&i\notin I\cup\{0\}.
 \end{array}
 \tag{3}
\]

In particular the actual support is recovered exactly as
`I={i != 0 : d_i > t/H}`. Shared zeros give equality at the threshold.
The marked coordinate is

\[
 d_0=\frac{a+t-(ra)^{-1}}H.
 \tag{4}
\]

Let `Pi` subtract the mean on `I`. This potential has the exact contrast and
norm formulas

\[
 \boxed{\begin{aligned}
 -a d_0-\mu\sum_{i\in I}d_i&=1,\\
 \Pi d_I&=v/H,\\
 r\|d\|&=(1-r^2)\sqrt B/H,\\
 \|(d)_+\|_\infty&\le(a+t)/H.
 \end{aligned}}
 \tag{5}
\]

For the contrast, put `z=a e_0+mu E_I 1_I`. On `I`,
`(Nx)_I=-eta x_I-eta t 1_I`; hence

\[
 \langle E_Iv,Nx\rangle=-\eta D,
 \qquad
 \langle z,Nx\rangle=\|Nx\|^2+\eta D
       =r^2B+\eta D=\eta H.
\]

This proves the first line of (5); the other lines follow from (2), (3),
`Nx=rNy`, and the coordinate cap on `x`. Consequently

\[
 \|\Pi d_I\|\le H^{-1/2},\qquad
 r\|d\|\le\sqrt{1-r^2}\,H^{-1/2},\qquad
 -\frac\mu H\le(\Pi d_I)_i\le\frac{a-\mu}H.
 \tag{6}
\]

At `r=p^(-1/3)`, `t=O(p^(-1/6))`. Thus any sequence of actual optimizers
with `D -> infinity` necessarily gives opposite-sector vectors satisfying
**all** of

\[
 \begin{gathered}
 -a d_0-\mu\sum_I d_i=1,\qquad
 \|\Pi d_I\|\longrightarrow0,\qquad
 \|d\|=o(p^{1/3}),\\
 \|(d)_+\|_\infty\longrightarrow0,\qquad
 I=\{i\ne0:d_i>t/H\}.
 \end{gathered}
 \tag{7}
\]

The global positive cap and the threshold relation are extra constraints
absent from a generic centered sampling failure. They use nonnegativity and
complementarity at every coordinate. An arbitrary signed opposite vector
with small samples on a chosen dense mask need not have them.

There are two limitations. First, `H` also contains the opposite energy `B`;
`H -> infinity` does not imply `D -> infinity`. This witness supplies a
necessary condition, not the equivalence proved by the supported-preimage
test in [astra-energy-13.md](astra-energy-13.md). Its preimage in (2) is the
full `x`, with a mark and nonzero mean, rather than a centered vector
supported on `I`. Second, the decomposition

\[
 A=a^2+L^2/m+D-c^2-r^2B
 \tag{8}
\]

still requires control of `L^2/m`. A divergence caused only by that term
need not produce `D -> infinity`.

## 2. A weighted Jacobi condition on every actual-support cut

Set `S={0} union I` and `d_r=(1-r)/(1+r)`. For distinct coordinates,

\[
 Q_{ij}=-\frac{1-r^2}{2r}
               \left(\sigma K_{ij}+\frac{d_r}{n}\right).
 \tag{9}
\]

Take any real `h` supported on `S` and let `xh` denote the coordinatewise
product. Expanding squared differences and using
`x_i(Qx)_i=1_{i=0}` gives the exact ground-state identity

\[
 \boxed{\langle xh,Q(xh)\rangle
   =h_0^2+\frac{1-r^2}{4r}
       \sum_{i,j\in S}x_ix_j
       \left(\sigma K_{ij}+\frac{d_r}{n}\right)(h_i-h_j)^2.}
 \tag{10}
\]

The diagonal summands vanish. Although the individual conductances in the
sum can have either sign, the resulting quadratic form is positive when
`h_0=0`; in fact its right-hand sum is at least
`4r^2 ||xh||^2/(1-r^2)` in that case. Applying a positive-edge graph
inequality to these signed conductances without justification would be an
error.

In particular, for **every** `U subset I`, write
`x_U=1_U x`, `L_U=sum_U x_i`, `E_U=||x_U||^2`, and
`F_U=||N x_U||^2`. Then

\[
 \boxed{\begin{aligned}
 &\sum_{i\in U,\ j\in S\setminus U}
     x_ix_j\left(\sigma K_{ij}+\frac{d_r}{n}\right)\\
 &\hspace{10mm}=2F_U+2\eta E_U+
                   \frac{2r}{1+r}\frac{L_U^2}{n}.
 \end{aligned}}
 \tag{11}
\]

The cross sum counts a pair with its first endpoint in `U` once. Formula
(11) follows either from (10) with `h=1_U`, or from
`<x_U,Qx_U>=-<x_U,Q(x-x_U)>`. It is strictly positive for nonempty `U`.
It applies simultaneously to high-coordinate sets, unions of such sets,
and cuts collecting energy from many spectral bands. No small-eigenvalue
window or support persistence is involved.

In arithmetic terms, writing $\rho_{i-j}$ for the character indexed by $i-j$,

\[
 K_{ij}=\frac1n\sum_{z\in Q_{\rm field}}
              \chi(1-z)\,\rho_{i-j}(z)
\]

is the real Jacobi kernel. Thus (11) is a concrete weighted arithmetic
restriction on the actual support. The corresponding identity for a
general nonnegative reciprocal pair `u,w=Qu` is instead

\[
 \sum_{i\in U,j\notin U}u_i u_j
       \left(\sigma K_{ij}+\frac{d_r}{n}\right)
 =\frac{2r}{1-r^2}
       \left(\langle u_U,Qu_U\rangle-
                       \sum_{i\in U}u_iw_i\right).
 \tag{12}
\]

Actual complementarity removes the entire last term. Bounding its maximum
summand does not remove its sum on a large set.

Equations (10)–(11) are necessary conditions, rather than a new character-sum
upper bound. The entry estimate `|K_ij| <= sqrt(p)/n` does not control these
adaptively weighted cuts sharply enough. A proof using them still needs
arithmetic information about the weights and the selected support. The
identities alone are also valid at square order.

## 3. The existing prime phase-packing hierarchy is trivial in a broad mass range

Normalize one actual spectrum to the probability `x/(c sqrt(n))`, and let
`f` be its positional characteristic function. Set

\[
 C_2=\sum|f|^2=1+\frac{A+r^2B}{c^2},\qquad
 D_{\rm leak}=\sum_{s(z)=-\sigma}|f(z)|^2=\frac{r^2 B}{c^2},\qquad
 T_p=\left\lfloor\frac{1+\sqrt{1+4n}}2\right\rfloor.
\]

The actual energy identity `r(A+B)=1-c^2` proves

\[
 C_2\le1+\frac{1-c^2}{r c^2}.
 \tag{13}
\]

Therefore

\[
 \boxed{c^2\ge\frac1{1+r(T_p-1)}\quad\Longrightarrow\quad C_2\le T_p.}
 \tag{14}
\]

The [Hanson–Petridis](https://arxiv.org/abs/1905.09134v3) phase-packing
application in [astra-quadratic-10.md](astra-quadratic-10.md) and its
[higher-moment extension](astra-convolution-11.md#4-what-iteration-of-the-prime-moment-bound-actually-gives)
have the form

\[
 C_{2k}\le\alpha^{k-1} C_2+(1-\alpha^{k-1})T_p,
 \qquad \alpha=(1+\sqrt{D_{\rm leak}})/2,
 \tag{15}
\]

when `D_leak<1`. If `C_2<=T_p`, the right side of (15) is at least `C_2`,
whereas `|f|<=1` already gives `C_{2k}<=C_2`. Applying the same argument
to convolution powers cannot help: `C_{2k}<=C_2<=T_p` for every power,
so their phase-packing inequalities are also implied by `|f|<=1`.

At the requested width,

\[
 \frac1{1+p^{-1/3}(T_p-1)}
       =(\sqrt2+o(1))p^{-1/6}.
 \tag{16}
\]

Under (14), the leakage is at most `r^2(T_p-1)=O(p^(-1/6))`, so the
requirement `D_leak<1` also holds for large `p`. In particular, **if the
actual mass is bounded below, this whole scalar hierarchy imposes no
additional restriction at this width**, even on an actual optimizer with
large dispersed energy. This is a scale obstruction for the cited use of
Hanson–Petridis, not a limitation asserted for every possible use of that
theorem or for its positional rectangle inequalities.

The alternative `c^2` below the threshold is not excluded here. No
uniform positive mass lower bound at `p^(-1/3)` is assumed. A new prime
argument must either use more than the scalar hierarchy, or also address
that low-mass possibility.

## 4. A sharper genuine-prime obstruction for local KKT residuals

The earlier Fejér construction already proves energy divergence for
nonnegative reciprocal near-complementary pairs. The refinement here is
that translation is unnecessary: using the **untranslated** kernel retains
the maximum-at-mark property and gives polynomially small coordinatewise
KKT errors. This also gives relative near-optimality for the rooted QP.

For either sign and every sufficiently large prime $p\equiv1\pmod4$, put
`k=floor(log_2(p)/4)`. The character-sum argument already proved in
[quadratic-fourth.md](quadratic-fourth.md#unbounded-allowed-energy-with-vanishing-residual)
gives a square `t_*` of order greater than `2k` such that
`chi(1-t_*^j)=sigma` for `1<=j<=k`. Briefly, expansion gives
`p/2^(k+1)+O(k^2 sqrt(p))` choices before excluding `O(k^2)` elements of
small order. A primitive root of unity for the largest selected exponent
proves that each nontrivial character product is nonsquare. This uses the
[quadratic Weil bound](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/).

The nonnegative, inversion-even vector

\[
 h_i=\frac1{\sqrt n(k+1)}
                 \left|\sum_{j=0}^k i(t_*)^j\right|^2
\]

satisfies

\[
 Jh=j,\quad Nh=0,\quad
 0\le h_i\le h_0=\frac{k+1}{\sqrt n},\quad
 E_k:=\|Ph\|^2=\frac{k(2k+1)}{3(k+1)}.
 \tag{17}
\]

Also `Qh=rh+(1-r)j>=0`, with maximum `(1+rk)/sqrt(n)` at zero. For
the actual pair at `r=p^(-1/3)`, take `delta=k^(-1/4)` and set

\[
 u=x+\delta h,\quad w=y+\delta Qh=Qu,\quad
 E=\langle u,w\rangle,\quad
 x'=u/\sqrt E,\quad y'=w/\sqrt E.
 \tag{18}
\]

They have exact reciprocal sector equations, nonnegativity, inversion
symmetry, common mean, inner product one, and **each vector is maximal at
zero**. Their common normalized mass is at most one, by their unit
quadratic energy. Since `Qh>=0`,

\[
 1\le E\le\left(1+\delta\sqrt{1+rE_k}\right)^2=1+O(\delta).
 \tag{19}
\]

Positivity gives `<x,h>>=0`, so

\[
 \langle Px,Ph\rangle=\langle x,h\rangle-c\ge-c.
\]

Consequently no choice of a translated kernel is needed for

\[
 \boxed{\|Px'\|^2\ge
       \frac{A+\delta^2E_k-2\delta c}{E}
       \gg\sqrt{\log p}.}
 \tag{20}
\]

This bound holds regardless of whether the actual `A` itself diverges.
After reanchoring `x'` to the true root `a`, its energy relative to the
actual minimum is

\[
 \frac{E}{(1+\delta h_0/a)^2}=1+O(\delta),
 \tag{21}
\]

and is at least one by optimality. Thus these are relatively near-optimal
rooted trials. Their total bulk overlap `omega=sum_{i!=0}x'_i y'_i` obeys
`0<=omega<=1-E^(-1)=O(delta)`.

There is a much smaller **local** error. At every bulk coordinate at least
one of the original `x_i,y_i` is zero. Hence the natural nonnegative KKT
residual satisfies

\[
 \boxed{\left\|\min(x',y')_{\ne0}\right\|_\infty
       \le\frac{\delta(k+1)}{\sqrt{nE}}
       =O\left(\frac{(\log p)^{3/4}}{\sqrt p}\right)=o(r).}
 \tag{22}
\]

The coordinate products have the explicit bound

\[
 \begin{aligned}
 \| (x'y')_{\ne0}\|_\infty
 &\le\frac\delta{E\sqrt n}
       \left[a(1+rk)+a^{-1}(k+1)\right]\\
 &\quad+\frac{\delta^2(k+1)(1+rk)}{En}
 =O\left(\frac{(\log p)^{3/4}}{\sqrt p}\right).
 \end{aligned}
 \tag{23}
\]

Combining the sum and maximum bounds, for any fixed `s>3` the **unnormalized**
`ell_s` norm of the coordinate-product error also is `o(r)`:

\[
 \|(x'y')_{\ne0}\|_s
 \le\omega^{1/s}\|(x'y')_{\ne0}\|_\infty^{1-1/s}
 =O\left((\log p)^{3/4-1/s}
               p^{-(1-1/s)/2}\right)=o(p^{-1/3}).
 \tag{24}
\]

Thus an energy estimate deduced from nonnegativity, maximum at the mark,
relative objective error `o(1)`, exact reciprocal equations, and a **maximum
norm** KKT residual `o(r)` would be false on genuine prime inputs, including
the actual larger-theta sign chosen separately at each prime. The pair in
(18) is not an optimizer: its total off-mark overlap need not be `O(r)`,
and its positive support need not satisfy the zero-potential equations.
There is no contradiction with the existing certificates based on an
`ell_2` fixed-point residual of order `r`, or with the compressed source
error of order `r^2` in [astra-energy-13.md](astra-energy-13.md).

## 5. Replay and what it establishes

[astra-sampling-14.py](astra-sampling-14.py) checks both signs at 15 primes
through 153649 and ten prime squares through `389^2`, always at
`r=q^(-1/3)`. The [50 numerical rows](astra-sampling-14-results.jsonl)
check (2), (5), four cuts in (11), (17), (20)–(23), the mark maxima, and
the scalar threshold (14). Numerical support detection uses `1e-8`.
The largest checked discrepancy is below `4.4e-11`, and the largest QP
solver residual is below `2e-11`. These rows do not certify the larger
ordinary-theta sign; both signs are retained.

Selected actual-energy and potential values are:

| Order and sign | Actual `A` | Centered `D` | `H=D+(1-r^2)B` |
|---|---:|---:|---:|
| `97,+` | 1.23163 | 0.17831 | 1.33995 |
| `4001,+` | 2.15538 | 0.51564 | 2.68271 |
| `9413,+` | 2.31434 | 0.58833 | 2.90290 |
| `153649,+` | 2.59969 | 0.71762 | 3.32871 |
| `153649,-` | 2.61200 | 0.71781 | 3.31660 |
| `97^2,+` | 3.02784 | 1.28160 | 3.48352 |
| `389^2,+` | 3.79479 | 1.90178 | 4.44742 |

The sampled Fejér degrees on the large primes are only 11–16. In this
range `delta=k^(-1/4)` is not small; some perturbed energies are less than
the corresponding actual energies. The asymptotic divergence assertion
is the proved lower bound (20), not a trend claimed from these small-degree
rows. The square search caps the degree at 64; it is not a claim to find
the longest possible square run.

For scale, at `p=153649` the two actual masses have `c^2=0.902695`,
whereas the sufficient threshold in (14) is `0.162521`; their `C_2` values
are approximately 3.881 and 3.895, compared with `T_p=277`. The hierarchy
is already vacuous on both of these actual samples. This finite comparison
does not establish a uniform lower bound on `c^2`.

The separate `--certificate` mode uses 192-bit Arb at the **algebraic**
width `r=13^(-1/3)`. It verifies the full strict orthant and `|gamma|<1`,
then checks the contrast, threshold signs and a nonempty cut on each side.
It encloses

\[
 H_+=0.64898706612857731318\ldots,\qquad
 H_-=0.55938448541422573575\ldots,
\]

with contrasts equal to one to the checked ball precision. The two cut
values are `0.166501971403344733...` and
`0.00284297495928962399...`; both sides of (11) agree within `1e-45`.
The interval comparison tests formulas; their exact equality is proved
algebraically above.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-sampling-14.py --large
.venv/bin/python -B research/astra-sampling-14.py --certificate
```

The remaining task is a prime arithmetic estimate that applies to the
**actual** potential/support constraints (3), (5), (10)–(11), or to the
full centered source response, while controlling `L^2/m` on the chosen
side. No such estimate is proved here. This pass wrote only this note,
its uniquely named experiment, and its numerical JSONL. No ledger,
README, shared script, or remote was changed.
