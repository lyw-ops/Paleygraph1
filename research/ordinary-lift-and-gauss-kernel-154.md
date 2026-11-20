# Two complete lifts and the favorable cross-ratio sector

Keep the genuine near-critical deficit \(b\), the true anchor law \(\nu=b/(nr)\), the two-lift law \(w\), and all conventions of [Round 153](ordinary-affine-jacobi-factorization-153.md). In particular \(b_0=0\), \(r=\mathbb E b>0\), \(m_{\rm eff}\sim n/\sqrt p\), \(\|L_\sigma b\|_{2,n}/r=o(1)\), and \(\max\nu=O(p^{-1/2})\). Let \(\mathcal M_p\) be the true-anchor restricted moment of [Round 152](ordinary-affine-correlations-152.md). Here \(\rho=-\sigma\), \(\chi(v)=\rho\), and all counting norms on the physical field have no divisor.

## The two complete moments differ by \(p+o(p)\)

Fix a supported full anchor \(\gamma\). In the affine extension \(h_\gamma(x)=f(1-vx)\overline{\gamma(1-vx)}\) let \(g\) be the square row and \(r'\) the nonsquare row identified with \(Q\) by a fixed nonsquare \(v_0\). Round 153 gives
\[
 \|g\|_2^2=O(\sqrt p),\quad \|\widehat g\|_\infty=O(\sqrt p),
 \qquad r'=R+e_\gamma,\quad
 \|\widehat R\|_\infty=O(1),\quad \|e_\gamma\|_2=o(1).
\]
The bounds are uniform on supported anchors. For \(u=v_0z\), \(z\in Q\), the complete correlation is
\[
 C_\gamma^{\rm full}(u)
 =1+\sum_{x\in Q}r'(zx)\overline{g(x)}
       +\sum_{x\in Q}g(v_0^2zx)\overline{r'(x)}.
\]
The counting squared norm in \(z\) of either cross term is \(O(\|g\|_2^2+p\|e_\gamma\|_2^2)=o(p)\) by multiplicative Parseval. Therefore \(\sum_{\chi(u)=-1}|C_\gamma^{\rm full}(u)|^2=n+o(p)\), uniformly. Define
\[
 M_e=\mathbb E_{\gamma\sim w}\sum_{u\ne0,1}\chi(u)^e
                                      |C_\gamma^{\rm full}(u)|^2,\qquad e=0,1.
\]
Then \(M_0-M_1=(1+o(1))p\). The true-anchor square correction from Round 153 gives \(M_0=\mathcal M_p+(3+o(1))p\) and \(M_1=\mathcal M_p+(2+o(1))p\). This controls the difference of the regular real phase averages at the required \(O(p^{-1/2})\) scale. It leaves the common upper open.

## The two-character Gauss kernel and its centered graph

Set \(m=p-1\), \(e_p(t)=\exp(2\pi i t/p)\), and \(\tau(A)=p^{-1/2}\sum_{z\ne0}A(z)e_p(z)\) on full characters, including \(\tau(1)=-p^{-1/2}\). Write
\[
 H_\gamma(U,V)=w_U w_V\,\tau(U/\gamma)\overline{\tau(V/\gamma)}
                                      \overline{\tau(U/V)},\qquad
 K_e(\xi,\eta)=\overline{\tau(\xi\chi^e)}\tau(\eta\chi^e)\tau(\xi/\eta).
\]
On regular tuples the normalized Jacobi product of Round 153, times its prescribed value at \(-1\), is exactly \(H_\gamma(U,V)\overline{H_\gamma(U',V')}K_e(U/U',V/V')\) with weights included. Use \(J(A,B)/\sqrt p=\tau(A)\tau(B)\overline{\tau(AB)}\) on its regular locus and \((\gamma/V)(-1)\tau(\gamma/V)=\overline{\tau(V/\gamma)}\). The full Gauss product on a canonically degenerate tuple has at least one \(\tau(1)\) factor and thus modulus at most \(p^{-1/2}\) before weights. The fixed-relation bound of Round 153 then puts its total normalized cost at \(O(p^{-1})\). The genuine degenerate Jacobi products cost \(O(p)\) in the unnormalized moment.

For \(x,y\in\mathbb F_p^\times\), take the minus transform of \(K_e\) and the plus transform \(\mathcal H_\gamma(x,y)=\sum_{U,V}H_\gamma(U,V)U(x)V(y)\). Orthogonality in \(\xi,\eta\) in the three Gauss sums sets their variables to \(A,xA,xyA\) with additive phase \(e_p(A[-1+x+xy])\). Hence
\[
 \widehat K_e(x,y)=\frac{m^2}{p^{3/2}}\chi(xy)^e
                                  \bigl(p\,1_{x(1+y)=1}-1\bigr).
\]
The Gauss product averaged over the four variables is \(m^{-2}\sum_{x,y}\widehat K_e|\mathcal H_\gamma|^2\). Parseval gives \(\sum_{x,y}|\mathcal H_\gamma|^2\le m^2(\sum_Uw_U^2)^2=O(p)\). In particular
\[
 \mathcal M_p=p\,\mathbb E_\gamma\sum_{\substack{x(1+y)=1\\xy\in Q}}
                         |\mathcal H_\gamma(x,y)|^2+O(p).
\]
The \(O(1)\) restriction bound on the right is the same open prime estimate in this representation.

In fact the graph can be unwound exactly. Put \(P_\gamma(t)=\sum_U w_U\tau(U/\gamma)\overline{U(t)}\), and \(Q_\gamma(t)=e_p(-t)P_\gamma(t)\). On the graph set \(s=1-x=xy\ne0,1\). Expanding \(\overline{\tau(U/V)}\) and changing its variable to \(xt\) gives \(p^{-1/2}\sum_{t\ne0}Q_\gamma(t)\overline{Q_\gamma(st)}\). By the two-lift inverse transform,
\[
 P_\gamma(t)=p^{-1/2}\overline{\gamma(t)}
                 \sum_z f(z)\overline{\gamma(z)}e_p(tz).
\]
Additive orthogonality in \(t\) now imposes \(z-1=s(z'-1)\). Removing \(t=0\) gives precisely
\[
 \mathcal H_\gamma(x,(1-x)/x)
    =p^{-1/2}\gamma(s)
           \left[C_\gamma^{\rm full}(s)-\frac{(n\nu_{\gamma|_Q})^2}{p}\right].
\]
In true-anchor probability \((n\nu_{\gamma|_Q})^2/p\to1\) with a uniform cap by Round 153. The nonsquare graph portion of \(\mathbb E_\gamma\sum|\mathcal H_\gamma|^2\) is consequently \(o(1)\), by the cross-term estimate above. This identity also explains why the graph formula alone cannot bound the square part.

There is a more precise comparison for the two *canonical* regular Gauss averages (only the Jacobi degeneracies removed). Their full Gauss difference is
\[
 2p^{-1/2}\,\mathbb E_\gamma\sum_{\substack{x(1+y)=1\\\chi(xy)=-1}}|\mathcal H_\gamma|^2
 -2p^{-3/2}\,\mathbb E_\gamma\sum_{\chi(xy)=-1}|\mathcal H_\gamma|^2.
\]
The first term is \(o(p^{-1/2})\). For the second, Parseval expresses the sum as \(m^2/4\) times the squared coefficient norm of \(H_\gamma(U\chi,V\chi)-H_\gamma(U,V)\). The simultaneous shift keeps the last \(\tau(U/V)\) and the weights fixed. On ratios \(\xi\notin\{1,\chi\}\), the unit ratio \(R_\chi(\xi)=\tau(\xi\chi)/\tau(\xi)\) has real part \(k(\xi|_Q)\) by the Gauss quotient for \(J(\xi,\chi)\) and the positive quadratic Gauss value for \(p\equiv1\bmod4\). The common-flat-set result from Round 152 therefore gives \(R_\chi(U/\gamma)\to\rho\) in probability for \(U\) drawn with normalized \(w_U^2\) and \(\gamma\) drawn with \(w_\gamma\). The exceptions have probability \(O(p^{-1/2})\) since the normalized squared law also has an \(O(p^{-1/2})\) cap. The same applies to \(V\). The bounded factors then give expected squared coefficient difference \(o((\sum_Uw_U^2)^2)=o(1/p)\). Thus the two canonical regular real averages differ by \(o(p^{-1/2})\). If extra fixed character relations are removed, the general comparison remains \(O(p^{-1/2})\).

For the untrimmed ratio law of independent true lifts the weights at \(1,\chi\) are both \(1/(2m_{\rm eff})\). Since \(R_\chi(1)=-\sqrt p\) and \(R_\chi(\chi)=-p^{-1/2}\), the untrimmed expectation is \(\rho-1+o(1)\). The exceptional contribution explains the apparent discrepancy with the regular near-alignment.

## The wrong Legendre sign costs \(O(p)\) at the selected actual step

Now assume \(b\) is on the actual short block selected in [Round 151](ordinary-retargeted-motion-151.md), still in the near-critical branch. This adds the quantitative estimate \(\|L_\sigma b\|_{2,n}/r=O(n^{-1/3}T^{-2/9})\). In the Round 152 cross-ratio expansion set \(A_u(x)=F_0(ux)\overline{F_0(x)}\), \(t=r_u(y)/r_u(x)\), and
\[
 Z(t)=\sum_{\substack{u\in Q\setminus\{1\},x,y\\ r_u(y)/r_u(x)=t}}
                                            A_u(x)\overline{A_u(y)}.
\]
All indices use contributing terms, so the two denominator factors are squares. On \(x\ne y\), \(1-t=v(u-1)(y-x)/[(1-vy)(1-vux)]\). The wrong sign \(\chi(1-t)=\sigma=-\rho\) is exactly \(\chi((u-1)(y-x))=-1\). The \(x=y\) terms have \(t=1\), and no other terms do by injectivity of \(r_u\).

On this wrong sector \(f(t)=c+e(t)\) by the exact pin of Round 153. Here \(c=O(p^{-1/2})\) and \(\|e\|_2\le\|L_\sigma b\|_{2,n}/r\) by multiplicative Parseval on that sector. The Mellin transform of \(Z\), with the convention \(\sum_t Z(t)a(t)\), is \(M_a=\sum_{u\ne1}|C_a(u)|^2\ge0\). Orthogonality and the pointwise multiplicative Fourier cap give
\[
  \mathbb E_{a\ {\rm uniform}}M_a=O(p),\qquad
  \max_a M_a\le\max|\widehat g_a|^2\,\|g_a\|_2^2=O(p^{3/2}),\qquad
  \|Z\|_2^2=\mathbb E_a M_a^2=O(p^{5/2}).
\]
This gives an absolute \(O(p^{11/12}T^{-2/9})=o(p)\) error from \(e\), uniformly over this block whenever the near-critical size holds.

For the \(c\) term, the signed mask gives the exact scalar
\[
 \sum_{\chi(1-t)=\sigma} Z(t)=\tfrac12
 \left(M_1-Z(1)-\sum_{u\ne1}\chi(u-1)\sum_{x,y}
                                A_u(x)\overline{A_u(y)}\,\chi(y-x)\right),
\]
where \(M_1\) here means the trivial-anchor Mellin coefficient. The first two contributions before multiplication by \(c\) are \(O(p^{3/2})\) and \(O(p)\). The last is \(O(\sqrt p\sum_u\|A_u\|_2^2)=O(p^{3/2})\) by the additive convolution norm \(\sqrt p\) of \(\chi\) and \(\sum_{u\ne1}\|A_u\|_2^2\le\|F_0\|_2^4=O(p)\). Thus the entire wrong-sign off-diagonal contributes \(O(p)\). The uniform-anchor diagonal also contributes \(O(p)\). The actual remaining test is an \(O(p)\) signed upper on the favorable off-diagonal \(\chi((u-1)(y-x))=+1\), with the original complex values of \(f\) and the true weights. The quantitative step bound is essential to this conclusion about the wrong sector.
