# A common positive lift for periodic caps

For a Paley sign let \(Q=\mathbb F_p^{\times2}\), \(G=\widehat Q\), \(n=|Q|\), and let \(D\) be its forbidden positional set. Write \(K=D\cup\{1\}\) for the opposite allowed positions. Use \(\widehat q(x)=\sum_i q_i i(x)\). The full objective is \(\Theta=n\max q_0\). For a subgroup \(B<Q\) of order \(b\) write \(P=B^\perp\), \(H=G/P\). The restricted objective \(\Theta_B=b\max h_0\) uses the forbidden set \(B\cap D\) on \(H\). Uniform lifting gives \(\Theta_B\le\Theta\). Equality is equivalent to existence of a true optimizer periodic by \(P\), and to a true optimizer having an entire \(P\)-coset at its cap, by averaging those translates to the root. The estimates below use the true restricted problem even when equality fails. The reciprocal identities on the full group and on every subgroup follow by the same vertex-transitive theta duality. [Full formulation](fourier.md) · [Previous cardinality test](astra-cap-74.md)

## A weighted return forces a relative theta gap

Let \(h\) be any tested quotient optimum and \(r\) any opposite full optimum, so \(r_0=1/\Theta\). For \(z\in Q\) set
\[
 M(z)=\sum_{x\in B\setminus\{1\}:\ zx^{-1}\in K}|\widehat h(x)|.
\]
For every positive integer \(k\) with \(z^k\notin K\),
\[
 1-\frac{\Theta_B}{\Theta}\ \ge\ \tfrac12\big(k^{-2}-M(z)\big)_+. \tag{1}
\]
This holds for every subgroup order. In particular a return of bounded length with \(M(z)\le k^{-2}-\epsilon\) loses at least \(\epsilon/2\) of the full objective, uniformly in the prime. The overlap weights are the actual quotient Fourier coefficients. One may retain the factors \(|\widehat r(zx^{-1})|\) inside \(M\) when they are bounded separately.

Indeed \(u_i=b h_{[i]}r_i\) is a probability by disjoint nonconstant Fourier supports, with \(u_0=\Theta_B/\Theta\). Fourier inversion gives
\[
 \widehat u(z)=\sum_{x\in B}\widehat h(x)\widehat r(zx^{-1}),\qquad
 1-\operatorname{Re}\widehat r(z)\le 2(1-u_0)+M(z).
\]
For any unit complex number \(w\), \(|1-w^k|^2\le k^2|1-w|^2\). Integrating against \(r\) and using \(\widehat r(z^k)=0\) proves (1). For \(M(z)=0\) and an exact period, \(\widehat r(z)=1\) so *every* positive coordinate of *every* opposite optimum satisfies \(i(z)=1\). Consequently its transform is invariant under multiplication by \(z\). When \(b\) is prime, the central opposite transform occupies all of \(K\cap B\), as proved below. Thus \(\langle z\rangle(K\cap B)\subset K\). In particular, if \(K\cap B\ne B\) then \(\langle z\rangle\cap B\) is trivial. These statements apply whenever an exterior fiber can be aligned so that \(\{v\in B:zv\in K\}=K\cap B\), since the central mask is inversion invariant. They propagate one aligned fiber across all its powers.

For any tested optimizer \(q\), every coset of \(P\) has total mass at most \(|P|\Theta_B/n\) by quotient projection and translation. If \(q_i\ge(1-\tau)\Theta/n\) on a fraction \(f\) of such a coset, then \(f(1-\tau)\le\Theta_B/\Theta\). Hence (1) also forces missing near-cap sites in the same cosets, with no lower bound on how much mass lies in an individual missing site.

## Exact simultaneous positivity and the price of failure

Suppose now that \(b\) is prime. The two reciprocal restricted optimizers are unique even before assuming a full period. Let \(J=\operatorname{supp}h\) and \(K_1=K\cap B\). For a nonzero row on the prime group with Fourier support in \(S\), at most \(|S|-1\) coordinates vanish. Thus \(|J|\ge |K_1|\), from the tested Fourier zeros. The quotient opposite optimizer vanishes on \(J\setminus\{0\}\) by complementary slackness, so \(|J|\le |K_1|\), and its transform uses all of \(K_1\). The midpoint of two tested optima must have the same support size, which fixes their common support. The \(|J|-1\) forbidden Fourier equations determine the row there up to normalization by the prime Fourier minor theorem. Swapping signs proves the reciprocal uniqueness. [Prime cyclic uncertainty](https://arxiv.org/abs/math/0308286)

Normalize the opposite quotient optimizer by its root and denote it by \(W^*\), so \(W^*(0)=1\). It is the unique row with Fourier support in \(K_1\) whose restriction to \(J\) is \(\mathbf1_{j=0}\). For each real function \(\phi\) on \(G\) with Fourier support in the *exterior positions forbidden to the opposite sign*, \((Q\setminus B)\setminus K\), write \(a_j=-\min_{i\in j}\phi_i\). Each fiber mean vanishes, so \(a_j\ge0\). Then
\[
 \Theta=\Theta_B\quad\Longleftrightarrow\quad
 \phi_0\le\sum_{j\ne0}W_j^* a_j\quad\hbox{for every such }\phi. \tag{2}
\]
If equality of the objectives holds, projecting \(r/r_0\) gives \(W^*\). Indeed the projected probability has root at least \(r_0=1/\Theta_B\), the quotient opposite cap. Its root fiber therefore consists solely of the root atom. The other fibers carry specified masses \(W_j^*\), and annihilation of all \(\phi\) implies (2). Conversely, prescribe these masses on the nonroot fibers, with the unit atom at the root. The resulting nonnegative rows form a product of compact simplices. Its image under the exterior forbidden Fourier evaluations is compact and convex over the reals. The minimum pairing against a real linear combination of evaluations equals \(\phi_0-\sum_{j\ne0}W_j^*a_j\). Separation gives a simultaneous zero precisely under (2). All central equations hold by the marginal. The lift has mass \(\sum W^*=\Theta_B\), so normalization gives an opposite feasible probability of root \(1/\Theta_B\) and forces equality. The minima in each fiber price the same positive lift over *all* exterior positions.

There is a quantitative version. Write \(H_j=h_j/h_0\). Let \(L_j\) be the cardinal interpolation row in the space with Fourier support in \(K_1\) such that \(L_j(k)=\mathbf1_{k=j}\) for \(k\in J\). These rows are real by conjugation and uniqueness. Let \(W_j=\sum_{i\in j}r_i/r_0\). On \(J\), \(e_j=W_j-\mathbf1_{j=0}\ge0\), and on all sites \(W-W^*=\sum_{j\in J}e_j L_j\). The probability identity for \(u\) gives \(\sum_{j\in J}H_j e_j=\Theta/\Theta_B-1\). The full exterior constraints with the one root atom split off imply \(\phi_0+a_0\le\sum W_j a_j\). Therefore every strictly positive violation \(V=\phi_0-\sum_{k\ne0}W_k^*a_k\) gives
\[
 \frac{\Theta}{\Theta_B}-1\ \ge\
 \frac{V}{\displaystyle\max_{j\in J}H_j^{-1}\sum_{k\in H}L_j(k)a_k}. \tag{3}
\]
The denominator is positive when \(V>0\) by the inequalities just proved. Its size can depend on the prime. Formula (1) avoids this interpolation constant for the stated return patterns.

For odd prime \(b\) the subgroup generated by \(B\) and \(-1\) has order \(2b\). On it the exterior probe is \(\phi_i=i(-1)g([i])\), where \(g\) is any real function on \(H\) with Fourier support in \(E=\{v\in B:-v\notin K\}\). Thus (2) on these two layers becomes \(g(0)\le\sum_{j\ne0}W_j^*|g(j)|\) for every such \(g\). A strict violation excludes the full period for arbitrary \(|P|\). Equivalently \(\Theta_{B\cup(-B)}>\Theta_B\). When \(|P|=2\) this is already the full simultaneous test.

## Certified quotient gaps on actual surviving masks

The [checker](astra-quotient-75-check.py) tests previously surviving prime quotients with \(b^2\ge4n\) and \(p\le3000\). It forms the actual signed masks on \(B\) and \(B\cup(-B)\). It certifies a feasible tested row on the latter and a feasible *opposite* row on the former. Their rational lower bounds \(L_{2b}\) and \(L_b^-\) give \(\Theta_{2b}\ge L_{2b}>b/L_b^-\ge\Theta_B\) in **all 51 cases**. The candidates come from floating LPs, followed by Arb cosine enclosures, integer coefficient rounding, and the diagonal repair in the repository's exact verifier. The [rational records](astra-quotient-75-checks.jsonl) give the separate bounds for each case. For example \(p=137,b=17,\sigma=+1\) has \(\Theta_{2b}>6.3067\), \(\Theta_B<5.4360\), with \(2b=34<n=68\). The smallest certified relative gain \(L_{2b}/(b/L_b^-)-1\) exceeds \(0.0178\) at \(p=997,b=83,\sigma=-1\). No full-field optimizer reconstruction enters these comparisons. The finite exclusions and (1)–(3) leave the general growing-prime period and singleton-window bounds open.

1. Bound the weighted two-layer probe minimum on the actual quotient optimum through primes, or exhibit a bounded return with the weighted overlap in (1) uniformly below \(k^{-2}\). Either route can turn a count-surviving family into a quantitative near-cap exclusion.
2. For actual singleton caps, compare the per-coset near-cap deficits with the occupied sites of an actual negative window mask. A global missing-site count alone gives no weighted collision bound there, and the ordinary all-prime theta limit remains open.
