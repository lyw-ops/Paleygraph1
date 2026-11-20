# Round 182 native Claude draft: one-match operator norm of the actual affine weight

- call_id: `ordinary-prime-one-match-operator-norm`
- agent_label: `session/r182-opnorm`
- Mission: `coordination/missions/round-182/ordinary-prime-one-match-operator-norm.md` (coordinator record `coordination/round-181.json`, SHA-256 `f237fdab…2d51`). All seven listed inputs were read; their SHA-256 hashes matched the mission.
- Status: agent draft (complete). Not an acceptance, not a human review, not a mathematical certification.
- Scripts: `research/paley-182-opnorm-identities.py` (exact), `research/paley-182-opnorm-models.py` (floating evidence, exact integer moment columns).

## Result summary

**Outcome: inconclusive, with a sharpened criterion.** No bound improving the accepted one-match covariance exponent 115/64 is proved.

1. **Re-proved (a).** The splitting \(S(t)=M_1^2G^2/p+\|\pi(\mu)h_t^\circ\|^2\) and, for every \(k\ge1\), the trace identity
\[
 \operatorname{tr}\bigl((\pi(\mu)\pi(\mu)^*)^k\bigr)=p\,T_k(\mu)-T_k^\times(m),
\]
whose \(k=1\) case is the Hilbert–Schmidt identity \(\|\pi(\mu)\|_{HS}^2=p\sum\mu^2-\sum_r m(r)^2\). The one-dimensional representations of the affine group remove exactly the slope-closed words, averaged over translations; at \(k=2\) this is the fibrewise variance \(p\sum_a\sum_c(\Delta(a,c)-C(a)/p)^2\).
2. **Criterion b1′ is saturated, not refuted (a).** The kernel of the actual chart has one degenerate row, the output \(s=1\): \(K(1,x)=g(1/x)\,n(1/x)\) with \(n(Y)\) a square-class mass of \(g\). Hence
\[
 \|\pi(\mu)\|_{op}^2\ \ge\ \sum_Y g(Y)^2 n(Y)^2-M_1^2/p,
\]
which is \(\asymp p^{3/2}\) whenever \(\sum g^2\asymp\sqrt p\) and both square classes of \(1-D\) carry \(\asymp\sqrt p\) of the mass of \(g\). Every entry of \(K\) is at most \(G\) (using \(g\le1\)), so every row and column has norm at most \((GM_1)^{1/2}=O(p^{3/4})\). The exponent \(3/4\) in b1′ is therefore exact under that hypothesis. It cannot be improved without first proving \(\sum g^2=o(\sqrt p)\). With the row included, every trace-moment criterion \(\operatorname{tr}((\pi\pi^*)^k)=O(p^{3k/2})\) is at its floor and has no room for a \(p^{o(1)}\) loss.
3. **The physical criterion never sees that row (a).** \(H_\alpha\) carries \(1_{s\ne1}\) (Round 169). So the sufficient criterion is the row-deleted b1″: \(\|R\,\pi(\mu)\|_{op}=O(p^{3/4})\), where \(R\) deletes the outputs \(s=0,1\). By interlacing, \(\sigma_3(\pi(\mu))\le\|R\pi(\mu)\|\le\sigma_1(\pi(\mu))\). After the deletion, every remaining fibre except the diagonal is an irreducible conic, and the diagonal costs at most \(G\).
4. **Blocking terms (a, method statements).**
   - *k = 2.* The verified bound is \(\operatorname{tr}((\pi\pi^*)^2)\le p\,\mathcal E(\mu)=O(p^{59/16})\), which gives \(\|\pi(\mu)\|\le p^{59/64}\); the need is \(\operatorname{tr}((\pi\pi^*)^2)=O(p^{3})\). The point–plane route contains \(p\sum_\xi W_\xi^{3/2}\ge pM_1^3/\sqrt{p-1}\), so it cannot pass \(p^{1/8}M_1^{3/4}\) (that is \(p^{7/8}\) if \(M_1\asymp p\)). Moreover \(p^3\) is the floor of the second moment (row and Hilbert–Schmidt), so \(k=2\) would need an optimal-order affine energy.
   - *k = 3.* The trivial representation leaves \(pT_3\ge M_1^6/(p-1)\), which exceeds the target \(p^{9/2}\). The slope-energy subtraction is therefore indispensable. The blocking term is the translation discrepancy of slope-closed six-words, \(p\,T_3-T_3^\times(m)\). Its verified bound is \(O(p^{177/32})\); the need is \(O(p^{144/32})\).
5. **Evidence (c), floating point.** Four auxiliary 0/1 models, not the actual optimiser: an exact multiplicative subgroup, a log-interval, a random subset and an interval of squares. Each has \(|\operatorname{supp}g|=q=\sqrt{p-1}\) at \(p=q^2+1\in\{401,677,1297,1601,2917\}\).
   - \(\sigma_1(\pi(\mu))\) exceeds the exact row-one lower bound by at most 12%, at \(0.45\text{–}0.57\,p^{3/4}\).
   - \(\sum\sigma^4/p^3\in[0.36,0.64]\), so the second moment sits at its floor.
   - The row-deleted norm \(\|R\pi(\mu)\|\) is \(1.3\text{–}1.9\sqrt p\), with local growth exponents \(0.54\) (random) to \(0.60\) (subgroup) between \(p=401\) and \(2917\). That is \(0.19\text{–}0.37\,p^{3/4}\), decreasing.
   - This supports b1″ in these models and shows no power-excess obstruction, including for the exact subgroup.

## Setup recalled

All objects are the accepted ones of Rounds 169, 171, 173, 178 and 180. Counting norms are used throughout.

- **Weights.** \(g=|f|^2\) on the squares \(Q\), extended by zero; \(0\le g\le1\); \(G=\sum g=O(\sqrt p)\); \(w=g(1-g)\ge0\), so \(\sum_t w(t)\le G\). On nonzero \(x\), \(g(x)=\sum_\alpha\omega(\alpha)\alpha(x)\) with \(\omega\) the actual law (a probability on the characters of \(Q\)) and \(\max\omega=O(p^{-1/2})\) (Rounds 171 and 173).
- **Chart (Round 171).** For \(Y,D\in\mathbb F_p\setminus\{0,1\}\) with \(Y\ne D\),
\[
 r=\frac{Y-D}{1-D},\qquad b=\frac{D(1-Y)}{Y(1-D)},\qquad j_{Y,D}(e)=re+b .
\]
The map \((Y,D)\mapsto(r,b)\) is injective, and \(r,b\notin\{0,1\}\). The physical square mask is \(b\in Q\), equivalently \(\chi(1-Y)=\chi(1-D)\) for the Legendre symbol \(\chi\) when \(Y,D\in Q\).
- **Weight on the affine group.** \(\mu(r,b)=g(Y)g(D)\) on admissible pairs and zero elsewhere. Write \(M_1=\sum\mu\le G^2\), \(m(r)=\sum_b\mu(r,b)\), \(\Delta(h)=\sum_j\mu(j)\mu(jh)\), \(\mathcal E(\mu)=T_2(\mu)=\sum_h\Delta(h)^2\), \(C(a)=\sum_c\Delta(a,c)=\sum_r m(r)m(ar)\).
- **Group law.** \((r,b)\circ(r',b')=(rr',rb'+b)\).
- **Operators.** \(U_jf(s)=f(j^{-1}s)\), \(F_\mu=\sum_j\mu(j)U_j\), with kernel \(K(y,x)=\sum_{j:\,jx=y}\mu(j)\). \(\pi(\mu)\) is the restriction of \(F_\mu\) to the mean-zero functions \(\mathbf 1^\perp\); it is the \((p-1)\)-dimensional irreducible representation of the affine group (Round 171). \(R\) is the coordinate restriction to outputs \(s\notin\{0,1\}\).
- **Twisted input (Round 178).** \(h_t(e)=g(t/e)\) for \(e\ne0\) and \(h_t(0)=0\). Then \(\sum_e h_t(e)=G\) for \(t\ne0\), and \(\|h_t\|_2^2=\sum g^2\le G\). The last inequality is the only place where \(g\le1\) is used for \(h_t\).
- **One-match normalization (Rounds 169, 173, 178).**
  - The covariance target \(O(p^{3/2})\) is equivalent to \(\sum_{s\ne0,1,t}w(t)|H_\alpha(s,t)|^2=O(p^{5/2})\); covariance exponent = weighted exponent − 1.
  - After the endpoint terms, which are already priced at \(O(p^{5/2})\), completing the factor \(g(C)\) by one gives \(0\le H_\alpha(s,t)\le (F_\mu h_t)(s)\) for \(s\notin\{0,1\}\). This is the positive upper of Round 173, used verbatim in Round 178.
  - The accepted state (Round 180) is weighted \(O(p^{179/64})\), covariance \(O(p^{115/64})\), with \(\mathcal E(\mu)=O(p^{43/16})\), \(E^\times(m)=O(p^{27/8})\) and \(\sum_\xi W_\xi^{3/2}=O(p^{43/16})\).
- **Weights majorized by one.** \(g\le1\) is used for \(\|h_t\|^2\le G\) and for the entry bound \(K(y,x)\le G\). \(w\) is used only through \(\sum_t w\le G\). The square mask and \(g(C)\) are majorized by one (positive completion). Nothing else is majorized.

## Argument

Throughout, \(t\ne0\) and \(p\) is an odd prime. All statements in this section are proved in full here. None of them cites a Round 181 proof.

### Proposition 1 (splitting; re-proof of the Round 181 claim)

\[
 S(t):=\|F_\mu h_t\|_2^2=\frac{M_1^2G^2}{p}+\|\pi(\mu)h_t^\circ\|_2^2,\qquad h_t^\circ=h_t-\frac Gp\mathbf 1 .
\]

*Proof.* Each \(U_j\) is a permutation matrix. Hence \(F_\mu\mathbf 1=M_1\mathbf 1\) and \(\sum_s(F_\mu f)(s)=M_1\sum_e f(e)\), so \(F_\mu\) maps \(\mathbf 1^\perp\) into \(\mathbf 1^\perp\). Since \(\sum_e h_t(e)=\sum_{e\ne0}g(t/e)=G\), we get \(F_\mu h_t=(M_1G/p)\mathbf 1+\pi(\mu)h_t^\circ\). The two summands are orthogonal and \(\|\mathbf 1\|^2=p\). \(\square\)

The same argument applies to the adjoint \(F_\mu^*=\sum_j\mu(j)U_{j^{-1}}\): it fixes \(\mathbf 1\) up to \(M_1\) and preserves \(\mathbf 1^\perp\). So \(\mathbb C^p=\mathbb C\mathbf 1\oplus\mathbf 1^\perp\) reduces every word in \(F_\mu,F_\mu^*\).

### Proposition 2 (trace identity for every moment; Hilbert–Schmidt re-proved)

For \(k\ge1\), let \(\nu_k(h)\) be the \(\mu^{\otimes2k}\)-weight of the words \(j_1j_2^{-1}j_3j_4^{-1}\cdots j_{2k-1}j_{2k}^{-1}=h\). Put \(T_k(\mu)=\nu_k(\mathrm{id})\). Let \(T_k^\times(m)\) be the \(m^{\otimes2k}\)-weight of \(r_1r_2^{-1}\cdots r_{2k}^{-1}=1\) in \(\mathbb F_p^*\). Then
\[
 \operatorname{tr}\bigl((\pi(\mu)\pi(\mu)^*)^k\bigr)
 =p\,T_k(\mu)-T_k^\times(m)
 =p\Bigl(\nu_k(1,0)-\frac1p\sum_{c}\nu_k(1,c)\Bigr).
\]

*Proof.* Expanding, \((F_\mu F_\mu^*)^k=\sum_h\nu_k(h)U_h\). The trace of the permutation matrix \(U_h\) is the number of fixed points of \(h=(a,c)\):
- \(p\) for \(h=\mathrm{id}\);
- exactly one when \(a\ne1\), since \(ae+c=e\) has the single root \(c/(1-a)\);
- none when \(a=1\) and \(c\ne0\).

Hence \(\operatorname{tr}_{\mathbb C^p}=p\,\nu_k(\mathrm{id})+M_1^{2k}-\sum_c\nu_k(1,c)\). The slope is a homomorphism \((r,b)\mapsto r\), so \(\sum_c\nu_k(1,c)\) is the weight of the words with slope product \(1\), which is \(T_k^\times(m)\). Finally, by the reduction above, \(\operatorname{tr}_{\mathbb C^p}=M_1^{2k}+\operatorname{tr}_{\mathbf 1^\perp}\). \(\square\)

**Which part each representation removes.**
- In the permutation module, the trivial summand removes exactly \(M_1^{2k}\).
- In the regular representation, \(|\mathrm{Aff}|\,T_k=\sum_\chi|\hat m(\chi)|^{2k}+(p-1)\operatorname{tr}_\pi\). The \(p-1\) one-dimensional characters \(\chi(r)\) see only the slope marginal \(m\), and they remove \(T_k^\times(m)\): the slope-closed words averaged over their translation part. The trivial character's share is \(M_1^{2k}/(p-1)\).

**The cases \(k=1,2\).**
- At \(k=1\), \(\|\pi(\mu)\|_{HS}^2=p\sum\mu^2-\sum_rm(r)^2\). This is the Round 181 identity, now re-proved.
- At \(k=2\), \(\operatorname{tr}((F^*F)^2)=\operatorname{tr}((FF^*)^2)\) gives \(T_2=\sum_h\Delta(h)^2=\mathcal E(\mu)\), the genuine right energy of Round 178, and \(\sum_c\Delta(a,c)=C(a)\). Therefore
\[
 \operatorname{tr}\bigl((\pi\pi^*)^2\bigr)=p\,\mathcal E(\mu)-E^\times(m)
 =p\sum_a\sum_c\Bigl(\Delta(a,c)-\frac{C(a)}p\Bigr)^2 .
\]
The one-dimensional part is exactly the fibrewise mean.

**Exact check.** C3 of `paley-182-opnorm-identities.py` verifies the identity exactly for \(k=1,2,3\) on the actual masked chart, with random integer \(g\) on \(Q\), at \(p=13,17,29\).

### Proposition 3 (geometry of the actual kernel)

**(i) Fixed point.** \(j_{Y,D}\) has fixed point \(b/(1-r)=D/Y\), since \(1-r=(1-Y)/(1-D)\).

**(ii) Fibre equation.** For \(x\in\mathbb F_p\), \(j_{Y,D}(x)=y\) is equivalent to
\[
 D\bigl(1-(1+x-y)Y\bigr)=Y(y-xY).
\]
To see this, multiply \(b+rx=y\) by \(Y(1-D)\ne0\).

**(iii) At most one \(D\) per \(Y\) unless \(y=1\).** Suppose the coefficient of \(D\) vanishes. Then \(Y(y-xY)=0\) forces \(y=xY\), and \(1-(1+x-xY)Y=(1-Y)(1-xY)=0\) forces \(xY=1\) and \(y=1\). When \(y=1\) the equation reads \((D-Y)(1-xY)=0\), and \(D=Y\) is excluded. Hence, exactly,
\[
 K(1,x)=g(1/x)\,n(1/x)\ (x\ne0),\qquad K(1,0)=0,\qquad
 n(Y)=\!\!\sum_{\substack{D\in Q\setminus\{1,Y\}\\ \chi(1-D)=\chi(1-Y)}}\!\! g(D).
\]
(\(K(1,0)=0\) because \(j(0)=b\ne1\).)

**(iv) The diagonal.** For \(y=x\), the equation is \((1-Y)(D-xY)=0\), so \(K(x,x)=\sum_Y g(Y)g(xY)\) over admissible \(Y\), which is at most \(G\).

**(v) The other fibres are irreducible conics.** The conic \(D-(1+x-y)YD-yY+xY^2=0\) has symmetric-matrix determinant \(-(x-y)(1-y)/4\). For \(y\notin\{1,x\}\) it is therefore a nondegenerate conic. C5 checks by brute force at \(p=7,11,13\) that the zero set contains a line exactly when \(y\in\{1,x\}\).

**(vi) Entries, rows and columns.**
- By (iii) and \(g\le1\), \(K(y,x)\le\sum_Y g(Y)\cdot\max g\le G\) for every \((y,x)\).
- Every row and every column of \(K\) sums to \(M_1\), since each \(j\) is a bijection.
- Hence every row and column has squared norm at most \(GM_1\le G^3=O(p^{3/2})\). (C6 checks this exactly.)

### Proposition 4 (the \(s=1\) row saturates b1′)

\[
 \|\pi(\mu)\|_{op}^2\ \ge\ \frac{\sum_Y g(Y)^2n(Y)^2-M_1^2/p}{1-1/p}
 \ \ge\ (G_{\min}-1)_+^2\sum_{Y\ne1}g(Y)^2-\frac{G^4}{p}.
\]
Here \(G_\pm=\sum_{D\in Q\setminus\{1\},\,\chi(1-D)=\pm1}g(D)\) and \(G_{\min}=\min(G_+,G_-)\). Conversely \(\sum_Y g^2n^2\le G^2\sum g^2\le G^3\), so the row never exceeds \(G^{3/2}\).

*Proof.* Take \(v=\delta_1-p^{-1}\mathbf 1\in\mathbf 1^\perp\), so \(\|v\|^2=1-1/p\). Since \(F_\mu^*\delta_1=K(1,\cdot)\) and \(F_\mu^*\mathbf 1=M_1\mathbf 1\),
\[
 \|\pi(\mu)^*v\|^2=\sum_x K(1,x)^2-2\frac{M_1}p\sum_xK(1,x)+\frac{M_1^2}p=\sum_xK(1,x)^2-\frac{M_1^2}p .
\]
Now use \(\|\pi(\mu)\|=\|\pi(\mu)^*\|\), Proposition 3(iii), the substitution \(x\leftrightarrow Y=1/x\), and \(n(Y)\ge G_{\chi(1-Y)}-g(Y)\ge G_{\min}-1\). \(\square\)

**Corollary 4′ (exponent 3/4 is exact under a mass hypothesis).** Assume \((\mathrm H_{\rm sat})\): \(G\ge c_0\sqrt p\), \(\sum g^2\ge c_1G\) and \(G_{\min}\ge c_2G\). Then for large \(p\), \(\|\pi(\mu)\|_{op}\ge\tfrac12c_2c_1^{1/2}c_0^{3/2}p^{3/4}\). Consequently:
- \(\|\pi(\mu)\|=o(p^{3/4})\) cannot hold under \((\mathrm H_{\rm sat})\).
- For every \(k\), \(\operatorname{tr}((\pi\pi^*)^k)\ge c^{2k}p^{3k/2}\), so each moment criterion \(\operatorname{tr}((\pi\pi^*)^k)=O(p^{3k/2})\) for b1′ is at its floor.
- Without \((\mathrm H_{\rm sat})\) the row is still at most \(G^{3/2}\), so it never refutes b1′.

This settles the mission's refutation branch for this obstruction. A coset-concentrated level set does not push \(\|\pi(\mu)\|\) above \(p^{3/4}\) by a power through any single row or column, because Proposition 3(vi) caps all of them at \((GM_1)^{1/2}\).

### Proposition 5 (the physical criterion only needs the row-deleted operator)

Let \(\sigma_R=\|R\,\pi(\mu)\|_{\mathbf 1^\perp\to\ell^2}\). Then
\[
 \sum_{s\ne0,1,\,t}w(t)\,|F_\mu h_t(s)|^2\ \le\ \frac{2G^7}{p}+2\sigma_R^2\,G\sum g^2\ \le\ \frac{2G^7}p+2\sigma_R^2G^2,
\]
and \(\sigma_3(\pi(\mu))\le\sigma_R\le\sigma_1(\pi(\mu))\).

*Proof.* Write \(c=M_1G/p\le G^3/p\) and \(v=\pi(\mu)h_t^\circ\). Then \(\sum_{s\notin\{0,1\}}|c+v(s)|^2\le2c^2p+2\|Rv\|^2\), and \(\|h_t^\circ\|^2=\sum g^2-G^2/p\le\sum g^2\). Sum against \(w\), using \(\sum w\le G\).

For interlacing: \(R\) is an orthogonal projection, which gives the upper inequality. For the lower one, let \(V\) be the span of the top three right singular vectors. Some unit \(u\in V\) satisfies the two linear conditions \((\pi u)(0)=(\pi u)(1)=0\), so \(\|R\pi u\|=\|\pi u\|\ge\sigma_3\). \(\square\)

**Criterion b1″ (conditional (b)).** Combined with \(0\le H_\alpha\le F_\mu h_t\) on \(s\notin\{0,1\}\) and the endpoint terms already priced at \(O(p^{5/2})\) (Rounds 169, 173, 178), \(\sigma_R=O(p^{3/4})\) implies a one-match covariance of \(O(p^{3/2})\).

Furthermore, write \(K=K_{(1)}+K_{\rm diag}+K_{\rm irr}\) (the row \(s=1\), the diagonal of Proposition 3(iv), and the irreducible conic fibres). On \(\mathbf 1^\perp\), \(|\sigma_R-\|RK_{\rm irr}\||\le\max_xK(x,x)\le G\). So b1″ is equivalent to \(\|RK_{\rm irr}\|_{\mathbf 1^\perp\to\ell^2}=O(p^{3/4})\): an operator assembled only from nondegenerate conics.

### Proposition 6 (what blocks each moment)

**(k = 2) Verified bound, floor and method limit.**
- *Verified bound.* By Proposition 2 and \(\mathcal E(\mu)=O(p^{43/16})\) (Round 180), \(\operatorname{tr}((\pi\pi^*)^2)\le p\,\mathcal E(\mu)=O(p^{59/16})\). Hence \(\|\pi(\mu)\|\le O(p^{59/64})\), against the need \(p^{48/64}\). Through Proposition 5 this alone gives a weighted bound of \(O(p^{91/32})\), covariance \(O(p^{118/64})\). That is weaker than the accepted \(115/64\), so the operator route does not improve the accepted exponent at \(k=2\).
- *Floor.* The needed bound \(O(p^3)\) is the floor. Under \((\mathrm H_{\rm sat})\), \(\sigma_1^4\asymp p^3\) by Corollary 4′. For the row-deleted operator, \(\operatorname{tr}((R\pi\pi^*R)^2)\ge\|R\pi\|_{HS}^4/(p-2)\) and \(\|R\pi\|_{HS}^2\ge\|\pi\|_{HS}^2-2GM_1\). This is \(\asymp p^3\) whenever \(p\sum\mu^2-\sum m^2\asymp p^2\). So a \(k=2\) proof needs \(p\,\mathcal E(\mu)-E^\times(m)=O(p^3)\) with no \(p^{o(1)}\) loss, an affine energy of optimal order.
- *Method limit.* The point–plane bound of Round 178 has the form \(\mathcal E(\mu)\ll\sum_\xi\bigl(W_\xi^2/p+W_\xi^{3/2}+G(1+\log p)W_\xi\bigr)\). Its first term could at best cancel against \(E^\times(m)/p=\sum_\xi W_\xi^2/p\); the middle term cannot. By Hölder over the \(p-1\) values of \(\xi\), \(\sum_\xi W_\xi^{3/2}\ge M_1^3/\sqrt{p-1}\). So that route yields at best \(\|\pi(\mu)\|\ll p^{1/8}M_1^{3/4}\), which is \(p^{7/8}\) when \(M_1\asymp p\).

**(k = 3) The blocking term.**
- *The subtraction is indispensable.* \(T_3=\sum_h\lambda(h)^2\) with \(\lambda\) the law of \(j_1j_2^{-1}j_3\) (the reversed word has the same law), so \(T_3\ge M_1^6/(p(p-1))\) and \(pT_3\ge M_1^6/(p-1)\). This is \(\asymp p^5\gg p^{9/2}\) when \(M_1\asymp p\). The slope-energy subtraction \(T_3^\times(m)\) must therefore cancel the main term to relative precision \(p^{-1/2}\).
- *The blocking term.* It is the translation discrepancy of slope-closed six-words,
\[
 \mathcal D_3:=p\Bigl(\nu_3(1,0)-\frac1p\sum_c\nu_3(1,c)\Bigr)=\operatorname{tr}\bigl((\pi\pi^*)^3\bigr),
\]
which needs \(O(p^{9/2})=O(p^{144/32})\).
- *Verified bound.* \(\mathcal D_3\le\sigma_1^2\operatorname{tr}((\pi\pi^*)^2)\le\operatorname{tr}((\pi\pi^*)^2)^{3/2}=O(p^{177/32})\). It brings no gain over \(k=2\).
- *Floors and inputs.* The floor of the row-deleted analogue is \(\|R\pi\|_{HS}^6/(p-2)^2\asymp p^4\), so \(k=3\) is the first moment with room, \(p^{1/2}\). The full operator has floor \(\asymp p^{9/2}\) under \((\mathrm H_{\rm sat})\) and no room, so the row must be deleted before taking moments. I know of no incidence or sum-product theorem in \(\mathrm{Aff}(\mathbb F_p)\), with hypotheses met by \(\mu\), that controls six-word translation discrepancy. Petridis–Roche-Newton–Rudnev–Warren (arXiv:1911.03401, Theorem 2.1) and Rudnev–Shkredov (arXiv:1812.01671, Theorem 8) treat four-words, i.e. \(k=2\).

**Remark (character expansion).** \(\mu=\sum_{\alpha,\beta}\omega(\alpha)\omega(\beta)\,\mu_{\alpha\beta}\), with \(\mu_{\alpha\beta}(j_{Y,D})=\alpha(Y)\beta(D)\) on all admissible pairs. The trivial term \(\mu_{11}\) is the indicator of the whole admissible set (about \(p^2/8\) elements). Its row \(s=1\) has norm \(\asymp p^{3/2}\) by Proposition 4. So bounding \(\|\pi(\mu)\|\le\sup_{\alpha,\beta}\|\pi(\mu_{\alpha\beta})\|\) loses everything. A proof through the actual law must use cancellation across \(\omega\), not uniformity in the characters.

## Proved (a) / conditional (b) / evidence (c)

**Proved (a)**, on the inherited chart and normalizations of Rounds 169, 171, 173, 178 and 180, with the stated hypotheses only:
- **(a1)** Splitting \(S(t)=M_1^2G^2/p+\|\pi(\mu)h_t^\circ\|^2\) for \(t\ne0\) (Proposition 1).
- **(a2)** \(\operatorname{tr}((\pi(\mu)\pi(\mu)^*)^k)=pT_k(\mu)-T_k^\times(m)\) for every \(k\ge1\). Special cases:
  - \(k=1\): Hilbert–Schmidt, \(p\sum\mu^2-\sum m^2\).
  - \(k=2\): \(p\,\mathcal E(\mu)-E^\times(m)=p\sum_{a,c}(\Delta(a,c)-C(a)/p)^2\).
  - general \(k\): \(p\) times the identity-versus-translation discrepancy of slope-closed \(2k\)-words.

  The trivial summand of the permutation module removes \(M_1^{2k}\); the one-dimensional characters remove \(T_k^\times(m)\) (Proposition 2).
- **(a3)** Kernel geometry (Proposition 3): fixed point \(D/Y\); the fibre equation; \(K(1,x)=g(1/x)n(1/x)\); diagonal \(K(x,x)\le G\); every other fibre is a nondegenerate conic; entries \(\le G\) using \(g\le1\); row and column squared norms \(\le GM_1\).
- **(a4)** The row-one lower bound \(\|\pi(\mu)\|^2\ge\sum_Y g^2n^2-M_1^2/p\), and Corollary 4′: under \((\mathrm H_{\rm sat})\), \(\|\pi(\mu)\|\gg p^{3/4}\). Hence b1′ is exact at exponent \(3/4\) and every trace-moment criterion for b1′ is at its floor. The row is at most \(G^{3/2}\), so this is a saturation, not a refutation.
- **(a5)** The physical criterion is controlled by \(\sigma_R=\|R\pi(\mu)\|\): the weighted one-match sum over \(s\ne0,1\) is at most \(2G^7/p+2\sigma_R^2G\sum g^2\). Also \(\sigma_3(\pi)\le\sigma_R\le\sigma_1(\pi)\), and \(\sigma_R\) agrees with the norm of the irreducible-conic part up to \(G\) (Proposition 5).
- **(a6)** The verified operator bound is \(\|\pi(\mu)\|=O(p^{59/64})\), which gives covariance \(O(p^{118/64})\), weaker than the accepted \(115/64\). Method statements:
  - the \(k=2\) point–plane route cannot pass \(p^{1/8}M_1^{3/4}\);
  - at \(k=3\), \(pT_3\ge M_1^6/(p-1)\), so the slope subtraction is indispensable;
  - the verified bound is \(\operatorname{tr}((\pi\pi^*)^3)=O(p^{177/32})\), against the need \(O(p^{144/32})\) (Proposition 6).
- **(a7)** Method comparison. Put the optimal energy \(\mathcal E(\mu)=O(p^2)\) into the Rudnev–Shkredov level route of Round 178 at \(|U|\asymp\sqrt p\), \(M_1\asymp p\). That route gives \(S(t)\ll p^{17/8}\), covariance \(p^{13/8}\). The operator route with the fibre-variance energy \(p\mathcal E(\mu)-E^\times(m)=O(p^3)\) gives the target \(p^{3/2}\). The operator route is therefore the only one of the two that can reach the target at \(k=2\), and only with an optimal-order energy.

**Conditional (b):**
- **(b1″)** \(\sigma_R=O(p^{3/4})\) implies a one-match covariance of \(O(p^{3/2})\). It follows from b1′, and by (a4) it is the correct form.
- **(b1‴)** More precisely, \(\sigma_R^2\sum g^2=O(p^2)\) suffices; this couples b1 and b1″. For example, \(\sum g^2=O(p^{1/2-\delta})\) relaxes the need to \(\sigma_R=O(p^{3/4+\delta/2})\), i.e. a row-deleted second moment \(O(p^{3+2\delta})\).
- **(b-k3)** \(\operatorname{tr}((R\pi\pi^*R)^3)=O(p^{9/2})\) implies b1″. This is the first moment whose floor (\(\asymp p^4\) when \(\|\pi\|_{HS}^2\asymp p^2\)) leaves room \(p^{1/2}\).

**Evidence (c), floating power iteration on auxiliary models only.** The integer columns M1, HS2 and E2 are exact. Output of `python3 research/paley-182-opnorm-models.py 20 26 36 40 54` (ratios divided by \(p^{3/4}\); `conv` is the change of the estimate over the last five iterations):

```
p = 401 (q = 20),  p^(3/4) = 89.61
model         M1  HS2/p^2   E2/p^3 E2^(1/4)/p^.75 row1/p^.75  s1/p^.75 s1prime/p^.75     conv
subgroup     162   0.4023   0.3648         0.7772     0.4060    0.4535        0.3124  3.4e-07
geom         180   0.4467   0.4300         0.8098     0.4384    0.4735        0.2942  1.6e-04
random       180   0.4470   0.4248         0.8073     0.4384    0.4651        0.2894  7.4e-04
interval     188   0.4667   0.4740         0.8298     0.4682    0.4992        0.2978  9.4e-03
p = 677 (q = 26),  p^(3/4) = 132.72
subgroup     328   0.4831   0.5798         0.8726     0.5106    0.5709        0.3710  0.0e+00
geom         314   0.4626   0.4692         0.8276     0.4569    0.4854        0.2630  2.1e-02
random       314   0.4625   0.4658         0.8261     0.4569    0.4770        0.2629  7.7e-03
interval     314   0.4624   0.4647         0.8256     0.4569    0.4781        0.2639  4.7e-04
p = 1297 (q = 36),  p^(3/4) = 216.12
subgroup     578   0.4451   0.4465         0.8175     0.4463    0.4708        0.2400  2.5e-02
geom         614   0.4727   0.4943         0.8385     0.4679    0.4906        0.2287  3.6e-03
random       630   0.4850   0.5195         0.8490     0.4862    0.5009        0.2274  2.8e-02
interval     684   0.5264   0.6397         0.8943     0.5435    0.5612        0.2489  1.3e-04
p = 1601 (q = 40),  p^(3/4) = 253.10
subgroup     746   0.4654   0.5087         0.8445     0.4740    0.5106        0.2725  1.6e-13
geom         792   0.4941   0.5498         0.8611     0.4984    0.5186        0.2214  1.1e-02
random       778   0.4854   0.5223         0.8501     0.4858    0.4982        0.2170  2.5e-02
interval     760   0.4741   0.4935         0.8381     0.4690    0.4819        0.2152  4.2e-02
p = 2917 (q = 54),  p^(3/4) = 396.92
subgroup    1364   0.4673   0.5052         0.8431     0.4700    0.4982        0.2303  1.7e-12
geom        1502   0.5145   0.6154         0.8857     0.5254    0.5461        0.2388 -1.4e-14
random      1454   0.4981   0.5559         0.8635     0.5023    0.5115        0.1899  2.2e-02
interval    1406   0.4816   0.5134         0.8465     0.4780    0.4879        0.1869  4.1e-02
```

Reading the table:
- \(\sigma_1\approx\) the row-one bound, consistent with (a4).
- \(E_2=\sum\sigma^4\asymp p^3\), the floor of (a6).
- The row-deleted \(\sigma_R\) (`s1prime`) grows like \(p^{0.54\text{–}0.60}\), i.e. \(\approx1.3\text{–}1.9\sqrt p\) over this range.
- The models have \(\sum g^2=G\), so they satisfy \((\mathrm H_{\rm sat})\) whenever the square classes are balanced, as here.
- The power iteration value is a Rayleigh lower bound for each norm; the small `conv` column indicates it has essentially converged.
- Finite models do not settle the asymptotic target and are not evidence about the actual \(g\).

**Exact checks.** Output of `python3 research/paley-182-opnorm-identities.py`:

```
p=13 seed=0: C1-C4, C6 exact OK (k<= 3); M1=8, G=4
p=13 seed=1: C1-C4, C6 exact OK (k<= 3); M1=16, G=6
p=17 seed=0: C1-C4, C6 exact OK (k<= 3); M1=12, G=7
p=17 seed=1: C1-C4, C6 exact OK (k<= 3); M1=16, G=9
p=29 seed=0: C1-C4, C6 exact OK (k<= 3); M1=58, G=13
p=29 seed=1: C1-C4, C6 exact OK (k<= 3); M1=72, G=14
p=7: C5 degenerate fibres exactly y in {1, x}
p=11: C5 degenerate fibres exactly y in {1, x}
p=13: C5 degenerate fibres exactly y in {1, x}
all exact checks passed
```

These are finite exact checks of identities that are proved above for all \(p\); they are not the proof.

## Exact remaining gap

1. **One-match covariance target.** It is \(O(p^{3/2})\); the accepted bound is \(O(p^{115/64})\), unchanged by this draft. The operator route would close it through the single statement
\[
 \sigma_R^2\sum_Y g(Y)^2=O(p^2),\qquad \sigma_R=\|R\,\pi(\mu)\|_{\mathbf 1^\perp\to\ell^2},
\]
where \(R\) deletes the outputs \(s=0,1\), with the actual masked \(\mu\). By Proposition 5 this is equivalent, up to \(O(G)\), to the same bound for the operator built only from the nondegenerate conic fibres.
2. **Weakest unproved moment inequality.** It is \(\operatorname{tr}((R\pi\pi^*R)^3)=O(p^{9/2})\): the row-deleted translation discrepancy of six-words. At \(k=2\) the corresponding statement \(p\,\mathcal E(\mu)-E^\times(m)=O(p^3)\) has no room at all. Its verified bounds are:
   - \(O(p^{59/16})\) at \(k=2\), through \(\mathcal E(\mu)=O(p^{43/16})\);
   - \(O(p^{177/32})\) at \(k=3\).
3. **Unchanged.** The zero-match estimate, the generic J sum \(O(p^{9/4})\) and the coupled full diagonal are unchanged. Nothing here concerns the direct first mass or the cold route.
4. **What would change the proof plan.**
   - A proof of the six-word statement in 2, or of \(\sum g^2=o(\sqrt p)\) jointly with a \(k=2\) bound \(O(p^{3+2\delta})\).
   - Conversely, an actual-\(g\) configuration with \(\sigma_R\ge p^{3/4+\varepsilon}\) would refute b1″. Then the one-match target would need the specific vectors \(h_t^\circ\). None was found; the subgroup model is at \(\approx1.7\sqrt p\).

## Two ranked next tests

1. **Row-deleted sixth moment, by word type** (aims at b-k3).
   - First, compute \(\operatorname{tr}((R\pi\pi^*R)^3)\) exactly in the four models at \(p\le 677\). Split it by six-word type (coinciding letters, common fixed point \(D/Y\), common slope, generic) to see which classes reach \(p^{9/2}\).
   - Then seek a point–conic incidence bound for the generic class, using Proposition 3(v) that every surviving fibre is a nondegenerate conic. For any incidence theorem used (for example a Stevens–de Zeeuw-type or Vinh-type bound for conics over \(\mathbb F_p\)), state its exact hypotheses before applying it.
   - Success means \(O(p^{9/2})\), or any \(O(p^{9/2+\eta})\) with \(\eta<\tfrac{57}{64}\). That weaker bound still gives \(\sigma_R\le p^{3/4+\eta/6}\) and covariance \(p^{3/2+\eta/3}<p^{115/64}\).
2. **Decide \((\mathrm H_{\rm sat})\) for the actual \(g\)** (aims at b1‴).
   - Bound \(\sum g^2\) from the actual law (\(\sum_\alpha\omega(\alpha)^2=2\sum g^2/(p-1)\) by Parseval on \(Q\)), together with the square-class balance \(G_\pm\).
   - If \(\sum g^2=O(p^{1/2-\delta})\), the operator target relaxes to \(\sigma_R=O(p^{3/4+\delta/2})\).
   - If instead \(\sum g^2\asymp\sqrt p\), Corollary 4′ makes the unrestricted b1′ exactly critical. Every later operator argument must then delete the \(s=1\) row before any moment step.

## Replay

```
python3 research/paley-182-opnorm-identities.py            # exact, < 1 s
python3 research/paley-182-opnorm-models.py 20 26 36 40 54   # floating, a few minutes, ~140 MB peak
```
Both scripts use the Python 3 standard library only.
