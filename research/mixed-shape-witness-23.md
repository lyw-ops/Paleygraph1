# Mixed graph shapes in a Paley Fourier witness

[Potechin and Xu](https://arxiv.org/abs/2609.30064) prove the sharp leading constant for the ordinary Lovász theta of $G(n,1/2)$ using polynomial graph matrices. The [Paley graph-matrix comparison](parallel-graph-shapes-23.md) computes an obstruction to their norm estimates on the deterministic 1-localization. The Paley matrices are all circulant, and their mixed moments are different even for the first path and triangle shapes. The endpoint mask in their construction nonetheless suggests finite Fourier trial families whose feasibility can be checked directly.

## The Fourier columns

Let $s(x)=\chi(1-x)$ on the nonzero square group $Q$, $D_\sigma=\{s=\sigma\}$, $n=(q-1)/2$, and $K=F\operatorname{diag}(s)F^{-1}$, with $F$ the unnormalized Fourier transform. The cyclic convolution of positional rows corresponds to multiplication of their Fourier symbols. For any even real symbol $L$, the edge-supported column is

$$
C_\sigma[L]=F(\mathbf1_{D_\sigma}F^{-1}L)=\tfrac12(L+\sigma KL-\overline L\mathbf1).
\tag{1}
$$

This follows from $2\mathbf1_{D_\sigma}=\mathbf1-\delta_1+\sigma s$. In particular the masked column has mean zero and lies in the nonconstant sector $P_\sigma$.

Put $X=Fs/\sqrt q$, $Y=K(2X^2-1)$ and $Z=K(XY)$. The normalized triangle graph matrix has spectrum $(q/(2n))Y$. The positional row for $Z$ is $2s\cdot(s*(s\cdot(s*s)))/q^{3/2}$, where $*$ denotes unnormalized cyclic convolution. Products of symbols here use matrix multiplication, with no restriction to injective embeddings for the concatenated matrices. The trial columns comprise three nested families.

- **Paths** uses the constant positional row, the opposite-point row, and the inverse symbols $T_j(X)$ for Chebyshev degrees $2$ to $8$. This is the combined family of [the earlier replay](../witnesses.py).
- **Mixed** adds inverse symbols $XY,Y^2,X^2Y,XY^2,Y^3,XZ,YZ,Z^2$.
- **Absolute value** also adds the inverse symbols $|X+dY|$ for $d=-2,-1/2,0,1/2,2$.

All positional rows are masked as in (1). A linear program chooses their coefficients with the diagonal term fixed at one and the off-root spectrum nonnegative. The zero column frequency gives the objective. The final spectrum is independently rounded and checked with [the interval Fourier certificate](../smoothing.py), producing an exact rational lower bound on ordinary theta. This certifies each proposed row after diagonal repair. Numerical LP optima and the sign of their unrounded minima are diagnostics.

## A finite convex-hull test for the leading gain

For any such finite library let $c_q(k)$ denote the vector of off-root column entries at frequency $k\ne0$, and put $v_q=c_q(0)/\sqrt n$ for the vector of normalized objectives. Write $C_q=\operatorname{conv}\{c_q(k):k\ne0\}$. The normalized contribution above the diagonal is

$$
\alpha_q=\max_a\{v_q\cdot a:1+c_q(k)\cdot a\ge0\ (k\ne0)\}.
$$

For $v_q\ne0$, exact LP duality gives

$$
\alpha_q=\frac1{\max\{t>0:-t v_q\in C_q\}}.
\tag{2}
$$

Indeed the dual minimizes $\sum w_k$ subject to $w\ge0$ and $\sum w_kc_q(k)=-v_q$. It is feasible by the zero-mean column identity. Normalizing the weights to sum one gives (2). This also supplies an upper bound for any finite choice of nonnegative weights satisfying the displayed vector identity.

At $q=t^2$ on the minus witness sign, the subfield annihilator $I$ of size $h=(t+1)/2$ lies in the plus sector as an indicator. It is orthogonal to every masked minus column, giving the exact average

$$
\frac1{h-1}\sum_{k\in I\setminus\{0\}}c_q(k)
=-\frac{\sqrt n}{h-1}v_q.
\tag{3}
$$

Consequently (2) recovers the exact square-minus bound $\alpha_q+1/\sqrt n\le h/\sqrt n$, for any library. This identifies the particular vector a fixed family must separate from its prime constraints to improve on $1/\sqrt2$ by a fixed amount. Approximate containment suffices if on a set of at least $\eta n$ modes the entries obey $\|c_p(k)\|\le B$ and the Gram average satisfies $\mathbb E c_p(k)c_p(k)^{\mathsf T}\succeq\gamma I$. In fact a feasible $g(k)=a\cdot c_p(k)$ has mean zero on all modes and is at least $-1$ everywhere, including the root for a trial attaining the maximum. Thus the total $\ell_1$ mass is at most $2n$, and its mean absolute value on the chosen set is at most $2/\eta$. The Gram estimate gives $\mathbb E g^2\ge\gamma\|a\|^2$ there, and $|g|\le B\|a\|$ gives $\|a\|\le2B/(\eta\gamma)$. If $-\sqrt2v_p$ approaches $C_p$, the Fourier constraints and this coefficient bound imply $\limsup_p\alpha_p\le1/\sqrt2$.

The known joint bulk law of $X,Y$ can be used this way for the first path and triangle columns. For the larger library the relevant symbols include $K$ of the mixed products. Weak equidistribution on all prime and square frequencies alone does not transfer (3), since $I$ has vanishing density. A support comparison for the relevant square averages, or a direct prime estimate for (2), remains open.

## Which part of the constraint cloud matters

For a bounded raw symbol $L$, (1) gives its leading mark contribution from one mixed moment:

$$
\frac{C_\sigma[L](0)}{\sqrt n}
=\frac{\sigma}{2}\sqrt{\frac qn}\,\mathbb E(XL)+O_L(n^{-1/2}).
\tag{4}
$$

Here $K_{0k}=\sqrt q X(k)/n$, and the expectation is the arithmetic mean on modes. The [full-mode mixed law](parallel-graph-shapes-23.md) makes $X$ the real part of a Haar circle and $Y$ a mean of two independent Haar $SU(2)$ traces, independently of $X$. Their second moments are both $1/2$. Thus among the first five mixed products only $XY^2$ has a nonzero limiting contribution in (4), equal to $\sigma/(4\sqrt2)$. Chebyshev orthogonality settles the path degrees $2$ to $8$. Simultaneous sign reversal settles the absolute-value inputs. For the opposite-point symbol, $\mathbb E((-1)^kX^2)=(s*s)(-1)/q=O(q^{-1/2})$ by the same complete Legendre sum as in [the triangle calculation](parallel-witness-6.md).

The remaining three products $XZ,YZ,Z^2$ have zero leading contribution as well. In the [bounded Mellin expressions of the fixed-width proof](parallel-fixed-width-13.md#2-mellin-traces-and-the-two-needed-estimates), $X$ is a real negative expression, and $Y$ is one up to a normalized $\ell_2$ error $O(q^{-1/2})$ by applying $K$ to $2X^2-1$. Applying $K$ to their product gives the same kind of approximation for $Z$. All three actual symbols are uniformly bounded: the errors before applying $K$ have ordinary $\ell_2$ norm $O(1)$, which also bounds their image's supremum, and the Mellin expressions are bounded. The three tests $X^2Z,XYZ,XZ^2$ are odd in the joint negative expressions, so their averages tend to zero. Replacing the approximants by the bounded actual symbols changes these averages by $O(q^{-1/2})$.

The constant positional feature has symbol $L_c=\sqrt n e_0$. On the allowed positions $s=\sigma$, so

$$
C_\sigma[X]=\sigma\sqrt{n/q}\,C_\sigma[L_c].
$$

Replacing the mixed symbol $XY^2$ by $X(Y^2-1/2)$ therefore preserves the finite LP and removes its limiting objective. In this basis the only nonzero limiting objective is $1/2$ on the constant positional feature. Its bulk constraint coordinate is $\sigma X/\sqrt2+o(1)$, and $|X|\le1$. Consequently a sequence of convex combinations that realizes the square threshold $-\sqrt2 v$ in (2) must concentrate at $X=-\sigma$. Indeed the constant coordinate's mean is at its minimum, so the nonnegative gap $1+\sigma X$ has expectation tending to zero. The remaining task in this family is to control the joint support of the corrected columns near this face, including $K$ of the mixed symbols. Marginal support for each column does not locate their joint convex hull. The fixed-width Mellin argument gives uniform bounds for the masked even polynomial columns by applying $K$ to the positive expressions. For odd polynomial columns the twist can introduce Kummer terms, which can give exceptional Fourier spikes. Suprema of the absolute-value columns also require a separate estimate.

There is a conditional way to use the sparse square modes. Suppose the good-character tuples of a fixed polynomial library lie in the image of a common compact Mellin group over $\mathbb F_p$ and its even-degree extensions, with uniformly bounded exceptional sets and uniform fixed-degree moment errors on primes. The image is taken in the relevant trace coordinates with bounded complexity. At each $p$, take even extensions of growing degree. If the exceptional subfield modes contribute $o(1)$ to the average in (3) and the good-mode errors tend to zero there, (3) approaches the convex hull of that same image. Uniform moment estimates for the prime tuples then fill this image to arbitrarily small error as $p\to\infty$. More precisely, Haar measure of a fixed-radius group ball centered at a point of the group is bounded below uniformly for subgroups in a fixed unitary dimension, by a finite packing bound and translation invariance. A finite grid of continuous bumps on the feature range, approximated by polynomials, transfers the positive Haar mass to the prime tuples. If the normalized objective is common and the Gram estimate in the previous section holds, this implies the leading upper bound $1/\sqrt2$. The arithmetic component comparison, the exceptional contributions in (3), and the Gram estimate remain to be verified for the full polynomial library.

## Replay

The [replay](mixed-shape-witness-23.py) computes the columns by cyclic FFTs, solves both ordinary theta witness LPs, and calls the existing interval Fourier check. On square orders it verifies that each resulting rational lower bound is at most the exact value. The optional transfer run fixes all coefficients at $p=1000033$, changes the field, and only uses the same rigorous diagonal repair. This checks how far finite fitted coefficients carry across field orders.

The [main sweep](mixed-shape-witness-23-certified.jsonl), [million-order sweep](mixed-shape-witness-23-million-certified.jsonl), and [four-million-order sweep](mixed-shape-witness-23-four-million-certified.jsonl) give 48 rational lower bounds from per-field fitting. The [transfer sweep](mixed-shape-witness-23-transfer-certified.jsonl) gives 18 more. Dividing by $\sqrt n$ and rounding the lower bounds down gives the following comparison.

| Field order | Sign | Paths | Mixed | Absolute value | Absolute value transferred from $1000033$ |
|---:|:---:|---:|---:|---:|---:|
| $153649$ | $+$ | 0.71654470 | 0.76428106 | 0.76804693 | — |
| $153649$ | $-$ | 0.71428179 | 0.76529664 | 0.76788010 | — |
| $1000033$ | $+$ | 0.71154879 | 0.75038437 | 0.75307219 | — |
| $1000033$ | $-$ | 0.70929401 | 0.74754791 | 0.74972857 | — |
| $4000037$ | $+$ | 0.70807086 | 0.74291510 | 0.74507318 | 0.72267321 |
| $4000037$ | $-$ | 0.70884232 | 0.74200661 | 0.74392783 | 0.72601252 |
| $389^2$ | $+$ | 0.71178133 | 0.75992352 | 0.76432465 | — |
| $389^2$ | $-$ | 0.70892687 | 0.70892687 | 0.70892687 | — |

The path-only optimum at any fixed degree has leading constant $1/\sqrt2$ by the [joint Mellin support argument](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain). Thus the added products account for the main finite gain in these comparisons. The largest improvements here are from fitting each field independently. At the separate $997^2$ check, the absolute-value coefficients transferred to the minus sign needed a diagonal increase of about $0.20145$ before normalization. The resulting normalized bound is $0.62415313$, below the exact value $(997+1)/(2\sqrt n)$. These sweeps give no field-uniform lower bound for the mixed family.

As checks on (2)–(3), 24 separate numerical LP dual solves tested both signs and all three libraries at $9413$, $153649$, $97^2$, and $389^2$. The largest dual discrepancy was $1.2\cdot10^{-13}$ and the largest subfield column-sum error was $3.0\cdot10^{-14}$.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/mixed-shape-witness-23.py 9413 37633 153649 --square-roots 97 193 389 \
  --certify-max-order 153649
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/mixed-shape-witness-23.py 1000033 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/mixed-shape-witness-23.py 4000037 --certify-max-order 4000037
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/mixed-shape-witness-23.py 2000029 4000037 --square-roots 997 \
  --train-order 1000033 --certify-max-order 4000037
```
