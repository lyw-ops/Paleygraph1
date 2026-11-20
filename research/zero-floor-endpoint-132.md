# A signed identity for the fixed-cap and ordinary means

Use the actual zero-floor capped row \(U=Ka\) and the actual cap-inactive bulk ordinary row \(Y=Kb\) of the [mixed-cap construction](zero-floor-ordinary-mixed-cap.md). They use the same marked cap \(M\) and marked floor \(n\). More generally write \(W\) for an actual averaged capped iterate, \(a=\Phi_0(C_M(W))\), \(\mu=\mathbb E_n a\) and \(r=Ka-W\), so \(r=0\) at the fixed point. Let \(\nu=\mathbb E_n b\), \(\eta=Y_0/b_0\), and \(\tau_i=\operatorname{sgn}Y_i\) on the bulk, with sign zero at zero. Use the two normalized ordinary factors \(F_\pm=(b\pm Y)/\nu\).

Define the exact ordinary weights
\[
 G=\frac{b-\eta Y}{\nu}
   =\frac{1-\eta}{2}F_++\frac{1+\eta}{2}F_-,
 \qquad J=\frac{Y-\eta b}{\nu}.
\]
In particular \(G\ge0\) and has mean one. On the bulk \(b=|Y|\), so \(J_i=\tau_iG_i\). Orthogonality of the sectors gives \(KJ=G-\mathbf1\), while \(J_0=0\) and \(G_0=n\nu/b_0\) since \(b_0^2-Y_0^2=n\nu^2\). Pairing \(r=Ka-W\) with \(J\) and moving the marked term gives the exact identity
\[
 \boxed{\quad
 \mu-\frac{a_0}{b_0}\nu
  =\mathbb E_n[1_{\{i\ne0\}}G(a-\tau W)]-\langle J,r\rangle_{2,n}.
 \quad}                                                        \tag{1}
\]
There is no division by a bulk entry. This holds at all primes, including ties and zero bulk entries.

At nonzero \(Y_i\), the integrand after removing \(G_i\) is \(-|h_i|\) if \(\tau_iW_i\ge0\), and \(2|C_M(W_i)|+|h_i|\) if \(\tau_iW_i<0\), where \(h=W-C_M(W)\). At zero \(Y_i\) the weight is zero. Consequently the endpoint direction is governed by
\[
 \text{weighted sign mismatch}\;-\;\text{weighted aligned spill}.
\]
The ratio \(a_0/b_0=1+O_M(n^{-1})\) uniformly for the fixed point and every iterate. Applied at \(U\), (1) yields an exact asymptotic test for the direction \(\limsup_p(\mu-\nu)\le0\). A sufficient test is that the positive mismatch term alone tends to zero. Agreement of both signs on the ordinary support immediately gives \(\mu\le\nu+O_M(n^{-1})\).

## Finite-height averaging and the second necessary contribution

In the genuine averaged recurrence \(W_{j+1}=W_j+r_j/2\), summing the last term of (1) leaves only \(-2\langle J,W_J\rangle_{2,n}/J\). This is \(O_M(J^{-1})\) uniformly. In fact \(J\) is the signed combination \(((1-\eta)F_+-(1+\eta)F_-)/2\). For each sign the quantities \(B_j^\epsilon=\epsilon\langle F_\epsilon,W_j\rangle_{2,n}\) satisfy the exact averaging recursion in the [weighted test](zero-floor-averaged-weighted-tail.md#the-actual-weighted-quantity-telescopes). Its forcing \(\mathbb E_n(F_\epsilon a_j)-\mu_j\) lies between \(-O_M(1)\) and \(O_M(1)\), by positivity, \(a_{j,i}\le M\) on the bulk, and \(F_\epsilon(0)\le1+\sqrt p\). The [uniform mean comparison](zero-floor-mean-131.md) bounds the difference of the averaged activation and the fixed activation mean by \(O_M(J^{-1/2})\). Thus the prime-first limit of the signed test through fixed horizons has exactly the same limsup as \(\mu-\nu\), with error vanishing as the horizon increases. The identity keeps the compensation between the two weighted contributions.

There is a separate restriction from the [quadratic energy comparison](zero-floor-ordinary-mixed-cap.md#energy-charged-only-to-the-actual-signed-bulk-spill). At the actual fixed point put \(A=\{i\ne0:|U_i|>M\}\), \(u=|h|\) and \(y=\operatorname{sgn}(U)Y\) there. Keeping the spill price in that comparison gives
\[
 (\mu-\nu)^2+\frac{1-q_{\rm mark}^2}{n}(U_0-Y_0)^2
 \ \le\ 
 2\mathbb E_n[1_A u(y-M-u/2)_+] .
\]
The unremoved terms on the right before taking the positive part are the negative half of this signed contribution and \(-4\mathbb E_n[1_{\{i\ne0\}}(C_M(U)Y)_-]\). The displayed upper therefore permits aligned overshoots below \(M+u/2\), unlike a bound on the entire positive overlap. It follows also from \(2u(y-M-u/2)_+\le 1_{\{y>M+u/2\}}(y-M)^2\).

In particular a positive endpoint gap \(\mu-\nu\ge c>0\) for arbitrarily large primes forces a definite positive weighted mismatch term by (1) and a definite shifted aligned spill term by the energy comparison. They are supported on disjoint sign sets. If the unweighted fixed-cap deficit tends to zero and one of the two ordinary theta ratios stays above \(1+\delta\), such a positive endpoint gap follows from the mixed-cap marked identity. Proving either needed arithmetic upper at one large cap with unweighted vanishing would then imply the original limit. Neither upper is established here.

## A reflection with a larger capped endpoint mean

For a seven-coordinate algebraic control, let \(v=(6,-8,3,-9,2,3,3)\) and let \(K=J_0-I+2vv^{\mathsf T}/\|v\|_2^2\), using the unnormalized Euclidean norm of the integer vector. Because \(v\perp\mathbf1\), this operator is symmetric and \(K^2=I-J_0\). In units where the marked activation is one, take \(m=1/4\) and the two rows
\[
\begin{aligned}
 U&=(-52/129,-19/86,121/516,-151/516,55/258,121/516,121/516),\\
 Y&=(-19/44,5/264,5/22,-21/44,5/24,5/22,5/22).
\end{aligned}
\]
Exact substitution gives \(U=Ka\) with \(a=(1,\min(|U_i|,m)_{i>0})\) and \(Y=Kb\) with \(b=(1,(|Y_i|)_{i>0})\). Their means are \(44/129\) and \(15/44\), with difference \(1/5676>0\). Both marked amplitudes exceed \(m\) in modulus. Scale both rows by \(L=8\sqrt{7/15}\) and set \(M=L/4\). Then the common marked floor is \(7\) because \(\sqrt{28+M^2}=L\), and the original clipped marked activation of both rows is exactly \(L\). The chosen bulk cap \(L\) on the second row is inactive. This proves a strict endpoint comparison failure for a non-Paley reflection under the actual nonlinear marked activation. It gives no prime-family counterexample.
