# A quadratic residual test for the critical real cap rate

The real cap rate can be reduced to a quadratic residual once an approximate row is close in normalized second norm to any fixed inner cap. In particular a bounded genuine row can have order \(\sqrt n\) exceptional coordinates near the outer cap.

Use the [real capped map](real-amplitude-cap-102.md) at fixed \(t,M>0\), \(n\ge t\), with \(F_M(W)=K\Phi_t(C_M(W))\), \(t_0=n\), \(t_i=t\) off the mark. Its fixed point is \(U\), its normalized second-norm contraction factor at most \(q_M=M/\sqrt{4t+M^2}<1\), and its actual cap deficit \(\alpha=\mathbb E_n(U_i^2-M^2)_+\). All norms below are normalized. Fix \(0\le m<M\). For any real scalar \(v\) with \(|v|\le m\) and any real \(u\), one has
\[
 (u^2-M^2)_+\le \frac{M^2}{M^2-m^2}|u-v|^2.                       \tag{1}
\]
For \(|u|\le M\) the left side vanishes. Otherwise \(|u-v|\ge |u|-m\), and writing \(x=|u|\) shows
\[
 M^2(x-m)^2-(M^2-m^2)(x^2-M^2)=(mx-M^2)^2\ge0 .
\]
For \(0<m<M\), equality in (1) occurs at \(x=M^2/m\) with \(v\) of magnitude \(m\) and the same sign. At \(m=0\) the coefficient one is sharp in the limit \(x\to\infty\).

For any proposed real row \(W\), put \(r_M(W)=\|K\Phi_t(C_M(W))-W\|_{2,n}\) and \(h_m(W)=\|(|W|-m)_+\|_{2,n}\). By contraction, \(\|U-W\|_{2,n}\le r_M(W)/(1-q_M)\). Apply (1) against \(C_m(W)\) to get the exact sufficient bound
\[
 \boxed{\quad \alpha\le \frac{M^2}{M^2-m^2}
       \left(\frac{r_M(W)}{1-q_M}+h_m(W)\right)^2 .\quad}             \tag{2}
\]
If \(F(W)=K\Phi_t(W)\) is the actual uncapped map, then
\[
 r_M(W)\le \|F(W)-W\|_{2,n}+\|(|W|-M)_+\|_{2,n},
\]
because each real activation is \(1\)-Lipschitz and \(K\) is a contraction. For a genuine Picard row before outer-cap exit with \(\|W\|_\infty\le M\), the capped residual equals the actual consecutive increment residual. If all but \(O(\sqrt n)\) entries satisfy \(|W_i|\le m\), then \(h_m(W)=O(n^{-1/4})\). Thus \(r_M(W)=O(n^{-1/4})\) suffices there for the critical cap rate. With both \(r_M(W),h_m(W)=o(n^{-1/4})\), (2) gives \(\alpha=o(n^{-1/2})\). The [entry-bound version of the real comparison](real-cap-exterior-103.md) then gives \(\max K\tau=o(1)\) and vanishing of the true log mark at this fixed floor, since the capped mark tends to zero there. The little-\(o\) conclusion applies, for example, to a pre-exit choice with only \(o(\sqrt n)\) inner-cap exceptions and a residual \(o(n^{-1/4})\). The \(O\) version leaves the [prime-specific high-set test](overlapping-overflow-106.md) open.

In particular if the pre-exit contraction with factor \(q_M\) applies along a moving bounded Picard segment starting at a fixed row with bounded normalized residual, then exceeding \((\log n)/(4|\log q_M|)\) steps by a quantity tending to infinity is sufficient for the little-\(o\) residual part. This is a sufficient geometric envelope; an actual residual can be smaller earlier. Controlling the inner-cap exceptions at that moving row is a distinct requirement. Neither hypothesis is established at logarithmically growing prime heights by the available fixed-prefix checks.

## Two choices with explicitly controlled residual

The independent reviewer noted that the actual capped row \(W=F_M^j(0)\) can be used in (2) even after an outer-cap exit of the uncapped map. Its residual is at most \(2q_M^j\) since \(\|F_M(0)\|_{2,n}\le2\). Therefore at a logarithmically growing choice of \(j\) as above the residual requirement is automatic. Only the inner excess \(h_m(W)\) at that genuine **capped** row needs an estimate. Since \(h_m\) is a 1-Lipschitz functional in the normalized second norm, it differs from \(h_m(U)\) by at most \(2q_M^j/(1-q_M)\).

Alternatively let \(0<m<M\) and take \(U^{(m)}\) to be the actual fixed point of the smaller capped map. With \(W=C_m(U^{(m)})\), one has
\[
 F_M(W)=K\Phi_t(C_m(U^{(m)}))=U^{(m)} .
\]
Its residual is exactly \(\|(|U^{(m)}|-m)_+\|_{2,n}\) and its inner excess is zero. Thus a mean **square of the spill** bound at the smaller cap transfers to the deficit at the larger cap:
\[
 \alpha_M\le \frac{M^2}{(M^2-m^2)(1-q_M)^2}
       \mathbb E_n(|U^{(m)}|-m)_+^2 .                              \tag{3}
\]
For the smaller cap, if the maximal spill is \(s_m\), then the mean squared spill is at most \(s_m\alpha_m/(2m)\), by the exact local defect \(2m(|U^{(m)}|-m)_++(|U^{(m)}|-m)_+^2\). This version can use mild overflows across many sites. A rate for either the moving capped excess or the smaller-cap spill remains open at the desired floors.

1. Seek a bound on squared excess above a single inner cap along the genuine capped flow, or a quantitative square-spill bound at a smaller fixed cap. For genuine uncapped pre-exit rows, the count test \(O(\sqrt n)\) for the near-cap exceptions and the actual residual give another sufficient version.
2. At a fixed floor where the little-\(o\) bounds can be proved, apply the true mark comparison directly. To finish by real weights alone the argument needs an appropriate sequence of floors tending to zero.
