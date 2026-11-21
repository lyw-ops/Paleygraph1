# Removing the mark from a mixed reciprocal moment

Work under the [fixed-floor critical cap-rate marked obstruction](persistent-repair-deficit-109.md), with the true late average \(h=\bar h\) and two actual stationary factors \(g=f_\epsilon/\sqrt n\), \(g_-=f_{-\epsilon}/\sqrt n\) of [Round 112](full-repair-moments-112.md). Means and norms are normalized. Put \(u=\epsilon Kh\), \(A=u(0)\), and \(\mu=\mathbb E_n g=\mathbb E_n g_-=\nu/(2\sqrt n)\). The selected mark is the original coordinate \(0\). In particular \(h(0)=0\), while \(A\) can have either sign and is uniformly bounded. The exact reciprocal product is \(gg_-=t/n+(1-t/n)1_{\{0\}}\), where \(t\) is fixed before the prime limit.

## Exact polynomial calculation

Let \(P\) be a real polynomial of fixed degree whose coefficients stay bounded along the subsequence, with \(P(0)=P'(0)=0\). Then
\[
 \mathbb E_n[P(u)(Kg)(Kg_-)]
 =\mu\mathbb E_n[P(h)g]-\frac{1-t/n}{n}P(A)+O_P(n^{-5/4}). \tag{1}
\]
The error is uniform over a bounded coefficient set at fixed degree. In fact stationarity gives the pointwise identity
\[
 (Kg)(Kg_-)=\mu(g+g_-)-\mu^2-t/n-(1-t/n)1_{\{0\}}.
\]
For each monomial of degree at least two, factor the difference at \(u,h\), bound all but one of the remaining factors in supremum norm and use Cauchy–Schwarz. Thus \(\mathbb E_n|P(u)-P(h)|=O_P(n^{-3/4})\). The bounds used are \(\|u-h\|_{2,n}=O(n^{-1/2})\), bounded supremum norms and \(\|u\|_{2,n}+\|h\|_{2,n}=O(n^{-1/4})\). Also \(\mathbb E_n|P(u)|\ll_P\mathbb E_n u^2=O(n^{-1/2})\), and \(\mathbb E_n |P(h)|g_-\ll_P\mathbb E_n(h^2 g_-)=O(n^{-3/4})\) by the actual opposite-sector comparison. Multiplying by the relevant coefficients yields (1). The marked contribution remains at its exact size, because \(P(u(0))\) can be order one despite \(h(0)=0\).

For \(P(z)=z^2\), the two explicit terms on the right side have order up to \(n^{-1}\), and the first has a positive lower at that order. If \(|A|\le a_0\) for a sufficiently small fixed \(a_0>0\), the fourth mixed moment has a fixed positive multiple of \(n^{-1}\) as a lower. In particular there is a new necessary test using both reciprocal factors on this subcase of the late obstruction. There is no cancellation estimate for this fourth moment at that scale yet.

For general \(A\), take \(P_A(z)=z^2(z-A)^2\). Then (1) shows
\[
 n\mathbb E_n[P_A(u)(Kg)(Kg_-)]
       = n\mu\mathbb E_n[h^2(h-A)^2g]+O(n^{-1/4}).             \tag{2}
\]
The mark cancels identically. For the actual probability law \(\rho_y=h_y^2g_y/(n\mathbb E_n h^2 g)\), the quantity on the right equals \(n\mu(\mathbb E_n h^2g)\,\mathbb E_\rho(h-A)^2+O(n^{-1/4})\). Its prefactor is comparable to one. Thus an \(o(n^{-1})\) bound for the modified reciprocal moment would force the \(h^2g\)-weighted amplitude to concentrate at \(A\). In particular, under that hypothetical bound \(A\) would have to be bounded away from zero on the positive side. Indeed \(\mathbb E_\rho h\ge (\mathbb E_n h^2g/\mathbb E_n g)^{1/2}\gtrsim1\) by monotonicity of the second and third norms under the probability proportional to \(g\). This would leave a quantitatively anchored alternative, rather than the entirely unrestricted bulk alternative of Round 112. Equation (2) alone has no such small upper bound.

## Collision precision at the new scale

Expanding \(u^d(Kg)(Kg_-)\) for fixed \(d\ge2\) uses \(d\) independent draws from \(\pi\) and one each from \(\omega,\omega^-\), the probability weights of [Round 112](full-repair-moments-112.md). For a law \(\sigma\) write \(F_\sigma(x)=\sum_y\sigma_y k(x-y)\); these functions are bounded by one, and are respectively \(Kh/(\sqrt p\,m)\), \(Kg/(\sqrt p\,\mu)\), and \(Kg_-/(\sqrt p\,\mu)\). All scalar prefactors in the moment expansion are comparable to one in modulus. Each law has maximum \(O(n^{-1/2})\). The particular overlap masses are
\[
 \sum_y \pi_y\omega^-_y=O(n^{-3/4}),\qquad
 \sum_y \omega_y\omega^-_y=O(n^{-1}),
\]
by \(\mathbb E_n h g_-=O(n^{-3/4})\) and the exact reciprocal product, using \(n m\mu,n\mu^2\asymp1\).

For a specified equal pair of draws, initially allow all other coincidences. The conditional kernel from that pair is \(k(x-y)^2\), bounded by one. In the four possible types, the absolute sum *after summing the other unconstrained draws* is bounded as follows.

| Equal pair | Pair mass | Bound for the remaining transformed product in normalized first norm |
| --- | --- | --- |
| Two repair draws | \(O(n^{-1/2})\) | \(O(n^{-1})\) from \(\mathbb E_n|(Kg)(Kg_-)|=O(n^{-1})\) by the product identity |
| Repair and favored | \(O(n^{-1/2})\) | \(O(n^{-3/4})\) from \(\mathbb E_n|(Kh)(Kg_-)|=O(n^{-3/4})\) |
| Repair and opposite | \(O(n^{-3/4})\) | \(O(n^{-1/2})\) by \(\|Kh\|_{2,n}\|Kg\|_{2,n}=O(n^{-1/2})\) |
| Favored and opposite | \(O(n^{-1})\) | \(O(n^{-1/2})\) by \(\mathbb E_n|Kh|^d=O_d(n^{-1/2})\) |

For the second row, expand \(|Kg_-|\le g_-+\mu\), replace \(|Kh|\) by its upper \(h+|u-h|\), and use \(\mathbb E_n h g_-=O(n^{-3/4})\) and \(\|u-h\|_{2,n}\|g_-\|_{2,n}=O(n^{-3/4})\). All additional factors \(F_\pi\) are bounded. This argument uses the signed sum over the unconditioned remaining shifts, rather than the sum of absolute values of the individual correlations.

To restore the union of all equality events, subtract their intersections by finite inclusion–exclusion. Every pattern in an intersection has at least two repeated draws, meaning the number of draws minus its number of distinct classes is at least two. If one class has odd multiplicity, Katz and the individual mass bound give \(O(n^{-3/2})\). An all-even pattern with at least three repetitions has the same bound by mass alone. The remaining all-even case has four draws and two pairs. If the reciprocal draws are paired together, its mass is \(O(n^{-3/2})\) by the reciprocal overlap bound. If they are each paired with a repair draw, its mass is \(O(n^{-5/4})\) by the repair/opposite overlap bound. Therefore the sum over **all coincidences** is \(O_d(n^{-5/4})\). The distinct tuple expansion alone computes (1) and (2) at their required precision, after applying the degree-dependent scalar prefactor to each monomial. In particular, deleting collisions at order \(n^{-1}\) here uses the true reciprocal factor pair and cannot be obtained from the uniform pointwise Katz bound for arbitrary dilute laws.

## Using the opposite mark to limit favored mass on any sparse set

Write \(q=\sqrt n\mu\), so that \(q^2=1+t-t/n\), and let \(\omega_y=g_y/(n\mu)\). The \(u=0\) specialization of the [returned reciprocal budget](api-astra-overflow-113.txt) applies to any off-mark set \(D\) of size \(O(\sqrt n)\). Here is the direct calculation. Put \(z(y)=\epsilon k(y)\), \(B=\sqrt{n/p}(g_-(0)-\mu)\). We have \(B\ge B_0>0\) on the obstruction subsequence by the bounded true log mark. Also \(\mathbb E_n z=0\), since \(K1=0\), and \(\sqrt n\mathbb E_n(zg_-)=-B\) by exact stationarity. With fixed \(v\in(0,1/2)\), Cauchy–Schwarz on the complement of \(D\cup\{0\}\) using \(g\) and \((1+vz)g_-\) gives
\[
 q(1-\omega(D))(q-vB)\ \ge\ t\big(\mathbb E_n\sqrt{1+vz}-O(n^{-1/2})\big)^2.              \tag{3}
\]
The error is uniform over sets with a fixed size coefficient. By Taylor's theorem on \([1/2,3/2]\), zero mean of \(z\) and \(|z|\le1\), the squared mean on the right is \(\ge1-Cv^2-O(n^{-1/2})\). Choose a fixed \(v>0\) small enough using \(B_0\) and an upper bound on \(q\). Then \(q-vB>0\), since \(B\le q\) by \(|z|\le1\) and the weighted-mean identity. The reduction of the second factor in (3) is linear in \(v\) and dominates the quadratic loss. In particular there is a fixed \(\delta>0\) (which may depend on \(t\)) such that, for all sufficiently large primes,
\[
                   q^2\omega(D)\le 1-\delta .                 \tag{4}
\]
Indeed (3) gives \(q^2\omega(D)\le q^2-t(1+\delta')\) for some fixed \(\delta'>0\), and \(q^2=1+t-t/n\).

Set \(U_2=n\mathbb E_n[u^2(Kg)(Kg_-)]\) and \(V=n\mathbb E_n[P_A(u)(Kg)(Kg_-)]\). There is a fixed \(c_0>0\) such that every sufficiently large prime in the obstruction has
\[
                          \max(-U_2,V)\ge c_0 .                 \tag{5}
\]
If this failed, there would be a sequence with \(\max(-U_2,V)\le o(1)\). Equation (2) gives \(V\ge-o(1)\), hence \(V\to0\). The weighted concentration shown above gives \(A\ge a_0>0\) eventually, and \(\mathbb E_\omega[h^2(h-A)^2]=o(1)\). Take \(D=\{h\ge a_0/2\}\); it avoids the mark and has size \(O(\sqrt n)\) by the repair mean. On its complement, \(|h-A|\ge a_0/2\) shows that the contribution to \(\mathbb E_\omega h^2\) is \(o(1)\). On \(D\), the same concentration and \(h\ge a_0/2\) give \(\mathbb E_\omega[1_D(h-A)^2]=o(1)\). Boundedness and Cauchy–Schwarz give \(\mathbb E_\omega h^2=A^2\omega(D)+o(1)\). But (1) for \(P(z)=z^2\) and (4) now yield \(U_2=q^2\mathbb E_\omega h^2-(1-t/n)A^2+o(1)\le-\delta a_0^2+o(1)\). This is a contradiction.

Together with the collision estimate, (5) is a two-sign necessary test on distinct mixed sums of degrees four through six, with the coefficients of \(P_A\) known from the genuine marked linear transport. In particular the two moments cannot both be \(o(n^{-1})\). Equation (5) does not provide the required prime-uniform upper bounds on \(-U_2\) and \(V\). A next arithmetic test is to estimate the signed degree-four, five, and six sums with both actual reciprocal laws present, at the smaller scale now left after deleting collisions.
