# The actual masked functional and stability at fixed repair depth

Use the real stationary factors of [Round 120](reflected-offmark-cubic-120.md), with normalized factors \(g,g_-\), common mean \(\mu\asymp n^{-1/2}\), and fixed floor \(t\). They satisfy \(Kg=\epsilon(g-\mu)\), \(Kg_-=-\epsilon(g_--\mu)\), \(gg_-=t/n\) off the mark and \(gg_-=1\) at the mark. In particular both factors have bounded sup and normalized second norm \(O(n^{-1/4})\). Set \(F=1_{\{x\ne0\}}\), \(X_y(x)=\sqrt p\,k(x-y)\), and
\[
K_\ell d(x)=\mathbb E_y X_y(x)^\ell d_y
\]
so \(K_1=K\), and each \(K_\ell\) is symmetric since the real Jacobi kernel \(k\) is even. All vector means and second norms use denominator \(n\).

## A linear identity with both true factors

Let \(T(q)=M_q^{\mathrm{dist},\circ\mathrm{out}}\) be defined by the raw distinct sum with prefactor \(\epsilon p^{3/2}\) over three normalized input means with integrand \(q_a g_b (g_-)_c T_3^{\circ\mathrm{out}}(a,b,c)\). This defines \(T\) for every signed \(q\), including zero mean. Inclusion–exclusion for the three input equalities gives \(T(q)=\mathbb E_n(q\mathcal A)\) with the exact coefficient
\[
\begin{aligned}
\mathcal A=\epsilon\bigg[
&K\big(F((Kg)(Kg_-)-K_2(gg_-)/n)\big)\\
&-\frac{g}{n}K_2(F Kg_-)-\frac{g_-}{n}K_2(F Kg)
 +\frac{2gg_-}{n^2}K_3 F\bigg].
\end{aligned}                                                     \tag{1}
\]
Each pair equality costs \(1/n\) in the three normalized means. All intersections of two pair equalities are the same triple equality and restore its coefficient \(2/n^2\). The indicator \(F\) remains on the output of every term.

Define \(\Lambda^-_y=\sum_x k(x-y)^2(g_-)_x/(n\mu)\) and \(\Lambda^+_y=\sum_x k(x-y)^2 g_x/(n\mu)\), which both take values in \([0,1]\). There is a uniform estimate for every signed \(q\),
\[
 T(q)
  =\frac pn\mu\,\mathbb E_n\!\left[q\left(g\Lambda^--g_-\Lambda^+\right)\right]
          +O\!\left(n^{-1}\|q\|_{2,n}\right).                       \tag{2}
\]
In particular the error is \(O(n^{-5/4})\) at the critical second-norm scale, with no eigendefect condition.

To prove (2), write \(c=t/n\), \(v_n=(n-1)/p\) and \(\sigma=\mu(g_0+(g_-)_0)-\mu^2-c=O(\mu)\). By the exact reciprocal product,
\[
\epsilon K[F(Kg)(Kg_-)]=\mu(g-g_-)-\epsilon\sigma K e_0 .
\]
The last term is \(O(n^{-1})\) in normalized second norm since \(\|Ke_0\|_{2,n}\le n^{-1/2}\). In the first collision of (1), \(K_2(gg_-)=c(n-1)\mathbf1+(1-c)K_2 e_0=O(1)\) in sup. Thus the \((1/n)K[F K_2(gg_-)]\) term costs \(O(n^{-1})\) in normalized second norm. The repair/favored collision contributes \(+(p/n)\mu\,g(\Lambda^--v_n)\) and the repair/opposite collision contributes \(-(p/n)\mu\,g_-(\Lambda^+-v_n)\), up to their output-mark corrections of size \(O(n^{-1})(g+g_-)\) pointwise. Indeed \((Kg)_0,(Kg_-)_0=O(1)\) and \(\|K_2 e_0\|_\infty\le p/n\). The remaining coefficient of \(\mu(g-g_-)\) after collecting the two baseline terms is \(1-(p/n)v_n=1/n\). Finally \(\|K_3 F\|_\infty\le p^{3/2}\), and the all-equal term is \(O(n^{-3/2})\) off the input mark by \(gg_-=t/n\). Its \(O(n^{-1/2})\) value at the single input mark costs \(O(n^{-1})\) in normalized second norm. These bounds give (2) after pairing.

Formula (2) allows a single signed test of an approximate repair row while keeping both actual factors. For an error \(e\), it gives \(n|T(e)|\ll n^{1/4}\|e\|_{2,n}\). It also gives \(nT(e)=o(1)\) under the weighted condition \(\mathbb E_n[|e|(g+g_-)]=o(n^{-1/2})\) and the bounded critical error scale \(\|e\|_{2,n}=O(n^{-1/4})\). The weighted estimate permits errors of critical size where both true factors are small.

There is also a first-norm bound \(n|T(e)|\ll \sqrt n\,\|e\|_{1,n}\), including errors with a nonzero input mark. Indeed \(\|\mathcal A\|_\infty=O(n^{-1/2})\) globally. The potentially larger \(K[F K_2(gg_-)]/n\) term costs at most \(O(\sqrt p/n)\) by the Jacobi entry bound, and the all-equal term costs \(O(n^{-1/2})\) even at the mark because \(gg_-\) is bounded everywhere. The remaining terms have this sup bound by the estimates just proved.

## Uniform seed approximation and a localized critical repair error

Use the original capped seed \(z\), deficit \(\alpha\), and actual ordinary iteration \(b^0=z,\ h_j=(b^j)_-,\ b^{j+1}=b^j+Ph_j\) from [Round 108](iterated-sector-projection-108.md). Assume the critical rate \(\alpha\le B/\sqrt n\), with \(t,M,B\) fixed. For any fixed \(0<s<\sqrt{M^2+4t}-M\), Round 109 gives \(|\{z\le s\}|/n\le \alpha/L_s\), \(L_s=(\sqrt{M^2+4t}-s)^2-M^2>0\), for sufficiently large \(n\). The true dissipation gives \(\sum_{i<j}\|Ph_i\|_{2,n}^2\le\alpha\). Thus, for \(A_j=\{b^j\le s/2\}\),
\[
 \frac{|A_j|}{n}
 \le \frac{\alpha}{L_s}+\frac{4\|b^j-z\|_{2,n}^2}{s^2}
 \le \alpha\left(L_s^{-1}+4j/s^2\right).                             \tag{3}
\]

Suppose a real approximate seed \(\widetilde b^0\) has \(\|\widetilde b^0-z\|_\infty=\delta_n=o(1)\), and run the same signed update \(\widetilde b^{j+1}=\widetilde b^j+P(\widetilde b^j)_-\). It may also be taken in \(\operatorname{im}P\), in which case this is the ordinary \(P(\widetilde b^j)_+\) update. For any fixed \(J\), through \(j=J\) one has
\[
\begin{aligned}
 \|\widetilde b^j-b^j\|_\infty&=O_J(\delta_n),\\
 \|(\widetilde b^j)_--h_j\|_{2,n}&=O_J(\delta_n\sqrt{\alpha})
                                    =o(n^{-1/4}).
\end{aligned}                                                       \tag{4}
\]
In fact when the current sup error is less than \(s/2\), the negative-part difference \(d_j=(\widetilde b^j)_--h_j\) is supported on \(A_j\). Its sup is bounded by the current sup error, denoted \(e_j\). From \(P=(I-\epsilon K+J_0)/2\) and \(|K_{xy}|\le\sqrt p/n\),
\[
 e_{j+1}
 \le e_j+\|P d_j\|_\infty
 \le \left(\frac32+\frac{1+\sqrt p}{2}\frac{|A_j|}{n}\right)e_j .
\]
The factor is uniformly bounded for \(j\le J\) by (3) and the critical rate. Induction keeps \(e_j<s/2\) for all these depths for sufficiently large \(n\). Taking the normalized second norm of the localized \(d_j\) proves (4). In the actual marked obstruction \(b^j_0/\sqrt n\) stays above a fixed positive constant at fixed depths. Hence the approximate negative row also vanishes at the mark. Combining (2) and (4) gives \(\sup_{j\le J} n|T((\widetilde b^j)_-)-T(h_j)|=o(1)\).

This changes the approximation question at fixed repair depth. A uniform \(o(1)\) approximation to the genuine cap seed is sufficient, even if the full seed error has a second norm larger than \(n^{-1/4}\). The critical support estimate enters only when the negative part is taken. There is also a two-limit version. If for every sufficiently small \(\delta>0\) a fixed approximant has seed sup error at most \(\delta\) eventually and satisfies \(nT((\widetilde b^{j_0})_-)=o(1)\) at the same fixed ordinary depth \(j_0\), then \(\limsup |nT(h_{j_0})|\le C_{j_0}\delta\). The constants in (4) depend on \(j_0\) and the obstruction parameters and are independent of the approximant. Sending \(\delta\downarrow0\) gives the required upper.

The first-norm bound also allows some large seed errors. Write \(e^0=\widetilde b^0-z\). If
\[
\sum_{i\in B_{\rm top}}|e_i^0|=o(\sqrt n),\qquad
 |B_{\rm top}|=\lceil\sqrt n\rceil,                                 \tag{5}
\]
where \(B_{\rm top}\) consists of the largest absolute errors, then the normalized first norm of every \(d_j\) for \(j\le J\) is \(o(n^{-1/2})\). In fact \(x\mapsto x+x_-/2\) is one-Lipschitz. Therefore the update gives the pointwise bound \(|\widetilde b^j-b^j|\le |e^0|+\tau_j\) with \(\tau_j=(\sqrt p+1)\sum_{\ell<j}\|d_\ell\|_{1,n}/2\). If \(\tau_j\le s/4\), off \(A_j\) the negative-part error is at most \((|e^0|-s/4)_+\). The support of this excess lies within \(B_{\rm top}\) eventually, since the smallest error on \(B_{\rm top}\) tends to zero. On \(A_j\) the difference is at most \(|e^0|+\tau_j\); the initial error on \(A_j\) costs at most \(O_J(1)\) times the sum in (5) by (3). Consequently \(\|d_j\|_{1,n}\le o(n^{-1/2})+O_J(n^{-1/2})\tau_j\). Fixed-depth induction keeps \(\tau_j=o(1)\), and the first-norm bound transfers the full \(nT\) with \(o(1)\) error.

## An explicit projected cap Picard approximant

Let \(\Upsilon_m\) be the genuine real capped Picard orbit from zero, \(a_m=\Phi_t(C_M(\Upsilon_m))\), and seed the approximate ordinary repair with \(\widetilde b^0=(I-\epsilon K)a_m=a_m-\epsilon\Upsilon_{m+1}\). This belongs to \(\operatorname{im}P\), as does \(z\). The capped contraction factor is \(q_M=M/\sqrt{4t+M^2}<1\) by [Round 102](real-amplitude-cap-102.md). The norm of the first capped Picard increment is at most \(2\) in normalized second norm, since the sole nonconstant seed component is the marked activation. Thus \(\|\widetilde b^0-z\|_{2,n}=O(q_M^m)\). The ordinary \(P(b_+)\) update and then the negative part are nonexpansive in that norm. Taking
\[
 m\ \ge\ (1/4+\kappa)\frac{\log n}{|\log q_M|},\qquad \kappa>0 ,
\]
gives every negative-row difference \(O(n^{-1/4-\kappa})\) with an error constant independent of the repair depth. At each fixed depth of the persistent window the actual positive mark is of order \(\sqrt n\). The pointwise mark error \(O(n^{1/4-\kappa})\) preserves its positivity. By (2) this explicit seed transfers \(nT\) at the required scale.

The resulting open arithmetic test uses logarithmic cap Picard height and both exact stationary factors. A uniformly approximating lower-height or fixed-complexity seed could instead use (4) or (5), and still needs an independent prime upper on the full masked functional. These estimates leave the critical rate premise in place.
