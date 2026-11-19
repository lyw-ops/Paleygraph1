# Clipped mass beyond the largest coordinates of a true endpoint

Let \(p\equiv1\bmod4\) be prime, \(n=(p-1)/2\), \(G=\widehat Q\), and \(q\) an actual sign-\(\sigma\) feasible probability. For \(B\ge0\) put \(x_i=(q_i-B/n)_+\), \(z=q-x\), and \(M=\sum x_i\). Counting measure is used in all norms. Write \(M_E=\sum_{i\in E}x_i\). Fix \(\delta,\varepsilon>0\), with \(\varepsilon<1\). For all sufficiently large primes, if \(\sqrt n q_0\ge1+\delta\), every exceptional set \(A\subset G\) of size at most \((1-\varepsilon)^2 n/(1+\sqrt p)\) obeys
\[
       B+\sqrt p\,M_{G\setminus A}^2\ \ge\ c_{\delta,\varepsilon}D(p).
       \tag{1}
\]
The set may contain the singleton mark, every near-cap site, or the entire observed marked defect. In particular an optimizer consisting of \(o(\sqrt n)\) exceptional coordinates and a background with clipped mass \(o(p^{-1/4}\sqrt{D(p)})\) at \(B=o(D(p))\) cannot have a fixed supercritical mark. There is no restriction on the total mass or difference geometry of these exceptional coordinates.

## Removing arbitrary exceptional coordinates

Write \(P\) for the orthogonal Fourier projection on the forbidden positions, so \(Pq=0\). Its diagonal is \(\lambda=|\{s=-\sigma\}|/n=(n-1+\sigma)/(2n)\), and its off-diagonal entries have modulus at most \(\mu=(1+\sqrt p)/(2n)\). Indeed \(2\mathbf1_{s=-\sigma}=\mathbf1-\delta_1-\sigma s\), and every nontrivial multiplicative Fourier coefficient of \(s\) has modulus at most \(\sqrt p\). [Jacobi coefficients](fourier.md)

Diagonal expansion and the triangle inequality give
\[
 (\lambda+\mu)\|x\|_2^2
 \le \|Px\|_2^2+\mu\|x\|_1^2,\qquad
 n\|Px\|_2^2=n\|Pz\|_2^2\le B(1-M).
\]
Thus for \(k=|A|\), without any hypothesis on the mass of \(A\),
\[
 (\sqrt{\lambda+\mu}-\sqrt{k\mu})\sqrt n\|x\|_2
 \le \sqrt{B(1-M)}+\sqrt{n\mu}\,M_{G\setminus A}.             \tag{2}
\]
Use \(\sum_A x_i\le\sqrt k\|x\|_2\) after taking the square root of the preceding bound. The coefficient on the left is at least \(\varepsilon\sqrt{\lambda+\mu}\) in (1), since \(2n(\lambda+\mu)=n+\sqrt p+\sigma\ge n\).

If (1) failed along a sequence, let \(U=B+\sqrt p\,M_{G\setminus A}^2=o(D)\) and \(d=\lfloor\sqrt{D\max(1,U)}\rfloor\). Then \(d\to\infty\), \(d=o(D)\), and \(B=o(d)\). On any of the [selected smooth windows](smooth-windows-72.md) the actual fixed-deficit mask \(S=\{i\ne0:R_{-\sigma}(i)<-\delta/8\}\) has \(n\sum_{i\in S}x_i^2\gg_\delta d\). Equation (2) bounds the full clipped collision by \(O_\varepsilon(U)=o(d)\), a contradiction. This proves the uniform constant in (1) by the subsequence criterion. The argument also applies when \(A\) is chosen after seeing \(q,B,S\). For each size the strongest cost in (1) drops the largest entries. The minimum of that cost over \(B\ge0\) is a one-dimensional convex minimization. The factor depending on the fraction of the square-root threshold matters when comparing bounds of the form (2).

## Keeping the signed interactions on the actual negative mask

With \(E=G\setminus A\), assume \(a=\lambda-(k-1)\mu>0\) and \(k>0\). The orthogonal projector onto the forbidden-space functions vanishing on \(A\) is
\[
 H=P-P_{:,A}(P_{AA})^{-1}P_{A,:}.
\]
The matrix subtracted is the orthogonal projector onto the span of the columns of \(P\) on \(A\). The minimum eigenvalue of \(P_{AA}\) is at least \(a\). Thus \(Hq=0\), \(0\le H\le I\), and every row or column on \(A\) vanishes. On \(E\) one has \(H_{ii}\ge\ell=\lambda-k\mu^2/a\) and \(|H_{ij}|\le\mu+k\mu^2/a\) for \(i\ne j\), by the Euclidean norms of the restricted columns. Take \(H=P\) if \(A\) is empty. For \(y=x\mathbf1_{S\cap E}\), \(L=n\sum y_i^2\), the exact signed comparison is
\[
 n\sum_{i\in S\cap E}H_{ii}x_i^2
   = -n\operatorname{Re}\sum_{\substack{i\in S\cap E,\ j\in E\\j\ne i}}
             x_i H_{ij} x_j - n\operatorname{Re}\langle y,Hz\rangle.       \tag{3}
\]
The last term has magnitude at most \(\sqrt{L\,n\langle z,Hz\rangle}\le\sqrt{L B\sum_E z_i}\). This price uses the low part only outside the exceptions. Terms containing a high root or any other deleted high coordinate vanish exactly. If \(k\le(1-\varepsilon)^2n/(1+\sqrt p)\), then \(\ell=1/2+O_\varepsilon(p^{-1/2})\). When \(n\sum_{S\cap A}x_i^2=o(d)\), supercriticality at \(B=o(d)\) forces the signed off-diagonal term in (3) to be at least \((1/2-o(1))L\gg_\delta d\). This applies with \(A=\{0\}\) on every selected window. If masked collision on \(A\) is large, (1) still applies.

## Deleting whole cosets together with arbitrary sites

Let \(K=\bigcup_{j=1}^r(h_j+H_j)\) with \(r\) fixed. The subgroups \(H_j\) may differ. Put \(E=G\setminus K\). There is a positive semidefinite matrix \(T\) vanishing on the rows and columns of \(K\) with
\[
 Tq=0,\quad T_{ii}=1\ (i\in E),\quad \|T\|\le C_r,\quad
 \max_{i\ne j}|T_{ij}|\le \mu_r=C_r\sqrt p/n.                    \tag{4}
\]
To see this, independently sample \(v_j\) uniformly on \(H_j^\perp\) and use \(w_i=\prod_j(i(v_j)-h_j(v_j))\). Then \(w|_K=0\) and \(\mathbb E|w_i|^2=2^r\) on \(E\). For each realization take all distinct subset products of the \(v_j\), and let \(F\) be the positions sent into the forbidden mask by multiplication by **each** such product. The transform of \(wq\) is zero on \(F\) by expansion. With \(b\le2^r\) distinct products, the uniform twisted sign-pattern bound gives \(|F|=2^{-b}n+O(b\sqrt p+b)\), and each nontrivial Fourier coefficient of \(\mathbf1_F\) is \(O(b\sqrt p+b)\). This follows by expanding the sign indicators, omitting the at most \(b\) roots, and applying the twisted distinct-shift estimate to each nonempty product. [Exterior annihilators](astra-face-46.md) · [Twisted character-sum estimate](parallel-torus-8.md#a-uniform-bound-for-twisted-translate-correlations)

Let \(P_F\) project onto \(F\), and average \(2^{-r}\operatorname{diag}(\bar w)P_F\operatorname{diag}(w)n/|F|\) to get \(T\). Its diagonal follows from the mean square of \(w\). On quadratic forms the norm is bounded by \(\max n/|F|\) by the same average. Cauchy–Schwarz gives \(\mathbb E|w_i w_j|\le 2^r\), proving the off-diagonal estimate. All claims hold uniformly in the cosets for sufficiently large \(p\).

For any \(A\subset E\) with \(|A|\le c_r n/\sqrt p\) and \(c_r\) sufficiently small, write \(M'=\sum_{E\setminus A}x_i\). The diagonal expansion on \(E\) and \(Tq=0\) give
\[
 (1+\mu_r)\|x_E\|_2^2
 \le \langle z,Tz\rangle+\mu_r\|x_E\|_1^2,\qquad
 n\langle z,Tz\rangle\le C_r B\sum_E z_i.
\]
Consequently \(n\|x_E\|_2^2\ll_r B+\sqrt p\, (M')^2\), by the same absorption as in (2). On an actual selected window this bounds the full hinge by
\[
 n\sum_{S\cap K}x_i^2+O_r\!\left(B+\sqrt p\,(M')^2\right).
\]
Only the intersection of the cosets with the marked mask is charged. Large cosets with small masked hinge can thus be removed simultaneously with an arbitrary square-root-sized set, whose masked hinge is unrestricted. Their total removed clipped mass may be large. A uniform \(o(d)\) upper bound on the displayed expression at \(B=o(d)\) on one selected window per tested face would exclude a fixed supercritical gap. The estimate alone gives no such upper bound on actual prime optimizers.

## Four finite singleton endpoints

The [checker](astra-masked-76-check.py) takes the complementary active systems of the actual larger-side even optimizer on four primes. The exact linear systems with Arb invertibility and positivity certify the rows; their off-root supports are complementary and the two exact feasible roots have product \(1/n\) by Fourier orthogonality. The endpoint checks certify a strict singleton cap on each exhibited row. We remove the largest \(k\) coordinates including this root and compare \(\min_B [B+\sqrt p M_E(B)^2]\) with its untrimmed counterpart. The actual cold windows use length five, taper from round 72, allowance \(1/1000\), and deficit cutoff \(1/40\). For (3) the density cutoff is \(B=1\). These fixed diagnostic windows have no asymptotic selection claim.

| Prime | \(k\) | Window start | Minimum trimmed / untrimmed cost | Full / exterior masked hinge | Signed / negative-entry-only off-diagonal price |
|---:|---:|---:|---:|---:|---:|
|101|3|24|2.05870 / 2.72120|0.74896 / 0.59230|0.25109 / 0.37621|
|257|3|10|2.52974 / 3.16800|1.00044 / 0.83372|0.37452 / 0.64915|
|409|5|20|2.69828 / 3.44379|1.16385 / 0.85391|0.38522 / 0.77753|
|769|7|2|2.78855 / 3.30537|0.71342 / 0.54510|0.25485 / 0.69004|

The checker encloses the convex minimum by 46 derivative bisections and monotonicity of the clipped mass on the final bracket. For the signed comparison it forms the exact Schur complement with interval Fourier entries on the measured support; discarding positive off-diagonal entries gives the last column's larger price. At \(769\) the latter exceeds the signed value by more than \(0.4351\). The 768-bit [outward records](astra-masked-76-checks.jsonl) include the actual weighted negative tails \(\sum_{i\in S}q_i(-R_i)\), both pieces of the diagonal comparison and the endpoint marks.

1. Minimize the trimmed mass cost over the cutoff on genuine primary optimizers. Allow a bounded union of cosets only at its measured hinge on the selected window. An \(o(D)\) trimmed cost in (1), or an \(o(d)\) masked cost in the coset extension, excludes that supercritical sequence, including singleton caps.
2. If the trimmed mass remains large, use (3) on the actual support with the root and any troublesome high coordinates removed. Test the signed term against its retained diagonal, together with the observed hinge on deleted sites and the low part's forbidden energy. The all-prime ordinary theta limit remains open.
