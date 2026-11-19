# A positive trial starting from three distinguished feedbacks

For the actual real stationary mark, through sufficiently large eligible primes and prime squares, the following strict uniform limiting bounds hold.

| Floor interval | Upper bound on \(\limsup_q\sup_t|m_q(t)|\) | Lower bound on scaled bulk trial products |
| --- | ---: | ---: |
| \([83/16,31/5]\) | \(0.01699\) | \(1.49\) |
| \([5,83/16]\) | \(0.0199\) | \(0.92\) |
| \([19/4,5]\) | \(0.0258\) | \(0.52\) |

The prime \(0.017\) tolerance now reaches \(83/16\). The trial uses one update from a specified sum of the first three arithmetic feedback fields. Its input and output have pointwise bounds derived from the **difference**, in which the dominant constant and first cosine coefficients cancel before absolute values are taken.

## Exact trial and the pointwise difference

Write \(x=\sqrt n K e_0\), \(y=K(x^2)\), \(z=K(xy)\), \(w=K(xz)\), \(S=2x\), and \(H(s)=\sqrt{4t+s^2}\). Let \(P_t\) be the degree-16 polynomial from the eighth Taylor expansion of the square root centered at squared input 12, as in [round 57](weighted-positive-57.md). Let \(c_{jk}\) be its expansion after substituting \(S+R\) with limiting seed \(S=2\sqrt2 C_1\), in the terms \(R^j C_k\) where \(C_k=T_k(C_1)\). Take
\[
 b=c_{02},\quad \kappa=(4t+6)^{-1/2},\quad
 \lambda=2\kappa b\ell_*,\quad \nu=2\kappa\lambda n_*,
 \qquad V=S+by+\lambda z+\nu w,\quad V^+=S+KP_t(V).
\]
Here \((\ell_*,n_*)=(19/20,3/4)\) on the first two intervals and \((9/10,13/20)\) on the last. All amplitudes are positive. The exact difference is
\[
 V^+-V=K\big[P_t(V)-bx^2-\lambda xy-\nu xz\big].
\]
The three source subtractions here are finite-field identities.

For the upper bound, replace \(by+\lambda z+\nu w\) by \(bY+\sqrt2\lambda W_3+2\nu F_4\), using the Legendre and rank-three lift fields \(Y,W_3\) and the rank-four field \(F_4\). The exceptional corrections are controlled in the same two-character convolution calculus. In detail, \(y=(q/(2n))Y-x/\sqrt n\), \(z=(c^3/2)(W_3+C_1/q)-y/\sqrt n\), \(w=(c^4/2)(F_4-D_4Ke_0)+y/(2n)-z/\sqrt n\) with \(c=\sqrt{q/n}\) and bounded \(D_4\). Thus each replacement is a finite sum of fixed-rank fields with coefficients \(O(n^{-1/2})\). Expanding each fixed-degree product before applying \(K\) gives a vanishing rank cost even after \(K\), including the one exceptional lift correction. This also justifies the limiting scale substitution in \(c_{jk}\). The three subtractions then become \(b C_2,\sqrt2\lambda C_1Y,2\nu C_1W_3\), up to a constant killed by \(K\) and the same vanishing cost. [Rank-three lift identities](astra-rankthree-55.md#exact-feedback-and-arithmetic-weights) · [Rank-four alias](rank-four-arithmetic-56.md#the-next-distinguished-complex-feedback) · [Fixed-rank exceptional control](marked-domain-53.md#the-exceptional-character-stays-at-the-mark)

Let \(D_Y,D_{W_3},D_{F_4}\) denote their positive symmetric boundary measures. Their masses are \(2,3,4\). For the general source \((j,k)\) use the measure \(D_R^{*j}*(\delta_k+\delta_{-k})/2\) with \(D_R=bD_Y+\sqrt2\lambda D_{W_3}+2\nu D_{F_4}\). Its first absolute moment times \(|c_{jk}|\) bounds the rank cost after \(K\). For a centered symmetric input measure with atom at weight \(j\) and \(-j\), this shifted first moment uses \(\max(j,k)\) in place of \(j\). In \((0,2)\) replace the coefficient by \(c_{02}-b\). In \((1,1)\) use the three amended coefficients \(c_{11}b-\sqrt2\lambda,\ c_{11}\sqrt2\lambda-2\nu,\ c_{11}2\nu\) for \(Y,W_3,F_4\) respectively. All remaining terms are charged positively. The checker computes the resulting difference radius \(\Delta\) by convolution of the finite weight arrays. The input radius for \(R\) is \(B_R=2b+3\sqrt2\lambda+8\nu\), so \(\|V\|_\infty\le B=2\sqrt2+B_R+o(1)\) and \(\|V^+-V\|_\infty\le\Delta+o(1)\). [Packet projection and boundary moments](astra-feedback-52.md#reading-rank-from-two-mellin-characters)

## Residual bound in Euclidean norm

Use normalized counting norm and the old compact probability model of \((X,Y,Z,W)\), with \(S=2X\) now the limiting seed. Define \(A(S)=H''(S)/2\), \(a_{\max},a_{\min},a_{\rm var},M_3,D,L\) as in [round 56](centered-positive-56.md#scalar-bounds-for-an-expansion-at-the-seed), and \(a_2^*=(a_{\max}^2+a_{\min}^2)/2\). The chord bound gives \(\mathbb E A(S)^2\le a_2^*\) as in round 57. Write \(R=bY+\lambda Z+\nu W\) and \(v=\mathbb E(R^2\mid S)=(b^2+\lambda^2+\nu^2)/2\). The conditional moments satisfy
\[
 \begin{split}
 \mathbb E(R^3\mid S)&=\lambda^3 S/16,\\
 \mathbb E(R^4\mid S)&=3v^2-b^4/8+\nu^4 S^2/256,\qquad
 Q_*:=2v^2-b^4/8+\nu^4/32\ \ge\ \operatorname{Var}(R^2\mid S).
 \end{split}
\]
Indeed \(Y\) is independent of \((S,Z)\), the first conditional moments of \(Z\) through degree four are \(0,1/2,S/16,3/4\), and \(W\) has conditional moments \(0,1/2,0,3/4+S^2/256\) given the entire older family. Expanding uses those conditional identities directly. [Rank-three conditional moments](nested-positive-54.md#the-tilted-midpoint-in-the-third-increment) · [Exact rank-four fourth moment](rank-four-arithmetic-56.md#common-compact-law-and-an-exact-fourth-moment)

Expand \(H(S+R)\) at \(S\) to order two. Bring in \(P_t(S)\) in the scalar term, with its uniform approximation error \(e_S\). Subtract all three sources of the difference and a constant, and separate the centered source into the following terms up to approximation errors:
\[
 \begin{split}
 &P_t(S)-bX^2-\mathbb E[P_t(S)-bX^2]+v(A(S)-\mathbb E A(S)),\\
 &\big(bH'(S)-\lambda S/2\big)Y+
   \big(\lambda H'(S)-\nu S/2\big)Z+\nu H'(S)W,\\
 &A(S)(R^2-v).
 \end{split}
\]
The first line has norm at most \(\tau+v a_{\rm var}\), where \(\tau^2=\tfrac12\sum_{k\ge4}c_{0k}^2\). It is orthogonal to the remaining two by conditioning on \(S\). The third line has variance at most \(a_2^*Q_*\).

For a coefficient pair \((r,f)=(b,\lambda)\) or \((\lambda,\nu)\), put \(o=\kappa r-f/2\). An upper bound for \(\|rH'(S)-f S/2\|^2\) is
\[
 L_{r,f}=r^2D^2+4o^2+2r(o)_+\frac{6}{(4t)^{5/2}}.
\]
In fact \(\|H'(S)-\kappa S\|\le D\), and the cross term before multiplying by \(2ro\) is \(C=\mathbb E[S H'(S)]-4\kappa\). Jensen applied with density \(S^2/4\) gives \(C\ge0\), using the tilted mean 6 of \(S^2\). Taylor at 6 with the same tilt gives \(C\le6/(4t)^{5/2}\) since \(\mathbb E[S^2(S^2-6)^2]=16\). The second line therefore has variance at most \((L_{b,\lambda}+L_{\lambda,\nu}+\nu^2 L)/2\). Its only nonzero covariance with the third line comes from the \(Z^3\) contraction, so twice its absolute value is at most \(\lambda^2\sqrt{L_{\lambda,\nu}}\,a_{\max}/4\) by Cauchy–Schwarz. This variance calculation keeps the signed linear and quadratic covariance without asserting independence of \(S,Z\).

Take one square root of the sum of the three variance bounds and the covariance bound. The cubic Taylor remainder adds at most \((M_3/6)B_R\sqrt{v^2+Q_*}\). Also add \(e_S+e_B\), the uniform polynomial errors on the seed and full input radii. These bounds prove a limiting upper bound \(D_\Delta\) for \(\|V^+-V\|_{2,n}\), since \(K\) contracts and kills constants. Uniformity in \(t\) follows by fixed-degree polynomial approximation of the bounded continuous model tests on each compact floor interval.

## Positive transfer and replay

Use the trial with scaled bulk sum \(P_t(V)\), marked sum 2 and complementary difference \(K\) of this sum. Its scaled bulk product differs from \(t+(V^2-(V^+)^2)/4\) by at most \(C=(2H(B)+e_B)e_B/4+o(1)\). Positivity follows from the strict bounds \(2\sqrt t>e_B\) and \(t-(2B+\Delta)\Delta/4-C>0\). The same square-root weight comparison as in [round 52](prime-increments-52.md#positive-pair-and-marked-transfer) bounds the distance via \(D_\Delta\) and certifies the stated mark tolerances after normalizing at the root. The [checker](distinguished-positive-58-check.py) uses rational closed slabs with Arb192 for the scalar margins. The [three records](distinguished-positive-58-checks.jsonl) certify the three ranges. The ordinary proofs supply the arithmetic and analytic hypotheses for those interval checks.

In point diagnostics at \(t=5\), using the undamped next coefficient at each step and stopping after three distinguished terms gave a mark upper enclosure about \(0.0255\). Adding a fourth undamped term at that floor made the scalar product envelope negative. These observations motivated the reduced coefficients. The finite polynomial envelope's failure leaves positivity of that different trial undecided.

A floating calculation of the specified damped trial at \(p=1000033\) gives RMS difference \(0.0218731\) at \(t=5\), compared with \(0.0254662\) from the Taylor bound. Substituting just that floating RMS into the pointwise transfer gives about \(0.016892\). At \(19/4\), the corresponding RMS is \(0.0261397\), and the substituted bound is about \(0.022134\). These diagnostics motivate an exact compact variance calculation at 5 and a separate improvement of the pointwise bound at lower floors.

1. Compute the exact centered \(K\)-input variance of the degree-16 trial from compact mixed moments through degree 32, and retain further signed terms for the pointwise bound. A strict product floor and a transferred mark bound below \(0.017\) at \(t=5\) are the first joint test. A certified lower bound for the exact variance whose transfer expression already reaches \(0.017\) rejects changing only the variance estimate with the current pointwise bound. A lower bound on the true weight distance can likewise reject certification by the specified transfer formula.
