# Two cell-moment certificates and the gap to relaxed pinning

This continues [Round 24](parallel-vacancy-24.md) for the **ordinary** theta in [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). The uniform prime gap is still open. I obtain two transfer statements, with different cell families:

* A third/fourth **affine** factorial-moment certificate gives a lower bound for nonsquare vacancies, hence a quantitative twist obstruction. It has an exact signed Jacobi-sum expression.
* A field-first product of two **product-cell** tails suffices to exclude twisted critical subgroups. It can ignore escaping cells whose normalized second-moment mass tends to zero, even when their `5/2` moments diverge. It does not assume a uniform weak endpoint bound.

Neither statement is an unconditional growing prime mismatch bound. There is also a precise connection to the [relaxed pinned defect](pinned-penalty-24.md): the full target is equivalent to excluding bounded-energy witnesses with a fixed mass margin. The existing cell reductions only cover special subgroup configurations; extracting such a configuration from every witness in that obstruction class is an additional, unproved requirement. In particular, proving a subgroup moment bound alone must not be reported as proving the relaxed defect estimate or Problem 26.

## 1. Affine cells: a third/fourth moment certificate for vacancies

Let the field have odd order `q=1 mod 4`, and let `B` be an even-order subgroup of the nonzero squares, of size `b`. Its nontrivial order-two character is `d`. Use the **affine** cells of Round 24:

\[
 N_C=\#\{(\alpha,\beta)\in C_1\times C_2:\alpha+\beta=1\},
 \qquad \chi(C_1C_2)=-1.
\]

Define falling factorial moments and two character sums by

\[
 F_j=\sum_{C:\chi(C_1C_2)=-1}(N_C)_j,\qquad
 T=\sum_{x\in B\setminus\{1\}}\chi(1-x),\qquad
 S=\sum_{x\in B\setminus\{1\}}d(x)\chi(1-x).
\]

The correspondence `u=-beta/alpha` identifies the solutions in these cells with all `(q-1)/2` nonsquares. Each solution in a cell of size `N` has affine overlap `R(u)=N-1`, with `Y=(1-B)\{0}` and `R(u)=|Y intersect uY|`. Consequently

\[
 F_1=\frac{q-1}{2},\qquad
 F_2=\frac{(b-1)^2-T^2}{2}.
 \tag{1}
\]

The second identity also follows by counting the ordered pairs in `Y` with opposite quadratic characters. Let `V` be the number of nonsquare vacancies and put

\[
 E=\sum_C N_C(N_C-2)_+.
\]

There is the exact identity

\[
 V=F_1-F_2+E.
 \tag{2}
\]

For the rich cells put `w_C=N_C(N_C-2)`. Then

\[
 F_3=\sum_{N_C\ge3}w_C(N_C-1),\qquad
 F_4+2F_3=\sum_{N_C\ge3}w_C(N_C-1)^2.
\]

Cauchy--Schwarz proves

\[
 \boxed{\quad
 V\ \ge\ \frac{q-1-(b-1)^2+T^2}{2}
       +\frac{F_3^2}{F_4+2F_3}.
 \quad} \tag{3}
\]

The last fraction is defined to be zero if `F_3=0`. It is sharp as a bound for `E` when all rich cells have the same size. Equivalently, for every real `A>0`, the integer occupancy inequality gives

\[
 E\ge\frac{4(AF_3-F_4)}{(A+2)^2}.
 \tag{4}
\]

Optimizing at `A=2+2F_4/F_3` gives (3). Indeed the ratio of the cellwise numerator in (4) to `w_C` is bounded by the maximum of the concave quadratic
`(N-1)(A+3-N)`, namely `(A+2)^2/4`. Thus (4) can also be used as a linear certificate in the two moments before optimizing.

Combining (3) with the [cell-square identity](parallel-vacancy-24.md), `S^2+2V<=q`, gives

\[
 \boxed{\quad
 S^2+T^2+\frac{2F_3^2}{F_4+2F_3}\le (b-1)^2+1.
 \quad} \tag{5}
\]

For either sign, if `r` counts mismatches away from 1, then `S=sigma(b-1-2r)`. In particular,

\[
 \frac{F_3^2}{F_4+2F_3}
 \le 2r(b-1-r)+\frac{1-T^2}{2}.
 \tag{6}
\]

Here `T` is odd, so its square is at least one. A lower bound

\[
 \frac{F_3^2}{F_4+2F_3}\ge c b^2
 \tag{7}
\]

would therefore force `r` to be a fixed positive fraction of `b`, directly from (6). More modest lower bounds have a corresponding growing implication: the left side divided by `2(b-1)` is a lower bound for `r`. This is a sufficiency statement, **not** an estimate of that left side on primes.

For a near-twist sequence, `T=O(r+1)` by the balance of `d`. If `b~sqrt(q)` and `r=o(b)`, (6) forces the left side of (7) to be `o(q)`. Thus a positive-density affine third moment is useful only with control preventing the fourth moment from putting all its weight on a few very rich cells. A lower bound for `F_3` alone does not establish (7).

### Exact Jacobi form of this arithmetic target

Let `k=(q-1)/b`, let `H` be the group of multiplicative characters trivial on `B`, and extend every character, including the trivial character, by zero at zero. Write

\[
 J(\eta,\xi)=\sum_{x+y=1}\eta(x)\xi(y),\qquad
 M_m^- =\sum_{C:\chi(C_1C_2)=-1}N_C^m.
\]

For every integer `m>=1`, character orthogonality gives the exact identity

\[
 \boxed{\quad
 M_m^-=\frac{1}{2k^{2m-2}}
 \left[
 \sum_{\substack{\prod_i\eta_i=1\\\prod_i\xi_i=1}}
       \prod_{i=1}^mJ(\eta_i,\xi_i)
 -
 \sum_{\substack{\prod_i\eta_i=\chi\\\prod_i\xi_i=\chi}}
       \prod_{i=1}^mJ(\eta_i,\xi_i)
 \right],\quad \eta_i,\xi_i\in H.
 \quad} \tag{8}
\]

To prove it, expand
`N(C_1,C_2)=k^{-2} sum eta(C_1)^-1 xi(C_2)^-1 J(eta,xi)`, raise to the `m`th power, and sum with the filter `(1-chi(C_1C_2))/2`. The two character products in (8) are precisely the two surviving orthogonality conditions. Then

\[
 F_3=M_3^- -3M_2^-+2M_1^-,\qquad
 F_4=M_4^- -6M_3^-+11M_2^- -6M_1^-.
\]

Equation (8) specifies which *difference* of Jacobi convolutions has to be estimated. Bounds on the absolute value of each individual Jacobi factor lose the needed cancellation, and apply to the norm-one square example as well. Exceptional trivial-character factors must also be kept: for example `J(1,1)=q-2`, not a quantity bounded by `sqrt(q)`.

## 2. Product cells: an alternative to a uniform `5/2` moment

The rest of the note uses the **different** cells from [Rounds 21--22](parallel-crossratio-22.md). For a multiplicative coset `C` of `B` and `gamma notin {0,1}`, put

\[
 N_C(\gamma)=\#\{(X,Z)\in C^2:
                 (1+X^{-1})(1+Z^{-1})=\gamma\}.
\]

Let `F_C(gamma)<=2` count the solutions with `X=Z`. For an anchor `a in B\{1}` set

\[
 X_a=\{(x-a)/(x-1):x\in B\setminus\{1,a\}\},\qquad
 r_a(u)=|X_a\cap uX_a|.
\]

Delete `u=0,1,a,a^{-1}`, and put the overlap equal to zero at deleted pairs. The exact correspondence from Round 22 is

\[
 \#\{(a,u)\hbox{ in a cell}\}=N_C-F_C,\qquad
 r_a(u)=N_C-2.
 \tag{9}
\]

For positive overlaps the two directions are inverse:

\[
 a=Z/X,\quad u=(1+X)/(1+Z),\qquad
 X=(u-1)/(1-ua),\quad Z=aX.
\]

There can be omitted pairs with zero overlap and no nonempty cell; these have no effect on any moment below. At each anchor there are at most two deleted off-identity ratios. For a fixed cap order their contribution tends to zero even if they have full overlap.

Give each pair `(a,u)` mass `1/((b-1)q)`. For `t>=1` define the two **joint**, not anchor-mean, quantities

\[
 \begin{aligned}
 A_q(t)&=\frac{1}{(b-1)q}
       \sum_C (N_C-F_C)(N_C-2)^2\,
                        \mathbf1_{\{2<N_C\le t+2\}},\\
 B_q(t)&=\frac{1}{(b-1)q}
       \sum_C (N_C-F_C)(N_C-2)\,
                        \mathbf1_{\{N_C>t+2\}}.
 \end{aligned} \tag{10}
\]

The sum includes all `gamma notin {0,1}`. Thus `A_q` is a truncated third cell moment, and `B_q` is a tail of the second cell moment. The elementary estimate

\[
 \sum_{\gamma,C}N_C^2\le b^3+2b(q-1)
 \tag{11}
\]

implies a uniform bound for `B_q(t)` when `b~sqrt(q)`, and bounds `A_q(t)` by a constant times `t`. It does not prove that `B_q(t)` tends to zero uniformly with `t`.

### A finite cap inequality

The [smooth Jacobi cap](parallel-rectangle-20.md) has coefficients `a_M` and off-identity magnitude `v_M(u)=sqrt(q)|a_M(u)|`. Its bounds, from the Jacobi lift and [Xi's character-sum estimates](https://arxiv.org/pdf/1809.04286), are

\[
 |a_M(1)|\ll M^{-1/2}+q^{-1/4},\quad
 \|v_M\|_{L^2(1/q)}\ll M^{-1/4}+q^{-1/8},\quad
 \|v_M\|_\infty\ll\sqrt M+q^{-1/2}.
 \tag{12}
\]

For any family of anchor correlations dominated by `r_a`, the normalized off-identity cap pairing on undeleted ratios is at most

\[
 \boxed{\quad
 \frac{\sqrt q}{b}
 \left[\|v_M\|_2\sqrt{A_q(t)}+\|v_M\|_\infty B_q(t)\right].
 \quad} \tag{13}
\]

Indeed use Cauchy--Schwarz on the joint pairs with `r_a<=t`, and the pointwise coefficient bound on the rest. The `L^2` norm of `v_M` in the joint space is at most its `1/q` field norm. Restricting to square ratios only decreases these bounds. Averaging over good anchors changes (13) by at most the ratio of the number of all anchors to good anchors.

Suppose now that `chi(1-x)=sigma d(x)` outside an exceptional set of `e` elements of `B`, including 1. For each good anchor, the squared norm of the filtered/scaled indicator is `b-O(e+1)`, and its Paley deficit is

\[
 O\bigl(b(e/b+|b/\sqrt q-1|+b^{-1})\bigr).
\]

Its cap mass divided by `b` is consequently `1-o(1)` along a critical near-twist sequence, for every fixed `M`. The identity coefficient contributes the first term in (12); the deleted ratios cost `O(sqrt(M)/sqrt(q))`. More explicitly, for `e/b<1/4`, (12)--(13) imply, with a constant uniform in a fixed critical size window,

\[
\begin{aligned}
1\le C\big[&M(e/b+|b/\sqrt q-1|+b^{-1})+M^{-1/2}+q^{-1/4}\\
 &+(M^{-1/4}+q^{-1/8})\sqrt{A_q(t)}
 +(\sqrt M+q^{-1/2})B_q(t)+\sqrt M/\sqrt q\big].
\end{aligned} \tag{14}
\]

This is a quantitative transfer from product-cell moments to a twist mismatch, not a bound for the moments themselves.

### A field-first tail-product criterion

Fix a family of prime subgroups with `b/sqrt(p)->1`, and put

\[
 A(t)=\limsup_p A_p(t),\qquad B(t)=\limsup_p B_p(t).
\]

If there are fixed thresholds tending to infinity such that

\[
 \boxed{\qquad \liminf_{t\to\infty}(1+A(t))B(t)=0,\qquad} \tag{15}
\]

then that family cannot have `e=o(b)` for either twist sign.

For proof, pass to the field limit in (14) for fixed `t,M`. Under a supposed near-twist it gives

\[
 1\le C\big[M^{-1/2}+M^{-1/4}\sqrt{A(t)}+\sqrt M B(t)\big].
 \tag{16}
\]

Write `U=1+A(t)`. When `B(t)>0`, choose an integer `M` comparable to `U^{2/3}B(t)^{-4/3}`. The two off-identity terms are `O((U B(t))^{1/3})`, and the diagonal term tends to zero when `U B(t)` does. If `B(t)=0` for some fixed `t`, send `M` to infinity at that `t`. This contradicts (16). Every selected `M` is fixed before the field limit; no growing-order character-sum estimate or exchange of limits is used.

Condition (15) is an alternative to the finite-index Lorentz conditions in Round 22. No claim is made that either condition implies the other for every varying family. It can work without a uniform weak bound and without a uniform `5/2` cell moment. For an **abstract occupancy model**, let `b=m^6`, take `m^9` rich cells of size `m^4`, and have the remaining cells contribute bounded truncated third moments. Their normalized second-moment tail is at most

\[
 b^{-3}m^9m^8=m^{-1},
\]

while their normalized `5/2` moment is `b^{-3}m^9m^{10}=m`. For fixed thresholds, the escaping rich cells disappear from both the field-first truncated moment and the field-first second-moment tail. Thus (15) can pass while every uniform finite-index `5/2` Lorentz bound fails. The model respects the scale `N<=b^{2/3}` and (11), but is **not asserted to occur for Paley cells**.

## 3. What this does, and does not, imply for relaxed pinned defects

Use the weighted normalization of [pinned penalty, (1)](pinned-penalty-24.md):

\[
 \nu(W)=\frac{\sum W}{\sqrt n},\qquad
 e(W)=\frac1n\sum_{i\ne0}M_i h_iW_i^2,\qquad
 D_p(1,1+\epsilon)^2=
 \max_{\substack{W\ge0,\ W_0=1\\W\in U_\sigma}}
 \frac{(1-(1+\epsilon)\nu(W))_+^2}{e(W)}.
 \tag{17}
\]

The energy is positive on these anchored witnesses. Introduce the explicit obstruction class

\[
 \mathcal W_p(\epsilon,E)=
 \{W\ge0:\ W_0=1,\ W\in U_\sigma,
       \ \nu(W)\le(1+\epsilon)^{-1},\ e(W)\le E\}.
 \tag{18}
\]

For both signs, the following are equivalent:

1. For every `epsilon>0`, `D_p(1,1+epsilon)->0` along primes.
2. For every `epsilon,E>0`, the set (18) is empty for all sufficiently large primes.

For `2=>1`, split (17) at energy `E`. The low-energy part has no positive numerator; the other part is at most `1/E`. Then send `E` to infinity. Conversely, a witness in (18) gives

\[
 D_p(1,1+\epsilon/2)^2
 \ge \frac{\epsilon^2}{4(1+\epsilon)^2E},
 \tag{19}
\]

so infinitely many such witnesses contradict `1`. This reformulation retains the fixed positive mean slack and does not replace it by the harder exact-mean endpoint. By [pinned penalty, (8)](pinned-penalty-24.md), the two-sign assertion is the needed relaxed target for ordinary theta.

Here is a rigorous **conditional** completion path using the present cell results:

* Prove a prime estimate such as (7), or the product-cell criterion (15), on every critical subgroup family that could arise from a near-twist. The first excludes the twist by (6); the second excludes it by (16).
* Prove an extraction statement for (18): any sequence of these bounded-energy, fixed-margin witnesses has a subsequence yielding either a nonalternating configuration already excluded by Round 20, or an even critical subgroup with `e=o(b)` and the nontrivial order-two twist.
* The two alternatives are then impossible. Equations (18)--(19) give the relaxed defect limit, and hence Problem 26.

The **second bullet is not proved** by the affine vacancy identities, the product-cell moment correspondence, or the existing high-energy inverse argument. That argument requires near-critical effective size and a specified high-additive-energy layer; (18) imposes neither hypothesis. Broad witnesses remain in (18). Even a proof of (7) for every prime critical subgroup would not by itself fill this extraction gap. This is the precise additional claim needed to connect this subgroup research to the full relaxed pinning target.

## 4. Norm-one square controls

Let `q=ell^2`, with `ell` an odd prime power, and take the norm-one group `B`, of size `ell+1`. In the affine cells, every nonempty nonsquare cell has `N=2` and opposite labels. Thus

\[
 F_3=F_4=V=0,\qquad T^2=1,\qquad S^2=q.
\]

Equations (3)--(8) are compatible with this, and therefore cannot supply a prime obstruction without an extra arithmetic estimate.

For the product cells, every anchor has `X_a=v_a F_ell^*`. Its nonzero off-identity overlaps all equal `ell-1`. There are `ell` anchors and `ell-2` such ratios per anchor. Of the deleted ratios, only `(a,u)=(-1,-1)` is among them, since `B intersect F_ell^*={1,-1}`. Therefore the number of remaining positive joint overlaps is exactly

\[
 \ell(\ell-2)-1.
\]

For every fixed threshold `t`, eventually

\[
 A_{\ell^2}(t)=0,\qquad
 B_{\ell^2}(t)=
 \frac{(\ell(\ell-2)-1)(\ell-1)}{\ell^3}
 =1-\frac3\ell+\frac1{\ell^2}+\frac1{\ell^3}\longrightarrow1.
 \tag{20}
\]

Thus (15) fails with limiting product one. The `1+` in `(1+A)B` is essential: the incorrect criterion `AB->0` alone would accept this square obstruction. Taking the threshold above all overlaps at each individual field would also give a false conclusion; (20) shows why the thresholds must be fixed before the field limit.

## 5. Exact checks and their scope

The [standard-library checker](parallel-cells-25-check.py) independently constructs the affine cells and the full affine ratio histogram, checking (1)--(6) with integer counts and rational bounds. It independently constructs the product cells and **all** anchor overlaps, checking the positive-overlap multiplicities and both quantities in (10). It checks the square formula (20) at `ell=7,11,13,31`.

Some exact affine certificates are:

| `p,b` | `F_3` | `F_4` | Actual `V` | Lower bound from (3) |
|---|---:|---:|---:|---:|
| `97,12` | 24 | 0 | 12 | 12 |
| `401,20` | 168 | 144 | 80 | `394/5` |
| `1153,32` | 264 | 144 | 244 | `1678/7` |
| `2113,48` | 888 | 480 | 320 | `14360/47` |
| `4177,72` | 2784 | 3648 | 544 | 409 |
| `13217,112` | 5712 | 7200 | 2464 | `217268/97` |

In total, eight primes and four square controls pass the exact cell/histogram/anchor checks. At `p=17,b=4`, an additional check convolves the Jacobi array **exactly in `Z[i]`** and verifies (8) for powers one through four, obtaining `8,12,20,36`. A separate direct Fourier calculation at `p=97` checks 32 Cauchy/tail splits, for four cap orders, both signs, and four thresholds. Those Fourier comparisons are floating point, not interval certificates. The exact finite counts do not establish (7), (15), or the extraction statement over unbounded primes.

Reproduce with:

```sh
python3 -B research/parallel-cells-25-check.py > research/parallel-cells-25-run.json
```

The structured output is [parallel-cells-25-certified.json](parallel-cells-25-certified.json). Only `research/parallel-cells-25*` is written. No shared files, commits, or pushes are changed.
