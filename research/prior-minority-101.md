# The triangular forcing and the genuine previous-state charge

On the original bounded recurrent block, small triangular forcing leaves two distinct ways to pay the signed quotient obstruction. A large negative flat mean inside the original block forces an expensive signed exterior for every shrinking-root law. In its absence a large wrong-sign time occupation inside the block forces an expensive nonnegative charge on the true previous absolute states. The second implication comes from an exact projector identity.

## A projector equality between nonnegative prior and minority rows

Use the genuine zero-start states \(Y_j\), \(W_j=|Y_j|\), \(0\le j<J\), fixed filtered block \(L\) of size \(m\), and companion sign \(\sigma\) of [round 98](astra-quotient-98.md). The quotient is \(X=G/L\) with size \(b=n/m\). A quotient block \(R\) has signed state \(Z_j(R)=\sigma\mathbb E_RY_j\) and absolute state \(A_j(R)=\mathbb E_R W_j\). With \(c_j=\beta_j\sqrt n/m\) and the inherited global mean scalar \(2g_j\), the exact quotient update is
\[
 Z_{j+1}=\sigma K_B(A_j+c_j e_0),\qquad
 2g_j=b^{-1}\sum_R A_j(R)+c_j/b .
\]
Here \(K_B\) uses the actual identity positional fiber \(B=L^\perp\). Put \(\rho=2/(J-1)\), and use \(\omega_j=2(J-1-j)/(J(J-1))\). Denote by \(\omega\) the weighted sum over \(0\le j<J\), by \(\flat\) the flat average over the same \(J\) times, and by \(\prec\) the sum over \(0\le j<J-1\) divided by **\(J\)**. Set \(G_\omega=2\sum\omega_j g_j\le4\), \(G^\prec=2\sum_{j<J-1}g_j/J\le2\). The exact triangular time shift is
\[
 \sum_{j<J}\omega_j Z_{j+1}=Z_\omega+\rho Z^\flat ,
\]
since \(Z_0=0\) and \(\omega_{J-1}=0\). Define \(N_\omega=A_\omega-Z_\omega\), the nonnegative twice-wrong-sign row.

Let \(P\) be the real orthogonal projector onto the constant and the allowed companion sector on \(X\). Applying \(P\) to the two weighted quotient updates gives
\[
\begin{split}
 P Z^\flat&=P A^\prec+c^\prec P e_0-G^\prec\mathbf1,\\
 P(Z_\omega+\rho Z^\flat)&=P A_\omega+c_\omega P e_0-G_\omega\mathbf1 .
\end{split}
\]
Equivalently,
\[
 P\left[N_\omega-\rho A^\prec+(c_\omega-\rho c^\prec)e_0\right]
                 =(G_\omega-\rho G^\prec)\mathbf1 .                \tag{1}
\]
Thus any allowed **nonnegative** law \(q\) with root \(w=q(0)>0\) obeys
\[
 \rho\,\frac{\langle q,A^\prec\rangle}{w}
 \ \ge\ N_\omega(0)-\frac{4}{w}-\rho c^\prec .                       \tag{2}
\]
Here \(c_\omega\ge0\) and \(G^\prec\ge0\), and
\(\langle q,N_\omega\rangle\ge wN_\omega(0)\). All \(c\) averages are \(O(1)\) on the original filtered list \(m\asymp\sqrt n\). Formula (1) holds before erasures. In (2) one can measure \(A^\prec\) with independently permitted original exterior erasures \(A^{\rm del}_j\), leaving the same block denominators and leaving the root intact. The change in \(\langle q,A^\prec\rangle\) is \(O(\varepsilon_p)\), before dividing by \(w\), by the [original erasure budget](quotient-floor-99.md). At \(w\ge(8/c_0)/J\) the loss in (2) is \(o(1)\).

## Two ways the flat expense can arise

Use the same genuine recurrence hypothesis as in [the shrinking-root test](quotient-floor-99.md), so \((1-\sigma\lambda)A_\omega(0)\ge c_0J\) with \(c_0>0\) depending on the fixed recurrence parameters. The original-block triangular forcing, before erasure, is
\[
 F=\sigma(K_B(1_{\{0\}^c}A_\omega))(0)
   =(1-\sigma\lambda)A_\omega(0)-N_\omega(0)
      +\rho Z^\flat(0)-\sigma\lambda c_\omega .
                                                                    \tag{3}
\]
The equality is the unprojected triangular update at the root. The original per-time erasures on the triangular input change \(F\) by \(O(\varepsilon_p)\). Let \(v\) be the actual signed flat exterior cost of [round 99](astra-quotient-99.md), with the root removed and independent permitted erasures. All admissible laws with \(w\ge(8/c_0)/J\) obey
\[
 \frac{\langle q,v\rangle}{w}
   = \frac{\langle q,A^\prec\rangle-G^\prec}{w}
        +c^\prec-Z^\flat(0)+O(\varepsilon_p/w).                     \tag{4}
\]
This follows by pairing the first projector equality with \(q\) and then removing the root. Formula (4) is a conversion from the signed exterior to the nonnegative prior *including the root*, plus the explicit signed root-price correction.

For sufficiently large eligible primes on the same recurrent list, at least one of the following holds.

* The actual measured triangular forcing exceeds \(c_0J/8\).
* The signed flat original block is very negative, \(Z^\flat(0)\le -c_0 J(J-1)/16\). Then every law of root at least \((8/c_0)/J\) has the normalized **signed exterior** charge \(\langle q,v\rangle/w>c_0J^2/32\).
* The original block has \(N_\omega(0)\ge11c_0J/16\). Then every such law has normalized **nonnegative prior** charge greater than \(c_0 J^2/16\), allowing the stated exterior erasures. If its prior root \(A^\prec(0)\) is at most \(c_0J^2/32\), the same laws also pay more than \(c_0J^2/32\) on the prior exterior alone.

Indeed, if the first case fails, (3) gives \(N_\omega(0)-\rho Z^\flat(0)\ge13c_0J/16\), absorbing the bounded mark and the \(o(1)\) deletion error. If also the second case fails, this forces the stated minority size. In that case (2) subtracts at most \(c_0J/2+o(1)+O(1/J)\). Multiplying the remaining \(3c_0J/16-O(1/J)-o(1)\) by \(1/\rho\) gives the third charge bound. In the second case (4) can drop the entire nonnegative prior; the only negative errors are \(O(J)\), so its signed charge bound follows. In particular a trial with one-sided \(o(J^2)\) normalized signed exterior charge already excludes the very negative **original** flat mean on a recurrent sequence. A nonnegative prior upper \(o(J^2)\) at the same root removes the large-minority branch even if a signed exterior upper uses a different law.

This decomposition retains the terminal weights, the original subgroup, and the observable source of each charge. It leaves the genuine signed triangular upper, the actual nonnegative prior upper on minority-dominated candidates, and the escape branch open. The finite replay checks the weighted quotient identities on the original \(p=769\) path with \(m=8,J=16\) and independent per-time erasures for all three inputs. It uses no recurrent assumption at that prime. [Arb checker](prior-minority-101-check.py) · [Replay](prior-minority-101-checks.jsonl)

1. Test the real nonnegative prior price in (2) on candidates with a genuinely large wrong-sign occupation. After the positive root price is separated, an \(o(J^2)\) upper for one shrinking-root law on this branch would eliminate that source of compensation.
2. For the same candidate and horizon, couple a true signed flat exterior trial to the measured \(Z^\flat(0)\). This rules out the very negative original-block case without estimating a second absolute history. The two bounds still require a signed triangular upper.
