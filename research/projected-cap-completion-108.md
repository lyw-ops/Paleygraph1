# A direct opposite-sector completion with coordinatewise slack

An exact signed projection repairs the capped opposite factor once a one-sided **slack-adjusted** transport maximum is small. It gives a feasible ordinary Fourier-LP row directly. For large fixed caps, the normalized marked loss is uniformly small without a cap-defect rate.

Use the [mark-oriented cap notation](mark-oriented-overflow-107.md) at fixed \(t>0\) and \(M\ge2\), with \(U=Ka\), \(a=\Phi_t(C_M(U))\), \(\mu=\mathbb E_n a\), and \(\nu=2\sqrt{1+t-t/n}\). Here \(n\ge t\), \(A=\sqrt{M^2+4t}\), and \(\alpha=\nu^2-\mu^2\) is the actual real cap deficit. For \(\epsilon\in\{+1,-1\}\), put
\[
 z=a-\epsilon U,\qquad
 T_{\epsilon,i}=(\epsilon U_i-A)_+\ (i\ne0),\quad T_{\epsilon,0}=0.
\]
The bulk negative part of \(z\) is precisely \(T_\epsilon\). The actual marked cap limit at fixed \(t,M\) gives \(z_0/\sqrt n=d_\epsilon\to2\), so \(z_0>0\) eventually. Define the following quantities on those fields:
\[
 c_\epsilon=\max_i\big(\epsilon(KT_\epsilon)_i-(z_i)_+\big)_+,\qquad
 \ell_\epsilon=\frac{(\epsilon(KT_\epsilon)_0)_+}{\sqrt n}.
\]
In particular \(c_\epsilon\) only charges the transported excess that exceeds the available nonnegative slack at each coordinate.

The proposed completed row is
\[
 B_{-\epsilon}=z+T_\epsilon-\epsilon K T_\epsilon+c_\epsilon\mathbf1.
                                                                    \tag{1}
\]
It is nonnegative because \(z+T_\epsilon=z_+\). Its centered part is in the \(-\epsilon\) sector by the two exact calculations
\[
 Kz=-\epsilon(z-\mu\mathbf1),\qquad
 K(T_\epsilon-\epsilon K T_\epsilon)
   =-\epsilon(T_\epsilon-\epsilon K T_\epsilon
                     -(\mathbb E_n T_\epsilon)\mathbf1).
\]
The correction can change sign. The actual capped row is even in the frequency index by uniqueness and reflection invariance of the clipped map, and all the operations in (1) preserve evenness.

## Mean and mark of the feasible row

The bulk overflow defect gives \(\mathbb E_n T_\epsilon\le\alpha/(2A)\). Also \(\mu\ge2\sqrt t\), so \(0\le\alpha\le4(1-t/n)\). Because \(M\ge2\) gives \(A\ge\nu\), the deficit pays the entire added overflow mass:
\[
 \mathbb E_n B_{-\epsilon}=\mu+\mathbb E_n T_\epsilon+c_\epsilon
 \le\mu+\frac{\alpha}{\mu+\nu}+c_\epsilon=\nu+c_\epsilon .
\]
The normalized marked coordinate of (1) is at least \(d_\epsilon-\ell_\epsilon\). By the Jacobi entry bound,
\[
 \ell_\epsilon\le\sqrt{p/n}\,\mathbb E_n T_\epsilon
 \le \frac{2\sqrt{p/n}}{A}.
\]
Thus the lower marked bound is eventually positive for fixed \(M\ge2\). The ordinary Fourier-LP mark test and complementary product in [the Fourier notes](fourier.md) give
\[
 \frac{\theta_\epsilon}{\sqrt n}
      \le \frac{\nu+c_\epsilon}{d_\epsilon-\ell_\epsilon}.           \tag{2}
\]
Here \(\theta_+=\vartheta(\overline H)\), \(\theta_-=\vartheta(H)\), and the product is \(n\). One can also use \(\max\{c_\epsilon,(\epsilon(KT_\epsilon)_0)_+\}\) as the constant in (1); this makes the completed mark at least the original \(z_0\), and replaces the loss by that constant's mean cost.

In particular a sufficient full-target condition uses fixed pairs \(t_j\downarrow0\), \(M_j\ge2\), \(M_j\to\infty\), with
\[
 \lim_{j\to\infty}\limsup_{p\to\infty} c_\epsilon(t_j,M_j,p)=0
                \quad\text{for each sign }\epsilon .
\]
Indeed at each fixed pair \(d_\epsilon\to2\), while the marked loss is \(O(M_j^{-1})\) independently of the cap-defect rate. Apply (2) in the stated order and use the complementary product for the lower bound. The same proof would apply with bounded caps if both the adjusted transport and marked loss vanish in this two-limit sense. Full one-sided transport as in Round 107 bounds both quantities, but (1) can use positive coordinate slack and needs only a scaled marked loss if the mark is allowed to decrease slightly.

## A fixed cap that pays the entire potential marked loss

The mean estimate can absorb the marked loss even at a sufficiently large **fixed** cap. Suppose \(A\ge \nu+(\nu^2/2)\sqrt{p/n}\). Then
\[
 \frac{1+(\nu/2)\sqrt{p/n}}{2A}\le\frac1{2\nu}
                              \le \frac1{\mu+\nu}.
\]
Consequently \(\mu+\mathbb E_n T_\epsilon+(\nu/2)\ell_\epsilon\le \nu\): the two added terms are at most \(\alpha[1+(\nu/2)\sqrt{p/n}]/(2A)\), and \(\nu-\mu=\alpha/(\mu+\nu)\). Therefore the actual feasible mean is at most \(\nu(1-\ell_\epsilon/2)+c_\epsilon\), so (2) sharpens to
\[
 \frac{\theta_\epsilon}{\sqrt n}
 \le \frac{\nu}{2}
       +\frac{c_\epsilon+(\nu/2)(2-d_\epsilon)}{d_\epsilon-\ell_\epsilon}.
                                                                    \tag{3}
\]
For all fixed \(0<t\le1\), \(M=10\) gives the required inequality using \(\nu\le2\sqrt2\) and \(\sqrt{p/n}\le\sqrt3\). The denominator stays bounded below, by the fixed-cap mark limit and the marked-loss bound. Thus at that one fixed cap, vanishing of \(c_\epsilon\) alone gives \(\limsup_p \theta_\epsilon/\sqrt n\le\sqrt{1+t}\) at fixed \(t\). The same conclusion for both signs at a sequence of such \(t\downarrow0\) suffices for Problem 26. This version needs neither a cap-defect rate nor an additional normalized marked-loss estimate.

This is a sufficient construction on the actual capped row. The claimed through-primes upper on \(c_\epsilon\) remains open. The necessary redistribution result of Round 107 concerns mean-small corrections preserving the mark on specified obstructions. Equation (1) explicitly gives its own correction and its full mean and marked budgets.

1. Estimate the positive part of \(\epsilon K T_\epsilon-z_+\) directly, especially where the actual opposite factor has small slack. For the fixed cap \(M=10\) this single adjusted transport suffices at each \(0<t\le1\).
2. If using the prior exact \(\alpha_M\) estimates, compare the resulting cost to (2) with \(\ell_\epsilon\) bounded separately. At a fixed cold floor report only that floor's implication.
