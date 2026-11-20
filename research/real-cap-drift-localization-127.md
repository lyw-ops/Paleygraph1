# Cap crossings and signed repair drift in the actual adjoint

Use the fixed real floor \(t>0\), cap \(M\), and sign of [Round 125](real-masked-cap-adjoint-125.md). Write \(A=\sqrt{M^2+4t}\), \(a_m=\Phi_t(C_M(U_m))\), and \(z_m=a_m-\epsilon U_{m+1}\), with \(U_{m+1}=Ka_m\). The exact capped fixed point and projected seed are \(U\) and \(z=\Phi_t(C_M(U))-\epsilon U\). Write \(b_{\ell,i},q_{\ell,i}\) for the actual ordinary repair and its negative part at cap height \(\ell\). The backward preimage \(r=r_{m,j}\) and the exact masked coefficient are those of Round 125. In particular the two true stationary factors and the exact deleted output are retained throughout.

All vector means and second norms are normalized. Put \(\delta a_m=a_{m+1}-a_m\) and \(\delta U_m=U_{m+1}-U_m\). By \(K\delta a_m=\delta U_{m+1}\) and self-adjointness, the exact Round 125 signed increment is
\[
 E_{m,j}:=n[T(q_{m+1,j})-T(q_{m,j})]
       =-n\langle r,\delta a_m\rangle_{2,n}
          +\epsilon n\langle r,\delta U_{m+1}\rangle_{2,n}.
 \tag{1}
\]
Both terms can therefore be tested on the same union of actual slope supports before any Jacobi transport. The direct term samples a clipped activation difference, while the transported term samples the next genuine cap Picard increment.

## A saturated initial seed and the true lag at cap height

At ordinary depth zero, \(r=M_0\mathcal A\) is supported on negative sites of \(z_m\) or \(z_{m+1}\). At a bulk site a nonzero \(\delta a_m\) implies at least one of \(U_m,U_{m+1}\) has magnitude below \(M\), because both saturated values have the same activation \(A\). If \(z_m<0\) and \(U_m\) is unsaturated, then \(\epsilon U_{m+1}>\sqrt{4t+U_m^2}\) and hence \(|\delta U_m|\ge A-M\). If \(z_m<0\) and \(U_m\) is saturated, then \(\epsilon U_{m+1}>A\), so \(\delta a_m=0\). If \(z_{m+1}<0\) and \(U_{m+1}\) is unsaturated, \(|\delta U_{m+1}|\ge A-M\). Finally if \(z_{m+1}<0\), \(U_{m+1}\) is saturated and \(\delta a_m\ne0\), then \(|U_m|<M\) and \(\epsilon U_{m+2}>A\). In all cases with a nonzero direct coefficient on the bulk,
\[
                  |\delta U_m|+|\delta U_{m+1}|\ge A-M .
 \tag{2}
\]
This is a statement about the **staggered** projected Picard seed. Replacing \(U_{m+1}\) in \(z_m\) by \(U_m\) would not give this exact seed. The marked direct activation difference is \(O(M^2 n^{-1/2})\), from the marked radicand \(4n+C_M(U)^2\).

## Direct terms after a fixed number of repairs

Fix \(0<s<A-M\), and choose \(\eta>0\) with \(2\eta\le s/2\) and \(\eta<A-M-s\). Let \(C_m\) be the actual subset on which at least one of \(|U_\ell-U|\), \(\ell=m,m+1,m+2\), exceeds \(\eta\). The genuine capped contraction gives
\[
           |C_m|/n\ll_{s,t,M} q_M^{2m}.
\]
Outside \(C_m\) we have \(|z_\ell-z|\le 2\eta\) for \(\ell=m,m+1\). At a bulk site with \(z\le s\), one necessarily has \(\epsilon U\ge A-s>M\). This follows because the uncapped branch on \(|U|\le M\) has \(z\ge A-M\), and the capped branch has \(z=A-\epsilon U\). Thus \(U_m,U_{m+1}\) are both saturated outside \(C_m\) here, so \(\delta a_m=0\).

At the remaining bulk sites outside \(C_m\) one has \(z>s\) and \(z_m,z_{m+1}\ge s/2\). For \(\ell=m,m+1\) define the cumulative actual negative row \(H_{\ell,i}=\sum_{h<i}q_{\ell,h}\). Ordinary projection gives exactly
\[
 b_{\ell,i}=z_\ell+\tfrac12
        (H_{\ell,i}-\epsilon K H_{\ell,i}+J_0H_{\ell,i}).
\]
Hence if \(b_{\ell,i}<0\) at one of these sites, then \(i\ge1\) and \(\epsilon(K H_{\ell,i})> s\). Consequently on the support of \(r\,\delta a_m\) the only bulk sites apart from \(C_m\) obey at least one of these true signed drift inequalities with \(\ell=m,m+1\) and \(1\le i\le j\). Nothing here assumes that the activated sets stay inside the initial spill.

Under the actual critical cap rate and \(q_M^m=O(n^{-1/4})\), Round 125 supplies \(\|r\|_\infty\ll_J n^{-1/2}\) for every fixed \(j\le J\). The direct part of (1) therefore satisfies the explicit estimate
\[
\begin{split}
 n|\langle r,\delta a_m\rangle_{2,n}|
 \ll_J\;& n^{-1}
       +\sqrt n\,\mathbb E_n[|\delta a_m|1_{C_m}]\\
 &+\frac{\sqrt n}{s^2}
       \sum_{\ell=m}^{m+1}\sum_{i=1}^{j}
           \mathbb E_n\big[|\delta a_m|(\epsilon K H_{\ell,i})_+^2\big].
\end{split}                                                     \tag{3}
\]
The first term pays the mark independently. The second may also be bounded by \(O(\sqrt n q_M^{2m})\) using the bounded activation difference. For \(j=0\), one can instead use the true adjacent crossing set (2) in this term and omit the double sum. For \(j>0\) the double sum retains the same actual signed transport that creates negative mass beyond the initial slack. Critical second-norm bounds alone allow a nonzero constant in (3). A stronger bound can use that \(\delta a_m\) vanishes on saturation and that the drift is tested only on its positive side.

Equation (1) leaves a separate signed sample of \(\delta U_{m+1}\) on the actual preimage. Sufficient conditions for this increment to be smaller than the critical scale are a subcritical bound in (3) and a subcritical corresponding signed sample, or a joint estimate with their signs carried from (1). The real endpoint and the finite signed prefix from a controlled lower height still require an independent prime estimate.

## Strict scalar contraction on large cap jumps

There is a separate necessary test for large increments of the masked statistic at critical cap height. Write \(q=q_M=M/\sqrt{4t+M^2}\) and, for \(0<d<M\), put
\[
 q_d=\frac{\sqrt{4t+M^2}-\sqrt{4t+(M-d)^2}}{d}<q,\qquad
 L_m=q^2\|\delta U_m\|_{2,n}^2-\|\delta U_{m+1}\|_{2,n}^2 .
\]
For \(|u-v|\ge d\), the absolute clipped activation secant on the bulk is at most \(q_d\). In fact the clipped magnitudes are in \([0,M]\) and differ by at most \(\min(M,|u-v|)\). Convexity of \(r\mapsto\sqrt{4t+r^2}\) on that interval bounds their difference in activation by the integral of its derivative over the rightmost interval of that length. The average derivative there decreases as the length grows to \(M\). Beyond \(M\), the full activation difference is divided by a still larger distance. The derivative is strictly increasing on \([0,M]\), giving \(q_d<q\). At the mark the same argument with \(n\ge t\) in place of \(t\) gives a bound at most as large.

Since \(K^2=I-J_0\), the actual next increment has squared norm \(\|\delta a_m\|_{2,n}^2-(\mathbb E_n\delta a_m)^2\). Subtracting from \(q^2\|\delta U_m\|_{2,n}^2\) proves the nonnegative loss inequality
\[
 L_m\ge(q^2-q_d^2)\,
       \mathbb E_n[|\delta U_m|^2 1_{\{|\delta U_m|\ge d\}}]
        +|\mathbb E_n\delta a_m|^2 .
 \tag{4}
\]
Under the critical cap rate and \(q^m=O(n^{-1/4})\), take \(d\) small and fixed. In the direct term of (1), \(|\delta a_m|\le q|\delta U_m|\), so the part with \(|\delta U_m|<d\) costs \(O_J(d)\) using \(\|r\|_{1,n}=O_J(n^{-1})\). On the complement, \(|\delta U_m|\le |\delta U_m|^2/d\). Using \(\|r\|_\infty=O_J(n^{-1/2})\) and (4) pays this part by \(O_J(\sqrt n L_m/[d(q^2-q_d^2)])\). The same split for the next Picard increment pays the transported term with \(L_{m+1}\). Thus
\[
 |E_{m,j}|
   \ll_J d+\frac{\sqrt n\,(L_m+L_{m+1})}{d(q^2-q_d^2)} .
 \tag{5}
\]
In particular if \(|E_{m,j}|\ge c>0\) along a subsequence of critical cap heights, choosing a sufficiently small fixed \(d\) gives a positive lower for \(\sqrt n(L_m+L_{m+1})\) on that subsequence. More directly, the split before using (4) pays the two large-jump contributions by \(\sqrt n/d\) times the sum of their normalized squared tail masses. If these scaled squared tail masses tend to zero for every fixed \(d>0\), taking the prime limit and then \(d\downarrow0\) gives \(E_{m,j}=o(1)\). The vanishing scaled losses are a sufficient condition for this tail estimate.

An analogous inequality to (4) holds for errors \(U_m-U\), by comparing the cap iterate to the true fixed point. In particular
\[
 |C_m|/n\ \le\ 
 \frac{\sum_{\ell=m}^{m+2}(q^2\|U_\ell-U\|_{2,n}^2-\|U_{\ell+1}-U\|_{2,n}^2)}
      {\eta^2(q^2-q_\eta^2)}
\]
when \(\eta<M\). This refines the lag cost in (3) using actual losses. Neither loss estimate asserts a prime gain for the full endpoint. For example, if an independently controlled endpoint with \(q^m=O(n^{-1/4})\) differs from the true obstruction value by a fixed positive amount in \(nT\), the tail bound \(O(n^{1/4}q^{m+k})=O(q^k)\) shows that this amount must already be detectable in a fixed number of further heights. By (5), some one of those two-step loss budgets has size \(\gtrsim n^{-1/2}\). Proving a uniform upper below this conditional lower remains open.
