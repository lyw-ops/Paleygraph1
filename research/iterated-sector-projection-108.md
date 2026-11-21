# Iterated positivity correction in the capped sector

Repeatedly projecting the actual negative part gives an ordinary feasible completion at each fixed field. Its mean and marked costs are controlled by the sum of the negative means. There are two specific sufficient ways to make those costs vanish along primes. One uses an effective-width bound below the entry-scale threshold and does not require a cap-deficit rate.

Fix \(t>0\), a fixed \(M\ge2\), and one sign \(\epsilon\). Use the actual real capped row \(U=Ka\), \(\mu=\mathbb E_n a\), and \(z=a-\epsilon U\) from [the single-step completion](projected-cap-completion-108.md). The centered part of \(z\) is in the \(-\epsilon\) sector, its normalized mark is \(z_0/\sqrt n=d_\epsilon\to2\), and \(\mu\le\nu=2\sqrt{1+t-t/n}\). On even rows let \(P=(I-\epsilon K+J_0)/2\), the orthogonal projection onto that sector plus constants. Start \(b^0=z\) and form the genuine repair iterates
\[
 h_j=(b^j)_-,\qquad m_j=\mathbb E_n h_j,\qquad b^{j+1}=b^j+P h_j .
\]
All rows are real even and stay in the required sector plus constants. The normalized \(2\)-norm is used throughout. At a stop \(k\), the row \(b^k+\|h_k\|_\infty\mathbf1\) is nonnegative with mean
\(\mu+\sum_{j<k}m_j+\|h_k\|_\infty\). The normalized mark is at least
\[
 d_\epsilon-\tfrac12\sqrt{p/n}\sum_{j<k}m_j,
\]
because \((P h_j)_0=(h_{j,0}-\epsilon(Kh_j)_0+m_j)/2\) and \(|(Kh_j)_0|\le\sqrt p\,m_j\). A sequence of stops with \(\sum_{j<k}m_j+\|h_k\|_\infty=o(1)\) therefore gives
\(\limsup_p\theta_\epsilon/\sqrt n\le\sqrt{1+t}\), by the [ordinary Fourier-LP ratio and exact complementary product](fourier.md). For both signs at a sequence of fixed floors tending to zero this suffices for the original limit.

## Exact contraction test on the negative rows

Since \(b^{j+1}=(b^j)_+-(I-P)h_j\), the new negative part is entrywise bounded by \(((I-P)h_j)_+\). Consequently
\[
 \begin{aligned}
 \|h_{j+1}\|_{2,n}^2&\le\|h_j\|_{2,n}^2-\|Ph_j\|_{2,n}^2,\\
 2\|Ph_j\|_{2,n}^2
   &=\|h_j\|_{2,n}^2-\epsilon\langle h_j,Kh_j\rangle_{2,n}+m_j^2 .
 \end{aligned}                                                     \tag{1}
\]
Here \(Ph_j\) is a signed, pointwise unconstrained sector correction. Nonnegativity is imposed on the completed row.

For completeness, the iteration itself converges to a feasible row for every fixed field. Orthogonality and \(P b^j=b^j\) give
\[
 \|b^{j+1}\|_{2,n}^2
 =\|b^j\|_{2,n}^2-2\|h_j\|_{2,n}^2+\|P h_j\|_{2,n}^2 .
\]
Thus its norms decrease, while its means \(\mu+\sum_{i<j}m_i\) increase and stay bounded by \(\|z\|_{2,n}\). The series of nonnegative \(m_j\) converges. At fixed \(n\), \(\|P h_j\|_\infty\le n m_j\) follows from the normalized second norm and \(h_j\ge0\), so the rows converge uniformly in the coordinates to a nonnegative sector row. This existence statement alone permits an order-one added mean.

## Effective width and a signed alternative

Assume for the actual negative rows through the proposed stop that
\[
         \sqrt p\,m_j^2\le\eta\,\|h_j\|_{2,n}^2
                        \quad\text{with a fixed }0<\eta<1 .        \tag{2}
\]
The Jacobi entry bound gives \(|\langle h_j,Kh_j\rangle_{2,n}|\le\sqrt p\,m_j^2\). By (1), \(\|h_{j+1}\|_{2,n}\le q\|h_j\|_{2,n}\) for \(q=\sqrt{(1+\eta)/2}<1\). Also \(m_j\le\sqrt\eta\,p^{-1/4}\|h_j\|_{2,n}\). The initial \(h_0=T_\epsilon\) for all large primes at the fixed floor and cap, and \(\|h_0\|_{2,n}^2\le\alpha\le4\). Thus \(\sum_{j<k}m_j=O(p^{-1/4})\), while \(\|h_k\|_\infty\le2\sqrt n q^k\). Taking \(k-(\log n)/(2|\log q|)\to+\infty\) proves the stated real-floor upper under (2) for those actual steps. The normalized effective support \(n m_j^2/\|h_j\|_{2,n}^2\) in (2) is below \(\eta n/\sqrt p\). No upper of this kind is presently proved for the genuine repair sequence.

If instead the true critical cap rate \(\alpha=O(n^{-1/2})\) holds, one can replace (2) by a uniform fixed gap
\[
 \epsilon\langle h_j,Kh_j\rangle_{2,n}
                       \le(1-\delta)\|h_j\|_{2,n}^2,\qquad\delta>0.
                                                                    \tag{3}
\]
Then \(q=\sqrt{1-\delta/2}<1\) in (1), \(\|h_0\|_{2,n}=O(n^{-1/4})\), and \(\sum m_j\le\sum\|h_j\|_{2,n}=O(n^{-1/4})\). It suffices to exceed \((\log n)/(4|\log q|)\) steps by a quantity tending to infinity. In particular a persistent excess above \(\sqrt{1+t}\) in the specified theta sign at the critical cap rate forces failure of (3) somewhere in such a finite repair window for every fixed \(0<\delta<1\).

The two estimates target the actual negative rows of a prescribed signed completion, rather than the coordinate supremum of a single transport. Neither width control nor the prime-specific signed gap for this sequence has been established at the relevant floors.

1. Track effective width and signed negative-row Rayleigh quotient jointly on the genuine projected repair, with mean cost and residual supremum accounted for as above.
2. At a fixed floor where width or gap control fails, compare the actual negative repair set to the favored true stationary factor and its mandatory weighted redistribution.
