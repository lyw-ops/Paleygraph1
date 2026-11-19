# What can actually be extracted from a fixed-margin witness

Round 26, ordinary theta. The prime assertion in [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) remains open. This note treats the actual obstruction class (18) of [Round 25](parallel-cells-25.md), with the weights of [pinned penalty](pinned-penalty-24.md). It does not replace general witnesses by subgroup indicators.

The main findings are:

* The upper energy bound in that class is automatic: **every** feasible witness satisfies `e(W) <= nu(W)^2`. Thus this bound cannot supply the missing concentration.
* A positive **lower** energy bound gives a high truncation on a constant multiple of the critical number of coordinates, with an explicit relative sector error. It does not give asymptotically critical size, a flat indicator, or high additive energy.
* Near-critical collision size does give a quantitative, explicit high-layer extraction. The required hypothesis is energy **saturation**, not just a positive energy lower bound.
* An exact square-order family with a fixed mass margin and positive limiting energy refutes both direct near-critical collision-size extraction and direct weighted phase concentration. Autocorrelation destroys its mass margin. Pointwise powers, which improve its mass, do not preserve the sector for general witnesses: an exact bad witness at `p=17` demonstrates this.

The square example still has a critical high layer. It is not a counterexample to the desired assertion that **some** such layer can be extracted from every prime obstruction.

## 1. Normalizations and an automatic energy bound

Let `q=1 mod 4` be an odd field order, `n=(q-1)/2`, `Q` the nonzero squares, and `G=Q^` its cyclic character group. All vector norms and sums below use counting measure. Set

\[
s(x)=\chi(1-x),\qquad
\lambda_j=\sum_{x\in Q}s(x)j(x),\qquad
k_j=\lambda_j/\sqrt q,\qquad m_0=n/\sqrt q.
\]

The real symmetric convolution `K` on `G` has entries `K_ij=lambda_(i-j)/n`; its Fourier multipliers are `s`. With `J=11^T/n`, put

\[
P=P_{-\sigma}=(I-J-\sigma K)/2,\qquad U_\sigma=\ker P.
\]

In particular, for `W in U_sigma`,

\[
KW=\sigma(W-S\mathbf1/n),\qquad S=\sum_iW_i.       \tag{1}
\]

The bound `|k_j|<=1` needs no prime-specific input. For completeness, additive Paley convolution `T_xy=q^(-1/2) chi(x-y)` satisfies `T^2=I-J_add`, by the quadratic-character correlation identity. Its compression to `Q` is diagonal in multiplicative characters, with eigenvalues `k_j` (substitute `y=xu` and use `chi(x)=1`). Its norm is at most one. This proves the bound, including the exceptional trivial character. The character correlation itself follows from counting solutions of `v^2=u^2-a`, for nonzero `a`, using `(u-v)(u+v)=a`.

Assume `W>=0`, `W_0=1`, and `PW=0`. Write

\[
T=\sum_i W_i^2,\qquad \nu=S/\sqrt n,\qquad
m_{\rm eff}=S^2/T,\qquad \mathcal L=m_{\rm eff}/m_0.
\tag{2}
\]

Here collision size includes the mark. When energy is bounded below, removing the mark changes it by `1+o(1)`.

Use exactly the repair geometry in pinned penalty:

\[
\ell=Pe_0,\quad \kappa=P_{00},\quad
L=P-\ell\ell^\mathsf T/\kappa,\quad M=\mathbf1-\ell/\kappa,
\]

and the nonnegative zero-mark, mean-one repair rows `R^(i)` whose receiving heights are `h_i=R^(i)_i`. These are `R^(i)=M+eta L e_i`, with

\[
\omega=\frac{1+\sqrt q}{2n},\qquad
\eta=\frac{1-\omega/\kappa}{\omega+\omega^2/\kappa},\qquad
h_i=M_i[1+\eta(\kappa+\ell_i)].
\]

The usual positive-padding assumption is in force. To recall why these are nonnegative: off the root and receiving site, `L_ji>=-omega-omega^2/kappa` and `M_j>=1-omega/kappa`; the receiving diagonal is nonnegative. They belong to the opposite sector, have mean one and vanish at the root.

Complementary Fourier support gives, **exactly**,

\[
\langle W,R^{(i)}\rangle=S,\qquad \langle W,M\rangle=S.
\]

Since both rows in the first pairing are nonnegative,

\[
h_iW_i\le S\quad(i\ne0),\qquad
\sum_{i\ne0}M_iW_i=S.
\]

Therefore

\[
\boxed{\quad
e(W)=\frac1n\sum_{i\ne0}M_i h_iW_i^2
\le\frac Sn\sum_{i\ne0}M_iW_i
=\frac{S^2}{n}=\nu(W)^2.
\quad}                                                    \tag{3}
\]

Thus `nu<=c=(1+epsilon)^(-1)` implies `e<=c^2`, for all feasible witnesses, without choosing an optimizer. The quantifier over `E` in Round 25's equivalence is legitimate, but an upper energy cap at `E=c^2` excludes nothing further. It is not a compactness or concentration hypothesis.

There is also an exact probability interpretation. Put

\[
\pi_i=M_iW_i/S,\qquad x_i=h_iW_i/S\quad(i\ne0).
\]

Then `sum pi=1`, `0<=x_i<=1`, and

\[
e/\nu^2=\sum_i\pi_ix_i.                                  \tag{4}
\]

Consequently `e >= (1-delta) nu^2` forces `pi{x<=1-t}<=delta/t`. This is a **saturation** statement. A bound `e>=e_0>0` need not put the expectation close to one.

## 2. What a lower energy bound adds, and what it does not

Equation (1) and `|K_ij|<=1/m_0` give a uniform point cap on the whole vector:

\[
0\le W_i\le B_*:=\frac{S}{m_0}(1+q^{-1/2}).               \tag{5}
\]

Thus `S>=m_0/(1+q^(-1/2))` and `T<=B_* S`. Under `nu<=c<1`, the root-normalized witnesses have bounded height, and `nu` stays bounded below by `1/sqrt(2)+o(1)`. One can also translate a maximum to the root and divide by that maximum to arrange `0<=W<=1`, without increasing mass. The resulting energy again satisfies (3). A positive energy lower bound survives this operation up to a constant factor, by (5) and the uniform weight asymptotics below.

Uniformly off the root and in the sign,

\[
M_i h_i=m_0(1+O(q^{-1/2})),\qquad
e=(1+O(q^{-1/2}))\frac{T-1}{\sqrt q}.
\tag{6}
\]

In particular, if `e>=e_0>0`, then

\[
\boxed{\qquad
\mathcal L=\frac{\nu^2}{T/\sqrt q}
\le \frac{c^2}{e_0}+o(1).
\qquad}                                                   \tag{7}
\]

Without a lower energy bound, (3) and the obstruction definition allow `e->0`, equivalently `mathcal L->infinity` along a bounded-mass witness sequence. This states what the assumptions allow; it does **not** construct such a prime sequence. A positive lower bound only makes `mathcal L` bounded. Near-critical collision size would require `mathcal L->1`, equivalently `e/nu^2->1` in this regime.

### An explicit truncation with controlled sector error

For any `C>mathcal L`, let

\[
t=\frac{S}{Cm_0},\qquad A=\{i:W_i\ge t\},\qquad z=W\mathbf1_A.
\]

Then

\[
\boxed{\begin{aligned}
|A|&\le Cm_0,\\
\|W-z\|_2^2&\le tS=(\mathcal L/C)T,\\
\|z\|_2^2&\ge(1-\mathcal L/C)T,\\
\frac{\|Pz\|_2^2}{\|z\|_2^2}
&\le\frac{\mathcal L}{C-\mathcal L}.
\end{aligned}}                                            \tag{8}
\]

The second line uses `W_i^2<=tW_i` below the threshold; the last uses `Pz=-P(W-z)` and the contraction property of an orthogonal projection. If also `C>S/m_0`, then `t<1`, so **`z_0=1` and `sum z<=S`**. The mass margin survives this truncation; exact sector membership is replaced by the displayed error.

With `e>=e_0`, taking a sufficiently large fixed `C` gives a support on a constant multiple of the critical scale and any prescribed fixed relative sector error. Making the error tend to zero by this argument requires `C` to grow. It does not yield a fixed critical support with an error tending to zero.

There is also a high amplitude shell of this scale. Take `C=2mathcal L`, increasing it if needed to keep the root. The retained part carries at least half of `T`, and

\[
B_*/t=C(1+q^{-1/2}).
\]

Partition its amplitudes into `J=O(log(2+C))` dyadic shells. One shell carries at least `T/(2J)` squared mass. Its cardinality is between `T/(2J B_*^2)` and `Cm_0`, hence is comparable to `m_0` when `e>=e_0`. **The sector error of an individual shell is not controlled by (8)**: forbidden components of distinct shells can cancel.

A concrete sufficient prime estimate for using (8), without pretending the support is a subgroup, would be

\[
\gamma_p(C):=\inf_{\substack{v\ge0,\ v\ne0\\
|\operatorname{supp}v|\le Cm_0}}
\frac{\|P_{-\sigma}v\|_2^2}{\|v\|_2^2},\qquad
\liminf_p\gamma_p(C)>\frac{L_0}{C-L_0},                   \tag{9}
\]

for some fixed `C>L_0`, where `mathcal L<=L_0` on the obstruction family. This contradicts (8). Formula (9) is **unproved**. Even knowing merely `liminf gamma_p(C)>0` for each fixed `C` would not automatically meet its quantitative requirement, since that lower bound could decay too quickly with `C`. Existing subgroup estimates do not estimate (9) over arbitrary nonnegative profiles.

## 3. A quantitative extraction when collision size really is near critical

There is a direct finite-field version of the qualitative flatness argument, with no stationarity assumption. Define

\[
\delta=(1+q^{-1/2})\mathcal L-1\ge0,\qquad
u=W/\sqrt T,\qquad a=B_*/\sqrt T.
\]

Assume `delta<1` and use the explicit level

\[
A=\{i:W_i\ge B_*/2\}=\{i:u_i\ge a/2\},\qquad m=|A|.
\]

Then

\[
\boxed{\begin{aligned}
\|u-a\mathbf1_A\|_2^2&\le\delta,\\
\|u_{A^c}\|_2^2&\le\delta,\\
1-\delta\le a^2m&\le1+3\delta,\\
\frac{\|P\mathbf1_A\|_2^2}{m}&\le\frac{\delta}{1-\delta}.
\end{aligned}}                                            \tag{10}
\]

For proof, (5) gives `0<=u_i<=a` and the exact identity

\[
\sum_i u_i(a-u_i)=a\sum_i u_i-1=\delta.
\]

Below `a/2`, `u_i^2<=u_i(a-u_i)`; above it, `(a-u_i)^2<=u_i(a-u_i)`. This proves the first two bounds. Above the threshold,
`a^2-u_i^2 <= 3u_i(a-u_i)`, proving the upper size bound, while the retained norm proves the lower one. Finally `Pu=0` proves the projection bound.

In particular,

\[
\frac{1-\delta}{(1+\delta)(1+q^{-1/2})}
\le\frac m{m_0}\le
\frac{1+3\delta}{(1+\delta)(1+q^{-1/2})}.                  \tag{11}
\]

The signed within-set Jacobi deficit also has an explicit bound. Put

\[
d_\sigma(A)=\frac1{m^2}\sum_{i,j\in A}(1-\sigma k_{i-j}).
\]

Using (1),

\[
\sum_{i,j}u_i u_j(1-\sigma k_{i-j})
=m_{\rm eff}-m_0(1-m_{\rm eff}/n)=m_0\delta.
\]

All summands are nonnegative. On `A x A`, `u_i u_j>=a^2/4`. Therefore

\[
\boxed{\qquad
d_\sigma(A)\le
\frac{4\delta(1+\delta)(1+q^{-1/2})}{(1-\delta)^2}.
\qquad}                                                   \tag{12}
\]

Thus `delta->0` really does give a nonnegligible (indeed asymptotically full-energy), flat, near-critical high layer with signed deficit tending to zero. This is a usable input for subsequent critical-set cap arguments.

It does **not** supply `E(A)>=(1/2+Delta)|A|^3`, where `E(A)=sum_h |A intersect(A+h)|^2`. The high-additive-energy hypothesis in the existing overlap/subgroup reduction is still separate. A positive lower energy bound in (7) supplies neither `delta->0` nor this additive-energy condition.

## 4. Exact bad square witnesses with positive nonsaturating energy

Let `q=r^2`, with `r` an odd prime power, and let `I<=G` be the annihilator of `F_r^*`, so

\[
h=|I|=(r+1)/2,\qquad |G/I|=r-1.
\]

Let `C` be the order-two coset in `G/I`. In cyclic coordinates,

\[
I=(r-1)\mathbb Z/n\mathbb Z,\qquad C=(r-1)/2+I.
\]

For `0<beta<1`, set

\[
W=\mathbf1_I+\beta\mathbf1_C.                             \tag{13}
\]

This is an exact, even, nonnegative, root-normalized witness in `U_+`. Its Fourier transform is supported on `F_r^*`, where `chi_q(1-x)=1` away from 1. In fact the transform is itself nonnegative: at the frequency `kh` it equals `h(1+beta(-1)^k)` and vanishes elsewhere.

Write `L_beta=1+beta`, `Q_beta=1+beta^2`. Exactly,

\[
S=hL_\beta,\quad T=hQ_\beta,\quad
\nu^2=\frac{r+1}{2(r-1)}L_\beta^2,\quad
\mathcal L=\frac r{r-1}\frac{L_\beta^2}{Q_\beta}.
\tag{14}
\]

By (6), `e -> Q_beta/2`. For the rooted squared-weight phase deficit,

\[
\delta_2:=\frac{\sum_iW_i^2(1-k_i)}{T}
=1+\frac1r-\frac{r-1}{rQ_\beta}
\longrightarrow\frac{\beta^2}{1+\beta^2}.                \tag{15}
\]

To check the exact identity, `W^2=1_I+beta^2 1_C` is also in `U_+`, so applying the root equation (1) to `W^2` gives `sum k_iW_i^2=m_0-T/r`. This special closure will matter below. The weighted *pair* deficit is separately

\[
\frac{\sum_{i,j}W_iW_j(1-k_{i-j})}{S^2}
=1+\frac1r-\frac{r-1}{r}\frac{Q_\beta}{L_\beta^2}
\longrightarrow\frac{2\beta}{(1+\beta)^2}.               \tag{16}
\]

Take `beta=1/4`. The limits are

| Quantity | Limit |
|---|---:|
| `nu` | `5/(4 sqrt(2)) = 0.883883...` |
| `e` | `17/32` |
| `m_eff/m_0` | `25/17` |
| `delta_2` | `1/17` |
| weighted pair deficit | `8/25` |

For every odd prime power `r>249/7`, these satisfy `nu<10/11`; hence they belong to the actual square obstruction class with `epsilon=1/10, E=1`, by (3). Both upper and positive lower energy bounds hold, but collision size is not asymptotically critical and neither deficit tends to zero. These conclusions are algebraic, not numerical extrapolations.

There **is** a good high layer: for `beta<t<1`, `{W>=t}=I`. It carries the fraction `1/Q_beta=16/17` of the squared norm when `beta=1/4`, has size asymptotic to `m_0`, signed deficit exactly `2/r`, and additive energy `h^3`. Consequently (13) invalidates the direct whole-witness arguments, not a nonlinear existence theorem about some layer. These mixtures need not minimize mass or defect; they also do not refute a proposed theorem with an additional extremal-selection hypothesis. A successful general extraction must accomplish at least this separation without assuming the coset structure in advance.

## 5. Two natural purification operations have opposite failures

### Fourier-preserving autocorrelation can lose the obstruction

For any real nonnegative feasible `W`, define cyclic autocorrelation

\[
V=\frac{W*\widetilde W}{T},\qquad \widetilde W_i=W_{-i}.
\]

It has `V>=0`, `V_0=1`, `V<=1`, and `V in U_sigma`: its Fourier transform is `|FW|^2/T`, with the same allowed support. But

\[
\boxed{\qquad \sum V=S^2/T=m_{\rm eff}.\qquad}            \tag{17}
\]

If `0<=W<=1`, then `T<=S`, so this operation never decreases mass. For the actual square family (13),

\[
V=\mathbf1_I+\frac{2\beta}{1+\beta^2}\mathbf1_C.
\]

At `beta=1/4`,

\[
\nu(V)\longrightarrow\frac{25}{17\sqrt2}>1,
\]

although `nu(W)<10/11` eventually. Thus even one exact Fourier-preserving autocorrelation can erase the fixed-margin obstruction. Repeating it only increases the secondary coset height toward one.

### Pointwise powers reduce mass but need not preserve the sector

In the special algebra of (13), pointwise powers replace `beta` by `beta^k` and extract `1_I`. This is not a legitimate general operation on `U_sigma`.

Here is an exact example already inside a prime fixed-margin obstruction class. At `p=17`, use primitive root 3 and index `G` by `0,...,7`. The positional signs are

\[
s=(0,1,-1,-1,1,-1,-1,1).
\]

Set `x=2-sqrt(2)`, `y=3-2sqrt(2)` and

\[
W=(1,0,0,x,y,x,0,0).
\tag{18}
\]

It is nonnegative, at most one, and its Fourier coefficients at all forbidden positions `1,4,7` vanish: at 1 the expression is `1-sqrt(2)x-y=0`, and at 4 it is `1-2x+y=0`. Thus `W in U_-`, with

\[
S=8-4\sqrt2,\qquad \nu=2\sqrt2-2<10/11.
\]

For its pointwise square, however,

\[
\widehat{W^2}(1)=-8+6\sqrt2\ne0,\qquad
\widehat{W^2}(4)=6-4\sqrt2\ne0.                            \tag{19}
\]

The half-level indicator `1_{W>=1/2}=1_{ {0,3,5} }` likewise has forbidden coefficient `1-sqrt(2)` at 1. These are exact closure failures, not projection residuals. This small prime is not an asymptotic counterexample to extraction.

## 6. Remaining hypotheses and checks

The conclusions for the general obstruction class are now quite specific:

1. **Without a lower energy bound**, the upper bound in (18) gives no extra restriction; `mathcal L` may escape. No prime theorem controlling that escape is proved here.
2. **With a lower energy bound**, (8) extracts an anchored, mass-preserving truncation on `O(m_0)` coordinates with a tunable fixed sector error. A prime estimate such as (9), with the stated quantitative comparison, would exclude it. No such general-support estimate is supplied by the subgroup results.
3. **With energy saturation / near-critical collision size**, (10)--(12) give the desired flat near-critical layer explicitly. The further additive-energy hypothesis needed for the existing subgroup reduction remains unproved.
4. A lower energy bound by itself cannot be upgraded to the third case: (13)--(16) give actual square witnesses refuting that inference. They also show why Fourier-preserving autocorrelation is not a remedy. Formula (19) prevents using the square algebra's pointwise purification without a new argument.

The [checker](astra-extraction-26-check.py) verifies (18)--(19) in `Q(sqrt(2))`, constructs the square fields using integer arithmetic, and verifies exact Fourier-sector membership of the coset family from its transform support. It uses 160-bit Arb transforms for the weighted energies, redundant phase/padding checks, and four direct checks of the truncation inequality (8) at `p=17`. The square mixture checks use `r=7,11,13,31,97,389`; pure-subfield controls use `r=7,31,97`. The small mixture rows need not all have the chosen mass margin; the exact threshold is stated above. The rounding inequalities (10) are also checked with rational arithmetic on these rows.

Reproduce with:

```sh
.venv/bin/python -B research/astra-extraction-26-check.py \
  > research/astra-extraction-26-certified.json
```

The [output](astra-extraction-26-certified.json) consists of exact rational/algebraic records and interval enclosures. These checks validate finite identities and the two failed operations. They do not certify stationary points, discover a growing prime obstruction family, prove an additive-energy lower bound, or settle Problem 26. Only files prefixed `research/astra-extraction-26` were created; no shared campaign file, commit, or push was changed.
