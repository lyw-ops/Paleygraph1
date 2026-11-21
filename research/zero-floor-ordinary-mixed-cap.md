# The ordinary theta pair from a zero-floor map with a marked cap

Research draft. Let \(p\equiv1\pmod4\) be prime, \(n=(p-1)/2\), and use the Fourier operator \(K\), with \(K^*=K\), \(K^2=I-J_0\), and \(|K_{ij}|\le\sqrt p/n\). All norms and means below are normalized by \(n\). In the position variable \(K\) has symbol \(\chi(1-x)\), and \(J_0\) is the averaging projection in the frequency variable. Write \(\theta_+=\vartheta(\overline H_p)\) and \(\theta_-=\vartheta(H_p)\), so that \(\theta_+\theta_-=n\). A nonnegative even row in the \(\epsilon\) sector plus constants gives the usual ordinary-theta lower bound by its marked entry divided by its mean. [Fourier LP](fourier.md) · [Published Fourier LP](https://arxiv.org/abs/1907.05971)

## A true ordinary optimizer pair at zero floor

Fix any \(M>0\) at the mark. Set the bulk floor to zero, the marked floor to \(n\), and the bulk cap to \(2\sqrt p\) while keeping the marked cap \(M\). The actual capped fixed-point equation for these coordinatewise caps has a real even solution. To see this, give the bulk a positive floor, iterate the strict contraction from zero, and let the floor decrease to zero at fixed \(p\). The scalar Lipschitz constant for a positive floor is strictly less than one because each individual cap is finite at fixed \(p\). The rows are uniformly bounded as the floor decreases because the cap vector is fixed at that prime. Take a finite-dimensional convergent subsequence and pass through the continuous map.

Denote the zero-floor solution by \(Y\), its activation by \(b\) and its mean by \(\nu\), so \(Y=Kb\). At zero floor the squared norm identity gives \(\nu^2=4-\mathbb E_n(Y_i^2-C_i(Y_i)^2)\le4\), where \(C_i\) is the clip at the cap of coordinate \(i\). As \(b\ge0\), the entry bound gives \(\|Y\|_\infty\le\sqrt p\,\nu\le2\sqrt p\). Consequently the chosen bulk cap is inactive at this **actual** solution, so \(b_i=|Y_i|\) off the mark. At the mark \(b_0=\sqrt{4n+C_M(Y_0)^2}>0\). All the difference \(b_i^2-Y_i^2\) is now at the mark, and equals \(n\nu^2>0\) there. The latter inequality uses that \(b_0>0\) and the activation is nonnegative.

It follows that \(F_\epsilon=(b+\epsilon Y)/\nu\) is nonnegative in the correct sector and has mean one. The rows obey \(F_+(i)F_-(i)=0\) in the bulk and \(F_+(0)F_-(0)=n\). The two sector lower certificates therefore simultaneously attain the **ordinary** theta bounds, and
\[
 \frac{Y_0}{b_0}
       =\frac{\theta_+-\theta_-}{\theta_++\theta_-},
 \qquad b_0=2\sqrt n+O_M(n^{-1/2}).                                 \tag{1}
\]
This holds for any real even fixed point of the specified mixed cap. In particular the marked ratio is the same for every such point. Equation (1) and the theta product imply that the original limit holds if and only if \(Y_0/\sqrt n\to0\). No comparison to positive-floor ordinary stationary factors is needed in this identity.

## Energy charged only to the actual signed bulk spill

Let \(U=Ka\) be a true zero-floor capped row with cap \(M\) at every site, including the same mark as above. Write \(C=C_M(U)\), \(h=U-C\), \(\mu=\mathbb E_n a\), and \(q_{\rm mark}=M/\sqrt{4n+M^2}\). The capped zero-floor mark satisfies \(U_0/\sqrt n\to0\) by the fixed-cap comparison in the [zero-floor draft](zero-floor-mark-and-cap-budget.md). This is the one place where the prime mark input from positive floor is used.

Use \(F_{\rm bulk}=1_{\{i\ne0\}}\). There is a direct comparison with the ordinary optimizer pair:
\[
\begin{aligned}
 (\mu-\nu)^2
 &+\frac{1-q_{\rm mark}^2}{n}(U_0-Y_0)^2\\
 &+\mathbb E_n\big[F_{\rm bulk}(h^2+2M|h|+4(CY)_-)\big]
       \ \le\ 2\mathbb E_n(F_{\rm bulk}hY).                         \tag{2}
\end{aligned}
\]
In fact
\[
 \|U-Y\|_{2,n}^2=\|a-b\|_{2,n}^2-(\mu-\nu)^2 .
\]
For a bulk coordinate the exact difference of squares is
\[
 (U_i-Y_i)^2-(a_i-b_i)^2
   = h_i^2+2M|h_i|-2h_iY_i+4(C_iY_i)_-,
\]
because \(a_i=|C_i|\), \(b_i=|Y_i|\), \(U_i=C_i+h_i\), and \(C_i h_i=M|h_i|\). At the mark \(a,b\) use the same clipped activation and its Lipschitz constant is \(q_{\rm mark}\). Combining the bulk identity and the marked bound proves (2).

Thus it suffices for the original theta limit to establish
\[
 \limsup_p\mathbb E_n(F_{\rm bulk} hY)\le0
 \tag{3}
\]
at one fixed \(M>0\), or the vanishing double limit of this signed overlap along fixed caps \(M\to\infty\) after the prime limit. For the latter version the normalized ratio in (1) is independent of \(M\), and \(b_0/\sqrt n\to2\) at each fixed cap. A stronger positive test is vanishing of the aligned overlap \(\mathbb E_n[F_{\rm bulk}(hY)_+]\). The nonnegative term \(4(CY)_-\) in (2) retains the contribution of actual opposite signs, even on bulk coordinates with no cap spill.

This uses only the two zero-floor physical rows and the true ordinary Fourier-LP pair. It does not assume a particular rate on \(\mathbb E_n h^2\), but still requires the signed prime estimate in (3) or a direct estimate on the left side of (2). The marked part of the cap deficit is \(o(1)\) at each fixed \(M\), since \(U_0/\sqrt n\to0\). In particular the positive small-cap deficit proved in the zero-floor draft would already rule out (3) for \(2\le M\le9/4\), regardless of the eventual theta ratio.

## Actual one-sided weighted source and the critical threshold

For the zero-floor \(U\), put \(z_\epsilon=a-\epsilon U\) and \(T_\epsilon=F_{\rm bulk}(\epsilon U-M)_+=F_{\rm bulk}(\epsilon h)_+\). At large primes \(z_\epsilon(0)/\sqrt n\to2\), so \((z_\epsilon)_-=T_\epsilon\). For the exact optimizer \(F_\epsilon\) above, opposite-sector orthogonality gives
\[
 \mathbb E_n(F_\epsilon T_\epsilon)
 \ \ge\ \frac{\theta_\epsilon}{\sqrt n}
              \frac{z_\epsilon(0)}{\sqrt n}-\mu .                  \tag{4}
\]
Indeed \(\mathbb E_n(F_\epsilon z_\epsilon)=\mu\) and the marked entry alone lower-bounds \(\mathbb E_n(F_\epsilon(z_\epsilon)_+)\). A fixed theta excess of sign \(\epsilon\) therefore forces a fixed lower on the genuine aligned spill weighted by the exact optimizer of that sign. Here there is no adjusted overshoot or positive-floor tail. On the bulk the aligned overlap in (2) is exactly
\[
 F_{\rm bulk}(hY)_+
    =\frac{\nu}{2}\big(T_+ F_+ + T_- F_-\big).
\]

Finally \(F_\epsilon=1+\epsilon KF_\epsilon\) and \(\mathbb E_n F_\epsilon=1\) give \(\|F_\epsilon\|_\infty\le1+\sqrt p\). Also the true capped deficit \(\alpha_M=4-\mu^2\) controls \(2M\mathbb E_n T_\epsilon\). Thus (4) yields the explicit necessary rate \(\alpha_M\gtrsim_{M,\delta}p^{-1/2}\) on any subsequence where \(\theta_\epsilon/\sqrt n\ge1+\delta>1\). The actual \(o(p^{-1/2})\) cap rate at one fixed cap would therefore imply the original limit without an adjusted-weight estimate.

Without a critical rate, the same inequality localizes to a moving high weight. For every \(L\ge0\),
\[
 \mathbb E_n[(F_\epsilon-L)_+T_\epsilon]
 \ge \frac{\theta_\epsilon}{\sqrt n}
          \frac{z_\epsilon(0)}{\sqrt n}
             -\mu-\frac{L\alpha_M}{2M}.
\]
If \(\alpha_M=o(1)\) along a fixed-excess subsequence, this retains a positive lower as far as a fixed small multiple of \(\alpha_M^{-1}\). Thus a proof can test only the genuine high part of the zero-floor ordinary optimizer once cap-defect vanishing is known. It would still need an arithmetic upper on this actual weighted overlap.
