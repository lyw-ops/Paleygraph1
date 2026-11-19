# A bounded physical adjoint resolvent and a signed stationary remainder

Let \(a=2031/128\), let \(Q\) be the closed complex square of half-width \(2^{-17}\) about \(a\), and take the actual nine-center marked Picard rows \(V_j\). For \(n=(p-1)/2\ge10^{30}\) the physical residual \(K\Phi_t(V_{300})-V_{300}\) has sup norm below \(0.000312\) throughout \(Q\). At \(V_{250}\) the actual linearization contracts a weighted norm on represented rows by a factor below \(0.996681\), uniformly in the field and the complex floor. At \(V_{600}\) its iterated physical adjoint tests have sup norm at most \(1.5(1.047)^k\). Consequently the actual stationary **real** mark satisfies
\[
 \limsup_{p\to\infty}\sup_{t\in Q\cap\mathbb R}|m_p(t)|<7.57\cdot10^{-426}.
\]
At unbounded field size there is also a genuine stationary square centered at \(16640292/2^{20}\) with half-width \(2^{-21}\), extending the earlier real lower edge by \(2^{-21}\). On the cold square \(Q\) the residual-forced equation below has a common branch through \(|\lambda|\le0.998955034\); the original equation is at \(\lambda=1\). The mark estimate retains a positive tolerance. A uniform solution on the original complex square at unbounded field sizes is still open. The terms below also yield a single bounded signed test of the genuine real stationary Taylor remainder at height 250. [Physical nine-center rows](astra-predictor-76.md) · [Huber and signed adjoint identities](astra-mixed-81.md) · [Arb checker](astra-adjoint-82-check.py) · [Records](astra-adjoint-82-checks.jsonl)

## Physical packet prices for the actual derivative

We work on physical rows admitting symmetric positive upper comparison measures \(\sum_{k\ge1} h_k Q_k\), with \(Q_k=(\delta_{-k}+\delta_k)/2+(k-1)\delta_0\). For a negative simple the absolute first moment of its pooled boundary weights equals its dimension. Thus after bounding the nonzero masses by a symmetric upper measure, each pair of absolute index \(k\) needs only \((k-1)h_k\) of zero allowance. The seed, products through the symmetric kernel bounds and transported sums all have these upper representations. A scalar bound for the row is \(\sum k h_k\). Use the price \(\sum \pi(k) h_k\), where the checker's 24 explicit rational prices are extended affinely to larger \(k\), with \(\pi(0)=0\) and \(k\le\pi(k)\le 2k\). The corresponding norm is the infimum over admissible representations; it dominates the actual coordinate sup. The physical exceptional column \(Ke_0\) costs \(\sqrt p/n\) since \(\pi(1)=1\). Absolute series converge in the finite-dimensional represented subspace after taking the quotient norm. Only perturbations in this subspace are used. [Pooled transport and lift averaging](astra-feedback-52.md) · [True physical column](marked-domain-53.md)

Let \(C\) be the nine-center row. At \(W=V_j=C+Y\), the symmetric measure of \(F'_t(W)\) before transport is bounded by the derivative of the signed, arity-collected expansion used in the physical prefix. If \(U_d\) is the polynomial upper kernel at arity \(d\), its contribution is \(d U_d*Y^{*(d-1)}\), with \(Y\) replaced by its packet upper measure. All root subtractions are constant in the free argument, and the signed coefficient collections internal to each arity precede differentiation. This also bounds any straight segment between consecutive rows ending at \(V_j\): their core is the same, both residual measures are bounded by the larger stored packet envelope, and convex interpolation preserves that bound. The common off-grid tilted allowance is retained, including for the segment. [Collected arity kernels](astra-joint-65.md) · [Complete prefix and cut convention](astra-predictor-76.md)

For a retained symmetric kernel \(\mu\), write \(\pi(u)=\pi(|u|)\) and integrate over its full signed weight indices with its **nonnegative** masses. For an input packet \(k\), the output price is at most
\[
 A_{\mu}(k)=(k-1)\int\pi(u)\,d\mu(u)+\int\pi(k+u)\,d\mu(u).
\]
Indeed positive transport retains the nonzero weights and fills zeros to form the packets above. Beyond the retained kernel support plus the last stored price, both \(A_\mu(k)\) and \(\pi(k)\) are affine. Thus the supremum of the ratio requires only a finite list of tests and the two slopes at infinity. For discarded measure the ratio at every \(k\) is bounded by integrating \(2(1+|u|)\le10\cosh(u/5)\). The checker replays the stored prefix recurrence, reconstructs its derivative with the original degree and strip cuts, and subtracts the retained tilted masses from the full nonnegative comparison before charging discarded paths. For binomial orders \(l\ge15\) the derivative charge at tilted radius \(M\) is at most
\[
 \frac{4\sqrt{|t|}}M\left|{1/2\choose15}\right|s^{15}
 \left(\frac{15}{1-s}+\frac{s}{(1-s)^2}\right),\qquad s=M^2/(4\inf_Q\Re t).
\]
The physical product and geometric preimage differ only at site zero. More generally, on the exceptional site the preimage for a derivative applied to a unit-price physical row has absolute size at most one from the actual marked derivative; the geometric product subtraction and lift corrections cost less than ten in total before multiplying by \(Ke_0\). For instance, the uncollected derivative series costs at most \(2\sqrt{\sup_Q |t|}\,4.8/[4\inf_Q\Re t\sqrt{1-4.8^2/(4\inf_Q\Re t)}]<1\), and the two-character comparison costs at most twice that. Thus the added \(10^{-12}\) in the physical rate covers all these sources at the stated sizes. [Physical exceptional correction](marked-domain-53.md)

Write \(R_j=V_{j+1}-V_j\), and \(q_j\) for the rate at the larger envelope of the segment \([V_{j-1},V_j]\). The initial price is below \(0.169724\) from the first residual packets, including at most \(8\epsilon\) for the tilted excess at \(\epsilon=5\cdot10^{-7}\). The fundamental theorem of calculus on this physical segment gives \(\|R_j\|_\pi\le q_j\|R_{j-1}\|_\pi\). The stored positive packets increase entrywise, as checked at every step. The replay uses every rate through height 300 and the right envelope on each subsequent block of five. Selected bounds on the full complex square follow.

| Height | Linear operator or incoming secant | Price of outgoing physical residual |
| ---: | ---: | ---: |
| 100 | 0.984138 | 0.001180 |
| 250 | 0.996681 | 0.000343 |
| 275 | 0.998086 | 0.000322 |
| 300 | 0.999421 | 0.000312 |
| 600 | 1.046434 | 0.010955 |

In particular the height-250 Neumann sum for the true correction \(H=(I-KD)^{-1}R_{250}\), with \(D=\Phi_t'(V_{250})\), converges in packet norm uniformly on the square. It gives \(\|H\|_\infty\le\|H\|_\pi<0.104\), including at the physical mark.

## A single bounded test of the true stationary remainder

Fix a real floor in the square and put \(W=V_{250},\ R=R_{250},\ r=\|R\|_2\) in normalized counting norm. For the true stationary row write \(h=V_*-W\) and \(B_W(u)=\Phi_t(W+u)-\Phi_t(W)-Du\). Set \(X_0=S/2\) and \(Z=\sum_{k\ge0}(KD)^kX_0\); this is the physical test function of sup norm below 453. The finite-dimensional stationary equation and absolute convergence give the exact identity
\[
 \frac{(V_*)_0}{\sqrt n}=\frac{(K\Phi_t(W))_0}{\sqrt n}
           +\langle DZ,R\rangle+\langle Z,B_W(h)\rangle .
\]
For fixed terms, parity makes the compact pairing of \(DX_k\) and \(R\) zero. It also makes the pairing of \(X_k\) and **the exact Newton remainder** \(B_W(H)\) zero: both \(H,W\) are negative under the common central parity, while \(F(W+H)-F(W)-F'(W)H\) is even. The summable physical packet bounds justify the two infinite series after taking the field limit. One can first approximate \(H\) by its fixed Neumann sums since the real remainder is globally 2-Lipschitz; the marked exceptional derivative and activation differences contribute vanishing normalized error at those fixed sums. The first term also vanishes by the bounded prefix. Uniformly for real floors, the scaled mark therefore differs from \(\langle Z,B_W(h)-B_W(H)\rangle\) by \(o(1)\). [Compact fixed-depth transfer of the true Newton correction](astra-fixed-79.md) · [Physical adjoint parity](astra-mixed-81.md)

There is a finite-field bound on this **difference** of quadratic remainders. Real-site curvature gives \(\|H\|_2<2.084r\) and \(r'=\|(I-J_0)B_W(H)\|_2\le (2\sqrt{63})^{-1}\|H\|_\infty\|H\|_2<0.0137r\). Here \(J_0\) projects onto constants. The corrected predictor \(W'=W+H\) has cap 4.9 and residual \(KB_W(H)\), with centered preimage \(e'=(I-J_0)B_W(H)\) of sup norm less than 0.0014. Put \(d=h-H\). The real loss in the [Huber calculation](astra-mixed-81.md) about \(W'\) is at least \(0.65\min(d_i^2,|d_i|)\) pointwise, since \(63/[\sqrt{63+4.9^2}(\sqrt{63+4.9^2}+1)]>0.65\). For \(|d_i|\le1\) the activation difference is at most \(0.6|d_i|\), so its cross term against \(2e'_i\) is bounded by \(0.32d_i^2+1.125(e'_i)^2\). Above one that cross term is bounded by \(0.0028|d_i|\). Summing the stationary squared balance yields
\[
 \mathbb E_n\min(d^2,|d|)\le7(r')^2.
\]
Now \(B_W(h)-B_W(H)=(\Phi'(W')-D)d+B_{W'}(d)\). On \(|d|\le1\) the first term costs at most \(\|H\|_2\sqrt7 r'/\sqrt{63}\) in first norm. On the complement use \(\|H\|_\infty/\sqrt{63}\) times the tail first norm. The last term is always bounded by \(2\min(d^2,|d|)\). Altogether
\[
              \|B_W(h)-B_W(H)\|_1<0.013r^2
\]
when \(r>0\), with equality at zero in the non-strict bound. This is an estimate for the true stationary remainder paired against a bounded resolvent test, with its even Newton comparator removed. The stronger numerical mark bound quoted above instead uses \(W=V_{600}\). In the 568-step signed identity of the previous round replace \(12^k\) by \(G^k\), \(G=1.047\), keeping its angular \(L^2\) contraction and stationary Huber bounds. With \(r_0=4(0.428236)^{600}\), the resulting upper bound is
\[
 \tfrac12\{25(0.52)(0.428236)^{568}r_0+
 [1875(G^{569}-1)/(G-1)+625(0.52)(1.5)G^{568}]r_0^2\}.
\]
These depths are fixed before taking the field limit.

## The residual-forced section and a genuine warm extension

Write \(T=K\Phi_t\), \(C=V_0\) for the actual nine-center row, and \(R_0=T(C)-C\). Consider exactly
\[
                  U=T(U)-(1-\lambda)R_0.                              \tag{1}
\]
The solution at \(\lambda=0\) is \(C\). On substituting \(U=C+Y\), only the arity-zero residual in the update of \(Y\) acquires a factor \(\lambda\). Every term of positive arity is the same as for the original equation. Use the 50 rational packet caps in the [invariant checker](astra-adjoint-82-homotopy-check.py), scaled in units of \(10^{-20}\). Multiply the original collected polynomial upper row \(U_0\) by \(0.998955\). The omitted arities of the binomial tail still cost at most the old full tail since \(|\lambda|\le1\). The [weighted invariant test](astra-joint-64.md) computes the positive excess over the proposed caps and all descendants of the omitted packets at tilt \(1/5\). On the entire cold square the excess is below \(4.726\cdot10^{-7}\), with budget \(5\cdot10^{-7}\); the coordinate upper bound is 4.653. All physical corrections fit in another \(10^{-12}\) of tilted first-packet cost: the exceptional and marked packages for \(T(C+Y)\) and \((1-\lambda)T(C)\), including the center preimages, cost less than three times the previous round's \((34+11+16)\sqrt p/n\) at these sizes, times \(\cosh(1/5)\). In this comparison cancel the two main marked seed terms with the corresponding copies of the center before bounding the residual corrections. [Cold and warm invariant records](astra-adjoint-82-homotopy-checks.jsonl)

Iteration of (1) from \(C\) stays in this invariant. On the coordinate disks the physical bulk and marked derivatives have modulus below \(3/4\) by the same denominator test as in the genuine warm certificate. The additive forcing is independent of \(U\), so the physical normalized second norm of each successive difference decreases by this factor. For each finite field the limit is jointly holomorphic in the interiors and has the stated cap up to the boundaries. It has all invariant bounds by taking closures of the comparison sets in the finite-dimensional space. This also follows for its derivative by passing to limits of uniform derivative operator bounds along the rows. At \(\lambda=0.998955\) one thus has a holomorphic predictor for the **original** cold problem with residual exactly \(0.001045 R_0\) and packet price below \(0.000178\) in the original price.

The derivative at this forced section has a stronger full-site bound than its coordinate Lipschitz estimate. Repeat the single-packet Schur test with the second 24-entry rational price list in the invariant checker and its frozen cold envelope. The resulting physical packet rate is below \(0.999847\) everywhere on the closed \(\lambda\)-disk. In this price the true parameter direction \(R_0\) costs less than \(0.17\) from its arity-zero kernel and its entire tail. In particular the directional derivative \((I-T'(U))^{-1}R_0\) has coordinate cap below 1112. For a ball of packet radius \(b=0.00007\) around one of these solutions, the second derivative operator costs less than 2. To see this, take \(A=4\inf_Q\Re t\) and \(f(x)=2\sqrt{\sup_Q|t|}(2-\sqrt{1-x^2/A})\). Each unit-price direction costs at most one in dimension and absolute first weight moment. At total dimensional radius \(x\) this bounds the transported second derivative by \(2(x f'''(x)+2f''(x))\), since its output price is bounded by twice the first absolute moment of the preimage product. It is less than 2 for \(x\le4.8\), including the \(10^{-12}\) physical column allowance. With the certified rate \(q\) and forcing price \(P_0\), the additional parameter radius \(((1-q)b-b^2)/P_0\) exceeds \(34\cdot10^{-9}\), with derivative rate \(q+2b<1\). The local solutions agree with the original section on overlap by contraction and analytic uniqueness; overlapping boundary disks meet inside the initial disk, or are identical. This proves (1) through \(|\lambda|\le0.998955034\) with full-site modulus below 4.654. The remaining distance to one is greater than \(10^{-3}\).

For a **genuine stationary** domain put \(\lambda=1\) and take the square of half-width \(2^{-21}\) about \(16640292/2^{20}\). Use the separate warm caps in the same checker and the unscaled polynomial. The excess is below \(5.487\cdot10^{-8}\) against budget \(6\cdot10^{-8}\), with full coordinate bound below 4.653. The same physical contraction proves a common true solution there; positivity at real parameters identifies the stationary pair and its marked log satisfies \(|m_p(t)|\le3/\sqrt n\). The new square overlaps the [round-75 common rectangle](astra-fourth-75.md) on an open set, where uniqueness on the positive real slice identifies their holomorphic branches. Its real left edge is \((16640291+1/2)/2^{20}\). All these domain claims hold for \(n\ge10^{30}\) in the eligible prime sequence.

## Independent second derivative test and next comparisons

The separate radius scan in the adjoint checker uses the homotopy (1) with \(C,R_0\) replaced by \(V_j,R_j\), for \(1\le j\le300\). A crude second-derivative cap 2 on balls of radius at most 0.03 gives a guaranteed radius 0.0787 in \(\lambda\) at \(j=20\). For a sharper test, let \(\mu\) be the retained symmetric **second** derivative kernel, obtained by replacing \(dU_d\) by \(d(d-1)U_d\) and lowering the free power by two. Put \(P(v)=\int\pi(v+u)\,d\mu(u)\). The numerator of its column for two packets \(k,l\) is
\[
 (k-1)(l-1)P(0)+(l-1)P(k)+(k-1)P(l)
   +[P(k+l)+P(k-l)]/2 .
\]
Divide by \(\pi(k)\pi(l)\). If both indices are at least 30, use \(2(m_1+2m_0)[30/\pi(30)]^2\) for kernel mass \(m_0\) and first absolute moment \(m_1\), since \(\pi(k)/k\) increases. For a fixed smaller index the numerator and denominator are affine beyond the interaction strip. Omitted tilted kernel mass costs at most 12 per unit. For any trial radius \(b\) the third derivative is bounded by \(2(x f''''(x)+3 f'''(x))+10^{-12}\) with \(x=\|V_j\|_{\mathrm{dim}}+b\), by the same raw moment argument with three direction factors. The checker debits the quadratic and cubic terms from \((1-q_j)b\) and tests strict contraction. At \(j=1\), \(b=0.488\), the second and third derivative bounds are below 0.241 and 0.783. This gives a certified \(\lambda\)-radius of 0.5021 for that distinct residual direction. The tests at \(j\ge1\) and the invariant at \(j=0\) use different forcing vectors.

1. On the remaining cold interval in \(\lambda\), estimate the signed directional second derivative applied twice to \((I-T'(U))^{-1}R_0\). The current ball treats both perturbations as arbitrary packet directions. At the certified forced section the remaining source is the explicit scalar multiple \(0.001045R_0\).
2. In the genuine stationary identity at \(V_{250}\), estimate \(\langle Z,B_W(h)-B_W(H)\rangle\) directly on the real high coordinates. The bounded test and the improved Huber inequality permit comparison to further parity-correct predictors with bounded preimage defect.
3. Between the new warm square and the cold square, collect two successive signed derivative kernels before taking packet absolute values. The current single frozen price bounds the height-600 operator by 1.046434, leaving room for a directional estimate to change the convergence criterion.
