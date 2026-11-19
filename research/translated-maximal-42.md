# A sharper maximal estimate for translated feasible tests

For the notation of the [round-42 concentrated witness proof](astra-witness-resume-42.md), the actual signed endpoint scores satisfy

\[
\frac1n\#\{x:\text{some integer }t\ge L\text{ has }Q_t(x)>\eta t\}
\ \ll\ \frac{W(1+\log(2/\eta))^2}{\eta^2 L},
\qquad 0<\eta\le1.                                               \tag{1}
\]

Here \(L\ge1\), \(0\le\tau\le1\) and the constant is absolute. This is uniform over the choice of a single nonnegative feasible probability whose translates are being tested. The exceptional set can depend on that probability.

Use the exact one-sided update from the concentrated-witness proof, \(m_{j+1}(x)\ge m_j(x)-2g_j\), and the orbit energy identity \(\sum_{j=0}^{N-1}g_j^2\le WN\). For \(L\le s\le2L\) let \(C_s=2\sum_{j=L+1}^{s}g_j\). Sort the integer times into bins by \(\lfloor 2C_s/(\eta L)\rfloor\), and select the last time in each nonempty bin. The bins may be skipped when the increment is large. This is harmless since \(C_{2L}\le2\sqrt{LW(2L+1)}\). The number \(J\) of samples is at most \(1+4\sqrt{3W}/\eta\). If \(Q_s(x)>\eta s\) at any time in the band, its last-bin time \(t\) obeys

\[
Q_t(x)\ge Q_s(x)-(C_t-C_s)>\eta L/2 .
\]

Thus the time grid adapts to the actual scalar mean and applies simultaneously at all spatial shifts.

For two times \(s\le t\), Jensen over the translates of the same probability and nonexpansiveness of the actual map give

\[
\|Q_t-Q_s\|_{L^2(x)}^2
\le\|v_{t+1}-v_{s+1}\|_2^2
\le\|v_{t-s}\|_2^2
\le4W(t-s).
\]

The first norm uses uniform probability on the translations. The other norms are counting norms. To bound the maximum on the grid, prepend time \(L\), and pad its list by repeating the final time until there are \(2^r+1\) entries, with \(r=\lceil\log_2 J\rceil\). For each path from the first entry to a grid entry use the binary decomposition of its index. It uses at most one dyadic interval per length. For any one fixed length, the corresponding grid-interval increments are across disjoint time intervals of total length at most \(L\). The \(L^2(x)\) norm of their pointwise maximum in absolute value is at most \(2\sqrt{WL}\), since its square is bounded by the sum of their squares. The same bound applies to the initial \(Q_L\). The triangle inequality now bounds the grid maximum norm by \(2(r+2)\sqrt{WL}\), including the full padded interval. Chebyshev at \(\eta L/2\) and summation over the dyadic time bands prove (1).

The proof uses only the two actual-orbit inequalities and holds on primes and eligible squares. It is a sharper empirical estimate at fixed or moving relative thresholds. The known square witness illustrates why an empirical upper bound can coexist with a large value at the distinguished root. In particular (1) supplies no prime uniform bound at that root or at the critical \(T^{1/3}\) scale.
