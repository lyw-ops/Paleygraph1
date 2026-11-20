# A twisted positive physical collision test for one match

Use the same full character group of order \(m=p-1\), actual law \(\omega\), bulk weight \(g=|f|^2\) extended by zero, \(w(t)=g(t)(1-g(t))\), and the same completed physical pairs and \(u\) square mask of [Round 166](ordinary-regular-character-collisions-166.md). In particular \(\sum_t w(t)\le\sum_t g(t)=m\omega(1)=O(\sqrt p)\). Keep the physical mark. The two independent lift sums in [Round 168](ordinary-one-match-positive-form-168.md) remain in the construction.

## Removing the Mellin regularization at the target norm

For a four-character tuple \(W\), let \(J_i(W;s)\) denote the unnormalized character integrand \(J(\overline{\alpha\gamma}\chi^i,\alpha\beta\gamma\delta)\mathscr T(s)\) of Round 166. Write \(J_{i,\mathrm{gen}}(W;s)\) for its regular Mellin inversion with both the outer tuple and inner frequency cuts. Thus its transform on a regular pair \((W,\psi)\) is exactly \(p^{3/2}\) times the regular Gauss phase including the selected moving factor. Retain the selected slot label \(a_k(W)\) from Round 168. Define the physical kernels
\[
 H_{k,\mathrm{gen}}(s,t)=\frac12\sum_i\mathbb E_W
             [J_{i,\mathrm{gen}}(W;s)a_k(W)(t/s)],\qquad
 H_k(s,t)=1_{s\ne1}\frac12\sum_i\mathbb E_W
             [J_i(W;s)a_k(W)(t/s)] .
\]
For each sign, sum its two kernels as \(H_{\sigma,\mathrm{gen}}\) and \(H_\sigma\). In the co-moving coordinate \(r=a_k/\psi\), restoring the selected moving factor multiplies the entire Fourier row \(\widetilde U_{\sigma,r}(t)\) by \(g_r\) or its conjugate. Off \(r=1\) this has modulus one. For \(r=1\) both expressions vanish since the regular Mellin cut includes the selected slot. By Mellin inversion the restored row is exactly \(p^{-3/2}\sum_s r(s) H_{\sigma,\mathrm{gen}}(s,t)\). Parseval in \(r\) therefore yields
\[
 \mathcal P_1=p^{-3}\sum_{s,t} w(t)\sum_\sigma
                                  |H_{\sigma,\mathrm{gen}}(s,t)|^2 .
\]

The replacement by \(H_k\) has squared cost \(O(p^{-1/2})\) in this normalized weighted norm. Indeed, for \(s\ne1\) the exceptional tuple contribution has modulus \(O(\sqrt p)\) after the expectation, since the Round 166 pointwise proof uses absolute values and the additional \(a_k(W)(t/s)\) has modulus one. Deleting at most four deficient Mellin frequencies on any regular tuple adds \(O(1)\) pointwise, also before that phase. At \(s=1\) the inner sum on regular tuples is, up to a character value at \(-1\), the Jacobi sum \(J(\beta\delta,\overline{\alpha\beta\gamma\delta})\). Its factors and product are nontrivial by the regular root exclusions. Thus its size is \(\sqrt p\), the outer Jacobi size is also \(\sqrt p\), and the retained regular inversion at \(s=1\) is \(O(p)\), including the \(O(1)\) inner-frequency correction. The one slope \(s=1\) therefore costs \(O(p^2)\) before multiplying by \(\sum_t w(t)\) and \(p^{-3}\). The \(m-1\) other slopes cost \(O(p^2)\) together. The two kernels within each sign are combined using the triangle inequality.

It follows that the sought \(\mathcal P_1=O(p^{-1/2})\) is equivalent in scale to
\[
 \sum_{s\ne1,t} w(t)\sum_\sigma |H_\sigma(s,t)|^2=O(p^{5/2}) .
\]
This equivalence concerns one-match only, with the same positive square-mask completion and all terms of the original actual weights.

## A dilation formula for one physical kernel

The additional phase replaces one of the actual four argument weights. For the plus slot \(\alpha\), write the raw physical pair coordinates as
\[
 A=1-vx,\quad C=1-vux,\quad Y=1-vy,\quad D=1-vuy,
 \qquad s=\frac{D A}{C Y}.
\]
The actual kernel is the nonnegative sum of \(g(tA/s)g(C)g(Y)g(D)\) over the completed inputs at fixed \(s\), with the original \(u\in Q\setminus\{1\}\). All four arguments of the untwisted pair must be nonzero since the character expansion extended every character by zero. The other three slots replace \(D\) by \(tD/s\), or \(C\) or \(Y\) by \(s/t\) times that argument. Swapping \(x,y\) and swapping \((A,C),(Y,D)\) internally by \(x\mapsto ux,y\mapsto uy,u\mapsto u^{-1}\) preserve the completed domains. Each swap sends \((s,t)\) to \((1/s,1/t)\) for the corresponding sign-changing slot. Their composition exchanges the two plus slots at fixed \((s,t)\). Since \(w(t)=w(1/t)\) and all \(H_k\ge0\), it suffices to estimate the single \(\alpha\) kernel in this criterion.

Set \(z=C/D=A/(sY)\). For \(s\ne1\) both \(z\) and \(sz\) differ from \(1\), since either equality forces the endpoints equal. With \(Y,D\ne1\), the common \(u\) equation gives
\[
 (1-zD)(1-Y)=(1-D)(1-szY),\quad
 \frac{1-D}{D}=\frac{1-z}{1-sz}\frac{1-Y}{Y}.
\]
Thus at fixed \(z\) the remaining sum is a multiplicative cross-correlation of \(g(Y)g(tzY)\) and \(g(D)g(zD)\) in the displaced reciprocal coordinates \((1-Y)/Y,(1-D)/D\). Retain the actual square condition on \(u=(1-D)/(1-Y)\), and exclude \(u=1\) and the reconstructed \(szY=1\) boundary at \(x=0\). In the permitted range the dilation is an injective function of \(s\) at fixed \(z\). The omitted \(Y=1\) or \(D=1\) case is \(y=0\); similarly \(A=1\) or \(C=1\) means \(x=0\). Each case costs \(O(\sqrt p)\), uniformly in \(s\ne1,t\): at fixed \(s\) the other endpoint both has nonzero arguments and each argument is injective as a nonconstant fractional-linear function of \(u\) away from poles. At least one surviving untwisted weight on that endpoint supplies \(\sum g=O(\sqrt p)\). This is again within the target weighted squared error.

For example, at fixed \(z\) the translated normalized kernels in the two reciprocal coordinates have counting first norm \(O(\sqrt p)\) and second norm \(O(p^{1/4})\). Dropping only the \(u\) mask positively, Young's inequality and the injective dilation give squared norm \(O(p^{3/2})\) over \(s\). Any (possibly \(t\)-dependent) group of \(O(p^{1/4})\) distinct \(z\) rows hence costs \(O(p^2)\) over \(s\), by the triangle inequality, and contributes at most \(O(p^{5/2})\) in the exact weighted criterion. The missing estimate is the full coupled weighted \(s,t,z,z'\) collision. The single-row bound alone does not supply it. The independent zero-match \(4+4\) class is still open.

In the expanded square the entire \(z=z'\) diagonal also costs at most the target. Let \(L_z=\sum_D g(D)g(zD)\), so \(L_z\le G:=\sum g=O(\sqrt p)\) and \(\sum_z L_z=G^2\). For fixed \(t\), the bare first norms of the two rows before dilation are at most \(L_{tz},L_z\), and their squared second norms are at most their first norms since they are bounded by one. Young gives the individual squared energy \(O(L_{tz}^2 L_z)\le G^2L_z\). Summing yields \(O(G^4)=O(p^2)\) for every \(t\), so the outer weight costs \(O(p^{5/2})\). The physical mask only decreases each of these nonnegative diagonal terms. This leaves different reciprocal-ratio rows \(z\ne z'\).

The square condition in this formulation is entirely a slope condition on a nonzero row. In fact \(g(C)g(D)g(Y)\ne0\) forces \(C,D,Y\in Q\), hence \(z\in Q\). With \(\lambda_z(s)=(1-z)/(1-sz)\),
\[
 u=\frac{1-D}{1-Y}=\lambda_z(s)\frac D Y .
\]
Therefore \(u\in Q\) if and only if \(\lambda_z(s)\in Q\). Also \(u=1\) would give \(D=Y\) and \(\lambda_z(s)=1\), hence \(s=1\); these slopes were deleted already. After the named endpoint errors are paid, each remaining row is a bare reciprocal multiplicative cross-correlation multiplied by \(1_{\lambda_z(s)\in Q}\) and restricted by \(szY\ne1\). Completing that last boundary changes only the already-priced \(x=0\) terms. For \(z\ne z'\), the two reciprocal dilation parameters at common slope obey the exact relation
\[
 \frac1{\lambda_{z'}(s)}
 =1+\frac{z'(1-z)}{z(1-z')}\left(\frac1{\lambda_z(s)}-1\right).
\]
The affine coefficient differs from \(1\). The off-diagonal next estimate can use these two distinct slopes in the common parameter \(1-s\), with both square masks in place.
