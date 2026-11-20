# Actual overflow transport and its natural scale

The [returned Astra draft](api-astra-overflow-107.txt) tests the [aligned overflow](overlapping-overflow-106.md) against the exact capped equation and the positive stationary factor. Its stationary-factor bridge is correct. Its cap equation needs a sign correction and a different scale comparison. [Completion receipt](api-astra-107-receipt.json)

On the genuine aligned overflow set \(S\) of sign \(\epsilon\), use \(q=\epsilon\tau 1_S\) and \(y=\epsilon Y\) there. Pairing \(Kf_\epsilon=\epsilon(f_\epsilon-\nu\mathbf1/2)\) with \(q\), and using \(0\le b-y\le2\sqrt t\) on \(S\), gives
\[
 \epsilon \langle Kq,f_\epsilon\rangle_{2,n}
 =\langle q,y\rangle_{2,n}
  -\left\langle q,\frac{\nu-(b-y)}{2}\right\rangle_{2,n}.
\]
For \(n\ge t\), the last term is between zero and \((\nu/2)\mathbb E_n q=O(n^{-1/2})\) under the critical cap rate. The two genuine pairings thus differ by only \(O(n^{-1/2})\). This excludes the suggested fixed deduction between these two pairings on an obstruction subsequence. It does not bound the signed Rayleigh quotient from above on the actual high set.

In the capped identity \(KU=a-\mu\mathbf1\), its pairing with \(q\) is \((A-\mu)\mathbb E_n q\). On \(S\), \(U=\epsilon(A+q)\). The corrected form of draft (C) is
\[
 \langle Kq,(A+q)1_S\rangle_{2,n}
  =\epsilon(A-\mu)\mathbb E_n q
      -\epsilon\langle Kq,U1_{S^c}\rangle_{2,n}.
\]
The factor \(\epsilon\) in the first term is required. The fixed capped \(U\) obeys \(\|U\|_{2,n}\le2/(1-q_M)\) with the actual capped contraction rate \(q_M\). The draft's comparison to an \(O(n^{1/4})\) normalized size misses this bound. It would already give exterior transport \(O(n^{-1/4})=o(1)\). In fact the exact corrected identity gives the better bound \(O(n^{-1/2})\), because \(\mathbb E_n q=O(n^{-1/2})\) and the left side is at most
\[
 \|q\|_{2,n}\|(A+q)1_S\|_{2,n}=O(n^{-1/2}).
\]
Here \(q\le L\) and \(|S|=O(\sqrt n)\). At the intrinsic \(\sqrt n\) rescaling this is only an \(O(1)\) bound. An unscaled vanishing exterior term therefore gives no exclusion of a fixed positive rescaled correlation. Moreover this identity concerns the bounded capped row on \(S\), not the true stationary high-source vector of the Rayleigh test.

The draft's broader warning from [the arbitrary weighted example](parallel-cap-19.md) requires care. That example is for a one-direction gain with probability weights and a rectangular receiver, rather than an actual one-sign stationary Rayleigh quotient. It gives no counterexample for the present high-source restriction. The unresolved arithmetic question is the genuine gap with the actual factors and actual cap rate. [The mark-oriented comparison](mark-oriented-overflow-107.md) additionally identifies the sign of one relevant factor by retaining the exact marked term.

The returned suggestions were an exterior transport estimate and an independent stationary-sector restricted estimate. The first only distinguishes the obstruction if it controls the appropriate rescaled term and supplies a bridge from the cap to the true high source. The second remains a direct prime-uniform target.
