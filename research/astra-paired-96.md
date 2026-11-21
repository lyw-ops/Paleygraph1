# Two consecutive physical derivatives at the cold floor

Let \(Q\) be the square of half-width \(2^{-17}\) about \(2031/128\), and \(n=(p-1)/2\). At the actual real stationary row, uniformly for \(t\in Q\cap\mathbb R\), the fraction of singular values of the **physical two-step derivative** \((K\operatorname{diag}\Phi'_t(U_*))^2\) above \(0.8\) has prime limsup below \(1.096\cdot10^{-874}\). Its signed normalized trace has absolute limsup below \(1.65\cdot10^{-440}\), and its normalized Hilbert–Schmidt norm has limsup below \(0.059287\). For the actual real Picard secants, a corresponding bound holds on at least half of arbitrarily long disjoint pairs of steps, up to one endpoint. The estimates permit a small space of slow directions at unbounded field size.

Separately, on the unforced complex rectangle
\[
16640220<2^{20}\Re t<16640241,\qquad 2^{20}|\Im t|<1,
\]
the true nine-center Picard iteration at every height has coordinate cap \(4.654\) and secant rate \(0.526\) for every eligible prime with \(n\ge10^{30}\). Its real left edge advances 17 units of \(2^{-20}\) relative to round 95. The remaining gap to the right edge of \(Q\) is \(2260/2^{20}\). [Inherited unforced rectangle](astra-depth-95.md)

## Mixing of the actual paired matrix

Write \(\mathbb E\) for uniform coordinate averaging, \(J\) for projection onto constants, and \(C=K\circ K\) for the entrywise square of the real symmetric physical Jacobi transform. Its eigenvalue on constants is \(1-1/n\). For a nonidentity positional label \(a\) in the square subgroup its eigenvalue is
\[
 \frac1{2n}\left(-2+\sum_{x\in\mathbb F_p}\chi(x(1-x)(x-a))\right).
\]
Indeed the quadratic sum over the full field equals \(-1\), and its term at zero is \(\chi(-a)=1\). Restricting to nonzero squares first removes that term, then uses the quadratic character indicator. The cubic has three distinct roots, so Hasse's bound gives \(\|C-(1-1/n)J\|_{2\to2}\le\epsilon_p=(1+\sqrt p)/n\). This includes the omitted zero explicitly. [Fourier formula for the squared column](threshold-repair-19.md)

For real diagonal multipliers \(D_i=\operatorname{diag}(d_i)\) with \(|d_i|\le1\), expanding entries gives
\[
 n^{-1}\operatorname{tr}(K D_2 K D_1)=\mathbb E(d_2 C d_1),\qquad
 n^{-1}\|D_2 K D_1\|_{\rm HS}^2=\mathbb E(d_2^2 C d_1^2).
\]
In either expression the error after replacing \(C\) by \((1-1/n)J\) is at most \(\epsilon_p\) times the product of the centered second norms of its two inputs. Adding the outer \(K\) in the squared Hilbert–Schmidt formula decreases the normalized quantity by at most \(1/n\), since \(K^*K=I-J\) and the discarded projection has rank one.

At the real stationary row put \(b_i=\Phi_{t,i}(U_{*,i})\), \(d_i=U_{*,i}/b_i\), \(t_0=n\) and \(t_i=t\) elsewhere. Stationarity and \(K^*K=I-J\) give \((\mathbb E b)^2=4\mathbb E t_i\) exactly. For \(n\ge t\), Jensen yields
\[
  \mathbb E d^2=1-4\mathbb E(t_i/b_i^2)
  \le 1-t/(\mathbb E t_i)\le 1/(1+t).
\]
The paired Hilbert–Schmidt estimate follows, with no height-600 input.

For the signed trace, use the real nine-center \(W=V_{600}\) and \(r=\|K\Phi(W)-W\|_{2,n}\). The true row satisfies \(\mathbb E\min(|U_*-W|^2,|U_*-W|)\le625r^2\) and \(\limsup_p\sup_t r\le r_0=4(0.428236)^{600}\). The derivative of \(\Phi'_t\) on real coordinates is bounded by \(1/\sqrt{4t}\), including the marked site. Consequently
\[
 |\mathbb E d-\mathbb E\Phi'(W)|\le25r/\sqrt{4t}+1250r^2
\]
by separating the sites where the difference of the rows exceeds one. In the fixed-height compact limit the mean of \(\Phi'(W)\) vanishes by the common central parity of the negative input and oddness of the scalar derivative. The uniform finite-height cap, uniform polynomial approximation and the single modified mark give the same vanishing field limsup uniformly on the real interval. Applying the first matrix identity gives the stated signed trace tolerance. [True Huber estimate](astra-mixed-81.md) · [Compact parity and marked transfer](astra-adjoint-82.md)

## A quadratic improvement in the dimension of slow directions

Suppose \(|d_i|\le d=0.6\) off a set \(H_i\) of density \(\delta_i\), and \(|d_i|\le1\) everywhere, for each of two multipliers. Let \(P_i\) project onto \(H_i\). The number \(k\) of singular values of \(P_2 K P_1\) exceeding \(c=0.1\) satisfies
\[
 \frac{k}{n}\le \frac{(1-1/n)\delta_1\delta_2+
         \epsilon_p\sqrt{\delta_1\delta_2}}{c^2}.                 \tag{1}
\]
This is the preceding Hilbert–Schmidt identity applied to the two indicators. The full \(KD_2KD_1\) has at most \(k\) singular values above \(q=0.8\). To see this, impose the at most \(k\) linear equations that \(P_1D_1x\) be orthogonal to the large right singular vectors of the compression. For a unit vector in this subspace, if \(\|D_2KD_1x\|>q\), the total squared loss bounds both \(\|(I-P_1)x\|\) and \(\|(I-P_2)KD_1x\|\) by \(s=\sqrt{(1-q^2)/(1-d^2)}\). It would follow that
\[
 \sqrt{q^2-d^2s^2}<\|P_2 K D_1x\|\le c+ds,
\]
an impossibility for these constants. Min–max and left contraction prove the assertion.

At stationarity take both sets to be \(H=\{|U_*-W|>1\}\). The actual predictor cap \(4.768\) gives \(|d_i|<0.6\) off \(H\), since \(|U_{*,i}|<5.768\) there. The single-vertex exceptional density is at most \(625r^2\). Applying (1) gives the paired bound \((625r_0^2/0.1)^2<1.096\cdot10^{-874}\). [Predictor coordinate cap](astra-predictor-76.md)

There is also a consecutive-height conclusion for the genuine orbit. Put \(Y_j=V_{600+j}\), \(B_j=\{|Y_j-W|>1\}\), and let \(b_j\) be its density. For every \(N\) the telescoped Huber inequality gives \(\sum_{j<N}b_j\le N\delta\), where \(\delta=625r^2\). In \(m\) disjoint consecutive pairs of secants starting at \(j=0,2,\ldots,2m-2\), call a pair good if each of \(b_j,b_{j+1},b_{j+2}\le8\delta\). Each vertex occurs in at most two triples, hence at least \(m/2-1\) pairs are good. If \(r=0\) the orbit is constant and every pair is good. For each good pair, take the secant multipliers on \([Y_j,Y_{j+1}]\) and \([Y_{j+1},Y_{j+2}]\). They satisfy the hypotheses with \(H_1=B_j\cup B_{j+1}\), \(H_2=B_{j+1}\cup B_{j+2}\). Formula (1) bounds their slow fraction simultaneously in the height, with prime limsup below \(2.805\cdot10^{-872}\). All these matrices retain the coordinate signs of the physical secants.

For example, a sufficient remaining directional condition is that on every good pair the squared projection of its incoming increment onto the actual right singular space above \(0.8\) cost at most \(\alpha<1\) times its squared norm, uniformly in the field. Its squared norm then decreases by a factor at most \(0.64+0.36\alpha\). Every real pair is nonexpansive, so the density bound yields a field-uniform geometric tail for the real increments. Formula (1) alone controls the dimension of that projection space. The cold complex coordinates would also require continuation control. [Limiting one-vertex divergence](astra-direction-83.md)

## Four quadratic unit contributions and an unforced complex extension

At the same inner power-series prefix and eight nontrivial rank-three labels as round 95, also retain the trivial label. For each fixed free arity \(j\le6\), Legendre pair \((u,v)\), determinant-corrected Jacobi exponent \(e\) and chosen inner label, combine the direct signed coefficient with the unit returns from two copies of one later center:
\[
 \binom{j+2}{2}\big(\delta_*^2/16+z^2+2w^2+2v_*^2\big)\,A_{j+2}.
\]
Here \(\delta_*,z,w,v_*\) are the signed amplitudes of \(G,R,D+D^\vee,U+U'\) respectively, with \(v_*\) denoting the ninth-center amplitude in this formula. The unit multiplicities are the sixteen ordered dual pairs in \((16G)^2\), the unit in the self-dual standard square, the two ordered dual pairings of the \(D\) sum, and one unit from each of the independent symplectic squares. All have zero determinant shift. Only the selected scalar constituents enter this sum. [Rank-five unit](astra-ranknext-58.md) · [Last three centers](astra-joint-65.md)

For the trivial inner and Legendre labels with \(|e|\le5\), both the direct coefficient and \(A_{j+2}\) are the already collected scalar coefficients after the rank-four quadratic and shifted quartic terms. Their source exponents in that older scalar pool are restricted to \([-5,5]\), with inner arity at most eight. In the other retained sectors \(A_{j+2}\) uses rank-four degree zero. The direct coefficient includes the earlier rank-four quadratic unit wherever round 84 or 95 combined it. Omit the later root amendments at \(j=0\) on the three Legendre labels with \(e=0\) and the scalar at \(|e|=4\). The earlier linear or cubic returns with a nontrivial later-center label remain disjoint from these quadratic units. The triangle saving against the summed return is a lower bound on the saving against the four separate charges. Compute it on every signed arithmetic label before taking the smaller reflected boundary debit, as in round 95. [Rank-four scalar prefix](astra-rankfour-57.md) · [Other prefix debits](astra-imaginary-84.md)

Four overlapping rectangles use the previous 58-packet invariant with unit imaginary half-width, the original forcing parameter one and the full exceptional allowance. The first packet overruns the same coldest frozen cap if the four new returns are removed. The physical contraction and positive real identification yield the genuine holomorphic stationary row with \(|m_p|<3/\sqrt n\); the Picard residual is bounded by \(9.308(0.526)^h\). The harmonic-action conclusion and the finite-small-prime shrinking on closed real subintervals follow as in round 95. [Arb checker](astra-paired-96-check.py) · [Frozen caps](astra-paired-96-caps.json) · [Replay](astra-paired-96-checks.jsonl)

1. Estimate the projection of the actual incoming real increments onto the slow right singular spaces on the selected disjoint pairs. A uniform positive fraction of their energy off these spaces gives the geometric real tail above. The dimension estimate allows all incoming energy to lie inside.
2. On the nominated complex square, control the imaginary displacement on coordinates supporting these slow modes along a true stationary continuation. The real two-step estimates and the new common rectangle leave this field-uniform continuation open.
