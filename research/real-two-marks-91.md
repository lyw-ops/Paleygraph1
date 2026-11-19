# Real stationary problems underlying the complex cap

A clipped complex stationary row in the cold square is equivalent to two genuine nonnegative real stationary pairs sharing all their bulk weights. These pairs have different real marked weights. At each cap site their two zero factors are exchanged between the endpoints. The midpoint of the two marked weights is the unique root of a scalar equation with a dimension-independent lower slope. Thus one can search for the bulk weights alone, using real log maximization including on the zero-weight boundary. The reduction also gives a signed objective price for cap switches on the actual real optimization paths.

## Stationary pairs with zero weights

Let \(U_\pm=\mathbb R\mathbf1\oplus H_\pm\) be the two complementary Paley sectors. For nonnegative bulk weights \(k\) and positive marked weight \(\tau\), write \((P(\tau),Q(\tau))\) for any nonnegative complementary pair in \(U_+\times U_-\) with products \((\tau,k)\) and common mean \(m_\tau=\sqrt{(\tau+\sum k)/n}\). Such a pair exists by making zero weights strictly positive and passing to a limit in the positive stationary pairs. At fixed \(n\) the bounded means bound all nonnegative coordinates; the products bound each charged coordinate away from zero.

The normalized row \(P/m_\tau\) maximizes \(\sum_{i:w_i>0}w_i\log z_i\) among mean-one nonnegative plus rows. In fact the first-order upper bound, summed over the charged sites, is nonpositive. The full linear test with the opposite row has mean zero, and its deleted terms on zero sites are nonnegative. The same argument applies to \(Q/m_\tau\). Strict concavity fixes each positively weighted coordinate of these maximizers. In particular the two unscaled marked factors are unique and continuous in \((\tau,k)\) as long as the marked weight stays positive. Continuity follows by the same compactness argument, now applied to the varying weights.

At fixed \(k\) both unscaled marked factors strictly increase with \(\tau\). To prove this for \(P\), compare the two normalized optimizers for \(\tau_2>\tau_1\) against each other and add their objective inequalities. This gives \((\tau_2-\tau_1)\log[(P_0(\tau_2)/m_{\tau_2})/(P_0(\tau_1)/m_{\tau_1})]\ge0\). Now \(m_\tau\) is strictly increasing. The proof for \(Q\) is identical. This argument includes zero bulk weights. If the zero-weight set supports no nonzero row in either \(H_\pm\), both full pairs are unique: two optima can differ only on that set and have equal means.

## Eliminate the two marked floors

Use normalized complex factors \(A,B\) with \(A_0B_0=s=u+iv=n/t\), positive real parts and common mean. Off the mark \(A_iB_i=1+e_i\), with the phase cap \(|\arg A_i|\le\arctan a\), \(0<a<1\), and \(e_i>0\) allowed only at the cap. On the cold square the two marked absolute angles are strictly inside that cone. Define
\[
 P^\pm=\Re A\pm a^{-1}\Im A,\qquad Q^\pm=\Re B\pm a^{-1}\Im B .
\]
These are nonnegative real rows in the required sectors. Within each sign they have equal positive means. The two products coincide on the bulk, since their difference is \(2a^{-1}\Im(A_iB_i)\). Denote this common product by \(k_i\). At the mark the products are \(h\pm d\) where \(d=v/a\). Assume \(u>|d|\), as holds on the nominated cold square.

For any fixed candidate \(k\ge0\), take the real pairs at \(\tau_\pm=h\pm d\) and write
\[
 \delta_i=(P_i^+-P_i^-)(Q_i^--Q_i^+),\qquad c=(1+a^2)/4.
\]
Their recovered complex product has real part \(k_i+c\delta_i\) in the bulk and \(h+c\delta_0\) at the mark. The mark therefore asks for \(F_k(h)=u\), where
\[
 \begin{split}
 F_k(h)&=h+c\delta_0\\
       &=\frac{1-a^2}{2}h+
          c\big(P_0(h+d)Q_0(h-d)+P_0(h-d)Q_0(h+d)\big).
 \end{split}                                                        \tag{1}
\]
Every term in the cross sum increases with \(h>|d|\). In particular
\[
 F_k(h_2)-F_k(h_1)\ge (1-a^2)(h_2-h_1)/2 .
\]
Monotonicity of both marked factors in their weight also shows \(\delta_0\le0\), for either sign of \(d\). Since \(F_k(h)\le h\) and \(F_k(h)\to\infty\), (1) has a unique solution for \(u>|d|\), for every \(k\ge0\). There is a sharper bracket independent of \(k\):
\[
 0\le h-u\le c(\sqrt{h+d}-\sqrt{h-d})^2
          =\frac{2cd^2}{h+\sqrt{h^2-d^2}}.                           \tag{2}
\]
Indeed, expand \(-\delta_0\) as \(2h\) minus the cross sum and use the arithmetic-geometric mean inequality on the latter.

The map \(h=h(k)\) is stable even at zero weights. Write \(\gamma_0(k,\tau)=\frac12\log(P_0/Q_0)\). The marked-response estimate for a fixed mark, extended to nonnegative bulk by continuity, yields
\[
 |\gamma_0(k,\tau)-\gamma_0(k',\tau)|\le
      \|\sqrt{k}-\sqrt{k'}\|_2/\sqrt{\tau}.
\]
The cross sum in (1) is \(2\sqrt{h^2-d^2}\cosh(\gamma_0(k,h+d)-\gamma_0(k,h-d))\). The magnitude of its hyperbolic argument is at most \(\frac12|\log((h+d)/(h-d))|\) by monotonicity of both \(P_0,Q_0\). Throughout this interval \(\sqrt{h^2-d^2}\,|\sinh(\cdot)|\le |d|\). Compare (1) at \(h(k')\) for the two profiles, then use the lower slope to obtain
\[
 |h(k)-h(k')|
 \le \frac{1+a^2}{1-a^2}|d|
       \left(\frac1{\sqrt{u+d}}+\frac1{\sqrt{u-d}}\right)
         \|\sqrt{k}-\sqrt{k'}\|_2 .                                  \tag{3}
\]
It follows that the normalized shift \(|h(k)-h(k')|/n\) is \(O_a(|\Im t|)\) times the normalized counting second norm of the bulk square-root change on the cold square. [Fixed-mark real estimate](marked-response.md#weighted-complementary-projections)

## The exact remaining bulk system and the switching price

The condition on \(k\) and the two actual real endpoint optimizers is exactly
\[
               k_i=(1-c\delta_i)_+,\qquad
               e_i=(c\delta_i-1)_+,\qquad i\ne0 .                    \tag{4}
\]
For \(k_i>0\), the phases in the reconstructed factors are strictly below the cap, since all four real values there are positive. A clipped pair with any zero \(k_i\) has opposite multiplicative zeros at the two ends: if the phase of \(A_i\) is positive, \(P_i^-=Q_i^+=0\) and \(P_i^+,Q_i^->0\). The signs reverse for negative phase. Thus \(c\delta_i=1+e_i\) there, including any tie. Conversely take real pairs for some \(k\) satisfying (1) and the first equation of (4), and put
\[
 A=(P^++P^-)/2+ia(P^+-P^-)/2,\qquad
 B=(Q^++Q^-)/2+ia(Q^+-Q^-)/2.
\]
They are in the complexified sectors with equal means. Their products have the stipulated imaginary parts and real parts \(1+e_i\) in the bulk and \(u\) at the mark. Where \(k_i=0\), the first equation of (4) gives \(\delta_i\ge1/c>0\), forcing an exchange of zeros and positive real parts of \(A_i,B_i\). Their mark is inside the angular cone since all four real marked factors are positive. This proves the claimed equivalence, with existential choices in the real pairs when the zero set allows nonuniqueness. In particular an extinction of the common positive weights is equivalent to attaining the phase cap, whereas a zero weight with \(c\delta_i=1\) carries no correction. At positive \(k_i\), one has the equivalent formula \(k_i[1+(1+a^2)\sinh^2((\gamma_i^+-\gamma_i^-)/2)]=1\), where \(\gamma_i^\pm=\frac12\log(P_i^\pm/Q_i^\pm)\).

Here the switches are paid by the *actual* variational gaps. Let \(Z=\{i\ne0:k_i=0\}\), and for each end write \(L_\pm(z)=\sum_{i:w_i^\pm>0}w_i^\pm\log z_i\), with \(w^\pm=(h\pm d,k)\), and \(z_\pm=P^\pm/m_\pm\). Take \(\mathcal B(r)=r-1-\log r\). At the minus end the exact identity is
\[
 L_-(z_-)-L_-(z_+)=
 \frac{m_-}{m_+}\sum_{i\in Z}P_i^+Q_i^-+
 \sum_{i:w_i^->0} w_i^-\,\mathcal B(z_{+,i}/z_{-,i}).                \tag{5}
\]
Expand \(-\log r=(1-r)+\mathcal B(r)\) and evaluate the linear term using the complementary pairing \(P^\pm\cdot Q^-=n m_\pm m_-\) after adding back the zeros. Interchanging signs gives the reverse gap and the opposite switching price. Their sum has the exact scalar value \(2d\log(z_{+,0}/z_{-,0})\). At each switch the corresponding sum in (5) contributes precisely \((1+e_i)/c\) before its mean factor. Both Bregman costs are nonnegative, so each sign's switching price is bounded by a real optimal-objective comparison. The formula tests the same common bulk weights at both ends, including the zero and small positive weights.

At \(p=173\), \(t=1/50+13i/1000\) and \(a=1/\sqrt2\), the outward check below validates a clipped root in a ball about a numerical proposal. The unique capped orbit is \(43\), with a switch and a correction in \((0.03578583886,0.03578583887)\). Both real mark products are positive and their midpoint satisfies (1)–(2). The signed switch term in (5) exceeds \(6.5938\) in counting normalization. This demonstrates the zero-weight boundary at a genuine prime outside the nominated cold square. [Checker](real-two-marks-91-check.py) · [Outward record](real-two-marks-91-checks.jsonl)

1. For the real pairs at common \(k\) selected by (4), compare the two signed switching terms in (5) to the excess above the best real objective achievable with the suspected zero set removed. A through-primes bound below the price of the first switch would exclude cap contact.
2. Use (3) to fix the two roots to high accuracy when changing only a tiny set of bulk weights. A uniform real mark-to-bulk response on both real endpoint paths down to \(k_i=0\) is the remaining pointwise estimate. The global scalar slope alone does not prevent zero bulk weights.
