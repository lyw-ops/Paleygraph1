# How much of each genuine third coset can have equal signed first prices?

Write \(X(x)=\Re F(x),\,Y(y)=\Re R(y)\) for genuine optimal rows on the plus and minus sectors \(D_+,D_-\subset Q=(\mathbb F_p^\times)^2\), with \(p\equiv1\bmod4\), \(n=(p-1)/2\), and marks \(a,b\). On the actual strict matches \(x=u^2z\in D_+,\,y=v^2(z+1)\in D_-,\,w=z+2\in C\), let \(D_z=Y(y)-X(x)\). Here \(C\) runs over the \(d\) cosets of a fixed subgroup of \(Q\). For an additive interval \(I\), let \(M_C\) denote its matches, \(N_C=|M_C|\), and \(\mathcal U\) an arbitrary union of cosets. Put \(\alpha=|I|/p,\ \beta=|\mathcal U|/d\) where \(|\mathcal U|\) counts cosets. All prices are sums of \(D_z/\sqrt p\).

## Equal retention in each third coset on the original short primes

Let \(m_C\) be any median of the scores on \(M_C\) and set
\[
 H={1\over\sqrt p}\sum_{C\in\mathcal U}\sum_{M_C}D_z,\qquad
 V={1\over\sqrt p}\sum_{C\in\mathcal U}\sum_{M_C}|D_z-m_C|.
\]
Empty bins contribute zero. Among fractional subsets retaining exactly half of **each** chosen bin, the range of total signed prices is exactly
\[
                       [(H-V)/2,(H+V)/2].                             \tag{1}
\]
Indeed, use the lower half and then the upper half of each sorted bin, splitting a median site at odd size. The two sums add to the full sum, and their difference is the sum of deviations from the median. Convexity fills the interval. For ordinary subsets retaining \(\lfloor N_C/2\rfloor\) sites in each bin, the two endpoints move by at most \(d/\sqrt p\), since \(|D_z|\le2\). A sequence of within-bin swaps from the bottom selections to the top selections has successive price changes between zero and \(4/\sqrt p\). Thus the best absolute signed price differs from \((|H|-V)_+/2\) by at most \((d+4)/\sqrt p\). The two endpoint first marginals in this comparison are evaluated on the same sharp subset.

There is a sufficient test for (1) using a preselected cloud of exterior Fourier atoms on the original independent primes \(u,v\le(\log p)^A,\ A>6\). Take \(P,S,K\) as in [the cloud estimate](astra-fiber-91.md#whole-fiber-residual-for-a-cloud-of-exterior-atoms): \(S^2\) is the combined squared evenized exterior mass on the \(K\) chosen modes, and \(P=(\sum_{J_q}q_j^e\overline{j(x)}-\sum_{J_r}r_j^e\overline{j(y)})/S\). Write \(T_z=P(x,y)-\overline P_C\), subtracting the actual complex bin mean. For any \(B>0\) define the realized excess
\[
 J_B={1\over\sqrt p}\sum_{C\in\mathcal U}\sum_{M_C}
              |D_z-m_C|(|T_z|-B)_+ .
\]
Then
\[
 B V+J_B\ \ge\ {\alpha\beta n S\over8\sqrt p}-\mathcal E,\qquad
 \mathbb E\sup_{I,\mathcal U}|\mathcal E|
 \ll_{A,\alpha_0}\sqrt{Kd}\,E_A+
       {\sqrt K\,d\Lambda\over\sqrt p}(1+\sqrt d E_A),                  \tag{2}
\]
where \(\Lambda=1+\log p,\ E_A=\Lambda(\log p)^{1/2-A/4}\), \(\alpha\ge\alpha_0>0,\ d\Lambda/\sqrt p=o(1)\). To see this, take the absolute value of the centered signed pairing in the proof of the cloud estimate. Each bin contributes exactly \(\sum(D_z-m_C)T_z\) before division by \(\sqrt p\). The triangle inequality followed by splitting at \(B\) gives (2), simultaneously for every realized choice of \(B\).

For example, fix \(B>0\), take \(KdE_A^2=o(1)\), and a macroscopic union and interval. With an \(o_{\mathbb P}(1)\) slack, the condition
\[
         J_B \le {\alpha\beta n\over8\sqrt p}\big(S-B|b-a|\big)          \tag{3}
\]
suffices to equalize the signed first marginals to \(o_{\mathbb P}(1)\) on an ordinary half-selection in every chosen bin, in the sense of the **total** signed price. Use the full price \(H=\alpha\beta n(b-a)/(8\sqrt p)+o_{\mathbb P}(1)\) on those same bins and substitute (2) in (1). Conversely, if every such selection has price of absolute value at least \(c>0\), its realized cloud excess must satisfy
\[
        J_B\ \ge\ {\alpha\beta n\over8\sqrt p}\big(S-B|b-a|\big)
                    +2Bc-o_{\mathbb P}(1).
\]
The price of all omitted sites need not be small. The formula deals with medium atoms collectively and allows large values of the character polynomial away from sites bearing median deviation. No upper bound for \(J_B\) on arbitrary optimal faces has been established.

## The signed difference law at all retention fractions on longer prime probes

Let \(\nu\) be the law of \(D=Y(y)-X(x)\) for **independent** uniform \(x\in D_+\), \(y\in D_-\). Both rows and their phases are the actual rows. Let \(\widehat\nu_C\) be the empirical law of \(D_z\) on a bin; interpret its terms weighted by \(N_C=0\) as zero. Draw \(u,v\) independently uniformly from any predetermined set \(\mathcal P\subset\{1,\ldots,p-1\}\) of size \(M\); it may consist entirely of rational primes. Then, with \(W_1\) the real-line 1-Wasserstein distance,
\[
 \left\|\sup_I\sum_C {N_C\over\sqrt p}W_1(\widehat\nu_C,\nu)\right\|_{L^2(u,v)}
       \ll {p-1\over M}\sqrt d\,p^{-1/4}\Lambda^{3/2}.                 \tag{4}
\]
For the full interval the last power is \(\Lambda^{1/2}\). In particular for all rational primes up to \(p^\kappa\), fixed \(3/4<\kappa\le1\) and excluding \(p\), the interval error is \(O_\kappa(\sqrt d\,p^{3/4-\kappa}\Lambda^{5/2})\). The shorter polylogarithmic primes in (2) use different arithmetic input.

Here is the proof. First use independent uniform residues \(u,v\in\mathbb F_p^\times\), so their squares are independent uniform elements of \(Q\). For a function \(W\) on \(Q^2\) of mean zero, and third character \(\gamma\) and additive frequency \(l\), define
\[
 Z_{\gamma,l}(W)={1\over\sqrt p}
 \sum_{z,z+1,z+2\in Q}W(u^2z,v^2(z+1))\gamma(z+2)e_p(lz).
\]
Every Fourier mode \(i(x)j(y)\) with \((i,j)\ne(0,0)\) has a complete column of modulus \(O(1)\). Expand the three square-restricted characters into their two multiplicative lifts. At \(0,-1,-2\) the finite roots are distinct, and a nontrivial character on \(Q\) forces a nontrivial lift at its own root. For \(l\ne0\) the additive phase also has a simple pole at infinity. These are the fixed distinct-root bounds used in the affine estimate. [Affine columns](astra-linear-89.md#complete-twisted-columns-and-short-averaging) · [Mixed Weil bound, Theorem 5](https://pmc.ncbi.nlm.nih.gov/articles/PMC10941333/). Independent dilation orthogonality now gives
\[
          \mathbb E |Z_{\gamma,l}(W)|^2
                  \ll\sum_{i,j}|\widehat W(i,j)|^2
                   =\mathbb E_{Q^2}|W|^2.                             \tag{5}
\]
The third-quotient character expansion and Parseval cost \(\sqrt d\) for the sum of absolute bin errors. Completion with the common interval coefficient envelope costs \(O(\Lambda)\). Both bounds hold in \(L^2\). Restricting the two residues to \(\mathcal P\) costs at most \((p-1)/M\) in that norm by conditioning on the two independent events.

For each \(t\in[-2,2]\), put \(s_t=\nu((t,\infty))\) and apply (5) to
\[
 W_t(x,y)=1_{D_+\times D_-}(x,y)\big(1_{Y(y)-X(x)>t}-s_t\big).
\]
This has mean exactly zero; its squared norm is \((|D_+||D_-|/n^2)s_t(1-s_t)\). Its actual bin sum divided by \(\sqrt p\) is exactly \(N_C(\widehat\nu_C((t,\infty))-s_t)/\sqrt p\). Integrate the absolute threshold errors. In one dimension the area between distribution functions equals both \(W_1\) and the integral of the absolute difference of the quantiles; this follows by counting the area between their graphs by horizontal or vertical slices. Minkowski's inequality permits the integration in \(L^2\).

Finally \(\mathbb E_\nu D^2\ll p^{-1/2}\): Parseval gives \(\sum_Q |F|^2\le na,\ \sum_Q |R|^2\le nb\), with sector sizes comparable to \(n\). On \(|t|\le p^{-1/4}\) bound the integrand \(\sqrt{s_t(1-s_t)}\) by one. Outside this interval, bound it by \(\Pr_\nu(|D|\ge |t|)^{1/2}\), then use Cauchy–Schwarz with weights \(t\) and \(1/t\) on the positive half. The integral of \(t\Pr(|D|\ge t)\) is at most \(\mathbb E D^2/2\), and the reciprocal weight costs \(O(\Lambda)\). This proves (4).

For a macroscopic interval and a positive fraction of the third cosets the realized total \(N=\sum_{C\in\mathcal U} N_C\) is \((\alpha\beta/32+o_{\mathbb P}(1))p\) whenever (4) is \(o(1)\). In fact apply (5) to \(1_{D_+\times D_-}-|D_+||D_-|/n^2\) to compare \(N\) to the corresponding fraction of the base count, at price \(O_{L^2}((p-1)\sqrt{pd}\Lambda/M)\) in raw counts. The base count of \(z,z+1\in Q,\ z+2\in\mathcal U\) is \(\alpha\beta p/8+O(\sqrt{pd}\Lambda)\), by the same fixed-root estimates and quotient Parseval. Also \(|D_+|=(n-2)/2,\ |D_-|=n/2\). This argument accommodates long probes for which moving sign roots might coincide, since the sign restrictions belong to the test on \(Q^2\).

## What an adaptive signed comparison can and cannot remove

Write \(Q_\nu(v)\) for the ascending quantile on \(0<v<1\), and set \(L(\rho)=\int_0^\rho Q_\nu(v)\,dv,\ U(\rho)=\int_{1-\rho}^1 Q_\nu(v)\,dv\). After observing all data, choose any \(\mathcal U,I\), and for each bin any integer \(0\le k_C\le N_C\). The smallest and largest signed prices among ordinary subsets retaining \(k_C\) sites there are respectively
\[
 \sum_{C\in\mathcal U}{N_C\over\sqrt p}L(k_C/N_C),\qquad
 \sum_{C\in\mathcal U}{N_C\over\sqrt p}U(k_C/N_C)                       \tag{6}
\]
up to the **same simultaneous error** bounded by the left side inside the norm in (4). This follows from sorting and the quantile representation of \(W_1\). Every intermediate price is attained to within another \(4/\sqrt p\) by the sequence of swaps used for (1). There is no lower cutoff on retained or deleted fractions. At full retention the two endpoints coincide with \(N\mathbb E_\nu D/\sqrt p\), including the true means \(\mathbb E_\nu D=(nb-1)/|D_-|-(na-1)/|D_+|\).

* If \(\sqrt p\,\mathbb E_\nu|D|\to\infty\), the signed marginals can be equalized within \(2/\sqrt p\) on \(1-o_{\mathbb P}(1)\) of all sites of **each macroscopic chosen union**, uniformly on draws with the error in (4) tending to zero. The intact union has bounded signed price because \(|\mathbb E_\nu D|\ll p^{-1/2}\), while its absolute price diverges by (4) applied to the 1-Lipschitz function \(|D|\). Hence its two sign totals both diverge. Remove same-sign sites in decreasing order of magnitude until the remaining signed sum first crosses zero. The removed fraction is at most the original absolute signed price divided by the corresponding absolute sign total, plus \(1/N\), since the largest fraction carries at least its proportional share. This selects within the union and gives no bound on the signed cost of the removed sites.
* If the laws of \(\sqrt p\,D\) under \(\nu\) are uniformly integrable and \(\liminf\sqrt p|\mathbb E_\nu D|>0\), **every** deletion of a vanishing fraction from a macroscopic union preserves its sign and changes its price by \(o_{\mathbb P}(1)\). For each fixed \(T\), the removed price in modulus is at most \(T\#\mathrm{removed}/p\) plus the full empirical sum of \((|D_z|-T/\sqrt p)_+/\sqrt p\). This hinge is 1-Lipschitz, so (4) replaces the latter by \(N\mathbb E_\nu[(|\sqrt pD|-T)_+]/p+o_{\mathbb P}(1)\). First take \(p\to\infty\), then \(T\to\infty\). The intervening non-uniformly-integrable cases with bounded first moments retain the exact quantile test (6).

At half retention (6) has the particularly simple product endpoints \(N(\mathbb E_\nu D\pm\operatorname{MAD}_\nu(D))/(2\sqrt p)\), up to (4) and rounding \(O(d/\sqrt p)\), with \(\operatorname{MAD}(Z)=\min_c\mathbb E|Z-c|\) the **mean** absolute deviation from a median. Independence gives \(\operatorname{MAD}(D)\ge\max(\operatorname{MAD}_{D_+}(X),\operatorname{MAD}_{D_-}(Y))\) by conditioning. A preselected cloud gives a deterministic sector test with arbitrary cardinality. For \(P(x)=\sum_{j\in J}q_j^e\overline{j(x)}/S,\ S^2=\sum_J(q_j^e)^2>0\), \(0\notin J\), put \(P_+=\mathbb E_{D_+}P,\ B_+=\max_{D_+}|P-P_+|\). If \(B_+>0\), then
\[
 \operatorname{MAD}_\nu(D)\ \ge\
 {\,|nS-P(1)-(na-1)P_+|\over |D_+| B_+}.                              \tag{7}
\]
Test \(X-c\) by \(P-P_+\) and use Fourier orthogonality, the strict sector, and \(X(1)=1\). The minus analogue holds independently. In particular an origin spike in \(P\) incurs its exact signed correction in (7). The unrestricted quantiles in (6) continue to see the entire frequency population when both such cloud estimates are weak.

For the genuine subfield optimizers over \(\mathbb F_{s^2}\) and nonzero subfield probes, every actual match has \(D_z=2/(s+1)>0\), so its within-bin width in (1) is zero. In the independent sector product law \(X=1\) on the \(s-2\) strict subfield sites and \(X=0\) elsewhere, while \(Y=2/(s+1)\). Thus its median width is \((s-2)/|D_+|\sim4/s\) and its mean is asymptotic to \(-2/s\). Independent-product half prices straddle zero whereas every nonempty retained subfield selection has positive price. This checks why one cannot replace the prime probe family in (4) by probes confined to the subfield. [Genuine square pair and affine matches](astra-affine-90.md#subfield-obstruction-and-finite-checks)

## Finite checks and the next two tests

The [Arb384 replay](astra-price-92-check.py) reconstructs genuine pairs at \(53,257,409\), with feasible odd minus perturbations at \(257,409\). At \(53\) it enumerates all \(26^2\) independent square dilations for a nonlinear strict joint threshold and checks its measured variance against the exact two-coordinate Fourier sum. It outward-encloses all product quantiles, half-price endpoints and cloud bounds in (7), and checks the finite \(W_1\) comparison for the observed bins. At \(257\) the product half-price interval per site is approximately \([-0.04477331,0.06687204]\); for probes \((2,3)\) the two actual bins have three sites each, and retaining one in each has minimum total price between \(0.001657339\) and \(0.001657340\). At \(409\) the observed six-mode cloud certifies a summed median width above \(0.029099299\), using the best of four cap values per bin in the exact clipped inequality. The intact price is below \(0.029080868\), so there is an exactly balanced fractional half-selection. The actual floor-half total price ranges from about \(-0.01328634\) to \(0.03635531\). Among all 210 such ordinary selections the smallest absolute price lies between \(0.000004762\) and \(0.000004763\). These are finite checks of the identities. [Outward data](astra-price-92-checks.jsonl)

1. On the original short primes, measure the joint excess in (3) on an actual macroscopic third coset for preselected medium modes. If it is too large, (2) determines the deficit any improved bounded clipping estimate must pay. To use a resulting half-selection for the intact gap one also needs a signed comparison on its complementary sites.
2. On fixed-gap candidate faces, test the scaled independent-sector product quantiles against uniform integrability, including their contribution from rare positional values. Equation (6) decides even adaptive vanishing-density deletion on the longer prime draws. Transferring that nonlinear comparison to the original polylogarithmic draws or controlling the price on the entire third coset would require further input. The ordinary all-prime theta limit remains open.
