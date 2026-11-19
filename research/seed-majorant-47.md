# Separating the Jacobi seed in the stationary majorant

The actual real stationary mark satisfies

\[
 |m_q(t)|=O_t(n^{-1/125000}),\qquad t\ge28,\qquad n=(q-1)/2.
\]

The constants are uniform on compact real intervals in this range. This holds through both primes and prime squares. The proof saves generic rank before estimating the binomial coefficients, by cancelling opposite convolution powers of the initial Jacobi field. It improves the threshold of the [unseparated rank majorant](astra-measure-47.md), using its product-weight repair. The argument gives real marked decay. A uniform cold complex section remains open.

## Mixed words with a distinguished rank-one seed

Let \(x=\sqrt n K e_0\), \(S=2x\), and \(s_q=2\sqrt{q/n}\). Retain the negative Mellin objects and lift averages from [the inertia calculation](iteration-parity.md). As in the [rank-square norm calculation](large-smoothing.md), a rank-\(r\) negative object has convolution dimension \(r\), and \(\mathcal A(M)\) has supremum at most \(r\). Here the cost of a finite negative representation is \(\sum |c|r\). The correcting column \(K e_i\) has rank-one cost at most \(\sqrt{q/n}/\sqrt n\).

Let \(L\) be the rank-one quadratic Kummer object for \(s(a)=\chi(1-a)\). At good full characters, its two lifts have dual Mellin traces by \(s(a^{-1})=\chi(a)s(a)\) and Mellin duality. Thus, up to the common sign of the perverse trace, \(S\) evaluates to \(s_q(L+L^\vee)/2\). The convolution dimension of \(L\) is one, so it is tensor-invertible. The \(k\)-th power of the two-lift average accordingly has summands in powers \(L^{\star(2i-k)}\), including the unit when \(2i=k\), with weights \(2^{-k}\binom{k}{i}\).

Consider \(S^k\) times \(j\) other negative fields of ranks \(r_1,\ldots,r_j\), with \(m=k+j\ge2\) even. After expanding the other lifts, a term with seed exponent \(2i-k\) uses only \(|2i-k|+j\) negative factors before applying \(K\). This number is even. Its middle convolution followed by the quadratic twist has rank at most \((|2i-k|+j)\prod r_i\), by the [generic convolution bound](large-smoothing.md#an-exact-bound-for-even-products), with rank zero in the purely punctual case. The generic rank cost for the output is at most

\[
 s_q^k\bigl(\mathbb E|W_k|+j\bigr)\prod_{i=1}^j r_i,
 \qquad \mathbb E|W_k|=2^{-k}\sum_{i=0}^k\binom{k}{i}|2i-k|.
 \tag{1}
\]

Here \(W_k\) is a length-\(k\) sum of independent fair signs, used to write the binomial weights. In the unseparated bound the factor in parentheses would be \(k+j\).

For the arithmetic error, select good full characters for the original inputs before cancelling powers. The relevant powers and duals are in the generated tensor category on this good set. On the exceptional characters the discrepancy has magnitude at most \(2s_q^k\prod r_i\), by the convolution dimension bound. There are at most \(O(k+\sum_i r_i)\) of them, including both lifts. Apply \(K\) to the discrepancy via the exact columns \(K e_i\). The output therefore has an exact finite negative representation with cost at most (1) plus

\[
 O\!\left(s_q^k (k+\textstyle\sum_i r_i)\prod_i r_i/\sqrt n\right).
 \tag{2}
\]

The absolute constant is uniform. This also treats terms whose generic part is purely punctual and killed by \(K\).

## An actual finite-degree approximation

Define real vector coefficients \(V_d\) by the exact formal rule

\[
 V(z)=zS+K\sqrt{4t+V(z)^2},\qquad V(0)=0 .
 \tag{3}
\]

At each positive degree the nonlinear term depends only on earlier coefficients. \(V_1=S\), and later coefficients are real coordinate polynomials with \(K\) applied.

For \(m\ge2\) even put

\[
 A_m(a,b)=\sum_{k=0}^m\binom m k a^k b^{m-k}
             \bigl(\mathbb E|W_k|+m-k\bigr),\qquad
 F_t(a,b)=2\sqrt t\sum_{\ell\ge1}
        |\tbinom{1/2}{\ell}|(4t)^{-\ell}A_{2\ell}(a,b).
\tag{4}
\]

Let \(D=\lfloor(\log_2 n)/3\rfloor\). Every individual representation term at degree \(d\le D\) has rank at most \(2^{d-1}\), by induction. Indeed for \(m\) input factors of degrees \(d_i\), the generic rank before cancellation is at most \(m\prod 2^{d_i-1}\le 2^{d-1}\), and the exceptional correction terms have rank one. In (2) the ratio of exceptional overhead to (1) is \(O(D2^D/\sqrt n)=o(1)\), uniformly through degree \(D\), since \(\mathbb E|W_k|+m-k\ge1\). Choose each exact representation recursively by (1)–(2). Summing the costs of the nonlinear coefficients is then bounded coefficientwise through degree \(D\) by the scalar series

\[
 B(z)=(1+\varepsilon_n)F_t(s_q z,B(z)),\qquad B(0)=0,
 \qquad \varepsilon_n=O(D2^D/\sqrt n)\ge0.
\tag{5}
\]

Each selected seed has degree one. All other occurrences use the previously constructed coefficients of degree at least two. Counting the seed positions gives the binomial factors in (4). No bound for all degrees at a fixed field is required.

Choose \(a=5657/2000\), \(b=33/20\), and \(\rho=50001/50000\). The [exact rational check](seed-majorant-47-check.py) gives \(F_{28}(a,b)<1.6493<b\), \((a+b)^2/(4\cdot28)<1/5\), and \(2\sqrt2\,\rho<a\). The nonconstant coefficient weights \(2\sqrt{t}(4t)^{-\ell}\) decrease with \(t\). Hence for all large \(q\), \(s_q\rho\le a\) and the positive iteration defining (5) at \(z=\rho\) stays in \([0,b]\). Its fixed-degree coefficients stabilize as formal iteration proceeds. It follows that

\[
 \sum_{d=1}^D \rho^d\|V_d\|_\infty\le a+b .
 \tag{6}
\]

Set \(V_D=\sum_{d\le D}V_d\), and let \(U_D\) be the value at \(z=1\) of the degree-\(D\) truncation of \(\sqrt{4t+(\sum_{d\le D}V_d z^d)^2}\). Equation (3) gives \(KU_D=V_D-S\) exactly. The weighted coefficient bound (6) places the binomial series within its convergence radius, with absolute coefficient sum weighted by \(\rho^d\) of order \(O_t(1)\). Hence

\[
 \|U_D-\sqrt{4t+V_D^2}\|_\infty=O_t(\rho^{-D}).
 \tag{7}
\]

This passage retains the exceptional values at every frequency.

## Identification with nearby actual stationary weights

Set \(u_0=2\), \(u_i=U_{D,i}/\sqrt n\) otherwise, and \(v=Ku\). The exact expression for \(KU_D\) gives

\[
 \sqrt n\,v=V_D-(U_D)_0 K e_0 .
\]

The largest entry of \(K e_0\) is \(O(n^{-1/2})\) in absolute value. Thus the scaled entries of \(v\) are uniformly bounded and their discrepancy from \(V_D\) is \(O_t(n^{-1/2})\). By (7), the two factors \(A_\pm=(u\pm v)/2\) are strictly positive at every site for large \(n\). They lie in the complementary Fourier spaces and have equal mean because \(v=Ku\). Thus they are exactly stationary for product weights \(w'=A_+A_-\), with \(w'_0=1+O_t(n^{-1})\) and

\[
 n w'_i=t+O_t(\rho^{-D}+n^{-1/2})\quad (i\ne0).
\]

Divide all weights by \(w'_0\) to put the marked weight at one. The marked logarithmic ratio is unchanged, and is \(O_t(n^{-1/2})\) there since \(u_0=2\) and \(v_0=O_t(n^{-1/2})\). The [square-root weight comparison](marked-response.md#weighted-complementary-projections) bounds its change to the actual constant bulk floor by \(O_t(\rho^{-D}+n^{-1/2})\). The claimed rate follows since \(\rho^{125000}>8\) and \(D=\lfloor(\log_2 n)/3\rfloor\). These arguments compare the actual marked scalars without giving a supremum bound on the actual bulk vector. Error constants can be chosen uniformly on compact floor intervals in \([28,\infty)\).

## A shorter square control for the real measure budget

In the [whole-half-plane Chebyshev stencil](astra-pick-46.md), take \(T=32\), \(a_{\rm cold}=1/2\), \(J=128\), and \(x_i=1-i/[5(J+1)]\). All its hot floors \(T\sqrt{x_i}\) exceed 28, as does the anchor. The exact square theta and real leverage give \(\liminf m_q(1/2)\ge\frac12\log(4/3)>0.14\). The budget is at most \(4(63/65)^{128}<0.074\). The fixed hot coefficients have vanishing marked contribution by the new theorem. Consequently the stencil violates the entire right-half-plane budget by more than \(0.06\) for every sufficiently large square. This is an asymptotic statement with no computed first square.

The [checker records](seed-majorant-47-checks.jsonl) concern scalar constants only. There is a limit to improving this particular estimate by changing radii. Its quadratic contribution is \((a^2+4ab+2b^2)/(4\sqrt t)\). For it to be smaller than \(b>0\) one needs

\[
 4(\sqrt t-a)>a^2/b+2b\ \ge\ 2\sqrt2\,a .
\]

Even with the limiting seed cost \(a=2\sqrt2\), this requires \(t>(2+2\sqrt2)^2\). Lower floors already require improving the quadratic mixed-product estimate or changing the construction. The majorant is field-general, and the square theta forces actual marked nondecay at every fixed floor below one.
