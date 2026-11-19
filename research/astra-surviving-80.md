# A polynomial deletion or a concentrated positive Schur price on the true terminal mask

Fix a supercritical gap on the larger prime face. At each of the good terminal times of [round 79](terminal-height-79.md), either order-depth opposite height survives deletion of polynomially more sites than the previous guarantee, or a small, explicit set of exterior heads carries most of a signed Schur interaction. Its size is controlled by every moment of the actual translated Jacobi columns. When the allowed Fourier correlation of the bounded excess test is small, the interaction starts from the same underestimation sites that carry the surviving terminal height. The Schur estimate below prices a head after summing its signed incident entries.

## Weighted translated Jacobi moments

Let \(G=\widehat Q\), \(n=(p-1)/2\), \(k(h)=\widehat{\chi(1-\cdot)|_Q}(h)/\sqrt p\). Thus \(|k|\le1\), \(k(0)=-1/\sqrt p\), and multiplying the circulant with entries \(k(j-i)\) by \(\sqrt p/n\) gives the cold involution \(K\) with \(K^2=I-J\). For any probability \(v\) on distinct sites in \(G\) define
\[
 W(j)=\sigma\sum_i v_i k(j-i),\qquad m=(\sum_i v_i^2)^{-1}.
\]
For all integers \(l\ge1\),
\[
 \mathbb E_j W(j)^2=\frac np(m^{-1}-n^{-1}),\qquad
 \mathbb E_j W(j)^{2l}\le(Cl/m)^l+Cl/\sqrt p.                 \tag{1}
\]
The first identity follows by applying \(K^2\) to \(v\).

For the second inequality replace the translates by independent \(\cos\theta_i\) for Haar angles. Each monomial in the expansion uses at most \(2l\) distinct translates, even when the whole support is much larger. At a nonexceptional full character each translate is the real part of a ratio of two normalized Gauss sums at the two quadratic lifts, up to the fixed unit Gauss factor. Different translates have disjoint pairs of twists. Expand each cosine into two powers and collect exponents for repeated translates. All-zero exponents give the same contribution in the finite-field and independent-angle models. Every other term has a nontrivial Gauss monomial with total absolute exponent at most \(4l\). Katz's bound for its average is \(O(l/\sqrt p)\) with an absolute constant. Omitting and reinserting the at most \(4l\) exceptional full characters of the monomial costs \(O(l/p)\) for \(l\ll\sqrt p\). Larger \(l\) are covered by the trivial bound. The absolute coefficients of the entire expansion sum to at most one. Averaging both lifts gives exactly the average on \(G\). For the independent angles the exponential moment is at most \(\exp(t^2/(2m))\), by the centered bounded-variable estimate on each coordinate. Integrating its Gaussian tail gives \((Cl/m)^l\). This proves (1) uniformly in the sites, weights, sign and prime, including choices made from the endpoint. The same arithmetic moment argument applies to eligible prime powers. [Two-lift calculation](fourier.md#joint-distribution-on-the-even-modes) · [Katz, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf#page=84)

## Where a large collision gets its signed price

Let \(q\) be a feasible probability on side \(\sigma\). Take a common deletion \(A\), \(E=G\setminus A\), \(x_i=(q_i-B/n)_+\), \(z=q-x\), and \(M=\sum_E x_j>0\). For a set of charged rows \(S\) put
\[
 M_S=\sum_S q_i,\quad L=n\sum_S q_i^2,\quad v_i=q_i\mathbf1_S/M_S,
 \quad \rho=\frac{L}{\sqrt n M_S M}.
\]
Use \(L>0\). The identity \(\rho^2m=L/M^2\) is exact. For \(T\subseteq E\), let
\[
 \Pi(T)=-n\sum_{j\in T}x_j\sum_{i\in S,\ i\ne j}q_i K^A_{ij},
\]
where \(K^A_{ij}\) is the forbidden-projector Schur row with \(A\setminus\{i\}\) eliminated and diagonal retained. Suppose along a sequence
\[
 L\gg1,\qquad B=o(L),\qquad
 |A|\le c\sqrt n,\qquad (1+|A|)/\sqrt n=o(\rho).
                                                                    \tag{2}
\]
For the applications below one may always take \(A=\{0\}\): then the last condition follows from \(L\to\infty\) and \(M_S,M\le1\). Define the explicit head set
\[
                     T=\{j\in E:W(j)>\rho/8\}. 
\]
Uniformly under (2), eventually
\[
 \sum_{j\in E\setminus T}\Pi(\{j\})_+\le L/8,\quad
 \Pi(T)\ge L/3,\quad \sum_{j\in T}x_j\ge c\rho M,               \tag{3}
\]
and
\[
 \frac{|T|}{n}\le \min\!\left(1,\frac{C M^2}{L},\;
       (Cl M^2/L)^l+\frac{Cl}{\sqrt p}(8/\rho)^{2l}\right)
                       \qquad(l\ge1).                            \tag{4}
\]
These bounds involve the positive clipped mass on actual exterior heads. On the exposed face, for any opposite optimizer \(r^*\) all paying exterior heads other than the root have \(r^*_j=0\) by complementarity. One can intersect \(T\) with this zero set when \(0\in A\).

To prove this, the [retained-diagonal estimates](astra-schur-77.md) give \(K^Aq=0\), diagonal \(1/2+O(n^{-1/2})\) and bounded operator norm. The off-diagonal part restricted to exterior columns has bounded norm too, as \(K^A\) on \(A^c\) is an orthogonal projection there and its remaining rows have bounded norm as a single operator by the Frobenius correction argument. Separate the full diagonal \(q_i\), and write each remaining exterior coordinate as \(x_j+z_j\). Since \(n\|z\|_2^2\le B\), this gives \(\Pi(E)=(1/2+O(n^{-1/2}))L+O(\sqrt{BL})\).

For a surviving off-diagonal, the original coefficient is \((-1-\sigma\sqrt p\,k(j-i))/(2n)\). Schur recomputation changes it by \(O(|A|/n)\) by diagonally dominant elimination. For every exterior head,
\[
 \Pi(\{j\})=\frac{\sqrt p}{2}M_S x_j
        \left[W(j)+O\!\left(\frac{1+|A|}{\sqrt n}\right)\right].
                                                                    \tag{5}
\]
Here reinserting the surrogate diagonal within \(W\) costs at most \(1/\sqrt p\) because \(k(0)=-1/\sqrt p\). The true Schur diagonal was already separated. On \(E\setminus T\) bound the positive part of (5) and sum to get at most \((\sqrt{p/n}/16+o(1))L<L/8\). Equations (2) and (5), with \(|W|\le1\), prove the other two assertions of (3). Apply Markov to each moment in (1) and use \(\rho^2 m=L/M^2\) to obtain (4). This argument does not bound the sum of the positive parts of individual pairs at one head.

## Polynomial deletion on the actual weighted terminal height

Fix \(0<\delta\le1\). Use the times \(a,b\), length \(d=b-a+1\asymp D(p)\), true primary pin of opposite sign, deficit \(r\), true companion terminal row \(Z=Z_{\sigma,b}\), density band \(I\), allowance, \(B=o(d)\), and tower parameter \(H\) of [the finite terminal theorem](terminal-height-79.md). Choose \(A=\{0\}\) and define \(M\) as above. Take \(\sqrt n q_0\ge1+\delta\). For each **fixed** integer \(l\ge2\) set \(a_l=1/(8l)\). Split \(I\) by the inequality
\[
               q_i\le M p^{-a_l}/\sqrt n                         \tag{6}
\]
into a low and a high part. The following alternative holds at each good terminal time and for every such prime row eventually.

* On the low part, after **every** deletion of at most \(p^{2a_l}H^2/M^2\) sites, the deficit price is \(\gg_\delta1\), the true terminal height price is \(\gg_\delta d\), and the collision is \(\gg_\delta d\).
* After every deletion of the original size \(H^2/M^2\), its high part has those same three lower bounds. For that surviving high row set \(S\), (3) holds and the set of paying heads has counting fraction at most \(C_{l,\delta}(d^{-l}+p^{-1/4})\).

Indeed choose the first conclusion if the initial low deficit price is at least a sufficiently small fixed \(c_\delta\), chosen below half the uniform lower bound after the original deletions. On a low deleted set \(F\) of the enlarged size, \(\sqrt n\|q\mathbf1_F\|_2\le H\) and \(\sum_F q_i\le p^{a_l}H^2/(M\sqrt n)\) when \(F\) contains just low sites. The terminal proof gives \(n^{1/4}M/H\to\infty\). Its bounded finite-prefix approximants for the three terms of the terminal envelope have sup norm \(O(1+\log\log p)\) and normalized second error \(o(1/H)\). The sup bound uses the terminal tower margin explicitly: with \(\Lambda=\log_2^*p\) the resource tower through the last required input has height at most \((1-\xi)\Lambda+O(1)\le\Lambda-3\). In the notation of [the tower comparison](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon), its value is at most \(T_{\Lambda-3}\le\log_2\log_2p\). Thus the deleted deficit price tends to zero, since \(a_l<1/4\) and \(H\le\log_2\log_2 p\) eventually. Apply \(Z\ge(2d-1)r\) on the deficit and \(\|r\|_{2,n}\ll d^{-1/2}\) for the other two costs. If the initial low price is smaller than \(c_\delta\), the earlier deletion theorem leaves a fixed high price for every original deletion. On those rows \(\rho\ge p^{-a_l}\), because \(\rho\) is the \(q\)-weighted mean of \(\sqrt n q_i/M\). Now (4) gives the displayed power bounds. A larger common Schur set satisfying (2) can be used if its associated \(M\) and bands are used throughout.

### A second allowed correlation with no exceptional approximation set

For the actual high rows \(S\) take the nonnegative test
\[
                       F_S(j)=(W(j)/\rho)^{2l}.
\]
It is an exact polynomial of translated Jacobi columns selected by the genuine row. In particular its construction uses \(S\) and \(q\). For this same row one necessarily has
\[
       C_q(F_S)=\sum_j q_j F_S(j)-\mathbb E_j F_S(j)
           \ \ge\ c_l M
                                                               \tag{7}
\]
eventually. Here \(C_q\) equals the nonconstant allowed Fourier pairing with the conventions below. In fact (5) and the full signed price imply \(M^{-1}\sum_E x_j W(j)=(\sqrt{n/p}+o(1))\rho\). Jensen with the exterior clipped probability \(x\mathbf1_E/M\) gives \(\sum q_j F_S(j)\ge M(1/2)^{2l}\) eventually. By (1) the counting mean is
\[
 \mathbb E F_S\le(ClM^2/L)^l+Cl \rho^{-2l}/\sqrt p=o(M).
\]
The first term is \(o(M)\) by \(M\le1\) and \(L\to\infty\); the second is \(O_l(p^{-1/4})=o(M)\) by (6)'s high-side reverse inequality and the trimmed-mass lower bound. The quotient of the true weighted mean by the counting mean consequently diverges uniformly at this fixed moment. The same statement follows more generally under \(M\rho^{2l}\sqrt p\to\infty\) in place of the power threshold. The unscaled test \(W^{2l}\) is bounded by one and has required correlation \(\gg_l M\rho^{2l}\). Thus even if the original fixed window test has small correlation, charging the high-density part of its underestimate set forces a positive allowed correlation with a second, adaptive, exact test.

One can extract a single bounded test with **exactly \(h=2l\) distinct surviving row sites**, using no coefficients of \(q\) in the test once its centers have been chosen. Write \(a_i(j)=\sigma k(j-i)\) and set
\[
 D_h(j)=\sum_{i_1,\ldots,i_h\ \mathrm{distinct}}
                 \prod_{b=1}^h v_{i_b}a_{i_b}(j).
\]
Partition-lattice inclusion–exclusion writes \(D_h-W^h\) as a sum indexed by partitions with a block of size at least two. A singleton block contributes \(W\), and a block of size \(u\ge2\) has absolute contribution at most \(\sum_i v_i^u\le m^{-u/2}\). Summing the fixed Möbius coefficients gives
\[
 |D_h-W^h|\le C_h\sum_{b=2}^h m^{-b/2}|W|^{h-b}.
\]
By Hölder the error in its \(q\)-mean, relative to \(\mathbb E_q|W|^h\), is bounded by \(C_h\sum_{b=2}^h (m^{-1/2}/\|W\|_{L^h(q)})^b\). The Jensen estimate above gives \(\|W\|_{L^h(q)}\ge M^{1/h}\rho/2\); the ratio is at most \(2M^{1-1/h}/\sqrt L=o(1)\). Thus the true \(q\)-mean of \(D_h\) is at least \(c_l M\rho^{2l}\). Every distinct product individually has counting mean \(O_l(p^{-1/2})\): in every cosine expansion term all its distinct twist pairs have nonzero exponent, so Katz's nontrivial bound applies. The total coefficient mass in \(D_h\) is at most one. Since \(M\rho^{2l}\sqrt p\to\infty\), one ordered tuple therefore satisfies
\[
 C_q\!\left(\prod_{b=1}^{2l}k(\cdot-i_b)\right)
          \ge c'_l M\rho^{2l}\gg_l p^{-1/2},\qquad
             i_1,\ldots,i_{2l}\in S\text{ distinct}.             \tag{8}
\]
In fact the ratio of its lower bound to \(p^{-1/2}\) tends to infinity. This holds for some tuple after each stipulated deletion. In the small-correlation branch its centers all lie in the actual underestimate set with the high-density and terminal-height constraints. The independent-angle comparison of (1) only uses balanced boundary exponents for the constant term; pairwise disjoint quadratic lifts make each nonzero exponent vector nontrivial in the Gauss moment theorem.

### The small allowed-correlation branch

For completeness the [bounded excess construction](astra-excess-79.md#allowed-fourier-correlation-or-concentrated-approximation-failure) applies to this terminal primary window. Put \(u=\delta/8\), \(P=(r-u)_+\) on the bulk, \(e=(H+D)^{-4}\), and take the same positive bounded polynomial approximation \(f\) with
\[
 \|P-f\|_{2,n,\mathrm{bulk}}\le\tau=C D(e+p^{-3/8}),\qquad
 \bar f\ll 1/d,qquad 0\le f\ll1+\log\log p.
\]
Indeed the terminal primary coefficients have bounded absolute sum, its pin increment and constant are bounded, and the three terminal terms are within the same finite horizon. The positive-part and final excess approximations take place after the bulk fields have been approximated; the Jacobi term of the pin extends to the full group with its diagonal delta omitted. The mean estimate follows from \(P\le r\), the first norm of \(r\), and the one bounded root coordinate. This constructs a fixed test for a chosen terminal profile and horizon, independently of the tested row.

Let \(E_f=\{i\ne0:r(i)>2u,\ f(i)<P_i/2\}\). Then \(|E_f|/n\le4\tau^2/u^2\) and \(P\le2|P-f|\) there. With unnormalized Fourier transforms on \(G\), the allowed correlation is
\[
 C_q(f)=n^{-1}\operatorname{Re}\sum_{t\in D_\sigma}
           \widehat q(t)\overline{\widehat f(t)}.
\]
If \(C_q(f)<\delta/16\), positivity and the Fourier equations give \(\sum q_i f(i)\le\delta/12\) eventually. The total bulk deficit price is at least \(7\delta/8-o(1)\) from the pin allowance. Discard the low-density band at cost at most \(\delta/8\) by choosing its fixed cutoff small, and the upper cap at cost \(o(1)\). Passing directly to \(P\mathbf1_{r>2u}\) costs at most \(2u\), since \(0\le r-P\mathbf1_{r>2u}\le2u\) everywhere. Outside \(E_f\) the remaining price is at most \(2\sum q_i f(i)\). Thus \(\sum_{I\cap E_f}q_iP_i\gg_\delta1\). In this calculation there is no separate charge for cutting \(r\le u\).

Split \(I\cap E_f\) by (6). In the low alternative, after **any** deletion of at most
\[
                      c_\delta p^{2a_l}\tau^{-2}/M^2
\]
sites the remaining low part has \(P\)-price \(\gg_\delta1\), true terminal height price \(\gg_\delta d\), and collision \(\gg_\delta\tau^{-2}\). In the high alternative these three prices survive every deletion of at most \(c_\delta\tau^{-2}/M^2\) sites on the original band. The resulting high row set \(S\) forces (3) on exterior heads in a set of counting fraction
\[
                       C_{l,\delta}(\tau^{2l}+p^{-1/4}).
\]
For both assertions, deleting \(N\) sites where \(q_i\le Q\) inside \(E_f\) costs at most \(2\tau\sqrt{nN}\,Q\) in \(P\)-price. Use (6) on the low side, and the terminal band cap \(2C_0 M/\sqrt n\) on the high side. Choose \(c_\delta\) small in both bounds and split as for the full mask. Cauchy–Schwarz on the surviving \(P\)-price gives its collision via the same \(2\tau\) error. The height bound follows from \(Z\ge(2d-1)r\), and (4) from \(\rho\ge p^{-a_l}\). In particular the low alternative requires polynomially many surviving high-height sites even if the correlation is small. In the other alternative both the original underestimation set and the exterior Schur head set are specified from the true data.

## Four interval checks and the remaining estimate

The [Arb384 checker](astra-surviving-80-check.py) uses terminal windows starting at time one, with the smallest nonnegative zero-allowance pin. It uses all positive larger-face sites where the opposite deficit exceeds \(0.01\), \(B=1\), \(A=\{0\}\) and the exact Schur coefficients. The finite low-part error matters at these cuts. The checker verifies the terminal threshold, opposite support zeros, Schur diagonal identity exact second moment of \(W\), and the nonconstant allowed Fourier pairing for the quartic power and a distinct-site quartic product in each field. These finite tests have positive mass on the signed-bias heads; they do not instantiate the growing-depth hypotheses. [Outward intervals](astra-surviving-80-checks.jsonl)

| Prime | Terminal time | Charged rows | Bias heads / with positive clipped mass | Exterior clipped mass fraction there | Positive outside price divided by collision |
|---:|---:|---:|---:|---:|---:|
| 101 | 4 | 13 | 13 / 5 | 0.36989 | 0.14815 |
| 257 | 5 | 22 | 26 / 18 | 0.67839 | 0.05458 |
| 409 | 6 | 42 | 50 / 28 | 0.63081 | 0.06999 |
| 769 | 7 | 74 | 104 / 58 | 0.62728 | 0.06429 |

For the distinct quartic tests, the certified nonconstant allowed correlations exceed \(0.18041,0.12802,0.09608,0.07028\) respectively. The four tuples, their counting means and the adaptive quartic correlations are retained in the outward records. Repeating the checker reproduced all four records byte for byte.

The moment error in (4) is amplified by \(\rho^{-2l}\). Using a fixed moment with no density split loses the arithmetic bound at polynomially small \(\rho\). A small counting fraction also allows a large clipped mass of a feasible endpoint. On the low branch, deleting polynomially many sites still leaves an uncontrolled sum over the others. No unrestricted \(o(d)\) upper on the surviving height has been established.

1. Price the explicit Schur heads on the actual exposed support. For any mixture \(w\) of translates of opposite feasible probabilities, \(n\sum_jq_jw_j=1\). If \(n w\ge t>0\) on the exposed exterior heads, then \(\sum_T x_j\le(1-nq_0w_0)/t\) with \(0\in A\). A bound below the mandatory \(c\rho M\) excludes the high branch. Another sufficient upper is \(C_q(F_S)=o(M)\) for the exact Jacobi power (7), or a uniform \(O_l(p^{-1/2})\) allowed correlation for the bounded distinct-site products in (8). Positive correlation still requires pricing the full terminal mask.
2. On the low branch test the height after the enlarged deletion of the largest actual prices. A uniform \(o(d)\) upper on the remaining low sites, together with exclusion of the high branch for one genuine larger optimizer, excludes a fixed gap. Test the stronger underestimate deletion when the bounded test has small allowed correlation.
