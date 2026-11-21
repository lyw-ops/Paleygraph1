# Bounded windows and the actual ordinary seed pairing

Use the ordinary cap-inactive activation \(b\) of [Round 133](zero-floor-sector-133.md), with \(S=2\sqrt n\,Ke_0\), ordinary marked ratio \(\eta\), and fixed positive marked cap \(M\). Its bulk weighted seed pairing is \(4\eta+O_M(n^{-1})\). The seed supremum bound is \(2\sqrt{p/n}=2\sqrt2+O(p^{-1})\).

For any fixed bounded even polynomial expression \(Q_p\) in bounded negative Mellin fields of fixed complexity, its bulk average against \(S\) is \(O_{Q}(p^{-1/2})\). Each monomial of \(Q_pS\) has odd total arity, so the [fixed-expression trace estimate](iteration-parity.md#uniform-fixed-expression-trace-estimates) applies, including exceptional frequencies. Omitting the mark costs \(O_Q(n^{-1})\).

One may use the continuous clip \(b^{[L]}_i=\min(b_i,L)\) on the bulk. Define
\[
 T_{p,L}=\mathbb E_n[1_{\{i\ne0\}}(b_i-L)_+ S_i].
\]
If the bulk \(L^1\) distance from \(Q_p\) to \(b^{[L]}\) is at most \(\rho\), uniformly for sufficiently large primes, then
\[
 |4\eta-T_{p,L}|
 \le 2\sqrt{p/n}\,\rho+O_Q(p^{-1/2})+O_M(n^{-1}).
\]
Thus a fixed-window polynomial completion and a signed tail estimate suffice together. Absolute uniform integrability of the actual bulk weights is one sufficient input for the signed tail. The polynomial completion is a different input. For example, if an actual ordinary bias stays bounded away from zero and the absolute tails vanish, a failure of the bounded-window completion must occur.

Replacing the discontinuous high-value indicator by a continuous clip means that a bulk \(L^1\) approximant to the actual \(Y\) by a fixed bounded negative-field expression would suffice for the window, using the Lipschitz function \(\min(|y|,L)\) and an even polynomial on its bounded range. An arbitrarily accurate sequence of such bulk \(L^1\) approximants also gives uniform integrability directly and allows one to use \(|y|\) without a window. The approximation for fixed capped iterates does not provide these approximants for the actual ordinary row. The necessary support-sensitive work remains open.

Bounded auxiliary weights can already carry a nonzero pairing with the real Jacobi seed. Set \(b'_i=1+S_i/4\) on the bulk and \(b'_0=0\). For sufficiently large primes these weights are nonnegative and below 2. Using \(\mathbb E_n S=0\), \(S_0=-2/\sqrt n\) and \(\mathbb E_n S^2=4(1-1/n)\), their bulk pairing is
\[
 \mathbb E_n b'S=1-\frac1n+\frac{2}{n^{3/2}}-\frac1{n^2}.
\]
This bounded profile shows why even a perfectly controlled tail does not by itself prove weighted parity. It does not satisfy the ordinary optimizer equations.
