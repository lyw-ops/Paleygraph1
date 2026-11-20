# Mark-oriented actual overflow from one stationary factor

At sufficiently small fixed real floor, a persistent true log mark forces genuine capped overflow in the sign of that mark. The signed location can be determined from an exact pairing with just the corresponding positive stationary factor. The argument also gives a one-sided sufficient test for the original theta limit along real floors tending to zero.

Use [the real cap notation](real-cap-exterior-103.md) at fixed \(t,M>0\), with \(a=\Phi_t(C_M(U))\), \(b=\Phi_t(Y)\), \(U=Ka\), \(Y=Kb\), \(\mu=\mathbb E_n a\), \(\nu=\mathbb E_n b\), \(\gamma=\operatorname{arsinh}(Y_0/(2\sqrt n))\), and \(\alpha=\nu^2-\mu^2\). Write \(A=\sqrt{M^2+4t}\) and for each sign \(\epsilon\) set
\[
 f_\epsilon=\frac{b+\epsilon Y}{2},\qquad
 T_{\epsilon,i}=
 \begin{cases}
  (\epsilon U_i-A)_+ & i\ne 0,\\
  0 & i=0 .
 \end{cases}
\]
The factor \(f_\epsilon\) is nonnegative with \(\mathbb E_n f_\epsilon=\nu/2\), \(f_{\epsilon,0}=\sqrt n\,e^{\epsilon\gamma}\), and \(Kf_\epsilon=\epsilon(f_\epsilon-\nu\mathbf1/2)\). The signed overflow from Round 103 is \(T_+-T_-\) eventually.

## One exact factor identity

Self-adjointness and \(U=Ka\) give
\[
 \mathbb E_n[f_\epsilon(a-\epsilon U)]
 =\mu\nu/2 .
\]
Off the mark \(a_i-\epsilon U_i\ge -T_{\epsilon,i}\), with equality wherever \(T_{\epsilon,i}>0\). At the mark let \(d_\epsilon=(a_0-\epsilon U_0)/\sqrt n\). Thus
\[
 \mathbb E_n[f_\epsilon T_\epsilon]
 \ge d_\epsilon e^{\epsilon\gamma}-\mu\nu/2 .                    \tag{1}
\]
This is finite and exact as an inequality. Along the prime limit at fixed \(t,M\), \(d_\epsilon\to2\) by the actual capped mark limit. The true \(e^{\epsilon\gamma}\) is bounded there by the Jacobi entry estimate \(|Y_0|\le\sqrt p\,\nu\).

For \(i\ne0\) one has \(0\le f_{\epsilon,i}-(\epsilon Y_i)_+\le\sqrt t\), since \(0\le b_i-|Y_i|\le2\sqrt t\). Also \(\mathbb E_n T_\epsilon\le\alpha/(2A)\) by the bulk defect on each overflow coordinate. The independent reviewer noted that
\[
 \frac{\mu\nu}{2}+\sqrt t\,\mathbb E_nT_\epsilon
 \le\frac{\nu^2}{2}+\frac{\alpha}{2}
         \left(\frac{\sqrt t}{A}-\frac{\nu}{\mu+\nu}\right)
 \le\frac{\nu^2}{2}.
\]
Here \(\sqrt t/A\le1/2\le\nu/(\mu+\nu)\). Combined with (1) this gives \(\mathbb E_n[T_\epsilon(\epsilon Y)_+]\ge d_\epsilon e^{\epsilon\gamma}-\nu^2/2\). Consequently if \(\epsilon\gamma\ge\delta>0\) along a subsequence, then
\[
 \liminf\mathbb E_n[T_\epsilon(\epsilon Y)_+]
       \ge 2(e^\delta-1-t).                                    \tag{2}
\]
Here \(\nu^2/2=2(1+t-t/n)\). When \(t<e^\delta-1\) the lower bound is positive. The pairing itself requires no cap-defect rate. Under the critical cap-defect rate, the bounded-overflow and high-source localization by the [Round 106 proof](overlapping-overflow-106.md) can start with the pairing in (2), already supported where \(\epsilon U>A\) and \(\epsilon Y>0\). The aligned overflow side and the associated nonnegative signed Rayleigh test can therefore be chosen with \(\epsilon=\operatorname{sgn}\gamma\). The other high-source side of the rectangle can still have either stationary sign. The coefficient \(2(e^\delta-1-t)\) comes from retaining the marked entry of the favored factor.

## One-sided transport version

The same eigen-sector identity gives
\[
 \mathbb E_n[f_\epsilon T_\epsilon]
 =\epsilon\,\mathbb E_n[f_\epsilon K T_\epsilon]
       +(\nu/2)\mathbb E_n T_\epsilon
 \le (\nu/2)\big(\kappa_\epsilon+\mathbb E_nT_\epsilon\big),
 \qquad \kappa_\epsilon=\max_i \epsilon(K T_\epsilon)_i.
\]
Together with (1) this yields
\[
 d_\epsilon e^{\epsilon\gamma}
 \le \frac{\mu\nu}{2}+\frac{\nu}{2}
             \big(\kappa_\epsilon+\mathbb E_nT_\epsilon\big).    \tag{3}
\]
For fixed \(M\ge2\) one has \(A\ge \nu\) and hence \(1/(2A)\le1/(\mu+\nu)\). It follows that
\[
 \frac{\mu\nu}{2}+\frac{\nu}{2}\mathbb E_nT_\epsilon
 \le\frac{\nu^2}{2}
       +\frac{\nu\alpha}{2}\left(\frac1{2A}-\frac1{\mu+\nu}\right)
 \le\frac{\nu^2}{2}.
\]
Thus vanishing of both \(\kappa_\epsilon\) alone suffices at each fixed real floor with such a cap to give \(\limsup|\gamma|\le\log(1+t)\). For \(0<M<2\), (3) also gives this implication if \(\alpha\to0\). Along a sequence of fixed real floors decreasing to zero, these estimates imply the original limit by the [ordinary theta smoothing bracket](smoothing.md). For a subsequential obstruction of specified sign at small \(t\), (1)–(3) require only the matching transported overflow. These through-primes transport estimates remain open.

## Necessary redistribution for an opposite-sector repair

The independent reviewer noted a direct application to positivity completion. The capped opposite factor \(f^c_{-\epsilon}=(a-\epsilon U)/2\) has centered part in the \(-\epsilon\) Jacobi sector and equals \(-T_\epsilon/2\) on the bulk overflow. Let a real correction \(w\) have centered part in that same sector and satisfy \(f^c_{-\epsilon}+w\ge0\). Orthogonality to the centered true \(f_\epsilon\) gives
\[
 \frac{\nu}{2}\mathbb E_n w+\mathbb E_n(f_\epsilon w_-)
 =\mathbb E_n(f_\epsilon w_+)
 \ge\frac12\mathbb E_n(f_\epsilon T_\epsilon)
 \ge \frac{d_\epsilon}{2}e^{\epsilon\gamma}-\frac{\mu\nu}{4}.   \tag{4}
\]
On the persistent marked-sign subsequence of (2), the last term has a fixed positive lower in the prime limit if \(t<e^\delta-1\). Thus a coordinatewise nonnegative completion costs order-one mean despite the small mean negative part of the capped factor at the critical scale. A signed mean-\(o(1)\) completion has to remove order-one \(f_\epsilon\)-weighted mass. In particular an upper \(w_-\le o(1)f_{-\epsilon}\) is incompatible with such a repair: the exact stationary product \(f_\epsilon f_{-\epsilon}=t_i\) makes its weighted cost \(o(1)\).

If in addition \(w_0=0\) and \(\|w_-\|_{2,n}\le D n^{-1/4}\) for fixed \(D\), this necessary removal uses order \(\sqrt n\) sites within an actual high set of \(f_\epsilon\). To see it, take \(H_\eta=\{i\ne0:f_{\epsilon,i}\ge\eta\sqrt n\}\) for small fixed \(\eta>0\). The weighted contribution from the remaining bulk is at most \(D\sqrt{\eta\nu/2}\) by Cauchy–Schwarz. The mark contributes zero. Hence \(\mathbb E_n(f_\epsilon w_-1_{H_\eta})\) is bounded below by a positive constant when \(\eta\) is sufficiently small. As \(\max f_\epsilon=O_t(\sqrt n)\), a second Cauchy–Schwarz bound gives \(|H_\eta\cap\{w_->0\}|\gtrsim\sqrt n\); the mean of \(f_\epsilon\) gives \(|H_\eta|=O(\sqrt n)\). These conclusions specify the forced negative redistribution for this constrained class. Signed repairs that meet this redistribution requirement remain unresolved.

1. In a proof by contradiction at small \(t\), test the genuine one-sign high stationary factor in the sector of the persistent mark. Preserve the actual aligned overflow subset and the required cap-defect rate.
2. Estimate the matching one-sided Jacobi transport or test whether a proposed signed positivity repair moves the necessary weighted mass while preserving the mark and mean. If working only at the cold diameter, retain its specific floor scope.
