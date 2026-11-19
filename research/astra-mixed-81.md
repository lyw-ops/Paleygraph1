# A weighted second increment and all-height tracking of the real stationary row

Let \(a=2031/128\), and let \(Q\) be the closed complex square centered at \(a\) of half-width \(2^{-17}\). The actual marked Picard orbit from the Jacobi seed \(V_0=S=2\sqrt n K e_0\) satisfies, uniformly for \(t\in Q\) at all sufficiently large eligible primes,
\[
        0.0230 <
 \frac{\mathbb E_n|V_1-S|^2|V_2-V_1|^2}{\mathbb E_n|V_2-V_1|^2}
        < 0.0377.                                                     \tag{1}
\]
Here and below the second norm is normalized by counting probability. For the separate nine-center orbit at real \(t\in Q\), its height-600 predictor tracks the genuine stationary row in a truncated quadratic cost. The estimate holds directly at finite field size, also for arbitrarily many subsequent real Picard steps. Applying 150 adjoint tests to the stationary equation gives
\[
       \limsup_{p\to\infty}\sup_{t\in Q\cap\mathbb R}|m_p(t)|
                 <1.67\cdot10^{-275}.                               \tag{2}
\]
The positive tolerance concerns the real mark. The complex stationary section at arbitrarily large sizes and the theta limit remain open. [Interval checker](astra-mixed-81-check.py) · [Three records](astra-mixed-81-checks.jsonl)

## The two actual transports on the complex square

In a subsequential compact model put \(S=\sqrt8\Re J\), \(F(x)=\sqrt{4t+x^2}\), \(G=\mathcal K F(S)\), and \(\Delta=\mathcal K(F(S+G)-F(S))\). Write \(Y_m=\mathcal K T_{2m}(\Re J)\), \(Y=Y_1\). The \(Y_m\) are independent, each distributed as the half sum of two independent compact symplectic standard traces of dimension \(2m\), independently of \(J\). In particular each has variance \(1/2\), sup bound \(2m\), mean zero and vanishing odd moments. Its fourth cumulant is \(-1/8\) for \(m=1\) and zero for \(m\ge2\). Indeed the standard tensor square splits as the trivial and symmetric-square representations in dimension two, with an additional primitive exterior square in higher dimension. The fourth moment of one standard is consequently two or three. Independence and scaling give the stated cumulant. [Joint symplectic factors and exact physical Chebyshev columns](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain)

The absolutely converging expansion is \(G=\sum_m b_m(t)Y_m\), where
\[
 b_m(t)=2\sqrt t\sum_{k\ge m}{1/2\choose k}(2/t)^k
                     2^{1-2k}{2k\choose k-m}.
\]
It follows from the cosine series of \(\cos^{2k}\). The sum of the uniform costs at binomial order \(k\) is at most \(4\sqrt{|t|}\,k|2/t|^k\), since the cosine coefficients are nonnegative and sum to one before the scalar binomial coefficient. In particular the joint fourth moment of first transports at any four floors in \(Q\) follows exactly by polarization of the independent series. For \(B_{uv}=\frac12\sum_m b_m(u)b_m(v)\), this gives
\[
 \mathbb E G_u G_v G_w G_z
    =B_{uv}B_{wz}+B_{uw}B_{vz}+B_{uz}B_{vw}
      -b_1(u)b_1(v)b_1(w)b_1(z)/8.                                \tag{3}
\]
The identity also permits conjugations by conjugating the corresponding coefficients.

To estimate the distinct, nested second increment set
\[
 Z=\mathcal K(SY),\qquad A=\mathcal K(Y^2),\qquad
 T=c\beta Z+\tfrac12 q\beta^2 A,\qquad c=0.120,\quad q=0.112.
\]
Here \(\beta\) is the coefficient of \(Y\) truncated through order 18. Conditional on \(J\), \(Z,A\) are centered and orthogonal. Their second moments are \(2,3/8\), respectively. Indeed \(Z\) is twice the rank-three field, and \(A=(D+D^\vee+2R)/4\) in the compact model, for the transported Legendre symmetric squares and cross product. The fresh \(SL_3^2,SL_4,Sp_8\) derived factors act independently over the Jacobi torus. The second moment of \(A\) can also be computed by \(\operatorname{Var}(Y^2)=3/8\). Its two new group types have constant second moments on their determinant cosets. [Rank-three normalization](joint-law-32.md) · [Transported symmetric squares](astra-joint-64.md) · [Transported cross product](astra-rankeight-60.md)

The independence from the whole family \(Y_m\) needs one extra comparison. The only possible shared simple factor with \(Z,A\) is a pure dimension-eight symplectic standard with the \(Sp_8\) of \(R\). On the two boundary fibers the latter has the identical weight lists \((-2,-2,0^4,2,2)\). For \(N_8\), the two ordinary boundary blocks have size eight and trivial character. Thus one fiber has the two nonzero weights \(-8,8\) and the other is all zero, with fibers exchanged for its quadratic twist. Neither standard can coincide with \(R\) up to a scalar line twist or duality, since the weight diameters differ. A shared simple symplectic factor would identify the standards up to those operations by the product-group criterion (the standard is the unique dimension-eight irreducible of type \(C_4\)). Goursat now gives simultaneous independence for any finite list, also jointly with the circle subject to the older determinant relations. Consequently
\(\|GT\|_2=\|G\|_2\|T\|_2\), with \(\mu^2=\|T\|_2^2=2|c\beta|^2+(3/8)|q\beta^2/2|^2\). [Boundary blocks for the pure sources](parallel-graph-shapes-23.md) · [Two lists of the mixed source](astra-rankeight-60.md)

Here are the bounds used for the nonlinear remainder. Put \(v=\|S(1/F(S)-c)\|_2\), \(\tau=\|G-\beta Y\|_2\), \(M\ge\|G\|_\infty\), and \(\delta\ge\sup_{0\le u\le1}|F''(S+uG)-q|\). Since \(G\) and its tails are independent of \(J\), contraction of the positive transport gives
\[
 \|\Delta-T\|_2\le v\|G\|_2+2c\tau+
        \tfrac12 q(M+2|\beta|)\tau+\tfrac12\delta\|G\|_4^2 =:e,       \tag{4}
\]
using upper bounds on the right. The four terms control the linear multiplier, the higher harmonics in its constant multiple, the difference of squares, and the integral Taylor remainder. The uniform imaginary cap on \(G\) follows by differentiating each binomial term in the floor along a vertical segment. Its bound is \(4\cdot2^{-17}\sqrt{|t|}\rho(1+\rho)/[(\inf\Re t)(1-\rho)^3]\) with uniform upper \(\rho\ge |2/t|\), less than \(10^{-5}\). To enclose \(\delta\), compare first to \(F_a''(\Re(S+uG))\) on the real interval \(|x|\le\sqrt8+M\), then bound the change in \(x,t\) by absolute derivatives on the rectangle of comparison. There \(|4t+x^2|\ge4\inf\Re t-M^2\). The 512 angular boxes in the checker enclose \(v\). Formula (3) gives the truncated fourth-norm bound with the unexpanded dimensional tail added in fourth norm.

The checker gives \(M<0.49454,\ e<0.00131,\ \mu>0.04138\). The lower and upper endpoints for (1) are \(((\mu\|G\|_2-Me)/(\mu+e))^2\) and \(((\mu\|G\|_2+Me)/(\mu-e))^2\); the former numerator is positive. For each finite polynomial truncation the physical-to-compact identification uses fixed-word orthogonality, then the uniformly converging first transport series and second-norm contraction of the second transport. The actual first two physical inputs and outputs have common sup caps on the larger disk. Thus convergence in normalized second norm of the successive approximations suffices for the mixed moment by bounded truncation of the approximants, or by joint weak convergence with the sup caps. The marked restoration has vanishing normalized cost at these fixed steps. Taking subsequences of floors in the closed square makes the strict margins uniform. [Physical full prefix](astra-fourth-75.md) · [Compact transfer](astra-fixed-79.md)

## A finite-field estimate beyond height 600

Use the real nine-center orbit and \(n\ge10^{30}\). Put \(W=V_{600},\ W_-=V_{599}\), write \(\Phi\) for the coordinatewise \(F\) with \(n\) at the mark, and let
\[
 R=K\Phi(W)-W,\qquad e=(I-J_0)(\Phi(W)-\Phi(W_-)),\qquad r=\|R\|_2=\|e\|_2 ,
\]
where \(J_0\) projects onto constant vectors. The compact Haar symbol \(J\) above denotes the Jacobi angle. In this section \(\Psi(h)=\min(h^2,|h|)\) coordinatewise. For every real full-site row \(U=W+h\) one has
\[
 \|K\Phi(U)-W\|_2^2 +0.04\,\mathbb E_n\Psi(h)
                \le \|h\|_2^2+25r^2.                                \tag{5}
\]
In particular, for \(h_j=V_{600+j}-W\), telescoping gives
\(\|h_H\|_2^2+0.04\sum_{j<H}\mathbb E_n\Psi(h_j)\le25Hr^2\)
simultaneously for all integers \(H\). At the genuine real stationary row \(U_*\) it gives \(\mathbb E_n\Psi(U_*-W)\le625r^2\) at each such field. Thus the unbounded part \(|U_*-W|>1\) costs at most \(625r^2\) in first norm, and the bounded part costs at most \(25r\) in second norm. By the angular prefix bound \(\limsup_p\sup_t r\le r_0=4(0.428236)^{600}<4.093\cdot10^{-221}\). This last numerical constant is field-first. Equation (5) uses the actual \(r\) at any admitted field and a height-independent constant. [Physical prefix and caps](astra-predictor-76.md) · [Jacobi covariance and contraction](astra-dissipation-80.md)

To prove (5), let \(b=4t\) or \(4n\) at the relevant coordinate, \(f(x)=\sqrt{b+x^2}\), \(x=W_i\), \(y=x+h_i\). Then
\[
 h_i^2-(f(y)-f(x))^2
   =\frac{2b h_i^2}{f(x)f(y)+xy+b}
   \ge\frac{b h_i^2}{f(x)(f(x)+|h_i|)} .
\]
The last coefficient increases with \(b\) at fixed \(x,|h_i|\). Use \(b\ge63,\ |x|\le4.8\). Both bounded predictors take their activation in an interval of length at most \(\sqrt{63+4.8^2}-\sqrt{63}\) relative to the common coordinate base \(\sqrt b\). Hence \(\|e\|_\infty<2.68\), including the physical mark. For \(|h_i|\le64\) the displayed loss exceeds \(0.09 h_i^2\) for nonzero \(h_i\). Debit \(2|e_i h_i|\le0.05h_i^2+20e_i^2\). For \(|h_i|>64\) the loss exceeds \((2\|e\|_\infty+0.04)|h_i|\). Finally \(\|K\Phi(U)-W\|_2^2=\|(I-J_0)(\Phi(U)-\Phi(W)+e)\|_2^2\) and \(|f(y)-f(x)|\le |h_i|\). Summation proves (5).

## The signed adjoint tests on the actual stationary row

Let \(h=U_*-W,\ D=\Phi'(W)\), and \(B=\Phi(W+h)-\Phi(W)-Dh\). Scalar Taylor and the global real Lipschitz bound give \(|B|\le2\Psi(h)\), so \(\|B\|_1\le1250r^2\). Put \(X_0=S/2,\ X_{k+1}=K(DX_k)\) using the true marked derivative. The stationary equation is \(h=R+K(Dh+B)\). For each \(k\),
\[
 \langle X_k,Dh\rangle=\langle DX_k,R\rangle+
                      \langle X_{k+1},Dh+B\rangle.                  \tag{6}
\]
The normalized inner product with \(X_0\) evaluates the marked component after \(K\), divided by \(\sqrt n\).

We give a numerical sup estimate for these tests. Use the absolute representation norm that sums each lift-averaged constituent's dimensional measure against \(\cosh(\eta w)\), with \(\eta=3/40\). It dominates the raw evaluation sup norm for negative fields. The symmetric lift-averaged product measures convolve, so the norm is submultiplicative for the unreduced product. For the actual \(W\) the bound is
\[
 P=4.768+3.77(\cosh(5\eta)-1)
       +1.94\,(\cosh(50\eta)-1)/50+10^{-5}<5.824 .
\]
Indeed the center mass is below 3.77 and its weights have absolute value at most five. The stored off-zero packet masses \(h_k\) have \(\sum_{1\le k\le50} k h_k<1.94\), since the full cap is 4.768 and the center includes the seed of mass at least \(2.8284\). The increasing ratio \((\cosh(k\eta)-1)/k\) bounds their excess above the unweighted mass. The off-zero excess outside those packets is at most \(5\cdot10^{-7}\) in the stronger \(1/5\) tilt, including the old unexpanded tail. Its extra zero cost does not grow under tilting. The displayed slack covers that contribution. These are the certified actual representations at height 600, with previous single-column errors included. [Full packet accounting](astra-predictor-76.md)

The bulk derivative expression \(D_t(W)=W(4t+W^2)^{-1/2}\) costs at most \(P/\sqrt{63-P^2}\) at this same tilt by the absolutely converging series. On a positive preimage the geometric transport keeps all nonzero weights and inserts at most \(\sum |w|\nu(w)\) zero mass. Since \(\cosh x\ge1+x^2/2\ge\sqrt2|x|\), it costs at most \(1+1/(\sqrt2\eta)\) times the preimage norm. For the exact physical operator, the difference between the raw product and its positive expression is supported at zero and has magnitude at most twice the unweighted product norm, termwise before summing. Replacing \(D_t(W_0)\) by \(D_n(W_0)\) costs at most \(2\|X_k\|_\infty\) there. All these errors produce a multiple of \(K e_0\), whose tilted norm is \((\sqrt p/n)\cosh\eta\). Thus if \(X_k\) costs \(M_k\), the full next cost is at most
\[
 [(1+1/(\sqrt2\eta))\,P/\sqrt{63-P^2}
     +(2P/\sqrt{63-P^2}+2)(\sqrt p/n)\cosh\eta]M_k<12M_k .
\]
The bound holds already at \(n\ge10^{30}\). Because \(X_0\) costs less than 1.5, all the true tests have cap \(1.5\cdot12^k\). [Exact one-column repair](marked-domain-53.md) · [Pooled transport measure](astra-feedback-52.md)

At each fixed \(k\), every subsequential compact limit of \(X_k\) is a negative field. For \(k\ge1\) it lies in the transport image. The positive \(DX_k\) is orthogonal to the negative \(R\) by the common parity element, so \(\langle DX_k,R\rangle=o(1)\) uniformly in the real floor at fixed \(k\). Fixed-depth identification follows by approximation of \(W\) as in the prefix proof, polynomial approximation of the bounded derivative and product, and normalized second-norm contraction under \(K\). The sup estimate just proved and the fixed uniform caps permit multiplication at each step. The exceptional derivative at the mark has vanishing normalized cost at fixed \(k\). The first output \(K\Phi(W)\) also has uniformly bounded physical sup norm: split its marked baseline \(2\sqrt n K e_0=S\), apply the same tilted estimate to the convergent bulk activation series, and absorb the bounded exceptional correction times \(Ke_0\). It follows that \(K\Phi(W)_0/\sqrt n=o(1)\).

Since \(\|X_0\|_2\to1\) and \(\|D\|_\infty<0.52\), the first adjoint step has limiting second norm at most \(0.52\). For every subsequent step \(\|DX_k\|_2\le0.428236\|X_k\|_2\) in the compact model. In fact \(|D|^2\le g_0(|\Re J|)\) by the actual predictor cap \(|W-S|<1.94\), and the conditional square of \(X_k\) is constant by the Jacobi covariance theorem. The certified angle integral supplies the factor. Hence \(\limsup\|DX_N\|_2\le0.52(0.428236)^N\) for every fixed \(N\ge1\). [Angular estimate and endpoint exclusion](astra-dissipation-80.md)

Iterate (6) \(N\) times to evaluate the scaled mark. The \(N\) residual pairings vanish in the field limit. Through \(k=N\), the \(B\) terms cost at most \(1250r^2\sum_{k=0}^N1.5\cdot12^k\). For the last \(Dh\) term apply the second norm of \(DX_N\) to \(|h|\le1\) and its sup to \(|h|>1\). The former costs \(25r\|DX_N\|_2\); the latter costs \(625r^2(0.52)(1.5)12^N\). Finally \(|m_p|=|\operatorname{arsinh}((U_*)_0/(2\sqrt n))|\le |(U_*)_0|/(2\sqrt n)\). Thus the uniform limsup is at most
\[
       \tfrac12[25(0.52)(0.428236)^N r_0+2600\,12^N r_0^2].
\]
At \(N=150\) the upper endpoint is below \(1.669\cdot10^{-275}\). All powers here have fixed length before taking the prime limit. The quadratic cost from the unbounded part and centered nonlinear remainder increases with the sup bounds on those tests.

1. Bound the weighted tails of the actual stationary remainder against the adjoint tests \(X_k\), or obtain subexponential physical sup growth for the \(X_k\). Equation (6) identifies the two outstanding priced terms after parity cancellation.
2. At heights past 600, use (5) to locate the rows whose large deviations have small first norm. Estimate their squared mass under the adjacent genuine increment and control branches on the complex exceptional sites. The all-height real first-norm bound alone allows concentrating second moments.
3. Extend (1) to the third actual marked return by retaining the multipliers of the full first feedback and the two transported quadratic sectors, including arithmetic determinant correlations when multiplying the associated fields.
