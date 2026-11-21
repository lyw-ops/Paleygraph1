# The zero-floor defect from one averaged-iteration height

Use the actual all-site cap \(M>0\), genuine zero-floor averaged iterates \(W_j\), and normalized real norms of the [capped zero-floor comparison](zero-floor-mark-and-cap-budget.md). Write \(F(W)=K\Phi_0(C_M(W))\), \(r_j=F(W_j)-W_j\), \(\mu_j=\mathbb E_n\Phi_0(C_M(W_j))\), and let \(\mu_*\) be the activation mean of an actual fixed point \(U\). The zero-floor deficit is exactly \(\alpha_M(p)=4-\mu_*^2\) when the marked spill is included.

## Field-uniform comparison at a single height

Set \(L=\sqrt{M^2+4}\), so \(\|U\|_{2,n}\le L\). The midpoint inequality gives \(\|W_j-U\|_{2,n}\le L\) and \(\sum_{j\ge0}\|r_j\|_{2,n}^2\le4L^2\). The averaged map is nonexpansive, so \(\|r_j\|_{2,n}=2\|W_{j+1}-W_j\|_{2,n}\) is nonincreasing. Thus \(\|r_j\|_{2,n}\le2L/\sqrt{j+1}\).

In comparing \(W_j\) and \(U\) before averaging, the normalization loss for \(K\) pays the squared difference of activation means. More precisely, \(K^*K=I-J_0\) and the scalar clipped activation is one-Lipschitz, so
\[
 |\mu_j-\mu_*|^2\le \|W_j-U\|_{2,n}^2-\|F(W_j)-U\|_{2,n}^2
 \le 2L\|r_j\|_{2,n}.
\]
It follows that
\[
 |\mu_j-\mu_*|\le \frac{2L}{(j+1)^{1/4}}.
\]
The bound using the actual residual can be sharper. For an average through \(J-1\), the [midpoint loss](zero-floor-mark-and-cap-budget.md#an-averaged-zero-floor-estimate-without-critical-scaling) gives \(J^{-1}\sum_{j<J}|\mu_j-\mu_*|^2\le2L^2/J\). The same upper after square root bounds the difference between \(\mu_*\) and either the ordinary average or the quadratic mean of the \(\mu_j\).

For fixed \(M\), the preceding uniform estimates give the exact prime-first relation
\[
 \limsup_{p\to\infty}\alpha_M(p)
     =4-\left(\lim_{j\to\infty}\liminf_{p\to\infty}\mu_j(p)\right)^2 .
\]
Indeed the inner liminf differs from \(\liminf_p\mu_*\) by at most \(2L/(j+1)^{1/4}\), and each mean is nonnegative. Any unbounded sequence of fixed horizons gives the same outer limit. A fixed-depth arithmetic upper or lower on the actual mean, with a stronger direct residual bound when available, can therefore test the unweighted defect. This comparison uses no variance estimate and gives no control of the ordinary-optimizer weight.

## The first two actual means at \(M=10\)

Let \(x=\sqrt n\,Ke_0\). Starting at zero gives exactly \(W_1=x\). The fixed-character Jacobi law in the [seed estimate](zero-floor-mark-and-cap-budget.md#a-small-cap-cannot-have-vanishing-zero-floor-defect) gives \(\mathbb E_n|x|\to a=2\sqrt2/\pi\). Also \(\|x\|_{2,n}^2=1-1/n\), and \(\limsup_p\|x\|_\infty\le\sqrt2\). Thus \(\mu_1\to a\).

For the second midpoint set \(y=K|x|\). At \(M=10\) the first bulk clip is inactive, and the mark differs from its added \(2\sqrt n\) seed by a bounded scalar. Therefore \(W_2=3x/2+y/2+o_{2,n}(1)\). From \(K^*K=I-J_0\) and \(Kx=\sqrt n(e_0-\mathbf1/n)\) one obtains \(\|y\|_{2,n}^2\to b=1-a^2\) and \(\langle x,y\rangle_{2,n}=O(n^{-1/2})\). Since \(g_M(w)=\min(|w|,M)\) is one-Lipschitz, the \(o_{2,n}(1)\) error has negligible effect on the mean. The true marked activation likewise changes this mean by \(O_M(n^{-1/2})\).

The normalized second norm of \(3x/2+y/2\) gives \(\limsup_p\mu_2\le\sqrt{9/4+b/4}\). For the lower bound test its absolute value against \(\operatorname{sgn}x\). The orthogonal projection of \(\operatorname{sgn}x\) off \(x\) has squared norm at most \(1-(\mathbb E_n|x|)^2/\|x\|_{2,n}^2\). The removed component contributes \(o(1)\) when paired with \(y\). Hence the \(\operatorname{sgn}x\) test on the unclipped mean gives a lower limit at least \(3a/2-b/2\).

The clipping cost is bounded pointwise by \((|y|/2-d_p)_+\), where \(d_p=M-3\|x\|_\infty/2>0\) for all sufficiently large primes. Using \((u-d)_+\le u^2/(4d)\) on \(u\ge0\), the mean cost has upper limit at most \(b/[16(M-3\sqrt2/2)]\). Altogether
\[
 1.254<\frac{3a}2-\frac b2-\frac{b}{16(10-3\sqrt2/2)}
 \le\liminf_p\mu_2\le\limsup_p\mu_2
 \le\sqrt{\frac94+\frac b4}<1.517 .
\]
The strict decimal comparisons are rational checks using \(3.14159<\pi<3.14160\) and \(1.41421<\sqrt2<1.41422\). This proves a strict increase from the first to the second mean in the prime limit. It leaves open the arithmetic bound along unbounded fixed horizons that the single-height relation needs.

## The isometry alone does not order means by cap

For a five-coordinate reflection, let \(P\) be the orthogonal projection onto the column span of
\[
 A=\begin{pmatrix}-3&4\\-5&0\\1&-4\\5&5\\2&-5\end{pmatrix},
 \qquad K=I-J_0-2P .
\]
The columns of \(A\) have sum zero, so \(K^*=K\) and \(K^2=I-J_0\). Take a constant marked activation \(a_0=2\), and take \(a_i=\min(|(Ka)_i|,M)\) for \(i>0\). This flat-mark convention is also the zero marked-cap activation after rescaling from \(2\sqrt n\) to \(2\). For \(M=11/20\) and \(M=3/5\), respectively, the exact activation rows are
\[
 \left(2,\tfrac{11}{20},\tfrac{14207}{68180},\tfrac{1107}{13636},\tfrac{11}{20}\right),\qquad
 \left(2,\tfrac35,\tfrac{2221}{17045},\tfrac{67}{3409},\tfrac35\right).
\]
To verify the fixed-point equations, use \(P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}\). The first and fourth bulk coordinates are above the cap in modulus, and the second and third bulk coordinates are below it with signs \(+\) and \(-\), respectively. The mean is unique at each cap by the squared-norm comparison, and strictly decreases from \(2311/3409\) to \(2284/3409\).

Thus cap monotonicity of the signed spill first norm cannot be upgraded to monotonicity of the activation mean using only the reflection identity and clipping. This is an exact algebraic control outside the Paley prime family. It leaves open a comparison between the fixed-cap mean and the cap-inactive ordinary mean on the genuine prime operators.
