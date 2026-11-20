# Old-slack dissipation on the ordinary projected orbit

Use the original actual orbit \(b^{j+1}=P(b^j)_+\) of [Round 108](iterated-sector-projection-108.md), with \(P=(I-\epsilon K+J)/2\). This is the ordinary projection update, separate from the reflected \(P|b|\) in Round 119. Write \(u_j=(b^j)_+\), \(h_j=(b^j)_-\), and \(w_j=(I-P)h_j\). Then \(b^{j+1}=u_j-w_j\) and \(h_{j+1}=(w_j-u_j)_+\). Orthogonality of \(P\) and the scalar slack identity give
\[
 \|h_j\|_{2,n}^2-\|h_{j+1}\|_{2,n}^2
   =\|Ph_j\|_{2,n}^2+\|(w_j)_-\|_{2,n}^2
    +\|\min((w_j)_+,u_j)\|_{2,n}^2+2\mathbb E_n(u_jh_{j+1}).
\]
Thus the total positive old-slack charge in the original orbit is at most half the genuine initial squared spill. This exact identity has no cap-rate hypothesis. It recovers the usual projection dissipation and separately identifies the mass arriving against positive old slack.

Under the actual [Round 109](persistent-repair-deficit-109.md) critical-rate marked obstruction, choose a late index with loss \(O(n^{-1})\) by averaging. Then \(\|h_{j+1}-h_j\|_{2,n}\le\|Ph_j\|_{2,n}=O(n^{-1/2})\). The true favored pairing and bounded amplitude give \(\asymp\sqrt n\) sites with both \(h_{j+1}\) above a fixed positive threshold and the true favored factor above a fixed multiple of \(\sqrt n\). The positive old slack on these sites sums to \(O(1)\) by the exact dissipation. At a cost of \(O(n^\sigma)=o(\sqrt n)\) sites one can keep only old slack \(\le n^{-\sigma}\), \(0<\sigma<1/2\). Also, on all but \(O(1)\) of them \(h_j\) was above half the original threshold, by the actual one-step second-norm estimate. The return now occurs on one step of the original trajectory. This is provisional local work for the next independent check.

## A bound on newly arriving negative mass

Write \(z=b^0\) for the actual capped initial row and let \(0<s<A-M\), \(A=\sqrt{M^2+4t}\). As in [Round 109](persistent-repair-deficit-109.md), \(z<s\) has at most \(n\alpha/L_s\) sites for all large fields, where \(L_s=(A-s)^2-M^2>0\). Indeed off the mark such a site has \(\epsilon U>A-s>M\) and pays at least \(L_s\) in the defining cap deficit. Denote the left side of the displayed dissipation above by \(\Delta_j\), and define the true arriving negative mass and downward drift by
\[
 N_j=\mathbb E_n[h_{j+1}1_{\{b^j\ge0\}}],\qquad D_j=\|(z-b^j)_+\|_{2,n}.
\]
There is an exact bound
\[
 N_j\le \frac{\Delta_j}{s}
       +\|Ph_j\|_{2,n}\left(\frac{\alpha}{L_s}+\frac{4D_j^2}{s^2}\right)^{1/2}.                \tag{1}
\]
For arrivals with \(b^j>s/2\), the old-slack term in the dissipation controls their mass by \(\Delta_j/s\). The other arriving sites are contained in \(\{z<s\}\cup\{(z-b^j)_+\ge s/2\}\). The normalized size bound on that union is the expression in parentheses. At every arriving site \(h_j=0\), and the negative-part Lipschitz inequality gives \(\|1_{\{b^j\ge0\}}h_{j+1}\|_{2,n}\le\|Ph_j\|_{2,n}\), since \(b^{j+1}-b^j=Ph_j\). Cauchy–Schwarz yields (1). The bound requires no critical rate.

At an actual late low-loss step of the critical-rate marked obstruction, \(\Delta_j=O(n^{-1})\) and \(\|Ph_j\|_{2,n}=O(n^{-1/2})\). If \(D_j=o(1)\), then \(N_j=o(n^{-1/2})\). Conversely, a fixed fraction of critical new negative mass forces fixed downward drift from the actual initial cap, even if the two late negative rows are close in normalized second norm. This identifies the specific first-moment retention that cannot be inferred from that late norm alone. Neither a prime-uniform drift exclusion nor the needed weighted real overshoot estimate follows here.

## Early blocks with negligible average fresh mass

Fix \(0<\rho<\sigma<1/2\) and consider the complete dyadic blocks \([J,2J)\) contained in \([n^\rho,n^\sigma]\). There are order \(\log n\) such blocks. Since \(\sum_j\Delta_j\le\alpha\), some actual block satisfies \(\sum_{j=J}^{2J-1}\Delta_j=O(\alpha/\log n)\), with fixed \(\rho,\sigma\). On it \(D_j\le\|b^j-z\|_{2,n}\le\sqrt{2J\alpha}\) by telescoping and the ordinary projection dissipation. Also \(J^{-1}\sum_{j=J}^{2J-1}\|Ph_j\|_{2,n}\le(\sum_{j=J}^{2J-1}\Delta_j/J)^{1/2}\). Averaging (1) therefore gives
\[
                   \frac1J\sum_{j=J}^{2J-1}N_j=O\!\left(\frac\alpha{\sqrt{\log n}}\right).
\]
The constants depend on the fixed cap and floor and on \(\rho,\sigma\). No prime arithmetic is used in this selection. Under the actual critical-rate persistent matching mark, the original marked-pairing lower for \(m_{j+1}\) holds on the whole block, since \(2J=o(\sqrt n)\). Hence on all but \(O(J(\log n)^{-1/4})\) steps of the selected block, \(N_j=O(n^{-1/2}(\log n)^{-1/4})=o(m_{j+1})\). Thus there is a growing early block on which the negative first mass on most updates is almost entirely on sites already negative one step before. This is a relative first-moment retention statement, and still does not identify a single common support across the block or improve the masked cubic at the later critical scale.
