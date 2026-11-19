# Uniform coherence does not give inverse-source tightness

Round 31, 2026-11-18. ETH Problem 26, ordinary theta.

**Result.** There is an exact positive-floor stationary counterfamily with
the **full uniform entry bound**

\[
\boxed{\quad |K_{ij}|\le C_\tau/\sqrt n\quad\text{for every }i,j,\quad}
\tag{1}
\]

where the finite constant is independent of the family index. The family
retains the two reciprocal stationary spectra, weights `w0=1`,
`wi=tau/n`, both exact masses, root product, Paley sector dimensions and
marked projector values. Its sources are uniformly integrable, both
centered energies diverge subcritically, and a **positive fraction** of the
actual first inverse source-moment mass approaches eigenvalue zero.
For `tau=.05` the fraction is approximately **0.3123122098**. These are
unique stationary points and zero-start Picard limits for their constructed
reflections.

Thus full uniform coherence, source UI and the complete reciprocal source
identities **do not imply** inverse-first-moment tightness. This strengthens
the obstruction in [source-pair 29](parallel-source-pair-29.md): it is not
merely a coherent-root-row construction and pays no `sqrt(log n)` loss.

The final reflections are **not convolution operators**. A Walsh
convolution gives one flat starting matrix; Section 9 additionally takes an
**actual prime Paley matrix** as the starting matrix, at its actual dimension.
The subsequent finite rank conjugations destroy translation and sector convolution closure.
This is neither a cyclic-circulant counterfamily nor a Paley multiplier,
and supplies **no counterexample for actual prime Paley stationary points**.
Coherence together with those additional structures remains a distinct
question. The stationary marker here is still exactly zero.
The theorem uses some fixed finite entry constant; it does not refute a
hypothesis that specifies a particular sharp numerical Paley constant.

The prime-seeded corollary gives `K=V K_Paley V^T` with
`rank(V-I)<=6` and `rank(K-K_Paley)<=12`, through primes `1 mod 8`.
It retains the same inverse-leakage limit. The difference has operator
norm at least `sqrt(2)-o(1)`, so this is not an approximation of the
actual Paley operator or its stationary point.

There is also a useful limit on what a coherent counterexample can do:
Section 7 proves that fixed full coherence and the retained root data keep
a positive amount of inverse mass away from zero. Accordingly the old
model's *all-mass* collapse is replaced here by a positive-fraction collapse,
which already disproves tightness.

## 1. The exact source being tested

We use counting norms and the conventions of
[reciprocal 28](parallel-reciprocal-28.md), [source-pair 29](parallel-source-pair-29.md)
and its [audit](parallel-audit-30.md). Put

\[
 c=\tau/n,\quad W=1+(n-1)c,\quad a=\sqrt{W/n},\quad
 J=n^{-1}\mathbf1\mathbf1^T,\quad P=I-J.
\]

A symmetric reflection has `K1=0`, `K²=P`,
`P_+=(P+K)/2`, `P_-=(P-K)/2`. Our positive pair satisfies exactly

\[
 AB=w,\quad \sum A=\sum B=na,\quad
 x=A-a\mathbf1\in V_+,\quad y=B-a\mathbf1\in V_-,
 \quad A_0=B_0=1.                                         \tag{2}
\]

Hence `v=A-B=K Phi(v)` for `Phi(v)i=sqrt(vi²+4wi)`.
This is the nonlinear stationary equation, not an arbitrary feasible vector
or an exterior choice of diagonal. In particular, with

\[
 D=\operatorname{diag}\frac{c}{aA},\quad
 T=P_+DP_+|_{V_+},\quad e=P_+e_0,\quad b=1-c,
\]

one has

\[
 Tx=be,\qquad Q=\langle x,Tx\rangle=b(1-a),\qquad
 d\nu(\lambda)=b^2\lambda^{-1}d\mu_e(\lambda),\quad
 \nu(\mathbb R_+)=Q.                                     \tag{3}
\]

The opposite diagonal is exactly `D_-=diag(c/(aB))`, so

\[
 d_i d_{-,i}=\rho\ (i\ne0),\qquad
 d_0d_{-,0}=\rho c,\qquad \rho=\tau/W.                    \tag{4}
\]

All the Schur and resolvent identities in source-pair 29 therefore apply
with their exceptional mark correction. We will compute the **entire**
source spectral measure in a two-dimensional invariant block.

## 2. An eight-group positive reciprocal pair

Fix `tau>0`. Write `s_infty=sqrt(1+tau)` and choose a fixed

\[
 0<d<s_\infty-\sqrt\tau.
\tag{5}
\]

The replay uses `d=(3/5)(sqrt(1+tau)-sqrt(tau))`. Let `t=2^k` tend to
infinity and set

\[
 n=2t^8,\quad m=t^4,\quad H=t^3,\quad r_N=2m-1,\quad
 M=n/4-m.
\tag{6}
\]

Thus every unmarked group below has size at least `m`, comparable to
`sqrt(n)`. Let `s=sqrt(W)` and define

\[
 S=\frac{n s-\sqrt n-r_N\sqrt\tau-m(H+\tau/H)}{4M},
 \quad S_1=S+d,\ S_2=S-d,
 \quad D_j=\sqrt{S_j^2-\tau},\quad L_j=S_j+D_j.
\tag{7}
\]

For all sufficiently large `t`, `S_j>sqrt(tau)`. Indeed

\[
 S=s_\infty-\frac1{2t}+O_\tau(t^{-4}),\qquad
 L_j+\tau/L_j=2S_j.
\tag{8}
\]

Here and below constants can also depend on the fixed choice in (5).
The pair's per-coordinate values are:

| Group | Size | `A` | `B` |
|---|---:|---:|---:|
| Mark | 1 | 1 | 1 |
| Neutral | `r_N` | `sqrt(tau)/sqrt(n)` | same |
| First tail | `m` | `H/sqrt(n)` | `tau/(H sqrt(n))` |
| Second tail | `m` | `tau/(H sqrt(n))` | `H/sqrt(n)` |
| Background `1+` | `M` | `L_1/sqrt(n)` | `tau/(L_1 sqrt(n))` |
| Background `1-` | `M` | `tau/(L_1 sqrt(n))` | `L_1/sqrt(n)` |
| Background `2+` | `M` | `L_2/sqrt(n)` | `tau/(L_2 sqrt(n))` |
| Background `2-` | `M` | `tau/(L_2 sqrt(n))` | `L_2/sqrt(n)` |

Their sizes sum to `n`. Products and (7) give `AB=w` and both masses in
(2) exactly. Swapping the members of each pair interchanges `A,B`.
Consequently

\[
 x\perp y,\quad x,y\perp\mathbf1,\quad
 \|x\|^2=\|y\|^2=:E=\frac{t^2}{2}+O_\tau(1)=o(\sqrt n).
\tag{9}
\]

The orthogonality follows from `sum AB=W=na²`, not a limiting calculation.
The growing squared norm is `m H²/n=t²/2`; the root and all background
squared norms are bounded. Also `A_i<=A_0=1`, `B_i<=B_0=1` for large
`t`. These coordinate caps are retained directly, without claiming the
translation identities that prove them for Paley kernels.

The actual scaled bulk source

\[
 G_i=\sqrt n(A_i+B_i-2\sqrt c),\quad i\ne0
\]

is zero on the neutral group, bounded on all backgrounds and has value
`H+tau/H-2sqrt(tau)` on the two tails. Their first mass is

\[
 \frac{2m}{n}(H+\tau/H-2\sqrt\tau)
 =t^{-1}+O_\tau(t^{-4}).                                  \tag{10}
\]

This proves source UI, with a uniform tail bound `O_tau(R^(-1/3))`
above the bounded background levels. Both normalized spectra `A/a,B/a`
are UI as well; their marked first mass is `O(n^(-1/2))`.

The extra bounded background levels in (7) are essential to this
construction. A single background pair with limiting half-sum
`sqrt(1+tau)` has too little norm slack for the root row used below.
The nonconstant but bounded background half-sums provide that slack
without harming UI.

## 3. A uniformly flat compatible root row

Let `F` be the eight-dimensional space of vectors constant on the groups.
We first prescribe a flat root row `r=K e0` in `F`, satisfying

\[
 r_0=-1/n,\quad r\perp\mathbf1,\quad
 \|r\|^2=1-1/n,\quad
 \langle r,x\rangle=1-a,\quad
 \langle r,y\rangle=-(1-a),\quad
 \|r\|_\infty=O_\tau(n^{-1/2}).                           \tag{11}
\]

The root row will be zero on both tails. Here are explicit formulas,
including the small symmetric correction needed for the nonzero root
diagonal. Put

\[
 h=1-a,\quad s_N=(\sqrt\tau-s)/\sqrt n,\quad
 s_B=(S-s)/\sqrt n.
\]

Define a group-constant vector `q` by

\[
 q_0=-1/n,\quad q_N=\frac{h-s_B}{n r_N(s_N-s_B)},\quad
 q_{\rm tails}=0,\quad
 q_{\rm backgrounds}=\frac{1/n-r_Nq_N}{4M}.               \tag{12}
\]

It is symmetric under `A<->B`, has zero sum, and is orthogonal to
`(A+B)/2-a1`. Thus `q` is orthogonal to both `x` and `y`. In particular
`q_N=O_tau(1/(r_N sqrt(n)))`, all its background entries are
`O_tau(n^(-3/2))`, and `||q||²=o(1)`.

Set

\[
 \beta=2M/n,\quad R^2=1-1/n-\|q\|^2,\quad
 \mathbf D=(D_1,D_2),\quad
 \mathbf D^\perp=(-D_2,D_1),
\]

and choose

\[
 \mathbf k=
 \frac{h\mathbf D}{\beta|\mathbf D|^2}
 -\sqrt{\frac{R^2}{\beta}
       -\frac{h^2}{\beta^2|\mathbf D|^2}}
       \frac{\mathbf D^\perp}{|\mathbf D|}.
\tag{13}
\]

The radical is positive eventually: `beta -> 1/2` and
`beta |D|² -> 1+d²>1`, while `h,R -> 1`.
Add to `q` the values `+k_j/sqrt(n),-k_j/sqrt(n)` on the two members
of background pair `j`, leaving the mark, neutral group and tails
unchanged. Call the result `r`. The odd part has norm squared
`beta |k|²=R²`, and its pairing with `x` is
`beta k.D=h`. Its pairing with `y` is `-h`.
This proves all of (11) exactly. The coefficients in (13) have finite
limits, so this row is uniformly flat.

Let `j=n^(-1/2)1` and define

\[
 e_+=\frac{Pe_0+r}{2},\quad e_-=\frac{Pe_0-r}{2},\quad
 p=\tfrac12-\tfrac1n,\quad p_-=\tfrac12,
 \quad u=e_+/\sqrt p,\quad u_-=e_-/\sqrt{p_-}.
\tag{14}
\]

These two unit vectors are orthogonal to each other and to `j`.
Define the root-free residuals

\[
 X=x-(h/p)e_+,\quad Y=y-(h/p_-)e_-,\quad
 F_0=F\cap\operatorname{span}\{j,e_0,r\}^\perp.
\tag{15}
\]

Then `X,Y` belong to `F0`, are orthogonal, have marked coordinate zero,
and `||X||²=E-h²/p -> infinity`. Write `g=X/||X||`.

We want a full reflection that gives `u,g` eigenvalue plus one, `u_-`
eigenvalue minus one, and **all of `F0 intersect g^perp`** eigenvalue
minus one. Then `Kx=x, Ky=-y`, and the plus part of `F` is exactly
two-dimensional. A flat compatible root row alone would not suffice.
The next section constructs the full uniformly coherent completion.

## 4. Full completion with no logarithmic loss

### 4.1 An explicit coherent starting reflection

Identify the coordinates with
`G=F_2^(8k+1)`, since `t=2^k`. For `z in F_2^(8k)` put

\[
 f(u,z)=(-1)^{u+z_1z_2+z_3z_4+\cdots+z_{8k-1}z_{8k}}.
\]

Let `F_W` denote the orthogonal normalized Walsh transform, and set

\[
 s_0(0)=0,\quad s_0(\xi)=f(\xi)\ (\xi\ne0),\qquad
 K_0=F_W\operatorname{diag}(s_0)F_W.
\tag{16}
\]

The function `f` is balanced and has value one at zero. Its unnormalized
Walsh transform is zero on half the characters and has magnitude
`sqrt(2n)` on the other half: the `u` sum is zero or two, and each
two-variable quadratic pair has Walsh magnitude two. Therefore

\[
 \begin{gathered}
 K_0^2=P,\quad K_0j=0,\quad (K_0)_{ii}=-1/n,\
 \dim V_+(K_0)=(n-2)/2,\quad \dim V_-(K_0)=n/2,\
 |(K_0)_{ij}|\le\sqrt2/\sqrt n+1/n.
 \end{gathered}                                           \tag{17}
\]

This is a Walsh convolution on an elementary abelian group, **not** a
cyclic circulant or the Paley sign multiplier.

The group partition in Section 2 can be chosen deterministically as
follows. Take the four cosets of an index-four subgroup, and remove
exactly `m` coordinates from each, including zero. Their remainders are
the four backgrounds, each of size `M`. Partition the removed `4m`
coordinates into the root, the neutral group and the two tails.
For example, remove the first `m` elements of each coset in binary order.

For a normalized full-coset indicator, `K0` has infinity norm at most
`2/sqrt(n)`: its Walsh support contains four characters. Removing `m`
points changes that bound by at most

\[
 (\sqrt2+n^{-1/2})\frac{m}{\sqrt{nM}}=O(n^{-1/2}).
\tag{18}
\]

Thus the normalized background indicators have `K0` images bounded by
`O(n^(-1/2))`. For a normalized tail or neutral indicator, the direct
coherence bound gives `O(n^(-1/4))`.

### 4.2 Implanting the root row

Write `r0=K0 e0`. From (12)--(13) and (18),

\[
 \|K_0r\|_\infty=O_\tau(n^{-1/2}),\qquad
 \langle r_0,r\rangle=(K_0r)_0=O_\tau(n^{-1/2}).
\tag{19}
\]

For the neutral contribution, use `|q_N|=O(1/(r_N sqrt(n)))` and
the entry bound, so its image is `O(1/n)`; the root contribution is
smaller. The remaining coefficients are bounded combinations of the
normalized background indicators. This proves (19) on all coordinates.

Hence `||r0-r|| -> sqrt(2)`. The unit vector

\[
 w=(r_0-r)/\|r_0-r\|,\qquad U_0=I-2w\otimes w
\]

has infinity norm `O_tau(n^(-1/2))`, has marked coordinate zero, and
is orthogonal to `j`. Since `r0,r` have equal norms,
`U0 r0=r`. Thus

\[
 K_1=U_0K_0U_0,\qquad K_1e_0=r.                           \tag{20}
\]

This conjugation preserves full uniform coherence. Indeed, expand

\[
 K_1=K_0-2w(K_0w)^T-2(K_0w)w^T
              +4\langle w,K_0w\rangle ww^T.
\tag{21}
\]

Use `||K0 w||infty<=1` and `||w||infty=O(n^(-1/2))`.
Every added entry is `O_tau(n^(-1/2))`, including the root entries.
In addition, (19) and `K0 r0=Pe0` show
`(K0 w)i=O_tau(n^(-1/2))` for every **unmarked** `i`.

For every unit `z in F0`, its root coordinate vanishes and all its
other coordinates are bounded by `1/sqrt(m)=O(n^(-1/4))`.
Equations (18)--(21) give the crucial two bounds

\[
 \boxed{\quad
 \|z\|_\infty\le B n^{-1/4},\qquad
 \|K_1z\|_\infty\le B_\tau n^{-1/4}.
 \quad}                                                   \tag{22}
\]

To check the possible root exception in the second bound, use
`(K1 z)0=<r,z>=0` exactly. All other terms in (21) have the displayed
unmarked bounds. There are only seven unmarked group indicators, so
their coefficient sum is uniformly bounded for unit `z`.

### 4.3 A finite-block implantation lemma

Here is a general elementary completion step used to finish the construction.

**Lemma.** Suppose a coherent reflection `L` has constant `C1`, has an
invariant subspace `W` of fixed dimension, and `z1,...,zd` are orthonormal vectors in
`W^perp`, where `d` is fixed. Suppose both `zi` and `L zi` have infinity
norm at most `B n^(-1/4)`. If the two sector dimensions tend to infinity,
one can prescribe either eigenvalue to each `zi`, preserving `L` on
`W`, by orthogonal conjugation. The resulting reflection has a full
entry bound `C'/sqrt(n)` with `C'` independent of `n`.

**Proof.** We first choose mutually orthogonal helper eigenvectors
`pi`, of the required signs, orthogonal to `W` and every `zj`, with
`||pi||infty=O(n^(-1/4))`. In this application `dim W` is fixed.
More generally the construction below needs a fixed number of linear
orthogonality constraints.

Put `k=floor(delta sqrt(n))` with fixed
`delta=1/(8(C1+1))`, and choose a coordinate set of that size. Impose
on a vector `h` supported there: zero mean, orthogonality to the
required-sector projections of `W` and the `zj`, and orthogonality
to the previous same-sector helpers. The number of constraints is
bounded independently of `n`.

A codimension-`r` subspace of `R^k` contains a unit vector `h` with
`||h||infty<=1/sqrt(k-r)`. To see this, take a vertex of the intersection
of that subspace with `[-1,1]^k`. At least `k-r` coordinates are
saturated; normalize the vertex. Also `||h||1<=sqrt(k)`.
Consequently

\[
 |\langle h,Lh\rangle|\le C_1k/\sqrt n\le1/8,
 \quad \|P_\eta h\|^2\ge7/16,
\]

where the last inequality uses the zero mean. Normalize `P_eta h` to
obtain `pi`. Its infinity norm is at most a fixed multiple of

\[
 k^{-1/2}+C_1\sqrt{k/n}=O(n^{-1/4}).
\tag{23}
\]

All imposed orthogonalities are preserved by this sector projection.
Opposite-sector helpers are automatically orthogonal. This proves the
helper assertion. It uses no union bound and loses no logarithm.

Now the vectors `wi=(zi-pi)/sqrt(2)` are orthonormal. Set
`U=I-2 sum_i wi wi^T`. It interchanges `zi` with `pi` and fixes `W`.
Both `wi` and `L wi` have infinity norm `O(n^(-1/4))`. The expansion

\[
 ULU=L-2\sum_i\{w_i(Lw_i)^T+(Lw_i)w_i^T\}
       +4\sum_{i,j}\langle w_i,Lw_j\rangle w_iw_j^T
\tag{24}
\]

has a fixed number of terms, all bounded entrywise by `O(n^(-1/2))`.
Moreover `ULU zi=eta_i zi`, as required. This proves the lemma. ∎

Apply the lemma to `L=K1`, `W=span{j,e0,r}` and an orthonormal basis
of the five-dimensional `F0`, starting with `g`. Prescribe sign plus
on `g` and minus on its four orthogonal directions. The hypotheses
follow from (22). The resulting `K` has **every entry** bounded as
in (1), preserves the full eight-group space `F`, and has on `F` the
two plus directions `u,g`, five minus directions, and one zero direction.
Conjugation preserves the full sector dimensions from (17).

In particular

\[
 \begin{gathered}
 K^2=P,\quad K\mathbf1=0,\quad Kx=x,\quad Ky=-y,\quad
 K_{00}=-1/n,\quad (P_+)_{00}=1/2-1/n,\quad (P_-)_{00}=1/2,\
 \dim V_+=(n-2)/2,\qquad\dim V_-=n/2.
 \end{gathered}                                           \tag{25}
\]

This completes the **full-coherence** part of the counterfamily.
It is an exact existence construction for every sufficiently large
`t=2^k`, with a finite constant depending on the fixed floor and background
choice. The proof does not claim that this constant is the optimized
Paley entry constant.

## 5. Complete source spectrum and a positive leakage fraction

We now prove failure of tightness, rather than infer it from the divergent
energy. Since multiplication by `D` preserves `F` and `F^perp`, and `K`
preserves `F`, the plus source measure is supported on the compression to
`span{u,g}`. There are no omitted source modes in the completion.

Set

\[
 E_X=\|X\|^2=E-h^2/p,\qquad F_t=\langle X,DX\rangle.
\tag{26}
\]

The source equation (3), `x=(h/sqrt(p))u+sqrt(E_X)g`, and `g0=0`
give the **exact** matrix and source coordinates

\[
 \boxed{\quad
 T\big|_{\operatorname{span}\{u,g\}}=
 \begin{pmatrix}
 p(Q+F_t)/h^2&-\sqrt p F_t/(h\sqrt{E_X})\\
 -\sqrt p F_t/(h\sqrt{E_X})&F_t/E_X
 \end{pmatrix},\qquad e=(\sqrt p,0).
 \quad}                                                   \tag{27}
\]

For example, the second row of `Tx=be` determines the off-diagonal,
and the first determines the upper diagonal. All entries also equal the
direct diagonal-weighted sums in the replay. The determinant is
`p F_t Q/(h² E_X)>0`.

Here `F_t` tends to a **strictly positive finite constant**. An explicit
formula makes this check independent of numerical solves. Put

\[
 s_* = \sqrt{1+\tau},\quad S_1^*=s_*+d,\quad S_2^*=s_*-d,
 \quad D_j^*=\sqrt{(S_j^*)^2-\tau},\quad
 \mathbf k^*=\frac{2\mathbf D^*}{|\mathbf D^*|^2}
 -\sqrt{2-\frac4{|\mathbf D^*|^2}}
                 \frac{(\mathbf D^*)^\perp}{|\mathbf D^*|}.
\tag{28}
\]

With `delta1=d`, `delta2=-d`, `zj=Dj*-kj*`, the limit is

\[
 \boxed{\quad
 F_*=\frac1{2s_*}\sum_{j=1}^2
 \left[S_j^*(\delta_j^2+z_j^2)-2D_j^*\delta_j z_j\right]>0.
 \quad}                                                   \tag{29}
\]

To verify (29), on background `j+` and `j-`, respectively, the limiting
scaled values of `X` are `deltaj+zj` and `deltaj-zj`. The limiting
diagonal weights are `(Sj*-Dj*)/s*` and `(Sj*+Dj*)/s*`, and `M/n -> 1/4`.
The tail contribution to `F_t` is `O_tau(mH/n)=O_tau(1/t)`, the neutral
contribution is `o(1)`, and the root contribution vanishes exactly.
Summing proves (29). Both background weights are strictly positive
because `tau>0`. Their weighted squares cannot all vanish when `d>0`,
which proves the strict inequality without relying on rounded decimals.

Since `Q,h -> 1`, `p -> 1/2`, `E_X/E -> 1`, (27) yields

\[
 \lambda_{\rm small}E\longrightarrow\frac{F_*}{1+F_*},
 \qquad \lambda_{\rm large}\longrightarrow\frac{1+F_*}{2}.
\tag{30}
\]

The inverse mass on the large eigenvalue tends to
`b² p/lambda_large -> 1/(1+F*)`, while the total tends to one.
Therefore

\[
 \boxed{\quad
 \nu(\{\lambda_{\rm small}\})\longrightarrow
 \eta_\tau:=\frac{F_*}{1+F_*}>0,\qquad
 \lim_{\epsilon\downarrow0}\limsup_{t\to\infty}
       \nu((0,\epsilon])=\eta_\tau.
 \quad}                                                   \tag{31}
\]

This is the actual source generated by the exact stationary pair, with
the exact reciprocal diagonal. A divergent second inverse moment alone
would not have proved (31).

For `tau=.05`, `d=(3/5)(sqrt(1.05)-sqrt(.05))`, the algebraic limit is

\[
 F_*\simeq .4541482549282572,\qquad
 \eta_\tau\simeq .3123122098376849.
\tag{32}
\]

## 6. Consequence for the mark-stripped weighted leakage

Use the actual quantities of source-pair 29:

\[
 \theta_i=\frac\delta{d_i+\delta},\qquad
 t_\delta=\theta x-\theta_0x_0e_0,\qquad
 \ell_\delta^2=\sum_i(d_i+\delta)[P_-t_\delta]_i^2.
\]

Their finite resolvent certificate gives

\[
 \Delta_\delta\le S_\delta+
    (\text{mark cost}+\text{mean cost}+\ell_\delta)^2,
 \qquad
 \Delta_\delta=\int\frac\delta{\lambda+\delta}\,d\nu.
\tag{33}
\]

The spatial and mean costs vanish in the field-first, then
`delta -> 0` order by UI; the stripped mark cost vanishes as well.
But (30)--(31) give

\[
 \lim_{\delta\downarrow0}\lim_{t\to\infty}\Delta_\delta
 =\eta_\tau.
\]

Consequently

\[
 \boxed{\quad
 \liminf_{\delta\downarrow0}\liminf_{t\to\infty}
       \ell_{t,\delta}\ge\sqrt{\eta_\tau}>0.
 \quad}                                                   \tag{34}
\]

Thus uniform entry coherence cannot supply the vanishing weighted
opposite leakage required there. The stronger requirement with actual
Paley convolution or arithmetic has not been tested by this counterfamily.
The [top-tail transfer note](top-tail-transfer-30.md) already blocks a
generic propagation estimate for arbitrary errors; the obstruction here
additionally imposes the full nonlinear stationary pair. Neither one
produces an actual prime Paley orbit error or prime stationary counterexample.

## 7. What full coherence does control: some inverse mass must remain

There is a complementary finite bound. It explains why retaining the
round-29 *all-mass* collapse would be too much to ask under a fixed entry
constant and these root data.

For any stationary pair with `|Kij|<=C/sqrt(n)`, let `p=(P_+)00` and keep
the notation `b,d,e,T,mu,nu,Q` of Section 1, allowing general `A0`.
For `i!=0`, `|ei|<= (C+n^(-1/2))/(2sqrt(n))`. The true mass identity
`sum d=n-b/a<n` therefore gives

\[
 M_1:=\int\lambda\,d\mu
 =\sum_i d_i e_i^2
 \le p^2d_0+\frac{(C+n^{-1/2})^2}{4}=:M.
\tag{35}
\]

Moreover `mu((0,epsilon]) <= epsilon Q/b²`, since
`dmu=lambda dnu/b²`. Cauchy--Schwarz on the remaining spectrum gives
the explicit bound

\[
 \boxed{\quad
 \nu((\epsilon,\infty))\ge
 \frac{b^2}{M}
 \left(p-\frac{\epsilon Q}{b^2}\right)_+^2.
 \quad}                                                   \tag{36}
\]

Indeed its squared unweighted mass is at most
`(int lambda dmu)(int lambda^(-1) dmu)` on that spectrum.
At fixed floor and fixed coherence, positivity and `K A=A-a1` give
`A0,B0<=a+C sqrt(W)`; their root product is one, so both are also bounded
below. Thus `b` stays bounded above and below, and `d0=O(n^(-1/2))`.
With the Paley marked value `p -> 1/2`, the right side of (36) has a
strictly positive ordered lower limit.

In our `A0=1` family, (36) in particular gives a retained inverse mass
at least `1/C²` in the ordered limit. It does **not** force all inverse
mass to remain: (31) exhibits the positive amount that can escape.
This is a genuine limited source consequence of coherence, rather than
a vanishing leakage estimate.

## 8. Stationarity, replay and scope

At each finite dimension all weights are positive. The construction
proves the existence of its fixed point exactly. On any finite ball
about that point, all scalar derivatives
`|vi|/sqrt(vi²+4wi)` are bounded by a common number less than one.
Since `||K||2<=1`, `K Phi` is a strict contraction on that ball and maps
it into itself. A ball containing zero proves zero-start Picard convergence;
one containing any proposed second fixed point proves uniqueness. No
uniform-time rate is asserted.

Replay from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-coherent-source-31.py \
  > research/parallel-coherent-source-31.jsonl
```

The script has no file-write operations; the displayed shell redirection
creates the allowed JSONL file. Its ten records comprise one algebraic
limit, seven invariant-block members and two independent full-matrix replays,
the second seeded by the actual prime Paley matrix at `p=1033`.
The large `n` values are handled in the normalized eight-group basis.
Those rows do **not** pretend that a huge full matrix was constructed.
Their full uniform-coherence completion is proved in Section 4.

Some block results at `tau=.05`:

| `t` | `E` | `lambda_small` | Small inverse-first mass | Tail source first mass |
|---:|---:|---:|---:|---:|
| 8 | 34.213534 | .00894325 | .29710021 | .12489084 |
| 32 | 514.398499 | .000599305 | .30770707 | .03124957 |
| 256 | 32770.454057 | .00000951169 | .31169324 | .00390625 |
| 4096 | 8388610.461554 | .0000000372259 | .31227314 | .000244141 |

For a feasible small **auxiliary** choice `n=512,m=16,H=4`, the script
actually constructs the full matrix, implants all five directions of
`F0`, and checks **all 262144 entries**. It finds

* full coherence constant `sqrt(n) max_ij |Kij| = 3.3447213676`;
* root-row constant `1.5113060365`;
* sector dimensions `255,256`, `K00=-1/512` and
  `(P_+)00=1/2-1/512`;
* full stationary residual below `7.8e-14`, reflection error below
  `1.3e-13`, and full source/block errors below `2.0e-14`.

This finite replay uses seeded projected numerical nullspaces to choose
helper eigenvectors. Section 4's asymptotic proof uses sparse cube vertices
and proves existence with uniform constants. The replay constant is **not**
claimed as a uniform asymptotic constant, and the small choice `H=4` is
not the asymptotic prescription `H=t³`. All decimals are floating-point
normalization checks, not interval-certified stationary solves. The
stationary and asymptotic assertions have algebraic proofs above.

The retained and lost properties are precise:

| Property | Status in this family |
|---|---|
| Exact positive nonlinear stationary point; zero-start limit | Retained |
| `w0=1`, bulk `tau/n`, exact two masses and root product | Retained |
| Both reciprocal diagonals, exceptional marked product, full source identities | Retained |
| Paley sector dimensions and marked projector values | Retained |
| Source UI, both `E ~ t²/2 = o(sqrt(n))`, root coordinate caps | Retained |
| Full uniform entry coherence, all rows and columns | Retained, with some finite `C_tau` |
| Marker `v0=gamma0=0` | Retained |
| All inverse mass collapsing to zero | Replaced by a proved positive fraction |
| Final translation invariance or sector convolution closure | Not retained |
| Actual prime Paley dimensions and actual Paley starting matrix | Also supplied in Section 9 |
| Final cyclic circulant multiplier or actual Paley sign | Not retained |

There is a direct obstruction to interpreting even this pair as a Walsh
convolution example. Label the four background cosets `00,01,10,11`, with
the first two making background pair 1. The nonconstant quotient character
`chi` equal to plus one on the first pair and minus one on the second has

\[
 n^{-1/2}\sum_i\chi(i)A_i\longrightarrow d,\qquad
 n^{-1/2}\sum_i\chi(i)B_i\longrightarrow d.
\tag{37}
\]

The backgrounds contribute `4Md/n -> d` to each. The tails contribute
`O(1/t)`, and the neutral and marked contributions vanish. Thus both
spectra have the **same nonconstant Fourier character** with a nonzero
coefficient. They cannot occupy complementary sectors of any Walsh
convolution reflection. This detects the lost convolution structure
directly, independently of the choice of completion helpers. Neither this
observation nor the prime-seeded extension below supplies a final cyclic
convolution or Paley-sign matrix.

The inherited source-pair and audit notes correctly left full coherence
open: their marked row diverged. The construction here closes that
specific gap for **general reflections**. A prime proof of inverse
tightness must use more than the listed stationary equations, UI and a
uniform entry constant. This result does not decide whether convolution
closure suffices, and does not resolve Problem 26.

## 9. Actual prime Paley seeds and dimensions: a rank-twelve corollary

**Corollary.** Fix the same `tau,d` as above. For every sufficiently large
prime `ell=1 mod 8`, put

\[
 n=(\ell-1)/2,\quad t=(n/2)^{1/8},\quad
 m=\lfloor\sqrt{n/2}\rfloor=\lfloor t^4\rfloor,\quad
 H=t^3,\quad M=n/4-m,\quad r_N=2m-1.
\tag{38}
\]

There is a real orthogonal `V`, fixing the constant vector and the marked
coordinate, such that

\[
 \boxed{\quad K=V K_{\rm Paley}(\ell)V^T,\qquad
 \operatorname{rank}(V-I)\le6,\qquad
 \operatorname{rank}(K-K_{\rm Paley}(\ell))\le12.\quad}
\tag{39}
\]

This `K` has the full uniform entry bound (1), the exact stationary pair
(2), all the dimensions and marked data (25), source UI, both subcritical
divergent energies, and the same nonzero leakage limit (31). The final
matrix is not cyclic convolution for all sufficiently large `ell`.
The pair is stationary for **this conjugated matrix**, not for the actual
Paley starting matrix.

**Proof.** Use coordinates `Z/nZ`. If `g` is a primitive root modulo
`ell`, the actual Paley multiplier is

\[
 s(j)=\chi(1-g^{2j}),\qquad
 K_{\rm Paley}=\mathcal F\operatorname{diag}(s)\mathcal F^{-1}.
\]

Here `s(0)=0`, every other value is plus or minus one, `sum s=-1`,
and `s(-j)=s(j)`. Thus the matrix is real symmetric, squares to `P`,
has constant diagonal `-1/n`, and has the sector dimensions in (25).
The Jacobi bound from the [Fourier notes](fourier.md) gives

\[
 |(K_{\rm Paley})_{ij}|\le\frac{\sqrt\ell}{n}
 =\frac{\sqrt{2+1/n}}{\sqrt n}.
\tag{40}
\]

These are facts about the **actual** seed, not an arbitrary sign
multiplier substituted for it. The new argument needs no further
Jacobi-sum law.

Since `4` divides `n`, take the four cosets `C_a={i:i=a mod 4}`.
Their normalized indicators have only four cyclic Fourier frequencies.
The absolute values of their four unitary Fourier coefficients are
`1/2`, so every coordinate of their `K_Paley` images is at most
`2/sqrt(n)`. Remove exactly `m` points from each coset, including the
root, and use the remainders as the four backgrounds. The removed-point
error is bounded by the analogue of (18) using (40), and is
`O(n^(-1/2))` because `m=O(sqrt(n))`, `M~n/4`.

Construct the pair, root row and finite block by the **same exact formulas**
(7), (12)--(15). Rounding `m` changes none of their mass or product
identities: the group sizes and (7) are used exactly. Also

\[
 m=t^4+O(1),\qquad S=s_\infty-1/(2t)+O_\tau(t^{-4}),\qquad
 E=t^2/2+O_\tau(1).
\]

Thus the root-row feasibility radical stays positive and every limiting
calculation in Sections 2, 3, 5 and 6 is unchanged. In particular `F_*`
and the leakage fraction are the same as (29)--(32).

Sections 4.2--4.3 require only: the fixed coherence constant, the seed
dimensions and marked diagonal, the four background-indicator image
bounds, and `m~sqrt(n/2)`. All have just been checked. Those sections
therefore construct `K=U K1 U^T`, where
`K1=U0 K_Paley U0^T`. Here `rank(U0-I)=1`, and `U-I` has rank five
because its five Householder normals are orthonormal. Set `V=U U0`.
Then `V` fixes `j,e0` and `rank(V-I)<=6`. Finally

\[
 K-K_{\rm Paley}=(V-I)K_{\rm Paley}V^T
                  +K_{\rm Paley}(V^T-I)
\]

proves the rank-twelve bound. The proof of full uniform coherence is
unchanged; no assumption that `n` is a power of two remains.

For completeness, primes `1 mod 8` are infinite by an elementary
argument. If there were only finitely many, take an even integer `X`
divisible by all of them. Every prime factor `q` of `X^4+1` is odd,
does not divide `X`, and gives multiplicative order exactly eight to
`X mod q`. Hence `q=1 mod 8`, contradicting the choice of `X`.

**The final matrix is not cyclic convolution.** This assertion can be
proved directly for the constructed pair, independently of how the
completion helpers are selected. Assign `C0,C1` to background pair 1
and `C2,C3` to background pair 2. For the nontrivial quotient character
`psi(r)=exp(2 pi sqrt(-1) r/4)`, put `Delta=D1*-D2*`. The backgrounds and the
vanishing tail/neutral/root errors give

\[
 \begin{aligned}
 n^{-1/2}\sum_i\psi(i)A_i
 &\longrightarrow \frac{2d+\Delta+\mathrm i(2d-\Delta)}4,\\
 n^{-1/2}\sum_i\psi(i)B_i
 &\longrightarrow \frac{2d-\Delta+\mathrm i(2d+\Delta)}4.
 \end{aligned}                                            \tag{41}
\]

Both limits are nonzero because `d>0`. Thus the two centered spectra
share a nonconstant cyclic Fourier frequency. They cannot belong to
opposite eigensectors of **any** cyclic convolution reflection. Since
our final `K` has `Kx=x`, `Ky=-y`, it cannot be such a convolution.
This proves the asserted loss of structure for the actual prime-seeded
corollary, rather than relying on the earlier Walsh test (37).

**Low rank is not a small perturbation.** The same background-indicator
bounds give `||K_Paley r||infty=O(n^(-1/2))`. As in (19),
`<K_Paley e0,r>=O(n^(-1/2))`. Since both vectors have squared norm
`1-1/n`,

\[
 \boxed{\quad
 \|K-K_{\rm Paley}\|_{2\to2}
 \ge\|(K-K_{\rm Paley})e_0\|
 =\|r-K_{\rm Paley}e_0\|\longrightarrow\sqrt2.
 \quad}                                                   \tag{42}
\]

In particular the Jacobi root-row law and the actual Paley initial
Picard field are not retained. Cyclic inversion symmetry is also lost:
`Delta>2d` since the derivative of `sqrt(S²-tau)` is greater than one.
Thus both limits in (41) have nonzero imaginary part, and the constructed
cyclic spectra are not inversion-even for all sufficiently large sizes.
The corollary rules out deductions using only the listed algebra,
coherence, the actual dimensions and the unlabeled operator spectrum.
It remains a statement about other reflections at prime Paley dimensions.
It supplies no actual Paley stationary counterexample.

**Additional full-matrix replay.** The script retains its original
`n=512` Walsh probe and adds the actual Paley seed at `ell=1033`,
`n=516,m=16,H=4`. The integer Legendre signs and primality of `1033`
are checked in the script. All `266256` matrix entries are inspected.
The output gives:

| Check | Value |
|---|---:|
| Seed coherence constant | `1.4148593322` |
| Final full coherence constant | `3.2120598702` |
| Stationary residual | `<5.6e-15` |
| Reflection error | `<5.4e-14` |
| Sector dimensions | `257,258` |
| `rank(V-I)`, `rank(K-K_Paley)` | `6,12` |
| `||K-V K_Paley V^T||_F` | `<4.4e-14` |
| `||K-K_Paley||_(2->2)` | `1.9486065051` |
| Cyclic translation defect `||K-S K S^-1||_F` | `6.6943883355` |
| Maximum minus minimum diagonal entry | `.1492035016` |

Both the translation defect and nonconstant diagonal detect failure of
circulant structure in this specific finite matrix. The rank checks use
numerical threshold `1e-8`; (39) is the exact algebraic proof. Like the
Walsh probe, `H=4` is an auxiliary finite prescription, not an asymptotic
test. All numerical statements remain floating-point diagnostics.

Only `research/parallel-coherent-source-31.md`, `.py` and `.jsonl` were
written. No shared files, commits, pushes, settings, credentials, other
projects or external communications were used or changed.
