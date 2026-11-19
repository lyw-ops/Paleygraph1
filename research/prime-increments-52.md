# Prime joint moments and positivity of adjacent polynomial iterates

For the actual stationary mark \(m_p(t)\) through eligible primes, three positive degree-28 polynomial updates give
\[
 \limsup_{p\to\infty}\ \sup_{35/4\le t\le 10}|m_p(t)|<0.0169,
 \qquad
 \limsup_{p\to\infty}\ \sup_{17/2\le t\le 35/4}|m_p(t)|<0.0184.
\]
With four updates, tracking the second Mellin moment of each difference strengthens the first bound to
\[
 \limsup_{p\to\infty}\ \sup_{63/8\le t\le 9}|m_p(t)|<0.0169 .
\]
Combined with the [round-51 bounds](astra-warm-51.md), the fixed \(0.017\) tolerance extends to \([63/8,25]\). The construction keeps the dependence between successive iterates in the positivity check. A fourth-moment estimate for the first Jacobi feedback then reduces the second increment in normalized Euclidean norm. The proof uses interval enclosures of scalar constants. The bounds concern a fixed positive tolerance and leave the \(t=1/2\) estimate and the all-prime theta limit open.

## A rank bound for differences

Use the [round-51 notation](astra-warm-51.md). Thus \(S=2\sqrt n Ke_0\) and \(s_p=2\sqrt{p/n}\). Let \(H_t(x)=\sqrt{4t+x^2}\), and let \(P_t\) be its Taylor polynomial of degree 28 at zero. Define the actual finite polynomial iterates
\[
 V_0=S,\qquad V_j=S+K P_t(V_{j-1}),\qquad R_j=V_j-S .
\]
For the limiting seed scale \(s=2\sqrt2\), write
\[
 P_t(sx+y)=\sum_{l,k}c_{lk}(t)T_k(x)y^l,\qquad
 F_t(b)=\sum_{l,k}(l+k)|c_{lk}(t)|b^l .
\]
Here \(T_k\) is the first-kind Chebyshev polynomial. Put \(b_0=0,\ b_j=F_t(b_{j-1})\), \(B_j=s+b_j\), and \(\Delta_j=b_j-b_{j-1}\). For each fixed \(j\), uniformly on compact positive floor intervals,
\[
 \|V_j\|_\infty\le B_j+o(1),\qquad
 \|V_j-V_{j-1}\|_\infty\le\Delta_j+o(1).                         \tag{1}
\]
The individual estimate is the graded rank calculation of round 51. For the difference, use
\[
 R_{j-1}^l-R_{j-2}^l
 =(R_{j-1}-R_{j-2})\sum_{r=0}^{l-1}R_{j-1}^{l-1-r}R_{j-2}^{r}
\]
in each summand before applying \(K\). The degree-zero input in \(R\) cancels. If the prior difference has rank cost \(\Delta_{j-1}+o(1)\), the cost for the new difference is bounded by
\[
 \sum_{l\ge1,k}(l+k)|c_{lk}|
       (b_{j-1}-b_{j-2})\sum_{r=0}^{l-1} b_{j-1}^{l-1-r}b_{j-2}^r
     +o(1)=\Delta_j+o(1).
\]
The base \(j=1\) is the ordinary individual estimate since \(R_0=0\). This works with the exact scale \(s_p\) first, then its limit. The bad-character cost is \(o(1)\) uniformly because the degrees and number of updates are fixed, including in the difference representation. The sup norm is bounded by the negative Mellin representation cost.

In particular, on the bulk
\[
 \frac{H_t(V_{j-1})^2-V_j^2}{4}
 \ \ge\ t-\frac{(2B_{j-1}+\Delta_j)\Delta_j}{4}-o(1)=L_0-o(1).
                                                                    \tag{2}
\]
This uses \(\big|V_j^2-V_{j-1}^2\big|\le(2B_{j-1}+\Delta_j)\Delta_j+o(1)\) pointwise. It exploits the shared \(V_{j-1}\) in the positive activation and the next field. At \(t=35/4\) the coarse-rank fourth-step comparison exceeds the target in a floating diagnostic, while the certified third step has slack.

## Second Mellin moment of a difference

The [second moment of Mellin weights](astra-feedback-52.md) bounds the rank cost and weight second moment of a positive absolute-coefficient sum. Use this both for \(R_j\) and its successive differences. All pooled distributions have mean zero, and the second moment of a convolution of two measures is the first measure's second moment times the other's mass plus the same term with the two measures exchanged.

To propagate the difference \(R_j-R_{j-1}\), use the same telescoping product as for (1). Suppose \((a,c),(b,d),(\delta,e)\) are mass and second-moment bounds for \(R_{j-1},R_{j-2},R_{j-1}-R_{j-2}\), respectively. At power \(l\), the term with \(u\) copies of the newer row and \(v\) copies of the older row, \(u+v=l-1\), has input mass and second moment at most
\[
 A=\delta a^u b^v,\qquad J=e a^u b^v+
   \delta\big(u c a^{u-1}b^v+v d a^u b^{v-1}\big).
\]
Terms whose exponents would be negative are omitted with their zero multiplicity. Sum \(A,J\) over \(v=0,\dots,l-1\). For seed mode \(k\) the second moment becomes \(E=k^2 A+J\), and the output mass is bounded by the minimum of \((k+l)A,\sqrt{AE}\), and \(kA+J/(4k)\), with the last bound used for \(k>0\). The second moment of the output is \(E\). These are the same inequalities for pooled weights proved for the individual row in the feedback calculation. They are monotone in all input bounds, so they can be applied to the sums over the telescoping terms. Summing over the Laurent coefficients supplies the next difference radii. The first difference and first row have the same radii because \(R_0=0\). The finite recursion makes every term containing an exceptional correcting column \(o(1)\) in sup norm uniformly on the compact floor interval, by the coarse-rank bound at that fixed degree. Replacing \(B_i,\Delta_j\) by these two-moment bounds in (2) is therefore justified.

## A tilted second-increment estimate

Write \(D_j=\|V_j-V_{j-1}\|_{2,n}\). Let \(G=V_1-S=K P_t(S)\). The fixed-mode joint prime law gives the limit of \((S,G)\) as \((X,Z)\), with \(X=2\sqrt2\cos\Theta\) and \(Z=\sum_{k\ge2}c_{0k}Y_k\). Here \(\Theta\) is uniform and the \(Y_k\) are the independent averages of two Haar symplectic traces of the indicated rank, independent of \(X\). Only the even \(k\)'s occur. The limit is uniform for the polynomials used on each compact interval, because it involves finitely many bounded fields and continuously varying coefficients. This gives
\[
 \mathbb E X^2=4,\quad \mathbb E X^4=24,\quad
 v:=\mathbb E Z^2=\tfrac12\sum_{k\ge2}c_{0k}^2,\quad
 \mathbb E Z^4\le 3v^2.
\]
For the last inequality, each trace has variance one and fourth moment at most three, with fourth moment two in rank two, and its average with an independent copy has variance \(1/2\) and fourth moment at most \(3/4\). Independence and centering then give the bound for the sum. [Joint law for the first-kind Chebyshev fields](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain) · [Symplectic trace moments](https://www.ruhr-uni-bochum.de/imperia/md/content/stochastik/veroeffentlichungen/stolzdsm.pdf)

Convexity of \(H_t\) gives the pointwise bound
\[
 [H_t(X+Z)-H_t(X)]^2
 \le Z^2\,\frac{(X+Z/2)^2}{4t+(X+Z/2)^2}.
\]
For \(v>0\), tilt by \(Z^2/v\) and put \(A=(X+Z/2)^2\). Under this probability, \(X\) keeps its law and stays independent of \(Z\). Thus the tilted mean of \(A\) is at most \(4+3v/4=:M\). Its tilted variance is at least \(\operatorname{Var}(X^2)=8\), by the law of total variance conditional on \(Z\), since \(\mathbb E X=\mathbb E X^3=0\). Also \(0\le A\le L=(s+b_1/2)^2\) by the rank bound for \(G\). The function \(f(u)=u/(4t+u)\) is increasing and satisfies \(f''(u)\le-8t/(4t+L)^3\) on \([0,L]\). Taylor's inequality at the tilted mean yields
\[
 \mathbb E[H_t(X+Z)-H_t(X)]^2
 \le v\left[\frac{M}{4t+M}-\frac{32t}{(4t+L)^3}\right].          \tag{3}
\]
If \(v=0\), the left side is zero. The field limit of the continuous ideal difference holds uniformly by boundedness of the input fields and continuity in \(t\). Since \(K\) contracts normalized Euclidean norm, the same square-root bound plus \(e_0+e_1+o(1)\) holds for \(D_2\), where \(e_i\) is the alternating Taylor remainder bound on \([-B_i,B_i]\). Also \(D_1\to\sqrt v\) uniformly. For \(j\ge3\) the usual Lipschitz recursion gives
\[
 D_j\le\frac{B_{j-1}}{\sqrt{4t+B_{j-1}^2}}D_{j-1}
              +e_{j-2}+e_{j-1}+o(1).
\]
The interval verifier checks \(B_i^2/(4t)<1\) at all inputs of the Taylor updates.

## Positive pair and marked transfer

Set \(U=P_t(V_{j-1})\), make \(u_0=2\) and \(u_i=U_i/\sqrt n\) for \(i\ne0\), and put \(v'=Ku\). Since \(KU=V_j-S\), one has \(\sqrt n\,v'=V_j-U_0 Ke_0\). The last term is \(O(n^{-1/2})\) in sup norm. Consequently the scaled bulk product of the trial factors \((u\pm v')/2\) differs from the ideal product \((H_t(V_{j-1})^2-V_j^2)/4\) by at most
\[
 C=\frac{(2\sqrt{4t+B_{j-1}^2}+e_{j-1})e_{j-1}}4+o(1).
\]
The verifier ensures \(L_0-C\) is bounded away from zero and \(2\sqrt t>e_{j-1}\). Thus \(u>|v'|\) at every coordinate for all sufficiently large primes, including the mark. The factors are in the complementary Fourier spaces and have equal means by \(K1=0\). Their product at the mark is \(1+O(n^{-1})\) and their marked logarithm is \(O(n^{-1/2})\).

Rationalizing the two square-root differences gives, with \(C\) denoting its nonvanishing bound above,
\[
 \|\sqrt{w'}-\sqrt{w}\|_2
 \le d:=
 \frac{(2B_{j-1}+\Delta_j)D_j}{4(\sqrt t+\sqrt{L_0})}
       +\frac{C}{\sqrt{L_0-C}+\sqrt{L_0}}+o(1)
\]
after normalizing the trial product weights \(w'\) at the mark. The first fraction compares the ideal product to the target. The second fraction transfers the Taylor remainder. The [marked weight comparison](marked-affinity-51.md#bulk-errors-at-cold-weights) bounds the resulting absolute marked logarithm by
\[
 d\,\frac{\sqrt t+d}{\sqrt{1+(\sqrt t+d)^2}}+o(1)
\]
using \(\|\sqrt{w'_{\rm bulk}}\|_2\le\sqrt t+d+o(1)\). The [checker](prime-increments-52-check.py) encloses every scalar bound by covering the displayed closed intervals with rational slabs of width \(1/256\). The four [records](prime-increments-52-checks.jsonl) include a fourth-step coarse comparison on \([9,10]\) and the two-moment fourth step on \([63/8,9]\). No arithmetic experiment at fixed \(p\) is used to establish the interval bounds.

1. Retain the pooled weight histogram of each difference to refine the second-moment bound. A strictly positive product lower bound and a defect below the target budget at a smaller fixed floor would extend the construction. If the calculated rank majorant loses positivity, that rejects this enclosure only. A certified nonpositive actual pair along unbounded primes would reject the underlying predictor.
2. Establish a joint estimate for the third increment, retaining covariance of the first two projected activation fields. A strict improvement over the sup-norm Lipschitz factor would reduce the transfer error where positivity is already known. A sharp prime lower bound on the same product dispersion could instead rule out this degree and depth at the proposed tolerance.
