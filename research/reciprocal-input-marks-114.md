# Input marks in the reciprocal mixed moments

Use the actual late source and the notation of [Round 113](reciprocal-repair-moments-113.md). Write \(g^\circ=g-g(0)1_{\{0\}}\), \(g_-^\circ=g_--g_-(0)1_{\{0\}}\), \(c_-=g_-(0)\sqrt p/n\), and \(z=\epsilon k\). For \(P\) in the class of (1) of Round 113, let \(M(P)=\mathbb E_n[P(u)(Kg)(Kg_-)]\) and \(M^\circ(P)=\mathbb E_n[P(u)(Kg^\circ)(Kg_-^\circ)]\). The input mark of \(h\) is already zero. The true output value \(A=u(0)\) is unaffected by this deletion.

The precise difference is
\[
 M(P)-M^\circ(P)=c_-\mathbb E_n[P(h)g z]+O_P(n^{-5/4}).          \tag{1}
\]
Indeed the complete opposite-mark term is \(c_-\mathbb E_n[P(u)(Kg)k]\). Inserting \(Kg=\epsilon(g-\mu)\) and replacing \(P(u)\) by \(P(h)\) gives (1) up to the contribution from the favored input mark paired with the trimmed opposite factor. That latter term is \(O(n^{-1/2})\mathbb E_n|P(u)Kg_-^\circ|\). The bound \(P(u)=O(|Kh|^2)\), the uniform bound on \(Kh\), and \(\mathbb E_n|Kh Kg_-|=O(n^{-3/4})\) show it is \(O_P(n^{-5/4})\). The additional trimmed-column error uses \(\|Kg_- - Kg_-^\circ\|_\infty=O(n^{-1/2})\) and \(\mathbb E_n|P(u)|=O_P(n^{-1/2})\). The discarded mean in the opposite-mark term costs \(O(n^{-3/2})\).

The signed collision bound of Round 113 holds for both the full and the trimmed expressions, with the original normalization of the laws. Replacing either law by a subprobability only decreases pair and intersection masses. The remaining transformed product bounds persist since each deleted column has supremum norm \(O(n^{-1/2})\), \(\mathbb E_n |Kg|+\mathbb E_n|Kg_-|=O(n^{-1/2})\), and \(\mathbb E_n|Kh|=O(n^{-1/2})\) by the full-source approximation. Thus (1) also identifies the critical contribution of input marks to the distinct expansion, with error smaller than \(n^{-1}\).

Together with the earlier exact product this gives
\[
 M^\circ(P)=\mathbb E_n[P(h)g(\mu-c_- z)]-\frac{1-t/n}{n}P(A)+O_P(n^{-5/4}).
\]
The sign of the coefficient \(\mu-c_-z\) is not guaranteed by the entry bound. The genuinely anchored weighted mean \(\mathbb E_n[P(h)g z]\) needs a through-primes sign or size estimate, unless one combines it with the unmarked expression directly.

## A signed test using the unmarked factor inputs

Suppose additionally \(0<t\le1/4\). This is a scope restriction on the following test; (1) used the original fixed-floor hypotheses. Set \(\beta_*=c_-/\mu\), \(W=1-\beta_* z\), and \(q=\sqrt n\mu\). Here \(0<c\le\beta_*\le3/2\) for all large primes, since \(g_-(0)=e^{-\epsilon\gamma}\) and \(\epsilon\gamma\ge\delta_0>0\) on the marked obstruction, with \(|\gamma|\) bounded. For any uniformly bounded real multiplier \(s\) define \(M_s^\circ(P)=\mathbb E_n[sP(u)(Kg^\circ)(Kg_-^\circ)]\). The exact product gives
\[
 nM_s^\circ(P)=q^2\mathbb E_\omega[sP(h)W]-(1-t/n)s(0)P(A)+O_{P,\|s\|_\infty}(n^{-1/4}).          \tag{2}
\]
Indeed, put \(c_+=g(0)\sqrt p/n\). Expanding the trimmed transforms gives the exact pointwise terms
\[
 (Kg^\circ)(Kg_-^\circ)
 =-gg_-+g(\mu-c_-z)+g_-(\mu+c_+z)-(\mu+c_+z)(\mu-c_-z).
\]
Use \(\mathbb E_n|P(u)-P(h)|=O(n^{-3/4})\), \(\mathbb E_n|P(h)|g_-=O(n^{-3/4})\), and the \(O(n^{-1/2})\) size of \(\mu,c_+,c_-\). The quadratic coefficient and the non-exceptional part of \(-gg_-\) cost \(O(n^{-3/2})\) before rescaling. The exceptional part is kept exactly.

The entire positive part of the signed measure in (2) has mass bounded away from one. In fact stationarity implies \(\mathbb E_n(gz)=(g(0)-\mu)/\sqrt p\), and \(g(0)g_-(0)=1\), so
\[
 q^2\mathbb E_\omega W = q^2-1+\mu g_-(0).
\]
Since \(W_-\le (\beta_*-1)_+\le1/2\), this gives \(q^2\mathbb E_\omega W_+\le t+(1+t)/2+o(1)\le 7/8+o(1)\). This uses only the true mark and factor mean, without selecting a high set.

Let \(J_2=n M_1^\circ(x^2)\), \(J_A=n M_W^\circ(P_A)\), where \(P_A(x)=x^2(x-A)^2\). By (2), \(J_A=q^2\mathbb E_\omega[h^2(h-A)^2W^2]+O(n^{-1/4})\). Along any subsequence with \(-J_2\le o(1)\), \(J_A\le o(1)\), one necessarily has
\[
 A\to0,\qquad \mathbb E_\rho W^2\to0,
 \qquad \rho_y=\frac{h_y^2g_y}{n\mathbb E_n(h^2g)}.          \tag{3}
\]
For if \(|A|\ge a>0\) on a further subsequence, put \(D=\{h\ge a/2\}\). On \(D\), Cauchy–Schwarz and \(h\ge a/2\) give \(\mathbb E_\omega[1_D|(h^2-A^2)W|]=o(1)\), using the vanishing squared expression for \(J_A\) and bounded \(h,A\). On its complement \(|h-A|\ge a/2\) likewise gives \(\mathbb E_\omega[1_{D^c}h^2|W|]=o(1)\). Then \(J_2=q^2 A^2\mathbb E_\omega[1_D W]-A^2+o(1)\) has a fixed negative upper by the bound for \(W_+\), a contradiction. Once \(A\to0\), \(\mathbb E_\omega h^4 W^2=o(1)\) from the expression for \(J_A\) and boundedness. A further Cauchy–Schwarz gives \(\mathbb E_\omega h^2 W^2=o(1)\) and hence (3), since \(\mathbb E_\omega h^2\gtrsim1\). Thus the paired unmarked moments force either a critical lower in the indicated signs or concentration of the favored repair weight at the Jacobi level \(z=1/\beta_*\). This is a level with parameters from the actual opposite mark.

In (3) the low favored factor must pay a separate cancellation. For some sufficiently small fixed \(\eta>0\), the set \(\{h\ge\eta,g\ge\eta,|W|\le1/2\}\) carries a positive fraction of \(\rho\)-mass. To see this, the contributions of \(h<\eta\) and \(g<\eta\) to \(\mathbb E_n h^2g\) are bounded by \(\eta^2\mathbb E_n g\) and \(\eta\mathbb E_n h^2\), respectively, and Markov handles \(|W|>1/2\). Boundedness of \(h,g\) and \(z\ge1/(2\beta_*)\) there give \(\mathbb E_n[hz1_D]\gtrsim n^{-1/2}\) on that set \(D\). On \(\{g\ge\eta,z<0\}\) we have \(W\ge1\), so (3) gives \(\mathbb E_n[h^2 1_{\{g\ge\eta,z<0\}}]=o(n^{-1/2})\). The size of that set is \(O_\eta(\sqrt n)\), and Cauchy–Schwarz bounds its negative first moment by \(o(n^{-1/2})\). Since \(\sqrt p\,\mathbb E_n(hz)=A\to0\), one obtains
\[
           \mathbb E_n[hz1_{\{g<\eta\}}]\le -c_1 n^{-1/2}
\]
for large primes on the indicated subsequence. It also lies in the bulk branch of the original mark-versus-exterior dichotomy. No uniform estimate excluding this two-region cancellation is known.

For \(s=1\) the distinct tuple expansion uses only unmarked inputs. For \(s=W=1-\beta_*\epsilon k\), it is a sum of two such expansions, the second with a single additional fixed shift zero. The marked fixed shift cannot collide with any trimmed input. Multiplication by bounded \(s\) preserves the single-pair conditional transform bounds. Intersections for the extra-shift term have an odd singleton at zero, so Katz still supplies square-root cancellation together with the at-least-two collision mass, yielding a smaller-than-\(n^{-1}\) contribution. Therefore the exact arithmetic tests above have distinct expansions with \(O(n^{-5/4})\) collision error before scaling.
