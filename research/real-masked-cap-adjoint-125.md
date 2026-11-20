# The actual cap-increment test for fixed-depth masked repair

Fix the real floor, cap, sign, and two true stationary factors from [Round 123](real-masked-functional-stability-123.md). Let \(T(q)=\langle q,\mathcal A\rangle_{2,n}\) be its full-input, distinct, output-masked functional, with the exact coefficient \(\mathcal A\) of that round. In particular \(\|\mathcal A\|_\infty=O(n^{-1/2})\) and \(\|\mathcal A\|_{2,n}=O(n^{-3/4})\). All vector norms and inner products here are normalized, and all matrices in the adjoint calculation are real.

Let \(U_m\) be the true real capped Picard iterate from zero, \(a_m=\Phi_t(C_M(U_m))\), and \(z_m=(I-\epsilon K)a_m\). Thus \(U_{m+1}=Ka_m\). Write \(P=(I-\epsilon K+J_0)/2\), \(b_{m,0}=z_m\), and \(b_{m,j+1}=P(b_{m,j})_+\) for the ordinary repair started at this projected approximate seed. Write \(q_{m,j}=(b_{m,j})_-\). The actual capped fixed-point seed is \(z\), with ordinary repair \(b^j\) and negative row \(h_j\).

## Exact adjacent-cap test with the two actual active sets

For a transition \(m\) to \(m+1\), define the real diagonal \(D_m\) by scalar secants of the actual clipped activation between \(U_m\) and \(U_{m+1}\), with zero on coordinates where their difference is zero. It obeys \(\|D_m\|_\infty\le q_M=M/\sqrt{4t+M^2}<1\). Put \(\delta U_m=U_{m+1}-U_m\), so
\[
 z_{m+1}-z_m=(I-\epsilon K)D_m\delta U_m .
\]
At ordinary depth \(i\), define \(M_i\) by the negative part on the **two** rows \(b_{m+1,i},b_{m,i}\):
\[
 q_{m+1,i}-q_{m,i}=-M_i(b_{m+1,i}-b_{m,i}),\qquad 0\le M_i\le I .
\]
Use the scalar difference quotient where the two values differ and zero where they agree. The support of \(M_i\) is contained in the union of their negative sets. Their row difference belongs to \(\operatorname{im}P\), and on that space updates by the self-adjoint positive contraction \(S_i=I-PM_iP\).

For any fixed repair depth \(j\), set
\[
 W_{m,j}= S_0 S_1\cdots S_{j-1} P M_j\mathcal A
 \quad\text{in }\operatorname{im}P.
\]
Empty products are the identity. Taking the adjoint of the genuine difference evolution gives exactly
\[
 n[T(q_{m+1,j})-T(q_{m,j})]
 =-n\langle \delta U_m,D_m(I-\epsilon K)W_{m,j}\rangle_{2,n}.
 \tag{1}
\]
The order of the \(S_i\)'s in \(W_{m,j}\) is reversed from the forward product acting on the seed error. The coefficient contains the original output mask and both true factors. This identity retains the actual time-dependent negative-part slopes, while the rightmost tested source is one cap Picard increment.

## Bounds and a criterion for a lower-height calculation

Assume the actual critical rate \(\alpha=O(n^{-1/2})\). For \(0\le i\le J\) with fixed \(J\), the genuine low-slack set \(\{b^i\le s/2\}\) has size \(O_J(\sqrt n)\) for the fixed positive \(s\) of [Round 123](real-masked-functional-stability-123.md). The projected approximate seed and nonexpansive repair give \(\|b_{m,i}-b^i\|_{2,n}=O(q_M^m)\) uniformly in \(i\). A negative approximate site outside the genuine low-slack set therefore costs at least \(s^2/4\) in counting squared discrepancy. Consequently
\[
 |\operatorname{supp} M_i|=O_J(\sqrt n+n q_M^{2m}).
 \tag{2}
\]
Self-adjoint contraction gives \(\|W_{m,j}\|_{2,n}\le \|P M_j\mathcal A\|_{2,n}=O(n^{-3/4})\).
At \(q_M^m=O(n^{-1/4})\), there is also the actual maximum bound \(\|W_{m,j}\|_\infty=O_J(n^{-1/2})\). For this, (2) bounds every active support by \(O_J(\sqrt n)\), and \(\|P f\|_\infty\le \frac12(1+(1+\sqrt p)|\operatorname{supp}f|/n)\|f\|_\infty\). The starting \(P M_j\mathcal A\) has the desired bound, and each \(S_i v=v-PM_i v\) on \(\operatorname{im}P\) multiplies it by at most a bounded constant. On that space \(I-\epsilon K=2I-J_0\), so the full tested vector \(D_m(I-\epsilon K)W_{m,j}\) obeys the same maximum bound in this height range.

There is an exact sparse preimage for this test. Set \(v_j=P M_j\mathcal A\) and \(v_i=S_i v_{i+1}\) in the backward recursion. Then
\[
 W_{m,j}=P r_{m,j},\qquad
 r_{m,j}= M_j\mathcal A-\sum_{i=0}^{j-1}M_i v_{i+1}.
\]
Indeed \(v_i=v_{i+1}-P M_i v_{i+1}\). The identity \((I-\epsilon K)P=I-\epsilon K\) rewrites the tested vector in (1) as \(D_m(r_{m,j}-\epsilon K r_{m,j})\). At \(q_M^m=O(n^{-1/4})\) this preimage is supported on the union of the **actual** slope supports in (2), has mean absolute size \(O_J(n^{-1})\), and has maximum size \(O_J(n^{-1/2})\). The first-norm bound follows from its support and the maximum bounds just proved for all the backward rows. This gives a local term and a single signed transport of a sparse preimage for each cap increment. It does not assert that the advancing active sets have a common support across different \(m\).

By summing (1), the difference between the actual \(nT(h_j)\) and any finite cap-height version is exactly the signed sum of the adjoint tests for all subsequent cap increments. The sum converges at each prime by the capped contraction. Since \(\|\delta U_m\|_{2,n}=O(q_M^m)\), the standard absolute bound for the tail from \(m\ge L\) is \(O(n^{1/4}q_M^L)\). Thus it suffices to prove a one-sided arithmetic bound on a finite signed prefix and use the known tail past \(L=\lceil(1/4+\kappa)\log n/|\log q_M|\rceil\).

More concretely, suppose on an obstruction subsequence that the actual fixed-depth lower \(nT(h_j)\ge c_*>0\) holds, and a candidate shorter cap-height calculation gives \(nT(q_{m_0,j})\le c_*/4\). For large \(n\) let \(L\) be as above and assume \(m_0<L\). Then among the actual adjacent cap tests with \(m_0\le m<L\) at least one satisfies
\[
 -n\langle \delta U_m,D_m(I-\epsilon K)W_{m,j}\rangle_{2,n}
 \ge \frac{c_*}{2(L-m_0)} .
 \tag{3}
\]
Indeed the signed sum through \(L-1\) is \(n[T(q_{L,j})-T(q_{m_0,j})]\), which is at least \(c_*/2\) by the tail bound. The condition refers to the true two repair trajectories of adjacent cap iterates, without replacing their active sets by a fixed mask. Excluding (3) would require a genuine signed estimate on these vectors, or a shorter-height estimate sufficiently near the limit for another reason. No arithmetic bound below the obstruction lower has been supplied here.
