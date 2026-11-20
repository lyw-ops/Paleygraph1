# Full analytic Jacobi seed price

Use the original closed cold square, actual Jacobi seed \(S=2\sqrt n\,Ke_0\), and old translated physical price \(P_{5000}\) from [Round 133](cold-seed-packet-133.md). Let \(D^{\mathrm J}\) be the diagonal \(\Phi'_{t_i}(S_i)\), with the actual marked floor \(t_0=n\). This includes every pure power of \(S\) in the odd derivative expansion, starting with the linear seed term of Round 133.

Write \(s_n=2\sqrt{p/n}\). At good full Mellin characters the reduced seed is \(s_n(L+L^{-1})/2\), where \(L\) is the invertible Jacobi object in the [seed-power rank comparison](seed-majorant-47.md#mixed-words-with-a-distinguished-rank-one-seed). For the bulk derivative \(d_t(z)=z/\sqrt{4t+z^2}\), the coefficient of \(L^{k}\) in its order-\(2\ell+1\) term is
\[
 (-1)^\ell \frac{\binom{2\ell}{\ell}}{4^\ell}
 \binom{2\ell+1}{(2\ell+1-k)/2}
 \left(\frac{s_n}{4\sqrt t}\right)^{2\ell+1}
\]
when \(k\) is odd and \(|k|\le 2\ell+1\). The negative-index coefficient is equal to the positive-index coefficient. The terms with the same exponent are signed coefficients of the same Mellin object. Taking their sum before modulus permits cancellation across the derivative orders.

Collect the first 14 binomial orders, with \(s_n\) enclosed in \([2.828427,2.828428]\) for \(n\ge10^{30}\). If \(c_k\) is the resulting coefficient, the comparison charges a folded mass \(2|c_k|\) at \(k>0\). For these masses let \(m\) be the total and \(\nu\) the moment in the fixed rational price \(\pi\). The base column ratios are
\[
 \frac{(j-1)\nu+\sum_{k>0}2|c_k|(\pi(|j+k|)+\pi(|j-k|))/2}{\pi(j)}.
\]
There are finitely many non-affine ratios, followed by an affine-over-affine ratio with limit \(m+\nu/\pi'_\infty\). The off-base column costs \(m+\nu/5000\), since its base zeros cost the \(\pi\)-moment of the multiplier. This uses the same boundary transport and price as [Round 96](shifted-resolvent-96.md).

For the omitted orders set \(\rho=(2.828428)^2/(4\inf_Q\Re t)\). A multiplier atom of weight \(k\) costs at most \(2(1+|k|)\) per unit translated price. In order \(2\ell+1\), the folded masses sum to at most \(\sqrt{\rho}\rho^\ell\) and \(|k|\le2\ell+1\). Thus the tail adds at most
\[
 4\sqrt\rho\,\rho^{14}
 \left(\frac{15}{1-\rho}+\frac{\rho}{(1-\rho)^2}\right).
\]
The [outward replay](cold-pure-seed-134-check.py) on the original square checks a geometric translated rate below \(0.5279\), including this tail. It uses the inherited rational price list and 192-bit Arb.

All bad-lift corrections retain the base pair and the input translated pair. Their pre-transport absolute costs are bounded by the summable absolute seed series times the input dimension. The physical marked derivative is restored at frequency zero, with a bounded pre-transport change. These corrections contribute \(O_{5000}(n^{-1/2})\) relative price after applying \(K\). Consequently \(KD^\mathrm J\) has eventual translated rate below \(0.528\), and \(KD^\mathrm J KD^\mathrm J\) has translated rate below \(0.279\) on the full square. This is an all-order bound for the pure seed piece. The full \(D_h\) has additional terms involving \(V_h-S\), beginning with \((V_h-S)/(2\sqrt{t_i})\).

For the actual rows \(h=601,602\), write \(E_h=D_h-D^\mathrm J\). An estimate \(\|K E_h\|_{P_{5000}}<0.472\) for both frozen rows would suffice to make both actual steps contract in that price. Alternatively a joint bound below \(0.721\) on \(KD_{602}KD_{601}-KD^\mathrm J KD^\mathrm J\) would suffice for the frozen block. Both leave the actual invariant-ball and half-step margins to be checked. No such remainder bound is established here.

## Flat entries and counting contraction alone cannot price a physical packet

Let \(P=I-J_0\), \(d=\sqrt{1-1/n}\), \(u=Pe_0/d\), and \(v=Ke_0/d\) in physical frequency coordinates. They have unit counting norm and mean zero. In unitary position coordinates both vanish at \(1\); at \(x\ne1\) they are \(1/\sqrt{n-1}\) and \(s(x)/\sqrt{n-1}\), respectively. The following auxiliary operator preserves the mean-zero space:
\[
 A=\frac18(uv^*+vu^*).
\]
It has counting norm at most \(1/4\), position entries \(O(1/n)\), and frequency entries \(O(n^{-1/2})\), since \(\|v\|_\infty=O(n^{-1/2})\). Nevertheless \(S=2\sqrt n\,d\,v\) is a genuine physical packet of bounded price and
\[
 (AS)_0=\frac{2\sqrt n\,d}{8}\bigl(u_0+\langle u,v\rangle v_0\bigr)
       \ \ge\ \frac{n-1}{4\sqrt n}.
\]
Here \(K_{00}=-1/n\) makes both \(v_0\) and \(\langle u,v\rangle\) negative. A physical packet price dominates the frequency supremum. These two entry bounds and the counting contraction therefore do not imply a physical packet rate even when the input is the actual seed. This auxiliary operator does not represent the actual cold derivative.

Replay the [saved outward record](cold-pure-seed-134-checks.jsonl) with python-flint \(0.9.0\).
