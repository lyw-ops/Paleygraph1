# Compact variance and a split transfer for three leading fields

The actual stationary mark obeys the following strict limiting upper bounds through eligible primes and prime squares.

| Floor interval | Upper bound on \(\limsup_q\sup_t |m_q(t)|\) | Lower bound on scaled bulk trial products |
| --- | ---: | ---: |
| \([309/64,83/16]\) | \(0.01699\) | \(0.89\) |
| \([75/16,309/64]\) | \(0.020\) | \(0.45\) |
| \([37/8,75/16]\) | \(0.022\) | \(0.24\) |

The \(0.017\) tolerance now reaches \(309/64\). Separately, at \(t=5\) replacing just the previous Euclidean estimate by the exact compact variance gives a mark bound below \(0.01694\) with the previous pointwise envelope. The interval result uses a sharper signed pointwise calculation and splits off a linear combination of three arithmetic fields in the square-root weight transfer.

## Exact compact moments through degree 32

Use the finite-field input \(V=S+by+\lambda z+\nu w\) and one update \(V^+=S+KP_t(V)\) of [round 58](distinguished-positive-58.md). In the compact law use capital letters \(X,Y,Z,W,U\) for \(x,y,z,w,u=K(xw)\), and \(S=2X\). For the interval trial use \(\lambda=(9/10)2b\kappa,\ \nu=(13/20)2\lambda\kappa,\ \kappa=(4t+6)^{-1/2}\), throughout. The coefficient \(b=c_{02}\) is the exact degree-16 polynomial coefficient at the limiting seed scale.

Write \(J\) for the positive Jacobi coordinate and \(J_0=J+J^{-1}\). Use raw trace sums \(Y_0=2Y,\ Z_0=2\sqrt2 Z,\ W_0=4W\). Conditional on \(J\), these are independent sums of the two \(SU(2)\) traces, two rank-three standard and dual trace pairs with determinant exponents \(1,-1\), and four rank-four standard and dual trace pairs with exponents \(2,-2,0,0\), respectively. Thus the compact input is
\[
 \mathcal V=\sqrt2 J_0+(b/2)Y_0+(\lambda/(2\sqrt2)) Z_0+(\nu/4) W_0.
\]
All the determinant coordinates here are those of the positive rank-three model. The even rank-four determinant exponents are unchanged by that central translation. [Common rank-three law](joint-law-32.md#2-a-concrete-compact-probability-model) · [Rank-four arithmetic determinants](rank-four-arithmetic-56.md#common-compact-law-and-an-exact-fourth-moment)

For each dimension \(d\), generate the integer multiplicity \(f_\rho\) of a partition in the \(k\)-fold standard tensor power by adding one box at a time to a dominant partition with at most \(d\) rows. A pair of partitions \(\rho,\sigma\) from powers \(j,k-j\) contributes to the conditional unit of a standard–dual product exactly when their difference is constant across the rows. If that difference is \((h,\ldots,h)\) and the determinant exponent is \(d_0\), the coefficient is \(f_\rho f_\sigma J^{h d_0}\). This follows by restricting the two irreducible \(GL_d\) representations to \(SL_d\), where they coincide exactly when their last-entry-normalized shapes coincide. Multiplying by \(\binom{k}{j}\) and summing gives the conditional Laurent polynomial for the \(k\)-th power of each standard plus dual trace. The \(SU(2)\) real traces have Catalan moments in even degree and zero odd moments, by the same one-box rule on the constant two-row partition. Products of independent trace sums use binomial convolution. Multiplying by the Laurent expansion of \(J_0^i\) and taking exponent zero produces the joint integer moments of the four raw variables.

Let
\[
 G=bX^2+\lambda XY+\nu XZ,\qquad F=P_t(\mathcal V)-G.
\]
The limiting normalized squared norm of \(V^+-V\) is exactly \(\operatorname{Var}(F)\). Indeed \(V^+-V=K[P_t(V)-bx^2-\lambda xy-\nu xz]\) at every field, and \(K^2=I-J_{\rm av}\) makes \(K\) isometric after centering. Here \(J_{\rm av}\) denotes the averaging matrix. The bounded-field common joint law transfers these fixed polynomial moments, uniformly on compact floor intervals by their continuous coefficients. The compact computation expands \(P_t(\mathcal V)\) as a degree-eight polynomial in \(\mathcal V^2\) and \(P_t(\mathcal V)^2\) to degree 16 in \(\mathcal V^2\). The corrections have \(\mathbb E G=b\), \(\mathbb E G^2=(3b^2+\lambda^2+\nu^2)/2\). The mixed terms are evaluated by appending the raw exponents for \(J_0^2,J_0Y_0,J_0Z_0\) to the multinomial expansion of each even power of \(\mathcal V\). Integer Laurent projection then gives the exact expression
\[
 \operatorname{Var}(F)=\mathbb E P_t(\mathcal V)^2-2\mathbb E[P_t(\mathcal V)G]
 +\mathbb E G^2-(\mathbb E P_t(\mathcal V)-b)^2.
\]
At \(t=5\) with the round-58 coefficients \((19/20,3/4)\), the resulting variance lies strictly between \(480948475/10^{12}\) and \(480948476/10^{12}\). Arb evaluates this exact expression with outward rounding. The earlier finite-prime RMS diagnostic is unnecessary for the estimate.

## Signed pointwise envelope

In the same Laurent expansion \(c_{jk}\) of \(P_t(S+R)\), now write the input correction as \(bY+\beta W_3+\gamma F_4\) in the lift coordinates, where \(\beta=\sqrt2\lambda,\ \gamma=2\nu\). The finite-field rank error goes to zero by the exact aliases and fixed-word argument of round 58. Use the signed expansion of \(Y^h\) in the two rank-two symmetric-power characters. If \(m_{h,u,v}\) is the coefficient on the pair with degrees \(u,v\), the coefficient of the corresponding term in \((\beta W_3+\gamma F_4)^r C_k\) is
\[
 \sum_{h\ge0}\binom{r+h}{r} b^h c_{r+h,k}m_{h,u,v}.
\]
Subtract the exact three distinguished sources as in round 58. The \(bC_2\) is subtracted from the scalar term at \(r=0,k=2\), and \(\beta C_1Y\) from the two standard terms at \(r=0,k=1\). Expand the remaining power in \(W_3,F_4\). Subtract \(\gamma C_1W_3\) in the \(W_3\)-linear, \(F_4\)-constant, Legendre-scalar term. Only then take moduli. The \(W_3,F_4\) powers use their positive symmetric measures. At twist one attach to the Legendre label its boundary measure \((v+1)\sum_{j=0}^u\delta_{-2u+4j}\). The twist at \(\chi\) exchanges \(u,v\). The grouped coefficients are symmetric under that exchange, so the sum at twist one gives the pooled bound. Its absolute first moments after the seed shifts \(\pm k\) give the radius \(\Delta\) for \(V^+-V\). The argument uses the same two-character projection and bounded exceptional costs as before. [Signed Legendre coefficients](astra-signed-54.md) · [Boundary projection](astra-feedback-52.md#reading-rank-from-two-mellin-characters)

## Split transfer using the next three fields

Fix \(a=(a_Z,a_W,a_U)=(1/125,1/96,3/400)\). Set the finite-field principal difference to \(\delta_0=a_Z z+a_W w+a_U u\), with corresponding compact expression \(\mathcal D=a_ZZ+a_W W+a_U U\). By the exact finite-field aliases this subtracts \(a_Zxy+a_Wxz+a_Uxw\) from the \(K\)-input. Each subtraction variable is centered with variance \(1/2\), and the three are mutually orthogonal by their conditional means and variances. Thus the residual squared norm has exact limiting value
\[
 \operatorname{Var}(F)+\tfrac12\sum_i a_i^2-2\sum_i a_i C_i,
 \qquad
 (C_Z,C_W,C_U)=(\mathbb E[P_t(\mathcal V)XY]-\lambda/2,\
 \mathbb E[P_t(\mathcal V)XZ]-\nu/2,\ \mathbb E[P_t(\mathcal V)XW]).
\]
For the last expectation append the raw exponents of \(J_0W_0\) with factor \(1/(4\sqrt2)\). The mixed moments of \(U\) needed below are supplied by the exact higher feedback family of [round 57](weighted-arithmetic-57.md#exact-lift-feedback-and-compact-moments).

For the numerator of the principal square-root weight difference set \(g=(2\lambda+a_Z,2\nu+a_W,a_U)\) and \(m=(3/4,49/64,3/4)\), the unconditional fourth moments of \(Z,W,U\). A direct expansion gives
\[
\begin{split}
 \mathbb E[(2\mathcal V+\mathcal D)^2\mathcal D^2]
 &= (8+b^2)\sum_i a_i^2+g_Z a_Z^2+\sum_i m_i g_i^2 a_i^2\\
 &\quad+\tfrac14\sum_{i<j}
       (g_i^2a_j^2+g_j^2a_i^2+4g_i g_j a_i a_j).
\end{split}
\]
For the first term condition on the old seed and \(Y\). The linear cross term retains only the \(Z^3\) contraction, since \(\mathbb E(Z^3\mid S)=S/16\) and the other odd contractions vanish. This gives \(g_Za_Z^2\). In the fourth-order terms each mixed pair of squares has mean \(1/4\) by the constant conditional second moments. Let \(N_\mu\) be the square root of this expression. On good frequencies \(|\delta_0|\le d_\mu=3\sqrt2 a_Z+8a_W+(23/\sqrt2)a_U+o(1)\).

If \(B\) bounds \(|V|\), set \(L=t-(2B+\Delta)\Delta/4\) and \(L_\mu=t-(2B+d_\mu)d_\mu/4\). The actual and principal ideal products \(P(V,d)=t-(2V+d)d/4\) with \(d=V^+-V,\delta_0\) have lower bounds \(L,L_\mu\). The mark is normalized separately as before. Let \(D_\mu\) bound the residual norm and \(C=(2H(B)+e_B)e_B/4\) be the polynomial product correction. Rationalize each square-root difference as in [round 57](weighted-positive-57.md#split-square-root-weight-comparison). This gives the distance upper bound
\[
 \frac{N_\mu}{4(\sqrt t+\sqrt{L_\mu})}
 +\frac{(2B+\Delta+d_\mu)D_\mu}{4(\sqrt L+\sqrt{L_\mu})}
 +\frac{C}{\sqrt L+\sqrt{L-C}}+o(1).
\]
The ordinary mark transfer applies on the strict positive product region with \(P_t(V)>0\). The polynomial error \(e_B\) here enters the product comparison. The exact residual formula already uses the polynomial \(P_t\) and needs no additional polynomial remainder for its Euclidean norm.

## Uniform interval calculation

The [checker](compact-variance-59-check.py) computes the compact residual norm at the midpoint of each rational slab. To extend to the slab, differentiate the finite polynomial source including its input. For \(T=4t+12\) the term with index \(j\) has coefficient \(\binom{1/2}{j}T^{1/2-j}\). The absolute sums of its \(t\) and input derivatives on \([-B,B]\) bound the composed source derivative with input speed \(2|b'|+3\sqrt2|\lambda'|+8|\nu'|\). The three subtractions contribute at most \((|b'|+|\lambda'|+|\nu'|)/\sqrt2\) in centered norm, since the centered norms of \(X^2,XY,XZ\) are \(1/\sqrt2\). The projection coefficients \(a\) are fixed. Adding that derivative bound times the slab half-width to the midpoint residual norm therefore bounds the centered \(L^2\) norm throughout the slab, without interval subtraction of large nearly equal expectations. All remaining bounds are directly evaluated on the closed slabs. The [six records](compact-variance-59-checks.jsonl) provide one exact compact point check with the round-58 envelope, four slab certificates for the refined trial, and the pointwise radius test below. The group laws and ordinary estimates determine their scope through the two field families.

In exploratory scalar evaluations, splitting off the entire \(2\kappa\nu u\) alone worsened the \(t=5\) transfer bound. The component using three smaller coefficients instead controls the weighted numerator and keeps the alternate product denominator large. A certified lower bound on weight distance whose transferred value exceeds \(0.017\) would reject certification by that comparison for a specified trial and floor.

1. Extend signed collection in the difference to the Jacobi shifts of the \(W_3\) characters. At \(19/4\), use the alternative scales \((13/15,17/30)\) and projection \((9/500,1/50,7/800)\) from the independent review. The current radius is below \(1.44904434\), and the pointwise formula gives a positive product above \(0.93359\) and mark bound between \(0.01734731\) and \(0.01734732\). With all other terms fixed the formula is strictly increasing in \(\Delta\) while the product remains positive. Its crossing of \(0.017\) lies in \((1.40323718,1.40323719)\). A radius at most the lower endpoint succeeds at this point, while a rigorous lower bound at least the upper endpoint rejects relying on that specified envelope alone. This is a point test for the next trial.
