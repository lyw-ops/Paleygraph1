# Bare-block means and true overflow energy

The two API responses remain drafts. [Receipts](api-astra-105-receipts.json) · [Bare-block draft](api-astra-newton-105.txt) · [Overflow draft](api-astra-overflow-105.txt)

## Bare-block mean

For an actual diagonal change \(E_j=D_{j+1}-D_j\), the trace of the bare \(K E_j K\) is \((n-1)\mathbb E_n(E_j)_{ii}\). This follows from \(K^2=I-J_0\). Consequently a uniform \(O(n^{-\beta}q^j)\) entry bound for the bare block requires that same held rate for the mean diagonal change. It is a necessary identity. The draft gives no genuine lower for the mean. An odd negative representation with bounded dimension mass and finitely many bad Mellin fibers does bound that scalar at order \(p^{-1/2}\), with an additional \(O(1/n)\) cost for a bounded exceptional coordinate, by the one-field specialization of the [parity estimate](frozen-entry-transfer-105.md#a-signed-bound-for-two-frozen-negative-mellin-columns). Its signed trilinear version treats the whole two-ended frozen block under the stated representation hypotheses. None of these establish a summable depth factor for actual increasing predictors. An assertion that those hypotheses hold on the whole growing orbit would require a separate proof.

The draft's ranked follow-ups target the genuine mean with its depth factor, then the traced and translated parts of the traceless block. A tiny measured mean by itself gives no entrywise bound.

For a purely scalar change, the scalar coefficient of the full two-ended kernel also survives its trace on real physical segments where both diagonal norms are at most \(d<1/\sqrt2\). In fact for mean-zero real \(v\), \(x_j=Z_jv\) satisfies \(\|x_j-Kv\|_2\le d\|x_j\|_2\) and \(\|x_j\|_2\ge\|v\|_2/(1+d)\). Each angle to \(Kv\) is at most \(\arcsin d\). Summing the lower bound for \(x_a\cdot x_b\) over an orthonormal mean-zero basis gives
\[
 \frac1n\operatorname{tr}(Z_bZ_a)\ge
 (1-1/n)\frac{1-2d^2}{(1+d)^2}.
\]
Both \(Z_j\) are real symmetric there and vanish on constants. This comparison for the pure scalar term supplies no lower for an actual diagonal change with its traceless part included.

## Energy concentration for the genuine receiving set

Use [the critical overflow rectangle](cap-overflow-rectangle-104.md). One can take the larger sign part \(R\) of the actual high-source set \(T'\), retaining comparable size and a fixed positive lower \(K\tau\ge d\) there. On \(R\) the actual \(Y\) has a fixed sign \(\epsilon\) and \(|Y|\ge\lambda\sqrt n\), since \(b-2\sqrt t\le|Y|\) off the mark. Let \(\rho=|R|/n\), \(u=1_R\), and \(S=\operatorname{supp}\tau\). Reciprocity gives \(\mathbb E_n u K\tau=\mathbb E_n (Ku)\tau\), and \(K^2=I-J_0\) gives \(\|Ku\|_{2,n}^2=\rho(1-\rho)\). Cauchy–Schwarz bounds the energy at the genuine sending support by
\[
 \|1_S Ku\|_{2,n}^2\ge d^2\rho^2/\alpha,\qquad
 \alpha\ge d^2\rho/(1-\rho).
\]
At the critical scale the first inequality places a positive fraction of the exact \(Ku\) energy on \(S\). The lower bound on \(\alpha\) is already implicit in the earlier upper on the size of the receiving set. It is not a new exception to the \(O(n^{-1/2})\) premise.

For \(A=\mathbb E_n uK\tau\), \(B_R=\mathbb E_n u\epsilon Y\), and \(g=b-2\sqrt t\), project \(K\tau,\epsilon Y\) off \(u\). The true equations and Cauchy–Schwarz give
\[
 \left|\epsilon\mathbb E_n[\tau_i((I-J_0)g)_i]-\frac{AB_R}{\rho}\right|
 \le \sqrt{\left(\|K\tau\|_{2,n}^2-\frac{A^2}{\rho}\right)
            \left(\|Y\|_{2,n}^2-\frac{B_R^2}{\rho}\right)} .
\]
The center \(AB_R/\rho\) has a fixed positive lower at critical scale. The right side can still be order one, so the formula forces the global signed overlap only with an additional small residual product. For example, under the established \(O(\sqrt n)\) upper on \(\|Y\|_{2,n}^2\) from the coherence bound and \(\mathbb E_n|Y|\le\nu\), a first residual factor \(o(n^{-1/2})\) suffices. No near saturation is established on the genuine sets.

The draft's ranked follow-ups ask for an upper on the actual restricted Jacobi energy and an estimate for the centered overlap. Both obligations and the critical cap-defect rate remain open.
