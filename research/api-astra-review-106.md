# Independent resource rates for a physical growing starter

The [Astra API draft](api-astra-newton-106.txt) proposes using actual adjacent increments and a signed negative representation of the derivative difference on the nominated square. [Completion receipt](api-astra-106-receipt.json). The useful part is a finite-variable correction for a growing bad-character count in the [frozen transfer](frozen-entry-transfer-105.md). The proposed starter mechanism still requires independent bounds on the genuine rows.

## A field-size budget for exceptional characters

Let \(Z_a=L_h+T_h\) be the true starting translated inverse and its truncated columns. Assume dimension mass at most \(B n^{-1/2}\rho^h\) for the columns of \(L_h\), with \(\rho>1\), and \(\|T_h\|_{2\to2}\ll q^h\), \(0<q<1\). Here \(q\) is the counting operator rate at the fixed starting row. Write the diagonal difference \(E=D_b-D_a\) as a negative-field sum of dimension mass \(W\) plus a residual supported on exceptional coordinates with counting first norm \(M_{\rm exc}\), as in Round 105. Suppose the three-field words used at cutoff \(h\) have at most \(F_{h,n}\) bad full Mellin characters, including those in the lift expansions. Assume the same rank and dimension bounds for the words. Then the signed estimate in the draft is valid in the form
\[
 \|Z_a E Z_a\|_{\max}\ll
 B^2 W\rho^{2h}\left(p^{-1/2}+\frac{F_{h,n}}{p}\right)
 + B^2 M_{\rm exc}n^{-1}\rho^{2h}
 + B \|E\|_{2,n}(\rho q)^h+\|E\|_\infty q^{2h}.
\]
Indeed the contribution from each missing character before averaging is at most a constant times the product of the three dimensions. The odd nonpunctual trace term continues to give \(p^{-1/2}\). Both counting-norm tail terms are unchanged. This assumes approximations with the displayed uniform resources at the actual starting row. A normalized second-norm bound on \(E\) gives no bound of this kind on \(W\).

In particular \(F_{h,n}=O(p^{1/2})\) preserves the full signed exponent. More generally assume \(F_{h,n}=O(p^\theta)\) at the needed cutoffs, for \(0\le\theta<1\), and put
\[
 \omega=\min(1/2,1-\theta),\qquad
 \ell=\log(\rho/q),\qquad
 h=\frac{\omega}{2\ell}\log n+O(1),\qquad
 \beta_\omega=\frac{\omega|\log q|}{\ell}.
\]
For bounded \(W,M_{\rm exc},\|E\|_\infty\), the first, second and fourth terms are \(O(n^{-\beta_\omega})\). For the crossed term \((\rho q)^h=O(n^{\omega/2-\beta_\omega})\). If the true normalized diagonal difference has \(\|E\|_{2,n}=o(n^{-(1-\beta_\omega)/2})\), this term is \(o(n^{-\beta_\omega})\), since \(\beta_\omega\le\omega\le1/2\). The usual single-column entry test at \(H=(\log n)/(2\ell)+O(1)\) gives \(O(n^{-|\log q|/(2\ell)})\), hence also \(O(n^{-\beta_\omega})\), provided the column and tail bounds hold up to \(H\). The signed mixed term and the quadratic transfer thus use the same residual exponent \((1-\beta_\omega)/2\) even with this relaxed boundary allowance. No growing \(F_{h,n}\) estimate is supplied for the genuine words.

## Keep Picard depth and column length independent

A hypothetical residual estimate \(r_a\le C q_R^{a-a_0}\) from a fixed initial height \(a_0\), with \(r_a=\|V_{a+1}-V_a\|_{2,n}\) and \(q_R<1\), makes
\[
 a-a_0-\frac{1-\beta_\omega}{2|\log q_R|}\log n\longrightarrow+\infty
\]
sufficient for the required residual scale. The estimate is an upper envelope. Failure to certify the residual at a particular depth gives no lower bound on the required Picard height. The API draft also calls \(h=(\log n)/(4\ell)\) the single-column cutoff at \(\omega=1/2\). It is the cutoff for the **two-column product**, while \(H=2h+O(1)\) is the single-column cutoff. Even with \(q_R=q\), choosing \(a\) at the single-column cutoff is sufficient on the geometric upper envelope when \(\beta_\omega=|\log q|/(2\ell)>1/3\). The depth choice is a comparison of sufficient tests.

The residual contraction rate \(q_R\), the counting inverse-tail rate \(q\), and the column packet growth allowance \(\rho\) are separate inputs. The rounded height-250, 300 and 600 packet upper bounds cited in the draft are indeed from [the fixed physical replays](astra-adjoint-82.md). Crossing one there concerns an absolute packet upper. The inverse-tail estimate can have a separate counting rate below one, as in the [translated calculation](shifted-resolvent-96.md). A packet norm envelope would have to start from a packet norm bound, rather than identify its initial constant with \(r_a\). A residual estimate from a fixed \(a_0\) requires control from that height up to the moving \(a\), not only after \(a\).

The draft ranks a cumulative residual product and a signed derivative-difference representation. In the corrected form, the first asks for a genuine normalized-\(2\) residual bound at a moving starting row that also has independent uniform translated column resources. The second asks for coefficient dimension mass and controlled bad fibers, neither of which follows from the normalized \(2\)-norm alone.
