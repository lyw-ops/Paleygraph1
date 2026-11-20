# Scalar subtraction and the trace of the true cold block

Use the genuine fully marked height-601 and height-602 derivatives \(D_h=\operatorname{diag}\Phi_t'(V_h)\) on the original closed square \(Q\). Let \(B=KD_{602}KD_{601}\), \(P=I-J_0\), and \(X=\operatorname{ran}P\). The left factor \(K\) makes \(B\) map into \(X\). Each of \(B\), \(P\), and \(B-sP\) therefore preserves \(X\).

At the real center \(t=a=2031/128\), the [height-601 counting estimate](cold-combined-height-130.md) gives \(\|KD_{601}\|_{2\to2}<0.5145\), and the [verified height-602 cap](cold-positive-block-131.md) gives \(\|V_{602}\|_\infty<4.8\). On the real physical sheet the derivative modulus at a site of floor \(u>0\) is \(|z|/\sqrt{4u+z^2}\). Both floors \(a,n\) are at least \(a\) for the fields in question. Thus \(\|KD_{602}\|_{2\to2}\le4.8/\sqrt{4a+4.8^2}<0.517\). Every eigenvalue \(\lambda\) of \(B|_X\) has \(|\lambda|<0.5145(0.517)\). For any scalar \(s\) and any induced norm on \(X\),
\[
 \|(B-sP)|_X\|\ge \rho((B-sP)|_X)\ge |s|-0.5145(0.517).
\]

The round-132 cold proposal writes the actual block as \(sP+(B-sP)\) at the center, for \(s=a/(4+a)=2031/2543\). The decomposition is an exact algebraic identity. The proposed sufficient triangle bound has value at least \(2s-0.5145(0.517)>1.33\), for every induced norm on \(X\). In particular the entire remainder cannot have norm below \(1-s\) in any such norm, even at the real center. The scalar \(a\) was the floor parameter. In the actual nine-center expansion the residual-degree-zero derivative is \(\Phi_t'(C)\) with \(C\) the center row. Off the mark its convergent expansion is odd in \(C\), whose components are negative trace fields.

## An arithmetic obstruction for any large scalar

There is also a square-uniform trace bound on the actual block. A translated column \(Ke_i\) is a physical negative trace representation with dimensional cost \(O(n^{-1/2})\) and one translated boundary pair, as in [Round 96](shifted-resolvent-96.md). The height-602 row has dimensional cost below \(4.8\). Off the mark expand its derivative by the same odd binomial expansion as in [Round 126](cold-actual-first-insertion-126.md#uniform-word-cost-and-the-two-translated-columns). At order \(2\ell+1\) of that expansion each term of \(d_{602}(Ke_i)^2\) has an odd number \(2\ell+3\) of negative factors. Their boundary characters belong to the union of the base and this one translated pair. The uniform odd trace estimate of Round 126 bounds their normalized mean by their dimensional product times \(O((2\ell+3)/\sqrt p+1/p)\). The two column factors supply \(O(n^{-1})\), and the remaining series sums absolutely because \(4.8^2<4\inf_Q\Re t\). After conversion of the normalized mean to a matrix entry,
\[
 (KD_{602}K)_{ii}=O(n^{-1/2})
\]
uniformly in the coordinate and in \(t\). The real-marked derivative differs from the bulk formula by a bounded scalar at the single marked coordinate. Its entry contribution is \(O(|K_{i0}|^2)=O(n^{-1})\). The physical exceptional products on the two boundary coordinates are already in the odd trace estimate.

The height-601 derivative has uniformly bounded entries on \(Q\), so the diagonal of \(B\) has the same bound. On the quotient by \(X\), \(B\) induces zero. Consequently
\[
 \left|\frac{\operatorname{tr}(B|_X)}{n-1}\right|=O(n^{-1/2}).
\]
The spectral radius of \((B-sP)|_X\) is at least the modulus of its mean eigenvalue. It follows that any induced norm on \(X\) satisfies
\[
 |s|+\|(B-sP)|_X\|\ge 2|s|-O(n^{-1/2}).
\]
Thus for any scalar of modulus exceeding \(1/2\) by a fixed amount, a separate triangle upper cannot give contraction through eligible primes. This uses the actual signed block, including both marked derivatives, without an assumption about the shape of a packet price. The real-center obstruction above is already a finite-prime strict comparison for the proposed scalar. A jointly collected estimate for the signed full block and both genuine half-step sheets remains open.
