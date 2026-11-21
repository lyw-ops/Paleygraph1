# Round 183 native Claude draft: the row-deleted one-match criterion

- call_id: `ordinary-prime-row-deleted-one-match`
- agent_label: `session/r183-rowdel` (Claude Opus 5.5 research side session)
- Mission: `coordination/missions/round-183/ordinary-prime-row-deleted-one-match.md` (coordinator record `coordination/round-182.json`, SHA-256 `bd56aa4c…680f`). All seven listed sources were read and their SHA-256 values match the mission. Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-182.md`, and, for the structural facts of Part 1, Rounds 20, 149, 151, 152, 153, 166, 173, 178, 180 (notes and acceptance proof scopes).
- Status: agent draft (complete). Not an acceptance, not a human review, not a mathematical certification.
- Script: `research/paley-183-rowdel-trace.py` (exact integer traces, exact type split, exact scalar inputs; spectral norms are floating and labelled).

## Result summary

**Verdict: inconclusive** (mission definitions). Neither \(\|R\pi(\mu)\|_{op}=O(p^{3/4})\) nor its failure is proved. The accepted one-match exponent \(115/64\) is unchanged. What changed:

1. **Part 1 (status of \(\sum g^2\)).** Not decided, but reduced and bounded.
   - The mission's normalization is off by a factor 2: \(\sum_x g(x)^2=(p-1)\sum_\alpha\omega(\alpha)^2=n\,\mathcal E(\nu)\), where \(\mathcal E(\nu)\) is the additive energy of the actual law \(\nu\) on \(\widehat Q\cong\mathbb Z/n\) (Proposition 1.1, exact).
   - **The square-class balance in \((\mathrm H_{\rm sat})\) is false for the actual law.** On the near-critical branch, the Round 151 sector estimate gives \(G_{-\rho}=O(1)\): almost all of the mass of \(g\) sits on \(\{\chi(1-x)=\rho\}\). Hence \(M_1=(1+o(1))p\) and \(G=(1+o(1))\sqrt p\), so the Round 182 hypothesis "\(M_1\asymp p\)" holds (Proposition 1.2).
   - The balance was never needed. The \(s=1\) row satisfies \(\|\pi(\mu)\|^2\ge(1-o(1))\,p\,(\sum g^2-C)\), so b1′ is saturated **iff** \(\sum g^2\asymp\sqrt p\) (Corollary 1.3).
   - **Upper bound:** \(\sum g^2\le(\tfrac12+o(1))\sqrt p\), and exactly \(\sum g^2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\) for the flat support \(S\) of \(\nu\). This uses the Round 20 gap theorem and the Round 151 flattening (Proposition 1.4).
   - So \(\sum g^2=o(\sqrt p)\) is **equivalent** to vanishing normalized additive energy of the near-critical support. That is the low-energy regime the ledger records as unresolved since Round 20. No accepted fact decides it, so the operator target is **not** relaxed through (b1‴).
2. **Part 2 (six-word types).**
   - Exact class decomposition (Proposition 2.1). Each quotient \(j j'^{-1}\) of a six-word is of type I (coinciding letters), S (common slope), P (common fixed point \(D/Y\)) or G (generic). The trace identity splits exactly over the \(4^3\) type patterns.
   - **The special classes are controlled at operator level** (Proposition 2.2):
     - \(\|\pi(\Delta_I+\Delta_S)\|=\max_{\eta\ne0}\sum_r|\hat\mu_r(\eta)|^2\le\sum_r m(r)^2=O(p^{34/23})\);
     - \(\|\pi(\Delta_I+\Delta_P)\|\le\sum_zL_z^2\le GM_1=O(p^{3/2})\).
     - Hence b1″ is **equivalent** to \(\|R\,\pi(\Delta_G)\,R\|=O(p^{3/2})\): the generic class alone.
   - **Exact model tables** at \(p\le677\) (sector-concentrated models; exact integers) show that the **dominant** class of \(\operatorname{tr}((R\pi\pi^*R)^3)\) is **IGG** (one coinciding pair, two generic quotients), then III, then GGG, whenever \(\sum g^2=G\). When \(\sum g^2=G/4\), the generic **GGG** leads instead. The random-like sector models (`rand`, `logint`, `interval`) give \(\operatorname{tr}(A^3)=0.15\)–\(0.27\,p^{9/2}\), which decreases in \(p\); the local growth is \(p^{4.21}\)–\(p^{4.25}\). Coset-union models are larger (up to \(2.4\,p^{9/2}\)), and their size tracks \(X\) and \(\mathcal E(\mu)\) (see the tables).
   - **The dominant class is a four-word quantity** (Propositions 2.3–2.4). Proved: if \(\operatorname{tr}(A^3)=O(p^{9/2})\) and \(\sum g^2\gg\sqrt p\), then the affine energy satisfies \(\mathcal E(\mu)=O(p^{5/2})\). The verified bound is \(\mathcal E(\mu)=O(p^{43/16})\), so the six-word criterion (b-k3) contains a \(p^{3/16}\) improvement of the affine energy. That improvement alone would already lower the one-match covariance to \(O(p^{7/4+o(1)})=O(p^{112/64+o(1)})\).
   - **Class-wise verified bounds:**

     | class | verified bound | needed |
     |---|---|---|
     | III | \(O(p^{4})\) | \(O(p^{144/32})\) |
     | IIX | \(O(p^{139/32})\) | \(O(p^{144/32})\) |
     | IXX (contains IGG) | \(O(p^{150/32})\) | \(O(p^{144/32})\) |
     | XXX (contains GGG) | \(O(p^{177/32})\) | \(O(p^{144/32})\) |

3. **Incidence input for the dominant class (conditional).** The accepted Round 178 point–plane inequality gives
   \[
   \mathcal E(\mu)\ll X M_1^2/p+X^{1/2}M_1^2+G\log p\,M_1^2,\qquad X=\sum_r m(r)^2 .
   \]
   So **\(X=O(p^{1+\varepsilon})\) implies \(\mathcal E(\mu)=O(p^{5/2+\varepsilon/2}+p^{5/2}\log p)\)**. This puts IXX at \(O(p^{9/2+\varepsilon/2}\log p)\) and the one-match covariance at \(O(p^{7/4+\varepsilon/4}\log^{1/2}p)\), which improves \(115/64\) iff \(\varepsilon<3/16\). The point–plane route cannot go below \(p^{5/2}\), because \(\sum_\xi W_\xi^{3/2}\ge M_1^3/\sqrt{p-1}\) and \(M_1\asymp p\). So \(p^{5/2}\) (up to \(\log p\)) is both its floor and exactly the necessary scale of Proposition 2.4.
4. **Candidate shared lemma.** The bound \(X=\sum_rm(r)^2=E_Q(h)=O(p^{1+\varepsilon})\) is the same estimate, at the same hypotheses, that the first-mass call needs: Round 182 accepted \(\mathcal M_w\le(E_Q(h)-\mathrm{diag})/4\), and \(\varepsilon\le1/1280\) gives \(\mathcal M_w=O(p^{1+1/1280})\). Here \(\varepsilon<3/16\) suffices for an improvement. The closeout should compare.

The rest of the report gives the arguments (proved, with hypotheses), the conditional criteria, the exact and floating evidence, and the gap.

## Setup and hypotheses

All objects are the accepted ones (Rounds 166, 169, 171, 173, 178, 180, 182); counting norms throughout.

- \(p\equiv1\pmod 4\) prime, \(n=(p-1)/2\), \(Q\) the squares, \(\chi\) the Legendre symbol, \(m_0=n/\sqrt p\).
- **Actual law.** \(b\ge0\) on \(\widehat Q\cong\mathbb Z/n\), \(b_0=0\), \(r=\mathbb Eb\), \(\nu=b/(nr)\) a probability on \(\widehat Q\). Put \(f(y)=\sum_j\nu_jj(y)\) on \(Q\), zero elsewhere (Rounds 151–153), and \(g=|f|^2\) (Round 166). Then \(0\le g\le1\) and \(g(1)=1\).
  - The law \(\omega\) on the \(p-1\) characters of \(\mathbb F_p^\times\) puts weight \(\lambda(\eta|_Q)/2\) on each lift \(\eta\), where \(\lambda=\nu*\check\nu\) (Round 166). Hence \(g=\sum_\alpha\omega(\alpha)\alpha\) on \(\mathbb F_p^\times\), and \(G=\sum g=(p-1)\omega(1)\) (Round 169).
  - \(m_{\rm eff}=1/\sum\nu_j^2\) (Rounds 20 and 151; equal to \(nr^2/\mathbb Eb^2\)). \(L=\max(1,m_{\rm eff}/m_0)\). \(\rho=-\sigma\) is the favorable sign.
- **(NC), the near-critical branch** (Rounds 151–154): \(\|L_\sigma b\|_{2,n}/r\to0\) and \(m_{\rm eff}/m_0\to1\), along the hypothetical sequence of eligible primes. All "\(o(1)\)" refer to this sequence. Statements marked (NC) assume it. Statements without the mark hold for any \(g\) with \(0\le g\le1\) on \(Q\).
- **Sectors.** \(T_\varepsilon=\{x\in Q\setminus\{1\}:\chi(1-x)=\varepsilon\}\) and \(G_\varepsilon=\sum_{T_\varepsilon}g\), so \(G=G_++G_-+1\).
- **Chart and operators** (Round 171, Round 182).
  - Chart: \(\mu(r,b)=g(Y)g(D)\) with \(r=(Y-D)/(1-D)\), \(b=D(1-Y)/(Y(1-D))\), \(Y\ne D\) in \(\mathbb F_p\setminus\{0,1\}\), and mask \(b\in Q\iff\chi(1-Y)=\chi(1-D)\). The map is \(j_{Y,D}(e)=re+b\), with fixed point \(D/Y\).
  - Masses: \(M_1=\sum\mu\), \(m(r)=\sum_b\mu(r,b)\), \(X=\sum_rm(r)^2\), \(c=\sum\mu^2\).
  - Operators: \(F=\sum_j\mu(j)U_j\), \(\pi\) its restriction to \(\mathbf 1^\perp\), \(\Delta(h)=\sum_{jj'^{-1}=h}\mu(j)\mu(j')\), so \(FF^*=\sum_h\Delta(h)U_h\). Energy \(\mathcal E(\mu)=\sum_h\Delta(h)^2=T_2\) (Round 182).
  - \(R\) deletes the outputs \(s=0,1\). \(A=R\pi\pi^*R\) acts on \(\ell^2(\mathbb F_p\setminus\{0,1\})\), and \(\sigma_R^2=\|A\|\).

## Part 1. The size of \(\sum g^2\)

### Proposition 1.1 (Parseval; exact, any law)
\[
 \sum_{x}g(x)^2=(p-1)\sum_\alpha\omega(\alpha)^2=n\,\mathcal E(\nu),\qquad
 G=n\sum_j\nu_j^2=\frac n{m_{\rm eff}} .
\]
Here \(\mathcal E(\nu)=\sum_{a+b=c+d}\nu_a\nu_b\nu_c\nu_d\) on \(\mathbb Z/n\).

*Proof.* \(g=\sum_\alpha\omega(\alpha)\alpha\) on \(\mathbb F_p^\times\), and \(g=0\) on the nonsquares; orthogonality on \(\mathbb F_p^\times\) gives the first equality. Also \(g=\sum_d\lambda_d\,d\) on \(Q\) with \(\lambda=\nu*\check\nu\). Orthogonality on \(Q\) gives \(\sum g^2=n\sum_d\lambda_d^2=n\,\mathcal E(\nu)\) and \(G=n\lambda_0=n\sum\nu^2\). \(\square\)

**Normalization correction.** The mission's \(\sum_\alpha\omega(\alpha)^2=2\sum g^2/(p-1)\) is off by a factor 2 for the full-character law of Rounds 166/169. Each square character has two lifts, each carrying half its weight, so \(\sum_\alpha\omega^2=\frac12\sum_d\lambda_d^2\). The asymptotic question is unaffected.

Hence \(\sum g^2=o(\sqrt p)\) is a statement about the **additive energy of the actual law \(\nu\)**, at the scale \(\mathcal E(\nu)=o(1/m_0)\). The trivial range is \(G^2/n\le\sum g^2\le G\), i.e. from \(O(1)\) to \(O(\sqrt p)\).

### Proposition 1.2 (sector concentration; (NC))
Assume \(b\ge0\), \(b_0=0\), \(\|L_\sigma b\|_{2,n}\le C\,r\) and \(L\le p^{1/12}\). Then
\[
 2G_{-\rho}+1\ \le\ C_1\,\frac{L\,G}{\sqrt p},\qquad C_1=C_1(C).
\]
Under (NC), therefore:
- (i) \(G_{-\rho}=O(1)\);
- (ii) \(G=(1+o(1))\sqrt p\);
- (iii) \(M_1=(1+o(1))\,p\);
- (iv) the Round 182 balance hypothesis \(G_{\min}\ge c_2G\) of \((\mathrm H_{\rm sat})\) is **false** for the actual law, since \(G_{\min}=G_{-\rho}=O(1)\).

*Proof.* Round 151 (accepted proof scope, item 3; `ordinary-prime-coset-spread-151.md`, "Application to the actual retargeted deficits") proves \(\langle b,(I-\rho K)b\rangle_{2,n}/\|b\|_{2,n}^2=O_C(L/\sqrt p)\). Its exact form is Round 152's \((2\|P_\sigma b\|^2+r^2)/\|b\|^2\). By the diagonalization of \(K\) stated there, this ratio is the relative integral of \((1-\rho\chi(1-x))|f(x)|^2\) over \(Q\). With \(\chi(0)=0\) at \(x=1\) the integrand is \(2g\) on \(T_{-\rho}\), \(0\) on \(T_\rho\) and \(g(1)=1\) at \(x=1\). Dividing by \(G\) gives the display.
- (i), (ii): \(G=n/m_{\rm eff}=\sqrt p\,m_0/m_{\rm eff}\), and \(m_{\rm eff}/m_0\to1\) under (NC). (Round 151 also proves \(m_{\rm eff}\ge(1-o(1))m_0\) on its block.) So \(LG/\sqrt p\to1\).
- (iii): the mask is \(\chi(1-Y)=\chi(1-D)\), so \(M_1=\sum_\varepsilon\bigl(G_\varepsilon^2-\sum_{T_\varepsilon}g^2\bigr)\). Hence \(G^2\ge M_1\ge(G-1-G_{-\rho})^2-G\). \(\square\)

**Consistency with Lemma S2 (Round 182).** On (NC), \(\rho\sum_xg(x)\chi(1-x)=G_\rho-G_{-\rho}=G-O(1)=(1+o(1))\sqrt p\). So the accepted bound \(|\sum g(x)\chi(1-x)|\le\sqrt p\) is asymptotically **tight** at the quadratic character. The actual law is extremal for that Jacobi-sum bound.

**Consequence for the Round 182 models.** Those four models were balanced (both sectors carried mass), so they violate (i) and have \(M_1\approx p/2\). The models of Part 2 below put \(g\) inside one sector \(T_\rho\), which gives \(M_1\approx p\).

### Corollary 1.3 (the \(s=1\) row needs no balance hypothesis)
Under (NC), with \(C_2\) from Proposition 1.2(i),
\[
 (1-o(1))\,p\,\Bigl(\sum g^2-C_2-2\Bigr)\ \le\ \|\pi(\mu)\|_{op}^2 .
\]
The \(s=1\) row itself has squared norm at most \(G^2\sum g^2\). Consequently b1′ is saturated (\(\|\pi(\mu)\|\gg p^{3/4}\)) **if and only if** \(\sum g^2\gg\sqrt p\). This replaces \((\mathrm H_{\rm sat})\): its balance part is false (Proposition 1.2(iv)) but superfluous.

*Proof.* Use Round 182 Proposition 4 (accepted): \(\|\pi\|^2\ge\sum_Yg(Y)^2n(Y)^2-M_1^2/p\) with \(n(Y)=G_{\chi(1-Y)}-g(Y)\) for \(Y\in Q\setminus\{1\}\). Restrict to \(Y\in T_\rho\), where \(n(Y)\ge G_\rho-1\), and use \(\sum_{T_\rho}g^2\ge\sum g^2-1-G_{-\rho}\). Then \(G_\rho=(1+o(1))\sqrt p\) and \(M_1^2/p=(1+o(1))p\). \(\square\)

### Proposition 1.4 (an upper bound, and an exact equivalent; (NC))
Under (NC), let \(S\) be the near-flat set of Round 151: \(|S|=(1+o(1))m_0\), and \(b_j^2/\sum b^2\to1_S/|S|\) in \(\ell^1\). Then
\[
 \frac{\sum g^2}{\sqrt p}=\frac{\mathcal E(S)}{|S|^3}+o(1),\qquad
 \limsup\frac{\sum g^2}{\sqrt p}\le\frac12 .
\]

*Proof.*
- **Setup.** Put \(\tilde\nu=\nu/\|\nu\|_2\) and \(e_S=1_S/\sqrt{|S|}\). Then \(\|\tilde\nu-e_S\|_2^2\le\sum_j|\tilde\nu_j^2-e_S(j)^2|\to0\), using \((a-b)^2\le|a^2-b^2|\) for \(a,b\ge0\).
- **The energy is a norm.** \(N(\eta)=\mathcal E(\eta)^{1/4}=n^{-1/4}\|\hat\eta\|_4\) is a norm. Moreover \(\mathcal E(\eta)\le\|\eta\|_2^2\|\eta\|_1^2\), since \(|\eta*\tilde\eta|\le\|\eta\|_2^2\) and \(\sum|\eta*\tilde\eta|\le\|\eta\|_1^2\). With \(\eta=\tilde\nu-e_S\) we have \(\|\eta\|_1\le\sqrt{m_{\rm eff}}+\sqrt{|S|}=O(\sqrt{m_0})\), so \(N(\eta)=o(m_0^{1/4})\). Also \(N(e_S)^4=\mathcal E(S)/|S|^2\in[|S|,|S|^2]\) is \(\asymp m_0\) up to the factor \(|S|\).
- **First claim.** \(\mathcal E(\tilde\nu)=\mathcal E(S)/|S|^2+o(m_0)\). By Proposition 1.1, \(\sum g^2=n\,\mathcal E(\tilde\nu)/m_{\rm eff}^2\). Since \(n/m_0=\sqrt p\) and \(m_{\rm eff},|S|\sim m_0\), this gives the first display.
- **Second claim: the Round 20 gap theorem.** Fix \(\tau\in(0,1)\) and \(\Delta>0\). The theorem (`anchored-repair-20.md`, "A uniform single-step gap for concentrated prime defects"; Round 20, inherited by Rounds 149/151/152; ledger line 205) applies to \(E=b\) on either sign. Its conclusion \(\|L_\sigma b\|\ge\epsilon\|b\|\) fails eventually under (NC), and \(m_{\rm eff}\le(1+\xi)m_0\) holds eventually. Therefore its energy hypothesis fails: the layer \(S_\tau=\{\tilde\nu_j\ge\tau/\sqrt{m_0}\}\) has \(\mathcal E(S_\tau)<(\frac12+\Delta)|S_\tau|^3\) eventually.
- **Comparing \(S\) and \(S_\tau\).** By the \(\ell^1\) convergence, \(|S\setminus S_\tau|\) and \(|S_\tau\setminus S|\) are \(o(m_0)\): each point of either difference costs at least \(\min(1-\tau^2,\tau^2)/|S|\) in \(\ell^1\). Hence
  \[
   \mathcal E(S)^{1/4}\le\mathcal E(S\cap S_\tau)^{1/4}+|S\setminus S_\tau|^{3/4}\le(\tfrac12+\Delta)^{1/4}|S_\tau|^{3/4}+o(m_0^{3/4}),
  \]
  and \(|S_\tau|\le(1+o(1))m_0\). Let \(\Delta\to0\). \(\square\)

**What this decides.**
- \(\sum g^2=o(\sqrt p)\) **iff** \(\mathcal E(S)=o(|S|^3)\) for the near-critical flat support. Round 20 excludes only \(\mathcal E(S)\ge(\frac12+\Delta)|S|^3\). The ledger (line 205) lists "the broad-support and low-energy prime regimes" as unresolved, and I found no accepted statement that forces either alternative.
- Equivalently, \(\sum g^2\asymp\sqrt p\) iff \(|f|\ge c\) on a set of size \(\asymp\sqrt p\) that carries a positive fraction of \(\|f\|_2^2\). Round 151 excludes such concentration only on bounded unions of multiplicative cosets of size \(\asymp\sqrt p\).
- **Status: open.** Proven range on (NC): \(1\le\sum g^2\le(\frac12+o(1))\sqrt p\).
- **(b1‴) is not relaxed by a power.** The bound \(\frac12\) improves (b1‴) and Corollary 1.3 only by a constant. The proof plan of b1″ is unchanged: the target remains \(\sigma_R=O(p^{3/4})\) whenever the energy of \(S\) does not vanish.
- Also \(c=\sum\mu^2=\sum_\varepsilon\bigl[(\sum_{T_\varepsilon}g^2)^2-\sum_{T_\varepsilon}g^4\bigr]\). So \(c\le(\sum g^2)^2\le(\frac14+o(1))p\), and \(c\ge(\sum g^2-C_2-1)^2-\sum g^2\).

## Part 2. The row-deleted cubic trace by six-word type

### Proposition 2.1 (exact class decomposition; any \(g\ge0\))
For an ordered pair of letters \(j,j'\in\operatorname{supp}\mu\), the type of the quotient \(jj'^{-1}\) is:
- **I** if \(j=j'\);
- **S** if \(\operatorname{slope}(j)=\operatorname{slope}(j')\) and \(j\ne j'\) (a nonzero translation);
- **P** if \(\operatorname{fix}(j)=\operatorname{fix}(j')\) and \(j\ne j'\) (a dilation about the common fixed point \(D/Y\));
- **G** otherwise.

S and P are disjoint, since slope and fixed point determine an affine map. Write \(\Delta=\Delta_I+\Delta_S+\Delta_P+\Delta_G\) accordingly. With \(\mu_r=\mu1_{\{\text{slope }r\}}\) and \(\mu_z=\mu1_{\{\text{fix}=z\}}\),
\[
 \Delta_I+\Delta_S=\sum_r\mu_r*\tilde\mu_r,\qquad \Delta_I+\Delta_P=\sum_z\mu_z*\tilde\mu_z,\qquad \pi(\Delta_I)=c\,P_{\mathbf 1^\perp}.
\]
For every \(k\),
\[
 \operatorname{tr}\bigl((\pi\pi^*)^k\bigr)=\sum_{\tau\in\{I,S,P,G\}^k}\ \sum_{\substack{h_i\in\text{type }\tau_i}}\prod_i\Delta_{\tau_i}(h_i)\,\bigl(p\,[h_1\cdots h_k=\mathrm{id}]-[\operatorname{slope}(h_1\cdots h_k)=1]\bigr).
\]
The row-deleted \(\operatorname{tr}(A^k)\) splits over the same patterns, with \(R\) inserted between the factors \(\pi(\Delta_{\tau_i})\).

*Proof.* Linearity of \(\pi\). On \(\mathbf 1^\perp\), \(\operatorname{tr}\pi(U_h)=\#\mathrm{Fix}(h)-1=p[h=\mathrm{id}]-[\operatorname{slope}h=1]\) (Round 182 Proposition 2). \(\square\)

Exact check: `paley-183-rowdel-trace.py --check` verifies at \(p=29,37,41\) (two random integer \(g\) each) that \(\sum_\tau M_\tau=KK^T\); that the full total equals \(pT_3-T_3^\times(m)\), computed independently by the Round 182 group convolutions; that sampled pattern values equal the typed-word formula; and that the row-deleted total equals a direct rational computation.

### Proposition 2.2 (the special classes are bounded in operator norm; any \(0\le g\le1\))
1. \(\pi(\Delta_I+\Delta_S)\) is diagonal in the additive Fourier basis \(\{e_\eta\}_{\eta\ne0}\) of \(\mathbf 1^\perp\). Its entries are \(\sum_r|\hat\mu_r(\eta)|^2\), where \(\hat\mu_r(\eta)=\sum_b\mu(r,b)e_p(-\eta b)\). Hence
\[
 0\le\pi(\Delta_I+\Delta_S),\qquad \|\pi(\Delta_I+\Delta_S)\|=\max_{\eta\ne0}\sum_r|\hat\mu_r(\eta)|^2\le X=\sum_rm(r)^2=O(p^{34/23}).
\]
2. \(0\le\pi(\Delta_I+\Delta_P)=\sum_z\pi(\mu_z)\pi(\mu_z)^*\), and
\[
 \max_zL_z^2\le\|\pi(\Delta_I+\Delta_P)\|\le\sum_zL_z^2\le G\,M_1=O(p^{3/2}),
\]
where \(L_z=\sum_{\operatorname{fix}j=z}\mu(j)\le G\).
3. Consequently \(\bigl|\,\|A\|-\|R\,\pi(\Delta_G)\,R\|\,\bigr|\le X+\sum_zL_z^2+c=O(p^{3/2})\). So
\[
 \textbf{b1″}\iff\|R\,\pi(\Delta_G)\,R\|=O(p^{3/2}),
\]
and likewise b1′ \(\iff\|\pi(\Delta_G)\|=O(p^{3/2})\). Only the generic class (distinct slopes **and** distinct fixed points in each quotient) is open.

*Proof.*
- **Part 1.** \((U_{(r,b)}e_\eta)(s)=e_\eta((s-b)/r)\). So \(\pi(\mu_r)e_\eta=\hat\mu_r(\eta/r)\,e_{\eta/r}\) and \(\pi(\mu_r)\pi(\mu_r)^*e_\theta=|\hat\mu_r(\theta)|^2e_\theta\). Also \(|\hat\mu_r|\le m(r)\). The bound \(X=O(p^{34/23})\) is Round 182 (accepted: "the squared \(r\)-row mass is \(O(p^{34/23})\)", \(X=E_Q(h)\) by the audit's §4). Trivially \(X\le\max_rm(r)\,M_1\le GM_1\), since the unmasked row is at most \(G\) (Round 180).
- **Part 2.** \(\|\pi(\mu_z)\|\le\|\mu_z\|_1=L_z\). For the lower bound, \(v_z=\mathbf 1-p\delta_z\in\mathbf 1^\perp\) is fixed by every map fixing \(z\), so \(\pi(\mu_z)^*v_z=L_zv_z\). Finally \(L_z\le\sum_Yg(Y)\max g\le G\) and \(\sum_zL_z=M_1\).
- **Part 3.** \(\pi\pi^*=\pi(\Delta_I+\Delta_S)+\pi(\Delta_I+\Delta_P)-cP+\pi(\Delta_G)\); compress by \(R\). \(\square\)

**Remark.** \(\sum_zL_z^2\) is, up to the mask and the diagonal \(Y=D\), the multiplicative energy of \(g\). Part 2 shows that the common-fixed-point class costs exactly the largest multiplicative autocorrelation squared, \(\max_zL_z^2\le G^2\). The common-slope class costs at most the squared slope-row mass \(X\).

### Proposition 2.3 (class-wise verified bounds for \(\operatorname{tr}(A^3)\); any \(0\le g\le1\))
Write \(A=c\,RPR+Z\) with \(Z=R\,\pi(\Delta_S+\Delta_P+\Delta_G)R\). Then
\[
 \operatorname{tr}(A^3)=\underbrace{c^3\operatorname{tr}((RPR)^3)}_{\rm III}+\underbrace{3c^2\operatorname{tr}((RPR)^2Z)}_{\rm IIX}+\underbrace{3c\operatorname{tr}(RPR\,Z^2)}_{\rm IXX}+\underbrace{\operatorname{tr}(Z^3)}_{\rm XXX}.
\]
In the pattern language, III is the pattern III, IIX has exactly two I's, IXX exactly one I, and XXX none. With \(\|\pi(\Delta_{\ne})\|_{HS}^2\le p(\mathcal E(\mu)-c^2)\), \(c\le M_1\le G^2\), and the accepted \(\mathcal E(\mu)=O(p^{43/16})\) (Round 180):

| class | bound | verified exponent | needed |
|---|---|---|---|
| III | \(c^3(p-2)\) | \(4=128/32\) | \(144/32\) |
| IIX | \(3c^2\sqrt p\,(p\,\mathcal E)^{1/2}\) | \(139/32\) | \(144/32\) |
| IXX | \(0\le\cdot\le3c\,p\,(\mathcal E(\mu)-c^2)\) | \(150/32\) | \(144/32\) |
| XXX | \(\|Z\|\,p\,\mathcal E\le((p\mathcal E)^{1/2}+c)\,p\,\mathcal E\) | \(177/32\) | \(144/32\) |

*Proof.*
- \(RPR\) has eigenvalues 1 (multiplicity \(p-3\)) and \(2/p\), so \(0\le RPR\le I\).
- \(\operatorname{tr}(Z^2)\le\|\pi(\Delta_{\ne})\|_{HS}^2=p\sum_h\Delta_{\ne}(h)^2-\sum_a(\cdot)^2\le p(\mathcal E(\mu)-c^2)\). This is the Hilbert–Schmidt identity of Round 182 applied to the measure \(\Delta_{\ne}=\Delta-c\delta_{\mathrm{id}}\).
- \(\|Z\|\le\|A\|+c\le\operatorname{tr}((\pi\pi^*)^2)^{1/2}+c\).
- The rest is Cauchy–Schwarz and Hölder for traces. \(\square\)

The XXX bound is the Round 182 \(177/32\). The new information is that the **IXX** class, which dominates every model (tables below), is a four-word quantity verified at \(150/32\).

### Proposition 2.4 (the six-word criterion contains a four-word statement; proved)
For every \(c_0\ge0\), and with \(\bar a=\operatorname{tr}(A)/(p-2)\),
\[
 \operatorname{tr}(A^3)\ \ge\ c_0\,\|A-c_0I\|_{HS}^2-(p-2)c_0^3,\qquad
 \mathcal E(\mu)\ \le\ 8c^2+\frac{\operatorname{tr}(A^3)}{p\,\bar a}+\frac{4G^7+E^\times(m)}{p}.
\]
Consequently:
- If \(\operatorname{tr}(A^3)\le Cp^{9/2}\) and \(\bar a\ge\kappa p\), then \(\mathcal E(\mu)=O_{C,\kappa}(p^{5/2})\).
- Under (NC), \(\bar a\ge c-O(p^{1/2})\) and \(c\ge(\sum g^2-C_2-1)^2-\sum g^2\). So \(\bar a\ge\kappa p\) whenever \(\sum g^2\ge\kappa'\sqrt p\), i.e. exactly in the saturated case of Corollary 1.3.

*Proof.*
- **Scalar inequality.** For \(z\ge0\), \(z^3-c_0(z-c_0)^2+c_0^3=z(z^2-c_0z+2c_0^2)\ge0\). Apply it to the eigenvalues \(a_i\ge0\) of \(A\).
- **Variance.** Take \(c_0=\bar a\): \(\sum(a_i-\bar a)^2\le\operatorname{tr}(A^3)/\bar a+(p-2)\bar a^2\), so \(\operatorname{tr}(A^2)\le2(p-2)\bar a^2+\operatorname{tr}(A^3)/\bar a\).
- **Mean eigenvalue.** \(\bar a\le\|\pi\|_{HS}^2/(p-2)\le pc/(p-2)\le2c\).
- **Rows 0 and 1.** Let \(\tilde A=P FF^*P\) on \(\mathbb C^p\). Then \(\operatorname{tr}((\pi\pi^*)^2)=\|\tilde A\|_{HS}^2\le\|A\|_{HS}^2+2\sum_{s\in\{0,1\}}\|\tilde Ae_s\|^2\), and \(\|\tilde Ae_s\|^2\le\|F\|^2\|K(s,\cdot)\|^2\le M_1^2\cdot GM_1\le G^7\). This uses the Schur bound \(\|F\|\le M_1\) and Round 182 Proposition 3(vi).
- **Energy.** By the trace identity, \(p\,\mathcal E(\mu)=\operatorname{tr}((\pi\pi^*)^2)+E^\times(m)\).
- **Lower bound on \(\bar a\).** \(\|R\pi\|_{HS}^2\ge\|\pi\|_{HS}^2-2GM_1=pc-X-2GM_1\), so \(\bar a\ge c-O(p^{1/2})\). For \(c\), use Part 1.
- **Size of the error terms.** \(E^\times(m)\le M_1^2X=O(p^{7/2})\) and \(G^7=O(p^{7/2})\). \(\square\)

**Reading.**
- In the saturated case, the six-word criterion (b-k3) implies \(\mathcal E(\mu)=O(p^{5/2})\). That is a \(p^{3/16}\) improvement of the accepted affine energy.
- By itself, that energy bound would already give \(\sigma_R^2\le\|\pi\|^2\le(p\,\mathcal E)^{1/2}=O(p^{7/4})\), hence a one-match covariance \(O(p^{7/4})=O(p^{112/64})\) through Round 182 Proposition 5. That beats the accepted \(115/64\).
- So (b-k3) is strictly stronger than an unproved statement that would already improve the headline exponent.
- The variance form is also natural. (b-k3) forces the spectrum of \(A\) to cluster at its mean \(\bar a\asymp p\) to within \(\sum(a_i-\bar a)^2=O(p^{7/2})\); the floor of that variance is \(\asymp p^3\) in all models.

### Proposition 2.5 (incidence input for the dominant class; conditional on \(X\))
The accepted Round 178 point–plane estimate (Petridis–Roche-Newton–Rudnev–Warren, Lemmas 3.1–3.2 and (9), with the weighted layer cake of Round 178) is
\[
 \mathcal E(\mu)\ll\sum_\xi\Bigl(\frac{W_\xi^2}p+W_\xi^{3/2}+G(1+\log p)W_\xi\Bigr)+p,\qquad W_\xi=\sum_rm(r)m(\xi/r)\le X,\quad \sum_\xi W_\xi=M_1^2 .
\]
Hence, for any \(0\le g\le1\),
\[
 \mathcal E(\mu)\ \ll\ \frac{X M_1^2}{p}+X^{1/2}M_1^2+G\log p\,M_1^2 .
\]
Its hypotheses are those of Round 178: the actual chart, weighted line multiplicities at most \(2G\) in both charts, weights cut at \(p^{-2}\), and Theorem (9) applied with the smaller set as points.

Consequences:
- (2.5a) If \(X=O(p^{1+\varepsilon})\), then \(\mathcal E(\mu)=O(p^{5/2+\varepsilon/2}+p^{5/2}\log p)\). This gives IXX \(=O(p^{9/2+\varepsilon/2}\log p)\) and IIX \(=O(p^{17/4+\varepsilon/4})\). It also gives a one-match covariance of \(O(p^{7/4+\varepsilon/4}\log^{1/2}p)\), which improves the accepted \(115/64\) iff \(\varepsilon<3/16\).
- (2.5b) **Floor of this route.** Hölder gives \(\sum_\xi W_\xi^{3/2}\ge M_1^3/\sqrt{p-1}\) (Round 182 Proposition 6). With \(M_1=(1+o(1))p\) (Proposition 1.2), the point–plane route cannot give \(\mathcal E(\mu)\) below \(\asymp p^{5/2}\). That floor coincides with the necessary scale of Proposition 2.4. Its third term is already \(p^{5/2}\log p\). So on (NC) the point–plane route can meet the IXX requirement at best up to a factor \(\log p\), with no room, and only if \(X=O(p)\).
- (2.5c) **XXX (GGG) is not touched.** No incidence statement that I know controls \(\operatorname{tr}((R\pi(\Delta_G)R)^3)\) below the trivial \(\|Z\|\operatorname{tr}Z^2\). Point–line theorems over \(\mathbb F_p\), such as Stevens–de Zeeuw Theorem 4 (Cartesian products, \(an\ll p^2\)), Vinh's spectral bound and PRNRW Theorem 2.1, control four-word energies (\(k=2\)).
  - The "conics" of Round 182 Proposition 3(v) are the point–line incidences \(s=rx+b\) between the points \((x,s)\in\mathbb F_p^2\) and the lines \(j\), written in the \((Y,D)\) chart. So a point–conic theorem for the fibres is a point–line theorem for the dual configuration.
  - In that configuration, \(\operatorname{tr}((KK^T)^3)\) counts closed six-chains point–line–point–line–point–line. Bounding its translation discrepancy needs a hexagon count in \(\mathbb F_p^2\) with \(M_1\asymp p\) weighted lines. I found no theorem with hypotheses met here that gives the needed \(p^{-1/2}\) relative cancellation.

### Candidate shared lemma (for the closeout)
\[
 \textbf{(SL)}\qquad X=\sum_rm(r)^2=E_Q(h)=O(p^{1+\varepsilon}),
\]
with the actual \(\mu\) and \(h(z)=g(1-z)\) as in Round 182. Its uses:
- First mass: Round 182 accepted \(\mathcal M_w\le(E_Q(h)-\mathrm{diag})/4\), so \(\varepsilon=1/1280\) gives \(\mathcal M_w=O(p^{1+1/1280})\), the first-mass target.
- This call: (2.5a), where any \(\varepsilon<3/16\) improves the one-match exponent and \(\varepsilon\to0\) brings the dominant IXX class to \(p^{9/2+o(1)}\).

The estimate, the object and the hypotheses are the same; the scales differ (\(\varepsilon\le1/1280\) there, \(\varepsilon<3/16\) here). This corrects the Round 182 audit's §4 observation for the present use: there \(X\) entered report 1 only as a subtracted term. Here it enters as an **upper** bound for \(W_\xi\) inside \(\mathcal E(\mu)\).

Accepted state: \(X=O(p^{34/23})\) (Round 182). The Round 182 BSG-plus-Young scheme is capped at \(p^{4/3}\), which is above \(19/16\), so that scheme cannot deliver \(\varepsilon<3/16\). Models: \(X/p\approx2.2\)–\(3\) (tables below).

## Evidence (c): exact traces in auxiliary models, \(p\le677\)

**These are not the actual optimiser.**

**Models.** All are 0/1 weights \(g=1_B\) with \(|B|\approx\sqrt p\), except `spread4`.
- Sector models (Proposition 1.2): \(B\subset T_\rho\) for both \(\rho=\pm1\).
  - `rand`: a random subset of \(T_\rho\).
  - `logint`: \(\{\theta^{2k}\}\cap T_\rho\), with \(\theta\) a primitive root.
  - `interval`: the first \(\lfloor\sqrt p\rceil\) elements of \(T_\rho\) in \([2,p)\).
  - `coset`: whole cosets of the subgroup of \(Q\) of order closest to \(\sqrt p\), intersected with \(T_\rho\), added until \(|B|\ge\sqrt p\). Its size overshoots: \(|B|=35\) at \(p=677\), \(\rho=+1\).
- Other models:
  - `spread4`: \(4\sqrt p\) points of \(T_\rho\) with weight \(1/4\), so \(\sum g^2=G/4\).
  - `randQ`: the balanced Round 182-type control; it violates Proposition 1.2.

All trace columns are exact rationals (printed as floats). \(\sigma_R\) and the class norms are floating `eigvalsh` values.

Full output: `.venv/bin/python -B research/paley-183-rowdel-trace.py P` for each \(P\in\{101,197,293,401,509,577,677\}\). The run takes 0.7 s to 193 s per prime, about 8 minutes in all, with a peak of 388 MB at \(p=677\). Selected lines are below. The class columns are values divided by \(p^{9/2}\), with \(A=R\pi\pi^*R\).

`rand`, \(\rho=+1\), all \(p\):

| p | tr\(A^3\)/\(p^{4.5}\) | IGG | III | GGG | IIG | \(\mathcal E(\mu)/p^2\) | \(X/p\) | var\(_R/p^{3.5}\) | \(\|R\pi(\Delta_G)R\|/p^{1.5}\) | \(\sigma_R/\sqrt p\) |
|---|---|---|---|---|---|---|---|---|---|---|
| 101 | 0.2699 | +0.1711 | +0.0683 | +0.0410 | −0.0148 | 2.624 | 2.238 | 0.0659 | 0.2352 | 1.825 |
| 197 | 0.2198 | +0.1408 | +0.0553 | +0.0321 | −0.0095 | 2.983 | 2.386 | 0.0514 | 0.1605 | 1.788 |
| 293 | 0.1976 | +0.1238 | +0.0463 | +0.0329 | −0.0067 | 3.077 | 2.730 | 0.0450 | 0.1423 | 1.840 |
| 401 | 0.1796 | +0.1125 | +0.0422 | +0.0293 | −0.0054 | 3.258 | 2.653 | 0.0400 | 0.1277 | 1.875 |
| 509 | 0.1895 | +0.1182 | +0.0433 | +0.0326 | −0.0052 | 3.744 | 2.778 | 0.0399 | 0.1273 | 1.969 |
| 577 | 0.1621 | +0.1005 | +0.0363 | +0.0288 | −0.0040 | 3.384 | 2.683 | 0.0352 | 0.1138 | 1.924 |
| 677 | 0.1529 | +0.0947 | +0.0339 | +0.0273 | −0.0035 | 3.428 | 2.520 | 0.0330 | 0.1053 | 1.926 |

All models at \(p=677\):

| model, \(\rho\) | \(G\) | \(M_1/p\) | tr\(A^3\)/\(p^{4.5}\) | IGG | III | GGG | \(\mathcal E(\mu)/p^2\) | \(X/p\) | \(\sigma_R/\sqrt p\) |
|---|---|---|---|---|---|---|---|---|---|
| rand +1 | 26 | 0.960 | 0.1529 | +0.0947 | +0.0339 | +0.0273 | 3.43 | 2.52 | 1.926 |
| rand −1 | 26 | 0.960 | 0.1526 | +0.0945 | +0.0339 | +0.0272 | 3.42 | 2.51 | 1.941 |
| logint +1 | 26 | 0.960 | 0.1541 | +0.0939 | +0.0339 | +0.0267 | 3.45 | 2.57 | 1.943 |
| logint −1 | 26 | 0.960 | 0.1528 | +0.0936 | +0.0339 | +0.0266 | 3.43 | 2.48 | 1.920 |
| interval +1 | 26 | 0.960 | 0.1502 | +0.0933 | +0.0339 | +0.0261 | 3.41 | 2.67 | 1.923 |
| interval −1 | 26 | 0.960 | 0.1515 | +0.0938 | +0.0339 | +0.0267 | 3.42 | 2.79 | 1.931 |
| coset +1 | 35 | 1.758 | 0.9286 | +0.5745 | +0.2078 | +0.1670 | 20.42 | 8.11 | 2.702 |
| coset −1 | 29 | 1.199 | 0.2982 | +0.1813 | +0.0660 | +0.0508 | 6.45 | 3.85 | 2.168 |
| spread4 ±1 | 26 | 0.989 | 0.0001–0.0002 | ≈0 | ≈0 | +0.0001 | 1.01 | 2.00 | 1.03–1.07 |
| randQ (balanced) | 26 | 0.508 | 0.0240 | +0.0146 | +0.0050 | +0.0046 | 0.65 | 0.94 | 1.418 |

Reading (floating evidence about models only):
- **Dominant type.** In every model with \(\sum g^2=G\) (all 0/1 models, at every prime), the row-deleted cubic trace is led by **IGG**: one coinciding pair and two generic quotients. In `spread4` (\(\sum g^2=G/4\)) the order changes: **GGG** leads, because the I-containing classes carry powers of \(c\approx(\sum g^2)^2\). So the blocking type depends on Part 1. If \(\sum g^2\asymp\sqrt p\), IGG blocks, and it is a four-word quantity; if \(\sum g^2\) is small, the genuinely six-word GGG blocks. In sector models it is about 62% of the total; III is about 22%, GGG about 18%, and IIG is slightly negative. Each pattern class containing S or P is at most \(0.0071\,p^{9/2}\) in absolute value in the random-like sector models (the maximum is IPP, `logint +1`, \(p=101\)), and at most \(0.0004\,p^{9/2}\) at \(p=677\).
- For the **full** operator the order flips. GGG leads (for example \(0.73\,p^{9/2}\) of the \(0.95\,p^{9/2}\) total for `rand +1` at \(p=677\)), because the \(s=1\) row lives in the generic class: \(\|\pi(\Delta_G)\|=0.89\,p^{3/2}\) against \(\|R\pi(\Delta_G)R\|=0.105\,p^{3/2}\).
- **No power excess.** Local growth of tr\((A^3)\) from \(p=101\) to \(677\) is \(p^{4.21}\) (`rand +1`, `logint +1`, `interval +1`) to \(p^{4.25}\) (`rand −1`), i.e. below \(p^{9/2}\) and decreasing in \(p^{9/2}\) units. \(\|R\pi(\Delta_G)R\|\) grows like \(p^{1.08}\), and the spectral variance var\(_R\) like \(p^{3.14}\). \(\sigma_R\approx1.8\)–\(1.97\sqrt p\), larger than Round 182's balanced models (\(1.3\)–\(1.9\sqrt p\)) because \(M_1\) doubles.
- **Coset-union models** are larger, with values set by the coset arithmetic of \(n\). They overshoot \(|B|\), with \(G\) up to \(1.35\sqrt p\). Their size tracks \(X\) and \(\mathcal E(\mu)\) exactly as Proposition 2.5 predicts: at \(p=677\), \(\rho=+1\), \(X=8.1p\), \(\mathcal E=20p^2\), and the total is \(0.93p^{9/2}\). These are the configurations where (SL) is tight, and the excess sits in IGG as predicted.
- **`spread4`.** With \(\sum g^2=G/4\) the trace collapses: \(c=\sum\mu^2\) shrinks by a factor of about 16, from 650 to 41.8 at \(p=677\), while \(M_1\) and \(G\) are unchanged. This matches (b1‴) and Proposition 2.3, whose III/IIX/IXX bounds carry powers of \(c\).
- \(\mathcal E(\mu)/p^2\approx2.6\)–\(3.4\) and \(X/p\approx2.2\)–\(2.9\) in the random-like sector models. These are far below the scales \(p^{5/2}\) and \(p^{1+\varepsilon}\) that the proofs need, so the models are consistent with (SL) at \(\varepsilon=o(1)\).
- **Finite models do not settle the asymptotic target and are not evidence about the actual \(g\).** The actual \(g\) has a flat Fourier law and sector concentration together. No 0/1 model here has the first property.

**Exact checks** (`--check`, about 3 s):
```
p=29 seed=0: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK
p=29 seed=1: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK
p=37 seed=0: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK
p=37 seed=1: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK
p=41 seed=0: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK
p=41 seed=1: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK
all exact checks passed
```
These are finite exact checks of identities that are proved above for all \(p\).

## Proved (a) / conditional (b) / evidence (c)

**Proved (a).** Inherited chart and normalizations; hypotheses as stated.
- (a1) \(\sum g^2=(p-1)\sum\omega^2=n\,\mathcal E(\nu)\) and \(G=n/m_{\rm eff}\), for any law. This corrects the mission's factor 2. (Proposition 1.1.)
- (a2) Under (NC):
  - \(G_{-\rho}=O(1)\), \(G=(1+o(1))\sqrt p\), \(M_1=(1+o(1))p\);
  - the balance part of \((\mathrm H_{\rm sat})\) is false;
  - Lemma S2 is asymptotically tight at \(\chi\).

  Inputs: Round 151's sector estimate and \(m_{\rm eff}\sim m_0\). (Proposition 1.2.)
- (a3) Under (NC), \(\|\pi(\mu)\|^2\ge(1-o(1))p(\sum g^2-C)\), so b1′ is saturated iff \(\sum g^2\asymp\sqrt p\). (Corollary 1.3.)
- (a4) Under (NC), \(\sum g^2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\le\frac12+o(1)\). Inputs: the Round 20 gap theorem and the Round 151 flattening. (Proposition 1.4.)
- (a5) The exact four-type split of every \(\operatorname{tr}((\pi\pi^*)^k)\) and of the row-deleted traces. (Proposition 2.1.)
- (a6) For any \(0\le g\le1\):
  - \(\|\pi(\Delta_I+\Delta_S)\|=\max_\eta\sum_r|\hat\mu_r(\eta)|^2\le X\);
  - \(\max L_z^2\le\|\pi(\Delta_I+\Delta_P)\|\le\sum_zL_z^2\le GM_1\);
  - hence b1″ \(\iff\|R\pi(\Delta_G)R\|=O(p^{3/2})\).

  (Proposition 2.2.)
- (a7) Class-wise verified bounds for \(\operatorname{tr}(A^3)\): III \(p^{4}\), IIX \(p^{139/32}\), IXX \(p^{150/32}\), XXX \(p^{177/32}\). (Proposition 2.3.)
- (a8) \(\operatorname{tr}(A^3)\ge c_0\|A-c_0\|_{HS}^2-(p-2)c_0^3\). Hence (b-k3) with \(\bar a\gg p\) implies \(\mathcal E(\mu)=O(p^{5/2})\). Under (NC), \(\bar a\gg p\) holds iff \(\sum g^2\gg\sqrt p\). (Proposition 2.4.)
- (a9) \(\mathcal E(\mu)\ll XM_1^2/p+X^{1/2}M_1^2+G\log p\,M_1^2\), from the accepted Round 178 inequality. Method floor of the point–plane route: \(p^{5/2}\) when \(M_1\asymp p\). (Proposition 2.5.)

**Conditional (b).**
- (b1) (SL) \(X=O(p^{1+\varepsilon})\) implies \(\mathcal E(\mu)=O(p^{5/2+\varepsilon/2}+p^{5/2}\log p)\). That gives:
  - IXX \(=O(p^{9/2+\varepsilon/2}\log p)\);
  - one-match covariance \(O(p^{7/4+\varepsilon/4}\log^{1/2}p)\), an improvement of \(115/64\) iff \(\varepsilon<3/16\);
  - with \(\varepsilon\le1/1280\), the first-mass target \(\mathcal M_w=O(p^{1+1/1280})\) (Round 182 row-pair formula).
- (b2) b1″ \(\iff\) \(\|R\pi(\Delta_G)R\|=O(p^{3/2})\). Equivalently, (b-k3) restricted to the generic class plus (b1).
- (b3) \(\sum g^2=O(p^{1/2-\delta})\iff\mathcal E(S)=O(|S|^3p^{-\delta})\). Either relaxes (b1‴) by \(p^{\delta/2}\) and lowers \(c\) by \(p^{-2\delta}\), which relaxes the IXX requirement on \(\mathcal E(\mu)\) to \(O(p^{5/2+2\delta})\).

**Evidence (c).** Exact traces in the models above (0/1 and \(1/4\)-weight sector models, coset unions, a balanced control); floating spectral norms. Dominant type: IGG. Growth \(p^{4.21}\)–\(p^{4.25}\) for tr\((A^3)\) in the random-like sector models.

## Exact remaining gap

1. **One-match covariance.** Target \(O(p^{3/2})\); accepted \(O(p^{115/64})\), unchanged. Via b1″ this is equivalent, up to \(O(p^{3/2})\) in \(\|A\|\), to
   \[
     \|R\,\pi(\Delta_G)\,R\|_{op}=O(p^{3/2}),
   \]
   where \(\Delta_G(h)\) sums \(\mu(j)\mu(j')\) over the pairs \(jj'^{-1}=h\) with distinct slopes and distinct fixed points.
2. **Six-word route (b-k3).** It splits into two parts.
   - A four-word part, which is necessary: \(\mathcal E(\mu)=O(p^{5/2})\) when \(\sum g^2\asymp\sqrt p\). It is verified at \(O(p^{43/16})\), a gap of \(p^{3/16}\). It would follow up to \(p^{o(1)}\) from (SL) with \(\varepsilon=o(1)\) by the point–plane route, and that route cannot do better than \(p^{5/2}\log p\).
   - A genuinely six-word generic part: XXX/GGG, verified \(O(p^{177/32})\) against the needed \(O(p^{144/32})\). No incidence input is known.
3. **\(\sum g^2\).** Open. It is equivalent to the normalized additive energy \(\mathcal E(S)/|S|^3\) of the near-critical flat support; the proven range is \([o(1),\frac12+o(1)]\cdot\sqrt p\).
4. **Unchanged.** The zero-match estimate, the generic J sum \(O(p^{9/4})\), the first mass \(O(p^{11/8})\) and the cold route are not addressed.

**What would change the proof plan.**
- (SL) with \(\varepsilon<3/16\) improves the one-match exponent through \(k=2\) alone. With \(\varepsilon\le1/1280\) it also closes the first mass.
- A proof that \(\mathcal E(S)=o(|S|^3)\) on (NC) would make the \(s=1\) row negligible and relax every operator target.
- Conversely, a near-critical configuration with \(\mathcal E(S)\asymp|S|^3\) would make b1′ exactly critical. Proposition 1.4 caps such a configuration at energy \(\le\frac12|S|^3\).

## Ranked next tests

1. **(SL): \(\sum_rm(r)^2=E_Q(h)=O(p^{1+\varepsilon})\)** for the actual \(h(z)=g(1-z)\), shared with the first-mass route. Use the sector concentration (Proposition 1.2): \(h\) lives on \(\{\chi(z)=\rho,\chi(1-z)=1\}\). Also use the tightness of Lemma S2 at \(\chi\) and the flat Fourier law of \(g\). The Round 182 BSG-plus-Young scheme is capped at \(p^{4/3}\), so a different input is needed, for example a large-values estimate for \(\hat h(\psi)=\sum_\alpha\omega(\alpha)J(\alpha,\psi)\) over \(\psi\). Success at \(\varepsilon<3/16\) improves \(115/64\).
2. **The generic six-word class.** Bound \(\operatorname{tr}((R\pi(\Delta_G)R)^3)\), or the fourth moment \(\operatorname{tr}((R\pi(\Delta_G)R)^4)\) (eight words, floor \(\asymp p^5\), need \(p^6\)), using that both letters of every quotient have distinct slopes and distinct fixed points.
3. **Energy of the near-critical support.** Decide \(\mathcal E(S)/|S|^3\to0\) on (NC), extending the Round 20 gap below energy \(\frac12|S|^3\). This would relax every operator target through (b3).

## Replay

```
.venv/bin/python -B research/paley-183-rowdel-trace.py --check        # exact identities, ~3 s
.venv/bin/python -B research/paley-183-rowdel-trace.py 101 197 293 401 509 577 677
                                                                     # models; ~8 min sequential, 388 MB peak
```
Script SHA-256 for the quoted output: `cfccf71b7629ab7f05a52f54c3256646ec5407e0a532fe1fa1dfba050561e6ee`. Requires numpy (tested with 2.3.5). The model sampler is seeded deterministically from \((p,\rho,\text{model})\). The `--check` mode imports `research/paley-182-opnorm-identities.py` for the independent group-convolution computation.

## Verdict

**Inconclusive** (mission definition).
- **Part 1:** \(\sum g^2\) is not decided. It equals \(\sqrt p\,(\mathcal E(S)/|S|^3+o(1))\le(\frac12+o(1))\sqrt p\) on (NC). The square-class balance fails, but that is harmless.
- **Part 2:** the exact six-word type is **IGG**. It dominates every model with \(\sum g^2\asymp\sqrt p\) (GGG leads when \(\sum g^2=G/4\)) and sits in the class IXX, verified at \(O(p^{150/32})\) against the needed \(O(p^{144/32})\); its input is the four-word energy \(\mathcal E(\mu)=O(p^{5/2})\), equivalently (SL) up to \(p^{o(1)}\). The genuinely six-word generic class GGG/XXX stays at the verified \(O(p^{177/32})\).
- No word type exceeds \(p^{9/2}\) by a power in any model; the random-like sector models grow like \(p^{4.2}\). So there is no refutation.
