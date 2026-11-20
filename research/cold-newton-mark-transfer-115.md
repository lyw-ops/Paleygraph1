# The marked derivative at the first corrected predictor

Use a genuine physical predictor \(V\) on the complex square of [Round 102](astra-resolvent-102.md). Keep its seed \(S\), \(R=K\Phi_t(V)-V\), \(D=\Phi_t'(V)\), \(A=I-KD\), \(Z=A^{-1}K\), \(H=A^{-1}R\), and frozen susceptibility \(P=fZe_0\), where \(f=-2n/(t\sqrt t\,\Phi_{t,0}(V_0))\). All physical sheets are those of that predictor. Assume the hypotheses of [the translated Newton construction](translated-newton-103.md), including a uniform coordinate bound on the first step inside the disks. Write \(r=\sup_Q\|R\|_{2,n}\), \(\delta_Z=O(n^{-\beta})\) for its maximum inverse entry, and assume \(n^{1-\beta}r^2=o(1)\). The construction gives the actual row \(Y=V+H+\ell\) with \(\sup_Q\|\ell\|_\infty=O(n^{1-\beta}r^2)\) and \(\sup_Q\|\ell\|_{2,n}=O(r)\). These are sufficient assumptions at a moving starter. No such starter through all primes is assumed known.

## Exact derivative of the corrected predictor

The exact Round 102 elimination has the linear residual already inside the corrected seed:
\[
 (1-\eta)P=Zb-\frac{2(V+H)-S}{2t\sqrt t}.
\]
Here \(b,\eta\) are the explicit Round 102 bulk preimage and scalar feedback. In particular a frozen cap can bound this actual combined expression with \(H\) of bounded size. Requiring \(H=o(1)\) as a separate input is one sufficient strategy for its linear term.

Put \(X=V/\sqrt t\) and \(G=H/\sqrt t\). In the normalized activation for \(X\), the entries under the radicals are \(4+X_i^2\) off the mark and \(4n/t+X_0^2\) at the mark. The derivative in \(X\) is \(D\); the partial derivative in \(t\) with \(X\) held fixed is exactly \(f e_0\). Thus \((R/\sqrt t)'=fKe_0-AX'\), where primes on the predictor or matrix mean total holomorphic derivatives. Differentiating \(AG=R/\sqrt t\) now gives the exact identity
\[
                  (X+G)'=P+Z D'G .                         \tag{1}
\]
On any fixed closed smaller square \(Q'\) in the interior of \(Q\), the Newton error is holomorphic and Cauchy's estimate gives
\[
 \sup_{Q'}\left\|\partial_t(Y/\sqrt t)-(P+ZD'G)\right\|_\infty
 \le C_{Q',Q}\, n^{1-\beta}r^2 .                           \tag{2}
\]
The bound uses a uniform positive distance to the outer boundary and the analytic square root on \(Q\). It proves transfer to the true stationary derivative on \(Q'\) at the quadratic Newton residual scale, given a suitable bound for the **combined** expression in (1). The original closed square requires an enlarged predictor domain to use this deduction at its boundary. On a smaller square centered on the same real point an angular cap follows by integration along its vertical segments whenever its half-width times the combined derivative bound lies below the required cutoff with fixed margin.

On such a smaller square the total derivative \(D'\) can also be replaced by a frozen diagonal, with only quadratic error. Write \(R_s=R/\sqrt t\). Its derivative satisfies \(X'=P-A^{-1}R_s'\), and Cauchy's estimate in normalized second norm gives \(\|R_s'\|_{2,n}=O_{Q',Q}(r)\). As a function of \(X,t\), the derivative of \(D\) in \(X\) is the diagonal \(\sqrt t\,\Phi_t''(V)\), and its partial derivative in \(t\) at fixed \(X\) is supported at the mark with size \(O(n^{-1/2})\) by the exceptional radicand. Thus, with \(C=\operatorname{diag}(\Phi_t''(V)P)\),
\[
 ZD'G=ZCH+O_{\infty,Q'}(n^{1-\beta}r^2+n^{-1/2-\beta}).
\]
Indeed the term with \(A^{-1}R_s'\) times \(H\) costs \(O(r^2)\) in normalized first norm by Cauchy–Schwarz and bounded curvature. The entry bound on \(Z\) gives the first coordinate-scale error. The explicit partial derivative of \(D\) multiplies the bounded marked first correction and only one column of \(Z\), giving the second error. It follows that
\[
 \sup_{Q'}\|\partial_t(Y/\sqrt t)-(P+ZCH)\|_\infty
       =O_{Q',Q}(n^{1-\beta}r^2+n^{-1/2-\beta}).             \tag{2a}
\]
This interior estimate needs neither an entry bound on \(Z C Z\) nor a separate small first correction. Its remaining estimate is a coordinate bound on the combined signed source \(P+ZCH\) at the same moving physical starter.

## Frozen transfer up to the full boundary under one diagonal bound

A related formulation avoids differentiating the predictor. Assume uniform scalar third derivative bounds on the disks containing the segments, \(\|Z_Y\|_{2\to2}=O(1)\) for the true \(Z_Y=(I-KD_Y)^{-1}K\), and \(\|P\|_\infty=O(1)\). For a full-boundary estimate require the genuine diagonal
\[
 C=\operatorname{diag}(\Phi_t''(V)P),\qquad
                         \|Z C Z\|_{\max}=O(n^{-\beta}).   \tag{3}
\]
These are additional assumptions. The norm on the right is a matrix entry maximum. The derivative \(P_Y=\partial_t(Y/\sqrt t)\) then satisfies
\[
 P_Y=\frac{f_Y}{f}\big[P+ZCH+O_{\infty}(n^{1-\beta}r^2)\big],\qquad f_Y/f=1+O(n^{-1}).            \tag{4}
\]
To see this, put \(E=D_Y-D\). The two-sided resolvent identity in [Round 105](frozen-entry-transfer-105.md) gives
\[
 P_Y=(f_Y/f)(P+ZEP+ZEZ_YEP).
\]
In counting second norm, the row of \(Z E\) and the vector \(E P\) have sizes \(O(n^{1/2-\beta}r)\) and \(O(n^{1/2}r)\). This gives the stated bound on the last term. Taylor expansion of \(D_Y-D\) leaves \(ZC(H+\ell)\) and one quadratic scalar remainder with normalized first norm \(O(r^2)\). The entry estimate bounds its output by \(O(n^{1-\beta}r^2)\). Finally \(\ell=Z B(H+\ell)\) exactly, with \(B\) the quadratic activation error from Newton. Hence (3) gives the same bound on \(ZC\ell\). The factor ratio follows from the bounded marked coordinates and the mark's radicand \(4n+V_0^2\).

Either formulation leaves a linear signed transport to be bounded on the actual predictor, and (4) additionally requires the two-column bound (3). These identities do not produce those prime estimates, construct a moving starter, or extend the original branch to all desired cold points. In particular, a condition on the ratio of counting and normalized residual scales cannot establish their failure.

## Independent Neumann cutoffs for the linear test

If the same starter has a uniform counting contraction \(\|KD\|_{2\to2}\le q_*<1\) and \(\|C\|_\infty=O(1)\), let \(L_j=\sum_{i<j}(KD)^iK\) and \(H_k=\sum_{i<k}(KD)^iR\). Split the difference as \((Z-L_j)CH_k+ZC(H-H_k)\). Counting second norm handles the first term and maximum entries of \(Z\) handle the second, yielding
\[
 \|ZCH-L_j C H_k\|_\infty
     \ll \sqrt n\,q_*^j r+n^{1-\beta}q_*^k r .
\]
At \(n^{(1-\beta)/2}r\to0\), it suffices to choose \(j\ge\beta\log n/(2|\log q_*|)\) and \(k\ge(1-\beta)\log n/(2|\log q_*|)\). The two lengths belong to distinct inverse uses at the *same* physical predictor. The finite signed term \(L_j C H_k\) still requires actual arithmetic representations and uniform packet and bad-character bounds up to both cutoffs. The counting contraction gives none of these resources by itself.
