# A terminal Jacobi charge on the actual marked window

Let \(p\equiv1\pmod4\) range over primes, \(n=(p-1)/2\), and let the floor \(\tau_p\) tend to zero. Use the exact undamped trajectory, \(g_t=\sqrt n\,\mu_t\), \(P_T=\sum_{t=1}^T(1-g_t)^2\), and \(E_t=\|v_t\|^2\) in counting Euclidean norm. Write \(L_2=\lim_p P_2\), \(m=2\sqrt2/\pi\), and \(\delta=1-m\). There is an absolute \(\eta>0\) such that, uniformly in \(3\le T\le D(p)\) in the proved marked window,
\[
P_T+\frac{E_{T+1}-E_1}{4}\ \ge\ L_2+\delta^2+\eta-o(1).
\tag{1}
\]
In particular any common additional scaled mean \(s\) giving nonnegative rows in the two sectors at the actual prescribed marks must satisfy
\[
2Ts+T(1-1/n)\tau_p\ \ge\ L_2+\delta^2+\eta-o(1).
\tag{2}
\]
The explicit lower bound \(0.022973-o(1)\) follows already from \(L_2+\delta^2\), compared with \(0.013037-o(1)\) from the first two deficits without the terminal term. A fixed positive increment is proved below using positivity of the actual immediately preceding activation. [Marked window and budgets](vanishing-floor-38.md) · [Second-mean bound](mean-energy-64.md)

## Retaining the whole terminal term

Let \(\mathbb E_p\) denote \(n^{-1}\sum_i\), and let all brackets and norms in the rest of the proof be normalized by \(n\). Set \(x=\sqrt n\,Ke_0\), \(V_t=\sqrt n\,v_t/2\), \(a_t=\sqrt{4+v_t(0)^2}/2\). Define \(W_t=V_t\) off the mark and \(W_t(0)=0\). Let \(\psi_t(i)=\sqrt{W_t(i)^2+\tau_p}\) off the mark and \(\psi_t(0)=0\). Then exactly
\[
V_{t+1}=a_t x+K\psi_t,\qquad
g_t=\mathbb E_p\psi_t+a_t/\sqrt n,\qquad
Kx=\sqrt n(e_0-\mathbf1/n).
\]
The marked theorem gives \(a_t=1+o(1)\) and \(\|V_t-W_t\|=o(1)\) uniformly through the window. The energy identity gives \(g_t=O(\sqrt{D(p)+1})\), so \(g_t/\sqrt n=o(1)\) there. Since \(K^2=I-J\) with \(J\) the averaging projector, it follows that
\[
\langle W_T,x\rangle=1+o(1),\qquad
\frac{E_{T+1}-E_1}{4}=\operatorname{Var}_p(\psi_T)+o(1).
\]
Indeed, \(\langle x,K\psi_t\rangle=-\mathbb E_p\psi_t/\sqrt n\) and \(\|x\|^2=1-1/n\). The starting energy satisfies \(E_1/4=(1-\sqrt{\tau_p/n})^2(1-1/n)=1+o(1)\). Thus the terminal part, including the last squared mean error, is
\[
(1-g_T)^2+\frac{E_{T+1}-E_1}{4}
=\mathbb E_p(\psi_T-1)^2+o(1).
\tag{3}
\]
This retains the next-state energy \(E_{T+1}\).

For all real \(f\), \(w\) and \(u\ge |w|\), completing the square gives
\[
(u-1)^2\ge fw-|f|-f^2/4.
\tag{4}
\]
Take \(u=\psi_T,\ w=W_T,\ f=2\delta x\). The Jacobi arcsine law gives \(\mathbb E_p|x|\to m\) and (4) yields \(\mathbb E_p(\psi_T-1)^2\ge\delta^2-o(1)\). This proves the explicit bound by using \(P_{T-1}\ge P_2\). The floor may vary throughout the proof because (4) uses \(\psi_T\ge |W_T|\). This use of the Jacobi law needs only its single marginal. [Jacobi equidistribution](https://arxiv.org/abs/1809.04286)

## The last activation cannot attain the scalar minimum

Write \(r_p=\sqrt{p/n}\) and \(Y_j=KT_j(x/r_p)\) for odd \(j\ge3\), using first-kind Chebyshev polynomials. For every finite family of such degrees their joint limit is the product of the averages of two independent Haar compact symplectic traces of matrix size \(j-1\) for each \(j\). The two-lift formula of round 23 gives the Mellin averages with vanishing errors for these odd degrees as well. After twisting at \(1\) the invariant stalk has rank one and its contribution is \(O_j(p^{-1/2})\), while the two convolution factors have dimension \(j-1\). Their group is symplectic by the self-duality sign computation. For fixed odd \(j\) the two factors are nonisomorphic up to translation by the singularity and the distinct inertia eigenvalues at zero. Across odd degrees the simple symplectic groups have different Lie algebra types or ranks. The joint group is their full product and the fixed-word argument works through varying primes. No extra independence with a later nonlinear iterate is used here. [Two-lift formula and joint groups](parallel-graph-shapes-23.md) · [Katz, Chapters 13 and 18](https://web.math.princeton.edu/~nmk/mellin331.pdf)

Take \(h\) proportional to \((Y_3-7/4)_+(-Y_5-7/2)_+\) off the mark, with \(h(0)=0\), normalized to have \(\mathbb E_p h=1\). Each selected compact endpoint lies in the support since both \(I\) and \(-I\) are symplectic. The limiting denominator is positive, so \(h\) is well defined with bounded normalized \(L^2\) norm through sufficiently large primes. Let \(z=Kh\), so \(\|z\|\le C\) for a fixed \(C\). The actual sign pairing satisfies
\[
\limsup_p\langle \operatorname{sgn}(x),z\rangle
\le -\frac7{3\pi}-\frac{14}{5\pi}<-\frac85 .
\tag{5}
\]
For this, use the cosine series of \(\operatorname{sgn}(\cos\theta)\) in \(L^2\), with odd Chebyshev coefficients \(4(-1)^{(j-1)/2}/(j\pi)\). At each cutoff the empirical squared approximation error tends to its limiting \(L^2\) value by boundedness, weak convergence and the fact that only the zero of \(x\) is a discontinuity. After applying \(K\), the tail in the pairing is bounded by this RMS error times \(\|h\|\). The \(j=1\) term has pairing \(O(p^{-1/2})\) because \(h(0)=0\) and \(Kx=\sqrt n(e_0-\mathbf1/n)\). All fixed \(j>5\) terms vanish in the limit by their independence from \((Y_3,Y_5)\) and their zero means. With only \(Y_3,Y_5\) left, the support of \(h\) and the signs of the coefficients give (5).

At every \(T\) in the window,
\[
\langle z,W_T\rangle
=-a_{T-1}/\sqrt n+\langle h,\psi_{T-1}\rangle
     -\mathbb E_p\psi_{T-1}+o(1)
\ge -g_{T-1}-o(1).
\tag{6}
\]
Here the equality follows from the exact recurrence and \(K^2=I-J\). Both \(\psi_{T-1}\) and \(h\) are nonnegative. Also \(\langle z,x\rangle=-1/\sqrt n\).

Suppose first that \(g_{T-1}\le6/5\). In (4) take \(f=2\delta x+\epsilon z\) with fixed \(\epsilon>0\). Its squared term adds at most \(\epsilon^2 C^2/4+o(1)\) to the charge over \(f=2\delta x\). For any fixed \(b>0\), the increase in the absolute-value term after subtracting its linear term \(\epsilon\langle \operatorname{sgn}(x),z\rangle\) is bounded above by
\[
2\epsilon C\,\sqrt{\mathbb P_p(|x|\le b)}
+\frac{\epsilon^2 C^2}{\delta b}.
\]
Indeed the remainder is at most \(2\epsilon|z|\) and vanishes when \(\epsilon|z|<2\delta|x|\). Use Cauchy–Schwarz on \(|x|\le b\), and \(\epsilon |z|\ge2\delta b\) on the other part of the remainder. First choose \(b\) so small that the limsup of \(2C\sqrt{\mathbb P_p(|x|\le b)}\) is less than \(1/10\) by the arcsine law. Then choose fixed \(\epsilon>0\) with \(\epsilon C^2((\delta b)^{-1}+1/4)<1/10\). The linear gain is at least \((2/5)\epsilon-o(1)\) by (5)–(6). In this case the terminal term in (3) is at least \(\delta^2+\epsilon/5-o(1)\).

If \(g_{T-1}>6/5\), then \(T\ge4\) for sufficiently large primes by the round-64 second-mean bound. The term with index \(T-1\) contributes more than \(1/25\) to \(P_{T-1}-P_2\), and the terminal term is still at least \(\delta^2-o(1)\). These two cases prove (1) with \(\eta=\min(\epsilon/5,1/25)>0\).

Finally the energy telescope gives \(2T(1-G)=P_T+(E_{T+1}-E_1)/4-T(1-1/n)\tau_p\), where \(G=T^{-1}\sum_{t=1}^Tg_t\). The product of the two actual marked entries is at least \(1-o(T^{-1})\) by the uniform marked theorem and the exact averaged endpoint identity. Complementarity of the Fourier sectors makes \((G+s)^2\) at least this product for any positive pair with those marks. This proves (2). Both (1) and (2) bound a necessary reserve, with no bound yet on the worst-site signed repair. [Exact budget and arbitrary completions](true-spill-63.md#a-necessary-whole-prefix-energy-bound-for-order-1t-allowance)

## Ranked next tests

1. Use several consecutive nonnegative activations in place of (6), retaining the actual \(K\) of each selected signed field and the common mean and energy terms. Test whether their lower charges grow over certified fixed prefixes, or whether a finite limiting budget is compatible with all these constraints. An unbounded lower charge would rule out every fixed \(C/T\) reserve in the late window.
2. At the same actual depth, bound the worst-site signed spill with a vanishing reserve. Passing requires both sectors to remain nonnegative with exact marks. The lower bound above can reject a reserve before testing that particular repair.
