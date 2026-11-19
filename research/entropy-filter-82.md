# A common high-density deletion from the entropy of the true row

The signed Jacobi test bounds the entire high-density part of a feasible row from its clipped exterior entropy. For a fixed genuine larger-side optimizer the resulting deletion is independent of the terminal time. The surviving height test can then use a larger deletion on the low part even when the entropy exceeds the threshold in the first alternative of [round 81](entropy-heads-81.md).

## An upper on high-density collision for a known entropy

Let \(q\) be a genuine primary probability and let \(n=(p-1)/2\), \(x=(q-B/n)_+\), \(B\ge0\). Delete only the mark in defining the exterior mass \(M=\sum_{i\ne0}x_i>0\), and set \(\mu=x\mathbf1_{i\ne0}/M\), \(\mathcal D=\sum_i\mu_i\log(n\mu_i)\). Logs here are natural. There is an absolute constant \(C\) such that for sufficiently large eligible primes the following holds. If \(0<\alpha\) and \(\alpha\log p\ge C(1+\mathcal D)\), put
\[
 S_\alpha=\{i\ne0:\sqrt n\,q_i>\alpha M\}.
\]
Then
\[
             L_\alpha:=n\sum_{S_\alpha}q_i^2
                       \le C(1+B+M^2(1+\mathcal D)),\qquad
             |S_\alpha|\le \frac{C(1+B+M^2(1+\mathcal D))}
                                    {\alpha^2 M^2}.                 \tag{1}
\]
In fact the proof of the collision bound applies on every subset of \(S_\alpha\), using its own weighted Jacobi field. No estimate of the entropy from above for an unknown genuine optimizer is assumed in (1).

To prove it let \(S\subseteq S_\alpha\) be nonempty, write \(L=n\sum_S q_i^2\), \(M_S=\sum_S q_i\), \(v_i=q_i\mathbf1_S/M_S\), \(m=(\sum v_i^2)^{-1}\), and \(\rho=L/(\sqrt n M_S M)\). Thus \(\rho>\alpha\) and \(\rho^2m=L/M^2\). Use the weighted Jacobi field \(W\) of [round 80](astra-surviving-80.md#weighted-translated-jacobi-moments), with sign equal to the sector of \(q\). The exact eigen-equation and symmetry give
\[
   \sum q_i W(i)=(L/M_S-1)/\sqrt p,\qquad
   \|W\|_2^2=(n^2/p)(1/m-1/n).
\]
Here \(\|\cdot\|_2\) is the counting norm. For the clipped-off part \(z=q-x\), \(\|z\|_2\le\sqrt{B/n}\). The point cap \(q_0=O(n^{-1/2})\) and \(|W|\le1\) bound the removed marked term by \(O(n^{-1/2})\). Therefore
\[
        \mathbb E_\mu W\ \ge\
        \sqrt{n/p}\,\rho\left(1-\sqrt{B/L}-C_1/L\right).
\]
For the clipped-off term use \(\sqrt{nB/(pm)}=(L/(\sqrt p M_S))\sqrt{B/L}\). The \(C_1/L\) term also uses \(M_S\le1\). If \(L\le C_2(1+B)\), (1) follows by increasing \(C\). Otherwise choose \(C_2\) large so the displayed bound is at least \(\rho/2\). The proof with the exponential test in [round 81](entropy-heads-81.md#an-exponential-comparison-for-weighted-translates) then gives
\[
                  \mathcal D+1\ge c\min\{L/M^2,\rho\log p\}.
\]
The error \(O((\log p)p^{-3/8})\) is uniformly below one in this estimate. Choose \(C>2/c\) in the hypothesis on \(\alpha\). This forces \(L\le c^{-1}M^2(1+\mathcal D)\) in the remaining case. The counting bound follows from \(nq_i^2>\alpha^2 M^2\) on \(S_\alpha\).

The same proof works for any split \(q=x+z\) with \(x,z\ge0\), \(z_i\le B/n\). No scalar clipping identity is needed beyond this cap. More generally the split can be specified just on the exterior: give the entire root to \(x\) and put \(z_0=0\). For example, average the exterior split with its reflection at the root, giving an even genuine row, the same mass \(M\), and entropy no larger by convexity. Its actual scalar clipping mass at \(B\) is at most \(M\) by Jensen. Therefore the round-79 allowed deletion computed with the true scalar clipping mass is at least \(H^2/M^2\), and the filter computed using the averaged split may be used on the genuine masks of the even row. See the [same-time comparison](astra-optimal-82.md#the-same-actual-terminal-price) for the density thresholds.

## One deletion for all the genuine terminal times

Assume a fixed supercritical gap \(\sqrt n\,q_0\ge1+\delta\), take \(B=o(D(p))\), and let \(H\ge2\) be an allowed tower parameter in [round 79](terminal-height-79.md#a-tower-scale-deletion-on-the-terminal-height). Put \(E_*=1+B+M^2(1+\mathcal D)\) and choose, with a sufficiently large absolute constant \(C_3\),
\[
       \alpha=C_3\max\left\{\frac{1+\mathcal D}{\log p},
                                          \frac{\sqrt{E_*}}{H}\right\}.    \tag{2}
\]
Then \(|S_\alpha|\le H^2/(2M^2)\) by (1). In particular the same set \(S_\alpha\) can be included in the arbitrary deletion of round 79 for **every** selected terminal time, with the same \(q,B,H\). Its complement intersects each actual joint height and density band in a set with deficit price \(\gg_\delta1\) and companion height price \(\gg_\delta D(p)\).

On the complement, one can in fact make a further deletion at each terminal time of any \(H^2/(M^2\alpha^2)\) sites. If \(F\) is the removed subset of the low-density part, \(\sqrt n\|q\mathbf1_F\|_2\le H\) and \(\|q\mathbf1_F\|_1\le H^2/(\alpha M\sqrt n)\). The actual finite terminal envelope of round 79 can be paired with these masses using a bounded Mellin approximation of sup norm \(O(1+\log\log p)\) and normalized second error \(o(1/H)\). This sup bound follows by retaining the iterated-logarithm slack of the dominating tower, as in [round 81](entropy-heads-81.md#a-common-alternative-at-one-true-terminal-time). Since \(\alpha^{-1}\le C_3^{-1}\log p\), \(H\le\log_2\log_2p\) and \(n^{1/4}M/H\to\infty\), the removed deficit price is \(o(1)\). Hence the surviving low sites still pay \(\gg_\delta D(p)\) companion height. When the computed \(\alpha\ge1\) only the original deletion is needed; the improved budget is useful when \(\alpha\) is small.

For example, uniformly if \(\mathcal D=O(D(p))\) and \(\log_2^*H\) is a fixed positive fraction of \(\log_2^*p\) in the allowed range with \(H\) chosen as the corresponding tower, (2) is \(O(\sqrt{D(p)}/H)\). The additional deletion budget is then at least a constant times \(H^4/(M^2D(p))\). This conclusion uses the entropy for the chosen true row. It does not require \(\mathcal D=o(D(p))\) or the same paid site set at different terminal times.

## A stronger entropy lower when the high branch persists

For a prescribed \(\alpha\) suppose instead that the part with \(\sqrt n q_i>\alpha M\) retains deficit price \(\gg_\delta1\) after every original deletion of \(H^2/M^2\) sites at one terminal time. Its initial row set has cardinality greater than \(H^2/M^2\), so its initial collision is greater than \(\alpha^2 H^2\). It also has \(L\gg_\delta D(p)\) by the second norm bound on the genuine deficit. The same signed test gives
\[
             \mathcal D+1\ge
                  c_\delta\min\left\{
                    \frac{\max(D(p),\,\alpha^2 H^2)}{M^2},
                    \alpha\log p\right\}.                           \tag{3}
\]
This is stronger than the single-collision threshold when the per-site density floor survives many deletions. If, for example, \(\alpha=H^{-1/4}\) with the above tower choice, the right side is at least \(c_\delta H^{3/2}\). The full terminal dichotomy of round 80 applies with this threshold as well: its row splitting and low-price deletion estimate use \(\alpha^{-1}\) only through the product of the clipped mass and the approximation sup norm. This yields a choice between an entropy lower at that scale and low height surviving solely on sites with \(\sqrt n\,q_i\le M H^{-1/4}\) after deletion of up to \(H^{5/2}/M^2\) sites. These are necessary implications of a fixed gap, with a prime-uniform upper on the surviving height still needed.

1. Measure \(E_*\) for an actual larger-side optimizer and remove the same \(S_\alpha\) before evaluating all selected terminal objectives. Look for an upper on the surviving low-height charge or show precisely where it grows.
2. Use the stronger high-branch entropy lower (3) at the same density threshold as the candidate low-price bound, with \(B\) and \(M\) taken from the same genuine clipped row.
