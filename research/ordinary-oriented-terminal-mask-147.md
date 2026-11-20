# The actual complementary terminal mask can be oriented by the Picard sign

Fix \(\tau>0\) and a growing marked time \(T\) with \(T+1\) in the actual simultaneous window. Use the true zero-start Picard orbit with physical root zero, \(s=-\sigma\), mean reserve \(M=M_T\), terminal increment \(g_T=\Phi(v_T)-\Phi(v_0)\), and \(G=\sqrt n\,g_T\ge0\). Expectations have divisor \(n\). As in [Round 145](ordinary-terminal-clipped-shift-145.md) use
\[
 \Xi=U_\sigma-\mathbf1-\frac{g_T-\mathbb E g_T}{2TM}\in V_\sigma,
 \qquad U_\sigma=\frac1{TM}\sum_{j=1}^{T} A_{\sigma,j},\quad
 A_{\sigma,j}=\frac{\Phi(v_j)+\sigma v_j}{2}.
\]
All \(A_{\sigma,j}\) are the actual nonnegative factors. Set \(U_{<T}=(TM)^{-1}\sum_{j=1}^{T-1}A_{\sigma,j}\), \(x_T=s\sqrt n\,v_T\), and \(Q_T=(x_T)_+\).

## Actual signed terminal balance

Let \(F,R\) be true opposite mean-one optima with roots \(q_s,q_{-s}\), and let \(\bar F=\sum_h\mu_h\tau_h F\) be supported as a mixture on near-cap shifts \(F_h\ge q_s-\epsilon\sqrt n\). Set \(\bar q=\bar F_0\), \(\lambda=1_{\rm bulk}\bar F\). Separating the last term in \(U_\sigma\) gives the exact identity
\[
 \Xi= U_{<T}-\mathbf1+\frac{\sigma v_T+\Phi(v_0)+\mathbb E g_T}{2TM}.
\]
Since \(\bar F\in \mathbf1+V_s\) and \(\Xi\in V_\sigma\), \(\mathbb E(\lambda\Xi)=-\bar q\Xi_0/n\), and therefore
\[
 \frac{\mathbb E(\lambda x_T)}{2T\sqrt n M}
 =\mathbb E(\lambda U_{<T})-1+\frac{\bar q(\Xi_0+1)}n
   +\frac{\mathbb E[\lambda(\Phi(v_0)+\mathbb E g_T)]}{2TM}.     \tag{1}
\]
Both row-dependent reserve terms on the right are nonnegative. The existing mark estimate gives \(\Xi_0+1=a/M+O_\tau(1+\sqrt n\,T^{-B-1})\) in a window with exponent \(B>0\), \(a\to1\), and \(\sqrt n M\le\sqrt{1+\tau}+o(1)\). Thus if \(q_s/\sqrt n\ge1+\eta\) on a prime subsequence, fix \(\sqrt{1+\tau}<1+\eta\) and let \(\epsilon=o(1)\). Uniformly in those near-cap mixtures and times, (1) gives
\[
 \liminf \frac{\mathbb E(\lambda x_T)}T
 \ \ge 2\bigl(1+\eta-\sqrt{1+\tau}\bigr)>0
\]
along the gap subsequence. The same lower bound holds with \(Q_T\) in place of \(x_T\). Conversely an upper \(o(T)\) for the signed terminal pair in (1), at near-optimal marks and one selectable growing time, would exclude a fixed gap of either sign by reciprocity.

The sign is the opposite direction to the positive averaged row, namely \(s=-\sigma\). It also follows from the endpoint \(T-1\), since for \(H=\sqrt n\,g_{T-1}\),
\[
 x_T=s\sqrt n\,v_1+sKH,\qquad
 \mathbb E(\bar F\,sKH)=\mathbb E(\bar F H)-\mathbb EH.
\]
The first term is of size \(O(1)\) uniformly by the physical Jacobi seed bound. Removing the output root costs \(O_{\tau,B}(T^{-B})\) in the signed pairing. This expresses the orientation as a sign of the true linear transported previous activation.

## The narrower complementary mask

Use the variables and true opposite overlap \(\mathbb E(\lambda R)\le C\epsilon\) of [Round 146](ordinary-near-cap-complementary-mask-146.md), and set
\[
 S^+=\{i\ne0:x_T(i)\ge cT,\ R_i\le\delta x_T(i)/T\}.
\]
The proof of that round's masked inequality applies with \(Q_T\) in place of \(G\), because \(Q_T\ge0\), \(\|Q_T\|_{2,n}\le\|\sqrt n v_T\|_{2,n}=O_\tau(\sqrt T)\), and (1) gives the requisite lower. Write \(X^\circ_j=1_{\{j\ne0\}}(F_j-L)_+\) and \(X_\mu^\circ=\sum_h\mu_h\tau_hX^\circ\). It gives the quantitative upper
\[
 \frac{\mathbb E(\lambda Q_T)}T
 \le c+C\epsilon/\delta+
 C_\tau T^{-1/2}\bigl(\sqrt L+\|1_{S^+}X_\mu^\circ\|_{2,n}
                       +\|\mu\|_{\ell^2}\bigr).                \tag{2}
\]
Under the gap hypothesis, at fixed sufficiently small \(c>0\), \(\delta\to0\), \(\epsilon=o(\delta)\), \(L=o(T)\), (2) forces the real masked collision to be at least a fixed multiple of \(T\) for every eligible choice. Its relative density is \(O_\tau(1/(c^2T))\). Off the physical mark, \(G=\sqrt{4\tau+x_T^2}-2\sqrt\tau\). On \(S^+\), \(G\ge x_T-2\sqrt\tau\). For large \(T\) this puts \(S^+\) inside the older unsigned complementary mask with thresholds \(c/2,2\delta\), and imposes the additional true orientation \(x_T>0\). An ordinary-prime bound for the new mask remains necessary.

The useful weighted difference formula on any actual mask \(S_0\) is
\[
 W_{S_0}(y,z)=\sum_i1_{S_0}(i)\mu_{y-i}\mu_{z-i},\qquad
 \|1_{S_0}X^\circ_\mu\|_{2,n}^2
   =\frac1n\sum_{y,z}X^\circ_yX^\circ_z W_{S_0}(y,z).
\]
There is only one masked common output. For the uniform law on \(A\) of size \(a\) this charges the diagonal by at most \(\|X^\circ\|_{2,n}^2/a\), and the off-diagonal by \(nK_{S_0}(A)/a^2\), where \(K_{S_0}(A)\) is the largest \(|S_0\cap(y-A)\cap(z-A)|\) among distinct contributing \(y,z\). In these off-diagonal terms \(R_y=R_z=0\) by exact complementarity of the original two optimizers. The concrete sufficient error regime is \(\sqrt n/a=o(T)\) and \(K_{S^+}(A)=o(a^2T/n)\). It is conditional on an actual suitable near-cap set and mask. Merely estimating the size of an ambient character pattern by \(n2^{-k}+O(k\sqrt p)\) cannot give its proposed required \(k\sqrt p=o(T)\) scale at any positive \(k\) in the proved growing marked window.

For the unshifted signed deleted tail, the same last-summand identity gives
\[
 \mathbb E(D\Xi)\ge -\mathbb E D
        -\frac{\mathbb E(DQ_T)}{2T\sqrt n M}.
\]
Here \(D=1_{\rm bulk}(F-L)_+\) lies on the true opposite zero set. Small mass and a small oriented weighted spike on this set would give the one-sided lower. These are additional arithmetic conditions, independently open from the direct signed cancellation.
