# Exact slack dissipation in a reflected opposite-sector repair

Use the actual capped opposite row \(b^0=z=a-\epsilon U\) and true favored stationary factor \(f=f_\epsilon\) from [Round 117](weighted-adjusted-cap-117.md). Write \(J\) for the constant projection, \(P=(I-\epsilon K+J)/2\), and use normalized counting inner products and norms throughout. The reflected update below is a new constructive trajectory starting at the same actual capped row. It is distinct from the previously studied update \(P(b_+)\), so results about late rows of one algorithm are not assigned to the other.

Set
\[
 b^{j+1}=P|b^j|,\quad u_j=(b^j)_+,\quad h_j=(b^j)_-,\quad m_j=\mathbb E_n h_j,\quad x_j=\epsilon K h_j.
\]
Every \(b^j\) is real even and lies in the range of \(P\), since both the projection and the absolute value preserve the even initial sector. Since \(P b^j=b^j\), the update is exactly \(b^{j+1}=b^j+2Ph_j=u_j+m_j\mathbf1-x_j\). Thus \(h_{j+1}=(x_j-u_j-m_j)_+\). In particular the first negative row is \((S-m_0)_+\), with the actual adjusted overshoot \(S\) of Round 117. Here and below a positive or negative part is taken coordinatewise.

## A finite-field energy identity retaining the old slack

Let \(d_j=u_j+m_j\mathbf1\), which is nonnegative. Pointwise, for \(x_j>d_j\), the identity \(x_j^2-h_{j+1}^2=d_j^2+2d_j h_{j+1}\) holds. On the complement use \((x_j)_-^2+\min((x_j)_+,d_j)^2=x_j^2\). Since \(K^2=I-J\), this gives the exact balance
\[
 \Delta_j:=\|h_j\|_{2,n}^2-\|h_{j+1}\|_{2,n}^2
 =m_j^2+\|(x_j)_-\|_{2,n}^2
 +\|\min((x_j)_+,d_j)\|_{2,n}^2
 +2\mathbb E_n(d_jh_{j+1}).                                  \tag{1}
\]
In particular \(\|x_j-h_{j+1}\|_{2,n}^2\le\Delta_j\), \(\sum_jm_j^2\le\|T\|_{2,n}^2\le\alpha\), and \(2\sum_j\mathbb E_n[u_j h_{j+1}]\le\alpha\). These statements and the reflected update require no cap rate. They give separate charges for signed negative transport and for arrivals against positive old slack.

At each fixed field the reflected orbit converges to a nonnegative row in the required sector. The counting norm of \(b^j\) is nonincreasing since \(P\) is orthogonal and \(|b^j|\) has the same norm. Its mean is \(\mu+2s_j\), so \(\sum_jm_j<\infty\). At fixed \(n\), \(\|h_j\|_{2,n}\le\sqrt n m_j\), which makes the increments \(2Ph_j\) summable. This finite-field convergence alone allows order-one added mean along primes.

For a sufficient repair test, put \(s_j=\sum_{i<j}m_i\). The exact mean is \(\mu+2s_j\) and the marked lower is \(b^j_0/\sqrt n\ge d-\sqrt{p/n}s_j\), using the entry bound on \(Kh_i\) and the nonnegative mark and mean terms in \(2Ph_i\). Also \(\|h_{j+1}\|_\infty\le\sqrt p\,m_j\) by the displayed update. Hence if there is an actual index \(j=j(p)\) with \(s_j=o(1)\) and \(\sqrt n m_j=o(1)\), then \(b^{j+1}+\|h_{j+1}\|_\infty\mathbf1\) is an ordinary feasible opposite-sector row, with eventual ratio upper \(\limsup_p\theta_\epsilon/\sqrt n\le\sqrt{1+t}\). Its promise uses \(\mu\le\nu\) and \(d\to2\) at fixed cap. For example, under the critical cap rate it suffices to show that up to some growing number of steps the actual slack charge obeys \(\mathbb E_n(u_i h_{i+1})\ge c\,m_{i+1}\) with fixed \(c>0\). Equation (1) then gives \(\sum_{i\ge1}m_i=O(n^{-1/2})\) over those steps and averaging yields a suitable stop. This is a sufficient condition on the actual receiver slack, not an unconditional slack lower bound.

## A paired transport forced on the actual reflected orbit

Suppose now \(\alpha\le B/\sqrt n\), \(\epsilon\gamma\ge\delta_0>0\) and \(t<e^{\delta_0}-1\), at fixed floor and cap on the same prime subsequence. For every \(j\le2c\sqrt n\), \(s_j\le\sqrt{j\alpha}\) is at most a small fixed constant when \(c>0\) is chosen small. The actual mark is positive there. The genuine favored factor has \(f_0=\sqrt n e^{\epsilon\gamma}\), \(m_f=\nu/2\), \(\|f\|_\infty=O(\sqrt n)\). Opposite-sector orthogonality implies
\[
 \mathbb E_n(fh_j)\ge b^j_0f_0/n-m_f\mathbb E_n b^j\gtrsim1.
\]
Indeed the limiting lower at zero cost is positive since \(\mu\le\nu\) and \(d\to2\), with \(s_j\)-dependent errors bounded uniformly by a constant times \(\sqrt c\). Thus \(m_j\gtrsim n^{-1/2}\) and \(\|h_j\|_{2,n}^2\gtrsim n^{-1/2}\) throughout the window, by the entry and second-norm upper bounds on \(f\).

Within the second half of the window choose an index \(j\) at which the sum of the four consecutive losses \(\Delta_{j-1},\ldots,\Delta_{j+2}\) is \(O(n^{-1})\). Such an index exists by averaging over complete four-step blocks and the total loss \(O(n^{-1/2})\). Each of \(h_j,h_{j+1},h_{j+2}\) then has mean \(\asymp n^{-1/2}\), squared second norm \(\asymp n^{-1/2}\) and bounded supremum, the latter by the preceding mean bound and \(h_i\le (x_{i-1})_+\). From (1) and \(K^2=I-J\) it follows that
\[
 \|\epsilon K h_j-h_{j+1}\|_{2,n}
  +\|\epsilon K h_{j+1}-h_{j+2}\|_{2,n}
  +\|h_{j+2}-h_j\|_{2,n}=O(n^{-1/2}).                         \tag{2}
\]
Thus the nonnegative sum of the two consecutive true negative rows is within \(O(n^{-1/2})\) in normalized second norm of its signed transport back to itself. Their difference instead satisfies the opposite sign relation up to the same error. There is no assertion that the two rows are close in one step.

The true favored factor also has nearly the same pairing with the two negative rows. Indeed \(\mathbb E_n(fx_j)=\mathbb E_n(fh_j)-m_f m_j\) by its exact sector identity. Equation (2) gives \(\mathbb E_n[f(h_{j+1}-h_j)]=O(n^{-1/4})\), using \(\|f\|_{2,n}=O(n^{1/4})\). This concerns the actual pairing and does not identify the two distributions.

For small fixed \(a_*,\eta>0\), both true sets
\[
 D_i=\{y:h_i(y)\ge a_*,\ f_y\ge\eta\sqrt n\},\qquad i=j,j+1,
\]
have size \(\asymp\sqrt n\). Indeed the low-\(h_i\) and low-\(f\) portions of the pairing are bounded by \(a_*m_f\) and \(\eta\sqrt n\,m_i\), respectively. The remaining pairing has a fixed positive lower, each summand is \(O(\sqrt n)\), and the means give upper counts. On \(D_{j+1}\) the full source \(h_j\) has signed transport exactly \(h_{j+1}+u_j+m_j\). On all but \(O(1)\) sites of \(D_j\) one has \(h_{j+2}\ge a_*/2\), by (2); there the reverse source \(h_{j+1}\) transports exactly to \(h_{j+2}+u_{j+1}+m_{j+1}\). By the explicit last term of (1), the sum of the respective old positive slacks on either recipient set is \(O(1)\). Deleting the sites with old slack above \(n^{-\sigma}\), for any fixed \(0<\sigma<1/2\), costs only \(O(n^\sigma)=o(\sqrt n)\) sites. Both transport lower bounds retain order \(\sqrt n\) genuine high recipients with uniformly vanishing old slack. The sources in this statement are the full actual rows, including their small-amplitude parts.

This result supplies a more restrictive pair of genuine signed transport tests at the critical cap rate. It does not exclude that pair on prime fields, prove the critical rate, or supply the rate-free weighted overshoot estimate.

## Two-step return count and the paired cubic

Choose \(a>0\) small enough that the same size lower bounds hold throughout \([a,2a]\), and let \(D_i(s)=\{h_i\ge s,\ f\ge\eta\sqrt n\}\). The set where \(\max(h_j,h_{j+2})\ge a\) has \(O(\sqrt n)\) sites. On that set the counting first norm of \(h_{j+2}-h_j\) is \(O(n^{1/4})\) by (2) and Cauchy–Schwarz. Integrating the symmetric difference over \(s\in[a,2a]\) is bounded by that first norm. Hence some common threshold has \(|D_j(s)\triangle D_{j+2}(s)|=O(n^{1/4})\). The same masks for the two transports retain order \(\sqrt n\) genuine high recipients after the slack pruning above.

The nonnegative source \(h_j+h_{j+1}\) meets the deterministic source hypotheses in [the single-repair reciprocal cubic](paired-legendre-cubic-116.md). Its input mark is zero, it is bounded at critical mean and second norm, and its signed eigendefect is \(O(n^{-1/2})\). With the two true factors normalized by \(\sqrt n\), the favored pairing has the critical lower above, and the opposite pairing is \(O(n^{-3/4})\) by the small opposite projection and the normalized second norm of the true opposite factor. Thus its full signed distinct cubic has a positive \(n^{-1}\)-scale lower whenever the actual transported output at the mark tends to zero. The output limit and any useful prime-uniform upper for this cubic remain unproved.
