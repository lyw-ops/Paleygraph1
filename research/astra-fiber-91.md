# Full third-coordinate price and a cost for transporting the two centered optima

On the actual affine matches, one can select an arbitrary union of third-coordinate cosets *after* drawing the short primes. Its signed first price equals the full third-coordinate price times the selected fraction, up to vanishing error simultaneously over all unions for subgroup index up to a growing scale. A displaced atom imposes a further constraint after subtracting the entire signed price separately in every coset. Every coupling of the centered endpoint populations must then pay for a change in their values or in the corresponding character phases. The phase origins and orientations may be fitted separately in every coset.

## Total variation on the third quotient

Let \(Q=(\mathbb F_p^\times)^2\), \(n=(p-1)/2\), \(G=\widehat Q\) additively indexed, \(p\equiv1\bmod4\) prime. Let \(F(x)=\sum_iq_i i(x)\), \(R(y)=\sum_i r_i i(y)\) for actual plus and minus optimal probabilities at zero, \(a=q_0,\ b=r_0\), \(nab=1\), \(a,b\ll p^{-1/2}\). Use \(q^e_i=(q_i+q_{-i})/2\) and similarly for \(r\). For independent uniform rational primes \(u,v\le(\log p)^A\), \(A>6\), impose the strict matches
\[
 x=u^2z\in D_+,\qquad y=v^2(z+1)\in D_-,\qquad w=z+2\in Q .
\]
Fix a subgroup of \(Q\) of index \(d\) before the draw. Let \(C\) run through its cosets. In an additive cyclic interval \(I\), write \(M_C(I)\) for these matches with \(w\in C\), \(\alpha=|I|/p\), \(E_A=(1+\log p)(\log p)^{1/2-A/4}\). For a two-variable test \(V=\sum_{h,k}v_{hk}h(x)k(y)\), put \(B=\sum|v_{hk}|\) and
\[
 H_C(V)=p^{-1/2}\sum_{M_C(I)} [\Re R(y)-\Re F(x)]V(x,y),\qquad
 L(V)=\sum_k v_{0k}r^e_{-k}-\sum_h v_{h0}q^e_{-h}.
\]
Then
\[
 \mathbb E_{u,v}\sup_I\sum_C\left|H_C(V)-{\alpha n\over8d\sqrt p}L(V)\right|
 \ll_A B\sqrt d\,E_A.                                                     \tag{1}
\]
The two marginal statements hold separately. For complex endpoint scores \(F,R\) in place of their real parts the same estimate uses the original \(q,r\) in \(L\). The coefficients of the test may depend on the optimizers. The bound also permits phases adapted to the probes under a predetermined absolute coefficient envelope, with \(L(V)\) computed for the chosen phases. For the full interval omit \(1+\log p\).

Here is the additional short-prime estimate needed to sum *absolute* errors across all cells. Write \(\mathcal P\) for the \(M\) primes up to \(L=(\log p)^A\), and \(s=\lfloor \log(p/3)/\log L\rfloor\). For any probability \(m_i\ll p^{-1/2}\), complex \(|b_i|\le1\), and either exponent sign,
\[
 \left(\mathbb E_{\ell\in\mathcal P}\left|\sum_i m_i b_i i(\ell^{\pm2})\right|^2\right)^{1/2}
 \le {(n\|m\|_\infty s!)^{1/(2s)}\over\sqrt M}
 \ll_A (\log p)^{1/2-A/4}.                                               \tag{2}
\]
Indeed, for arbitrary complex \(c_\ell\), the \(2s\)-moment of \(\sum_{\ell}c_\ell i(\ell^{\pm2})\) under \(m\) is at most \(n\|m\|_\infty s!(\sum |c_\ell|^2)^s\). Character orthogonality for the cap equates products modulo \(p\) up to sign. The products are positive and at most \(p/3\), hence the integer products coincide. Each ordered tuple has at most \(s!\) anagrams and their coefficient products agree. Apply Hölder and take the supremum over \(\sum |c_\ell|^2=1\). This strengthens mean-absolute sampling in [the short-family calculation](astra-diffuse-87.md#unique-factorization-in-the-short-family).

For a fixed \(h,k\), third-coordinate quotient character \(\gamma\), and additive frequency \(l\), the centered complete column after subtracting its main term has \(L^2(u,v)\) norm \(O_A(E_A/(1+\log p))\). For the plus column freeze \(v\), absorb the bounded mixed Weil sums in the coefficients of (2), and use the translated probability \(q^e_{i-h}\). Reverse the conditioning for the minus column. Identity corrections cost \(O(p^{-1/2})\). The trivial additive and third characters give \(nL(h(x)k(y))/(8\sqrt p)\) in the difference, including the requirement \(z+2\in Q\). These are the distinct-root columns of [the affine first-price calculation](astra-affine-90.md#the-two-endpoint-phases). Write \(e_\gamma\) for one complete third character's error. Quotient Parseval gives \(\sum_C|e_C|^2=d^{-1}\sum_\gamma|e_\gamma|^2\). Thus \(\sum_C|e_C|\le(\sum_\gamma|e_\gamma|^2)^{1/2}\). Take the \(L^2\) norm in the draws, sum the fixed character-pair envelopes, and sum the additive interval envelopes \(1,1/(2|l|)\). This proves (1), even in \(L^2(u,v)\) for the displayed supremum. Summing the errors before choosing coefficient phases justifies the envelope assertion.

For \(d=o(E_A^{-2})\), every adaptive union \(\mathcal U\) of cosets occupying a fixed positive fraction and every macroscopic interval on almost all draws has the sign of \(b-a\) on a fixed-gap sequence, with main price
\[
 {\alpha|\mathcal U|\over d}\,{n(b-a)\over 8\sqrt p}.
\]
Only membership in the third cosets enters this selection. For a polynomial scale take rational primes up to \(L=(p/3)^{1/4}\) and \(s=4\) in (2). All finite roots in the weighted and raw counts remain distinct for sufficiently large \(p\) because \(u^2v^2+v^2-u^2<p\), \(2u^2+1<p\) and \(u,v\ge2\). Now \(E=(1+\log p)p^{-1/16}\sqrt{\log p}\) suffices in (1). Adaptive unions are covered for \(d=o(p^{1/8}/(\log p)^3)\). The polylogarithmic assertion uses the original short probes.

## Paired conditional modulation

Let \(\mu_t(i)=nq_i r_{i+t}\), an actual probability for every displacement \(t\), and define two unit-Fourier-norm tests
\[
 K_t(x,y)=\sum_i\mu_t(i)i(x)\overline{(i+t)(y)},\qquad
 K_{t,j}(x,y)=\overline{j(x)}(j+t)(y)K_t(x,y).
\]
Thus \(K_{t,j}=\sum_i\mu_t(i)(i-j)(x/y)\), which modulates the full conditional transform at both endpoints. Reading the two axes in (1) gives
\[
 L(K_t)=\mu_t(0)r_t^e-\mu_t(-t)q_t^e,\qquad
 L(K_{t,j})=\mu_t(j)(b-a).                                                \tag{3}
\]
For \(t\ne0\) at most one term survives in the first formula, since \(q_{-t}>0\) forces \(r_t=r_{-t}=0\), and \(r_t>0\) forces \(q_t=q_{-t}=0\). In particular \(t=-j\) for a plus atom \(q_j>0\) gives \(\mu_t(j)=q_j/a\) and the raw coefficient \(-q_j q_j^e/a\). A minus atom \(r_j>0\) uses \(t=j\), \(\mu_t(0)=r_j/b\), recentering at zero. Equations (1) and (3) price the same entire adaptive union in both modulations without trimming an endpoint. At \(j=t=0\) the test is the constant one. [Conditional displacement law](astra-fibers-86.md#actual-conditional-law-at-each-positional-output)

## All couplings of the two centered endpoint populations

Suppose \(j\ne0,\ q_j>0\) and \(\alpha\ge\alpha_0>0\). Write \(X=\Re F(x)-\overline{\Re F}_C,\ Y=\Re R(y)-\overline{\Re R}_C\), where each bar is its arithmetic mean on \(M_C(I)\). These two real lists have mean zero separately for the realized finite primes. In each coset let \(\pi_C\) be *any* coupling of the lists' counting measures (both marginals give mass one per site). For \(x\) in the first marginal and \(y'\) in the second, put \(h=\overline{j(x)},\ k=\omega_C\,\overline{j(y')}^{\,\sigma_C}\), allowing any complex unit \(\omega_C\) and either \(\sigma_C=\pm1\). Define
\[
 \mathcal T_{\mathcal U}={1\over\sqrt p}\sum_{C\in\mathcal U}
   \int\Big(|X-Y'|+\min(|X|,|Y'|)|h-k|\Big)\,d\pi_C(x,y').
\]
All couplings, rotations, orientations and unions may be chosen after seeing the rows and probes. Uniformly over them and the indicated intervals,
\[
 \mathcal T_{\mathcal U}\ \ge\
 {\alpha|\mathcal U|\over d}\,{n q^e_j\over8\sqrt p}
       - O_{L^1,A,\alpha_0}\!\left(\sqrt d E_A+
            {d(1+\log p)\over\sqrt p}(1+\sqrt d E_A)\right).              \tag{4}
\]
Here \(d(1+\log p)/\sqrt p=o(1)\), as holds in both stated regimes. Interchanging the sides gives \(r_j^e\) for a minus atom. With complex \(X=F-\bar F_C,\ Y=R-\bar R_C\) the lower uses the full \(q_j\), or \(r_j\) on interchanging the roles. Complex modulation of the actual endpoint yields \(q_j\), while modulating its real first coefficient yields \(q_j^e\).

The raw count is \(\alpha p/(32d)+O(\sqrt p(1+\log p))\) per coset. The raw sum of either nontrivial phase \(j(x),j(y)\) is \(O(\sqrt p(1+\log p))\) there by the same distinct-root estimate. Hence its empirical phase mean is \(O_{\alpha_0}(d(1+\log p)/\sqrt p)\). Apply the separate marginal (1) with \(V=1\). The sum over cosets of the absolute *marginal totals* divided by \(\sqrt p\) has expected supremum \(O(1+\sqrt d E_A)\). This bounds the centering error after multiplication by the phase-mean bound. Applying (1) again with \(V=\overline{j(x)}\) on the plus side shows that its centered complex phase correlations divided by \(\sqrt p\) equal \(\alpha n q_j^e/(8d\sqrt p)\) with summed absolute error as in (4). The minus correlation has zero main term in either orientation by exact disjointness. The same argument with complex scores uses \(q_j\). An arbitrary unit phase per bin cannot enlarge its opposite correlation in magnitude.

For any coupling, \(|Xh-Y'k|\le |X-Y'|+\min(|X|,|Y'|)|h-k|\) by the two telescoping decompositions. Integrate and use the two exact marginals, then take the reverse triangle inequality on their complex correlation sums. This gives (4), retaining every site in each chosen coset. If \(q_j/a\ge c>0\) along a sequence, no coupling on a positive proportion of third cosets can make both costs vanish on most prime draws. This holds even if the original signed price tends to zero. Centering the two populations already removed their entire signed price exactly.

At square orders \(s^2\), take the genuine subfield pair with \(F=1_{\mathbb F_s^\times}\) and \(R=2/(s+1)\) on \(D_-\). Any match for nonzero subfield probes has \(F(x)=0\), since \(x\) in the subfield would force \(y\) there, contradicting its minus sign. Thus both centered scores are zero on every nonempty coset and the cost vanishes for every coupling. Nevertheless \(q_j/a=1\) for each nonzero \(j\) in the subfield annihilator. The prime input to (4) is necessary. [Square optimizers and affine matches](astra-affine-90.md#subfield-obstruction-and-finite-checks)

## Whole-fiber residual for a cloud of exterior atoms

There is also a test for the original pairing which can survive when every single exterior atom is \(o(n^{-1/2})\). Choose sets \(J_q,J_r\subset G\setminus\{0\}\) before the probes, \(K=|J_q|+|J_r|\), and
\[
 S^2=\sum_{j\in J_q}(q_j^e)^2+\sum_{k\in J_r}(r_k^e)^2>0,\qquad
 P(x,y)=S^{-1}\left(\sum_{j\in J_q}q_j^e\overline{j(x)}
                    -\sum_{k\in J_r}r_k^e\overline{k(y)}\right).
\]
This test has squared coefficient norm one, absolute coefficient sum at most \(\sqrt K\), and \(L(P)=-S\). Write \(\beta=|\mathcal U|/d,\ \Lambda=1+\log p,\ D_z=\Re R(y)-\Re F(x)\). Allow *arbitrary* fitted values \(g_C\) on the third cosets, with no size bound. Then
\[
 \begin{split}
 \left(\sum_{C\in\mathcal U}\sum_{M_C}|D_z-g_C|^2\right)^{1/2}
 \left({\alpha\beta\over32}+O\!\left({K\sqrt d\,\Lambda\over\sqrt p}\right)\right)^{1/2}
 \ \ge\ {\alpha\beta n S\over8\sqrt p}
  -O_{L^1}\!\left(\sqrt{Kd}\,E_A+
        {\sqrt K\,d\Lambda\over\sqrt p}(1+\sqrt d E_A)\right).             \tag{5}
 \end{split}
\]
The second factor may use a positive deterministic upper with implied absolute constant. The other constants depend on \(A,\alpha_0\), and the growing-index count condition of (4) applies. All \(g_C,\mathcal U,I\) may be chosen after the draw.

Subtract each bin's own phase mean \(\bar P_C\), which kills every \(g_C\) exactly. By (1) the normalized signed pairing with \(P\) on the union is \(-\alpha\beta n S/(8\sqrt p)+O_{L^1}(\sqrt{Kd}\,E_A)\). The raw-count phase bound gives \(\max_C|\bar P_C|\ll\sqrt K\,d\Lambda/\sqrt p\), so subtracting the phase means costs the second error in (5), by (1) with the original price. For the Gram factor, \(|P|^2\) has constant Fourier coefficient one and absolute coefficient sum at most \(K\). On each fixed endpoint mode, every additive and third Fourier mode of the raw centered count divided by \(p\) is \(O(p^{-1/2})\) by the distinct-root count. Quotient Parseval and the interval envelopes again bound the summed absolute coset error by \(O(\sqrt d\,\Lambda/\sqrt p)\). Thus \(p^{-1}\sum_{\mathcal U,M_C}|P-\bar P_C|^2\le p^{-1}\sum_{\mathcal U,M_C}|P|^2\le\alpha\beta/32+O(K\sqrt d\Lambda/\sqrt p)\). Cauchy–Schwarz with the actual centered test proves (5).

For instance, with the original polylogarithmic probes, if \(Kd E_A^2=o(1)\) and \(\sqrt n S\) is bounded below, the sum of squared residuals stays bounded below on every macroscopic interval and adaptive positive-density union on most draws, even for the empirical least-squares fit. Both other errors in (5) vanish in this regime. The criterion uses aggregated Fourier energy on a preselected set, without a lower bound on the largest individual atom. With one mode the stronger \(L^1\) price also follows: use \(\sup|P-\bar P_C|\le1+O(d\Lambda/\sqrt p)\) in the same signed pairing to lower-bound \(p^{-1/2}\sum|D_z-g_C|\). An exterior energy spread over too many characters may escape both estimates.

## Replay and two remaining tests

The [Arb384 replay](astra-fiber-91-check.py) reconstructs genuine optimal pairs at \(53,257,409\), including a feasible odd perturbation of the minus optimizer at the latter two. It checks the pointwise raw and recentered conditional transforms, quotient Parseval for the observed signed price, and exact centering on every used coset. At \(257\) both bins have three sites. The minimum scalar centered transport over every permutation lies in \((0.008747033,0.008747034)\). For the same marginals the phase-sensitive cost is at least \(0.019382343\) even with fitted rotations and orientations. This uses the observed magnitudes of the finite centered correlations and the coupling inequality, independently of the asymptotic main terms. At \(409\) a six-mode test gives a finite lower of \(0.197771451\) on the least-squares norm in (5), whose measured value lies in \((0.369740787,0.369740788)\). The minus masses at indices \(95\) and \(-95\) are respectively near \(0.001684565\) and \(0.001307524\). [Outward records](astra-fiber-91-checks.jsonl)

1. Compare the two *signed* first marginals on one adaptive union of a positive proportion of third cosets at the resolution in (1). On a displaced-atom sequence the comparison can instead use their joint recentered transform in (3). Equalizing the phase-sensitive absolute transports of the centered endpoints on that union is excluded by (4).
2. On a diffuse exterior sequence test whether the energy seen by (5) fits on \(K=o(1/(dE_A^2))\) modes. A successful signed comparison must accommodate its residual, or else use the remaining frequency mass at finer resolution. An upper for the full signed first price and the all-prime theta limit remain open.
