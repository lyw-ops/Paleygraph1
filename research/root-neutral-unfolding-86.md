# The actual floor unfolding at a root-neutral phase contact

Every finite unforced first spread contact on the cold square within the enlarged absolute sector, reached on a straight parameter ray in the closed spread chamber, admits local holomorphic continuation of the physical germ. This holds at any kernel dimension. Hermitian pairing of two Puiseux conjugates forces all earlier angular terms of a hypothetical fractional motion to tie across its active extremes. The separate bulk phase balances then exclude the motion. The same argument yields an explicit sufficient residual bound at a first contact on the actual height-600 forcing line. Uniform continuation after the branch leaves the chamber remains open.

## A real form on the actual phase extremes

Take an unforced first spread contact within the enlarged sector of [round 85](relative-phase-rotation-85.md), on the stated cold square. Write \(s_i=\pm1\) on the extreme sets \(S_\pm=\{i:\phi_i=c\pm\pi/4\}\) and \(S=S_+\cup S_-\). The marked site is outside \(S\) by the exact phase budget there. All linear kernel vectors \(h\) are supported on \(S\). Use
\[
 w=n/t,\qquad V=U/\sqrt t,\qquad
 F(V,w)=V-K\Psi(V,w),\quad
 \Psi_i=\sqrt{4+V_i^2}\ (i\ne0),\quad \Psi_0=\sqrt{4w+V_0^2}.
\]
The local square roots are the actual ones. The linearization \(L=I-KD\), \(D_i=V_i/\Psi_i\), is unchanged by this rescaling. Put \(\omega_i=h_i/\Psi_i\), and retain \(z_i\) and \(x_i=\Re z_i\) of the relative-factor coordinates.

For the rotation in round 85, write \(u=(I-i\tan c\,D)h\), \(v=\widetilde D u\). At contact \(u=Kv\), \(v=Ku\), and both rows have mean zero and support in \(S\). The two rows
\[
       f=u+v,\qquad g=i(u-v)
\]
have \(Kf=f\), \(Kg=-g\). At each active site they satisfy
\[
 f_i=s_i e^{2x_i}g_i,\qquad
 g_i=\frac{2i}{\cos c}\,e^{-x_i-is_i\pi/4}\omega_i .               \tag{1}
\]
Indeed \(u_i=2\cosh(z_i-ic)\omega_i/\cos c\) and \(v_i=2\sinh(z_i-ic)\omega_i/\cos c\). Conversely, if \(f,g\) have the stated sign, support and pointwise relation, put \(u=(f-ig)/2\) and \(v=(f+ig)/2\). These satisfy \(u=Kv\), \(v=Ku\), and \(v=\widetilde D u\) by \(\tanh(x_i+is_i\pi/4)=(s_i e^{2x_i}+i)/(s_i e^{2x_i}-i)\). The inverse rotation gives a kernel vector. Thus the kernel is isomorphic to the complexification of this real constrained pair space. A kernel basis can be chosen with \(g\) real.

For one such real direction put \(a_i=e^{x_i}g_i\) and \(\xi=(\cos c/2)e^{-i\pi/4}\). Then \(\omega_i=\xi a_i\) on \(S_+\) and \(\omega_i=-i\xi a_i\) on \(S_-\). Round 85's identities \(\sum_{S}\omega_i=0\) and \(\sum_{S}\omega_i^2=0\) give separate zero sums of \(a\) on the two sides and equal sums of its squares. The two real sectors also give the weighted zero sums \(\sum_S e^{-x_i}a_i=\sum_S s_ie^{x_i}a_i=0\).
In particular the bulk cubic of this real direction is
\[
            \sum_S\omega_i^3
                 =\xi^3\left(\sum_{S_+}a_i^3+i\sum_{S_-}a_i^3\right).  \tag{2}
\]
Its vanishing requires a separate signed cubic cancellation on each actual phase extreme set.

The physical branch from the positive real axis is invariant under frequency inversion \(i\mapsto-i\). The map \(F\) commutes with this reflection, and analytic continuation preserves the symmetry. Both \(D\) and the rotated equations at a contact therefore split into even and odd spaces. An odd-only kernel cannot obstruct continuation of the actual even row, since the even Jacobian is then invertible. In the real form (1) an odd direction has zero cubic in (2) by inversion, including zero at all self-inverse sites. For the physical unfolding one may therefore work throughout on the even space.

## An exact reduction with no direct floor dependence

Let the contact be \((V_*,w_*)\). For any right null \(h\), the transposed left null \(b=Dh\) obeys \(b^{\mathsf T}K=h^{\mathsf T}\). Both rows are supported on \(S\) off the mark. Consequently for every \(V\) near the contact, with \(\Delta V=V-V_*\), the **full** projected equation is
\[
 b^{\mathsf T}F(V,w)=
 \sum_{i\in S}h_i\left[D_i\Delta V_i-
        \bigl(\Psi_i(V_{*,i}+\Delta V_i)-\Psi_i(V_{*,i})\bigr)\right],       \tag{3}
\]
independent of \(w\) at fixed \(V\). In particular every partial derivative containing the explicit floor parameter vanishes under this projection. Dependence on \(w\) can still enter through the actual solution \(V(w)\). Fredholm solvability supplies a particular vector \(y\) with
\[
            Ly=K e_0\,2/\Psi_{*,0}.
\]
For \(\eta_i=y_i/\Psi_{*,i}\) on \(S\), one has \(\sum_{i\in S}\omega_i\eta_i=0\). To check it, the homogeneous factor variation of \(A=(\Psi+V)/2\) in direction \(h\) has mean zero in one Fourier sector. The variation of \(B=(\Psi-V)/2\) for total derivative \((y,1)\) lies in the opposite sector plus constants because the displayed equation for \(y\) is the differentiated stationary relation. On \(S\) these variations are \(A_i\omega_i\) and \(-B_i\eta_i\), with product \(-\omega_i\eta_i\). The first variation vanishes off \(S\), so ordinary opposite-sector orthogonality gives the claim.

## The corank-one discriminant and the marked jets

Suppose \(\ker L\) is one-dimensional, either on the full space or on the even space when continuing the physical row. Choose a fixed input complement of \(h\) and project the equation onto \(\operatorname{ran}L\) in that space. Its implicit solution has the form
\[
 V=V_*+\zeta h+Y(\zeta,\delta),\qquad
        \delta=w-w_*,\qquad Y(0,0)=Y_\zeta(0,0)=0.
\]
The derivative \(Y_\delta(0,0)\) is a particular vector \(y\) as above. Let
\[
       A_3=\sum_S\omega_i^3,\qquad
       B_3=\sum_S\omega_i^2\eta_i,\qquad
       C_3=\sum_S\omega_i\eta_i^2 .
\]
By (3) and \(\Psi_i''=4/\Psi_i^3\) on the bulk, the one remaining scalar equation has quadratic part
\[
              -2(A_3\zeta^2+2B_3\zeta\delta+C_3\delta^2).             \tag{4}
\]
The lack of explicit mixed or pure floor derivatives in (4) holds for the actual normalized equation, with the true marked source in \(y\). Replacing \(y\) by \(y+\tau h\) changes \(B_3,C_3\) to \(B_3+\tau A_3,C_3+2\tau B_3+\tau^2 A_3\), so the discriminant \(B_3^2-A_3 C_3\) is independent of this choice.

If \(A_3\ne0\), the analytic preparation in \(\zeta\) writes the remaining equation, up to a nonzero analytic factor, as
\[
              \zeta^2+P(\delta)\zeta+Q(\delta)=0,\qquad
 P(\delta)=2(B_3/A_3)\delta+O(\delta^2),\quad
 Q(\delta)=(C_3/A_3)\delta^2+O(\delta^3).
\]
In particular \(B_3^2-A_3C_3\ne0\) gives two analytic local branches through the singular contact, because their discriminant has order exactly two. An identically zero discriminant or any positive even order also gives analytic branches. If its order is odd, it is \(j\ge3\), and the two branch coordinates are \(\zeta_c(\delta)\pm O(\delta^{j/2})\) with \(\zeta_c=O(\delta)\).

The actual marked logarithm is the local analytic function \(\operatorname{arsinh}(V_0/(2\sqrt w))\). As a function of \((\zeta,\delta)\) its \(\zeta\) derivative vanishes at zero because \(h_0=Y_{\zeta,0}(0,0)=0\). On the two branches the even part in the square root of the discriminant is analytic in \(\delta\). The leading odd part has order at least \(1+j/2\), since the first derivative along \(\zeta_c(\delta)\) is \(O(\delta)\) and odd terms of degree three or higher cost at least order \(3j/2\). Thus the first possible marked fractional order on such a local branch is \(5/2\), also in \(t-t_*\), since \(w=n/t\) has nonzero local derivative. These discriminant estimates are local at the fixed field and conditional on \(A_3\ne0\).

## No ramification at a straight-ray first contact

Suppose the physical unforced germ approaches a finite first contact from the closed spread chamber on a straight \(t\)-ray. The following argument works whenever the mark is absent from the two phase extremes, even if the activation chart is singular. There is an analogous conclusion for a straight \(w=n/t\) ray because the change of parameters is locally invertible. For the cold square inside the enlarged absolute sector, the phase budgets exclude the mark from both extremes. [Actual phase budgets](astra-phase-86.md#the-actual-height-600-forcing-and-the-marked-phase)

The unforced factor pair \(A,B\) lies in complementary Fourier sectors plus constants, with \(A_i B_i=t_i\), where \(t_0=n\) and \(t_i=t\) off the mark. Its common mean is on the physical sheet \(\sqrt{W}\) with \(W=1+(1-1/n)t\). Over the right half-plane the algebraic factor family is proper with finite fibers by [the subset-sum compactness argument](astra-phase-86.md). Its physical normalization gives locally convergent Puiseux expansions at the contact. Both factors are nonzero, so take relative logs \(z_i=\log(A_i/\sqrt{t_i})\) in local charts centered at the actual phase lifts. A straight ray \(t-t_*=\gamma r\) with \(r>0,\ \gamma\ne0\) makes all expansions Puiseux in \(r\), and every conjugate has the same common mean \(\sqrt W\) by analyticity of this sheet near the contact.

If an incoming relative log has a noninteger power, let \(\alpha>0\) be the first such exponent across the row and \(\omega^{\mathrm{in}}\ne0\) the vector of its coefficients. All Puiseux conjugates have the same integer truncation \(C_i(r)\) through order \(\lfloor\alpha\rfloor\). Choose two conjugates \(z^{(1)},z^{(2)}\) whose coefficients at \(\alpha\) differ. The limit
\[
   \lim_{r\downarrow0} \frac{z^{(1)}-z^{(2)}}{r^\alpha}
\]
is a nonzero scalar multiple of \(\omega^{\mathrm{in}}\), since conjugation multiplies each coefficient of a given exponent by the same root of unity. The two \(A\)-factor differences and \(B\)-factor differences have zero mean and lie in opposite sectors. Their Hermitian pairing is zero. Substitution of \(A=\sqrt{t_i}\,e^{z_i}\), \(B=\sqrt{t_i}\,e^{-z_i}\), with the continuous lifts \(\phi_i^{(j)}=\Im z_i^{(j)}\), gives
\[
 \sum_i |t_i|\,e^{i(\phi_i^{(1)}+\phi_i^{(2)})}
             \left|\sinh\big((z_i^{(1)}-z_i^{(2)})/2\big)\right|^2=0.     \tag{5}
\]
Neither conjugate needs to lie in the chamber.

Let \(\phi_i^C=\Im C_i\), and let \(c(r)\) be the midpoint of the largest and smallest of these truncated phases. It is real analytic on the one-sided ray including its endpoint. Because the phases are finitely many real-analytic functions, a fixed index realizes each extremum for all sufficiently small positive \(r\), with identically tied indices interchangeable. The \(\phi_i^C\) are all \(O(r^\alpha)\) from the phases of the incoming sheet. Its spread bound implies every \(\cos(2(\phi_i^C-c))\ge-O(r^\alpha)\). Divide (5) by \(r^{2\alpha}\), rotate by \(e^{-2ic(r)}\), take real parts, and replace \(\phi_i^{(1)}+\phi_i^{(2)}\) by \(2\phi_i^C\). This gives
\[
  \sum_i \Lambda_i(r)\cos(2(\phi_i^C-c))=O(r^\alpha),\qquad
  \Lambda_i(r)=|t_i|\left|\frac{\sinh((z_i^{(1)}-z_i^{(2)})/2)}
                                     {r^\alpha}\right|^2.             \tag{6}
\]
The weights are bounded and nonnegative. At every site with \(\omega_i^{\mathrm{in}}\ne0\) they have a strictly positive limit. Since every summand is bounded below by \(-O(r^\alpha)\), (6) bounds each active cosine above by \(O(r^\alpha)\) as well. The cosine there is real analytic and therefore \(O(r^{\lceil\alpha\rceil})\). At \(r=0\) every active site consequently belongs to an extreme, and its center angle obeys
\[
            \phi_i^C=c(r)\pm\pi/4+O(r^{\lceil\alpha\rceil})
\]
with its original sign, by the nonzero derivative of the cosine at that extreme. No earlier integer angular term can open a margin between active opposite sites.

In the limit, the leading factor differences divided by their common scalar and by \(r^\alpha\) give \(A_*\omega^{\mathrm{in}}\) and \(-B_*\omega^{\mathrm{in}}\) in the opposite mean-zero sectors. Their ordinary pairing gives \(\sum_S(\omega_i^{\mathrm{in}})^2=0\) because the active weights \(t_i=t_*\) are all equal. The Hermitian pairing gives equal squared moduli on the two sides, so both are active. Pair the first limiting difference with \(B_*\), and also with \(\overline{B_*}\). The ordinary pairing gives the total bulk sum of \(\omega^{\mathrm{in}}\) equal to zero, and the Hermitian pairing gives the difference of its two side sums equal to zero because \(e^{2i\phi_i}\) has opposite signs up to a common phase. Thus the sums vanish separately.

Finally, chamber membership of the incoming branch and the preceding center estimate force the largest \(\Im\omega_i^{\mathrm{in}}\) on the active upper side to be at most the smallest on the active lower side. The separate zero sums force all these imaginary parts to vanish, and the sum of the real squares then forces \(\omega^{\mathrm{in}}=0\). This contradiction rules out every noninteger exponent, regardless of the Jacobian nullity or projected cubic. The physical factor germ continues holomorphically across the contact. This local result does not bound the width of the extended germs through primes and does not control their later phase spreads.

## A sufficient forced-contact bound with both extreme sets

At fixed \(t\) on the cold square consider a first spread contact along the true real forcing line at \(q=1-\lambda>0\), in the enlarged absolute sector. The completed factor family has finite, locally bounded fibers there. Its Puiseux conjugates at the same \(q\) have sector differences with equal means, because the completion adds the same residual correction to each corresponding factor on the two rows. Thus the left side of (5) equals \(-n|E(A^{(1)}-A^{(2)})|^2/4\). After division and rotation the added mean term on the left of (6) is nonnegative, since \(\cos(2c)>0\) at these contacts. The proof again forces the hypothetical first fractional angular direction \(y_i=\Im\omega_i\) to satisfy \(\max_{S_+'}y\le\min_{S_-'}y\) on its active sites \(S_s'=\{i\in S_s:\omega_i\ne0\}\). The leading factor differences define a true contact null. Both active sets are nonempty by the Hermitian null identity, and the ordinary null identity gives \(\|y\|_2=\|\omega\|_2/\sqrt{2}\) in unnormalized Euclidean norm.

Put \(m_s=|S_s'|\), \(m=m_++m_-\), \(Y_s=\sum_{S_s'} y_i\), and
\[
 \mathcal R=q\min_{\epsilon=\pm1}
     \left(\sum_{i\in S_+'\cup S_-'} e^{2\epsilon\Re z_i}|R_i|^2\right)^{1/2}.
\]
The two [actual signed source identities](astra-phase-86.md#separate-signed-sources-on-the-two-true-extreme-sets) give \(|Y_s|\le D_0=\mathcal R\|\omega\|_2/(2\sqrt{|t|})\). If the angular order holds, choose \(u\) between the two active extreme limits. The average on \(S_+'\) is at most \(u\), and that on \(S_-'\) is at least \(u\), so \(|u|\le D_0/\min(m_+,m_-)\). Moreover,
\[
 \sum_{S_+'\cup S_-'}|y_i-u|
     =(m_+-m_-)u+Y_--Y_+
     \le |m_+-m_-|\,|u|+2D_0 .
\]
Consequently a ramified incoming branch requires the following lower bound on the actual residual over the active support of its first fractional direction:
\[
 \mathcal R\ \ge\
 \frac{\sqrt{2|t|}}
      {\,2+(\sqrt{m}+|m_+-m_-|)/\min(m_+,m_-)\,}.                       \tag{7}
\]
A strict reverse inequality on every nonzero contact null is therefore sufficient for local continuation along this forcing line. In the even physical space the support can be counted using the orbit multiplicities. No prime-uniform upper bound on this restricted residual has been established.

For the unforced post-contact three-row form, a quick obstruction comes from its nonpositive orbit set. If that set has more than \(\operatorname{rank}N\) orbits, a nonzero vector supported there lies in \(\ker N\) and defeats positivity at that orientation. More precisely, write \(D=\operatorname{diag}\cos(2\phi_o-\beta)\), divide the orbits into \(P=\{D_{oo}>0\}\), \(J=P^c\), and use the matching columns \(N_P,N_J\). For \(b\ge0\), the exact criterion is
\[
       D_{JJ}+bN_J^*(I+bN_PD_{PP}^{-1}N_P^*)^{-1}N_J\succ0 .          \tag{8}
\]
Eliminating the positive block \(D_{PP}+bN_P^*N_P\) gives (8) by the matrix inversion identity, also when \(P\) is empty. This form keeps the damping from the positive bulk and reduces the remaining test to at most three orbits whenever the three-row form can succeed. The rank obstruction concerns this proof test; the physical Jacobian can still be controlled with more of the complementary sector equations.

1. On the physical unforced continuation, use (8) and the signed cross compression beyond the first contact to bound the subsequent phase interval through primes. The removal of first-contact ramification leaves later finite ramification at larger spreads open.
2. On the actual forced line, estimate the signed residual on the active extreme supports, using (7) or a stronger angular separation from the exact two sums. This can exclude ramification before the next phase interval.
