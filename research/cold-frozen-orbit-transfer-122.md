# Frozen orbit estimates and transfer between genuine cold predictors

Let \(Q\) be the closed complex square in [Round 102](astra-resolvent-102.md). The physical map is \(F_t(W)=K\Phi_t(W)\), with the bulk radicals \(4t+W_i^2\) and the marked radical \(4n+W_0^2\) on the sheets of a genuine predictor \(V=V_m\). Use the normalized vector norms \(\|W\|_{a,n}=(n^{-1}\sum_i |W_i|^a)^{1/a}\), the counting matrix operator norms, and \(\|M\|_{\max}=\max_{i,j}|M_{ij}|\). The operator norm between second norms is the same for the two normalizations. Here \(\|K\|_{2\to2}\le 1\).

Put \(R=F_t(V)-V\), \(r=\sup_Q\|R\|_{2,n}\), \(D=\operatorname{diag}\Phi_t'(V)\), \(B=KD\), \(A=I-B\), \(Z=A^{-1}K\), and \(H=A^{-1}R\). Suppose the physical sheets are analytic about the coordinate disks of radius \(d>0\) around \(V_i(t)\), with a uniform curvature bound \(C\) and a uniform scalar first derivative bound \(0<q<1\) there. The predictor is holomorphic on a neighborhood of \(Q\). These assumptions give \(\|B\|_{2\to2}\le q\) and a second-norm contraction with factor \(q\) between any two vectors in these coordinate disks. All constants and little-oh estimates below are uniform in \(t\).

## Propagation of the actual Picard orbit

Fix \(0<\beta\le 1/2\) and suppose \(n^{1-\beta}r^2=o(1)\). For \(S_k=\sum_{j<k} B^jR\) assume
\[
 \sup_{Q,k\ge0}\|S_k\|_\infty\le d-\eta,\qquad
 \sup_{Q,j\ge0}\|B^jZ\|_{\max}\le C_Z n^{-\beta}
 \tag{1}
\]
for fixed \(\eta>0\) and \(C_Z<\infty\). Then for all sufficiently large \(n\) the actual orbit \(W_k=V_{m+k}\), with \(W_0=V\), stays on these sheets in the disks at every depth, and
\[
 \sup_{Q,k\ge0}\|W_k-V-S_k\|_\infty
      =O(n^{1-\beta}r^2),\qquad
 \sup_Q\|W_{k+1}-W_k\|_{2,n}\le q^k r .
 \tag{2}
\]

In fact let \(u_s=W_s-V\) and \(G_s=\Phi_t(V+u_s)-\Phi_t(V)-Du_s\). For a tentative first exit at step \(k\), only \(W_0,\ldots,W_{k-1}\) enter the right hand sides below, so their disk bounds are available. Contraction on every segment with endpoints already in the disks gives \(\|u_{s+1}-u_s\|_{2,n}\le q^s r\) for \(0\le s<k-1\), and \(\|u_s\|_{2,n}\le r/(1-q)\) for \(s<k\). For \(s=0\) the increment bound is the definition of \(r\). Taylor's formula and Cauchy–Schwarz give
\[
 \|G_s\|_{1,n}=O(r^2),\qquad
 \|G_{s+1}-G_s\|_{1,n}=O(q^s r^2).
\]
For the second estimate, the derivative of the Taylor remainder on each segment is bounded by \(C(|u_{s+1,i}|+|u_{s,i}|)\) at coordinate \(i\). The normalized second norms of this multiplier and the increment are \(O(r)\) and \(O(q^s r)\), respectively.

The exact recurrence \(u_{s+1}=R+Bu_s+KG_s\) and \(K=(I-B)Z\) give the summation by parts identity for \(k\ge1\),
\[
\begin{aligned}
u_k-S_k
 &= \sum_{s=0}^{k-1}B^{k-1-s} KG_s\\
 &= ZG_{k-1}-B^k ZG_0
       +\sum_{s=0}^{k-2}B^{k-1-s}Z(G_s-G_{s+1}).
\end{aligned}
\]
Here \(G_0=0\). Each matrix on the last line maps normalized first norm to maximum norm with cost at most \(C_Z n^{1-\beta}\). Summing the geometric difference bounds gives the first estimate of (2) with a constant independent of \(k\). The error is less than \(\eta\) for large \(n\), so (1) places the tentative step inside the disks. Induction proves confinement and the increment bound for every depth. Uniform convergence then follows from the increment bound and \(\|\cdot\|_\infty\le\sqrt n\|\cdot\|_{2,n}\) at each fixed prime. The limit is an actual stationary continuation of this Picard orbit, holomorphic in the interior of \(Q\).

The matrix hypothesis in (1) only needs the signed partial sums \(L_j=\sum_{\ell<j}B^\ell K\) through the cutoff \(\lceil\beta\log n/|\log q|\rceil\), since \(B^j Z=Z-L_j\) and \(\|B^j Z\|_{\max}\le q^j/(1-q)\). If \(\|H\|_\infty\le d-2\eta\), the signed \(S_k\) hypothesis likewise needs just the prefix through \(\lceil\beta\log n/(2|\log q|)\rceil\). Beyond it, \(S_k-H=-B^kH\) has maximum norm bounded by \(\sqrt n\,q^k r/(1-q)=o(1)\). The two cutoffs serve different inputs. This uses a supremum of shifted resolvents in place of a sum of the absolute entry bounds of all individual \(B^jK\).

The estimates in [Round 96](shifted-resolvent-96.md) already yield the shifted matrix input at the corresponding fixed depths. At heights 100 and 250 the weighted absolute column majorant is geometric with rate below one for all sufficiently large primes, so every tail has bound \(O(n^{-1/2})\). At height 600 use the same split \(h=\lfloor\log n/(2\log(1.048/0.514))\rfloor\) as in Round 96. For \(j<h\), sum the absolute column bound \(O(n^{-1/2}1.048^\ell)\) from \(\ell=j\) to \(h-1\), then add the counting tail \(O(0.514^h)\). For \(j\ge h\), the counting tail alone is at most \(O(0.514^h)\). This proves \(\sup_{j\ge0}\|B^jZ\|_{\max}=O(n^{-0.467})\) at that fixed depth. These bounds do not control the residual scale as \(n\) grows. The restriction \(\beta\le 1/2\) is intrinsic to the shifted input: \(Z-BZ=K\) and each row of the symmetric \(K\), with \(K^2=I-P_1\), has squared norm \(1-1/n\).

## Transfer of the corrected predictor

Let another genuine holomorphic predictor \(\widetilde V=V+s\) lie in the same coordinate disks, with \(\sup_Q\|s\|_{2,n}=O(r)\). Assume \(\sup_Q\|H\|_\infty=O(1)\) and \(\sup_Q\|Z\|_{\max}=O(n^{-\beta})\). In this part the shifted entry bounds in (1) are unnecessary. Define \(\widetilde D=D+E=\operatorname{diag}\Phi_t'(\widetilde V)\), \(\widetilde A=I-K\widetilde D\), \(\widetilde Z=\widetilde A^{-1}K\), and \(\widetilde H=\widetilde A^{-1}(F_t(\widetilde V)-\widetilde V)\). The disks give \(\|\widetilde Z\|_{2\to2}\le 1/(1-q)\).

With \(G(s)=\Phi_t(V+s)-\Phi_t(V)-Ds\), subtract \(\widetilde A(H-s)=R-As-KE(H-s)\) from \(\widetilde R=R-As+KG(s)\). The result is
\[
 \widetilde V+\widetilde H-V-H=\widetilde Z U,\qquad
 U=G(s)+E(H-s).
\]
Taylor's formula, \(\|H\|_{2,n}=O(r)\), and bounded coordinate norms give
\[
 \|U\|_{1,n}=O(r^2),\qquad
 \|U\|_{2,n}=O(r),\qquad
 \|(E_{ii})_i\|_{2,n}=O(r).
\]
The resolvent identity is \(\widetilde ZU=ZU+ZE\widetilde Z U\). The term \(ZU\) costs \(O(n^{1-\beta}r^2)\) in maximum norm. A row of \(ZE\) has counting second norm \(O(n^{1/2-\beta}r)\), and \(\widetilde ZU\) has counting second norm \(O(\sqrt n\,r)\). Their product has the same cost. Consequently
\[
 \sup_Q\|\widetilde V+\widetilde H-V-H\|_\infty
             =O(n^{1-\beta}r^2).
\]
This uses entrywise control only at the original predictor \(V\). Where the first part applies, it covers every actual \(\widetilde V=V_{m+k}\) with constants independent of \(k\), since their normalized displacement is at most \(r/(1-q)\). Dividing by the analytic \(\sqrt t\) and applying Cauchy's estimate gives the same scale for the difference of the corrected derivatives on each fixed smaller square, as in [Round 115](cold-newton-mark-transfer-115.md).

The prime estimates still needed are an admissible moving physical starter and signed partial sums and resolvent prices at that starter. [Round 103](translated-newton-103.md) gives existence via a translated Newton step under its own assumptions. The propagation bound above concerns the unmodified Picard trajectory. The transfer identifies corrected predictors at different admissible depths to quadratic accuracy.
