# Dissipation and a two-root spill test for the actual pinned repair

Fix the original floor \(\tau>0\) and a growing \(T\) with \(T+1\) in the simultaneous marked window. Work with the actual projected mean-one row \(Z=X_{\sigma,T}/M\) of sign \(\sigma\), mark \(a/M\), and the orthogonal pin projector \(L_\sigma\) from [Round 140](averaged-completion-dual-140.md). The mark is positive eventually. Norms and expectations use divisor \(n\). Put \(u=T^{-1/3}\) and \(d_0=0,\ d_i=(u-Z_i)_+\) on the bulk. Here \(d_0\) denotes the physical coordinate of \(d\). The [actual bounds](averaged-hinge-opposite-141.md) are \(\mathbb E d=O_\tau(T^{-2/3})\) and \(\|d\|_{2,n}^2=O_\tau(T^{-1})\).

## The actual first spill

Take \(y^{(0)}=Z+2L_\sigma d\). Its bulk formula is
\[
 y_i^{(0)}=\max(Z_i,u)+\sigma(Kd)_i-\mathbb E d
               -2\ell_i\ell^{\mathsf T}d/\ell_0,\qquad \ell=P_\sigma e_0.
\]
The last two terms are \(O_\tau(T^{-2/3})\) uniformly on the bulk. Thus with \(b^{(0)}=1_{\rm bulk}(-y^{(0)})_+\) and \(E_0=\{i\ne0:y_i^{(0)}<0\}\), one has
\[
 b^{(0)}\le 1_{E_0}(-\sigma Kd-u/2)_+,\quad
 |E_0|/n=O_\tau(T^{-1/3}),\quad
 \|b^{(0)}\|_{2,n}^2=O_\tau(T^{-1}).
\]
The last two bounds follow from \(\|Kd\|_{2,n}^2=\|d\|_{2,n}^2-(\mathbb E d)^2\). The normalized second moment being \(o(u^2)\) does not give a pointwise estimate.

Let \(F\) be any true opposite mean-one optimum with \(q=F_0\), and \(R\) any true mean-one optimum on sign \(\sigma\). Then \(FR=0\) on the bulk. The affine constraints on \(y^{(0)}\) give
\[
 \mathbb E(F b^{(0)})\ \ge\ \frac{qa}{nM}-1.
\]
When \(q/\sqrt n\ge1+\eta\) on a prime subsequence and \(\sqrt{1+\tau}<1+\eta\), the right side is bounded below by a positive constant. If \(H=o(T)\) and \(F_H=1_{\rm bulk}(F-H)_+\), the clipped part of the last left side has size \(O_\tau(\sqrt{H/T})\) by its mean-one mass cap and the bound on \(b^{(0)}\). Thus under a gap the actual signed pair
\[
 -\frac{\sigma}{n}
  \sum_{\substack{i\in E_0,\ R_i=0\\j\ne0,\ j\ne i}}
      (F_i-H)_+ K_{ij}d_j                                      \tag{1}
\]
is bounded below by a positive constant. Indeed \(b^{(0)}\le -\sigma Kd\) on \(E_0\) and \(F_H\) vanishes outside the true opposite overlap zero set. Removing the diagonal costs at most \(n^{-1}q\mathbb E d=O_\tau(n^{-1/2}T^{-2/3})\), since \(K_{ii}=-1/n\). Both physical roots and the diagonal have been removed. A prime-uniform \(o(1)\) upper on (1) with one true \(F\) and selectable marked \(T\) on the opposite larger side or both sides would exclude a gap by reciprocity. This is a weaker target than pointwise nonnegative repair and retains the actual secondary failure set.

## Exact repeated zero-reserve dissipation

Starting at \(y^{(0)}\), for \(j\ge0\) use only zero-reserve corrections
\[
 b^{(j)}=1_{\rm bulk}(-y^{(j)})_+,\quad
 z^{(j)}=y^{(j)}+b^{(j)},\quad
 y^{(j+1)}=y^{(j)}+2L_\sigma b^{(j)} .
\]
All \(y^{(j)}\) keep the actual mean, sector, evenness and mark, and \(z^{(j)}\ge0\). The projection satisfies \(2L_\sigma-I\) orthogonal, so
\(\|y^{(j+1)}-z^{(j)}\|_{2,n}=\|b^{(j)}\|_{2,n}\).
Resolving this difference into \(z^{(j+1)}-z^{(j)}-b^{(j+1)}\) and using \(z^{(j+1)}b^{(j+1)}=0\) gives the exact law
\[
 \|b^{(j)}\|_{2,n}^2-\|b^{(j+1)}\|_{2,n}^2
 =\|z^{(j+1)}-z^{(j)}\|_{2,n}^2+
  2\,\mathbb E(b^{(j+1)}z^{(j)}).                            \tag{2}
\]
This comparison holds with or without feasibility at the pinned mark. Summed over any number of reflections, the last two costs have total \(O_\tau(T^{-1})\). In particular the cumulative unweighted new negative mass on sites with previous \(y^{(j)}\ge r>0\) is at most \(O_\tau((rT)^{-1})\). At \(r=u\) it is \(O_\tau(T^{-2/3})\).

Let \(\bar b_m=m^{-1}\sum_{j=0}^{m-1}b^{(j)}\) for \(m\ge1\). The telescoping increment, the sum of positive-part step squares, and the bound on each \(b^{(j)}\) give
\[
 \|L_\sigma\bar b_m\|_{2,n}
 \le\frac{\sqrt m+2}{2m}\,\|b^{(0)}\|_{2,n}
 =O_\tau((mT)^{-1/2}).
\]
This is an actual approximate annihilator, with nonnegative \(\bar b_m\), bounded second norm \(O_\tau(T^{-1/2})\), and no marked component. It uses \(m\) repair iterations after the true trajectory, so the marked constraint remains only on the chosen original \(T\).

At every reflection the same true optimizer has \(\mathbb E(F b^{(j)})\ge qa/(nM)-1\). Under a fixed gap, if \(c>0\) is a sufficiently small fixed fraction of its lower bound, each set \(\{i\ne0:b^{(j)}_i\ge c,\ R_i=0\}\) has relative size \(O_{\tau,c}(T^{-1})\) and carries \(\mathbb E[F^2 1_{\{b^{(j)}\ge c,R=0\}}]\gg_{\tau,\eta}T\). This follows by subtracting the cost at \(b^{(j)}<c\) and applying Cauchy–Schwarz on the remainder. The approximate annihilator also retains \(\mathbb E(F\bar b_m)\gg_{\tau,\eta}1\). No prime estimate yet bounds this weighted persistence from the unweighted dissipation. An upper \(o(1)\) on the actual ergodic weighted cost for one optimum would suffice. Square orders are compatible with all the field-general identities.

## Relaxed updates select one actual small-projection deficit

One can instead use a fixed relaxation \(0<\omega<2\) after the first reserved reflection, setting \(y^{(j+1)}=y^{(j)}+\omega L_\sigma b^{(j)}\) and keeping the same definitions of \(b^{(j)},z^{(j)}\). All affine constraints are still exact. Orthogonality of \(L_\sigma b^{(j)}\) and \((I-L_\sigma)b^{(j)}\) gives
\[
 \|(\omega L_\sigma-I)b^{(j)}\|_{2,n}^2
 =\|b^{(j)}\|_{2,n}^2
    -\omega(2-\omega)\|L_\sigma b^{(j)}\|_{2,n}^2.
\]
Consequently the right side of (2) gains the nonnegative term \(\omega(2-\omega)\|L_\sigma b^{(j)}\|_{2,n}^2\) for this relaxed flow. In its first \(m\) stages there is at least one actual deficit with
\[
 \|L_\sigma b^{(j)}\|_{2,n}
 \le \|b^{(0)}\|_{2,n}/\sqrt{\omega(2-\omega)m}.
\]
A fixed gap still forces its order-one true optimizer-weighted cost and the same sparse high-level paying set. This conclusion concerns a single actual slack deficit, rather than a time average. It does not bound the size of its entire active support.
