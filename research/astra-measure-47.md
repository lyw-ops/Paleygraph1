# A stationary hot regime below 40 and a signed test at two cold floors

For each fixed real \(t\ge40\), the physical stationary mark is \(O_t(n^{-1/500})\) through all eligible primes and through prime squares. Convergence is uniform on compact subsets of this range. Below it, one genuinely sign-changing three-node stencil, with floors 1, 3 and 41, satisfies the whole-half-plane measure budget with a limiting margin above 0.075 in both families. A different explicit stencil with 135 hot interpolation nodes and one cold node violates the same budget on all sufficiently large squares. These results leave the general prime stencil inequalities and ETH26 open.

## Finite trace polynomials and actual complementary factors

Use the Fourier involution on mean-zero coordinates \(K\), its constant kernel, \(n=(q-1)/2\), and the real field \(x=\sqrt n K e_0\). For a finite representation of a vector by negative Mellin fields define its cost to be the sum of absolute coefficients times generic ranks. This bounds the supremum norm. The [even-product rank and exception bounds](large-smoothing.md) imply the following rule. For a fixed finite expression consisting of an even number \(k\) of negative input factors of ranks \(r_j\), the exact output after multiplying pointwise and applying \(K\) has a finite negative-field representation of cost
\[
 k\prod_j r_j+O_{k,r_1,\ldots,r_k}(n^{-1/2})
\]
as an upper bound. Indeed average over the quadratic lifts. The middle-convolution twist has rank at most \(k\prod r_j\) for each lift, and \(K\) kills the punctual part. The discrepancy has bounded entries on a bounded number of exceptional characters before applying \(K\). Each \(K\delta_h\) has a rank-one representation of cost at most \(\sqrt{q/n}/\sqrt n\). Retain these exceptional terms in the exact representation. The number and ranks of terms stay bounded for each fixed expression, even if the character labels depend on the field. The starting vector \(x\) has cost at most \(\sqrt{q/n}\). These are applications of the cited arithmetic bounds, including their square-field scope.

Define actual real vector coefficients by the formal identity
\[
 H(z)= z x/\sqrt t+K\sqrt{1+H(z)^2},\qquad H(0)=0 .
\]
At any positive degree the square-root term needs only lower coefficients, and \(K1=0\). All operations at fixed degree are finite. Write \(H_d=[z^d]H\). With \(a=\sqrt{2/t}\), let the scalar majorant be
\[
 B(h)=\sum_{j\ge1}2j|\tbinom{1/2}j|h^{2j}=h^2/\sqrt{1-h^2},
 \qquad y=az+B(y),\quad y(0)=0.
\]
By induction each \(H_d\) has an exact representation of bounded complexity at fixed \(d\) with cost of field limsup at most \([z^d]y\). In the induction expand the ordered products of lower coefficients and use the even-product rule before summing. The bounded-complexity exception costs vanish at fixed degree. This order of limits permits one power of the output rank in the majorant. An estimate uniform in the word degree at each finite field does not follow.

At \(h=2/5,\ \rho=201/200\) one has \(\rho/\sqrt{20}+B(h)<h\). Positive-coefficient iteration of the scalar equation at \(z=\rho\) therefore gives \(\sum [z^d]y\,\rho^d\le h\) for \(t\ge40\). More generally the proof works for every
\[
 t>t_*:=2\left(\max_{0<h<1}\{h-h^2/\sqrt{1-h^2}\}\right)^{-2},
 \qquad 39.25<t_*<39.26 .
\]
Indeed choose a positive maximizing margin and then \(\rho>1\) sufficiently near 1. The explicit constants below use \(t\ge40\).

For fixed \(D\ge1\) write \(H^{[D]}=\sum_{d=1}^D H_d z^d\), and \(U^{[D]}=[\sqrt{1+(H^{[D]})^2}]_{\le D}\), a vector polynomial. Evaluate both at 1 to get \(H_D,U_D\). Exactly \(KU_D=H_D-x/\sqrt t\). In field limsup the weighted sum of coefficient sup norms of \(H^{[D]}\), with weights \(\rho^d\), is at most \(h\). Eventually it is at most \(1/2\) for each fixed \(D\). By the absolutely convergent scalar binomial series, the weighted sum of coefficient sup norms of the full square root is then at most \(2-\sqrt{1-1/4}<2\), giving
\[
 \|U_D-\sqrt{1+H_D^2}\|_\infty\le 2\rho^{-D}.
\]
Here the square root is the positive real one. The vectors themselves are real by their exact coordinate recurrence.

Set \(u_0=2\), \(u_i=2\sqrt{t/n}\,U_{D,i}\) off the mark, \(v=Ku\). Exactly
\[
 v/(2\sqrt{t/n})=H_D-U_{D,0}Ke_0 .
\]
Thus \(v_0=O_t(n^{-1/2})\) and the scaled bulk is within \(O_t(n^{-1/2})\) of \(H_D\). At sufficiently large fixed \(D\) and then sufficiently large fields, \(A_\pm=(u\pm v)/2\) are positive. They belong to the respective complementary Fourier spaces and have the same mean. As a result they are exactly the stationary rows in product normalization for weights \(w'_i=A_{+,i}A_{-,i}\): after dividing each by its mean, the opposite row supplies the log objective's first-order equations and strict concavity gives uniqueness. In particular
\[
 w'_0=1+O_t(n^{-1}),\qquad
 w'_i=(t/n)(1+O(\rho^{-D})+O_t(n^{-1/2}))\quad(i\ne0).
\]
At those weights the mark is \(\frac12\log(A_{+,0}/A_{-,0})=O_t(n^{-1/2})\). Divide all weights by \(w'_0\), preserving the mark. The [marked square-root weight stability bound](marked-response.md) now compares to the required weights with mark 1 and constant bulk \(t/n\), at cost \(O_t(\rho^{-D}+n^{-1/2})\). Constants can be chosen independently of \(D\) once its fixed-degree field threshold has been met. First take field limsup, then \(D\to\infty\). The real leverage Lipschitz bound gives uniform convergence on compact floor intervals. This construction certifies scalar decay without a uniform pointwise bound on the actual stationary bulk.

## A quantitative truncation through logarithmic degree

Every negative object occurring in the exact representation of degree \(d\) has rank at most \(2^{d-1}\). The seed has rank one. At an internal product of arity \(k\ge2\) and input degrees adding to \(d\), its twisted main outputs have rank at most \(k\,2^{d-k}\le2^{d-1}\), and the exceptional translated columns have rank one. Large complexity at fixed degree does not affect this bound on the individual ranks.

Take \(D=\lfloor(\log_2 n)/3\rfloor\). The explicit exceptional cost in the [even-product proof](large-smoothing.md) is at most
\[
 (8\sqrt{q/n}/\sqrt n)(\textstyle\sum_j r_j)\prod_j r_j.
\]
At all degrees through \(D\), the full rank cost of one product is consequently at most \((1+8\sqrt3\,n^{-1/6})k\prod_j r_j\). Summing the absolute coefficients of each expansion charges this **relative** factor only where a product is applied. The finite-field cost coefficients through degree \(D\) are therefore majorized by the corresponding coefficients of
\[
 y_n=\sqrt{q/(nt)}\,z+(1+8\sqrt3\,n^{-1/6})B(y_n).
\]
For \(t\ge40,\ n\ge2^{90}\), the displayed explicit \(h,\rho\) satisfy \(\rho\sqrt{q/(nt)}+(1+8\sqrt3\,n^{-1/6})B(h)<h\). The same polynomial and complementary-weight proof applies with this simultaneous \(D\). Its error is \(O_t(\rho^{-D}+n^{-1/2})=O_t(n^{-1/500})\), since \(\rho^{500}>8\). Positivity of the approximate rows is required only for sufficiently large \(n\). Constants are uniform on compact subsets of \([40,\infty)\). For fixed \(t>t_*\), choose its own \(h,\rho\) with strict slack and obtain a positive exponent depending on that floor.

## A sign-changing cold test of the precise boundary measure

Use [the half-plane boundary measure and kernels](astra-pick-46.md) with anchor \(T=41\), nodes \(x=(1/T)^2,\ y=(3/T)^2\), and \(k=7/5\). The tested functional is
\[
 m_q(1)-k m_q(3)+(k-1)m_q(41).
\]
The reciprocal Jacobi variational estimate (5) of [round 41](astra-branch-41.md) bounds its absolute field limsup by \(E(1)+kE(3)<0.319\), where \(E(t)=\log(\sqrt2[1+(1-8/\pi^2)t]/\sqrt{1+t})\). This uses the new hot result at the anchor.

The combined kernel \(K_x-kK_y\) is negative at zero and positive near infinity. Its limiting budget is strictly greater than 0.395. To bound it from below, pair with the bounded function \(b(s)=(s-r)/(s+r)\), \(r=(4/T)^2\). Partial fractions give
\[
 bK_x=A_x K_x+B_x K_r,\qquad
 A_x=(x+r)/(x-r),\quad B_x=-2r(x-1)/[(x-r)(r-1)] .
\]
Use the same formula for \(y\). Since \(\int K_x d\nu=\log[(1+T\sqrt x)/(1+T)]\), half the absolute integral against \(b\) is greater than 0.395. Dominated convergence passes the finite-field budgets to this limit. Hence the limsup of the actual excess is below \(-0.075\). Both the strict margin and the sign change persist under small perturbations of all three floors and \(k\). The ordinary real leverage bound alone pays \(\frac12\log 2+\frac{k-1}2\log(42/4)>0.816\) for this functional, while the measure budget is strictly smaller than that leverage cost by cancellation of opposite kernel contributions. The calculation proves one open family of signed tests; it gives no physical marked extension on the entire right half-plane.

## Square obstruction and ranked next tests

For a shorter square obstruction use \(T=41,\ a=2/3,\ J=135\) and \(x_i=1-i/[64(J+1)]\) in the [Chebyshev stencil](astra-pick-46.md). Every node \(T\sqrt{x_i}\) and the anchor belong to the hot regime. The exact square theta and real leverage give \(\liminf m_q(a)\ge\tfrac12\log(2/(1+a))\). All coefficients are field independent. Thus the liminf excess of the absolute functional over its exact measure budget is at least
\[
 \tfrac12\log(2/(1+a))-
 \log((1+T)/(1+a))\,[(T-a)/(T+a)]^{135}>0.05.
\]
This is eventual in the square order; no first square or numerical stationary solve is asserted. The rational nodes refer to the half-plane variable. The fixed large coefficients can be ill-conditioned.

1. For a genuinely cold prime estimate, try the same 135-hot-node stencil (or shorter local-disk stencils with rational dual weights). Its prime excess has to be controlled with field order first. Positive limiting excess along a prime subsequence refutes the proposed whole-half-plane stencil inequality; the displayed square excess refutes a field-independent version.
2. Improve the rank majorant by exploiting the actual signed even products before applying triangle bounds. At a new proposed floor, build complementary factors with a vanishing bulk relative product error and bounded scaled mark; a fixed positive lower bound for the infimum of that error over the proposed trial class refutes that class. The square bracket excludes any class meeting these conditions at a fixed floor below 1 simultaneously in both families.

The [checker](astra-measure-47-check.py) replays analytic constants and a finite exact coefficient recurrence. Its [records](astra-measure-47-checks.jsonl) contain no measurements of stationary solutions or computed field limits.
