# The actual short-block pin removes all wrong-sign factors at collision scale

Use the actual near-critical selected short block of [Rounds 151 and 154](ordinary-lift-and-gauss-kernel-154.md), not an arbitrary capped law. Thus \(v\ne0\), \(\rho=-\sigma=\chi(v)\), and the physical \(f\) has the actual wrong-sector pin of [Round 153](ordinary-affine-jacobi-factorization-153.md). On
\[
 B_-=\{x\in Q\setminus\{1\}:\chi(1-x)=\sigma\}
\]
it gives \(f=c+e\) with
\[
 |c|=O(p^{-1/2}),\qquad
 \|e\|_{\ell^2(B_-)}=O(n^{-1/3}T^{-2/9}),\qquad n=(p-1)/2 ,
\]
in counting norm on the specified short block and its admissible \(T\). Write \(g=|f|^2\) extended by zero, \(w=g(1-g)\), and \(G=\sum g=O(\sqrt p)\). On \(B_-\), put \(M_-=\sup g\). Directly
\[
 \sum_{B_-}g=O(1),\qquad
 M_-=O(p^{-1}+p^{-2/3}T^{-4/9}).
\]
The more precise split \(g(s)\le2|c|^2+2|e(s)|^2\) is needed at the output of the full diagonal.

## Full positive diagonal

Remove the previously paid \(x=0,y=0\) boundary in weighted norm. On the remaining physical interior of [Round 173](ordinary-full-diagonal-two-pin-173.md), the actual four nonzero arguments \(A,C,Y,D\) all differ from \(1\). With \(s\ne0,1\), fixing any two different argument roles and their values gives at most two tuples. The remaining full positive diagonal kernel satisfies
\(\sup_s P_s\le2G^2\) and \(\sum_s P_s\le G^3\), by the two-argument and three-argument pins. These bounds do not need a sign restriction on \(s\).

The actual output contribution with \(s\in B_-\) is bounded by the pin split:
\[
 \sum_{s\in B_-}w(s)P_s^2
 \le 2|c|^2\sum_s P_s^2+2\|e\|_{\ell^2(B_-)}^2\sup_s P_s^2
 \ll p^{-1}G^5+p^{-2/3}T^{-4/9}G^4
 =O(p^{3/2}).
\]
Using only the crude \(O(1)\) wrong-output mass without this split would give a weaker estimate.

For a fixed input role \(j\) among \(A,C,Y,D\), restrict the corresponding nonnegative kernel \(P_{s,j}\) to that input in \(B_-\). Fix two of the other roles and use the at-most-two tuple bound, paying \(M_-\) on \(j\) and bounding the fourth factor by one. Then \(P_{s,j}\le2M_-G^2\) and
\[
 \sum_s w(s)P_{s,j}^2\ll M_-^2G^5=O(p^{7/6})
\]
for \(T\ge1\). Sum these four cuts by the triangle inequality in the weighted norm. Restoring the already priced endpoint errors, the \(O(p^{3/2})\) diagonal target is therefore equivalent in scale, on this actual branch, to the same positive criterion restricted to \(s,A,C,Y,D\) all in the favorable sign. With all four inputs favorable, \(u=(1-D)/(1-Y)\) is square automatically, and \(\chi(v)=\rho\) makes the reconstructed \(x,y\) squares. The output still has its actual amplitude weight. This is a physical restriction; applying it to \(g\) does not retain the original nonnegative Fourier coefficient law by default.

## Two-dimensional twisted collision

For the selected twisted kernel of Round 169, the four actual weighted arguments are \(C,Y,D,tE\) with \(E=A/s\), and \(s,t\ne0\). The fixed-\(s,t\) two-role pins are the same as above after rescaling \(tE\) by the fixed nonzero \(s/t\). Also \(\sup_s H_\alpha(s,t)\le2G^2\), \(\sum_s H_\alpha(s,t)\le G^3\), uniformly in \(t\). These are pins on the original interior; the Round 169 error costs for the boundary and Mellin regularization remain separate.

- Wrong outputs \(t\in B_-\) contribute at most \(O(G^5)\sum_{B_-}w(t)=O(p^{5/2})\).
- For any one wrong weighted input, the corresponding restricted kernel has pointwise bound \(O(M_-G^2)\) using the other two roles, and total \(s\)-mass at most \(G^3\). Thus its weighted squared norm summed in \(t\) is \(O(M_-G^6)=O(p^{7/3})\).

The tilted argument \(tE\) can equal \(1\) even for interior \(x,y\). This extra class also costs at most \(O(p^2)\), below the target \(O(p^{5/2})\). At fixed \(s,t\), \(tE=1\) fixes \(A=s/t\), so the \((A,C)\) pin and the \(C\)-mass give a pointwise bound \(O(G)\). At fixed \(t\), \(C,Y\) determine \(D=tCY\), then \(u,A,s\) uniquely, so the total \(s\)-mass is at most \(G^2\). The squared sum costs \(O(G^3)\) at fixed \(t\), hence \(O(G^4)\) after \(w(t)\). The other three factors already avoid \(1\), and \(w(1)=0\).

The twisted target is therefore likewise equivalent in scale to using favorable \(t,C,Y,D,tE\). No sign restriction on the auxiliary slope \(s\) itself follows, and the tilted argument \(tE\) cannot be replaced by \(A\) in this statement. The full sign-restricted collision estimate and separate zero-match contribution remain open.

## Size of the change in the Fourier law

For a character formulation one can keep the value at \(1\) and remove just the wrong sector. Set \(g^\sharp=g-g1_{B_-}\) and use the normalized Fourier coefficients on all characters. The actual wrong pin yields
\[
 \|g1_{B_-}\|_2\le2|c|^2\sqrt p+2\|e\|_2^2=O(p^{-1/2}),
 \qquad \|g1_{B_-}\|_1=O(1).
\]
By Parseval and Cauchy, the coefficient change from \(\omega\) to the coefficients of \(g^\sharp\) therefore has first norm \(O(p^{-1/2})\), and each individual change has modulus \(O(p^{-1})\) by the physical first norm. The same bounds hold when restricting \(w\) to its favorable sector because \(0\le w\le g\) and \(w(1)=0\). This quantifies the closeness of the coefficients to the original laws. It does not assert nonnegative coefficients for \(g^\sharp\).
