# Signed rank-three collection and a seven-field positive transfer

For the actual stationary mark the following bounds are uniform in the real floor, in the limit along the eligible primes and prime squares.

| Closed floor interval | Strict upper bound on the limiting absolute mark | Strict lower bound on the scaled bulk trial product |
| --- | ---: | ---: |
| \([35/8,143/32]\) | \(0.019\) | \(0.29\) |
| \([143/32,9/2]\) | \(0.01699\) | \(0.58\) |
| \([9/2,309/64]\) | \(0.01699\) | \(0.67\) |

This brings the contiguous \(0.017\) tolerance down to \(143/32\) from \(309/64\). It is a positive one-step trial bound. The desired completion at the marked cancellation depth and the ETH26 limit remain open.

## One-step source and signed collection

Keep \(V=S+by+\lambda z+\nu w\), \(S=2x\), and \(V^+=S+K P_t(V)\) with the degree-16 polynomial centered at squared argument 12. Write \(\kappa=(4t+6)^{-1/2}\) and
\[
 b=\rho c_{02},\qquad \lambda=2\ell\kappa b,\qquad \nu=2h_*\kappa\lambda.
\]
For the intervals use \((\rho,\ell,h_*)=(99/100,163/200,463/1000)\). The source of \(V^+-V\) is \(F=P_t(V)-bx^2-\lambda xy-\nu xz\). The exact aliases permit the lift expansion of this source using \(bY+\beta W_3+\gamma F_4\), where \(\beta=\sqrt2\lambda\) and \(\gamma=2\nu\), with vanishing error on application of \(K\). The fixed-word error bound and the exceptional frequency are treated by the earlier positive trial. [Exact aliases and transfer](distinguished-positive-58.md) · [Previous signed Legendre collection](compact-variance-59.md)

First collect the two Legendre symmetric-power labels \((u,v)\) within each cosine and correction degree. Expand the remaining powers as \(W_3^l F_4^h\). The three exact source terms are removed from the scalar \(C_2\), the \(C_1Y\), and the \(C_1W_3\) coefficients respectively. In the retained block \(l\le4,h\le3,u+v\le4,k\le8\), expand \((4W_3)^l\) in the two \(GL_3\) labels and Jacobi shift using the integer Pieri table. A \(C_k\) coefficient with \(k>0\) contributes half at each of the shifts \(\pm k\). Pool terms with the same Legendre degrees, \(F_4\) power, two \(GL_3\) labels and total Jacobi shift before taking absolute values. The weighted boundary first moment then bounds the dimension cost of \(K\) applied to the source. For the other terms use the unsigned shifted first moment of the existing lift packets. [Rank-three tables and boundary measures](rank-four-arithmetic-56.md)

In the sign convention of the integer table, a collected label at twist one has weight measure given by convolving the rank-three fiber at \((a,b,c,d)\), the centered \(F_4^h\) packet and \((v+1)\sum_{j=0}^u\delta_{-2u+4j}\), then shifting by the negative of the pooled exponent. The two boundary costs agree after exchanging the Legendre labels, the rank-three factors and reversing the signed exponents. Taking absolute values after collection and multiplying by these first moments yields a uniform bound \(\Delta\) on \(|V^+-V|\) up to the vanishing fixed-rank error.

At \(t=19/4\), with scales \((1,13/15,17/30)\), this specified collection gives \(1.43706<\Delta<1.43707\), above the previous three-field threshold \(1.40323719\). The seven-field transfer below gives an absolute mark below \(0.0148\) and a product above \(0.969\) at the same point. The bracket concerns this upper-envelope construction.

## Source projections and arithmetic moments

Use the seven principal directions
\[
 (y,z,w,u_5,Q,D,E)
 =K(x^2,xy,xz,xw,C_4,H_2,H_\times),
 \qquad H_2=(A^2+B^2)/2-1,\quad H_\times=AB .
\]
Here \(u_5\) denotes the earlier field \(K(xw)\). The two Legendre traces \(A,B\) are independent standard \(SU(2)\) traces. The last three arguments are the normalized finite Mellin lifts with these compact limits. At good characters their arithmetic nonpunctual components give the indicated transformations under \(K\); the finite defects in fixed products are handled as for the three earlier directions. For the standard-character unit in a symmetric-square expansion the ordinary \(K\) annihilates the constant term. In particular the variance calculation may use centered sources. [Exact feedback and higher moments](weighted-arithmetic-57.md) · [The next three sources](two-node-groups-59.md) · [Cross Legendre group](astra-rankeight-60.md)

In the compact limit put \(S=2X\), \(Y_0=A+B\), \(J_0=J+J^{-1}=\sqrt2 X\), and \(\mathcal V=S+bY+\lambda Z+\nu W\). The seven centered inputs
\[
 H=(X^2-1,XY,XZ,XW,J_0^4/2-2J_0^2+1,H_2,H_\times)
\]
are mutually orthogonal with variances \(v=(1/2,1/2,1/2,1/2,1/2,1/2,1)\). For the old coordinates this follows from their zero conditional means and constant second moments given the Jacobi torus. The Chebyshev term is orthogonal to the centered quadratic Jacobi term. For the Legendre contractions use the independent symmetric traces and note that both quadratic sources are centered and even under simultaneous sign reversal. Their own cross product has zero mean by a sign reversal of one factor. Since \(K^2=I-J_{\rm av}\), the compact centered residual norm squared after subtracting the seven principal fields with coefficient vector \(a\) is
\[
 \operatorname{Var}(F)+\sum_i\big(v_i a_i^2-2a_i\operatorname{Cov}(F,H_i)\big).
\]
The first and fifth covariances follow by multiplying the previous integer moments by \(J_0^2/2-1\) and \(J_0^4/2-2J_0^2+1\). For the last two replace the \(Y_0^j\) contraction by
\[
 \sum_{r=0}^j\binom jr c_{r+2}c_{j-r}-\mathbb E Y_0^j,
 \qquad
 \sum_{r=0}^j\binom jr c_{r+1}c_{j-r+1},
\]
respectively, with \(c_{2m}=\mathrm{Cat}(m)\), \(c_{2m+1}=0\). The old source subtractions are orthogonal to those terms. This is an exact compact computation of fixed polynomial moments.

Denote the output principal fields by \(T=(Y,Z,W,U_5,Q,D,E)\). Given the Jacobi coordinate they have zero means, constant second moments \(v_i\) and independent derived factors. The last three outputs are the real average of two independent \(Sp_4\) traces, the real part of an \(SL_4\) coset trace, and an independent real \(Sp_8\) trace. Consequently their fourth moments are \(3/4,3/4,3\), respectively. In the second of these evaluations the conditional fourth moment has the two determinant terms, which average to zero because the phase is the fourth power of the nontrivial Jacobi coordinate. The older fourth moments are \(5/8,3/4,49/64,3/4\). The only cubic term paired with \(S\) that survives is \(\mathbb E[Z^3\mid S]=S/16\). The older fifth-rank standards have no cubic invariants, and the new fields are sign-symmetric conditionally.

Write \(\mathcal D=\sum a_i T_i\) and \(g=(2b+a_1,2\lambda+a_2,2\nu+a_3,a_4,a_5,a_6,a_7)\). With \(M_i=\mathbb E T_i^4\), direct expansion gives the numerator squared of the principal square-root transfer,
\[
 \mathbb E[(2\mathcal V+\mathcal D)^2\mathcal D^2]
 =16\sum_i v_i a_i^2+g_2a_2^2+\sum_i M_i g_i^2a_i^2
 +\sum_{i<j}v_iv_j(g_i^2a_j^2+g_j^2a_i^2+4g_i g_j a_i a_j).
\]
For the ideal principal product use \(d_\mu=\sum_i |a_i|r_i\), where \(r=(2,3\sqrt2,8,23/\sqrt2,4,4,8)\). The final three bounds follow from the ranks and the trace averages.

## Closed-slab replay

Use the split square-root product estimate and the centered \(L^2\) derivative bound from the previous round. The three input-scale derivatives are all multiplied by \(\rho\) and the seven principal coefficients are fixed. The rational projection for the slabs is
\[
 a=(0,0.0295,0.0287,0.0089,-0.00865,0.00727,0.00727).
\]
The interval check uses the residual norm at the rational midpoint and the derivative times the half width, and evaluates the pointwise and remainder bounds outward on the entire closed slab. The decreasing mesh widths near \(143/32\) follow the available margin. The input interval calculations are Arb192 certificates for exact formulas. The moment laws and transfer give the uniform limiting statement. The point check uses the alternative vector in the checker. [Checker](signed-compact-60-check.py) · [Replay](signed-compact-60-checks.jsonl)

The next positive test should fit a compact conditional projection at the actual threshold and certify a uniform strict margin. For matched depth, the priority is a family of positive trials that can carry a depth-dependent spectral weight rather than a single improved fixed-floor mark.
