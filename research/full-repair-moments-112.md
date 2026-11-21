# Full late-repair moments and the genuine marked cost

Use the fixed-floor critical cap-rate marked obstruction of [Round 109](persistent-repair-deficit-109.md) on its true late interval, and the core and exterior of [Round 110](repair-core-defect-balance-110.md). All means, norms and inner products below are normalized. Put \(h=\bar h\), \(m=\mathbb E_n h\), \(b=b^i\), \(e=Ph-m\mathbf1\), \(g=f_\epsilon/\sqrt n\). Here \(f_\epsilon\) is the genuine favored factor from Round 109, and \(g\) is not a new optimized spectrum. Work on the prime subsequence under the same fixed parameters.

## Full source and distinct moments

The cap-rate bounds give \(m\asymp n^{-1/2}\), \(\|h\|_{2,n}^2\asymp n^{-1/2}\) and \(\|Kh-\epsilon h\|_{2,n}=O(n^{-1/2})\) for the R110 core window. The Jacobi entry bound gives \(\|Kh\|_\infty=O(1)\), and \(\|Kh-\epsilon h\|_\infty\le\sqrt n\|Kh-\epsilon h\|_{2,n}=O(1)\) gives a pointwise bound on the full \(h\). The same facts hold for each late row before averaging. For any fixed integer \(d\ge3\), expanding the difference of powers and bounding \(d-2\) factors in supremum norm gives
\[
 \mathbb E_n(Kh)^d=\epsilon^d\mathbb E_n h^d+O_d(n^{-3/4}).
\]
For nonnegative \(h\), Jensen under the law \(h/(nm)\) gives \(\mathbb E_n h^d\ge (\mathbb E_n h^2)^{d-1}/m^{d-2}\gtrsim_d n^{-1/2}\).

Use \(\pi_y=h_y/(nm)\) and define \(T_d(a_1,\ldots,a_d)=\mathbb E_x\prod_{s=1}^d k(x-a_s)\) for the genuine \(k=\lambda/\sqrt p\). The moment is \((\sqrt p\,m)^d\) times the weighted \(T_d\) sum. The max weight is \(O(n^{-1/2})\). Under any repeated-index pattern with an odd multiplicity, Katz's Gauss cancellation from [Round 111](distinct-cubic-repair-111.md) gives a pointwise \(O_d(p^{-1/2})\), and the total collision probability is \(O_d(n^{-1/2})\). For an all-even pattern with \(k_0\) classes, each of the \(d-k_0\) within-class repetitions costs at most \(\max\pi\). Since \(d\ge4\) in this case and \(k_0\le d/2\), its probability is \(O_d(n^{-d/4})\). The bounded kernel handles this pattern. Thus all repeated-index contributions sum to \(O_d(n^{-1})\), and
\[
 \epsilon^d\sum_{a_1,\ldots,a_d\,\text{distinct}}
         \pi_{a_1}\cdots\pi_{a_d}T_d(a_1,\ldots,a_d)
       \gtrsim_d p^{-1/2}.
\]
The implied constants here fix \(d\) before the prime limit. These tests retain the actual low-amplitude exterior.

## Exact marked contribution and a mixed cubic

The marked budget gives \(b^j_0\asymp\sqrt n\) with positive lower constant for every step in the R109 late window. Hence \(h(0)=0\) and \(0\notin C\). Symmetry of the Jacobi kernel gives
\[
 e_0=-\frac{m}{2}-\frac{\epsilon\sqrt p\,m}{2}\sum_y\pi_y k(y).
\]
The R110 negative pairing \(\langle b,e\rangle\le-c n^{-1/2}\) has a core contribution \(o(n^{-1/2})\) by the core estimate on \(e\) and the bounded \(\|b\|_{2,n}\). It follows that for all sufficiently large primes on the subsequence, either \(\epsilon\sum_y\pi_y k(y)\ge c_1>0\) or
\[
 \langle 1_{G\setminus(C\cup\{0\})}b,e\rangle\le-c_2 n^{-1/2}
\]
for some fixed \(c_1,c_2>0\). If the marked term pays at least half the required negative pairing, its exact formula forces the first alternative, since \(b_0m/n=O(n^{-1})\), and otherwise the bulk pays the remaining fixed share. This uses no sign assumption on the true bulk term. The mark-free square coset from Round 110 has \(\sum_y\pi_y k(y)=-1/\sqrt q\), which checks the first branch against that static control.

The R109 true factor pairing supplies \(\mathbb E_n(hg)\gtrsim n^{-1/2}\) by averaging the actual window. Also \(\mathbb E_n g\asymp n^{-1/2}\), \(\|g\|_\infty=O(1)\), \(\|g\|_{2,n}=O(n^{-1/4})\) and \(Kg=\epsilon(g-(\mathbb E_n g)\mathbf1)\). By weighted Cauchy–Schwarz, \(\mathbb E_n(h^2 g)\ge (\mathbb E_n hg)^2/\mathbb E_n g\gtrsim n^{-1/2}\). The exact transform for \(g\) and the bound on \(Kh-\epsilon h\) give
\[
 \mathbb E_n[(Kh)^2 Kg]=\epsilon\mathbb E_n(h^2 g)+O(n^{-3/4}).
\]
Indeed \((Kh)^2-h^2=(Kh-\epsilon h)(Kh+\epsilon h)\) has counting-normalized first norm \(O(n^{-3/4})\) by Cauchy–Schwarz, and the mean correction for \(g\) costs \(O(n^{-1})\). Put \(\omega_y=g_y/(n\mathbb E_n g)\). In the transform expansion with two draws from \(\pi\) and one from \(\omega\), every tie involves a draw from \(\pi\). Exactly two equal indices have mass \(O(n^{-1/2})\) and a pointwise Katz bound. Three equal have mass \(\sum_y\pi_y^2\omega_y\le\|\pi\|_\infty^2\). Therefore the true second weight also gives
\[
 \epsilon\sum_{a,b,c\,\text{distinct}}\pi_a\pi_b\omega_c T_3(a,b,c)\gtrsim p^{-1/2}.
\]
The true favored law satisfies \(\|\omega\|_\infty=O(n^{-1/2})\). In particular \(\omega_0=2e^{\epsilon\gamma}/(\nu\sqrt n)\asymp n^{-1/2}\), so the distinct summands with \(c=0\) cost \(O(n^{-1})\) by the pointwise Katz estimate. Since \(\pi_0=0\), the mixed lower still holds with all three distinct indices off the mark. The full anchored contribution, even including collisions, has the same smaller order by \(K(g_0\mathbf1_{\{0\}})=(g_0\sqrt p/n)k\) and \(\mathbb E_n(Kh)^2=O(n^{-1/2})\).

This unmarked mixed cubic is simultaneous with either branch of the marked-cost dichotomy. A prime-uniform mixed cancellation or an incompatibility with both cost alternatives remains open.

## Conditional squared-source transport and the opposite factor

For a fixed third shift \(c\), let \(F(c)=\sum_{a,b\,\text{distinct from each other and }c}\pi_a\pi_b T_3(a,b,c)\). Exactly two equal indices have total weight \(O(n^{-1/2})\) uniformly in \(c\), and all equal have weight \(\pi_c^2=O(n^{-1})\). Thus restoring collisions costs \(O(n^{-1})\). The exact transform expansion with collisions and symmetry of \(k\) give
\[
 \sqrt p\,F(c)=\frac{K[(Kh)^2](c)}{(\sqrt p\,m)^2}+O(n^{-1/2})
             =\frac{K(h^2)(c)}{(\sqrt p\,m)^2}+O(n^{-1/4})
\]
uniformly. The last replacement uses the entry bound and \(\mathbb E_n|(Kh)^2-h^2|=O(n^{-3/4})\). The entry bound and the existing exterior estimate also allow replacing \(h^2\) by \(1_C h^2\), at cost \(O(n^{-\beta})\) in output supremum norm on the moving core.

The exact signed transport into the true favored factor is
\[
 \epsilon\mathbb E_n[g K(h^2)]=\mathbb E_n[gh^2]-(\mathbb E_n g)(\mathbb E_n h^2)\gtrsim n^{-1/2}.
\]
Here \(\|K(h^2)\|_{2,n}\le\|h\|_\infty\|h\|_{2,n}=O(n^{-1/4})\), and \(\|1_{\{g<\eta\}}g\|_{2,n}\le(\eta\mathbb E_n g)^{1/2}\). The low-factor contribution is therefore \(O(\sqrt\eta n^{-1/2})\) and the marked contribution is \(O(n^{-1})\) by the uniform entry bound for \(K(h^2)\). Fixing small \(\eta>0\) and using \(\mathbb E_n g=O(n^{-1/2})\), sites with \(g\ge\eta\), \(c\ne0\), and \(\epsilon K(h^2)(c)\ge c_*>0\) must carry \(g\)-mass of order at least \(n^{-1/2}\). Since \(g\) is uniformly bounded, there are at least order \(\sqrt n\) such sites. Their number is also \(O_\eta(\sqrt n)\) by the mean. The moving core replacement retains a fixed positive lower on those genuine high sites.

Let \(g_-=f_{-\epsilon}/\sqrt n\), the genuine opposite stationary factor. It is in the range of \(P\), so \(\mathbb E_n(hg_-)=m\mathbb E_n g_-+\langle e,g_-\rangle=O(n^{-3/4})\), since \(\|e\|_{2,n}=O(n^{-1/2})\) and \(\|g_-\|_{2,n}=O(n^{-1/4})\). Positivity and bounded \(h\) give \(\mathbb E_n(h^2g_-)=O(n^{-3/4})\). The same transform and collision bounds with \(\omega^-_c=(g_-)_c/(n\mathbb E_n g_-)\) give the upper \(O(n^{-3/4})\) for the signed distinct cubic with the true opposite law. This establishes an asymmetry between two actual weights. The prime-specific obstruction remains open. The reciprocal product of the two true factors gives an additional constraint for testing this asymmetry with the centered exterior pairing.
