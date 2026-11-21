# Round 190 native Claude draft: does (NC) exclude the sector-type obstruction laws?

- **call_id:** `ordinary-nc-excludes-sector-laws`
- **Author:** Claude subagent started by the Round 190 coordinator (session/r190-nc-sector). This is an agent assessment. It is not an audit, not human acceptance and not a mathematical certification.
- **Mission:** `coordination/missions/round-190/ordinary-nc-excludes-sector-laws.md`, exported from `coordination/round-189.json` (SHA-256 `8901a11c…ce822`, matches).
- **Inputs read.** All eight SHA-256 values listed in the mission match:
  - `research/round-188-acceptance.json` (`e0face6c…dcc6`), `research/round-189-acceptance.json` (`ad4e0b5a…6176506`): `proof_scope`, `failed_paths_and_open_bounds`;
  - `research/native-claude-audit-189.md` (`0bf8b1c3…e7f508`): §2 and §5 in full;
  - `research/native-claude-ordinary-prime-intercept-fibre-t0-189.md` (`2a586af8…b53b852`): in full;
  - `research/native-claude-ordinary-prime-near-critical-support-energy-184.md` (`9cac8976…fc45c1fa`): in full;
  - `research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md` (`85702949…c6e6c02ec`): in full;
  - `research/ordinary-prime-coset-spread-151.md` (`2029d03c…47823282`): in full;
  - `research/anchored-repair-20.md` (`141a0fb1…f3721`): in full.

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-189.md`, `research/native-claude-ordinary-prime-row-deleted-one-match-183.md` (in full, for the (NC) definition at line 53 and Propositions 1.1–1.4), and the `proof_scope` entries of `research/round-183-acceptance.json` … `round-189-acceptance.json` that mention (NC).
- **Scripts (all new):**
  - `research/paley-190-nc-identity.py`: Part A checks the identity of Lemma 1 against an explicit construction of \(K,J,P_\sigma,L_\sigma\) (floating linear algebra, \(p\le197\)); Part B builds the diluted-interval models of §4 (floating, evidence only).
  - `research/paley-190-nc-gpclique.py`: exact integer computation of geometric-progression Paley cliques (§5, evidence only), with a brute-force `--check`.
  - `research/paley-190-nc-exponents.py`: exact `Fraction` arithmetic for every exponent in this report.
- **Nothing was committed.** I wrote only this file and the three scripts.

## Result summary

**Verdict: inconclusive** (mission definitions). The accepted near-critical properties exclude the *exact* subgroup and interval laws, but not the Round 189 obstruction family as a whole. One part of (NC), the sector condition, constrains the family much more sharply than the accepted record says. But turning that constraint into an exclusion needs an open arithmetic statement about Paley cliques that are geometric progressions. Even then the exclusion would be qualitative. No bound on \(T_0\), \(X\) or \(\Gamma_{\rm tot}\) improves. The findings:

1. **Exact form of (NC) (Lemma 1; proved).** Let \(f\) be the actual Fourier transform, \(T_{-\rho}\) the unfavourable sector and \(\bar f_{-\rho}\) the mean of \(f\) over \(T_{-\rho}\). Then
   \[
   \frac{\|L_\sigma b\|_{2,n}^2}{r^2}=V_{-\rho}:=\sum_{x\in T_{-\rho}}\bigl|f(x)-\bar f_{-\rho}\bigr|^2 .
   \]
   So (NC) is: \(G/\sqrt p\to1\) **and** \(f\) is asymptotically constant on \(T_{-\rho}\) in \(\ell^2\). Since \(\nu_0=0\), \(|\bar f_{-\rho}|\le2(\sqrt p+1)/(p-5)\).
2. **Pointwise sector exclusion (Theorem 1; proved on (NC)).**
   - \(\tau_p:=\sup_{T_{-\rho}}g\le(V_{-\rho}^{1/2}+2(\sqrt p+1)/(p-5))^2\to0\), and \(G_{-\rho}\le V_{-\rho}+(\sqrt p+1)^2/(p-5)=1+o(1)\).
   - Round 183 Prop. 1.2 had only \(G_{-\rho}=O(1)\). The constant 1 is sharp: the \(\mathbb F_{r^2}\) control has \(G_-\to1\).
   - Consequently, for every fixed \(\tau>0\) and large \(p\), the level set \(\{g\ge\tau\}\) lies in \(T_\rho\cup\{1\}\).
   - If \(g\ge\tau\) on \(I\cdot I^{-1}\) for a symmetric geometric progression \(I=\{\zeta^k:|k|\le K\}\), then \(I\) is a **clique of the Paley graph** (\(\rho=+1\)) or of its complement (\(\rho=-1\)) (Lemma 2). Hence \(|I|\le\sqrt p\) by an elementary argument, and \(|I|\le(\sqrt{2p-1}+1)/2\) by Hanson–Petridis (external, quoted from memory).
3. **Subgroup laws (Proposition 2).** The exact subgroup laws are excluded on (NC): (NC) forces \(|H|=(1+o(1))\sqrt p\), and then Round 151, Round 184 Prop. 4 and the Round 20 energy gap each exclude them. They were never an obstruction below 7/4 in \(\mathbb F_p\) anyway: Macourt–Shkredov–Shparlinski give \(X(\mathbf 1_H)\ll p\log p\) (Round 189 audit).
4. **Sector reduction of \(T_0\) (Proposition 3; proved on (NC)).**
   \[
   T_0=c+T_0^{(\rho)}+T_0^{(-\rho)},\qquad 0\le T_0^{(-\rho)}\le G_{-\rho}\,c\le(\tfrac14+o(1))\,p,
   \]
   where \(T_0^{(\varepsilon)}=\sum_{\lambda\in T_\varepsilon}g(\lambda)\Delta(\lambda,0)\). This uses \(\Delta(\lambda,0)\le c\) (Cauchy–Schwarz).
   - Only triangle ratios in \(T_\rho\) matter. Every heavy triangle \(\{1,Y,Y'\}\) is then a Paley \(\rho\)-triangle.
   - This is a reduction at the target scale \(O(p)\). It is not a power saving on \(T_0^{(\rho)}\).
5. **Method cap for the non-sector consequences of (NC) (Theorem 4; proved).** Let \(0<\theta<\tfrac12\). The diluted-interval laws \(D_\theta\) take \(\nu\) uniform on a suitable \(\theta\)-dense subset of size \(\mathrm{round}(m_0)\) of an interval of length \(m_0/\theta\). For all large \(p\) they satisfy every accepted consequence of (NC) that does not encode the sector condition:
   - \(m_{\rm eff}/m_0\to1\), exact flatness, \(\nu_0=0\), the cap;
   - the energy cap \(\mathcal E(S)\le(\tfrac12+o(1))|S|^3\);
   - the overlap dichotomy of Round 184 Theorem 2 with \(H_*=\{0\}\);
   - Round 184 Prop. 4;
   - the Round 151 coset mass.

   They also have \(g\ge4/\pi^2-o(1)\) on \(I\cdot I^{-1}\) for \(I=\{\gamma^{2k}:|k|\le K\}\), \(|I|\approx\theta\sqrt p/2\), and \((4/\pi^2)^2\theta\sqrt p\,(1-o(1))\le\Gamma_{\rm tot}\le(\theta+o(1))\sqrt p\) (models: \(\approx\frac{2\theta}3\sqrt p\)).
   - So the Round 189 obstruction (\(T_0\ge(4/\pi^2-o(1))^5X(\mathbf 1_I)\)) and the \(\Gamma\)-route cap at \(43/24\) both extend to every argument that uses (NC) only through those consequences.
   - **The only (NC) input that can distinguish the actual law from the obstruction family is the sector condition \(V_{-\rho}\to0\)** (equivalently \(d_\rho(S)\to0\)).
6. **What the sector condition would need (§5, conditional).** By Theorem 1, the (NC)-version of the interval family consists of laws carried by **Paley cliques of geometric-progression form** of size \(\asymp\sqrt p\).
   - Excluding them is the arithmetic statement (GP-Sub): for every \(c>0\), eventually no \(\zeta\in Q\) has \(\chi(1-\zeta^k)\) constant for \(1\le k\le c\sqrt p\).
   - Hanson–Petridis gives (GP-Sub\(_c\)) only for \(c>1/\sqrt2\) (cliques of size \(>\sqrt{p/2}+1\)). The families \(D_\theta\) need only \(c\approx\theta/2<\tfrac14\).
   - I know no proof for small \(c\). Completing the character sum gives only the trivial \(\sqrt p\log p\).
   - Even (GP-Sub) for all \(c\) would exclude the family only qualitatively, and it gives no bound on \(T_0\), \(X\) or \(\Gamma_{\rm tot}\).
   - A power-rate version, (GP-Sub\(_\kappa\)) below, would weaken the obstruction by \(p^{5\kappa}\). It would still give no positive bound.
7. **Evidence (models; not certificates).**
   - Lemma 1 holds to \(10^{-15}\) relative error at \(p\le197\), both signs.
   - The \(D_\theta\) models at \(p\le10^6\) behave as Theorem 4 says. Their sector mass \(G_{-\rho}\approx G/2\), so they are far from (NC), as expected of random sets.
   - Geometric-progression Paley cliques are short. The longest run \(R(\zeta)\) with \(\chi(1-\zeta^k)\) constant, over generators \(\zeta\) of \(Q\), is at most \(1.69\log_2p\) for all 8897 primes \(p\equiv1\pmod4\) in \([10^3,2\cdot10^5]\), and \(25\) at \(p=3\cdot10^7\) (\(\sqrt p\approx5477\)). This is consistent with (GP-Sub), but it is finite evidence.

**X and \(\Gamma_2\), stated separately.** No new bound on \(X\), \(\Gamma_2\) or \(\Gamma_{\rm tot}\) is proved.
- On (NC), the accepted \(\Gamma_{\rm tot}=\sum g^2\le(\frac12+o(1))\sqrt p\) (Round 183 Prop. 1.4) stands. It gives covariance exponent exactly \(43/24\) through Round 188 Cor. B1, so no gain.
- Theorem 4 shows that no argument using only the non-sector (NC) consequences can bring \(\Gamma_{\rm tot}\) below \(c(\theta)\sqrt p\).
- \(X\): unchanged at \(p^{4/3+o(1)}\).

## Setup and hypotheses

Notation is that of Round 183 (row-deleted report, "Setup and hypotheses", lines 47–59), Round 184 (support-energy report, lines 32–45) and Round 189 (T0 report, lines 64–90). Counting norms are used on \(Q\). \(\|\cdot\|_{2,n}\) is the normalized norm on \(\widehat Q\), \(\|v\|_{2,n}^2=\frac1n\sum_j|v_j|^2\) (this is the reading under which Round 151's \(\|P_\sigma b\|_{2,n}=O(r)\) and Round 183's display \((2\|P_\sigma b\|^2+r^2)/\|b\|^2\) are consistent; under the counting reading every conclusion below holds a fortiori).

- \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(Q\) the squares, \(\chi\) the Legendre symbol, \(\widehat Q\cong\mathbb Z/n\) with characters \(\psi^j\), \(m_0=n/\sqrt p\), \(s(x)=\chi(1-x)\) on \(Q\) (\(s(1)=0\)), \(T_\varepsilon=\{x\in Q\setminus\{1\}:s(x)=\varepsilon\}\). Exactly \(|T_+|=(p-5)/4\) and \(|T_-|=(p-1)/4\).
- **Actual law** (Round 183 line 50; Round 184 line 36): \(b\ge0\) on \(\mathbb Z/n\), \(b_0=0\), \(r=\mathbb Eb\), \(\nu=b/\sum b\), \(f=\sum_j\nu_j\psi^j\) on \(Q\), \(g=|f|^2\), \(G=\sum g=n\|\nu\|_2^2=n/m_{\rm eff}\), \(G_\varepsilon=\sum_{T_\varepsilon}g\).
- **Operators** (Round 20 lines 9–11; Round 151 line 41; Round 184 line 35):
  - \(K_{ij}=k(i-j)/m_0\), which is multiplication by \(s\) in \(x\)-space;
  - \(J\) is the projection onto constants;
  - \(I-\rho K=2P_\sigma+J\);
  - \(\ell=P_\sigma e_0\) and \(L_\sigma=P_\sigma-\ell\ell^{\mathsf T}/\ell_0\), the orthogonal projection onto \(\operatorname{im}P_\sigma\cap e_0^\perp\).
- **(NC)** (Round 183 row-deleted report, line 53): \(\|L_\sigma b\|_{2,n}/r\to0\) and \(m_{\rm eff}/m_0\to1\) along the hypothetical sequence of primes; \(\rho=-\sigma\) is the favourable sign. I write (NC1) for \(m_{\rm eff}/m_0\to1\) (equivalently \(G/\sqrt p\to1\)) and (NC2) for \(\|L_\sigma b\|_{2,n}/r\to0\).
- **Accepted (NC) consequences used or tested** (status from `round-183/184-acceptance.json` `proof_scope`):
  - (A1) Round 20 flattening, lines 74–76 (with Round 151 line 47): \(e=\nu/\|\nu\|_2=u_S+o_{\ell^2}(1)\), \(|S|=(1+o(1))m_0\), and the signed \(S\times S\) deficit \(d_\rho(S)\to0\).
  - (A2) Round 20 gap theorem, lines 66–76, in the form of Round 183 Prop. 1.4 (lines 104–120): \(\sum g^2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\le\frac12+o(1)\).
  - (A3) Round 183 Prop. 1.2 (lines 76–91): \(G_{-\rho}=O(1)\), \(G=(1+o(1))\sqrt p\), \(M_1=(1+o(1))p\).
  - (A4) Round 151 coset mass (line 47; acceptance item 3): \(t_B\ge c_0>0\) for bounded unions \(B\) of cosets of subgroups of size \(\asymp\sqrt p\).
  - (A5) Round 184 Lemma 0 (lines 49–60) and Theorem 2 (lines 79–112): the overlap dichotomy \((1-q_a)(2q_a-1)\le o(1)\), \(H_*\) a subgroup of order \(o(m_0)\), \(\max_{a\notin H_*}\widehat g(a)\le(\frac12+o(1))G\).
  - (A6) Round 184 Prop. 4 (lines 148–165): single-coset configurations.
- **Round 189 objects** (T0 report lines 72–79): \(\mu(r,b)=g(Y)g(D)\), \(\Delta(\lambda,0)=\sum_{r,b}\mu(r,b)\mu(\lambda r,b)\), \(T_0=\sum_\lambda g(\lambda)\Delta(\lambda,0)\), \(X=\sum_\lambda\Delta(\lambda,0)=\Lambda_0\), \(c=\sum\mu^2=\Delta(1,0)\), and Proposition 3(b): if \(g\ge\tau\) on \(I\cdot I^{-1}\) (\(I=I^{-1}\)), then \(T_0\ge\tau^5X(\mathbf 1_I)\).
- **External statements.** Hanson–Petridis (clique number of the Paley graph \(\le(\sqrt{2p-1}+1)/2\); B. Hanson and G. Petridis, *Refined estimates concerning sumsets contained in the roots of unity*, Proc. LMS 2021, arXiv:1905.09134) is **quoted from memory, not read at source in this call**. It is used only in remarks; the elementary bound \(|I|\le\sqrt p\) (Lemma 2) is proved here and suffices for every proved statement.

## 1. The exact form of the near-critical defect (Lemma 1; proved, any law)

**Lemma 1.** For any \(b\ge0\) with \(b_0=0\) and \(r>0\), and either sign \(\rho\) (with \(P_\sigma=(I-J-\rho K)/2\)):
\[
\frac{\|P_\sigma b\|_{2,n}^2}{r^2}=G_{-\rho},\qquad
\frac{\|L_\sigma b\|_{2,n}^2}{r^2}=V_{-\rho}=\sum_{x\in T_{-\rho}}|f(x)-\bar f_{-\rho}|^2,\qquad
\Bigl|\sum_{x\in T_{-\rho}}f(x)\Bigr|\le\frac{\sqrt p+1}2 ,
\]
with \(\bar f_{-\rho}=|T_{-\rho}|^{-1}\sum_{T_{-\rho}}f\). Hence
\[
G_{-\rho}=V_{-\rho}+|T_{-\rho}|\,|\bar f_{-\rho}|^2\le V_{-\rho}+\frac{(\sqrt p+1)^2}{p-5},\qquad |\bar f_{-\rho}|\le\frac{2(\sqrt p+1)}{p-5}.
\]

*Proof.*
1. **The transform.** Write \(\hat v(x)=\sum_jv_j\psi^j(x)\) for \(x\in Q\). Then \(\hat b=nrf\), and Parseval reads \(\sum_j|v_j|^2=\frac1n\sum_{x\in Q}|\hat v(x)|^2\).
2. **The multipliers.** \(K\) acts as multiplication by \(s\) (Round 184 line 35). \(J\) acts as multiplication by \(\mathbf 1_{x=1}\), since a constant vector transforms to a multiple of \(\mathbf 1_{x=1}\). So \(P_\sigma=(I-J-\rho K)/2\) is multiplication by \((1-\mathbf 1_{x=1}-\rho s)/2\). This equals \(0\) at \(x=1\) (where \(s(1)=0\)) and on \(T_\rho\), and \(1\) on \(T_{-\rho}\). So \(P_\sigma\) is the Fourier projection onto \(T_{-\rho}\).
3. **The projection \(L_\sigma\).** The condition \(v\perp e_0\) means \(v_0=\frac1n\sum_x\hat v(x)=0\). So \(\operatorname{im}P_\sigma\cap e_0^\perp\) consists of the \(v\) with \(\hat v\) supported on \(T_{-\rho}\) and summing to 0. The orthogonal projection onto it (Round 20 line 11) sends \(\hat b\) to \(\mathbf 1_{T_{-\rho}}(\hat b-\overline{\hat b}_{-\rho})\).
4. **The norms.** By Parseval,
   \[\|L_\sigma b\|_{2,n}^2=\frac1{n^2}\sum_{T_{-\rho}}|nr(f-\bar f_{-\rho})|^2=r^2V_{-\rho}.\]
   The same computation gives \(\|P_\sigma b\|^2_{2,n}=r^2G_{-\rho}\).
5. **The sum over \(T_{-\rho}\).** For \(j\ne0\),
   \[\sum_{x\in T_{-\rho}}\psi^j(x)=\tfrac12\Bigl(-1-\rho\sum_{x\in Q}s(x)\psi^j(x)\Bigr).\]
   The inner sum is \(\sqrt p\,k(\pm j)\) with \(|k|\le1\) (Round 184 line 35; it is half a sum of two Jacobi sums, each of modulus \(\sqrt p\)). Since \(\nu_0=0\) and \(\sum\nu=1\), \(|\sum_{T_{-\rho}}f|\le(\sqrt p+1)/2\).
6. **The last display.** \(\sum_{T}|f|^2=\sum_T|f-\bar f|^2+|T||\bar f|^2\), together with \(|T_{-\rho}|\ge(p-5)/4\). \(\square\)

*Check.* `paley-190-nc-identity.py --check` builds \(K\) from its definition and verifies \(K^2=I-J\) (Round 184 line 35), \(P_\sigma^2=P_\sigma\), the identity \(\|L_\sigma b\|_{2,n}^2/r^2=V_{-\rho}\) (relative error \(\le2.7\cdot10^{-15}\)) and the sum bound. The checks run at \(p=13,\dots,197\), both signs, five random \(b\) each.

**Reading.** (NC) is exactly:
- (NC1) \(G\sim\sqrt p\);
- (NC2) \(f\) is asymptotically constant, with constant \(O(p^{-1/2})\), on the unfavourable sector, in \(\ell^2(T_{-\rho})\).

The \(\mathbb F_{r^2}\) control (Round 184 slope-row-mass report, line 217) is exactly critical: there \(f\equiv-2/(r-1)\) on \(Q\setminus\mathbb F_r^\times\supseteq T_-\), so \(V_-=0\) and \(G_-\to1\).

## 2. Consequences of (NC2) for the obstruction families

### Theorem 1 (pointwise sector exclusion; (NC))
Put \(\tau_p:=\sup_{x\in T_{-\rho}}g(x)\). On (NC):
1. \(\tau_p\le\bigl(V_{-\rho}^{1/2}+2(\sqrt p+1)/(p-5)\bigr)^2\to0\).
2. \(G_{-\rho}\le1+o(1)\). The constant is sharp in the field-general sense: the \(\mathbb F_{r^2}\) control has \(G_-=1.043\) at \(r=47\), tending to 1 (Round 184 SRM Prop. 5(b)).
3. For every \(\tau>0\), \(\#\{x\in T_{-\rho}:g(x)\ge\tau\}\le G_{-\rho}/\tau\le(1+o(1))/\tau\). This holds for every \(\tau\), including \(\tau=p^{-1/24-\delta}\); it is the only quantitative form, since (NC) carries no rate.
4. For every fixed \(\tau>0\), eventually \(\{x\in Q:g(x)\ge\tau\}\subseteq T_\rho\cup\{1\}\).

*Proof.* Item 1: a single term of \(V_{-\rho}\) is at most \(V_{-\rho}\), and \(|\bar f_{-\rho}|\) is bounded by Lemma 1. Item 2 is Lemma 1. Item 3 is Markov's inequality. Item 4 follows from 1. \(\square\)

### Lemma 2 (sector-concentrated progressions are Paley cliques; any \(p\equiv1\bmod4\))
Let \(\zeta\in Q\) have order \(>4K\) and \(I=\{\zeta^k:|k|\le K\}\). Suppose \(\chi(1-y)=\rho\) for every \(y\in I\cdot I^{-1}\setminus\{1\}\). Then:
- \(\chi(x-x')=\rho\) for all distinct \(x,x'\in I\). So \(I\) is a clique of the Paley graph (\(\rho=1\)) or of its complement (\(\rho=-1\)), of size \(2K+1\).
- \(|I|\le\sqrt p\).

Conversely, \(\{\zeta^k:0\le k\le M\}\) is such a clique iff \(\chi(1-\zeta^k)=\rho\) for \(1\le k\le M\).

*Proof.*
- **Clique.** \(x-x'=x(1-x'/x)\), with \(\chi(x)=1\) and \(x'/x\in I\cdot I^{-1}\setminus\{1\}\).
- **Size bound.** Let \(A=I\) and fix a nonsquare \(\nu\). If \(a+\nu b=a'+\nu b'\) with \((a,b)\ne(a',b')\) in \(A^2\), then \(a\ne a'\) and \(b\ne b'\), and \(a-a'=\nu(b'-b)\). The left side has character \(\rho\) and the right side \(-\rho\), a contradiction. So \((a,b)\mapsto a+\nu b\) is injective and \(|A|^2\le p\).
- **Converse.** The same factorization. \(\square\)

(Hanson–Petridis improves \(\sqrt p\) to \((\sqrt{2p-1}+1)/2\); quoted from memory, not used in any proof here.)

### Corollary 1.1 (the (NC)-version of the interval family)
On (NC), fix \(\tau>0\) and suppose the actual \(g\) satisfies \(g\ge\tau\) on \(I\cdot I^{-1}\) for some \(I=\{\zeta^k:|k|\le K\}\) with \(\operatorname{ord}\zeta>4K\) (the hypothesis of Round 189 Prop. 3(b)). Then, for large \(p\):
- \(I\) is a Paley \(\rho\)-clique;
- \(|I|\le\sqrt p\);
- \(\chi(1-\zeta^k)=\rho\) for \(1\le k\le2K\).

The exact interval law of Round 189 Prop. 3(c), with \(\tau\le0.11\), has such \(I\) of size about \(0.72\sqrt p>(\sqrt{2p-1}+1)/2\) (since \(F_L(k)\ge(\sin\pi x/\pi x)^2\ge0.116\) at \(x=L|k|/n\le0.72\)), so it is excluded under Hanson–Petridis. It is excluded anyway by (A2), since \(\mathcal E(J)/|J|^3\to\frac23>\frac12\), and by (A5), since an interval has overlaps \(1-|a|/L\in(\frac12,1)\).

*Proof.* Theorem 1(4) and Lemma 2. \(\square\)

### Proposition 2 (subgroup laws on (NC))
Let \(\nu\) be uniform on \(H^\perp\setminus\{0\}\) for a subgroup \(H\le Q\) of order \(d\) (removing \(0\) enforces \(b_0=0\); then \(g=\bigl((n/d)\mathbf 1_H-1\bigr)^2/(n/d-1)^2\), which is \(\mathbf 1_H\) up to \(O(d^2/n^2)\) off \(H\)).
1. (NC1) forces \(G=d\,(1+o(1))=(1+o(1))\sqrt p\).
2. Such laws violate:
   - (A4), since \(t_H=O(d/n)\to0\);
   - (A6), since \(S=H^\perp\setminus\{0\}\) is a subgroup of \(\mathbb Z/n\) of order \(\sim m_0<(2-\delta)m_0\), minus a point;
   - (A2), since the energy ratio of that subgroup is 1.
3. Hence they are excluded on (NC).
4. The weaker hypothesis "\(g\ge\tau\) on \(H\)" is not excluded by (A4) or (A6). On (NC) it forces \(H\setminus\{1\}\subseteq T_\rho\), so \(H\) is a subgroup Paley clique, impossible for \(|H|>\sqrt{p/2}+1\) by Hanson–Petridis.
5. **Irrelevance below 7/4.** Subgroup-type pieces are not an obstruction in \(\mathbb F_p\) anyway. Through Round 189 Prop. 3(b) they give at most \(T_0\ge\tau^5X(\mathbf 1_H)\), and \(X(\mathbf 1_H)\le E^\times(\mathbf 1_{1-H})\ll p\log p\) for \(|H|\asymp\sqrt p\) (Round 184 SRM Prop. 4; Macourt–Shkredov–Shparlinski Cor. 4.1 as read at source in the Round 189 audit §2.4).

*Proof.* (1) Round 183 Prop. 1.1, \(G=n\|\nu\|_2^2=n/(n/d-1)\). (2) As stated, with Round 184 Prop. 4.4(a) and Round 183 Prop. 1.4. (4) Theorem 1(4) and Lemma 2 with \(I=H\). \(\square\)

## 3. Sector reduction of \(T_0\) (Proposition 3; proved on (NC))

**Proposition 3.** For any \(0\le g\le1\) on \(Q\) with \(g(1)=1\), write \(T_0=c+T_0^{(\rho)}+T_0^{(-\rho)}\) with \(T_0^{(\varepsilon)}=\sum_{\lambda\in T_\varepsilon}g(\lambda)\Delta(\lambda,0)\). Then, for every \(\lambda\),
\[
0\le\Delta(\lambda,0)\le c,\qquad 0\le T_0^{(-\rho)}\le\min\bigl\{G_{-\rho}\,c,\ \tau_p\,(X-c)\bigr\}.
\]
On (NC):
\[
T_0^{(-\rho)}\le(1+o(1))\,c\le(\tfrac14+o(1))\,p\qquad\text{and}\qquad T_0^{(-\rho)}=o(X).
\]
So \(T_0-c-T_0^{(\rho)}=O(p)\), the target scale.

*Proof.*
- **\(\Delta\le c\).** Cauchy–Schwarz in \((r,b)\) gives \(\Delta(\lambda,0)\le(\sum\mu(r,b)^2)^{1/2}(\sum\mu(\lambda r,b)^2)^{1/2}=c\), since \(r\mapsto\lambda r\) is a bijection.
- **The split.** \(g\) vanishes off \(Q\), \(Q=\{1\}\sqcup T_+\sqcup T_-\), and \(\Delta(1,0)=c\). Also \(\sum_{\lambda\ne1}\Delta(\lambda,0)=X-c\) (Round 189 audit §2.2).
- **On (NC).** Theorem 1 gives \(G_{-\rho}\le1+o(1)\) and \(\tau_p\to0\). Also \(c\le(\sum g^2)^2\le(\frac14+o(1))p\) (Round 183 lines 127 and 104–120). \(\square\)

**What it gives.**
- In the heavy-triangle reduction (Round 189 Prop. 5), beating 43/24 needs only
  \[\sum_{\lambda\in T_\rho,\ g(\lambda)\ge p^{-1/24-\delta}}g(\lambda)\Delta(\lambda,0)\le p^{31/24-\delta'}.\]
- In that sum both \(Y,Y'\) of a heavy term may be taken heavy. Then \(\{1,Y,Y'\}\) is a Paley \(\rho\)-triangle: \(\chi(1-Y)=\chi(1-Y')=\chi(Y-Y')=\rho\).
- This is a structural restriction, not a power saving. On sector-concentrated laws (all of \(\operatorname{supp}g\) in \(T_\rho\)) a generic pair already has \(\lambda\in T_\rho\) with probability about \(\frac12\). It removes only the \(T_{-\rho}\) part, which is \(O(p)\).
- *Not proved here:* an analogous sector reduction of \(X\) (energy of \(h=g(1-\cdot)\)). The \(T_{-\rho}\) part of \(h\) has \(\ell^1\)-mass \(\le1+o(1)\) and sup \(o(1)\), so its contribution is of lower order, but I did not write out the masked cross terms.

## 4. The non-sector consequences of (NC) do not see the interval obstruction (Theorem 4; proved)

**The family \(D_\theta\).** Fix \(0<\theta<\frac12\). Let \(m=\mathrm{round}(m_0)\), \(L'=\mathrm{round}(m/\theta)\), and \(J'=[a_0,a_0+L')\subset\mathbb Z/n\) an interval with \(0\notin J'\). Let \(S\subset J'\), \(|S|=m\), and \(\nu=\mathbf 1_S/m\). Let \(D_{L'}(k)=\frac1{L'}\sum_{j\in J'}e(jk/n)\), so that \(|D_{L'}|^2=F_{L'}\) is the Fejér kernel of Round 189 Prop. 3(c), and \(f(\gamma^{2k})-\frac{\theta L'}m D_{L'}(k)=\frac1m\sum_{j\in J'}(\mathbf 1_S(j)-\theta)e(jk/n)\).

**Theorem 4.** For all large \(p\) there is \(S\) (indeed a uniformly random \(m\)-subset of \(J'\) works with probability \(1-o(1)\)) such that the law \(\nu=\mathbf 1_S/m\) satisfies:
1. **Admissibility.** \(\nu\) is a probability, \(\nu_0=0\), the cap holds (\(n\max\nu=n/m=(1+o(1))\sqrt p\)), \(\omega\ge0\) and (H3) hold.
2. **(NC1).** \(m_{\rm eff}/m_0\to1\) and \(G/\sqrt p\to1\).
3. **(A1) without its sector part.** The flattening holds exactly: \(e=u_S\), \(|S|\sim m_0\).
4. **(A2).** \(\mathcal E(S)\le(\theta+o(1))|S|^3<\frac12|S|^3\), so \(\Gamma_{\rm tot}=\sum g^2=(\mathcal E(S)/|S|^3)\sqrt p\,(1+o(1))<\frac12\sqrt p\). The Round 20 gap hypothesis fails, so the gap theorem imposes nothing.
5. **(A5) conclusions.** \(\max_{a\ne0}r_S(a)\le\theta+o(1)<\frac12\). So the dichotomy holds, \(H_*=\{0\}\), item 3 of Theorem 2 is vacuous, and \(\max_{a\ne0}\widehat g(a)/G\le\theta+o(1)\).
6. **(A6) conclusions.** Every coset of every subgroup of \(\mathbb Z/n\) of order \(\le2m_0\) contains \(O(1/\theta)=o(|S|)\) points of \(S\).
7. **(A4).** For every bounded union \(B\) of cosets of multiplicative subgroups of order in \([c_1\sqrt p,c_2\sqrt p]\), \(t_B\to1\).
8. **The obstruction.** \(g\ge4/\pi^2-o(1)\) on \(I\cdot I^{-1}\), where \(I=\{\gamma^{2k}:|k|\le\lfloor n/(4L')\rfloor\}\), \(|I|=(1+o(1))\theta\sqrt p/2\). Hence, by Round 189 Prop. 3(b),
   \[T_0(g)\ge(4/\pi^2-o(1))^5\,X(\mathbf 1_I).\]
9. **\(\Gamma_{\rm tot}\) is large.** \(\Gamma_{\rm tot}\ge\sum_{I\cdot I^{-1}}g^2\ge(4/\pi^2-o(1))^2\,\theta\sqrt p\,(1-o(1))\), so \(\Gamma_{\rm tot}\asymp\sqrt p\).

*Proof.*
- **Items 1–3** are immediate: \(\nu\) is real, so \(g(1/x)=g(x)\); \(\omega=\frac12\nu*\check\nu\ge0\) (Round 188 Theorem A hypotheses); and \(G=n/m\).
- **Concentration.** For each fixed \(x\) and each fixed shift \(a\), the sums \(\sum_{j\in J'}(\mathbf 1_S(j)-\theta)e(jk/n)\) and \(|S\cap(S+a)|\) are Lipschitz functions of a uniformly random \(m\)-subset, with constant \(O(1)\) under a swap of two elements. McDiarmid's inequality for random subsets of fixed size, with a union bound over the \(n\) points \(x\) and the \(n\) shifts \(a\), therefore gives with probability \(1-o(1)\):
  - \(\sup_x|f(x)-\tfrac{\theta L'}mD_{L'}|=O(\sqrt{\log p/m})=o(1)\), where \(\theta L'/m=1+o(1)\);
  - \(\max_a\bigl||S\cap(S+a)|-\theta^2(L'-|a|)_+\bigr|=O(\sqrt{m\log p})\).
- **Item 5.** \(\theta^2(L'-|a|)\le\theta m\).
- **Item 4.** \(\mathcal E(S)=m^2+\sum_{a\ne0}|S\cap(S+a)|^2\le m^2+(\theta+o(1))m\cdot m^2\); then use Round 183 Prop. 1.1.
- **Item 8.** \(F_{L'}\ge4/\pi^2\) on \(|k|\le n/(2L')\) (Round 189 Prop. 3(c), audited), and \(I\cdot I^{-1}\subseteq\{|k|\le n/(2L')\}\). Since \(n/(2L')=(1+o(1))\theta\sqrt p/2\), we get \(|I|=(1+o(1))\theta\sqrt p/2\).
- **Item 6.** A coset of the subgroup of order \(e\le2m_0\) is an arithmetic progression of step \(n/e\ge n/(2m_0)=\sqrt p/2\). It meets \(J'\) (length \(L'\approx\sqrt p/(2\theta)\)) in at most \(1/\theta+1\) points.
- **Item 7.**
  - A coset \(aH\), \(|H|=d\), is in log-coordinates an arithmetic progression of step \(s=n/d\ge(1+o(1))\sqrt p/(2c_2)\).
  - Use \(|D_{L'}(k)|\le\min(1,n/(2L'|k|))\). Then \(\sum_{k\in\text{AP}}|D_{L'}(k)|^2\le1+2\sum_{t\ge1}(n/(2L'ts))^2=O(1+(d/L')^2)=O(1+c_2^2\theta^2)\).
  - So \(\sum_Bg\le2\sum_B|D|^2+2|B|\sup|f-D|^2=O(1)+o(\sqrt p)=o(G)\).
- **Item 9.** \(|I\cdot I^{-1}|=(1+o(1))\theta\sqrt p\). \(\square\)

**Corollary 4.1 (method cap; proved).** Let \(\mathcal H\) be the hypothesis set consisting of:
- probability, \(\nu_0=0\), the cap, \(\omega\ge0\), (H3);
- (NC1);
- exact or approximate flatness;
- the conclusions of (A2), (A4), (A5) and (A6).

Then:
- (i) Any argument that uses only \(\mathcal H\) and proves \(T_0\le Cp^{5/4-\delta}\) (or \(X\le Cp^{5/4-\delta}\)) proves \(X(\mathbf 1_I)\le(\pi^2/4+o(1))^5Cp^{5/4-\delta}\) for every symmetric geometric progression \(I=\{\gamma^{2k}:|k|\le K\}\), \(\gamma\) a generator, \(K\le(\frac18-\epsilon)\sqrt p\) (so \(|I|\) up to about \(\sqrt p/4\)). This is (GP) at \(|I|\asymp\sqrt p\) (`cand:gp-shifted-energy`), up to the factor 16 of the masked-to-unmasked step (Round 189 audit §2.4).
- (ii) No argument from \(\mathcal H\) bounds \(\Gamma_{\rm tot}\) by \(o(\sqrt p)\). So the \(\Gamma\) route, through Round 188 Cor. B1, cannot pass \(43/24\) from \(\mathcal H\).
- (iii) Consequently every (NC)-based route below \(7/4\) must use (NC2): the sector condition \(V_{-\rho}\to0\), or one of its accepted forms (A3), Round 184 Lemma 0, \(d_\rho(S)\to0\).

*Proof.* Theorem 4 and Round 189 Prop. 3(b). \(\square\)

This agrees with Round 184 SRM §7 (lines 338–342), which observed for the `aphalf` model that the energy gap and the coset mass leave such configurations open. Theorem 4 adds that the overlap dichotomy and Round 184 Prop. 4 leave them open too, and it applies to the \(T_0\) obstruction of Round 189.

## 5. What the sector condition would have to supply (conditional criteria)

By Theorem 1 and Lemma 2, a law that satisfies (NC) and belongs to the Round 189 interval family must be carried, at heights \(\ge\tau\), by a Paley \(\rho\)-clique of geometric-progression form, of size \(|I|\asymp\sqrt p\). Define, for \(\zeta\in Q\setminus\{1\}\),
\[
R(\zeta)=\max\{R:\ \chi(1-\zeta^k)=\chi(1-\zeta)\ \text{for }1\le k\le R\}\qquad(\le\operatorname{ord}\zeta-1).
\]

**(GP-Sub\(_c\)).** For all large primes \(p\equiv1\pmod4\), every \(\zeta\in Q\) with \(\operatorname{ord}\zeta>c\sqrt p\) has \(R(\zeta)<c\sqrt p\).

**(GP-Sub\(_\kappa\)), quantitative.** There are \(\kappa>0\) and \(c_0>0\) such that, for all large \(p\), every symmetric progression \(P=\{\zeta^k:|k|\le M\}\subset Q\) with \(c_0\sqrt p\le M<\operatorname{ord}\zeta/2\) satisfies \(\#\{y\in P:\chi(1-y)=\varepsilon\}\ge p^\kappa\) for both \(\varepsilon=\pm1\).

**Criterion 5.1 (qualitative exclusion; conditional on (GP-Sub\(_c\)) for all \(c>0\)).** On (NC), for every fixed \(\tau,c>0\), eventually no symmetric geometric progression \(I\) with \(|I|\ge c\sqrt p\) and \(\operatorname{ord}\zeta>4K\) has \(g\ge\tau\) on \(I\cdot I^{-1}\). That is, the Round 189 interval family (with fixed \(\tau\)) is excluded on (NC).
- *Proof.* Corollary 1.1 gives \(R(\zeta)\ge2K\ge c\sqrt p-1\). \(\square\)
- *Status.* (GP-Sub\(_c\)) is true for \(c>1/\sqrt2\) by Lemma 2 with Hanson–Petridis: the clique \(\{\zeta^k:0\le k\le R(\zeta)\}\) has \(R(\zeta)+1\le(\sqrt{2p-1}+1)/2\). The elementary bound of Lemma 2 gives \(c>1\). For \(c\le1/\sqrt2\) I know no proof. The families \(D_\theta\) need \(c\approx\theta/2<\frac14\), since \(R(\gamma^2)\ge2K\approx|I|\approx\theta\sqrt p/2\).
  - Completing \(\sum_{k\le M}\chi(1-\zeta^k)\) over the multiplicative characters gives \(O(\sqrt p\log p)\), which is trivial at \(M\asymp\sqrt p\).
  - Stepanov's method needs a subgroup; the Round 184 statement (Sub\(_C\)) is its subgroup analogue and is also open for \(|B|\asymp\sqrt p\).
  - Any \(o(\sqrt p)\) bound for the clique number of the Paley graph would imply (GP-Sub\(_c\)) for every \(c\); no such bound is known to me.
  - *To be checked at source by a literature call:* character sums \(\sum_{k\le M}\chi(1-\zeta^k)\) or \(\chi(\zeta^k+a)\) at \(M\asymp\sqrt p\), and Paley cliques of geometric-progression form.

**Criterion 5.2 (quantitative weakening; conditional on (GP-Sub\(_\kappa\))).** On (NC), if \(g\ge\tau\) on \(I\cdot I^{-1}\) with \(|I|\ge c_0\sqrt p\), then \(\tau\le(1+o(1))p^{-\kappa}\). So the interval-type lower bound of Round 189 Prop. 3(b) becomes \(T_0\ge\tau^5X(\mathbf 1_I)\) with \(\tau^5\le p^{-5\kappa}\).
- With MPRRS Lemma 33 (\(X(\mathbf 1_I)\ll|I|^{5/2}=p^{5/4}\)), the family then no longer obstructs \(T_0\le p^{5/4-\delta}\) for \(\delta<5\kappa\).
- *Proof.* Theorem 1(3): \(p^\kappa\tau\le\sum_{P\cap T_{-\rho}}g\le G_{-\rho}\le1+o(1)\). \(\square\)
- *This removes an obstruction; it proves nothing.* Lower-height sector laws, with \(g\approx p^{-\kappa}\) on longer progressions, still need their own analysis.

**What a usable bound would need (stated exactly).**
1. **For \(T_0\) (heavy-triangle part).** An (NC)-input that bounds
   \[\sum_{\lambda\in T_\rho,\ g(\lambda)\ge p^{-1/24-\delta}}g(\lambda)\Delta(\lambda,0)\]
   by \(p^{31/24-\delta'}\) (beats 43/24) or by \(p^{5/4-\delta'}\) (with the light part, below 7/4). By Corollary 4.1 such an input must use (NC2). By Corollary 1.1, on the sector side it must control the weighted Paley-triangle counts of the heavy level sets of \(g\) inside \(T_\rho\). The minimal arithmetic content is (GP-Sub\(_\kappa\)) with \(5\kappa>\delta\), together with a positive estimate for the non-progression part. No accepted statement supplies either.
2. **For \(X\).** The same, with \(X\) in place of \(T_0\) (Round 189: \(X(g)\ge\tau^4X(\mathbf 1_I)\) on these families).
3. **For \(\Gamma_{\rm tot}\).** On (NC), \(\Gamma_{\rm tot}=(\mathcal E(S)/|S|^3+o(1))\sqrt p\). The thresholds \(p^{11/24-\delta}\) (beats 43/24) and \(p^{5/12-\delta}\) (below 7/4) therefore need \(\mathcal E(S)\le|S|^3p^{-1/24-\delta}\), respectively \(\le|S|^3p^{-1/12-\delta}\): a **power-rate** low-energy statement for the near-critical support.
   - By Corollary 4.1(ii) this needs (NC2).
   - Along the route of Round 184 Criterion C2 it needs a quantitative inverse theorem (energy \(p^{-\eta}|S|^3\) gives a dense piece on a bounded-rank coset progression, with polynomial losses), together with (GP-Sub\(_\kappa\))-type bounds for multiplicative Bohr sets at the resulting density.
   - (NC) itself has no rate, so the power must come entirely from the arithmetic input.

## 6. Bounds on \(T_0\), \(X\), \(\Gamma_{\rm tot}\) (reported separately, as asked)

| quantity | before this call | after this call | how |
|---|---|---|---|
| \(T_0\) | \(T_0\le X\ll p^{4/3+o(1)}\); heavy-triangle reduction at \(p^{-1/24-\delta}\) | unchanged exponent. On (NC): \(T_0=c+T_0^{(\rho)}+O(p)\); only \(\lambda\in T_\rho\) matters (Prop. 3) | sector reduction; no power |
| \(X\) | \(p^{4/3+o(1)}\) (Round 187) | unchanged | — |
| \(\Gamma_{\rm tot}=\sum g^2\), \(\Gamma_2=\Gamma_{\rm tot}-1\) | on (NC) \(\le(\frac12+o(1))\sqrt p\) (Round 183) | unchanged. Under \(\mathcal H\) alone it cannot be \(o(\sqrt p)\) (Cor. 4.1(ii)) | covariance exponent \(43/24\) at \(\gamma=\frac12\) (exact, Fractions) |
| \(G_{-\rho}\) | \(O(1)\) (Round 183) | \(\le1+o(1)\), sharp (Theorem 1) | Lemma 1 |
| \(\sup_{T_{-\rho}}g\) | — | \(\to0\) (Theorem 1) | Lemma 1 |

Exponent arithmetic (`paley-190-nc-exponents.py`, `ALL OK`):
- \(\frac12+\frac{31}{24}=\frac{43}{24}\) and \(\frac12+\frac54=\frac74\);
- \(\min(1+2\gamma,\gamma+\frac43,\frac{43}{24})\) equals \(\frac{43}{24}\) at \(\gamma=\frac{11}{24}\) and at \(\gamma=\frac12\), and \(\frac74\) at \(\gamma=\frac5{12}\);
- \(-\frac1{24}+\frac43=\frac{31}{24}\);
- the sector remainder exponent is \(1<\frac54<\frac{31}{24}\);
- \(|I|^{5/2}=p^{5/4}\);
- \(\frac54-5\kappa<\frac54\).

## 7. Evidence (finite; models; not certificates)

### 7.1 Diluted-interval models (`paley-190-nc-identity.py P`, floating)
\(\nu\) is uniform on a random \(m\)-subset of an interval of length \(m/\theta\). For each \(\rho\) the table gives \(G_{-\rho}\), \(V_{-\rho}\), and "bad", the number of points of the progression \(\{|k|\le K\}\) lying in \(T_{-\rho}\). Here \(K=\lfloor n/(2L')\rfloor\approx\theta\sqrt p/2\), so \(\{\gamma^{2k}:|k|\le K\}=I\cdot I^{-1}\) for the progression \(I\) of Theorem 4, which has \(|I|\approx K\).

| \(p\) | \(\theta\) | \(\mathcal E/|S|^3\) | \(\max_{a\ne0}r_S\) | \(\Gamma_{\rm tot}/\sqrt p\) | \(K/\sqrt p\) | \(\min g\) on \(\{|k|\le K\}\) | coset frac \(\mathbb Z/n\) | coset mass \(Q\) | \(\rho=+1\): \(G_{-\rho}\), bad | \(\rho=-1\): \(G_{-\rho}\), bad |
|---|---|---|---|---|---|---|---|---|---|---|
| 10009 | 1.00 | 0.667 | 0.980 | 0.667 | 0.500 | 0.406 | 0.020 | 0.056 | 42.7, 38/100 | 56.4, 62/100 |
| 10009 | 0.25 | 0.198 | 0.380 | 0.198 | 0.120 | 0.461 | 0.040 | 0.056 | 48.5, 12/24 | 50.6, 12/24 |
| 160001 | 0.50 | 0.338 | 0.520 | 0.338 | 0.250 | 0.410 | 0.010 | 0.020 | 186.5, 86/200 | 212.5, 114/200 |
| 160001 | 0.25 | 0.166 | 0.290 | 0.166 | 0.125 | 0.360 | 0.015 | 0.020 | 189.7, 40/100 | 209.3, 60/100 |
| 1000033 | 0.50 | 0.331 | 0.512 | 0.331 | 0.250 | 0.396 | 0.004 | 0.008 | 507.4, 250/500 | 491.6, 250/500 |
| 1000033 | 0.25 | 0.170 | 0.280 | 0.170 | 0.125 | 0.409 | 0.008 | 0.008 | 500.3, 122/250 | 498.7, 128/250 |

Reading (models only):
- \(\theta=1\) is the exact interval law: energy \(\frac23\) and overlaps near 1, both excluded on (NC).
- For \(\theta\le\frac12\) the energy is about \(\frac23\theta\), the maximal overlap about \(\theta\) (at \(\theta=\frac12\) the finite-\(p\) fluctuation puts it at 0.51–0.57; Theorem 4 uses \(\theta<\frac12\)), the coset fractions and masses tend to 0, and \(g\ge0.36\) on the whole progression.
- The sector condition fails massively: \(G_{-\rho}\approx G/2\), \(V_{-\rho}\approx G_{-\rho}\), and about half the progression lies in \(T_{-\rho}\). This is what random \(S\) must do. It is no evidence about the hypothetical (NC) sequence.
- Other rows (\(p=40009\), \(640009\); \(\theta=0.75\)) are in the script output and show the same pattern.

### 7.2 Geometric-progression Paley cliques (`paley-190-nc-gpclique.py`, exact integers)

| range / prime | primes | max \(R\) over generators \(\zeta\) of \(Q\) | max \(R\) over all \(\zeta\in Q\setminus1\) | \(\max R_{\rm gen}/\log_2p\) | mean \(R_{\rm gen}/\log_2p\) |
|---|---|---|---|---|---|
| \(p\in[10^3,10^4)\) | 529 | 17 (\(\le0.283\sqrt p\), at \(p=1013\)) | 23 (\(p=9601\)) | 1.30 | 0.78 |
| \([10^4,5\cdot10^4)\) | 1940 | 23 | 29 | 1.52 | 0.85 |
| \([5\cdot10^4,10^5)\) | 2234 | 28 | 29 | 1.69 | 0.87 |
| \([10^5,2\cdot10^5]\) | 4194 | 28 | 33 | 1.59 | 0.88 |
| 640009 / 1000033 / 4000037 / 10000121 / 30000001 | 5 | 18 / 18 / 22 / 22 / 25 | 20 / 18 / 24 / 22 / 25 | ≤1.0 | — |

Reading:
- Over generators, the longest sector-constant run grows like \(\log_2p\) (mean ratio \(\approx0.85\), max \(\le1.7\)). That is the random heuristic: \(n\) runs, each geometric with parameter \(\frac12\).
- At \(p=3\cdot10^7\) the longest run is \(25\), against \(\sqrt p\approx5477\) and the Hanson–Petridis bound \(3874\).
- Over all \(\zeta\), the record values (e.g. \(R=23\) at \(p=9601\), the Round 184 example \(b=24\)) come from small subgroups that are entire Paley cliques.
- So progression cliques of size \(c\sqrt p\), which the (NC)-version of the interval family needs, do not occur at these primes. This supports (GP-Sub\(_c\)) as a heuristic. It is finite evidence and says nothing about every large \(p\).
- `--check` confirms the vectorized run lengths and the clique property of Lemma 2 by brute force for all \(p\equiv1\pmod4\) below 400.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved.** Hypotheses: \(p\equiv1\pmod4\) prime; the actual law (\(b\ge0\), \(b_0=0\)); the definitions of Rounds 20/151/183/184 quoted above. "(NC)" marks statements on the hypothetical near-critical sequence.
- (a1) Lemma 1, any law: \(\|P_\sigma b\|_{2,n}^2/r^2=G_{-\rho}\), \(\|L_\sigma b\|_{2,n}^2/r^2=V_{-\rho}\), \(|\sum_{T_{-\rho}}f|\le(\sqrt p+1)/2\), and \(G_{-\rho}\le V_{-\rho}+(\sqrt p+1)^2/(p-5)\).
- (a2) Theorem 1 (NC): \(\sup_{T_{-\rho}}g\to0\); \(G_{-\rho}\le1+o(1)\), sharp; \(\#\{T_{-\rho}\cap\{g\ge\tau\}\}\le(1+o(1))/\tau\); \(\{g\ge\tau\}\subseteq T_\rho\cup\{1\}\) eventually, for fixed \(\tau\).
- (a3) Lemma 2: sector-constant symmetric progressions are Paley cliques of size \(\le\sqrt p\). Corollary 1.1 (NC): the (NC)-version of the interval family is carried by such cliques.
- (a4) Proposition 2 (NC): exact subgroup laws are excluded; "\(g\ge\tau\) on \(H\)" forces a subgroup Paley clique.
- (a5) Proposition 3: \(\Delta(\lambda,0)\le c\); \(T_0^{(-\rho)}\le\min(G_{-\rho}c,\tau_p(X-c))\); on (NC), \(T_0^{(-\rho)}\le(\frac14+o(1))p\).
- (a6) Theorem 4 and Corollary 4.1: the laws \(D_\theta\), \(0<\theta<\frac12\), satisfy every accepted non-sector (NC) consequence and carry the Round 189 interval obstruction, with \(\Gamma_{\rm tot}\asymp\sqrt p\). Method cap: (NC)-based routes below 7/4, or a \(\Gamma\) route below 43/24, must use (NC2).

**(b) Conditional.**
- (b1) Criterion 5.1: (GP-Sub\(_c\)) for all \(c>0\) excludes the Round 189 interval family (fixed \(\tau\)) on (NC). It is true for \(c>1/\sqrt2\) by Hanson–Petridis (external, from memory) and for \(c>1\) by Lemma 2.
- (b2) Criterion 5.2: (GP-Sub\(_\kappa\)) forces \(\tau\le(1+o(1))p^{-\kappa}\) on (NC), and removes that family's obstruction to \(T_0\le p^{5/4-\delta}\) for \(\delta<5\kappa\).
- (b3) The exact properties a usable bound would need (§5, items 1–3).

**(c) Evidence.** Lemma 1 checked numerically at \(p\le197\). \(D_\theta\) models at \(p\le10^6\). Exact progression-clique run lengths for 8897 primes up to \(2\cdot10^5\) and five primes up to \(3\cdot10^7\).

## Remaining gap

1. **The mission question.** The accepted (NC) properties exclude the exact subgroup and exact interval laws, but not the obstruction family as a whole.
   - The diluted-interval laws \(D_\theta\) satisfy every accepted non-sector consequence (Theorem 4).
   - Whether (NC2) excludes the family is the arithmetic question (GP-Sub\(_c\)), \(c\le1/\sqrt2\): Paley cliques of geometric-progression form of size \(c\sqrt p\). It is open to my knowledge.
   - No (NC) law of interval type can be exhibited. Whether any (NC) law exists is the open near-critical question itself, and Rounds 184 and 189 found none in models.
2. **Quantitative.** (NC) has no rate. Its only quantitative content is \(G_{-\rho}\le1+o(1)\), which counts heavy points in \(T_{-\rho}\). Turning it into a bound needs (GP-Sub\(_\kappa\)) plus a positive estimate. No bound on \(T_0\), \(X\) or \(\Gamma_{\rm tot}\) moves. The one-match exponent stays \(43/24\).
3. **Unchanged.** First mass \(X=O(p^{1+1/1280})\) target, zero match, generic J sum, cold route, and the original theta-limit target. **Nothing here proves or refutes the original target.**

## Shared estimates (for the coordinator)

- `cand:gp-shifted-energy` (GP): **touched in use, value unchanged.** Corollary 4.1 shows that, without (NC2), (NC)-using arguments still need (GP) below 7/4. With (NC2), the relevant progressions are additionally Paley cliques. So (GP) restricted to clique progressions, or their non-existence (GP-Sub), would suffice to remove the obstruction.
- **New candidate (proposed, not recorded by me):** (GP-Sub\(_c\)) / (GP-Sub\(_\kappa\)), "no sector-constant symmetric geometric progression of length \(c\sqrt p\) in \(Q\)", and its quantitative form. It is shared with the Round 184 (Sub\(_C\)) subgroup statement and with Round 184 Criterion C2's progression case (multiplicative intervals). A literature call should check it together with (GP).
- `cand:slope-row-mass-x`: not touched in value.

## Ranked next tests

1. **Literature (cheap; can join the GP call):**
   - nontrivial bounds for \(\sum_{k\le M}\chi(1-\zeta^k)\) (or \(\chi(\zeta^k+a)\)) at \(M\asymp\sqrt p\);
   - bounds for Paley cliques that are geometric progressions or multiplicative Bohr sets, quoted at source;
   - whether Hanson–Petridis's Stepanov argument has a version for progressions.

   If (GP-Sub\(_\kappa\)) is known, Criterion 5.2 weakens the interval obstruction under (NC), and the next call must price the non-progression part.
2. **Lower-height sector laws.** Under (GP-Sub\(_\kappa\)), determine whether laws with \(g\approx p^{-\kappa}\) on progressions of length \(p^{1/2+\kappa}\) (cap-admissible) still obstruct \(T_0\le p^{5/4-\delta}\). This needs \(E^\times(I-1)\) for \(|I|>\sqrt p\), where MPRRS Lemma 33 needs \(|I|\le p^{2/3}\). This decides whether (GP-Sub\(_\kappa\)) is enough even in principle.
3. Otherwise record that the ordinary line below 7/4 needs an external sum-product input, (GP) or (GP-Sub\(_\kappa\)), with or without (NC). Stop internal (NC) estimate rounds on this lever.

## Replay

```bash
.venv/bin/python -B research/paley-190-nc-exponents.py                  # exact Fractions; ALL OK (<1 s)
.venv/bin/python -B research/paley-190-nc-identity.py --check           # Lemma 1 identity, p <= 197; PART A: ALL IDENTITY CHECKS OK (<1 s)
.venv/bin/python -B research/paley-190-nc-identity.py 10009 40009 160001 640009 1000033   # D_theta models (floating, ~2 s)
.venv/bin/python -B research/paley-190-nc-gpclique.py --check           # brute force vs vectorized runs, p < 400
.venv/bin/python -B research/paley-190-nc-gpclique.py 1000 200000       # exact, ~60 s
.venv/bin/python -B research/paley-190-nc-gpclique.py --list 640009 1000033 4000037 10000121 30000001   # ~5 s
```
numpy as in the repository `.venv`. The model seeds are deterministic in \(p\).

## Verdict

**Inconclusive** (mission definition). The property that would be needed is stated exactly in §5.
- **Excluded on (NC):**
  - exact subgroup laws: (NC1) together with Round 151, Round 184 Prop. 4 or the Round 20 gap;
  - exact interval laws: Round 20/183 energy cap or the Round 184 dichotomy, and under Hanson–Petridis also the new sector lemma.
- **Not excluded by any accepted consequence other than the sector condition:** the diluted-interval laws \(D_\theta\) (\(\theta<\frac12\)). They carry the Round 189 obstruction and have \(\Gamma_{\rm tot}\asymp\sqrt p\) (Theorem 4, proved).
- **The sector condition**, in its exact form (Lemma 1, Theorem 1), forces such a law onto a Paley clique of geometric-progression form of size \(\asymp\sqrt p\). Excluding those is the open statement (GP-Sub). Exact computation finds such cliques of length only \(O(\log p)\), but that is finite evidence.
- **Not quantitative.** Even the conditional exclusion gives no bound on \(T_0\), \(X\) or \(\Gamma_{\rm tot}\). The only quantitative (NC) content is \(G_{-\rho}\le1+o(1)\).
- **No new exponent.** The one-match exponent stays \(43/24\).

## Script hashes (final)

Final replay on 2026-11-21: exponents `ALL OK`; identity `PART A: ALL IDENTITY CHECKS OK`; clique `--check` OK; the model and clique runs as quoted in §7.

| script | SHA-256 |
|---|---|
| `research/paley-190-nc-exponents.py` | `4ff8df2626518148bb4049b1db06a27b39ebac7b782ff5c53d06ed6a6c88f2b6` |
| `research/paley-190-nc-gpclique.py` | `05c798f60e9462d962561f35cb9be88395d8646a4e78781da27a4b2008f61121` |
| `research/paley-190-nc-identity.py` | `d2371d6a62e0faca988cabb57019c6ba80a4da03700d59377de36d261b2b651e` |
