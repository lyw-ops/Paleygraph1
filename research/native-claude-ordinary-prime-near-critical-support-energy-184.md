# Round 184 native Claude draft: energy of the near-critical support

- call_id: `ordinary-prime-near-critical-support-energy`
- agent_label: Claude Opus 5.5 research side session, Round 184
- Mission: `coordination/missions/round-184/ordinary-prime-near-critical-support-energy.md` (coordinator record `coordination/round-183.json`, SHA-256 `1231bfe2ad7af3148d2574dab427d0f9c6c3e831b6207a8ccef72451daab4f8e`, matches). I read all six listed sources and their SHA-256 values match the mission. I also read `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-183.md`, and for the inputs of §2, `research/parallel-cap-19.md` (§3, overlap rigidity) and `research/parallel-rectangle-20.md` (§§2–4, the nonalternating coset gap).
- Status: agent draft. This is not an acceptance, a human review or a mathematical certification.
- Scripts: `research/paley-184-energy-search.py` (floating heuristic search) and `research/paley-184-energy-subgroup.py` (exact integer subgroup sums).

## Result summary

**Verdict: inconclusive** (mission definitions). I neither prove \(\mathcal E(S)=o(|S|^3)\) on (NC) nor construct a near-critical configuration with \(\mathcal E(S)\asymp|S|^3\). **The largest excluded energy constant stays \(1/2\).** The range \((\delta|S|^3,\tfrac12|S|^3)\) is not excluded for any \(\delta<1/2\), even conditionally on accepted inputs. What changed:

1. **An exact identity (any law; Proposition 1).** \(\sum g^2/G=\sum_a\lambda_a q_a\), where \(\lambda=\nu*\check\nu\) and \(q_a=\lambda_a/\lambda_0=\widehat g(a)/G\in[0,1]\). The quantity in question is the mean of the normalized multiplicative Fourier coefficients of \(g\), under the law \(\lambda\) itself.
2. **Overlap dichotomy for the actual law (on (NC); Theorem 2).** This is the structural input on the actual \(g\) the mission asks to be stated separately. Uniformly in \(a\),
   \[
   (1-q_a)(2q_a-1)\le o(1),\qquad\text{so}\qquad q_a\in[0,\tfrac12+o(1)]\cup[1-o(1),1].
   \]
   The large coefficients form a subgroup \(H_*\le\widehat Q\) of order \(o(m_0)\), and \(g\) puts mass \((1-o(1))G\) on the annihilator \(\Gamma_*=H_*^\perp\le Q\), a subgroup of order \(n/|H_*|\), which is much larger than \(\sqrt p\). Outside \(H_*\), every normalized multiplicative Fourier coefficient of \(g\) is at most \(\tfrac12+o(1)\).
3. **A second proof of the cap \(1/2\) (Corollary 3).** This proof uses the dichotomy and the Round 20 §3 gap (for \(|H_*|=o(m_0)\)), not the Round 20 energy hypothesis. It also explains why \(1/2\) is where the argument stops. The cap is approached only if almost all of the difference law \(\lambda\) sits at overlap level \(1/2\), on a difference set \(P\) with \(|P|\le(2+o(1))m_0\) (Corollary 3(ii)). The model that reaches \(1/2\) is a half-dense subset of a coset of a subgroup of order \(2m_0\).
4. **The coset models need one arithmetic input (Proposition 4, (NC)).** Suppose \(S\) is \(o(m_0)\)-close to a subset of a single coset \(a+H\) with \(|H|\le Cm_0\). Then the multiplicative subgroup \(B=H^\perp\), of order \(b\ge(1-o(1))\sqrt p/C\), has \(\chi(1-y)=\rho\) for all but \(o(b)\) of its elements, and \(\mathcal E(S)/|S|^3\ge1/C-o(1)\).
   - For \(C<2\) this is already excluded by Proposition 1.4 of Round 183 (unconditionally on (NC)).
   - For \(C\ge2\) it is excluded by the arithmetic statement **(Sub\(_C\))**: no subgroup of order \(\ge\sqrt p/C\) has its shifted quadratic-character sum \(\sum_{y\in B}\chi(1-y)\) equal to \((1-o(1))|B|\) in absolute value. I could not find (Sub\(_C\)) proved for \(|B|\asymp\sqrt p\). Round 20's gap (7) does not give it, because the additive defect of \(1_B\) is not small.
   - A partial corollary needs no input. On (NC), no coset of a subgroup of order \(\le(2-\delta)m_0\) contains more than \((1-\delta/2)^{1/4}|S|\) points of \(S\), up to \(o(|S|)\).
5. **Evidence (floating and exact, finite).**
   - Heuristic search for flat sets with signed pair average near 1 (the (NC) condition) finds best averages of 0.57, 0.52, 0.48, 0.45 and 0.30 at \(p=1009\), 4001, 10009, 20021 and 40009, far from 1. The best sets have energy near the random level \(2/m\). No near-critical model was found, so there is no model on which to measure \(\mathcal E(S)\).
   - Exact subgroup sums show that (Sub) is delicate at small \(p\): subgroups with \(b\approx0.25\sqrt p\) and \(\chi(1-y)\) constant on all of \(B\setminus\{1\}\) exist (e.g. \(p=9601\), \(b=24\)). At \(b\ge30\) and \(p\le2\cdot10^5\), the largest ratio \(|A(B)|/(b-1)\) is 0.93 at \(b/\sqrt p\approx0.25\), and 0.65 and 0.51 in the bands \(b/\sqrt p\in[0.5,1)\) and \([1,2)\). For \(2\cdot10^5<p\le2\cdot10^6\) (264 133 subgroups) these maxima fall to 0.49, 0.31 and 0.21.

So the energy question has a sharper form, but it remains the open low-energy regime. Below \(1/2\) the obstruction is a combinatorial stability statement (near-\(1/2\) overlap structure forces a subgroup) together with an arithmetic subgroup statement (Sub\(_2\)). Below that, for \(\delta<\mathcal E/|S|^3<\tfrac12-\eta\), no accepted input applies.

## Setup and hypotheses

Notation and normalizations are those of Round 183 (row-deleted report, "Setup and hypotheses"), with counting norms.

- \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(Q\) the squares, \(\widehat Q\cong\mathbb Z/n\) (characters \(\psi^j\), with \(\psi\) a generator), \(m_0=n/\sqrt p\), \(\chi\) the Legendre symbol, \(s(x)=\chi(1-x)\) on \(Q\).
- \(k(d)=p^{-1/2}\sum_{x\in Q}s(x)\psi^d(x)\), which is real since \(s(x^{-1})=s(x)\), with \(|k|\le1\). Also \(K_{ij}=k(i-j)/m_0\), which is multiplication by \(s\) in \(x\)-space, and \(K^2=I-J\) (Rounds 19, 20).
- **Actual law.** \(b\ge0\), \(b_0=0\), \(\nu=b/\sum b\), \(f=\sum_j\nu_j\psi^j\) on \(Q\), \(g=|f|^2\), \(G=\sum g=n\|\nu\|_2^2=n/m_{\rm eff}\), \(\lambda=\nu*\check\nu\) (so \(\lambda_a=\sum_j\nu_j\nu_{j+a}\), \(\lambda\ge0\), \(\sum_a\lambda_a=1\)), and \(e=\nu/\|\nu\|_2\).
- **(NC)** is the near-critical branch: \(\|L_\sigma b\|_{2,n}/r\to0\) and \(m_{\rm eff}/m_0\to1\) along the hypothetical sequence of primes. All \(o(1)\) refer to this sequence. Statements marked (NC) assume it. \(\rho=-\sigma\) is the favorable sign of Round 151/183.
- **Accepted inputs used** (mission scope):
  - (I1) Round 20 flattening (`anchored-repair-20.md`, lines 74–76 in the "uniform single-step gap" section; Round 183 audit (a4)): on (NC), \(\sigma Ke=e+o_{\ell^2}(1)\), \(e=|S|^{-1/2}1_S+o_{\ell^2}(1)\), \(|S|=(1+o(1))m_0\), and the signed pair deficit \(d_\sigma(S)=|S|^{-2}\sum_{i,j\in S}(1-\sigma k(i-j))\to0\).
  - (I2) The Round 20 nonalternating coset gap (`parallel-rectangle-20.md` §3): for a fixed \(r_0\), a union \(U\) of at most \(r_0\) cosets of one subgroup with \(|U|\sim m_0\) cannot have \(d_\sigma(U)\to0\). The conclusion is stable under \(o(m_0)\) changes of \(U\). This is the input inside the Round 20 gap theorem that the mission lists.
  - (I3) Round 183 Propositions 1.1, 1.2 and 1.4, as accepted on (NC): \(\sum g^2=n\mathcal E(\nu)\); \(G_{-\rho}=O(1)\) and \(G=(1+o(1))\sqrt p\); and \(\sum g^2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\le\tfrac12+o(1)\).
  - (I4) Round 151 coset-mass exclusion (`ordinary-prime-coset-spread-151.md`, item 3): \(t_B+d_a\gg L^{-4}\log^{-2}(2L)\). This is used only in remarks.
- The overlap-rigidity computation of Round 19 §3 is re-proved in Theorem 2 for the case \(A=T=S\) needed here, so this report does not rely on Round 19 as an accepted citation.

**Sign convention.** Round 20 writes the near-eigenvector relation with its own \(\sigma\) (there \(P=P_{-\sigma}\)); Rounds 151/183 write the defect as \(L_\sigma\) and the favorable sign as \(\rho=-\sigma\). To avoid mixing them I fix the sign by the sector: \(\rho\) is the sign with \(G_{-\rho}=O(1)\) in (I3). Lemma 0 below derives \(\rho Ke\approx e\) and \(d_\rho(S)\to0\) from (I3) and the flattening (I1) alone, so no sign bookkeeping between rounds is needed.

## 1. Proved statements

### Lemma 0 (the near-eigenvector relation in the sector sign; (NC))
Let \(u_S=|S|^{-1/2}1_S\). On (NC),
\[
\langle e,\rho Ke\rangle=1-O(1/\sqrt p),\qquad \|\rho Ke-e\|_2\to0,\qquad \|\rho Ku_S-u_S\|_2\to0,\qquad d_\rho(S)\to0,
\]
where \(d_\rho(S)=|S|^{-2}\sum_{i,j\in S}(1-\rho k(i-j))\).

*Proof.* \(\langle f,sf\rangle=\sum_{j,j'}\nu_j\nu_{j'}\sum_xs(x)\psi^{j-j'}(x)=n\langle\nu,K\nu\rangle\) and \(\langle f,f\rangle=n\langle\nu,\nu\rangle\). Hence
\[
\langle e,\rho Ke\rangle=\frac{\sum_x\rho s(x)g(x)}{G}=\frac{G_\rho-G_{-\rho}}{G}=1-\frac{2G_{-\rho}+1}{G},
\]
since \(s(1)=0\) and \(g(1)=1\). By (I3), \(G_{-\rho}=O(1)\) and \(G\sim\sqrt p\). Since \(\|K\|\le1\), \(\|\rho Ke-e\|^2\le2-2\langle e,\rho Ke\rangle\to0\). By (I1), \(\|e-u_S\|\to0\), and \(K\) is a contraction, so \(\rho Ku_S=u_S+o(1)\). Finally \(\langle u_S,\rho Ku_S\rangle=(|S|/m_0)(1-d_\rho(S))\to1\) and \(|S|/m_0\to1\). \(\square\)

This is a consistency check of the inputs; Round 20 obtains the same relation from \(\|Le\|\to0\).

### Proposition 1 (the energy is a mean overlap; exact, any law)
Put \(\widehat g(a)=\sum_{x\in Q}g(x)\overline{\psi^a(x)}\) and \(q_a=\lambda_a/\lambda_0\). Then
\[
\widehat g(a)=n\lambda_a\ge0,\qquad q_a=\frac{\widehat g(a)}{G}\in[0,1],\qquad \sum_a q_a=\frac1{\lambda_0}=m_{\rm eff},\qquad
\boxed{\ \frac{\sum_xg(x)^2}{G}=\sum_a\lambda_a\,q_a\ }.
\]
The function \(q\) is positive definite on \(\mathbb Z/n\).

*Proof.* On \(Q\), \(g=\sum_d\lambda_d\psi^d\) (Round 183, proof of Proposition 1.1), so \(\widehat g(a)=n\lambda_a\), \(G=n\lambda_0\) and \(\sum g^2=n\sum_a\lambda_a^2\). Divide: \(\sum g^2/G=\sum_a\lambda_a^2/\lambda_0=\sum_a\lambda_aq_a\). Also \(\lambda\ge0\) because \(\nu\ge0\), \(\lambda_a\le\lambda_0\) by Cauchy–Schwarz, \(\sum_a\lambda_a=1\), \(\lambda_0=\|\nu\|_2^2=1/m_{\rm eff}\), and the Fourier transform of \(\lambda\) is \(|\widehat\nu|^2\ge0\). \(\square\)

On (NC), \(G=(1+o(1))\sqrt p\) (I3), so \(\sum g^2/\sqrt p=(1+o(1))\sum_a\lambda_aq_a\). Moreover \(q_a=\langle e,\tau_ae\rangle\) with \((\tau_ae)_j=e_{j+a}\), and \(\|e-u_S\|\to0\), so uniformly in \(a\)
\[
q_a=r_S(a)+o(1),\qquad r_S(a)=\frac{|S\cap(S+a)|}{|S|}.\tag{1.1}
\]

### Theorem 2 (overlap dichotomy for the actual law; (NC))
Uniformly in \(a\in\mathbb Z/n\),
\[
(1-r_S(a))(2r_S(a)-1)\le d_\rho(S)+o(1)=o(1),\qquad\text{equivalently}\qquad (1-q_a)(2q_a-1)\le o(1).
\]
Let \(H_*=\{a:r_S(a)>3/4\}\). For all large \(p\) on the sequence:
1. \(H_*\) is a subgroup of \(\mathbb Z/n\), and \(r_S(a)=1-o(1)\) on \(H_*\), \(r_S(a)\le\tfrac12+o(1)\) off \(H_*\), uniformly.
2. \(|H_*|=o(m_0)\).
3. With \(\Gamma_*=H_*^\perp\le Q\), a multiplicative subgroup of order \(n/|H_*|\) (so \(|\Gamma_*|/\sqrt p\to\infty\)), \(\sum_{x\notin\Gamma_*}g(x)=o(G)\).
4. In particular \(\max_{a\notin H_*}\widehat g(a)\le(\tfrac12+o(1))\,G\).

*Proof of the dichotomy.* This is Round 19 §3 with \(A=T=S\), re-proved here. Fix \(a\), put \(U=S+a\), \(m=|S|=|U|\) and \(r=r_S(a)\), so \(|S\cap U|=rm\) and \(|S\setminus U|=|U\setminus S|=(1-r)m\). \(K\) commutes with translations, so by Lemma 0, \(\rho Ku_U=u_U+o(1)\) uniformly in \(a\). Since \(S\setminus U\) is disjoint from \(U\),
\[
\langle1_{S\setminus U},\rho K1_U\rangle=\sqrt m\,\langle1_{S\setminus U},u_U+o(1)\rangle\le\sqrt m\sqrt{(1-r)m}\;o(1)=o(m).
\]
On the other hand \(m_0\langle1_{S\setminus U},\rho K1_U\rangle=\sum_{i\in S\setminus U}\sum_{j\in U}\rho k(i-j)\). Split the inner sum.
- For \(j\in U\cap S\), the pairs lie in \(S\times S\), and every term satisfies \(1-\rho k\ge0\), so this part is at least \(|S\setminus U||S\cap U|-m^2d_\rho(S)\).
- For \(j\in U\setminus S\), \(\rho k\ge-1\), so this part is at least \(-|S\setminus U||U\setminus S|\).

Together, \(m^2[(1-r)(2r-1)-d_\rho(S)]\le m_0\,o(m)\). Since \(m\sim m_0\) and \(d_\rho(S)\to0\) (Lemma 0), the claim follows. The equivalent form uses (1.1). \(\square\)

*Proof of 1.* Let \(\varepsilon_p=\sup_a\max(0,(1-r_S(a))(2r_S(a)-1))\to0\). For \(\varepsilon_p<1/16\), every \(r_S(a)\) lies in \([0,\tfrac12+2\varepsilon_p]\cup[1-2\varepsilon_p,1]\): the function \(r\mapsto(1-r)(2r-1)\) is concave, and at the endpoints of \([\tfrac12+2\varepsilon,1-2\varepsilon]\) it equals \(2\varepsilon-8\varepsilon^2\) and \(2\varepsilon-8\varepsilon^2\); both exceed \(\varepsilon\) when \(\varepsilon<1/8\). So it exceeds \(\varepsilon_p\) on that whole interval (take \(\varepsilon=\varepsilon_p\)). If \(a,b\in H_*\), then \(|S\triangle(S+a)|=2m(1-r_S(a))\le4\varepsilon_pm\), and
\[
|S\triangle(S+a+b)|\le|S\triangle(S+a)|+|(S+a)\triangle(S+a+b)|\le8\varepsilon_pm .
\]
So \(r_S(a+b)\ge1-4\varepsilon_p>3/4\). Also \(r_S(-a)=r_S(a)\) and \(0\in H_*\).

*Proof of 2.* Suppose \(|H_*|\ge\eta m_0\) along a subsequence, for a fixed \(\eta>0\). Average over \(H_*\): \(\varphi=1_S*(1_{H_*}/|H_*|)\) is constant on \(H_*\)-cosets, and
\[
\|1_S-\varphi\|_1\le\frac1{|H_*|}\sum_{a\in H_*}|S\triangle(S+a)|\le4\varepsilon_pm .
\]
Let \(U\) be the union of the \(H_*\)-cosets on which \(\varphi\ge1/2\). Pointwise, \(|1_S-1_U|\le2|1_S-\varphi|\), so \(|S\triangle U|\le8\varepsilon_pm=o(m_0)\). \(U\) is a union of at most \((1+o(1))m/(\eta m_0)\le2/\eta\) cosets of \(H_*\), with \(|U|\sim m_0\). Since \(|k|\le1\), \(d_\rho(U)\le d_\rho(S)+O(|S\triangle U|/m)\to0\). This contradicts the Round 20 nonalternating coset gap (I2) with \(r_0=\lfloor2/\eta\rfloor\) (either sign).

*Proof of 3, 4.* For \(a\in H_*\), \(\widehat g(a)=Gq_a\) is real and \(q_a=1-o(1)\) uniformly by (1.1). So \(\sum_xg(x)(1-\Re\psi^a(x))=G(1-q_a)=o(G)\) uniformly on \(H_*\). Average over \(a\in H_*\), using \(|H_*|^{-1}\sum_{a\in H_*}\psi^a=1_{\Gamma_*}\): \(\sum_xg(x)(1-1_{\Gamma_*}(x))=o(G)\). Also \(|\Gamma_*|=n/|H_*|=\sqrt p\,(m_0/|H_*|)\), and \(m_0/|H_*|\to\infty\) by 2. Item 4 restates 1 through \(q_a=\widehat g(a)/G\). \(\square\)

**What Theorem 2 is, as a statement about \(g\).** On (NC), every normalized multiplicative Fourier coefficient \(\widehat g(a)/G\) of the actual \(g\) avoids the window \((\tfrac12+o(1),1-o(1))\). The near-1 ones form a subgroup of characters whose annihilator carries almost all of \(g\), and that annihilator has order much larger than \(\sqrt p\). This is a level-\(\tfrac12\) uniformity, with no power saving. It is the only structural input on the actual \(g\) proved here; see §4 for its relevance to the slope-row-mass call.

### Corollary 3 (the cap \(\tfrac12\), and what reaching it requires; (NC))
(i) \(\sum g^2/G\le\tfrac12+o(1)\), hence \(\sum g^2\le(\tfrac12+o(1))\sqrt p\) and \(\mathcal E(S)\le(\tfrac12+o(1))|S|^3\).

(ii) Suppose \(\sum g^2/G\ge\tfrac12-\eta\) with \(0<\eta<1/16\), and put \(t=\sqrt\eta\) and \(P=\{a\notin H_*:q_a\ge\tfrac12-t\}\). Then:
- \(\lambda(\mathbb Z/n\setminus P)\le\sqrt\eta+o(1)\);
- \((2-O(\sqrt\eta)-o(1))m_0\le|P|\le(2+O(\sqrt\eta)+o(1))m_0\);
- \(q_a\in[\tfrac12-\sqrt\eta,\tfrac12+o(1)]\) on \(P\);
- \(\widehat{1_P}(\xi)\ge-(O(\sqrt\eta)+o(1))\,|P|\) for every \(\xi\).

So the difference law of \(S\) is, up to \(O(\sqrt\eta)\) in \(\ell^1\), the uniform half-weight on a set \(P\) of size \(\approx2m_0\) whose indicator has almost nonnegative Fourier transform.

*Proof.* (i) \(\sum_a\lambda_aq_a\le\sum_{a\in H_*}\lambda_a+(\tfrac12+o(1))\sum_{a\notin H_*}\lambda_a\), and \(\sum_{a\in H_*}\lambda_a\le|H_*|\lambda_0=|H_*|/m_{\rm eff}=o(1)\) by Theorem 2.2. Then use \(G\sim\sqrt p\) and (I3).

(ii) Off \(H_*\), \(\tfrac12+o(1)-q_a\ge0\), so
\[
\sum_{a\notin H_*}\lambda_a(\tfrac12+o(1)-q_a)\le\eta+o(1).
\]
The \(\lambda\)-mass of \(\{a\notin H_*:q_a<\tfrac12-t\}\) is therefore at most \((\eta+o(1))/t\), and \(H_*\) has mass \(o(1)\). For the size of \(P\):
- the upper bound comes from \(\sum_aq_a=m_{\rm eff}\) and \(q\ge\tfrac12-t\) on \(P\);
- the lower bound comes from \(\sum_{a\in P}q_a=m_{\rm eff}\lambda(P)\ge(1-O(\sqrt\eta)-o(1))m_0\) and \(q\le\tfrac12+o(1)\) on \(P\).

For the Fourier bound, write \(q=\tfrac121_P+R\). Then
\[
\|R\|_1\le|H_*|+\sum_{a\in P}|q_a-\tfrac12|+\sum_{a\notin P\cup H_*}q_a\le o(m_0)+(t+o(1))|P|+m_{\rm eff}(\eta/t+o(1)),
\]
which is \(O(\sqrt\eta+o(1))\,m_0\). Positive definiteness gives \(0\le\widehat q=\tfrac12\widehat{1_P}+\widehat R\), with \(|\widehat R|\le\|R\|_1\). \(\square\)

**Reading.**
- (i) is the Round 183 bound with a second proof. The proof shows why \(\tfrac12\) is exactly where this method stops. The dichotomy caps every nontrivial overlap at \(\tfrac12\), and nothing in it penalizes overlaps of exactly \(\tfrac12\).
- The model attaining (ii) is \(S\) a "random" half of a coset of a subgroup \(H\) of order \(2m_0\), with \(P=H\) and \(\widehat{1_H}\ge0\). Arithmetic progressions and Bohr sets do not qualify: their overlaps decay linearly, and their indicators have negative Fourier lobes of order \(|P|\). A half-dense subset of an interval of length \(2m_0\) has energy about \(\tfrac13\).
- I do not prove that (ii) forces \(P\) to be close to a subgroup. That combinatorial stability statement is the first missing piece below \(\tfrac12\) (§3).

### Proposition 4 (single-coset configurations; (NC))
Let \(H\le\mathbb Z/n\) be a subgroup with \(|H|=C'm_0\), and \(a+H\) one of its cosets. Put \(c=|S\cap(a+H)|/|S|\), \(B=H^\perp\le Q\) and \(b=|B|=n/|H|=\sqrt p/C'\). Then:
1. The law mass of the coset is \(\nu(a+H)=c+o(1)\), and \(\nu(\mathbb Z/n\setminus S)=o(1)\).
2. \(\sum_{y\in B}g(y)\ge b\,c^2-o(b)\), and \(\mathcal E(S)/|S|^3\ge c^4/C'-o(1)\).
3. If \(c=1-o(1)\), then \(g\ge1-o(1)\) at every point of \(B\), and
   \[
   \#\{y\in B\setminus\{1\}:\chi(1-y)\ne\rho\}=O(1),\qquad \sum_{y\in B\setminus\{1\}}\chi(1-y)=\rho(b-1)-O(1),
   \]
   with \(\mathcal E(S)/|S|^3\ge1/C'-o(1)\) and \(C'\ge1-o(1)\).
4. Consequently, without further input:
   - (a) no near-critical \(S\) lies within \(o(m_0)\) of a single coset of a subgroup of order \(\le(2-\delta)m_0\);
   - (b) every coset of every subgroup of order \(\le(2-\delta)m_0\) contains at most \(\bigl((1-\delta/2)^{1/4}+o(1)\bigr)|S|\) points of \(S\).

*Proof.*
1. \(\nu_j=\|\nu\|_2e_j\), and \(\|\nu\|_2\|e\|_1=1\), so \(\|e\|_1=\sqrt{m_{\rm eff}}\). From \(\|e-u_S\|\to0\), \(\sum_{j\in S}e_j=\sqrt{|S|}\langle e,u_S\rangle=(1-o(1))\sqrt{m_0}\), hence \(\sum_{j\notin S}e_j=o(\sqrt{m_0})\) and \(\nu(S^c)=o(1)\). For \(T\subseteq S\), \(\sum_{j\in T}e_j=\langle e,1_T\rangle=|T|/\sqrt{|S|}+o(\sqrt{m_0})\), so \(\nu(T)=|T|/|S|+o(1)\). Apply this with \(T=S\cap(a+H)\).
2. Restricted to \(B\), \(f=\sum_{\text{cosets }D\text{ of }H}\nu(D)\,\psi^{a_D}|_B\). The restricted characters \(\psi^{a_D}|_B\) are distinct for distinct cosets, hence orthogonal on \(B\). So \(\sum_Bg=b\sum_D\nu(D)^2\ge b\,\nu(a+H)^2\). Then \(\sum g^2\ge\sum_Bg^2\ge(\sum_Bg)^2/b\ge b(c^2-o(1))^2\). Divide by \(\sqrt p\) and use (I3).
3. Write \(\nu=\nu'+\nu''\) with \(\nu'=\nu1_{a+H}\), so \(\|\nu''\|_1=o(1)\) by 1. For \(y\in B\), \(f'=\sum\nu'_j\psi^j\) satisfies \(f'(y)=\psi^a(y)\nu'(\mathbb Z/n)\), so \(|f'(y)|=1-o(1)\). Also \(|f''|\le\|\nu''\|_1=o(1)\) pointwise, so \(g\ge1-o(1)\) on \(B\). By (I3), \(\sum_{T_{-\rho}}g=G_{-\rho}=O(1)\), so \(B\cap T_{-\rho}\) has \(O(1)\) points. Every \(y\in B\setminus\{1\}\) has \(\chi(1-y)\ne0\). The energy bound is 2 with \(c=1\). Also \(b(1-o(1))\le\sum_Bg\le G\sim\sqrt p\) gives \(C'\ge1-o(1)\).
4. Proposition 1.4 of Round 183 gives \(\mathcal E(S)/|S|^3\le\tfrac12+o(1)\). Combine with 2 for \(C'\le2-\delta\), and with 3 for (a). \(\square\)

**What Proposition 4 isolates.** The cap configuration of Corollary 3(ii) (half of a coset of order \(2m_0\)) and every single-coset configuration with \(2\le C'\le1/\delta\) need a multiplicative subgroup \(B\) of order \(\sqrt p/C'\) on which \(\chi(1-y)\) is constant except at \(O(1)\) points. The arithmetic statement that excludes this is

> **(Sub\(_C\))** For every fixed \(C\) and \(K\), for all large primes \(p\equiv1\pmod4\), no subgroup \(B\le Q\) of order \(b\ge\sqrt p/C\) has \(\chi(1-y)\) constant on all but \(K\) points of \(B\setminus\{1\}\).

(Sub\(_C\)) is weaker than \(\bigl|\sum_{y\in B}\chi(1-y)\bigr|\le(1-c)|B|\). I do not know a proof for \(|B|\asymp\sqrt p\).
- Completing the sum over cosets gives only the trivial \(\sqrt p\).
- The Round 20 cap inequality (7) does not apply: the additive defect of \(1_B\) is \(1-|H|^{-1}\sum_{u\in H}\rho k(u)\), which is close to \(1-1/C'\), not small. For the same reason Round 20 §3 covers only \(|U|\sim m_0\).
- Round 151 (I4) excludes \(f\) whose mass is \(1-o(1)\) on a bounded union of cosets of size \(\asymp\sqrt p\). Here \(B\) carries only the fraction \(1/C'\le\tfrac12\) of the mass.

## 2. Which energy range is excluded, and on what grounds

| range of \(\mathcal E(S)/|S|^3\) on (NC) | status | grounds |
|---|---|---|
| \((\tfrac12,1]\) | **excluded** (accepted) | Round 20 gap theorem via Round 183 Proposition 1.4. Second proof: Theorem 2 with Corollary 3(i), using (I1), (I2), (I3). |
| near \(\tfrac12\), single-coset form (\(S\) within \(o(m_0)\) of one coset of a subgroup of order \(\le3m_0\)) | **conditional**: excluded under (Sub\(_3\)) | Proposition 4.3 |
| \([\tfrac12-\eta,\tfrac12]\) in general | **conditional**: excluded under (St) and (Sub\(_3\)) (Criterion C1) | Corollary 3(ii) and Proposition 4.3 |
| \([\delta,\tfrac12-\eta]\) | **not excluded** | no accepted input applies; see §3 |
| configurations with a fraction \(c\) of \(S\) in one coset of a subgroup of order \(C'm_0\), \(C'<2\) | **excluded** for \(c>(C'/2)^{1/4}\) | Proposition 4.2 with Proposition 1.4 |
| \(S\) within \(o(m_0)\) of a union of \(\le r_0\) cosets of one subgroup with \(|U|\sim m_0\) | **excluded** (accepted) | Round 20 §3 (this is (I2)) |

**The largest excluded energy constant below \(\tfrac12\) is none.** Unconditionally on (NC), the proved range is
\[
\frac1{\sqrt p}\lesssim\frac{\sum g^2}{\sqrt p}=\frac{\mathcal E(S)}{|S|^3}+o(1)\le\frac12+o(1),
\]
the same as Round 183. Only specific structured configurations inside \((\delta,\tfrac12]\) are excluded (rows 5 and 6).

## 3. Conditional criteria

**(St) Combinatorial stability at the half level.** Suppose \(S\subset\mathbb Z/n\), \(|S|=m\to\infty\), satisfies \(r_S(a)\le\tfrac12+o(1)\) off a subgroup of order \(o(m)\) and \(\mathcal E(S)\ge(\tfrac12-o(1))m^3\). Then some subgroup \(H\) of order \((2+o(1))m\) has a coset containing \((1-o(1))m\) points of \(S\).

The model is a half-dense subset of a subgroup. Corollary 3(ii) gives a set \(P\) of size \(\approx2m\) carrying the difference law at the half level, with \(\widehat{1_P}\ge-o(|P|)\). (St) says such \(P\) must be close to a subgroup. I did not prove (St). It concerns flat sets only and uses no arithmetic.

**Criterion C1.** (St) and (Sub\(_3\)) imply \(\limsup\mathcal E(S)/|S|^3\le\tfrac12-c\) on (NC), for some \(c>0\) depending on the rates in (St).

*Proof.* Take a contrary sequence with \(\mathcal E(S)/|S|^3\to\tfrac12\). By Theorem 2, \(S\) satisfies the hypotheses of (St), so it lies within \(o(m_0)\) of a coset of a subgroup of order \((2+o(1))m_0\le3m_0\). Proposition 4.3 then produces a subgroup \(B\) of order \(\ge\sqrt p/3\) on which \(\chi(1-y)=\rho\) except at \(O(1)\) points, contrary to (Sub\(_3\)). \(\square\)

**Criterion C2 (towards \(o(|S|^3)\); a sufficient programme, not a proof).** Suppose \(\mathcal E(S)\ge\delta|S|^3\).
- The Reiher–Schoen 2024 Theorem 1.2 BSG (as quoted in the Round 183 audit), applied with \(K=\delta^{-1}\), gives \(S'\subseteq S\) with \(|S'|\gg\delta^{1/2}|S|\) and \(|S'-S'|\ll\delta^{-4}|S'|\).
- Green–Ruzsa's Freiman theorem in abelian groups then places \(S'\) inside a coset progression \(H+P_d\), of rank \(d=O_\delta(1)\) and size \(O_\delta(m_0)\).

Excluding every such piece on (NC) would prove \(\mathcal E(S)=o(|S|^3)\). Proposition 4.2 handles the pure-subgroup piece (\(d=0\), \(|H|\le(2-\delta')m_0\)) only when the fraction is large. Two cases remain:
- the subgroup case at fraction \(c\le(C'/2)^{1/4}\);
- the progression case (\(d\ge1\)), where the \(x\)-space image of the piece is a multiplicative Bohr set, a union of "multiplicative intervals" \(\{\theta^i:i\in I\}\) of total size \(\asymp\sqrt p\). Its arithmetic analogue of (Sub) would be a nontrivial bound for \(\sum_{i\in I}\chi(1-\theta^{i})\) over intervals of length \(\asymp\sqrt p\) in the exponent. I know of no such bound at that length.

In both cases Theorem 2 constrains \(S\), but a piece with \(c\le\tfrac12\) can have relative overlaps \(\le\tfrac12\), so the dichotomy alone does not see it.

**Consequences, if the energy question were settled** (inherited, Round 183 (b3)):
- \(\mathcal E(S)=O(|S|^3p^{-\delta})\iff\sum g^2=O(p^{1/2-\delta})\). This relaxes (b1‴) by \(p^{\delta/2}\) and the IXX requirement on \(\mathcal E(\mu)\) to \(O(p^{5/2+2\delta})\).
- Bounded away from \(\tfrac12\) (Criterion C1) changes only constants.

## 4. Structural input on the actual \(g\) (for the closeout)

The single structural lemma on the actual \(g\) proved here is **Theorem 2**. On (NC):
- \(\widehat g(a)/G\in[0,\tfrac12+o(1)]\cup[1-o(1),1]\) for every \(a\);
- the large coefficients form a subgroup \(H_*\) of order \(o(\sqrt p)\);
- \(g\) has mass \((1-o(1))G\) on \(\Gamma_*=H_*^\perp\).

It also gives Proposition 4.2's coset-fraction bound.

**Relation to the slope-row-mass call (cand:slope-row-mass-x).** That call needs \(X=E_Q(h)=O(p^{1+\varepsilon})\) and \(\max_\xi W_\xi=O(p^{1+\varepsilon})\) for \(h(z)=g(1-z)\). These are multiplicative energies of the additive shift of \(g\). Theorem 2 is a level-\(\tfrac12\) statement about the multiplicative Fourier coefficients of \(g\) itself, with no power saving, and I see no way to turn it into a power bound for \(E_Q(h)\). The structure shared by the two calls is the inputs, not an estimate:
- the flattening \(e\approx u_S\) (I1);
- the sector concentration \(G_{-\rho}=O(1)\) (I3), which places \(h\) on \(\{\chi(z)=\rho\}\);
- Round 151 coset-mass exclusion (I4).

**There is no shared estimate in this report.** If the slope-row-mass call proves a lemma about the flat support \(S\), the statement to compare is Theorem 2 together with Proposition 4. The quantity \(\sum g^2\) enters both through Round 183's (G2)/(b3) at different scales; it is not decided here.

## 5. Evidence (finite; not proofs)

### 5.1 Heuristic search for near-critical flat sets (floating)
`research/paley-184-energy-search.py` maximizes the signed pair average \(\mathrm{avg}_\sigma(S)=|S|^{-2}\sum_{s,s'\in S}\sigma k(s-s')\) over sets with \(|S|=\mathrm{round}(m_0)\), for both signs. Near-criticality of a flat law on \(S\) is exactly \(\mathrm{avg}\to1\) (Lemma 0).
- Starts: random sets, a greedy build, and random subsets of every subgroup of order in \([m,4m]\), first restricted to the subgroup (`inH`) and then freed (`fromH`).
- Moves: greedy swaps with random perturbation.

The values are lower bounds for the true maximum at each \(p\). The search quality falls as \(n\) grows (fixed iteration budget, local moves only), so the downward trend is partly an artifact.

Best set found for each \((p,\sigma)\):

| \(p\) | \(m\) | \(\sigma\) | best avg\(_\sigma\) | start | \(\mathcal E(S)/|S|^3\) | \(\max_{a\ne0}r_S(a)\) |
|---|---|---|---|---|---|---|
| 1009 | 16 | +1 | 0.565 | random | 0.257 | 0.44 |
| 1009 | 16 | −1 | 0.582 | from subgroup 28 | 0.328 | 0.63 |
| 4001 | 32 | +1 | 0.484 | from subgroup 50 | 0.234 | 0.69 |
| 4001 | 32 | −1 | 0.521 | from subgroup 100 | 0.287 | 0.63 |
| 10009 | 50 | +1 | 0.477 | random | 0.114 | 0.34 |
| 10009 | 50 | −1 | 0.474 | from subgroup 139 | 0.491 | 0.92 |
| 20021 | 71 | +1 | 0.448 | greedy | 0.067 | 0.27 |
| 20021 | 71 | −1 | 0.357 | from subgroup 110 | 0.089 | 0.31 |
| 40009 | 100 | +1 | 0.305 | greedy | 0.026 | 0.06 |
| 40009 | 100 | −1 | 0.301 | greedy | 0.027 | 0.07 |

Reading:
- No set found is close to near-critical; the best pair averages are 0.30–0.58. So there is no finite near-critical model on which to measure the energy. This is consistent with the (NC) branch being a hypothetical contrary sequence. It is not evidence about \(\mathcal E(S)\) on (NC).
- Subsets of a subgroup, restricted to it (`inH` rows), have high energy (0.45–0.86) but low pair averages (−0.13 to 0.46). This matches the remark after Proposition 4: the pair average over a subgroup of order \(C'm_0\) is at most about \(1/C'\).
- The best unrestricted sets at the larger \(p\) have energy near the random level \(2/m\) (\(0.026\) against \(0.020\) at \(m=100\)).
- The one high-energy entry (\(p=10009\), \(\sigma=-1\), energy 0.49, overlap 0.92) has an overlap of 0.92, inside the window \((\tfrac12,1)\) that Theorem 2 forbids on (NC). With pair average 0.47 it is far from near-critical, so this does not contradict Theorem 2; it shows the dichotomy is a near-critical phenomenon.

### 5.2 Shifted-subgroup sums (exact integers)
`research/paley-184-energy-subgroup.py LO HI` computes \(A(B)=\sum_{y\in B\setminus\{1\}}\chi(1-y)\) for every subgroup \(B\le Q\) of order \(b\in[\sqrt p/4,2\sqrt p]\) and every prime \(p\equiv1\pmod 4\) in \([LO,HI]\).

| range of \(p\) | subgroups | band \(b/\sqrt p\) (\(b\ge30\)) | max \(|A|/(b-1)\) | at | mean |
|---|---|---|---|---|---|
| \([10^3,2\cdot10^5]\) | 35 861 | \([0.25,0.5)\) | 0.931 | \(p=14341,b=30\) | 0.115 |
| | | \([0.5,1)\) | 0.647 | \(p=4481,b=35\) | 0.084 |
| | | \([1,2)\) | 0.509 | \(p=2269,b=54\) | 0.060 |
| \([2\cdot10^5,2\cdot10^6]\) | 264 133 | \([0.25,0.5)\) | 0.487 | \(p=209569,b=118\) | 0.062 |
| | | \([0.5,1)\) | 0.307 | \(p=296137,b=324\) | 0.044 |
| | | \([1,2)\) | 0.214 | \(p=559549,b=891\) | 0.031 |

Reading:
- At small \(p\) the configuration that Proposition 4.3 requires does occur. There are subgroups with \(b\approx0.25\sqrt p\) and \(\chi(1-y)\) constant on all of \(B\setminus\{1\}\): for example \(p=9601\), \(b=24\), \(A=23\); and \(p=5113\), \(b=18\), \(A=17\). These have \(C'\approx4\), i.e. energy about \(\tfrac14\) in the single-coset model.
- For \(b\ge30\) the extreme ratios fall steadily, and the means scale roughly like \(b^{-1/2}\). This is consistent with (Sub\(_C\)), but it is finite evidence and says nothing about whether exceptional subgroups occur infinitely often.
- (Sub\(_3\)) needs a subgroup of order \(\ge\sqrt p/3\), i.e. band \(\ge0.33\). The largest \(b\ge30\) ratio there is below 0.65 for \(p<2\cdot10^5\) and below 0.49 beyond.

## 6. Proved / conditional / evidence

**Proved (a).**
- (a1) Exact, any law: \(\sum g^2/G=\sum_a\lambda_aq_a\), with \(q_a=\widehat g(a)/G\in[0,1]\) positive definite and \(\sum_aq_a=m_{\rm eff}\) (Proposition 1).
- (a2) On (NC), from (I1) and (I3): \(\rho Ke=e+o(1)\), \(\rho Ku_S=u_S+o(1)\), \(d_\rho(S)\to0\), in the sector sign (Lemma 0).
- (a3) On (NC), from (I1), (I2) and (I3): the overlap dichotomy, the subgroup \(H_*\) of order \(o(m_0)\), mass \((1-o(1))\) on \(\Gamma_*=H_*^\perp\), and \(\max_{a\notin H_*}\widehat g(a)\le(\tfrac12+o(1))G\) (Theorem 2).
- (a4) On (NC): \(\mathcal E(S)\le(\tfrac12+o(1))|S|^3\) by a second proof, and the half-level structure near the cap (Corollary 3).
- (a5) On (NC):
  - a coset of \(H\), \(|H|=C'm_0\), holding a fraction \(c\) of \(S\) forces \(\mathcal E(S)/|S|^3\ge c^4/C'-o(1)\);
  - if \(c=1-o(1)\), then \(B=H^\perp\) has \(\chi(1-y)=\rho\) except at \(O(1)\) points and \(g\ge1-o(1)\) on \(B\);
  - no near-critical \(S\) is \(o(m_0)\)-close to one coset of a subgroup of order \(\le(2-\delta)m_0\), and a coset of such a subgroup holds at most \((1-\delta/2)^{1/4}|S|+o(|S|)\) points of \(S\) (Proposition 4).

**Conditional (b).**
- (b1) (St) and (Sub\(_3\)) imply \(\mathcal E(S)/|S|^3\le\tfrac12-c\) on (NC) (Criterion C1).
- (b2) (Sub\(_C\)) excludes every single-coset configuration of energy \(\ge1/C\) (Proposition 4.3).
- (b3) Criterion C2: excluding dense pieces of bounded-rank coset progressions on (NC) gives \(o(|S|^3)\). Its subgroup case reduces to (Sub) at fraction \(c\); its progression case reduces to an open interval-in-exponent character-sum statement.

**Evidence (c).**
- (c1) Heuristic search (floating): best signed pair averages 0.30–0.58 at \(1009\le p\le40009\); no near-critical flat set found.
- (c2) Exact shifted-subgroup sums for \(p\le2\cdot10^6\): exact constancy at \(b\approx0.25\sqrt p\) for small \(p\); for \(b\ge30\) the maxima decrease with \(p\).

## 7. Exact remaining gap

1. **The mission question is open.** It is not known whether \(\mathcal E(S)=o(|S|^3)\) on (NC), equivalently \(\sum g^2=o(\sqrt p)\). The proven range is \([O(p^{-1/2}),\tfrac12+o(1)]\) for \(\mathcal E(S)/|S|^3\), unchanged from Round 183.
2. **Just below \(\tfrac12\):** (St), a purely combinatorial stability statement, and (Sub\(_3\)), an arithmetic statement about shifted subgroups of order \(\asymp\sqrt p\). With both, the excluded constant drops below \(\tfrac12\).
3. **The bulk range \([\delta,\tfrac12-\eta]\):** a way to exclude a \(c(\delta)\)-fraction of \(S\) in a coset progression of bounded rank and size \(O(m_0)\). Theorem 2 constrains only overlaps of the whole of \(S\). Round 151 (I4) gives only a fixed positive outside mass, and Round 20 §3 covers only unions of size \(\sim m_0\). None of them sees a piece of fraction \(\le\tfrac12\).
4. **Unchanged:** cand:slope-row-mass-x, the generic six-word class, the generic J sum and the zero-match estimate.

**What would change the proof plan.**
- A proof of (Sub\(_C\)) for all \(C\) would exclude every single-coset configuration of positive energy. It would leave progression pieces and fractional coset pieces.
- A near-critical flat set at large \(p\) (pair average \(\to1\)) with \(\mathcal E\asymp|S|^3\) would refute. The search found no set with pair average above 0.58.

## Replay

```
.venv/bin/python -B research/paley-184-energy-search.py 1009 4001 --restarts 4          # ~40 s
.venv/bin/python -B research/paley-184-energy-search.py 10009 20021 40009 --restarts 4  # ~90 s
.venv/bin/python -B research/paley-184-energy-subgroup.py 1000 200000                   # ~4 s
.venv/bin/python -B research/paley-184-energy-subgroup.py 200000 2000000                # ~130 s
```

Script SHA-256 values for the quoted output:
- `paley-184-energy-search.py`: `4cc396eabbbb49875036cea13e48ac6140224d6b07a1ecfc3622549475c7df35`
- `paley-184-energy-subgroup.py`: `ef44672e328c014b1204189de64f90c7827c9e9e52f4b2ebb75df3e2613b92e2`

The search is seeded by \(p\) (numpy `default_rng(p)`), so the runs are deterministic for a fixed numpy version (tested with the repository `.venv`). The subgroup sums are exact integer computations.

## Verdict

**Inconclusive** (mission definition).
- \(\mathcal E(S)=o(|S|^3)\) is neither proved nor refuted on (NC).
- **Largest excluded energy constant: \(\tfrac12\)** (unchanged). It now has a second proof through the overlap dichotomy (Theorem 2), which also shows that \(\tfrac12\) is exactly where the dichotomy stops.
- Below \(\tfrac12\), exclusion is conditional on (St) and (Sub\(_3\)) near the cap (Criterion C1). In the bulk range only specific coset configurations are excluded (Proposition 4).
- The structural lemma on the actual \(g\) is Theorem 2: on (NC), the normalized multiplicative Fourier coefficients of \(g\) avoid \((\tfrac12+o(1),1-o(1))\).
