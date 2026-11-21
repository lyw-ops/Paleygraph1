# Signed Jacobi and Legendre coefficients in the actual cold omission

Keep the original closed marked square, \(t_0=n\), both boundary pairs, and the translated \(P_{5000}\) norm. Fix \(h=601,602\) and write \(V_h=S+\alpha Y+H_h\), where \(H_h=\mathcal C_{\rm oth}+Y_h\) combines the other fixed fields with the actual Picard residual. As in [Round 149](cold-two-center-omitted-envelope-149.md), put
\[
 A_h=K\operatorname{diag}(d_{t_i}(V_{h,i})),\qquad
 B_2=K\operatorname{diag}(d_{t_i}(S_i+\alpha Y_i)).
\]
The signed comparison gives \(\|A_h-B_2\|_{P_{5000}}<0.540\), uniformly for sufficiently large eligible primes at both heights. The bounds for \(B_2\) and its square are inherited.

## Collecting equal labels before modulus

At good full Mellin characters use \(C_1=(L+L^{-1})/2\) and \(Y=(\operatorname{tr}N+\operatorname{tr}N^\chi)/2\), with the two determinant-one Legendre factors. The same tensor recurrence appears in the [signed older activation](astra-signed-54.md). For a nonnegative integer \(r\), let \(M_r(a,b)\) count length-\(r\) walks from \((0,0)\) to \((a,b)\) by unit coordinate steps in the nonnegative quadrant. The representation rule for \(SL_2\) is \(N\otimes\operatorname{Sym}^a N=\operatorname{Sym}^{a+1}N+\operatorname{Sym}^{a-1}N\), with the second summand omitted at \(a=0\). The choices of the two factors give the quadrant walk. In \(Y^r\) the coefficient of \(\operatorname{tr}(\operatorname{Sym}^a N\otimes \operatorname{Sym}^b N^\chi)\) is \(2^{-r}M_r(a,b)\).

In particular the unit coefficient at \(r=2s\) is
\[
 4^{-s}\sum_{\ell=0}^s{2s\choose2\ell}C_\ell C_{s-\ell}
 = 4^{-s} C_s C_{s+1},
\]
where \(C_s=\binom{2s}{s}/(s+1)\). Each factor returns to zero through a nonnegative walk of even length. For the identity, substitute the factorial formulas and apply \(\sum_\ell \binom{s}{\ell}\binom{s+2}{\ell+1}=\binom{2s+2}{s+1}\). The unit has phase \(+1\) by the arithmetic symplectic normalizations, so it combines with the same Jacobi Laurent label in the signed sum.

Retain the first 14 Taylor orders of \(d_t\), through total degree 27. Use the signed seed coefficients \(c_{q,k}\) of \((\alpha Y+H_h)^qL^k\) from [Round 136](cold-resummed-136.md). At prescribed degree \(j\ge1\) in \(H_h\), the coefficient of
\(H_h^j L^k\operatorname{tr}(\operatorname{Sym}^a N\otimes\operatorname{Sym}^bN^\chi)\) is
\[
 D_{j,k,a,b}
 =\sum_{q=j}^{27}
    c_{q,k}\binom qj(\alpha/2)^{q-j}M_{q-j}(a,b).
\]
This collects the same label for each specified word of \(j\) omitted factors, whatever those factors' internal decomposition. At degree one, the analytic term of order \(\ell\) with \(r\) Legendre factors has scalar \((2\ell+1)(-1)^\ell b_\ell (2\sqrt t)^{-1}\binom{2\ell}{r}u^{2\ell-r}v^r\) before the Jacobi and Legendre multiplicities, with \(u=s_n/(2\sqrt t)\), \(v=\alpha/(2\sqrt t)\), and \(b_\ell=4^{-\ell}\binom{2\ell}{\ell}\). The power of \(u\) accounts for the one selected \(H_h\) factor.

## Full fiber and translated pricing

In the base pair, \(L^k\) gives a shift \(k\) or \(-k\). In the fiber where \(N\) has weights \((-2,2)\), the symmetric powers have weights \(-2a,-2a+4,\ldots,2a\), each repeated \(b+1\) times. In the other fiber \(a,b\) switch roles. Both lists have dimension \((a+1)(b+1)\); in the extra pair the Legendre and Jacobi factors have weight zero. The coefficients satisfy both \(k\leftrightarrow -k\) and \(a\leftrightarrow b\) symmetry. The total comparison for each \(j\) is therefore symmetric and the same in each base fiber. The physical quadratic lift involution exchanges the full labels \((k,a,b)\) and \((-k,b,a)\). The lift sum and the identical good-character label collection commute. Both assertions concern the full symmetric coefficient collection, including the independent lift choices for omitted factors.

After modulus let \(\Gamma_j\) be the resulting symmetric weight measure. Convolve it with the \(j\)-fold positive retained envelope \(\mathfrak h_h^{*j}\) of \(H_h\) from Round 149, then use the common weight cutoff 150. Any words using the omitted residual tilt of mass at most \(\varepsilon\) cost at most
\[
 j\varepsilon\|\Gamma_j\|_{\mathrm{tilt}}
 (\|\mathfrak h_h\|_{\mathrm{tilt}}+\varepsilon)^{j-1}.
\]
Both this loss and the cutoff loss cost ten times their tilted mass. The same \(0.0000407\) absolute analytic tail applies because the selected infinite remainder has at least one \(H_h\). Compact exceptions can be estimated on the original uncollected words while using the signed identity on good full lifts. This is the earlier absolute summation with uniformly bounded \(O_{5000}(n^{-1/2})\) relative cost. The mark is restored at \(t_0=n\) with the same eventual slack. The [outward checker](cold-signed-legendre-omission-150-check.py) evaluates the actual complex \(\alpha(t)\) on the original square and checks the translated column supremum of the full retained sum. [Saved records](cold-signed-legendre-omission-150-checks.jsonl)

The \(0.540\) bound improves the complete \(0.542\) positive comparison. The remaining step criterion is \(0.356\), or \(0.567184\) for the signed same-height square after the height-transfer debit. Cancellations among internal \(H_h\) labels or across transport steps are still open. So are the nonlinear invariant ball and half-step. The computation gives a uniform eventual derivative bound at two fixed heights and on the stated square.
