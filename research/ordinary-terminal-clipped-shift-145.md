# Two exact reductions for positive ordinary near-root comparisons

Set \(n=(p-1)/2\) and retain the actual fixed-positive-floor, zero-start marked trajectory. Work at \(T=T(p)\to\infty\) with \(T+1\) in its simultaneous marked window. Use \(s=-\sigma\), \(g=g_T\), \(G=\sqrt n g\), \(M=M_T\), \(Z=X_{\sigma,T}/M\), and \(Z=U_\sigma-P_s g/(2TM)\) from the [approximate-sector test](ordinary-terminal-approximate-face-144.md). All expectations here use divisor \(n\).

## Mark-preserving clipping and the signed deleted tail

For any true ordinary optimizer \(F\) of sign \(s\) with root \(q_s\), choose \(L\ge0\), let \(D=1_{\rm bulk}(F-L)_+\), \(d=\mathbb ED\), and set
\[
 F'=F-D+\frac{dn}{n-1}1_{\rm bulk}.
\]
This nonnegative row has mean one and root \(q_s\). Its bulk part \(\lambda'=F'-q_s e_0\) has mean at most one and supremum at most \(L+2\). The actual bound \(\|G\|_{2,n}=O_\tau(\sqrt T)\) therefore gives
\[
 \frac{\mathbb E(\lambda'G)}{T}
 \le O_\tau\bigl(\sqrt{(L+2)/T}\bigr).
\]
Thus the cutoff may be any \(L=o(T)\), including fixed cutoffs. This uses the first mass of the clipped row in addition to its pointwise cap.

The projected score in the signed residual is
\[
 \Xi=Z-\mathbf1-\frac{P_\sigma g}{2TM}
     =U_\sigma-\mathbf1-\frac{g-\mathbb Eg}{2TM}\in V_\sigma .
\]
Since \(P_\sigma(F-\mathbf1)=0\), the exact residual of the clipped row in Round 144 is
\[
 \mathcal R_{F'}=-\mathbb E(D\Xi)-\frac{d}{n-1}\Xi_0.
\]
The second term uses \(\mathbb E\Xi=0\) and the exact restoration factor \(n/(n-1)\). In the actual marked window \(\Xi_0=O_\tau(\sqrt n)\) and is eventually positive. Indeed \(Z_0=a/M\gg_\tau\sqrt n\), while \((P_\sigma g)_0=(g_0-\mathbb Eg+\sigma(Kg)_0)/2\), so the second term of \(Z_0-1-(P_\sigma g)_0/(2TM)\) is \(O_\tau(1+\sqrt n\,T^{-B-1})\). This uses the true cancellation at \(T,T+1,1\), \(\mathbb Eg=O_\tau(\sqrt{T/n})\), and \(M\gg_\tau n^{-1/2}\). In particular the restoration contributes \(O_\tau(n^{-1/2})\) uniformly in \(F,L\).

Consequently a one-sided lower \(\mathbb E(D\Xi)\ge-o(1)\), for one true optimizer and a selectable growing marked time on each sign with some \(L=o(T)\), suffices to apply the clipped-row test. Conversely, if \(q_s/\sqrt n\ge1+\eta\) on a prime subsequence, fix \(\tau>0\) with \(\sqrt{1+\tau}<1+\eta\). On that subsequence every true optimizer and every such growing \(T,L\) must satisfy \(\mathbb E(D\Xi)\le-c_{\eta,\tau}\) eventually, because the clipped terminal cost is sublinear and the mark is untouched. For square order \(p=r^2\) in the field-size notation it gives the same control for the actual \(\sigma=-\) window, which tests \(s=+\), \(q_s=r-1\), at fixed \(0<	au<1\). An arithmetic upper on the magnitude of the negative part of the deleted-tail pairing on primes is still needed. In particular the sufficient bound is one-sided, rather than equality of the deleted-tail pairing to zero.

## Nonnegative convolution is equivalent to a selectable near-cap shift

For a fixed even true optimizer \(F\), let \(F_\mu=\sum_h\mu_h\tau_h F\) where \((\tau_hF)_i=F_{i+h}\) and \(\mu\) is an inversion-symmetric probability on the frequency group. This preserves Fourier-sector feasibility, nonnegativity and mean one. For each shift write
\[
 a_h=\frac{q_s-F_h}{\sqrt n},\qquad
 b_h=\frac{\mathbb E[1_{\rm bulk}(\tau_hF)G]}{T}.
\]
Both are nonnegative. The cap inequality \(F_h\le q_s\) follows by translation and, when needed, reflection, and \(G\ge0\) is the actual terminal activation. The normalized root loss and normalized terminal cost of \(F_\mu\) are exactly \(\sum_h\mu_h a_h\) and \(\sum_h\mu_h b_h\). The time and terminal mark do not move with the shift. Actual evenness of both \(F\) and \(G\) makes \(a_{-h}=a_h\) and \(b_{-h}=b_h\).

It follows that the feasible loss-cost pairs of such smoothing are precisely the convex hull of the pairs \((a_h,b_h)\). At a prescribed allowed root loss, a best convolution uses at most two symmetric shift orbits by the finite one-inequality linear program. More importantly, simultaneous \(o(1)\) in both coordinates is possible if and only if there is one shift \(h\) with \(a_h+b_h=o(1)\): take a support point minimizing the nonnegative sum, and use the symmetric probability on \(h,-h\) for the converse. A mixture with weight \(1-o(1)\) at zero retains at least \(1-o(1)\) of the original bulk cost. Exact sector feasibility and near-optimal root alone do not bound \(b_h\) at any near-cap shift. This reduction, like the clipping identity, leaves a prime-specific signed correlation to prove.
