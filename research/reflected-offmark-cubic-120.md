# The reflected reciprocal cubic with its output mark removed

Work on the actual reflected orbit \(P|b|\) of [Round 119](reflected-slack-repair-119.md), with fixed floor and cap and its critical cap-rate persistent marked obstruction. Use \(q=h_j+h_{j+1}\) at the chosen four-step block, \(u=\epsilon Kq\), \(A_q=u(0)\), \(m=\mathbb E_n q\), and the **normalized** true stationary rows \(g=f_\epsilon/\sqrt n\), \(g_-=f_{-\epsilon}/\sqrt n\), \(\mu=\mathbb E_n g=\mathbb E_n g_-\). The true laws \(\omega,\omega^-\) use these rows, and \(\pi=q/(nm)\). Means use denominator \(n\), even when one coordinate is removed.

The actual \(q\) is nonnegative, has bounded amplitude and zero input at the mark. Its mean and squared second norm are comparable to \(n^{-1/2}\), and \(\|u-q\|_{2,n}=O(n^{-1/2})\). Its normalized favored pairing obeys \(\mathbb E_n(qg)\asymp n^{-1/2}\), by persistent pairing and bounded \(g\). For the opposite pairing use \(2\Pi_- q=q-u-m\mathbf1\), where \(\Pi_-\) is the centered opposite projection. Thus \(\|\Pi_-q\|_{2,n}=O(n^{-1/2})\) and \(\mathbb E_n(qg_-)=O(n^{-3/4})\), by the exact opposite sector and \(\|g_-\|_{2,n}=O(n^{-1/4})\). These facts verify the collision assumptions of [Round 116](paired-legendre-cubic-116.md) for \(q\); no new collision hypothesis is needed. In the unscaled factors the same favored pairing is of order one.

Write \(k=\lambda/\sqrt p\), \(w_q=qg/(n\mathbb E_n(qg))\), and \(\mathcal L_q=\sum_{x,y}\omega^-_x w_q(y)k(x-y)^2\). The domination \(w_q\le C\omega\) holds with \(C=\|q\|_\infty\mu/\mathbb E_n(qg)=O(1)\). The true all-translate uniformity and arcsine argument of Round 116 therefore give \(\mathcal L_q\gtrsim1\) along the actual prime subsequence. The full signed distinct cubic satisfies
\[
 n M_q^{\rm dist}=p\mu\mathbb E_n(qg)\,\mathcal L_q-(1-t/n)A_q+O(n^{-1/4}).        \tag{1}
\]
The original \(A_q\) term comes from the exceptional reciprocal product \(gg_-\) at the output mark. The leading equal-input pair removes a different constant baseline. In particular a lower for \(\mathcal L_q\) alone does not control \(A_q\).

## A positive distinct lower with no transported-mark hypothesis

Define \(T_3^{\circ\mathrm{out}}(a,b,c)=\mathbb E_n[1_{\{x\ne0\}} k(x-a)k(x-b)k(x-c)]\), and let \(M_q^{\rm dist,\circ\mathrm{out}}\) be the signed distinct expansion using this kernel and the three **full** input laws. The actual stationary identity at zero gives
\[
 (Kg)(0)(Kg_-)(0)=\mu(g(0)+g_-(0))-\mu^2-1=-1+O(n^{-1/2}).
\]
Indeed \(g(0)g_-(0)=1\); both marked factors stay bounded. Removing the output mark from the full moment therefore adds \(A_q/n+O(n^{-3/2})\), since \(|A_q|\le\sqrt p\,m=O(1)\). Passing to the distinct difference changes this addition by \(O(n^{-3/2})\). The mass of any input collision is \(O(n^{-1/2})\), and a single output summand in the kernel costs at most \(1/n\) by \(|k|\le1\). The scalar prefactor \(\epsilon(\sqrt p)^3 m\mu^2\) is bounded. Combining with (1) yields
\[
 \boxed{\quad n M_q^{\rm dist,\circ\mathrm{out}}=p\mu\mathbb E_n(qg)\,\mathcal L_q+O(n^{-1/4})\gtrsim1.\quad}      \tag{2}
\]
This is a necessary lower on the actual reflected obstruction without assuming \(A_q\to0\) or either small trimmed moment. A prime-uniform one-sided \(o(n^{-1})\) upper for the indicated masked-output signed cubic would therefore exclude this obstruction at the stated critical cap rate. Deleting the output mark does not discard the input singleton of the opposite true factor; that term is still part of the required prime estimate.

## Separating the opposite input after masking the output

Write \(z=\epsilon k\), \(c_-=g_-(0)\sqrt p/n\), \(\beta_*=c_-/\mu\), and let \(\mathcal T_q\) be the restricted weighted Legendre trace in Round 116 with \(w_q\). In the opposite input singleton, substitution of \(K(g_-(0)1_{\{0\}})=c_- k\) and the genuine favored sector gives \(c_-\mathbb E_n(qgz)+O(n^{-5/4})\). The estimates are the same as for Round 116: replacing \(u\) by \(q\) costs \(c_-\|u-q\|_{2,n}\|g\|_{2,n}\), the mean term costs \(O(n^{-3/2})\), and that input singleton's removed collisions cost \(O(n^{-3/2})\). Removing the output at zero from this singleton costs \(O(n^{-2})\): it has \(O(n^{-1/2})\) input mass, and its single output summand includes \(k(0)=-1/\sqrt p\) as well as the factor \(1/n\). The favored input singleton is \(O(n^{-5/4})\), using \(\mathbb E_n|uKg_-|=O(n^{-3/4})\); the repair input mark is zero.

Thus the part with all inputs and the output unmarked obeys
\[
 n M_q^{\rm dist,\circ\mathrm{out},\circ\mathrm{in}}
 = n\mu\mathbb E_n(qg)\big[1-\mathcal T_q-\beta_*\mathbb E_{w_q}z\big]+O(n^{-1/4}).
\]
This identifies what must be controlled jointly with the actual input singleton. In particular the strict upper margin for \(\mathcal T_q\) does not imply a sign for the all-unmarked piece, and a small all-unmarked sum is insufficient in isolation. The rate-free weighted overshoot and common cold domain are separate open routes.

## A whole late slab and the actual marked drift

There is also a source from a complete late slab, without selecting a low-loss index. Let \([i,i+L)\) lie in the genuine marked window of Round 119, with \(i\ge1\) and \(L\asymp\sqrt n\), and put \(\bar h=L^{-1}\sum_{j=i}^{i+L-1}h_j\). All rows in that interval have zero input at the mark. The bound \(h_j\le(\epsilon Kh_{j-1})_+\), the entry bound and \(\sum m_j^2\le\alpha\) give \(\|\bar h\|_\infty\le\sqrt{p\alpha/L}=O(1)\). Its critical mean and second norm follow from the true positive pairing along the whole window, Cauchy–Schwarz and \(\|h_j\|_{2,n}^2\le\alpha\). Also
\[
 \epsilon K\bar h-\bar h
   = L^{-1}\sum_{j=i}^{i+L-1}(\epsilon Kh_j-h_{j+1})+(h_{i+L}-h_i)/L.
\]
The first term costs \(O(\sqrt{\alpha/L})\) in normalized second norm by the dissipation. The last costs \(O(\sqrt\alpha/L)\). Thus the same actual-input estimates apply to \(\bar h\), and (2) holds for its genuine output-masked distinct cubic as well.

For its full distinct cubic the output term has an exact dynamical meaning. At the actual marked coordinate the update has \(b^{j+1}(0)-b^j(0)=m_j-(\epsilon Kh_j)(0)\), since \(h_j(0)=0\). Hence \((\epsilon K\bar h)(0)=L^{-1}[\sum_{j=i}^{i+L-1}m_j+b^i(0)-b^{i+L}(0)]\). This gives the full signed relation
\[
 n M_{\bar h}^{\rm dist}+\frac{b^i(0)-b^{i+L}(0)}{L}
     =p\mu\mathbb E_n(\bar h g)\,\mathcal L_{\bar h}+O(n^{-1/4})\gtrsim1,
\]
where the mean term divided by \(L\) is \(O(n^{-1/2})\). Therefore a small full distinct cubic on a genuine long slab would force a fixed macroscopic marked decrease across that slab. Control of that decrease is an independent issue; the formula does not rule it out during repair.

## Exact favored projection at subcritical cost

Let \(q_*=q-\Pi_-q\) and keep the original normalization \(\pi_*=q_* /(nm)\). It is signed in general and has exact mass one. The fully input-inclusive output-masked distinct moment changes by \(O(n^{-5/4})\) on replacing \(q\) by \(q_*\). To check this, write \(d_q=q-q_*\). It has \(\|d_q\|_{2,n}=O(n^{-1/2})\), \(\|d_q\|_\infty=O(1)\). The exact reciprocal product off the marked coordinate gives \(\|1_{\{x\ne0\}}(Kg)(Kg_-)\|_{2,n}=O(n^{-3/4})\), using the normalized factor norms and \(\mu=O(n^{-1/2})\). Thus the unrestricted masked moment in the difference is \(O(n^{-5/4})\). Each collision of the difference input with either true factor has mass \(O(n^{-3/4})\) in absolute value by Cauchy–Schwarz and the critical normalizations. The two true factors' collision has mass \(O(n^{-1})\), and the signed difference law has bounded absolute total mass. The two-equal Katz bound remains \(O(p^{-1/2})\) after output deletion; three-equal mass is at most \(O(n^{-5/4})\) by the true factor maximum and one of the difference/factor collision bounds. This proves the stated replacement error. The same argument applies to the actual whole-slab source.

The new projected source has exact favored positional support plus constants. To exploit the true pair's uniform difference, define \(\xi_d(b)=n\omega_b\omega^-_{b+d}\), a probability for every \(d\). For an unmasked translated Jacobi triple set \(e=a-b\), \(d=c-b\). The exact conditional shifted source is \(\sum_b\xi_d(b)\pi_*(b+e)\) and the untranslated kernel is \(T_3(e,0,d)\), restricted by \(d\ne0\), \(e\ne0,d\). For the masked kernel one must also subtract \(k(-b-e)k(-b)k(-b-d)/n\) *inside* this conditional sum. Its total can be critical. The desired next estimate acts on this actual conditional law and the full masked kernel, with two exact favored inputs and one exact opposite input. The uniformity of \(d\) alone gives no sign estimate.
