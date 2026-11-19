# Half of the signed marked price on matched opposite-sector outputs

Let \(p\equiv1\bmod4\) be prime, \(Q=\mathbb F_p^{\times2}\), \(n=|Q|\), \(d(x)=\chi(1-x)\), \(D_\pm=\{x\in Q:d(x)=\pm1\}\). Orient the genuine complementary optimal probabilities \(q,r\) by the **plus and minus signs**, with a common mark at zero. Write \(F,R\) for their characteristic functions and \(a=q_0,\ b=r_0\). Thus \(nab=1\), the two point caps are \(a,b\ll p^{-1/2}\), and only the indicated sector can carry nonidentity coefficients of each law. Noneven optimizers are allowed. For a real output weight \(m\) on \(Q\setminus\{1\}\), its actual marked cubic is
\[
 C(m)=pE(f_mUV)=\frac1{\sqrt p}\sum_{x\ne1}m(x)d(x)[1-\Re F(x)-\Re R(x)],\qquad C=C(1).
\]
Here \(f_m(i)=p^{-1/2}\sum_{x\ne1}m(x)d(x)\Re i(x)\). The ordinary-theta conjecture is equivalent to \(C=o(1)\). [Complementarity and the full marked price](astra-complement-84.md#a-fixed-cubic-test-at-the-marked-root)

Fix \(A>2\), put \(L=(\log p)^A\), and let \(\mathcal P_L\) be the rational primes at most \(L\). For **every** \(h_0\in Q\), use the shifts \(h=h_0\ell^2\) with \(\ell\in\mathcal P_L\), uniformly. Define the genuine matched signed price
\[
 H(h)=\frac1{\sqrt p}\sum_{\substack{x\in D_+\\hx\in D_-}}[\Re R(hx)-\Re F(x)].
\]
Then, uniformly over both optimal faces and the translate \(h_0\),
\[
 \mathbb E_\ell |2H(h)-C|\ll_A (\log p)^{1/2-A/4}.                     \tag{1}
\]
Each of the two one-law prices in \(H\) separately receives half of its full sector price in the same mean absolute error. The two counting prices cancel **exactly for every \(h\)**. Except when \(h=1\), the sum has \(n/4+O(\sqrt p)\) pairs. Along a fixed gap, almost all shifts in each short family have the same sign as the full marked price and carry half of it up to \(o(1)\). At \(A=4\) the mean error in (1) is \(O(1/\sqrt{\log p})\).

After deleting the two balanced quadratic images, the same pairs carry half the actual round-86 remainder. For almost every sharp threshold in a shrinking interval of amplitudes of order \((\log\log p)^{-1/8}\), they also carry half the separate signed price of the diffuse coefficients below that threshold, uniformly on every translate of the short family. Equations (4) and (4a) give the two estimates.

## Unique factorization in the short family

For \(w\in\{q,r\}\) and any complex weights \(|c_i|\le1\), put \(P(z)=\sum_i w_ic_i i(z)\). Uniformly in \(z\in Q\), either choice of exponent sign gives
\[
  \mathbb E_{\ell\in\mathcal P_L}|P(z\ell^{\pm2})|\ll_A (\log p)^{1/2-A/4}.       \tag{2}
\]
Choose unit phases for each of the \(M=|\mathcal P_L|\) values to make their sum real and nonnegative. The triangle inequality and Hölder on probability \(w\) bound its unnormalized \(2j\)-th power by \(\sum_i w_i|\sum_\ell e_\ell i(\ell^{\pm2})|^{2j}\). Replacing \(w\) by its point cap and applying character orthogonality gives at most \(n\|w\|_\infty\) times the number of pairs of ordered \(j\)-tuples with equal squared products in \(\mathbb F_p^\times\). Take \(j=\lfloor\log(p/3)/\log L\rfloor\). Both underlying positive integer products are at most \(p/3\). Congruent squares force equality over the integers, and unique factorization leaves at most \(j!M^j\) pairs. Reversing the exponent gives the same count. Hence the average is at most
\[
 (n\|w\|_\infty)^{1/(2j)}\sqrt{j/M}
 \ll_A L^{1/4}\sqrt{\log p/L}.
\]
Indeed \(M\gg L/\log L\) by Chebyshev's prime-count bound, and rounding \(j\) increases \(p^{1/(4j)}\) by a bounded factor relative to \(L^{1/4}\). This argument uses the field characteristic relative to its order.

For \(k(i)=p^{-1/2}\sum_{x\in Q}d(x)i(x)\), the Jacobi bound is \(|k(i)|\le1\). For either endpoint \(W\), the **full** translated price has the exact transform
\[
 X_w(h)=\frac1{\sqrt p}\sum_{x\in Q}d(hx)W(x)=\sum_i w_i k(i)\overline{i(h)}.      \tag{3}
\]
Consequently (2) applies to \(X_w(h)\) and \(X_w(h^{-1})\), with the same bound for \(W(h^{\pm1}z)\) at every center \(z\). This estimate retains arbitrarily small signed coefficients of \(W\). [Jacobi normalization](astra-fibers-86.md)

Pair each positive disagreement output \(x\) with the negative output \((hx)^{-1}\). This bijects the two orientations, since \(d(y^{-1})=d(y)\) on \(Q\). Also \(\Re R((hx)^{-1})=\Re R(hx)\). Thus \(H(h)\) is precisely the cubic of the strict disagreement mask. Its pair count follows by expanding the sign indicators. The only mixed sum is \(\sum_{x\in Q}d(x)d(hx)\), which for \(h\ne1\) is \(O(\sqrt p)\) by the quadratic and cubic character bounds after inserting \((1+\chi(x))/2\) on \(\mathbb F_p^\times\). [Translate correlation bounds](parallel-torus-8.md#a-uniform-bound-for-twisted-translate-correlations)

For each row of sign \(\sigma\), strict disagreement selects \((1-\sigma d(hx))/2\) on its sector, up to half weight at the single exceptional point \(hx=1\). The sector sum with factor \(d(hx)\), divided by \(\sqrt p\), is \(X_w(h)-d(h)/\sqrt p\). Equation (2) now bisects each actual price. In the full cubic the sector count difference is \(\sum_Q d=-1\). Its contribution is \(O(p^{-1/2})\). This proves (1), including the strict-mask convention.

## Pair deletion on the actual round-86 remainder

For a fixed \(\tau>0\), take any equally sized subsets \(S_\pm\) of the two genuine nonidentity \(\tau\)-heads. Let \(E_\pm=T(S_\pm)\cap Q\) for \(T(x)=(1-2x)^2\), \(E=E_+\cup E_-\), and \(C_{\rm rem}=C(1_{Q\setminus E})\). The round-86 estimates give \(|E|\ll_\tau\sqrt p\), \(C_{\rm rem}=C+O_\tau(p^{-1/1056})\), and
\[
 \sum_{E_+}|F|+\sum_{E_-}|R|\ll_\tau \sqrt p\,p^{-1/1056}.
\]
Keep only pairs \(x,(hx)^{-1}\) for which **both outputs avoid \(E\)**, and write \(H_E(h)\) for their marked cubic. The shifted argument of \(R\) in its oriented formula is still \(hx\); the ban on outputs is tested at \((hx)^{-1}\), even when \(E\) is not inversion invariant. Uniformly in the chosen heads and \(h_0\),
\[
 \mathbb E_\ell |2H_E(h)-C_{\rm rem}|
       \ll_{\tau,A} p^{-1/1056}+(\log p)^{1/2-A/4}.                         \tag{4}
\]
The sum of the absolute prices at the banned endpoints is bounded by the displayed round-86 estimate. A banned positive endpoint \(z\) has opposite price at most \(|R(hz)|\). A banned negative endpoint \(z\) has opposite price at most \(|F(h^{-1}z^{-1})|\). Average (2) at each of the \(O_\tau(\sqrt p)\) banned endpoints, then divide by \(\sqrt p\). Deleting whole pairs preserves exact counting cancellation. [Image price and count estimates](astra-fibers-86.md#from-the-quadratic-image-to-the-true-fiber-price)

For this actual surviving output mask \(m_h\), the displacement identity is
\[
 H_E(h)=\frac{n}{n-2}B_{f_{m_h}}-Z_{f_{m_h}}.
\]
Here \(B_f=\sqrt p[a\Delta_r(f)-b\Delta_q(f)]+pabE(fk^2)\), \(\Delta_w(f)=w(fk)-E(fk)\), and \(Z_f\) sums the true distinct-center terms after centering each individual displacement. Thus (4) prices a dense collection of actual centered displacement tests with both one-law axes included. A gap sequence on which both heads have \(o(\sqrt p)\) sites at **every fixed positive threshold** allows a diagonal choice \(u(p)\downarrow0\) with combined \(u(p)\)-heads still of size \(o(\sqrt p)\). Removing pairs meeting either of those heads changes the matched price by \(o(1)\) **at every shift**, since each site removes at most one pair of bounded coefficients. Both coefficients of every surviving pair then tend uniformly to zero, and (1) still puts half the gap on the short-shift family. [Exact centered displacement identity](astra-fibers-86.md#from-the-quadratic-image-to-the-true-fiber-price)

## Genuine sharp shrinking cutoffs on the short prime shifts

For \(0\le u\le1\) let \(H_{\le u}(h)\) keep just those matched pairs for which **both** \(|F(x)|\le u\) and \(|R(hx)|\le u\). Define the true signed linear price
\[
 P_{\le u}=\frac1{\sqrt p}\left[\sum_{\substack{y\in D_-\\|R(y)|\le u}}\Re R(y)
              -\sum_{\substack{x\in D_+\\|F(x)|\le u}}\Re F(x)\right].
\]
The paired mask still has zero signed output count, even at a cutoff. Put \(\eta=(\log p)^{1/2-A/4}\). For any integer \(j\ge1\), \(0<b\le1/2\),
\[
 \frac1b\int_b^{2b}\sup_{h_0\in Q}\mathbb E_\ell
       |2H_{\le\sqrt t}(h_0\ell^2)-P_{\le\sqrt t}|\,dt
 \ll_A 3^j\eta+\frac{j^{-1/2}+\eta}{b}+p^{-1/2}.                        \tag{4a}
\]
In particular take \(j=\lfloor c_A\log\log p\rfloor\) with \(0<c_A<(A/4-1/2)/\log3\), and \(b=j^{-1/4}\). The left side is \(O_A(j^{-1/4})\) for a fixed such choice. Except on a fraction \(O_A(j^{-1/8})\) of the squared cutoffs in this interval, the error is \(O_A(j^{-1/8})\) simultaneously for **all** translates. Both actual coefficients in every retained pair then have modulus at most \(\sqrt2\,j^{-1/8}\). This directly samples the signed diffuse price of arbitrary genuine optima, even when the intermediate heads are large.

For a squared amplitude \(z\), use the polynomial \(G_{j,t}(z)=\Pr(\operatorname{Bin}(j,z)/j\le t)\). Its sum of absolute monomial coefficients is at most \(3^j\) by expanding the binomial probabilities. For each monomial \(W(x)|W(x)|^{2m}\), its law is the probability \(w*(w*\widetilde w)^{*m}\), with \(\widetilde w_i=w_{-i}\). Convolution with a probability preserves the point cap upper bound, so the proof of (2) and (3) applies to each of these laws. The nonidentity support also stays in the original sector. Hence the strict-disagreement selector bisects the one-law price \(W G_{j,t}(|W|^2)\) with mean absolute error \(O_A(3^j\eta+p^{-1/2})\). The axis error uses \(0\le G_{j,t}\le1\) on \([0,1]\); the possible identity term is bounded in the same way.

The discrepancy upon replacing the Bernstein polynomial by the sharp indicator in either the full or selected price is bounded by \(p^{-1/2}\sum |W|\,|G_{j,t}(|W|^2)-1_{|W|^2\le t}|\), uniformly in **all** shifts. For fixed \(z\) its unweighted mean indicator error on \([b,2b]\) is at most
\[
 b^{-1}\mathbb E|\operatorname{Bin}(j,z)/j-z|\le \frac{\sqrt z}{b\sqrt j}.
\]
Indeed an indicator can differ only when the threshold lies between the sample and its mean. Integrating the deterministic price error therefore charges only \(\sum |W|^2/\sqrt p=O(1)\). This allows the supremum in (4a) inside the integral. Finally a survivor whose opposite partner fails the cutoff contributes, in short-shift absolute average, \(O_A(\eta/\sqrt p)\) per offending opposite head site by (2). There are \(O(\sqrt p/b)\) such sites for each sign. This proves (4a) with exact paired counts. If \(P_{\le\sqrt t}\) carries a fixed price, this size of sharp diffuse modes carries half of it on the matched displacements. The estimate does not give the value of \(P_{\le\sqrt t}\) itself.

## Simultaneous diffuse cutoffs over the full group

Put \(b(x)=\max(|F(x)|,|R(x)|)\) on \(x\ne1\), \(L_u=\{x\ne1:b(x)\le u\}\), and \(0<\delta<1/4\). For the strict disagreement set \(D(h)\), uniform sampling over all \(h\in Q\) gives
\[
 \left\|\sup_{p^{-1/4+\delta}\le u\le1}
   |2C(1_{L_u\cap D(h)})-C(1_{L_u})|\right\|_{L^2(h)}
       \ll (\log p)p^{-\delta}.                                          \tag{5}
\]
In this single-output truncation the signed counting contribution need not cancel exactly, and is included in (5).

In fact \(Jv(h)=p^{-1/2}\sum_xd(hx)v(x)\) satisfies
\[
 \|Jv\|_{L^2(h)}^2=\frac1{n^2}\sum_i|k(i)|^2\Big|\sum_xv(x)i(x)\Big|^2
 \le\frac1n\sum_x|v(x)|^2 .
\]
For prefixes in any fixed ordering, the maximal \(L^2\) norm is bounded by \((2+\log_2 n)(\sum |v|^2/n)^{1/2}\). Split a prefix into at most one dyadic block of each length. At each level the maximum is bounded by the square root of the sum of squared block outputs. Apply the preceding inequality on disjoint blocks and the triangle inequality over levels. Order the sites by descending \(b\). All counts deleted by the cutoffs in (5) are prefixes of at most \(M\ll\sqrt p\,p^{1/2-2\delta}\) sites by Parseval and the two point caps. Their maximal translated count costs \(O(\log p\sqrt{M/n})\), while the full translated count is \(-1/\sqrt p\) before omitting the identity. The retained linear coefficients are tails of a sequence of squared norm \(\sum_{x\ne1}|\Re F(x)+\Re R(x)|^2\ll\sqrt p\). Their maximal translated cost is \(O((\log p)p^{-1/4})\). Expanding strict disagreement as above has only the single exceptional \(hx=1\) at price \(O(p^{-1/2})\). This proves (5).

For the **paired** cutoff and its linear price from (4a), complete-group sampling gives a simultaneous bound at every cutoff in a wider range. For \(0<\delta<1/8\),
\[
 \mathbb E_{h\in Q}\sup_{p^{-1/8+\delta}\le u\le1}
     |2H_{\le u}(h)-P_{\le u}|
     \ll (\log p)p^{-1/4}+p^{-2\delta}.                                  \tag{6}
\]
First apply the maximal linear estimate from the preceding paragraph to each truncated row separately with its own strict disagreement selector. To remove unpaired survivors uniformly in \(u\), majorize their absolute cost by the cost of all partners of the \(p^{-1/8+\delta}\)-heads. A head of size \(M_0\ll\sqrt p\,p^{1/4-2\delta}\) has average opposite cost at most \(M_0 n^{-1}\sum|W|/\sqrt p\ll p^{-2\delta}\) by Cauchy–Schwarz and Parseval. Exact counted pairs require no further deterministic correction. Equations (5) and (6) concern complete-group sampling. Equations (1), (4), and the threshold-averaged (4a) hold on every translate of the explicit short family.

## Square distinction and finite intervals

At field order \(v^2\), let \(v\) be an odd prime tending to infinity and use the genuine pair \(F=\mathbf1_{\mathbb F_v^\times}\) and \(R=2/(v+1)\) on \(D_-\) with \(R(1)=1\). For any \(h\ne1\) in the subfield multiplicative group, the shifted plus price on its exterior is \((v-3)/v\). Its full exterior plus price is \((v-2)/v\) and its strict-disagreement part vanishes, since no positive subfield site has a negative subfield translate. There are \(n/4+O(v)\) disagreement pairs, so \(H(h)=1/4+O(1/v)\), whereas \(C=-1/2+O(1/v)\). All the rational-prime squares in the short family at \(h_0=1\) are nonidentity subfield shifts eventually. Thus this failure concerns the actual two-sided signed price. [Square complementary optima](parallel-witness-6.md#the-four-coordinates-have-independent-limiting-support)

The [384-bit replay](astra-diffuse-87-check.py) reconstructs genuine even complementary optima at \(53,101,257,409,769\). It checks (3) at every shift for each endpoint, the exact translated second moments, the degree-five binomial multiplier through its positive convolution powers, three diffuse cutoffs, the paired deletion identity at every shift, and the displacement-centered expansion by direct FFT summation at \(h=4\) for both a cutoff and a paired deletion. The weighted agreement cutoff gives half weight at \(hx=1\). The paired deletion always uses strict disagreement. At \(769\), equal heads of size \(140\) give image sizes \(87,140\). At \(h=4\), the \(19\) surviving pairs have actual cubic in \((0.010416377,0.010416378)\), while the full remainder is in \((1.692146703,1.692146704)\). These finite values show the distinction between a single shift and the asymptotic average. The records also test the exact subfield price at \(v=11,19,43\). These finite intervals check the identities independently of the asymptotic short-family bound. [Interval records](astra-diffuse-87-checks.jsonl)

1. Bound the signed difference of the **surviving matched endpoints** in (4) to \(o(1)\) on a positive proportion of one short family after dividing by \(\sqrt p\). Equation (4) would then force the full marked cubic to vanish. In the conditional representation law of round 86 these matched outputs use distinct decomposition fibers. Their counts already cancel. The comparison must price both endpoint-weighted sums.
2. Compare \(P_{\le\sqrt t}\) in (4a) with the full price on a fixed-gap sequence at a good sharp cutoff. The outstanding companion is the signed difference between the **intermediate** linear prices of the two rows. A direct estimate on the paired diffuse price at good cutoffs and a bound on that companion would handle both possible sources of the gap. For a prescribed cutoff the Bernstein boundary instead requires the endpoint-weighted price of its transition band.
