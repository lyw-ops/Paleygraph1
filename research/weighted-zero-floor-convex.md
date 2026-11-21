# A convex test for the zero-floor cap defect

Use the real zero-floor capped equation in [the stationary-weighted excess note](weighted-zero-floor-spill.md), with the actual Paley reflection \(K\), \(M=10\), and \(p=2n+1\equiv1\pmod4\) prime. Write \(U_*=Ka_*\) for any zero-floor capped fixed point, with \(a_*=|C_M(U_*)|\) off the mark and \(a_{*,0}=\sqrt{4n+C_M(U_{*,0})^2}\). Put \(h_*=U_*-C_M(U_*)\), \(\mu_*=\mathbb E_n a_*\), and \(\alpha_0=4-\mu_*^2=\|h_*\|_{2,n}^2+2M\|h_*\|_{1,n}\). All means and norms use divisor \(n\). The mean and signed spill are independent of the choice of fixed point.

## Convex formulation

Consider the compact polytope

\[
 \mathcal A_p=\{a:a_0=2\sqrt n,\ \mathbb E_n a=2,\ 0\le a_i\le M\ (i\ne0)\},
\]

and the optimal residual

\[
 \delta_p=\min_{a\in\mathcal A_p}
 \left(\frac{(Ka)_0^2}{n}+\frac1n\sum_{i\ne0} (|(Ka)_i|-a_i)_+^2\right)^{1/2}.       \tag{1}
\]

The polytope contains the row with bulk constant \(b_n=2\sqrt n/(\sqrt n+1)\). To minimize the squared residual use one nonnegative variable \(d_i\) per bulk coordinate, subject to \(d_i\ge (Ka)_i-a_i\) and \(d_i\ge -(Ka)_i-a_i\). Thus (1) is a convex quadratic program with both signs and a fixed physical anchor.

For every trial \(a\in\mathcal A_p\), put \(u=Ka\) and \(d_i=(|u_i|-a_i)_+\) on the bulk, with \(d_0=0\). Write \(B=\sqrt{M^2+4}\), so \(\|U_*\|_{2,n}\le B\). Since \(K^2=I-J\), the exact cross identity is

\[
 2\mu_*=\mathbb E_n(aa_*-uU_*).
\]

At the mark the contribution is at least \(4-|u_0|\,|U_{*,0}|/n\). Off the mark, \(a_* = |U_*|-|h_*|\); positivity of \(a\) gives the lower bound \(-d_i|U_{*,i}|-M|h_{*,i}|\). Hence

\[
 4-2\mu_*\le B\bigl(|u_0|/\sqrt n+\|d\|_{2,n}\bigr)+M\|h_*\|_{1,n}.
\]

Subtract the last term using the exact defect identity. Minimizing over the trial yields

\[
 \boxed{(2-\mu_*)^2+\|h_*\|_{2,n}^2\le 2\sqrt2\,B\,\delta_p.}                     \tag{2}
\]

There is a converse bound \(\delta_p\le C_M(\sqrt{\alpha_0}+n^{-1/2})\). To construct the trial, replace \(a_{*,0}\) by \(2\sqrt n\) at cost at most \(M^2/(4n)\) in normalized second norm. The new mean \(\widehat\mu\) is at most \(2\). Push each bulk entry the same fraction of the way toward \(M\) to increase the mean to \(2\). The available mean increase is at least \(M(1-1/n)-2\ge3\). Thus the resulting trial \(a\) satisfies \(\|a-a_*\|_{2,n}=O_M(2-\mu_*+n^{-1})\). On the bulk the violation has norm at most \(\|h_*\|_{2,n}+2\|a-a_*\|_{2,n}\), by the contraction of \(K\) and the Lipschitz property of the positive part. The marked penalty in (1), before squaring, is at most \(M/\sqrt n+\|h_*\|_{2,n}+\|a-a_*\|_{2,n}\). Use \(\|h_*\|_{2,n}\le\sqrt{\alpha_0}\) and \(2-\mu_*=\alpha_0/(2+\mu_*)\).

It follows that \(\alpha_0(p)\to0\) through primes is equivalent to \(\delta_p\to0\). This reformulates the necessary zero-floor condition. The stronger assertion about the positive-floor stationary-weight tail still requires its own bound.

## Exact dual and the spread of a possible obstruction

For a real row \(x\) with \(\|x\|_{2,n}\le1\), let

\[
 D_p(x)=\frac{2(Kx)_0}{\sqrt n}
 +\min_{\substack{0\le b_i\le M\ (i\ne0)\\\sum_{i\ne0} b_i=2n-2\sqrt n}}
     \frac1n\sum_{i\ne0} b_i\big((Kx)_i-|x_i|\big).
\]

Then \(\delta_p=\max_{\|x\|_{2,n}\le1}D_p(x)\). In the inner minimum put weight \(M\) on the smallest bulk costs up to the prescribed mass, and any remaining fractional weight on the next smallest cost.

For the duality, each trial residual in (1) is the maximum over this unit ball of \(\mathbb E_n[xKa]-\mathbb E_n[1_{i\ne0}|x|a]\). The maximizing row at positive residual is the signed bulk violation together with the marked value \((Ka)_0\), all divided by the trial residual. For an optimal trial with positive residual, use this maximizing row \(x\). Along each segment to another feasible trial, the one-sided derivative of the square root in (1) is \(\mathbb E_n[(Kx-1_{i\ne0}|x|)\,\Delta a]\). A zero violation contributes zero derivative to the squared residual even at a kink. Optimality makes the derivative nonnegative, so this very trial minimizes the linear functional associated with \(x\). This proves attainment and equality. When the primal residual is zero, \(x=0\) attains equality.

The constant bulk trial in the inner minimum gives, using \(K\mathbf1=0\) and \(2-b_n/\sqrt n=b_n\),

\[
 D_p(x)\le b_n\left(\frac{(Kx)_0}{\sqrt n}-\mathbb E_n[1_{i\ne0}|x|]\right)
 \le b_n\left((\sqrt{p/n}-1)\mathbb E_n[1_{i\ne0}|x|]+\frac1n\right).       \tag{3}
\]

The last step uses the Jacobi entry bound, \(K_{00}=-1/n\), and \(|x_0|\le\sqrt n\). Therefore an order-one dual obstruction has order-one bulk first norm. In particular, bounded-second-norm rows supported on \(o(n)\) bulk sites have vanishing dual upper bound by Cauchy--Schwarz. The remaining prime-aspect test is the uniform upper on \(D_p(x)\) for bulk rows with nonvanishing first norm, or an explicit family of feasible trials with vanishing residual in (1).

## Finite checks

Floating-point quadratic minimization of the squared residual gave the following primal values and evaluated dual lower bounds. The dual row is the normalized signed residual of the returned trial, and its inner minimum is evaluated by sorting the bulk costs. The positive gaps are solver error at these inputs.

| \(p\) | Trial residual | Dual value |
| ---: | ---: | ---: |
| 13 | 0.259513024 | 0.259512763 |
| 101 | 0.136644833 | 0.136644267 |
| 401 | 0.016280294 | 0.016278734 |

The cross identity underlying (2) was also checked on eighteen feasible trials at the same primes, paired with depth-512 averaged zero-floor capped rows. The check includes the actual residual terms, using \(Ka'=U'+r\) and \(4-(\mathbb E_n a')^2=\|U'-C_M(U')\|_{2,n}^2+2M\|U'-C_M(U')\|_{1,n}+2\mathbb E_n(U'r)+\|r\|_{2,n}^2\). These finite diagnostics check signs and normalization.
