# Two opposite amplitude tails at an actual forced fold

On the full cold square of half-width \(2^{-17}\) about \(2031/128\), the genuine stationary section exists for \(10^{30}\le n\le10^{347}\), with \(|m_p|<3/\sqrt n\). Along the actual height-600 forcing line and within the enlarged absolute phase sector, every first right-angle spread contact has invertible Jacobian for \(n\ge10^{30}\) and \(p\le10^{692}\). At unbounded sizes a ramified first contact at \(q=1-\lambda>0\) with active counts within a factor \(3/2\) requires both large positive and large negative real log amplitudes. Each tail contains more than \(n/(2\sqrt p)\) distinct sites of the actual kernel support with \(|U_i|>891/q\). On the inner half-square one tail has an additional lower bound on \(e^{|\rho_i|}\) of order \(1/(q|\Im t|)\) for nonreal floors. The proofs use the coordinate geometry of the true prefix, both complementary Fourier equations and the residual's actual last preimage.

## The seed-centered disks on the complex square

Let \(p=2n+1\equiv1\pmod4\) be prime with \(n\ge10^{30}\), \(L=2031/128-2^{-17}\), \(Q\) the stated closed square and \(t\in Q\). Write \(V_{j+1}=K\Phi_t(V_j)\) for the physical nine-center prefix, \(R_j=V_{j+1}-V_j\), \(X=V_{600}\), \(R=R_{600}\) and \(r=\|R\|_{2,n}\) in normalized counting norm. The [actual prefix](astra-newton-77.md) has \(\|V_j\|_\infty<4.768\) and \(\|V_j-S\|_\infty< B=1.94\) through height 600, where the Jacobi seed \(S=2\sqrt n K e_0\) is real with \(\|S\|_\infty\le 2\sqrt{p/n}<s=2.828428\). Every straight segment between consecutive prefix rows stays in the same closed coordinate disks, including at the actual mark.

For one such segment coordinate \(v=x+iy\), set \(u=\sqrt{1-y^2/B^2}\). Then \(|x|\le s+Bu\) and \(|v|^2\le N(u)=s^2+B^2+2sBu\). Put \(C(u)=4L-2B^2(1-u^2)>0\). Since \(\Re(4t_i+v^2)\ge |v|^2+C(u)\), the squared derivative of the physical activation is at most \(N(u)/(N(u)+C(u))\). This uses \(t_0=n\) at the mark. The quotient increases throughout \(0\le u\le1\), because
\[
 N'C-NC'\ \ge\ 2sB(4L-2B^2)-4B^2(s+B)^2>0 .
\]
Its maximum at \(u=1\) gives \(|\Phi'_{t,i}(v)|<d=0.51358\) over the entire complex square. This maximum belongs to the rational upper comparison on the disks. The physical square-root branch is regular there since its argument has positive real part.

The [initial physical packet price](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) gives \(\|R_0\|_{2,n}\le\|R_0\|_\infty<0.169724\). The actual Jacobi operator contracts the second norm. The segment derivative just proved applies to exactly the 600 differences defining \(R\), so
\[
                   r<0.169724d^{600}<3.932\cdot10^{-175}.                 \tag{1}
\]
This is a finite-prime estimate with its lower threshold specified. For \(n\le10^{347}\), the unnormalized counting residual is below \(1/8\). On the closed counting ball of radius \(1/2\) around \(X\), the modulus and imaginary caps are \(5.268,2.44\). The coordinate derivative there is below \(2/3\), using \(M/\sqrt{4L+M^2-2b^2}\) for these caps. For every real \(0\le\lambda\le1\), the map \(U\mapsto K\Phi_t(U)-(1-\lambda)R\) sends the center to \(X+\lambda R\) and maps the ball strictly inside itself. Picard from \(X\) therefore converges uniformly in \(t\) and \(\lambda\), producing the holomorphic physical row in the interior of \(Q\), continuous on its closure and locally extendible there by the strict derivative margin. At \(\lambda=1\), real floors give the positive complementary factors, which identify the stationary branch. Its coordinate cap \(5.268\) gives the stated marked-log bound by \(m_p=\operatorname{arsinh}(U_0/(2\sqrt n))\). This extends the earlier complex cutoff \(n\le10^{321}\).

## An all-corank finite-prime exclusion on the forced line

Now allow all \(n\ge10^{30}\). Follow the same forcing germ in \(0\le\lambda\le1\) while all actual log phases remain in \(|\phi_i|\le\arctan(3/2)\). The [physical secant inequality](astra-imaginary-84.md#large-derivatives-at-height-600-beyond-unit-phase) reads
\[
 \sum_i\min(|U_i-X_i|^2,|U_i-X_i|)\le870n\lambda^2 r^2 .               \tag{2}
\]
At a first spread contact with diameter \(\pi/2\), the [marked-site bound](astra-phase-86.md) leaves both extremes in the bulk. On them \(|\sin\phi_i|\ge2/\sqrt{13}\), hence \(|\Im(e^{-i\arg(t)/2}U_i)|\ge4\sqrt L/\sqrt{13}\). The predictor has \(|\Im(e^{-i\arg(t)/2}X_i)|<2.00001\), so each extreme consumes more than \(2.4\) units in (2). If the Jacobian were singular, its [two complementary eigenrows](relative-phase-rotation-85.md#exact-rotation-of-the-linear-problem) give compression eigenvalues \(+1,-1\) on their joint support. Since \(|K_{ij}|\le\sqrt p/n\), the Frobenius estimate requires at least \(\sqrt2 n/\sqrt p\) sites. Consequently any singular first spread contact satisfies
\[
                 870\lambda^2\sqrt p\,r^2>2.4\sqrt2 .                  \tag{3}
\]
By (1), every such contact is regular for \(p\le10^{692}\), with no restriction on active-side counts or kernel parity. The [large-derivative Schur test](astra-imaginary-84.md#allowing-some-derivatives-larger-than-one) goes beyond spread contact in a smaller field range. There are at most \(3480n\lambda^2r^2\) sites with \(|\Phi'_i(U_i)|>3/5\) anywhere on the available enlarged-sector branch. If \(p\le10^{688}\), (1) makes their Jacobi compression norm below \(1/10\). With the full derivative bound \(3/2\) in this sector, that test excludes every Jacobian singularity along this part of the branch. Exit from the enlarged absolute sector is a separate event.

## The signed source seen by the two Fourier sectors

At any putative ramified first contact, fix a real log-kernel generator of the [actual contact real form](astra-forced-87.md). Write \(s_i=\pm1\) on the upper and lower extremes, \(\rho_i=\Re z_i\), and let \(a\) be its real amplitude vector. With full site multiplicities set
\[
 f_i=s_i e^{\rho_i}a_i,\qquad g_i=e^{-\rho_i}a_i,\qquad
 \gamma_a=\frac{[(\sum_+a_i)^2+(\sum_-a_i)^2]^{1/2}}{\sum_i|a_i|}.
\]
Both mean-zero rows vanish outside \(S_a=\operatorname{supp} a\) and satisfy \(Kf=f,\ Kg=-g\). The actual completed-factor identities give \(F=\sum f_iR_i,\ \sum g_iR_i=-vF\), with \(v=i e^{2ic}\), \(c\) the angular midpoint, \(|\Re v|\le5/13\) and \(|F|=2\sqrt{|t|}\gamma_a\|a\|_1/q\).

Use now the physical preimage \(H=\Phi_t(V_{600})-\Phi_t(V_{599})\), so that \(R=KH\). Symmetry gives \(\sum f_iH_i=F\) and \(\sum g_iH_i=vF\). The last [outward packet record](astra-adjoint-82-checks.jsonl) bounds \(\|H\|_\infty<0.005377\) by applying \(d\) to the previous increment. Specifically the round-82 majorant for height 600 equals the height-599 cumulative majorant times its last positive price \(1.04643288\ldots\), since the final five steps use the same right-end envelope. Dividing the certified majorant by this price recovers the one for \(R_{599}\); this division is on upper comparison products. The actual row \(H\) is real on real floors. On the concentric square of half-width \(2^{-18}\), vector-valued Cauchy on the outer square followed by vertical integration gives \(\|\Im H\|_\infty\le1410|\Im t|\), using the unrounded majorant.

In particular for any real \(\theta\), and arbitrary separate constants in \(Y=\sum f_i\Im(e^{-i\theta}H_i),\ Z=\sum g_i\Im(e^{-i\theta}H_i)\) by mean zero, one has the signed formula
\[
 |F|^2=\frac{Y^2+Z^2-2\Re(v)YZ}{(\Im v)^2}\le\frac{13}{8}(Y^2+Z^2).    \tag{4}
\]
The sign of its cross term uses the negative-sector equation for the *preimage*. More generally one may subtract any real row in the orthogonal complement of the plus sector from the tested profile in \(Y\), and any row in the orthogonal complement of the minus sector from the profile in \(Z\). These two choices need agree nowhere.

One explicit upper for these signed tests uses the physical amplitudes without a site maximum. For \(h=f,g\) let \(d_i=e^{\rho_i},e^{-\rho_i}\), respectively, and \(w_i=|h_i|/\|h\|_1\) on \(S_a\). Every atom has weight at most \(\kappa=\sqrt p/n\), since \(h=\pm Kh\); each of its positive and negative parts carries exactly half the probability. For any real tested row \(b\),
\[
 \frac{|\sum h_i b_i|}{\|a\|_1}
 =\frac{|\sum_i w_i\operatorname{sign}(h_i)b_i|}{\sum_i w_i/d_i}.       \tag{5}
\]
To upper bound (5) by \(D\), test both signs \(e=\pm1\) and sort \(e\operatorname{sign}(h_i)b_i-D/d_i\) on each of the two sign sets. In each sorted list put mass \(\kappa\) on the largest entries up to total mass \(1/2\), splitting the last atom if necessary. If the sum of the two weighted lists is nonpositive for both \(e\), the bound follows by linear maximization under the atom cap. The test can use different complementary-row subtractions in (4). It retains residual signs, amplitude signs and their simultaneous occurrence on the actual support.

## The two delocalized tails

The equal moduli \(|\sum fH|=|\sum gH|=|F|\) require **each** of \(h=f,g\) to satisfy
\[
 \frac{\|h\|_1}{\|a\|_1}\ \ge\ \frac{2\sqrt{|t|}\gamma_a}{q\|H\|_\infty}.
\]
For \(M>0\), \(T_h(M)=\{i\in S_a:d_i>M\}\) has
\[
   (1-\kappa|T_h(M)|)\|h\|_1\le M\|a\|_1 .                           \tag{6}
\]
Indeed the complement costs at most \(M\|a\|_1\), and each tail atom costs at most \(\kappa\|h\|_1\). Relations (4)–(6) apply to all real generators and all active-side ratios.

For a ramified contact let \(m_\pm\) count the active sites of the incoming square-root coefficient, \(m=m_++m_-\). If their ratio is at most \(3/2\) in either order, [the two projected cubic tests](astra-forced-87.md#a-counting-size-independent-test-for-the-true-active-support) furnish one generator with \(\gamma_a>0.3029\). In detail let \(\delta=|m_+-m_-|/m\le1/5\), let \(u\ne0\) separate the two incoming imaginary slopes, and take the real component that equals those slopes up to sign on the smaller side. Its sign-definite charge there is at least \(m(1-\delta)|u|/2\) and \(\|a\|_2^2\le m u^2(1+\delta+\delta/h_\delta)\), where \(h_\delta>0.368\). Now \(\|a\|_1\le\sqrt m\|a\|_2\) gives the claim, including equal counts.

For this generator both norm ratios exceed \(448/q\). By (6), the disjoint sets \(e^{\rho_i}>224/q\) and \(e^{-\rho_i}>224/q\) each contain more than \(n/(2\sqrt p)\) sites of \(S_a\). Every such site has \(|U_i|\ge\sqrt{|t|}(e^{|\rho_i|}-e^{-|\rho_i|})>891/q\). Adding their costs in (2) gives the explicit necessary inequality
\[
                     q\lambda^2\sqrt p\,r^2>1.01 .                      \tag{7}
\]
Since \(q=1-\lambda\), the product \(q\lambda^2\le4/27\). Equation (1) therefore excludes every ramified first contact in this active-count range for \(p\le10^{699}\). On the inner half-square (4) also gives \(\max(\|f\|_1,\|g\|_1)/\|a\|_1>0.000947/(q|\Im t|)\) for nonreal floors. Applying (6) to this larger factor requires one of the two signed tails to contain more than \(n/(2\sqrt p)\) sites with \(e^{|\rho_i|}>0.0004735/(q|\Im t|)\).

The [exact rational checker](astra-source-88-check.py) and [three replay records](astra-source-88-checks.jsonl) verify the numerical comparisons against the round-82 outputs. These estimates neither exhibit a physical fold nor bound \(\sqrt p\,r^2\) at unbounded order. A common complex cold section through all primes and the ordinary-theta asymptotic remain open.

1. Apply the signed test (5) with complementary-row subtractions to the two actual opposite tails. A bound uniform on both distributions, including the imbalanced active-count regime, would address the missing transverse source estimate.
2. Control the amplification of the true nonlinear stationary remainder through the predictor resolvent in a coordinate norm. The finite-prime normalized residual (1) and the post-contact Schur test control different parts of this problem.
