# Reducing the mixed block to one frozen row

Write \(A_h=KD_h\), \(J=KD^{\mathrm J}\), and \(R_h=A_h-J\). All prices here are translated physical \(P_{5000}\), on the original closed square with the actual physical marked floors. The two rows \(h=601,602\) are the genuine Picard iterates.

## Price of changing the row

Let \(W=V_{602}-V_{601}\). The [second outgoing coordinate estimate](cold-actual-first-insertion-126.md#a-second-genuine-outgoing-counting-step) is obtained by transporting \(V_{601}-V_{600}\) by the first secant, in the unshifted packet price. The secant price is less than \(1.074\), and the input price is less than \(0.011\). Thus \(W\) has an unshifted representation of price less than \(0.011814\), eventually and uniformly on the square. Its absolute coefficient-dimension sum obeys the same bound and its fields have only the base pair. Both endpoint rows have absolute dimension budget below \(4.8\) by the physical [prefix and extra step](cold-resummed-136.md).

Apply the [telescoping difference calculation](cold-actual-first-insertion-126.md#uniform-word-cost-and-the-two-translated-columns) to \(d_{t_i}(V_{602,i})-d_{t_i}(V_{601,i})\), with \(\varepsilon=0.011814\), \(M=4.8\), and \(N=4(2031/128-2^{-17})\). In each analytic word use the endpoint representations of the other factors, so the bound \(M\) applies without adding \(\varepsilon\). The translated all-column estimate of that calculation charges \(2C_{\rm odd}(1)\), with actual marked floor and bad-lift corrections \(O_{5000}(\varepsilon n^{-1/2})\). The exact rational comparison is
\[
 \frac{36\varepsilon^2}{N(1-M^2/N)^5}< (0.0275)^2.
\]
Hence \(\|A_{602}-A_{601}\|_{P_{5000}}<0.0275\) for all sufficiently large eligible primes on the closed square. The comparison is an exact inequality for the inherited physical envelope and analytic word bound. It uses no floating-point estimate or growing-height claim.

## Remaining signed estimates on the same row

The difference between the mixed pair and the height-601 anticommutator is \((A_{602}-A_{601})J\). Since \(\|J\|_{P_{5000}}<0.528\), this height correction costs less than \(0.01452\). Thus the mixed pair target \(0.277444\) follows from a strict uniform bound
\[
 \|R_{601}J+JR_{601}\|_{P_{5000}}<0.262924.
\]
Alternatively
\[
 A_{602}A_{601}-J^2=(A_{601}^2-J^2)+(A_{602}-A_{601})A_{601}.
\]
The last term costs less than \(0.02882\) by the [full height-601 price](cold-combined-height-130.md), so the full two-step \(0.721\) budget follows from \(\|A_{601}^2-J^2\|_{P_{5000}}<0.69218\). Both are sufficient fixed-row targets.

At the original two heights, before the outer \(K\), write \(E_h=D_h-D^{\mathrm J}\), \(\overline E=(E_{602}+E_{601})/2\), \(\Delta E=(E_{602}-E_{601})/2\). The exact mixed sum in brackets is
\[
 (\overline E K D^{\mathrm J}+D^{\mathrm J}K\overline E)
 +(\Delta E K D^{\mathrm J}-D^{\mathrm J}K\Delta E).
\]
The two displayed matrices are symmetric and skew-symmetric under transpose, respectively, even on the complex square. A cancellation between these two parts as matrices would force them both to vanish. This algebra alone gives no lower on the physical price. In particular, the small height correction reduces the question to actual same-row arithmetic, where the new bound is still open. The half-step and invariant-ball estimates remain separate.
