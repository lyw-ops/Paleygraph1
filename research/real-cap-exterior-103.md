# A signed exterior test for the real capped row

The real marked comparison can tolerate negative relaxed products. It suffices to bound the signed transport of the excess **above the larger positivity threshold**, together with the mean cap defect. Both quantities are computed on the globally contractive real capped row.

Use the notation of [real amplitude clipping](real-amplitude-cap-102.md). Fix \(t,M>0\) and \(n\ge t\). Write \(U=K\Phi_t(C)\) for the capped fixed point, \(C=C_M(U)\), \(a_i=\Phi_t(C)_i\), \(s_i=t_i-(U_i^2-M^2)_+/4\), and \(\alpha=\mathbb E_n(U_i^2-M^2)_+\). Let \(Y=K\Phi_t(Y)\) be the genuine stationary point at the original weights and \(b_i=\Phi_t(Y)_i\). Put \(\mu=\mathbb E_n a\) and \(\nu=\mathbb E_n b\). The two squared norm identities give
\[
 \nu=2\sqrt{1+t-t/n},\qquad \nu^2-\mu^2=\alpha .
\]
Always \(\mu,\nu>0\). Define the signed excess and its one-sided transported maximum by
\[
 \tau_i=\operatorname{sgn}(U_i)(|U_i|-\sqrt{M^2+4t_i})_+,\qquad
 \kappa=\max_i(K\tau)_i .
\]
In particular \(\tau_i=0\) on \(s_i\ge0\), and \(K\mathbf 1=0\) gives \(\kappa\ge0\). Assume only \(s_0>0\), which holds eventually through primes at fixed \(M,t\) by the cited mark limit \(U_0/\sqrt n\to0\). Set \(\gamma=\operatorname{arsinh}(Y_0/(2\sqrt n))\) and \(\gamma_c=\operatorname{arsinh}(U_0/(2\sqrt{s_0}))\). Then
\[
 4\sqrt{s_0/n}\,[\cosh(\gamma-\gamma_c)-1]
 \ \le\ \frac{\mu}{\mu+\nu}\,\alpha
         +\mathbb E_n \tau_i Y_i
 \ \le\ \frac12\alpha+(\nu-2\sqrt t)\kappa .                         \tag{1}
\]

Indeed \(K^2=I-J_0\) gives the cross identity
\[
 \mathbb E_n(a_i b_i-U_iY_i)=\mu\nu .
\]
At \(s_i\ge0\), \(a_i=\sqrt{U_i^2+4s_i}\), so \(a_i b_i-U_iY_i\ge4\sqrt{s_i t_i}\) by the hyperbolic identity, including \(s_i=0\) by continuity. The difference \(4t_i-4\sqrt{s_i t_i}\) is at most \(4(t_i-s_i)=(U_i^2-M^2)_+\). At the mark add the exact curvature excess \(4\sqrt{s_0 n}[\cosh(\gamma-\gamma_c)-1]\) to this lower bound. At \(s_i<0\), one has \(U_i-\tau_i=\operatorname{sgn}(U_i)a_i\), so
\[
 a_i b_i-U_iY_i=a_i(b_i-\operatorname{sgn}(U_i)Y_i)-\tau_iY_i
 \ge -\tau_iY_i .
\]
At these sites \(4t_i<(U_i^2-M^2)_+\). Summing the two estimates and subtracting \(4\mathbb E_n t_i=\nu^2\) bounds the curvature excess divided by \(n\) by \(\alpha+\mu\nu-\nu^2+\mathbb E_n\tau_iY_i\). The scalar part is \(\mu\alpha/(\mu+\nu)\). Finally symmetry, stationarity and vanishing mean of \(K\tau\) give
\[
 \mathbb E_n\tau_iY_i=\mathbb E_n (K\tau)_i(b_i-2\sqrt t).
\]
The second factor is nonnegative because \(n\ge t\). Its mean is \(\nu-2\sqrt t\), proving the one-sided bound (1).

Thus a sufficient real through-primes estimate at each fixed floor in a sequence \(t\downarrow0\) is
\[
                         \alpha+\kappa\longrightarrow0.             \tag{2}
\]
The cap \(M\) may depend on the fixed floor, and requires no dependence on the prime. The real capped mark vanishes and \(s_0/n\to1\) in this order of limits. Apply (1) and the [real theta bracket](smoothing.md). Exact relaxed positivity implies \(\kappa=0\). Alternatively, one can use \(\mathbb E_n\tau_iY_i\le\nu\|\tau\|_\infty\), so a uniform \(o(1)\) overshoot of the larger threshold also suffices in place of its exclusion. At the nominated real diameter, diverging genuine pre-exit lengths already imply \(\alpha\to0\) by the [capped contraction estimate](real-amplitude-cap-102.md#consequence-for-the-physical-pre-exit-path). The remaining condition there is the signed excess upper or any other bound forcing \(\mathbb E_n\tau_iY_i=o(1)\).

The entry bound \(|K_{ij}|\le\sqrt p/n\) alone gives
\[
 \kappa\le\sqrt p\,\mathbb E_n|\tau_i|
          \le \frac{\sqrt p\,\alpha}{2\sqrt{M^2+4t}} .
\]
For the last inequality use \(|\tau_i|=(U_i^2-M^2-4t_i)/(|U_i|+\sqrt{M^2+4t_i})\) on its support. Hence a vanishing mean defect without a rate yields no vanishing entry-bound estimate. The new test asks for signed arithmetic cancellation on the actual excess, or a sharper estimate of its interaction with the nonnegative true source. Equation (2) and the cold complex neighborhood remain open.

Suppose instead that \(\alpha\to0\) and \(|\gamma|\ge\delta>0\) on a prime subsequence at the fixed floor. Then (1), \(s_0/n\to1\), and \(\gamma_c\to0\) force \(\kappa\ge\eta\) eventually, where
\[
 \eta=\frac{\cosh\delta-1}{\sqrt{1+t}-\sqrt t}.
\]
At any maximizing index, a deletion of any set \(S\) with \(|S|\alpha\le\eta^2/12\) leaves a signed value of at least \(\eta/2\). Indeed \(\tau_i^2\le (U_i^2-M^2)_+\) at each site and the entry bound gives \(|(K1_S\tau)_i|\le\sqrt{p/n}\sqrt{|S|\alpha}\). This robustness holds even for erasures chosen after observing the capped row.

1. At the original real cold floor, derive a one-sided bound on \(K\tau\) for the actual capped fixed point, using the signed upper and lower log tails above the enlarged threshold. Quantify the cap and the field-first approximation loss jointly.
2. If a signed exterior row remains large, estimate its pairing with the true nonnegative source \(b-2\sqrt t\) using the exact identity in (1). This would allow large values where the true source has small total mass.
