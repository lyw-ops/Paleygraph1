# Persistence of the actual negative repair on a marked obstruction

At the critical cap-defect rate, a persistent marked obstruction forces a window of order \(\sqrt n\) actual projected repair steps before positivity. Each negative row late in that window has critical effective support and is within \(O(n^{-1/2})\) in normalized second norm of the favored sector. There is also a separate small-constant condition at the critical cap rate that guarantees successful repair.

Use the [actual repair](iterated-sector-projection-108.md) \(b^0=z=a-\epsilon U\), \(h_j=(b^j)_-\), \(m_j=\mathbb E_n h_j\), \(b^{j+1}=b^j+P h_j\), with \(P=(I-\epsilon K+J_0)/2\). Work at fixed real \(t>0\) and fixed cap \(M\ge2\). Use the true factor \(f_\epsilon=(b+\epsilon Y)/2\) and \(\gamma\) of [the mark-oriented comparison](mark-oriented-overflow-107.md). In particular \(f_{\epsilon,0}=\sqrt n\,e^{\epsilon\gamma}\), \(\mathbb E_n f_\epsilon=\nu/2\), \(K f_\epsilon=\epsilon(f_\epsilon-\nu\mathbf1/2)\), and \(\max f_\epsilon=O_t(\sqrt n)\). Norms and pairings below are normalized.

## A persistent block at critical cap deficit

Suppose on a prime subsequence that
\[
 \alpha\le B/\sqrt n,\qquad \epsilon\gamma\ge\delta_0>0,
                         \qquad t<e^{\delta_0}-1
\]
for fixed constants. Then some \(c>0\) has the following properties on the entire integer block \(c\sqrt n\le j\le2c\sqrt n\):
\[
 \|h_j\|_{2,n}^2\asymp n^{-1/2},\quad
 m_j\asymp n^{-1/2},\quad
 1-\frac{\epsilon\langle h_j,K h_j\rangle_{2,n}}{\|h_j\|_{2,n}^2}
                       =O(n^{-1/2}).                             \tag{1}
\]
The constants may depend on the fixed parameters. All of these rows are actual repair iterates of that cap, and no primal conclusion follows without an estimate on the actual window.

To prove this, let \(s_j=\sum_{r<j}m_r\). The contraction inequality of the repair gives
\(\sum_{r<j}\|P h_r\|_{2,n}^2\le\|h_0\|_{2,n}^2\le\alpha\), and \(m_r\le\|P h_r\|_{2,n}\) because \(P\) keeps the constant row. Thus \(s_j\le\sqrt j\,\sqrt B n^{-1/4}\). For \(j\le2c\sqrt n\), an appropriately small \(c\) keeps that bound below a fixed small constant. Opposite-sector orthogonality and nonnegativity of \(f_\epsilon\) imply
\[
 \mathbb E_n(h_j f_\epsilon)
 \ge \frac{b^j_0 f_{\epsilon,0}}n-\frac{\nu}{2}\mathbb E_n b^j .
\]
Indeed \(\mathbb E_n(b^j f_\epsilon)=(\nu/2)\mathbb E_n b^j\), and the positive part of \(b^j\) has at least its marked contribution. By the exact mean and marked budgets of the repair, the right side is bounded below by
\[
 \left(d_\epsilon-\frac12\sqrt{p/n}\,s_j\right)e^{\epsilon\gamma}
                          -\frac{\nu}{2}(\mu+s_j).
\]
At zero cost the last lower bound has liminf at least \(2(e^{\delta_0}-1-t)>0\), using \(d_\epsilon\to2\) and \(\mu\le\nu\). Since \(e^{\epsilon\gamma}=O_t(1)\), choosing \(c\) sufficiently small preserves a fixed positive lower for every \(j\le2c\sqrt n\). The entry and mean bounds on \(f_\epsilon\) give \(\|f_\epsilon\|_{2,n}^2=O_t(\sqrt n)\). Hence Cauchy–Schwarz and the entry bound give \(\|h_j\|_{2,n}^2\gtrsim n^{-1/2}\) and \(m_j\gtrsim n^{-1/2}\).

The update \(b^{j+1}=P((b^j)_+)\) is nonexpansive. The displacement norms \(\|P h_j\|_{2,n}\) are therefore nonincreasing. Their summed square bound gives
\[
 \|P h_j\|_{2,n}^2\le B/(\sqrt n(j+1)).
\]
At \(j\ge c\sqrt n\) this supplies the upper for \(m_j\), while \(\|h_j\|_{2,n}^2\le\alpha\) supplies the other upper. The Rayleigh formula in the exact contraction test supplies the gap in (1).

In particular these rows have effective support \(n m_j^2/\|h_j\|_{2,n}^2\asymp\sqrt n\). Also \(h_j-\epsilon K h_j=2P h_j-m_j\mathbf1\), whose \(2,n\) norm is \(O(n^{-1/2})\). The coherence bound gives \(\|K h_j\|_\infty\le\sqrt p\,m_j=O(1)\). Cutting the amplitudes of \(h_j\) at a sufficiently large fixed value costs only \(O(n^{-1/2})\) in \(2,n\) norm, because the positive excess is pointwise dominated by \(|h_j-\epsilon K h_j|\) there. At a small fixed lower amplitude \(\eta>0\), the discarded \(2,n\) mass squared is at most \(\eta m_j=O(\eta/\sqrt n)\), and the retained support has size \(O(\sqrt n/\eta)\). Thus the needed arithmetic improvement concerns genuine persistent near-eigenrows of one sign, not arbitrary weighted cuts.

## A sufficient small-constant cap deficit

This width bootstrap was suggested by the Round 108 independent reviewer. Fix \(0<\eta_0<1\), \(q=\sqrt{(1+\eta_0)/2}\), \(0<s<A-M\), and \(L_s=(A-s)^2-M^2>0\) with \(A=\sqrt{M^2+4t}\). The mark of \(z\) exceeds \(s\) eventually. On the bulk, \(z_i\le s\) implies \(\epsilon U_i\ge A-s>M\); the minimum of \(a_i-\epsilon U_i\) on \(|U_i|\le M\) is \(A-M\). The cap-defect count gives \(|\{z\le s\}|\le n\alpha/L_s\).

Up through any step reached by the width bound \(\sqrt p\,m_j^2\le\eta_0\|h_j\|_{2,n}^2\), the geometric norm decrease in the repair gives \(\|b^j-z\|_{2,n}\le\sqrt{\alpha}/(1-q)\). Any negative site of \(b^j\) with \(z_i>s\) pays at least \(s^2\) in counting squared difference. Consequently
\[
 |\operatorname{supp}h_j|\le
       n\alpha\big[L_s^{-1}+s^{-2}(1-q)^{-2}\big].
\]
If \(\sqrt p\,\alpha [L_s^{-1}+s^{-2}(1-q)^{-2}]\le\eta_0\) eventually, this support bound implies the width bound at that step by Cauchy–Schwarz. Induction, beginning at \(b^0=z\), gives it throughout, for either sign. The fixed-floor upper then follows by the previous repair theorem. This uses an explicit small **constant** at the critical cap rate and leaves the required estimate of that constant open.

1. Look for a prime-specific obstruction to the actual persistent near-eigenrow window (1), using the alternating cone/sector origin of consecutive rows and the true favored factor.
2. Try to prove the explicit small-critical-constant estimate on actual capped spill or the sharp inner excess. This would close the fixed-floor repair by induction.
