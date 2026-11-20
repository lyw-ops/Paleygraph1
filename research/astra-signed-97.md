# Signed exterior forcing after a square-root number of erasures

At the first boundary of the round-95 near-flat comparison, remove **any** bulk set \(S\) containing a first-hit site \(i\), with \(|S|\le\sqrt n/500\). Write \(O=(S\cup\{0\})^c\), \(H_j=\sinh(\gamma_j-g_j)\) for the hyperbolic displacement from the real height-100 predictor, and \(X=\sqrt{3B}\,J_w e_0\) for the actual midpoint column. For all sufficiently large eligible primes, at least one of the following holds.

* The original signed sum \(\operatorname{sgn}(X_i)\sum_{j\in O}R_{ij}H_jX_j\) exceeds \(5\cdot10^{-5}\).
* The counting norm \(\|(HX)_O\|_2\) exceeds \(7.05\cdot10^{-7} n^{1/4}\).

Unconditionally \(\|(HX)_O\|_2>6.843\cdot10^{-5}\), and \(\|(2\sinh((\gamma-g)/2))_O\|_2>0.650\). A single site of maximal physical imaginary difference retains a positive ordinary signed exterior after every such erasure containing that site. There an explicit Jacobi sum with the physical, uncentered input survives \(\lfloor\sqrt n/2\rfloor\) erasures. These necessary conditions use the actual first floor, including \(w_j=1-X_j^2/3\). The signed prime upper remains open. [First-floor construction and real transport](astra-count-96.md) · [All-source arithmetic bound](shifted-resolvent-96.md)

## A bounded multiplier on the physical imaginary row

Let \(R=MZM-D\), where \(D_j=\tanh g_j\), \(M_j=\operatorname{sech}g_j\), \(Z=(I-KD)^{-1}K\), and \(g\) is the real height-100 half log at the real part of the floor. Set
\[
 V_j=\cosh(\gamma_j)X_j,\qquad E_j=\tanh\gamma_j-D_j,\qquad
 m=\sqrt{1-0.514^2}.
\]
Throughout the bulk \(|X_j|\le t_*=10^{-4}\), with equality at a first hit. The real weight is \(1-X_j^2/3\), the complex product is one, and the two factors have opposite phases. Hence \(V_j\) is \(\sqrt3/2\) times their imaginary difference, up to the common ray sign. This physical row is independent of the reference. The real cap gives \(|D_j|<0.514,\ M_j>m,\ |E_j|<1.514\).

Write \(C_j=\cosh(\gamma_j-g_j)\) and \(\beta=C_0+H_0(J_w)_{00}\). The signed real transport at bulk site \(i\) is \(C_iX_i=\beta\sqrt{3B}R_{i0}+\sum_{j\ne0} R_{ij}H_jX_j\). The identities \(C_i+D_iH_i=M_i\cosh\gamma_i\) and \(M_jH_jX_j=E_jV_j\) give the exact bulk system
\[
 V_i=b_i+\sum_{j\ne0} Z_{ij}E_jV_j,\qquad
 b_i=\beta\sqrt{3B}\,Z_{i0}M_0.                                      \tag{1}
\]
The complete diagonal response is in this formula. The mark has already been removed from the sum. The R96 marked-source proof bounds \(\sqrt n\,|Z_{i0}|<89.158\) via the packet Neumann series on \(\sqrt n\,Ke_0\), before either \(M\) factor is inserted. Using \(\beta\le\exp(8\cdot10^{-12})\) and \(\sqrt{3B/n}\le\sqrt3\,2^{-17}/(2(2031/128-2^{-17})^{3/2})\) gives \(\|b\|_\infty<b_*<9.321\cdot10^{-6}\), where \(b_*\) is the product of these three upper bounds. The translated-source estimate gives \(\max_{ij}|Z_{ij}|<178/\sqrt n\) eventually. These bounds hold uniformly on the nominated square.

## Keep the specified first-hit site

Set \(L=Z_{SS}\operatorname{diag}(E_S)\), \(q=178(1.514)/500=0.538984\), and \(f^{\mathsf T}=e_i^{\mathsf T}(I-L)^{-1}\) on the individual sites of \(S\). The maximum absolute row sum of \(L\) is at most \(q\). Consequently \(\|f\|_1\le(1-q)^{-1}\), and (1) gives the signed test
\[
 \operatorname{sgn}(X_i) f^{\mathsf T} Z_{SO}(EV)_O
 \ge t_*-b_* /(1-q)>7.978\cdot10^{-5}.                               \tag{2}
\]
Here \(|V_i|\ge t_*\), irrespective of the real log at the hit or at any erased site. The set \(S\) may be chosen after observing the true row. More generally, (2) holds with \(178\sum_{j\in S}|E_j|/\sqrt n\) in place of \(q\) whenever this ratio is below one, retaining its actual right-hand side.

Each entry of \(f^{\mathsf T}-e_i^{\mathsf T}=f^{\mathsf T}L\) has magnitude at most \(178(1.514)/((1-q)\sqrt n)\). Therefore
\[
 \|f-e_i\|_2 <26.143\,n^{-1/4}.                                       \tag{3}
\]
Set \(F=R_{SO}(HX)_O\). Disjointness gives exactly \(Z_{SO}(EV)_O=M_S^{-1}F\). Since \(R\) contracts, \(\|F\|_2\le\|(HX)_O\|_2\). Thus (2) gives the lower \(m(t_*-b_* /(1-q))/(1+26.143 n^{-1/4})\) on the remaining source norm. At \(n\ge10^{30}\) it exceeds \(6.843\cdot10^{-5}\), once the translated estimate applies. The identity \(H_j^2=h_j^2+h_j^4/4\), \(h_j=2\sinh((\gamma_j-g_j)/2)\), and the first-floor cap give \(\|(HX)_O\|_2^2\le t_*^2(\|h_O\|_2^2+\|h_O\|_2^4/4)\), proving the stated \(0.650\). Taking absolute entries in (2) also gives
\[
 \|(HX)_O\|_1\ge\|(EV)_O\|_1
 >\frac{(1-q)t_*-b_*}{178}\sqrt n>2.066\cdot10^{-7}\sqrt n .          \tag{4}
\]

For the original row at the specified hit, suppose \(\operatorname{sgn}(X_i)F_i\le5\cdot10^{-5}\). Separate \(e_i\) from \(f\) in (2). Its direct term is at most \(5\cdot10^{-5}/m\), also when the signed term is negative. The remainder is at most \(26.143 n^{-1/4}\|(HX)_O\|_2/m\). This proves the alternative in the opening paragraph. Thus failure of the ordinary signed bound at a singleton costs a growing second norm even after the hit and the largest \(\lfloor\sqrt n/500\rfloor-1\) other sources have been deleted.

## One fixed physical site for all deletions

Choose \(k\) maximizing \(|V_k|\) on the bulk and write \(P=|V_k|\ge t_*\). This choice is made once for the floor and need not be a first-hit site. For every \(S\) containing \(k\) of the indicated size, the removed part of (1) has absolute value at most \(qP\). With \(O=(S\cup\{0\})^c\),
\[
 \operatorname{sgn}(X_k)\sum_{j\in O}R_{kj}H_jX_j
 \ge M_k((1-q)P-b_*)>3.155\cdot10^{-5}.                              \tag{5}
\]
Each aligned summand of the full sum in (1) costs at most \(178(1.514)P/\sqrt n\). There must be more than \(0.003364\sqrt n\) bulk indices with \(\operatorname{sgn}(X_k)Z_{kj}E_jV_j>0\), counting the one possible diagonal index. The estimate permits large individual real amplitudes because \(P\) is the maximum of the actual imaginary row.

A simultaneous signed test on the same \(V,k\) retains the individual Jacobi coefficients. Use zero reference diagonal in the exact transport, so \(Z=K\), \(M=I\), \(E_j=\tanh\gamma_j\). The mark pays at most \(\sqrt{3B}\,e^{|\gamma_0|}\sqrt p/n<1.480\cdot10^{-7}\), since \(|g_0|\le4.768/(2\sqrt n)\), \(|\gamma_0-g_0|<8\cdot10^{-12}\), and \(\sqrt{p/n}<1.415\) for \(n\ge10^{30}\). For every \(S'\) containing \(k\) with \(|S'|\le\sqrt n/2\),
\[
 \operatorname{sgn}(X_k)\sum_{j\notin S'\cup\{0\}}
       K_{kj}\sinh(\gamma_j)X_j
 \ge(1-1.415/2)P-1.480\cdot10^{-7}>2.910\cdot10^{-5}.                \tag{6}
\]
The full bare sum needs more than \(0.7056\sqrt n\) sign-aligned sites. Formula (6) uses the physical imaginary sum of the two factors, up to the same scalar and ray sign. Formula (5) uses their displacement relative to the height-100 predictor. The bare test holds at \(n\ge10^{30}\) without the eventual translated-column estimate.

## Signed Jacobi discrepancy on two actual superlevel sets

The weights in (6) can be removed from the arithmetic sum. There exist \(u,v\in[0,1]\), chosen once at the floor, such that the signed indicator
\[
 A_j=\operatorname{sgn}(X_k\gamma_j X_j)\,
       1_{\{|\tanh\gamma_j|>u,\ |V_j|>vP\}},\qquad j\ne0
\]
has \(\sum_{j\notin S'\cup\{0\}}K_{kj}A_j>0.2910\) **simultaneously for every** \(|S'|\le\sqrt n/2\). Indeed, integrating the full sum in \(u,v\) gives the untrimmed (6) divided by \(P\), which exceeds \(1-1.480\cdot10^{-7}/t_*\). Some single pair attains at least this average. Every later deletion then costs at most \(1.415/2\) since \(|A_j|\le1\). In particular the sign is retained at each of the two real-amplitude and physical-imaginary cuts.

At the same \(k\), possibly different levels produce
\[
 A'_j=\operatorname{sgn}(X_k E_j X_j)\,
       1_{\{|E_j|>1.514u,\ |V_j|>vP\}},\qquad j\ne0,
\]
with \(\sum_{j\notin S\cup\{0\}} Z_{kj} A'_j>0.2429\) simultaneously for every \(|S|\le\sqrt n/500\). Apply the same layer integral to (1), dividing the untrimmed sum by \(1.514P\), and deduct \(178/500\). Both statements allow the deleted set to be selected *after* seeing the cuts. An upper on the minimum signed sum over the permitted deletions, uniformly over the two real thresholds on the physical row, suffices. The indicators still depend on both the real amplitude and the imaginary row.

At \(p=173,\ T=2031/128,\ |y|=2^{-17}\), the certified physical unit-bulk row sets a tailored squared cutoff \(2.2479533444\ldots\cdot10^{-14}\). The phase maximum and imaginary-difference maximum at this floor both lie in orbit 16. With the bare Jacobi seed as a nontrivial trial diagonal, the union of the hit orbit and the six largest-source orbits consists of twelve individual sites. Erasing this union leaves a Schur-compensated exterior of \(1.25201520\ldots\cdot10^{-9}\) in \(Z\) units at the hit. The direct exterior is \(1.69666847\ldots\cdot10^{-9}\). The exact difference is resolved in 256-bit interval arithmetic. Integrating the two signed indicator cuts over all distinct pairs of levels gives \(0.0404449000\ldots\), agreeing with the normalized true bare-Jacobi sum within \(10^{-45}\). One untrimmed signed cut gives \(0.7867180002\ldots\). This finite replay tests the identities at the tailored floor. The large-prime margins above use the height-100 reference and \(\delta=10^{-8}\). [Arb checker](astra-signed-97-check.py) · [Two outward records](astra-signed-97-checks.jsonl)

1. Bound the ordinary signed exterior at the actual hit after deleting the largest sources, together with an \(o(n^{1/4})\) bound for the remaining counting second norm. The two estimates would contradict the first-floor alternative through sufficiently large primes.
2. Estimate the signed Jacobi discrepancy on the two physical superlevel cuts above, allowing a separate deletion for each pair of cuts. An upper at most \(0.2910\) on every minimized discrepancy at the physical maximum excludes the floor.
