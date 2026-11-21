# Leading mixed rank-three square on the genuine Jacobi column

Keep the original closed cold square, true \(t_0=n\), and both lifts in the \(P_{5000}\) class. The actual fixed center \(W\) is the [Round 55 field](astra-rankthree-55.md#exact-feedback-and-arithmetic-weights), the average of the two rank-three positive traces and their duals. It satisfies \(K(C_1Y)=W+C_1/p\) exactly. In perverse coordinates the average of those pure traces has the common negative sign relative to \(W\). The identities below use the actual positive-trace normalization. Here \(S=s_n C_1\) and \(s_n=2\sqrt{p/n}\).

Define the two leading Taylor steps \(J_1=K\operatorname{diag}((S_i+\alpha Y_i)/(2\sqrt{t_i}))\) and \(W_1=K\operatorname{diag}(\beta W_i/(2\sqrt{t_i}))\). Their mixed square on the genuine seed column obeys
\[
 (J_1 W_1+W_1 J_1)C_1
 =\frac{\beta}{4t}\left[
 s_n\left(-G+\tfrac12 K(WY)\right)+\alpha\left(K(YF_4)+K(W^2)\right)
 \right]+O_{P_{5000}}(n^{-1/2}).
\]
First use bulk denominators throughout. Inside the outer \(K\), the two orders involve \((s_nC_1+\alpha Y)K(WC_1)\) and \(W K((s_nC_1+\alpha Y)C_1)\). The exact all-lift identities are \(K(WC_1)=F_4-D_4Ke_0\) with bounded \(D_4\), \(K(C_1^2)=Y/2-C_1/\sqrt p\), and \(K(C_1Y)=W+C_1/p\). In turn \(K(C_1 F_4)=-G+D_5Ke_0\) for bounded \(D_5\). This gives the signs and the factor \(1/2\). The feedback error terms have price \(O_{P_{5000}}(n^{-1/2})\) since \(Ke_0=(\sqrt p/n)C_1\) and the selected bounded-rank bulk action has bounded price. Both changes from bulk to physical marked denominators cost \(O_{P_{5000}}(n^{-1/2})\), as in the [marked two-step computation](cold-mixed-seed-column-141.md). [Exact rank-four feedback](rank-four-arithmetic-56.md) · [Exact \(G\) feedback](weighted-arithmetic-57.md#exact-lift-feedback-and-compact-moments)

## Different labels in the four selected families

Before outer activation, \(C_1F_4\) has a rank-four derived factor and no Legendre factor. \(YF_4\) has a rank-four factor and a nontrivial Legendre factor. \(WY\) has a rank-three and a nontrivial Legendre factor. \(W^2\) has constituents from the rank-three factors and determinant lines alone. These signatures follow in the inherited joint product of the rank-two, rank-three and rank-four derived groups and are preserved by both lift choices. The rank-one ordinary twist by \(\chi(1-a)\) on the lisse part is invertible, so it cannot identify different surviving simple generic objects from these four families. Punctual units at \(1\) are killed by \(K\). Thus there is no signed merging across the four families of this leading expression. This argument leaves open overlap with higher Taylor words or on other input columns. [Independent group tables](rank-four-arithmetic-56.md) · [Activation and rank rule](astra-feedback-52.md#reading-rank-from-two-mellin-characters)

For the outward canonical price, convolve the inherited symmetric measures of \(C_1,Y,W,F_4\) in the four displayed products. Activation preserves each pooled nonzero weight, and zero in the base pair has price zero. The [checker](cold-leading-W-square-151-check.py) uses the actual complex \(\alpha,\beta\) on the square and the inherited \(\pi\) price. It proves the finite positive price is strictly below \(0.061\) with eventual room for the marked and exceptional terms. Hence \(\|(J_1W_1+W_1J_1)C_1\|_{P_{5000}}<0.061\) uniformly on the original square along sufficiently large eligible primes. [Outward record](cold-leading-W-square-151-checks.jsonl)

This leading piece is fixed at both true heights. Its input is \(C_1\). The full \(W\)-linear signed square, other columns, other fixed centers, the genuine residual and the \(0.567184\) same-height threshold remain open.

## Two signed returns at the next order

Within the \(\alpha^0\) part of the \(W\)-linear mixed term, include the cubic term of \(d_t(S)\) and the quadratic term of \(d_t'(S)\). Put \(b=\beta s_n/(4t)\) and \(\kappa=s_n^2/(8t)\). On \(C_1\), the next-order contribution, up to the marked errors, is \(-b\kappa K\) applied to
\[
 C_1^3 K(WC_1)+3 C_1 K(WC_1^3)
 +W K(C_1^4)+3 W C_1^2 K(C_1^2).
\]
The factor 3 comes from differentiating the cubic. Use \(C_1^3=(3C_1+C_3)/4\), \(C_1^4=(3+4C_2+C_4)/8\), \(C_1^2=(1+C_2)/2\) and \(K1=0\). The first two terms contribute \(3 C_1 F_4\) before outer activation. The other two contribute \(5 WY/4\). These explicit repeated terms combine with the lowest-order \(\alpha^0\) pieces to give
\[
 b(1-3\kappa)\,K(C_1F_4)
 +b(1/2-5\kappa/4)\,K(WY).
\]
The remaining cubic terms have their original coefficients. Before multiplying by \(-b\kappa K\) they are \(C_3F_4/4,\ 3C_1K(WC_3)/4,\ WK(C_4)/8,\ 3WC_2Y/4\). They contain neither of the selected label families. In \(C_3F_4\) and \(WC_2Y\) the Jacobi shifts (\(\pm3\) or \(\pm2\), respectively) differ from the selected shifts (\(\pm1\) or zero). Matching the same independent derived standards with different shifts would force a nonzero power of the infinite-order Jacobi line to be trivial by taking determinants. The two full-list shifts of a rank-three \(W\) standard by \(\pm3\), using the Round 55 lists, have combined absolute sums 16 or 20. Thus each constituent of \(K(WC_3)\) has dimension 8 or 10, preserved by convolution with a Jacobi line, whereas the selected pre-activation dimensions are 4 and 6. The constituents of \(K(C_4)\) carry the independent \(Sp_4\) factors of [Round 59](two-node-groups-59.md), absent from the two selected input families. These checks concern only overlap with the two selected labels in these degrees.

The same outward check gives \(|1-3\kappa|<0.812\), \(|1-5\kappa/2|<0.844\), and eventual price less than \(0.051\) for the two merged packets on this column. Their reductions concern the actual complex coefficients and both physical lifts. The four remaining cubic terms, words with \(\alpha\), higher degrees and other input columns are separate obligations in the full signed square.
