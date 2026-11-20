# A complementary mask for the actual near-cap terminal frontier

Work at fixed positive floor \(\tau\) in the actual growing marked window, with \(T+1\) included. Write \(G=\sqrt n\,g_T\ge0\) for the true terminal activation and use normalized expectations. Let \(F,R\) be mean-one ordinary optimizers on opposite signs \(s,-s\), respectively, with \(F_0=q_s\), \(R_0=q_{-s}\), and \(q_s q_{-s}=n\). Both are nonnegative. Let \(\epsilon\ge0\) and let \(\mu\) be a probability supported on the frequency shifts \(h\) with \(F_h\ge q_s-\epsilon\sqrt n\). Use \((\tau_hF)_i=F_{i+h}\) and \(\bar F=\sum_h\mu_h\tau_hF\). One can take symmetric \(\mu\) and even \(F,R\) without changing the terminal loss or the selected mark.

The complementary overlap is fully quantified even on this near-optimal face:
\[
 \mathbb E[1_{\rm bulk}\bar F R]
 =1-\frac{\bar F_0 q_{-s}}{n}
 =\frac{(q_s-\mathbb E_\mu F_h)q_{-s}}{n}
 \le C\epsilon .                                               \tag{1}
\]
This follows from orthogonality of the two mean-zero sectors. It requires \(R\) to have the optimal opposite root. If its root were \(r\) instead, the corresponding expression would be \(1-\bar F_0 r/n\).

For \(c,\delta>0\) define the actual mask
\[
 S=\{i\ne0: G_i\ge cT,\ R_i\le \delta G_i/T\}.
\]
At a cutoff \(L\ge0\), put \(X^\circ_j=1_{\{j\ne0\}}(F_j-L)_+\) and \(X_\mu^\circ=\sum_h\mu_h\tau_h X^\circ\). Then uniformly in \(\mu,L,S\),
\[
 \frac{\mathbb E[1_{\rm bulk}\bar F G]}{T}
 \le c+\frac{C\epsilon}{\delta}+
 \frac{C_\tau}{\sqrt T}
 \left(\sqrt L+\|1_S X_\mu^\circ\|_{2,n}+\|\mu\|_{\ell^2}\right). \tag{2}
\]
On the low \(G\) part the normalized cost is at most \(c\), since \(\mathbb E\bar F=1\). On the remaining part outside \(S\) it is at most \(\mathbb E[1_{\rm bulk}\bar F R]/\delta\). This comparison imposes no upper pointwise cutoff on \(G\). On \(S\), convexity bounds \((\bar F-L)_+\) by the convolution of \((F-L)_+\) with \(\mu\). Its difference from \(X_\mu^\circ\) is the single original-root term \((q_s-L)_+\mu_{-i}\), whose normalized second norm is at most \(C\|\mu\|_{\ell^2}\). The clipped part \(\min(L,\bar F)\) has second norm at most \(\sqrt L\) since it is nonnegative of mean at most one. Cauchy–Schwarz with the actual \(\|G\|_{2,n}=O_\tau(\sqrt T)\) proves (2). In particular the original input root and the physical output root have both been excluded from the unknown statistic.

If a prime subsequence has \(q_s/\sqrt n\ge1+\eta\), fix \(\tau>0\) with \(\sqrt{1+\tau}<1+\eta\). This may be the larger sign selected at each prime. Let \(\epsilon=o(\delta)\), \(\delta\to0\), and \(L=o(T)\). Each of these positive shift mixtures is in the correct sector, has \(\bar F_0=q_s+o(\sqrt n)\), and therefore pays a fixed positive normalized terminal cost by [Round 144](ordinary-terminal-approximate-face-144.md). Take \(c>0\) smaller than a fixed fraction of that lower bound. Equation (2) then forces
\[
 \|1_S X_\mu^\circ\|_{2,n}^2\ge c_{\tau,\eta}'T                 \tag{3}
\]
eventually, for every such \(\mu,F,R\) and selected growing marked time. The mask has density \(O_\tau(1/(c^2T))\), and \(R/G\le\delta/T\) there. Conversely an \(o(T)\) upper on this exact masked collision, for such a choice of optimizer, opposite optimum and mixture, excludes the putative gap. This is a conditional reduction requiring an estimate on ordinary primes.

The squared norm in (3) is exactly
\[
 \sum_{h,h'}\mu_h\mu_{h'}\,
            \mathbb E[1_S X^\circ_{i+h}X^\circ_{i+h'}].
\]
Its equal-shift part is at most \(\|X^\circ\|_{2,n}^2\|\mu\|_{\ell^2}^2\le q_s\|\mu\|_{\ell^2}^2\), using \(X^\circ\le F\le q_s\) and \(\mathbb E F=1\). If \(\|\mu\|_{\ell^2}^2=o(T/\sqrt n)\), (3) forces an order \(T\) contribution from distinct shifts on the actual mask. This sharpens the location of the required interaction for a sufficiently diffuse shift law. It says nothing about the existence of a diffuse near-cap law when the cap is sparse. Unmasked additive difference bounds alone leave this score-dependent mask unpriced.

For the independent clipping route, \(D=1_{\rm bulk}(F-L)_+\) is supported where \(R=0\), exactly, by (1) at the zero shift. The wanted bound is a lower bound on \(\mathbb E(D\Xi)\) for one optimizer and time. A negative minimum over the face does not refute the route: rejecting all optimizer choices would require a negative upper bound on the maximum at the corresponding times and cutoffs. Its signed layer integral also starts at the exact cutoff \(L\), retaining the fractional first layer. These corrections leave the prime weighted sign estimate open. The square-order comparison in Round 145 uses fixed \(0<\tau<1\) with \(\sigma=-\) and tested \(s=+\); this gives the intended notation in that note.
