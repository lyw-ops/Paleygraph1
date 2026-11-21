# A fixed-depth averaged zero-floor weighted test

Research draft. Fix \(M>0\) and use the genuine capped zero-floor activation \(a(W)=\Phi_0(C_M(W))\), with the marked floor equal to \(n\). Write \(F_0(W)=Ka(W)\) and start the genuine averaged orbit at zero,
\[
                W_{j+1}=\tfrac12(W_j+F_0(W_j)),\qquad W_0=0 .
\]
Let \(F_\epsilon\) be any true nonnegative ordinary optimizer of mean one in the Fourier sector \(\epsilon\). In particular it can be taken from the [ordinary pair at zero floor](zero-floor-ordinary-mixed-cap.md). Write \(\lambda_\epsilon=\theta_\epsilon/\sqrt n\), so \(F_\epsilon(0)=\theta_\epsilon\) and \(K F_\epsilon=\epsilon(F_\epsilon-1)\). Inner products, means and vector norms use denominator \(n\).

For the \(j\)-th actual row set
\[
\begin{gathered}
 a_j=a(W_j),\qquad
 \mu_j=\mathbb E_n a_j,\qquad z_j=a_j-\epsilon W_j,\qquad
 r_j=K a_j-W_j,\\
 h_j=W_j-C_M(W_j),\qquad
 \alpha_j=\|h_j\|_{2,n}^2+2M\mathbb E_n|h_j|,\qquad
 T_{\epsilon,j}=1_{\{i\ne0\}}(\epsilon W_j-M)_+ .
\end{gathered}
\]
The negative part of \(z_j\) on the bulk is exactly \(T_{\epsilon,j}\). The mark is considered separately.

## The actual weighted quantity telescopes

Put \(B_j=\epsilon\langle F_\epsilon,W_j\rangle_{2,n}\). By applying the true sector identity to the actual averaged update, one obtains
\[
 \mathbb E_n(F_\epsilon z_j)
       =\mu_j+2(B_{j+1}-B_j),\qquad
 B_{j+1}=\tfrac12 B_j+\tfrac12\big(\mathbb E_n(F_\epsilon a_j)-\mu_j\big).
\]
For all primes, \(\|F_\epsilon\|_\infty\le1+\sqrt p\) by the entry bound and mean one. At the mark \(a_j(0)=2\sqrt n+O_M(n^{-1/2})\), while off it \(0\le a_j\le M\). Thus \(B_j\le M+C_M\) uniformly in the height and the prime, starting from \(B_0=0\). This uses the actual optimizer identity on the averaged map. A second-norm pairing with the unweighted iterate would lose a power of \(n\).

For a fixed finite horizon \(J\), write \(d_{\epsilon,J}=J^{-1}\sum_{j<J} z_j(0)/\sqrt n\). At sufficiently large primes the marks in this whole fixed horizon are positive, and \(d_{\epsilon,J}\to2\), as shown below. Then
\[
 \frac1J\sum_{j<J}\mathbb E_n(F_\epsilon T_{\epsilon,j})
 \ \ge\ \lambda_\epsilon d_{\epsilon,J}
             -\frac1J\sum_{j<J}\mu_j-\frac{2B_J}{J}.                \tag{1}
\]
Indeed the positive part of \(z_j\) contributes at least its marked value to the weighted pairing, and the only negative part is \(T_{\epsilon,j}\). Summation of the signed \(B\)-differences leaves just the one terminal charge.

## The mean reserve pays for an unweighted part of the spill

Since \(K^*K=I-J_0\), the exact midpoint norm identity is
\[
 \|W_{j+1}\|_{2,n}^2-\|W_j\|_{2,n}^2
       =2-\tfrac12\mu_j^2-\tfrac12\alpha_j-\tfrac14\|r_j\|_{2,n}^2 .
\]
The constant \(2\) is half the marked activation-squared term \(4n/n\). Consequently, writing an overline for the average over \(j<J\),
\[
 \overline{\mu}\ \le\
 2-\tfrac14\left(\overline{\alpha}+
            \tfrac12\overline{\|r_j\|_{2,n}^2}
            +\frac{2}{J}\|W_J\|_{2,n}^2\right).
\]
Here Cauchy–Schwarz gives \(\overline\mu\le\sqrt{\overline{\mu^2}}\), and \(\sqrt{4-x}\le2-x/4\) is the tangent bound. In (1) discard at most \((M/2)\mathbb E_n T_{\epsilon,j}\) from each term when replacing \(F_\epsilon\) by \((F_\epsilon-M/2)_+\). The reserve \(\overline\alpha/4\) alone pays this cost, since \(\alpha_j\ge2M\mathbb E_n T_{\epsilon,j}\). More explicitly, the exact deficit and residual terms give
\[
\begin{aligned}
 \mathbb E_n\!\left[(F_\epsilon-M/2)_+\ \overline{T_\epsilon}\right]
 \ \ge\ {}&\lambda_\epsilon d_{\epsilon,J}-2-\frac{2B_J}{J}\\
 &+\frac14\,\overline{\|h_j\|_{2,n}^2}
  +\frac M2\,\overline{\mathbb E_n(|h_j|-T_{\epsilon,j})}
  +\frac18\,\overline{\|r_j\|_{2,n}^2}+\frac{\|W_J\|_{2,n}^2}{2J}.
\end{aligned}                                                       \tag{2}
\]
The unweighted term includes the opposite sign and the marked spill. Every term on the second line is nonnegative. This argument requires no vanishing or critical rate on the actual cap deficit.

For each sign one can therefore prove the ordinary upper \(\limsup_p\lambda_\epsilon\le1\) by proving the double-limit bound
\[
 \liminf_{J\to\infty}\ \limsup_{p\to\infty}
       \mathbb E_n\!\left[(F_\epsilon-M/2)_+\ \overline{T_\epsilon}\right]
         =0                                                        \tag{3}
\]
at any fixed cap \(M\), along a sequence of large finite horizons. For a given horizon, one may select any true optimizer to test (3), because (2) holds for each one with the same \(B_J\) bound. The two signs give the original limit using the theta product. The same sufficient condition works with cap and horizon chosen in sequence, as long as \((M+C_M)/J\to0\) and the prime limit is taken separately with each pair held fixed. This replaces weighted comparison of two limiting rows with a test on actual finite zero-floor iterates and the high part of a true ordinary optimizer. It leaves a genuine arithmetic estimate for that high part.

## Fixed-depth marked limit, with the zero floor kept

Let \(g_M(w)=\min(|w|,M)\), \(x=\sqrt n K e_0\) and \(S=2x\). The actual marked replacement gives
\[
 W_{j+1}
   =\tfrac12\big(W_j+S+K g_M(W_j)\big)+O_{2,n,M}(n^{-1/2}).
\]
In fact the coefficient of \(Ke_0\) after subtracting \(2\sqrt n\) is \(O_M(1)\), because both clipped functions at the mark are bounded after that subtraction. The seed \(x\) is a bounded negative Mellin field. At each fixed \(j\), approximate \(W_j\) in normalized second norm by a bounded linear combination of negative Mellin fields. Inductively this holds at zero. For the update compare \(g_M(W_j)\) to the activation on the bounded approximant using the global Lipschitz bound. On the approximant's bounded range approximate \(g_M\) uniformly by an even polynomial. Transport of such a polynomial lies in the negative class up to the fixed-expression exceptional errors, which are \(O(n^{-1/2})\) at fixed expression. The added linear averaging and seed preserve that class. All polynomial choices are fixed before the prime limit. [Fixed-depth parity and transport](iteration-parity.md)

Now
\[
        (K g_M(W_j))_0/\sqrt n=\langle x,g_M(W_j)\rangle_{2,n}.
\]
Apply the same even polynomial approximation. The limiting mean of each term with the negative seed \(x\) is zero by odd parity. The bounded \(x\) controls the approximation error, followed by taking the approximation accuracy to zero after the field limit. The marked value of \(S/\sqrt n\) is \(2K_{00}=O(n^{-1/2})\). Thus the averaged recurrence gives \(W_j(0)/\sqrt n\to0\) for every fixed \(j\), and hence the claimed \(d_{\epsilon,J}\to2\) at every fixed \(J\). This argument does not justify using a prime-dependent horizon in the fixed-depth trace step.

The precise remaining task is (3) or a smaller valid upper on its actual weighted tail. At a small cap, the [zero-floor defect lower](zero-floor-mark-and-cap-budget.md) is consistent with a persistent weighted cost even in the absence of theta excess. The large-cap case remains open.
