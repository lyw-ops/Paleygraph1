# The capped zero-floor mark and a necessary cap size

Research draft. Fix a bulk cap \(M>0\). At floor \(t\ge0\), use \(t_i=t\) off the mark \(0\), \(t_0=n\), and the actual capped map of [Round 102](real-amplitude-cap-102.md). Thus \(U_t=Ka_t\), \(a_{t,i}=(4t_i+C_M(U_t)_i^2)^{1/2}\), \(h_t=U_t-C_M(U_t)\), and \(\mu_t=\mathbb E_n a_t\). At \(t=0\) any actual capped fixed point can be used. Existence follows by taking a finite-dimensional limit of positive-floor capped fixed points, whose normalized second norms are bounded independently of the floor near zero. The means and vector norms use denominator \(n\).

## The actual capped mark is unique and uniformly continuous down to zero

Write \(q_{\rm mark}=M/\sqrt{4n+M^2}\). Comparing two actual fixed points at \(t,s\ge0\) gives
\[
\begin{aligned}
 |\mu_t-\mu_s|^2
 &+\mathbb E_n\!\left[1_{\{i\ne0\}}|h_t(i)-h_s(i)|^2\right]
   +\frac{1-q_{\rm mark}^2}{n}|U_t(0)-U_s(0)|^2\\
 &\hspace{14mm}\le 4(1-1/n)|\sqrt t-\sqrt s|^2 .
\end{aligned}                                                       \tag{1}
\]
Indeed, \(K^*K=I-J_0\) gives
\(\|U_t-U_s\|_{2,n}^2=\|a_t-a_s\|_{2,n}^2-|\mu_t-\mu_s|^2\).
At a bulk coordinate the reverse triangle inequality for the two vectors \((C_M(U)_i,2\sqrt t)\) gives
\[
 |a_{t,i}-a_{s,i}|^2
 \le |C_M(U_t)_i-C_M(U_s)_i|^2+4|\sqrt t-\sqrt s|^2 .
\]
Clipping and its signed remainder are both nondecreasing as real scalar functions. Therefore the difference of their squares obeys
\[
 |U_t(i)-U_s(i)|^2-|C_M(U_t)_i-C_M(U_s)_i|^2
 \ge |h_t(i)-h_s(i)|^2 .
\]
At the mark the floor is the same in both rows. Its scalar clipped activation is globally \(q_{\rm mark}\)-Lipschitz, and pays the marked loss directly. Averaging the two estimates proves (1).

In particular any two zero-floor fixed points have the same marked coordinate, activation mean and bulk spill. Their marked spill is equal as well, because their marked coordinates are equal. By the fixed-positive-floor marked limit of Round 102, for any sequence \(t_p\ge0\) tending to zero along the eligible primes, one gets
\[
                             U_{t_p}(0)/\sqrt n\ \longrightarrow\ 0 .  \tag{2}
\]
To justify the order of limits, compare first to a fixed \(s>0\). The limsup of the marked difference divided by \(\sqrt n\) is at most \(2\sqrt s\) by (1), since \(q_{\rm mark}\to0\). The marked coordinate at the fixed floor \(s\) divided by \(\sqrt n\) tends to zero. Then send \(s\downarrow0\). This is a capped marked statement. The original stationary mark and the capped spill are still separate quantities.

## An averaged zero-floor estimate without critical scaling

Let \(U\) be a zero-floor capped fixed point, \(F(W)=K\Phi_0(C_M(W))\), and \(W_{j+1}=(W_j+F(W_j))/2\) from \(W_0=0\). Write \(h(W)=W-C_M(W)\), \(\mu(W)=\mathbb E_n\Phi_0(C_M(W))\), and \(r(W)=F(W)-W\). The proof of (1) with a trial \(W\) compares \(\|W-U\|_{2,n}^2\) with \(\|F(W)-U\|_{2,n}^2\). In the bulk at zero floor there is an extra nonnegative loss
\[
 |C_M(W)_i-C_M(U)_i|^2-
       \big||C_M(W)_i|-|C_M(U)_i|\big|^2
       =4(C_M(W)_i C_M(U)_i)_- .
\]
Thus if \(D(W)\) denotes the three terms on the left of (1) for \(W,U\), plus \(4\mathbb E_n[1_{\{i\ne0\}}(C_M(W)_i C_M(U)_i)_-]\), the exact midpoint squared-norm identity yields
\[
 \|W_{j+1}-U\|_{2,n}^2
 \le \|W_j-U\|_{2,n}^2-\tfrac12 D(W_j)-\tfrac14\|r(W_j)\|_{2,n}^2 .
\]
Here \(D\) is a fixed-point comparison quantity. It uses the actual \(U\) even if several zero-floor fixed rows exist. Since \(\|U\|_{2,n}^2\le M^2+4\), for every prime and every \(L\ge1\),
\[
                     L^{-1}\sum_{j<L}D(W_j)\le 2(M^2+4)/L .
\]
This gives an \(O_M(L^{-1/2})\) bound in normalized second norm for the error of the averaged bulk signed spill. The same rate applies to the difference between the average of the mean activations and \(\mu_0\), and to the root-mean-square normalized marked error. The spill itself still requires an estimate on the actual finite-height averages.

## A small cap cannot have vanishing zero-floor defect

At zero floor put \(S=2\sqrt n\,Ke_0\) and \(\bar a=a_0^{\rm row}-2\sqrt n\,e_0\), where \(a_0^{\rm row}\) denotes the entire zero-floor activation row. Its entries lie in \([0,M]\) for all sufficiently large \(n\): on the bulk this is the clip, and on the mark the excess over \(2\sqrt n\) is at most \(M^2/(4\sqrt n)\). Set \(m_p=\mathbb E_n\bar a=\mu_0-2/\sqrt n\). Exactly,
\[
 \|U_0-S\|_{2,n}^2
 =\|K\bar a\|_{2,n}^2
 =\mathbb E_n\bar a^2-m_p^2 \le m_p(M-m_p).
\]
Writing \(g_M(w)=\min(|w|,M)\), the mark replacement in its empirical mean is \(O_M(n^{-1})\). Since \(g_M\) is one-Lipschitz,
\[
 m_p\le \mathbb E_n g_M(S)+\sqrt{m_p(M-m_p)}+O_M(n^{-1}).           \tag{3}
\]
The seed \(S\) has empirical law tending to \(2\sqrt2\cos\theta\) for uniform \(\theta\), by quadratic Jacobi equidistribution. In the lift formula the two characters over a quotient point give conjugate normalized Jacobi sums, outside the two exceptional lifts. Their real parts agree, so averaging over the quotient gives the same limit for \(g_M\). [Lift convention](fourier.md) · [Ping Xi, fixed-character Jacobi equidistribution](https://arxiv.org/abs/1809.04286)

There is a sharper lower bound on the defect from the exact seed pairing. Self-adjointness and \(KS=2\sqrt n(e_0-\mathbf1/n)\) give
\[
 \langle S,U_0\rangle_{2,n}
       =\frac{2}{\sqrt n}(a_{0,0}-\mu_0)=4+O_M(n^{-1/2}) .
\]
Split \(U_0=C_M(U_0)+h_0\). The signed spill costs at most
\(\|S\|_\infty\|h_0\|_{1,n}\le (\sqrt{p/n}/M)\alpha_0\), since
\(\alpha_0=4-\mu_0^2=\|h_0\|_{2,n}^2+2M\|h_0\|_{1,n}\).
For \(M\ge2\), put \(f=g_M(U_0)\), so \(0\le f\le M\) and \(\mathbb E_n f\le\mu_0\le2\), since the marked activation dominates the clipped magnitude. At any \(\tau\ge0\) the pointwise split at \(|S|=\tau\) gives
\[
 \langle S,C_M(U_0)\rangle_{2,n}\le\mathbb E_n(|S|f)
 \le \tau\mathbb E_n f+M\mathbb E_n(|S|-\tau)_+ .
\]
Choose \(\tau=2\sqrt2\cos(\pi/M)\). The mass above \(\tau\) for \(2\sqrt2|\cos\theta|\) is \(2/M\), so the limit of the right side with mean \(2\) is the integral over that part multiplied by \(M\). This proves
\[
 4\le \frac{4\sqrt2 M}{\pi}\sin\frac{\pi}{M}
             +\frac{\sqrt2}{M}\liminf_{p\to\infty}\alpha_0(p) .
 \tag{4}
\]
For \(2\le M\le9/4\) the first term in (4) increases with \(M\), since \(\sin x-x\cos x\ge0\) for \(0\le x\le\pi/2\). At \(M=9/4\) the term is \(9\sqrt2\cos(\pi/18)/\pi<3.991\), using the quartic cosine upper with \(3.14159<\pi<3.14160\). Thus \(\liminf\alpha_0(p)>0.012\) for each such fixed cap. For \(M<2\), the mean bound \(\mu_0\le M+2/\sqrt n\) already gives \(\liminf\alpha_0(p)\ge4-M^2>0\).

This rules out these small caps in a zero-defect argument. The cap \(M=10\) in the weighted spill route is outside the obstruction. Moreover if a cap does have \(\mu_0\to2\) on a subsequence, the direct Lipschitz step of (3) forces \(\liminf\|U_0-S\|_{2,n}\ge2-I(M)>0\) on it, since \(I(M)\le 4\sqrt2/\pi<2\). An estimate of the marked seed alone therefore leaves a nonzero bulk feedback to control.

## A rate-free comparison between true caps

At any common nonnegative floor, compare actual fixed points for two caps \(M>N>0\). Denote their means, clipped rows and signed spills by \(\mu_M,C_M,h_M\) and \(\mu_N,C_N,h_N\), where now each clipped row is evaluated at its own actual fixed point. Since the scalar activation at any coordinate is one-Lipschitz in the clipped value, the normalized squared norm identity for \(K\) yields
\[
 |\mu_M-\mu_N|^2+\|h_M-h_N\|_{2,n}^2
       \le -2\langle h_M-h_N,C_M-C_N\rangle_{2,n}.
\]
At every coordinate \(h_M C_M=M|h_M|\) and \(h_M C_N\le N|h_M|\). The corresponding inequalities for \(h_N\) give
\[
 |\mu_M-\mu_N|^2+\|h_M-h_N\|_{2,n}^2
 \ \le\ 2(M-N)\bigl(\|h_N\|_{1,n}-\|h_M\|_{1,n}\bigr).             \tag{5}
\]
In particular the actual spill first norm is nonincreasing in the cap. This is valid for any zero-floor fixed point at either cap, since the true means and spills are unique there. The estimate controls the variation of the actual means and signed spills in the cap parameter. It does not control the value of the defect at the larger cap in the prime-first limit.
