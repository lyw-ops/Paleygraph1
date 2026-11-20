# The ordinary terminal test concentrates in a signed off-diagonal sum

Use the actual zero-start Picard orbit at fixed \(\tau>0\) and its approved simultaneous marked window, with \(T+1\) inside the window. Use \(F\) for a nonnegative mean-one ordinary optimum in the opposite sign, \(q_*=F_0\), and \(\lambda=F-q_*e_0\). Let \(g_j=\Phi(v_j)-\Phi(v_0)\). These are the actual objects of the [terminal sufficient test](averaged-hinge-opposite-141.md#a-terminal-activation-test-without-a-positive-part-hinge), not a truncated fixed-word model.

For \(T\ge2\), put \(H=\sqrt n\,g_{T-1}\) and \(G=\sqrt n\,g_T\), with \(G\) tested only on the bulk. The exact update gives \(\sqrt n(v_T-v_1)=KH\). The scalar inequality \(\sqrt{b^2+u^2}-b\le |u|\) gives \(G\le|\sqrt n\,v_T|\) and \(\mathbb E H^2\le\|v_{T-1}\|_{\ell^2}^2\le4W(T-1)\), where \(W=\sum_iw_i\). The seed \(\sqrt n\,v_1\) has uniformly bounded supremum by the Jacobi entry bound.

Form the actual matrix \(B=K\operatorname{diag}(\lambda)K\) in frequency coordinates and the signed sum
\[
 S_{F,T}=\frac1n\sum_{j\ne k}H_jH_k B_{jk}.
\]
Its diagonal comparison is uniformly small on the target quadratic scale. Indeed \(0\le B_{jj}=\sum_i\lambda_i K_{ij}^2\le p/n\) since \(\lambda\ge0\), \(\sum_i\lambda_i\le n\), and \(|K_{ij}|\le\sqrt p/n\). Thus
\[
 \mathbb E[\lambda(KH)^2]
 =S_{F,T}+\frac1n\sum_j B_{jj}H_j^2
 =S_{F,T}+O_\tau(T).
\]
By Cauchy–Schwarz and \(\mathbb E\lambda\le1\), \(\mathbb E(\lambda G)\le O(1)+\sqrt{\mathbb E[\lambda(KH)^2]}\). Therefore the one-sided estimate \(S_{F,T}\le o(T^2)\) at a selectable growing marked time for one actual opposite optimizer on each sign would give the sufficient \(o(T)\) terminal bound in normalized variables and hence imply the original squeeze after \(\tau\downarrow0\). This comparison uses a quadratic moment and may be stronger than the direct terminal estimate. Its off-diagonal term retains all signs and the actual optimizer weights.

## Necessary concentration if an ordinary prime gap persists

Suppose a prime subsequence has \(q_*/\sqrt n\ge 1+\eta\) on a fixed opposite sign, for some \(\eta>0\). Fix \(\tau>0\) so that \(\sqrt{1+\tau}<1+\eta\). The actual mark and mean bounds are \(a=1+o(1)\) and \(\sqrt n M\le\sqrt{1+\tau}+o(1)\) for every growing \(T\) in the marked window. Then the [terminal identity](averaged-hinge-opposite-141.md#a-terminal-activation-test-without-a-positive-part-hinge) forces \(\mathbb E(\lambda G)\ge c_\eta T\) eventually for every actual optimum \(F\) on this sign and every such time choice, with \(c_\eta>0\) after fixing \(\tau\). It follows that \(S_{F,T}\ge c'_\eta T^2\) eventually. The diagonal cannot provide this mass.

The same necessary growth localizes the optimizer's second moment. On the bulk let \(A_T=\{i:G_i\ge c_\eta T/2\}\). The unweighted energy bound \(\mathbb E G^2\le4WT\) gives \(|A_T|/n=O_{\tau,\eta}(T^{-1})\). Since the complementary low part contributes at most \(c_\eta T/2\), Cauchy–Schwarz on \(A_T\) gives \(\mathbb E[1_{A_T}F^2]\ge c''_\eta T\). Thus a prime gap would force every genuine opposite-optimizer row to put a growing second moment specifically on the actual terminal high set, rather than only somewhere on its support.

These are deductions about a hypothesized ordinary prime gap, equivalently about either side by reciprocity. They give no estimate excluding such concentration. The same obstruction holds for the true square minus diagnostic at fixed \(0<\tau<1\), where its terminal lower bound is already known. A route via the off-diagonal sum must therefore use arithmetic specific to the primes.

## Fully unmarked distinct indices suffice for the quadratic test

Let \(H^\circ=1_{\{j\ne0\}}H\). The difference of \(KH\) and \(KH^\circ\) is \(H_0 Ke_0\). Its \(\lambda\)-weighted second norm is bounded by
\[
 |H_0|\max_i|K_{i0}|
 \le \sqrt{p/n}\,g_{T-1}(0)
 =O_{\tau,B}(T^{-2B})
\]
in the marked window with exponent \(B>0\), since \(g_{T-1}(0)\le v_{T-1}(0)^2/4\). This step takes the weighted second norm before dropping the physical mark of the source. It avoids any factor \(\sqrt n\) multiplying the marked-window error.

After this removal the diagonal \(j=k\) still costs \(O_\tau(T)\). Terms with \(i=j\ne k\) or \(i=k\ne j\) cost, in total absolute value, at most
\[
 \frac{2\sqrt p}{n}\,\mathbb E(FH^\circ)\,\mathbb E H^\circ
 \le \frac{2\sqrt p}{n}\|F\|_{2,n}\,\mathbb E[(H^\circ)^2]
 =O_\tau(p^{-1/4}T).
\]
Here \(K_{ii}=-1/n\), \(\|F\|_{2,n}\le (1+\sqrt p)^{1/2}\), and both expectations use divisor \(n\). Thus the quadratic comparison reduces to the exact signed sum
\[
 \mathscr D_{F,T}
   =\frac1n\sum_{\substack{i,j,k\ne0\\i,j,k\text{ distinct}}}
                  F_i H_j H_k K_{ij}K_{ik},
 \qquad
 \mathbb E[\lambda(KH^\circ)^2]=\mathscr D_{F,T}+O_\tau(T).
\]
A uniform upper \(o(T^2)\) for this sum is sufficient for the terminal test. A hypothesized prime gap forces it to be \(\Omega_{\tau,\eta}(T^2)\), by the same triangle and Cauchy–Schwarz estimates as above. All three indices here are unmarked and distinct, with the exact source and ordinary optimum. In particular, coincidence of input indices, twice using the same output index as an input, and exceptional physical marks cannot explain the quadratic obstruction.
