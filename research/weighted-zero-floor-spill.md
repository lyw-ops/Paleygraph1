# The zero-floor cap spill and the stationary-weighted excess

Fix \(M=10\), \(p=2n+1\equiv1\pmod4\) prime and real bulk floor \(0\le t\le1\). Use the actual capped equation of [Round 102](real-amplitude-cap-102.md) and the two true stationary weights of [Round 117](weighted-adjusted-cap-117.md). All means and vector norms below use divisor \(n\). The marked coordinate of the floor row is \(n\) at every \(t\), including zero.

For the capped row \(U_t=K a_t\), let

\[
 C_t=C_M(U_t),\quad a_t=\Phi_t(C_t),\quad h_t=U_t-C_t,\quad
 \mu_t=\mathbb E_n a_t,\quad \nu_t=2\sqrt{1+t-t/n},\qquad
 \alpha_t=\nu_t^2-\mu_t^2=\|h_t\|_{2,n}^2+2M\|h_t\|_{1,n}.
\]

For \(t>0\), use \(T_\epsilon,S_\epsilon,d_\epsilon,\ell_\epsilon\) of Round 117, with \(A=\sqrt{M^2+4t}\) the bulk spill threshold. Write \(w_\epsilon=(\epsilon Y)_+\) for the unscaled true stationary weight in the question, and \(B_\epsilon=\mathbb E_n(w_\epsilon S_\epsilon)\).

## An exact comparison with zero floor

At each finite prime the zero-floor capped map has a fixed point. For example, positive-floor fixed points lie in the common finite-dimensional ball \(\|U_t\|_{2,n}\le\sqrt{M^2+8}\) since \(\|K\|_{2\to2}\le1\) and \(\mathbb E_n a_t^2\le M^2+8\). A convergent subsequence as \(t\downarrow0\) gives a fixed point by continuity. The actual signed spill and activation mean are independent of the choice of zero-floor fixed point.

To see this, compare any two capped fixed points at \(s,t\in[0,1]\). Write \(c_t(i)=C_M(U_t(i))\). Off the mark, the reverse triangle inequality for the pair \((c_t(i),2\sqrt t)\) gives

\[
 |a_t(i)-a_s(i)|^2\le |c_t(i)-c_s(i)|^2+4(\sqrt t-\sqrt s)^2.
\]

At the mark the common second component is \(2\sqrt n\), so the floor term is zero. Both \(u\mapsto C_M(u)\) and \(u\mapsto u-C_M(u)\) are nondecreasing. Their differences therefore have nonnegative product, and the squared differences of these two parts sum to at most \(|U_t(i)-U_s(i)|^2\). Since \(K^2=I-J\), where \(J\) is averaging, the fixed-point identity also gives
\(\|a_t-a_s\|_{2,n}^2=\|U_t-U_s\|_{2,n}^2+(\mu_t-\mu_s)^2\). Thus

\[
 \boxed{(\mu_t-\mu_s)^2+\|h_t-h_s\|_{2,n}^2
 \le 4(1-1/n)(\sqrt t-\sqrt s)^2.} \tag{1}
\]

Taking \(s=t=0\) for two fixed points proves uniqueness of the mean and spill. Taking \(s=0\) gives \(\alpha_t=\alpha_0+O(\sqrt t)\) uniformly in the prime, since \(\nu_t^2-\nu_0^2=4t(1-1/n)\) and \(\mu_t\le2\sqrt2\). For the genuine nonnegative spill \(T_\epsilon\), the bulk entries are \((\epsilon U_t-A)_+\), and the marked entry is zero at every sufficiently large prime for fixed positive \(t\). Consequently \(\|T_\epsilon\|_{2,n}\le \|h_t\|_{2,n}\le \|h_0\|_{2,n}+2\sqrt t\). One can also compare \(T_\epsilon\) with the bulk-masked \((\epsilon h_0)_+\) in normalized second norm, at cost at most \(2\sqrt t+2t/M\), using \(A-M\le 2t/M\).

## The weighted claim forces the zero-floor defect to vanish

Fix \(0<t\le1\) before the prime limit. Set \(D_p(t)=\max_\epsilon |2-d_\epsilon|\), so \(D_p(t)\to0\) by the fixed-cap marked limit of Round 102. Put \(W_\epsilon=\mathbb E_n(f_\epsilon S_\epsilon)\). For all sufficiently large primes the genuine completed signed row \(V=z_+-\epsilon KT_\epsilon\) has \(V_0\ge\sqrt n(d_\epsilon-\ell_\epsilon)>0\). Exact opposite-sector orthogonality and \(V_+=V+S_\epsilon\) give

\[
 W_\epsilon\ge e^{\epsilon\gamma}(d_\epsilon-\ell_\epsilon)
     -\frac{\nu_t}{2}\big(\mu_t+\mathbb E_n T_\epsilon\big).
\]

Here \(f_{\epsilon,0}=\sqrt n\,e^{\epsilon\gamma}\). Choose the sign \(\epsilon_*\) with \(e^{\epsilon_*\gamma}=e^{|\gamma|}\). The sign may depend on \(p,t\). The actual spill and entry bounds of Round 108 give
\(\mathbb E_n T_{\epsilon_*}\le\alpha_t/(2A)\) and \(\ell_{\epsilon_*}\le\sqrt{p/n}\alpha_t/(2A)\). Also \(\mu_t=\nu_t-\alpha_t/(\nu_t+\mu_t)\) and \(d_{\epsilon_*}-\ell_{\epsilon_*}\ge3/2\) for large primes at each fixed floor, using \(\alpha_t\le4\), \(A\ge10\), and \(\sqrt{p/n}\le\sqrt3\). These yield

\[
 W_{\epsilon_*}\ge \frac32(e^{|\gamma|}-1)-D_p(t)-2t
   + \alpha_t\left(\frac{\nu_t}{2(\nu_t+\mu_t)}-rac{\nu_t}{4A}-\frac{\sqrt{p/n}}{2A}\right).
\]

The coefficient in parentheses is at least \(1/4-(\sqrt2+\sqrt3)/20>9/100\). Since \(S_{\epsilon,0}=0\) and \(f_\epsilon-w_\epsilon\le\sqrt t\) elsewhere, the correction from \(W_\epsilon\) to \(B_\epsilon\) is at most \(\sqrt t\mathbb E_n S_\epsilon\le\sqrt{t\alpha_t}/2\). This last estimate uses \(S_\epsilon\le(\epsilon KT_\epsilon)_+\), mean zero of \(KT_\epsilon\), and \(\|T_\epsilon\|_{2,n}\le\sqrt{\alpha_t}\). Young's inequality in the form \(\sqrt{t\alpha_t}/2\le (9/200)\alpha_t+(25/18)t\) proves

\[
 \boxed{\max_\epsilon B_\epsilon\ge \frac32(e^{|\gamma|}-1)
       +\frac9{200}\alpha_t-\frac{61}{18}t-D_p(t).} \tag{2}
\]

In particular, vanishing of the requested double limit along any sequence of fixed floors implies \(\alpha_0(p)\to0\) through primes, by (1) and (2). A positive \(\limsup_p\alpha_0(p)\) would disprove the proposed weighted bound at this fixed cap.

## A bounded-weight upper and the remaining tail

For each finite weight threshold \(L>0\), let \(B_{\epsilon,L}^{\mathrm{tail}}=\mathbb E_n[(w_\epsilon-L)_+S_\epsilon]\). The mean-zero transport estimate and (1) give the unconditional bound

\[
 0\le B_\epsilon-B_{\epsilon,L}^{\mathrm{tail}}
 \le \frac L2\|T_\epsilon\|_{2,n}
 \le L\sqrt t+\frac L2\|h_0\|_{2,n}. \tag{3}
\]

For qualitative vanishing the requested claim is equivalent to the conjunction of \(\alpha_0(p)\to0\) and vanishing of the same double limit for \(\max_\epsilon B_{\epsilon,L}^{\mathrm{tail}}\) at any one fixed \(L>0\). The \(O(\sqrt t)\) version is likewise equivalent to \(\alpha_0(p)\to0\) and the corresponding \(O(\sqrt t)\) tail bound after the prime limsup. These statements follow from (2), (3) and \(0\le B_{\epsilon,L}^{\mathrm{tail}}\le B_\epsilon\). Applying Cauchy–Schwarz to the tail with the available \(O(n^{1/4})\) second-norm bound on the true stationary weight loses a power of \(n\).

## A fixed-depth test of the zero-floor condition

Let \(F_0(W)=K\Phi_0(C_M(W))\), and form the genuine averaged zero-floor iterates \(W_0=0\) and \(W_{j+1}=(W_j+F_0(W_j))/2\). The map \(F_0\) is nonexpansive. Let \(B=\sqrt{M^2+4}\) so \(\|U_0\|_{2,n}\le B\) for any fixed point. The averaged-step norm identity gives
\(\|W_{j+1}-U_0\|_{2,n}^2\le\|W_j-U_0\|_{2,n}^2-\|F_0(W_j)-W_j\|_{2,n}^2/4\). The residual norms are nonincreasing because consecutive averaged-step distances are nonincreasing, so \(\|F_0(W_j)-W_j\|_{2,n}\le 2B/\sqrt{j+1}\).

For any trial \(W\), write \(r=F_0(W)-W\), \(h(W)=W-C_M(W)\), \(\mu(W)=\mathbb E_n\Phi_0(C_M(W))\). The proof of (1) at the common floor, retaining this exact residual, gives

\[
 (\mu(W)-\mu_0)^2+\|h(W)-h_0\|_{2,n}^2
 \le \|W-U_0\|_{2,n}^2-\|W-U_0+r\|_{2,n}^2
 \le 2\|W-U_0\|_{2,n}\|r\|_{2,n}.
\]

At \(W_j\) the distance to a fixed point is at most \(B\). In particular \(\|h(W_j)-h_0\|_{2,n}\le2B(j+1)^{-1/4}\) independently of the prime. This allows the zero-floor condition to be studied at fixed averaged depths before taking the field limit. The precise open test is

\[
 \lim_{j\to\infty}\limsup_{p\to\infty}\|(|W_{j,p}|-10)_+\|_{2,n}=0 .
\]

This condition is equivalent to \(\alpha_0(p)\to0\) by the uniform error and \(\alpha_0=\|h_0\|_{2,n}^2+2M\|h_0\|_{1,n}\). The zero-floor condition and the true stationary-weight tail bound remain open. The comparison uses the same fixed cap throughout, and none of the deductions require a critical cap rate.

As a check on the normalizations, the squared trial-row comparison was evaluated on 72 trial pairs at \(p=13,401,9413\), with both equal and unequal floors and with active clipping. Equation (2) was also checked on the 40 existing \(M=10\) sample pairs. These checks use floating point. The inequalities above follow from the finite identities and estimates in the derivation.
