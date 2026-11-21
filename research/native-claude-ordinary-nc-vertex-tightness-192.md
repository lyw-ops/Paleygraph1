# Round 192 native Claude draft: does (NC) force vertex tightness (V)?

- **call_id:** `ordinary-nc-vertex-tightness`
- **Author:** Claude session started by the Round 192 coordinator (generation-1 brain), working alone. This is an agent assessment. It is not an audit, not human acceptance and not a mathematical certification. Nothing was committed.
- **Mission:** `coordination/missions/round-192/ordinary-nc-vertex-tightness.md`, exported from `coordination/round-191.json` (SHA-256 `5af57ceb…7296ad`).
- **Sources checked.** All nine SHA-256 values listed in the mission match the files on disk:
  - `research/round-190-acceptance.json` (`11c42c0a…409b`), `research/round-191-acceptance.json` (`51b86804…9538`);
  - `research/native-claude-audit-191.md` (`0cf09db5…b7fb2cf`): read in full, including §§2 and 6;
  - `research/native-claude-ordinary-fixed-block-assembly-191.md` (`6bb5df8a…b64b69c`): read in full;
  - `research/native-claude-ordinary-prime-row-deleted-one-match-183.md` (`9af6768f…085a26a`): setup and Part 1;
  - `research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md` (`85702949…c6e6c02ec`): setup, §§2, 4, 5;
  - `research/native-claude-ordinary-nc-excludes-sector-laws-190.md` (`5081b11a…60d817`): read in full;
  - `research/ordinary-prime-coset-spread-151.md` (`2029d03c…47823282`): read in full;
  - `research/anchored-repair-20.md` (`141a0fb1…f3721`): read in full.

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-191.md`, and `research/native-claude-ordinary-prime-near-critical-support-energy-184.md` lines 30–170. That last file holds Lemma 0, which the mission attributes to the slope-row-mass report. Its acceptance is at `round-184-acceptance.json` line 273.
- **Scripts (new; nothing else written):**
  - `research/paley-192-vertex-exponents.py`: exact `Fraction` arithmetic for every constant and exponent below. Prints `ALL OK`.
  - `research/paley-192-vertex-models.py`: model evidence, floating point, numpy. Part A covers sector-free families. Part B covers the two-subgroup family, with the actual Legendre symbol. `check` runs a self-test.
  - `research/paley-192-vertex-sharp-search.py`: a field-free search for sets with a sharp spectrum, floating point. Evidence only.

**Citation keys.**
- "R*n* acc:*l*" means `research/round-n-acceptance.json` line *l*.
- R183 = `native-claude-ordinary-prime-row-deleted-one-match-183.md`.
- R184-SE = `native-claude-ordinary-prime-near-critical-support-energy-184.md`; R184-SRM = `native-claude-ordinary-prime-near-critical-slope-row-mass-184.md`.
- R190 = `native-claude-ordinary-nc-excludes-sector-laws-190.md`.
- ASM = `native-claude-ordinary-fixed-block-assembly-191.md`; AUD191 = `native-claude-audit-191.md`.
- R151 = `ordinary-prime-coset-spread-151.md`; R20 = `anchored-repair-20.md`.
- R157 = `ordinary-marked-frequency-localization-157.md`; R160 = `ordinary-matched-physical-truncation-160.md`.

Exponents are powers of \(p\).

---

## 0. Answer in brief

**Verdict: inconclusive.** I prove neither (V) nor its negation on (NC). The question does reduce, though, to one field-free statement, and its probable answer is "no".

1. **Scale (Proposition A, proved).** The relative form of (V), \((\mathrm V_{\rm rel})\): \(m_{<a}=o(\sqrt p)\), depends only on the flat near-critical support \(S\). It says that the spectrum of \(\mathbf 1_S\) is *sharp*: all but \(o(1)\) of its Fourier mass sits at levels \(\ge a\). (V) itself, \(m_{<a}=o(D)\) with \(D\le p^{1/4}/\log p\), is an absolute-scale statement on \(T_\rho\). No accepted (NC) statement constrains \(g\) on \(T_\rho\) at that scale. The accepted absolute-scale statements concern only \(T_{-\rho}\) and the point \(x=1\) (Lemma S).
2. **Sector-free part (Proposition B, proved).**
   - Every sector-free accepted (NC) consequence holds for a random flat law. That is the class \(\mathcal H\) of R190:228–233. Such a law has \(\sup_{x\ne1}g\to0\), hence \(m_{<a}(T_\varepsilon)=(\frac12-o(1))\sqrt p\) for both signs and every fixed \(a\), and \(\sum g^2=o(\sqrt p)\).
   - The \(D_\theta\) laws (R190 Theorem 4, accepted) have \(\sum g^2\asymp\sqrt p\) and still \(m_{<a}\ge(\frac{1-3\theta}2-o(1))\sqrt p\) for \(\theta<\frac13\).
   - So \(\mathcal H\) implies neither (V) nor \(\sum g^2\gg\sqrt p\), and \(\mathcal H\) together with \(\sum g^2\gg\sqrt p\) still does not imply (V). This upgrades ASM §5.3's model evidence to a proof.
3. **The auditor's uncertainty-principle heuristic, tested.**
   - **Its premise is excluded by (A2) (Proposition C).** Under \((\mathrm V_{\rm rel})\) the level set \(\Lambda_a=\{y\in T_\rho:g\ge a\}\) has \(|\Lambda_a|\ge(2-o(1))\sqrt p\), so \(|S|\,|\Lambda_a|\ge(2-o(1))n\). The configuration is never near the equality case \(|S||\Lambda|\approx n\) of the uncertainty principle, so stability of that inequality cannot force coset structure.
   - **Its conclusion holds only in part (Proposition D).** An explicit two-subgroup family has a sharp spectrum and satisfies (V) in robust form (\(m_{<a}\le0.64\) in all eight largest examples checked). It also satisfies flatness, (NC1), the cap and the conclusions of (A2), (A5) and (A6). It violates only (A4), the R151 coset mass, and the sector forms. So "(A2)/(A6) exclude it" is false; (A4) excludes it, and so does (NC2), through a Jacobi-sum count (Lemma J).
4. **Field-general cap on a refutation (Proposition F, bookkeeping).** The \(\mathbb F_{r^2}\) subfield law satisfies (V) with \(m_{<a}\le2(r+1)/(r-1)\to2\). It also satisfies every accepted (NC) statement with a field-general proof, including all the sector forms. A disproof of (V) must therefore use one of the prime-specific inputs (A2), (A4), (A5) item 2 or (A6), or a new prime-specific input.
5. **Conditional refutation (Theorem E).** Let (SS) be the following field-free statement: a set in \(\mathbb Z/N\) with a sharp spectrum carries its spectral mass on a bounded union of subgroups of order \(\asymp N/|S|\). This is a robust, sparse analogue of the Green–Sanders idempotent theorem. Then (SS) together with the accepted (A4) implies that **on (NC), \(m_{<a}\asymp\sqrt p\) for every fixed \(a\)**: (V) fails as badly as possible. Conversely, (V) on (NC) would make the near-critical support a counterexample to (SS).
   - (SS) is not proved here, and I do not know a source for it.
   - The finite evidence is weak and is described in §5.3. The natural non-coset structures (intervals, half-intervals, rank-2 Bohr sets, random sets) keep a fixed fraction of their mass at low levels, independent of \(N\). An annealing search is too weak to settle anything.
6. **\(\sum g^2\gg\sqrt p\).** Unchanged: open on (NC) (R183 acc:270). It is not implied by \(\mathcal H\) (Proposition B). On sector-free laws it is independent of (V) in both directions (\(D_\theta\) and Proposition D).
7. **No explicit (NC) family is possible with current knowledge.** A family satisfying *every* accepted (NC) statement must satisfy (NC2): \(f\) nearly constant on \(T_{-\rho}\) in \(\ell^2\). No prime-field law with (NC2) is known (R190:351–354). So an obstruction can only be an argument, and the argument reduces to (SS).

**Consequence for (A-vertex).** If (SS) holds, (V) is false on (NC). (A-vertex) then needs a genuinely signed estimate on the layers \(C^2/p<|F|^2<a\), which carry \(\asymp\sqrt p\) of vertex mass. The R160 device loses \(p^{1/2}\) there. This is the mission's "refuted" branch, conditional on (SS). Unconditionally the outcome is "inconclusive", and the exact decisive statement is (SS) in the form (SS\(^*\)) of §3.

---

## 1. Hypotheses and the accepted (NC) statements

**Branch hypotheses (used exactly as cited).**
- R157:3 is the genuine retargeted short block of Round 151, on the hypothetical critical-size branch \(m_{\rm eff}/m_0\to1\), with the actual \(b_0=0\) and the relative pin bound. R160:3 adds the physical row \(F(x)=f(1-vx)\) on \(x\in Q\), set to zero if \(1-vx\notin Q\).
- (NC) (R183:53): \(\|L_\sigma b\|_{2,n}/r\to0\) and \(m_{\rm eff}/m_0\to1\) along the hypothetical sequence of primes, with \(\rho=-\sigma\). As in R190:81, write (NC1) for \(G/\sqrt p\to1\) and (NC2) for \(\|L_\sigma b\|/r\to0\).
- Notation follows R190:74–81 and R184-SE:34–37: \(\nu\), \(f=\sum_j\nu_j\psi^j\) on \(Q\), \(g=|f|^2\), \(G=\sum_Qg=n\|\nu\|_2^2\), \(s(x)=\chi(1-x)\), \(T_\varepsilon=\{x\in Q\setminus\{1\}:s(x)=\varepsilon\}\), \(G_\varepsilon=\sum_{T_\varepsilon}g\).

**The vertex sector.** A vertex value is \(y=1-vx\) with \(x\in Q\) and \(\chi(v)=\rho\). Then \(\chi(1-y)=\chi(vx)=\rho\), and \(x\mapsto y\) is a bijection onto \(T_\rho\) (AUD191 §2.5, lines 88–89). Hence
\[
m_{<a}=\|F-F_{\ge a}\|_2^2=\sum_{y\in T_\rho,\ g(y)<a}g(y),\qquad \Lambda_a:=\{y\in T_\rho:g(y)\ge a\}.
\]
- (V) (ASM:199–203): \(m_{<a}=o(D)\) for one fixed \(a\); robustly, \(m_{<a}=O(1)\). Here \(D=E^{-1/2}/\log(2/E)\le p^{1/4}/\log(2\sqrt p)\) (ASM:12, 210).
- \((\mathrm V_{\rm rel})\): \(m_{<a}=o(\sqrt p)\) for one fixed \(a\). It is implied by (V).

**Accepted (NC) consequences, classified.** "Sector-free" means the statement does not mention \(T_{\pm\rho}\). That is the class \(\mathcal H\) of R190 Corollary 4.1 (R190:228–233), audited in R190 acc:295.

| label | statement | source | kind |
|---|---|---|---|
| cap | \(n\max\nu=O(\sqrt p)\) | R153:5–11 | sector-free |
| (NC1) | \(G=(1+o(1))\sqrt p\) | R183:76–91 (Prop. 1.2(ii)) | sector-free |
| (A1) flat | \(e=u_S+o_{\ell^2}(1)\), \(|S|\sim m_0\) | R20:74–76; R151:47 | sector-free |
| (A1) signed | \(d_\rho(S)\to0\) | R20:76; R184-SE Lemma 0 (49–62) | **sector** |
| (A2) | \(\sum g^2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\le\frac12+o(1)\) | R183:104–120 (Prop. 1.4); R183 acc:264 | sector-free statement (proved through R20's gap) |
| (A3) | \(G_{-\rho}=O(1)\), \(M_1=(1+o(1))p\) | R183:76–91; R183 acc:264 | **sector** |
| (NC2) exact | \(V_{-\rho}=\sum_{T_{-\rho}}|f-\bar f_{-\rho}|^2\to0\) | R190 Lemma 1 (94–115) | **sector** |
| R190 Thm 1 | \(\sup_{T_{-\rho}}g\to0\); \(G_{-\rho}\le1+o(1)\); \(\{g\ge\tau\}\subseteq T_\rho\cup\{1\}\) | R190:127–134 | **sector** |
| Lemma 0 | \(\langle e,\rho Ke\rangle=1-(2G_{-\rho}+1)/G\) | R184-SE:49–62 | **sector** |
| SRM Prop. 2 | \(X\ge(2-o(1))p\), \(\max W\ge(1-o(1))p\), \(\sup_{\lambda\ne1}C\ge(1-o(1))p\) | R184-SRM:130–141 | **sector** (through \(M_1\)) |
| (A4) | \(t_B\ge c_0(k,c_1,c_2)>0\) for unions \(B\) of \(\le k\) cosets of subgroups of order in \([c_1\sqrt p,c_2\sqrt p]\) | R151:5, 27–39, 47 | sector-free statement |
| (A5) | \((1-q_a)(2q_a-1)\le o(1)\); \(H_*\) a subgroup, \(|H_*|=o(m_0)\); \(\max_{a\notin H_*}\widehat g(a)\le(\frac12+o(1))G\) | R184-SE:79–114; R184 acc:273 | sector-free statement (proved through \(d_\rho\) and R20's coset gap) |
| (A6) | no \(S\) within \(o(m_0)\) of one coset of order \(\le(2-\delta)m_0\); coset share \(\le(1-\delta/2)^{1/4}+o(1)\) | R184-SE:148–170 | sector-free statement |

---

## 2. Proved statements

### 2.1 Proposition A (transfer to the flat support; what scale (V) lives at). Hypotheses: (NC1), (A1) flat, (A3).

Let \(f_S=|S|^{-1}\sum_{j\in S}\psi^j\) and \(g_S=|f_S|^2\) on \(Q\). Then:
1. \(\sum_{x\in Q}|f-f_S|^2=o(\sqrt p)\) and \(\Delta:=\sum_{x\in Q}|g-g_S|=o(\sqrt p)\).
2. **Level transfer (any \(g,g'\ge0\) on a finite set).** For \(0<a<b\),
   \[\sum_{g<a}g\le\sum_{g'<b}g'+\Delta\,\frac b{b-a}.\]
3. Put \(m^Q_{<a}(h)=\sum_{x\in Q\setminus\{1\},\,h(x)<a}h(x)\). Then \(m^Q_{<a}(g)-G_{-\rho}\le m_{<a}\le m^Q_{<a}(g)\), so \(m_{<a}=m^Q_{<a}(g)+O(1)\).
4. Consequently \((\mathrm V_{\rm rel})\) at some level is equivalent to: for some fixed \(a\), the spectral mass distribution \(\mu_S=(n/|S|-1)^{-1}\sum_{x\ne1}g_S(x)\,\delta_{g_S(x)}\) satisfies \(\mu_S([0,a))\to0\). This is a property of the sequence of sets \(S\) alone (**sharp spectrum** at level \(a\)), up to changing \(a\) by a fixed factor.
5. (V) at scale \(o(D)\), or \(O(1)\), is **not** determined by \(S\): item 1 controls \(g\) on \(T_\rho\) only to within \(o(\sqrt p)\).

*Proof.*
1. \(\nu-\mathbf 1_S/|S|=\|\nu\|_2(e-u_S)+(\|\nu\|_2-|S|^{-1/2})u_S\). Since \(\|\nu\|_2=m_{\rm eff}^{-1/2}\) and \(|S|\sim m_0\sim m_{\rm eff}\), this has norm \(o(m_0^{-1/2})\). Parseval on \(\mathbb Z/n\) (R183:63–70) gives \(\sum_x|f-f_S|^2=n\,o(1/m_0)=o(\sqrt p)\). Then
   \[\Delta\le(\textstyle\sum|f-f_S|^2)^{1/2}(2G+2G_S)^{1/2}=o(p^{1/4})\,O(p^{1/4}),\]
   where \(G_S=n/|S|\).
2. Split \(\{g<a\}\) according to \(g'<b\) or \(g'\ge b\). The first part is at most \(\sum_{g'<b}g'+\Delta\). On the second part \(g'-g\ge b-a\), so it has at most \(\Delta/(b-a)\) points, each with \(g<a\).
3. \(g(1)=1\). The points of \(T_{-\rho}\) contribute at most \(G_{-\rho}=O(1)\) (A3).
4. Combine items 1–3, using \(n/|S|-1\sim\sqrt p\).
5. Item 1 is the only link between \(g\) and \(S\). Lemma S below shows that no other accepted statement constrains \(g\) on \(T_\rho\) below scale \(\sqrt p\). \(\square\)

### 2.2 Lemma S (what the sector forms say on \(T_\rho\); bookkeeping)

Every sector form in the §1 table follows from \(\mathcal H\), (NC2) and flatness, by the cited proofs. Restricted to \(T_\rho\), their whole content is:
- (a) \(G_\rho=G-1-G_{-\rho}=(1-o(1))\sqrt p\), and \(\sum_{T_\rho}g^2\ge\sum g^2-1-G_{-\rho}\);
- (b) for each fixed \(\tau>0\), eventually \(\{g\ge\tau\}\subseteq T_\rho\cup\{1\}\) (R190 Theorem 1(4));
- (c) lower bounds on \(M_1\), \(X\), \(\max W\) and \(\sup C\), which are functions of \(G_\rho\) and \(\sum_{T_\rho}g^2\). Here \(M_1=\sum_\varepsilon(G_\varepsilon^2-\sum_{T_\varepsilon}g^2)\) (R183:89), and the SRM floors follow from \(M_1\) by Cauchy–Schwarz (R184-SRM:134–140).

None of (a)–(c) is an upper bound on the low-level mass of \(g\) on \(T_\rho\):
- (b) says where high levels may sit, not whether the mass is there;
- (a) and (c) are relative, scale-\(\sqrt p\) statements.

The only absolute-scale statements, \(V_{-\rho}\to0\), \(G_{-\rho}\le1+o(1)\) and \(\sup_{T_{-\rho}}g\to0\), concern \(T_{-\rho}\).

So a proof of (V) must carry information from "\(f\) is nearly constant on \(T_{-\rho}\)" to the level distribution of \(g\) on \(T_\rho\), through the positivity and flatness of \(\nu\). No accepted statement does this beyond (a)–(c). *(This is a reading of the logical form of the accepted list, not a theorem about all possible arguments.)*

### 2.3 Proposition B (sector-free method cap; proved)

**(i) Random flat laws.** Let \(S\subseteq\mathbb Z/n\setminus\{0\}\) contain each \(j\) independently with probability \(\pi=p^{-1/2}\), and let \(\nu=\mathbf 1_S/|S|\). With probability \(1-o(1)\), for all large \(p\):
1. \(\nu\in\mathcal H\). Concretely:
   - probability, \(\nu_0=0\), cap \(n/|S|\sim\sqrt p\), \(\omega=\frac12\lambda\ge0\), (H3) since \(\nu\) is real;
   - (NC1), and exact flatness \(|S|=(1+O(\sqrt{\log p/m_0}))m_0\);
   - (A2): \(\mathcal E(S)/|S|^3\le(1+C\log p)/|S|\to0\);
   - (A5): \(\max_{a\ne0}r_S(a)\le C\log p/|S|\to0\), \(H_*=\{0\}\);
   - (A6): every coset of every subgroup of order \(\le2m_0\) holds \(\le C\log p\) points;
   - (A4): \(\sum_Bg\le|B|\sup_{x\ne1}g+1=O(\log p)=o(G)\).
2. \(\sup_{x\ne1}g\le C\log p/m_0\to0\). So for every fixed \(a\in(0,1]\), eventually \(m_{<a}(T_\varepsilon)=G_\varepsilon\) for both \(\varepsilon\).
3. \(G_\varepsilon=(\frac12+o(1))\sqrt p\) for both \(\varepsilon=\pm1\), and \(\sum g^2\le1+C\log p=o(\sqrt p)\).

*Proof.*
- **Item 2.** For \(x\ne1\), \(\sum_{j\ne0}\xi_j\psi^j(x)\) has mean \(-\pi\) and variance \(\le m_0\). Bernstein's inequality for the real and imaginary parts, with a union bound over the \(n\) points, gives deviation \(\le C\sqrt{m_0\log p}\) for every \(x\).
- **Item 1.**
  - \(|S\cap(S+a)|\) is a sum over the edges of the cycles of \(j\mapsto j-a\). Split the edges into three matchings; each is a sum of independent indicators with mean \(\le n\pi^2\le1\), so Chernoff and a union bound over \(a\) give \(\le C\log p\).
  - A coset of a subgroup of order \(e\le2m_0\) holds a binomial count with mean \(\le2m_0\pi\le1\). Chernoff and a union bound over the \(\le n\,d(n)\) cosets give \(\le C\log p\).
  - \(\mathcal E(S)=|S|^2+\sum_{a\ne0}|S\cap(S+a)|^2\le|S|^2(1+C\log p)\).
  - The remaining items are immediate.
- **Item 3.**
  - \(\sum_{T_\varepsilon}g=|S|^{-2}\,\xi^{\mathsf T}M\xi\), with \(M_{jj'}=c(j-j')\) and \(c(d)=\sum_{x\in T_\varepsilon}\psi^d(x)\).
  - \(c(0)=|T_\varepsilon|\). For \(d\ne0\), \(c(d)=\frac12(-1+\varepsilon\sqrt p\,k(d))\) with \(|k|\le1\) (R190:112–114; R184-SE:35). So \(|c(d)|\le(\sqrt p+1)/2\), and \(\sum_{d'\ne d}c(d-d')=-|T_\varepsilon|\).
  - The diagonal gives \(|S||T_\varepsilon|/|S|^2=(\frac12+o(1))\sqrt p\).
  - The off-diagonal part has mean \(\pi^2\sum_{j\ne j'}c=O(p)\). Its variance is at most \(4\pi^2\sum_{j\ne j'}|c|^2+4\pi^3\sum_j|\sum_{j'}c_{jj'}|^2=O(p^2)\).
  - Dividing by \(|S|^2\asymp p\) gives \(O(1)\) in mean and \(O_P(1)\) in fluctuation (Chebyshev).
  - Finally \(\sum g^2\le1+\sup_{x\ne1}g\cdot G\). \(\square\)

**(ii) Diluted intervals \(D_\theta\), \(0<\theta<\frac12\).** These are R190 Theorem 4, accepted at R190 acc:295, so \(D_\theta\in\mathcal H\) and \(\sum g^2\ge c(\theta)\sqrt p\) (R190:211). In addition:
- (ii-1) \(\sum_{x\in Q,\,g(x)\ge a}g\le(\theta+o(1))\sqrt p\) for each fixed \(a\). Hence the heavier sign has \(m_{<a}(T_\varepsilon)\ge(\frac12-\theta-o(1))\sqrt p\).
- (ii-2) For the Bernoulli variant (each \(j\in J'\) independently with probability \(\theta\)), which satisfies Theorem 4's conclusions by the same proof: \(G_\varepsilon\ge(\frac{1-\theta}2-o(1))\sqrt p\) for both signs. Hence \(m_{<a}(T_\varepsilon)\ge(\frac{1-3\theta}2-o(1))\sqrt p\) for both signs when \(\theta<\frac13\).

*Proof.*
- **(ii-1).** The proof of Theorem 4 (R190:215–217) gives \(\varepsilon_p:=\sup_x|f-(\theta L'/m)D_{L'}|=o(1)\). Eventually \(g\ge a\) forces \(|D_{L'}|\ge\sqrt a/2\), and that set has \(O(\sqrt p/a)\) points, because \(|D_{L'}(k)|\le n/(2L'|k|)\). Then
  \[\sum_{g\ge a}g\le(1+o(1))\sum_x|D_{L'}|^2+O(\varepsilon_p\sqrt p/a),\qquad \sum_x|D_{L'}|^2=n/L'=(\theta+o(1))\sqrt p\ \text{(Parseval)}.\]
  Since \(G_++G_-=G-1\), one sign has \(G_\varepsilon\ge(G-1)/2\).
- **(ii-2).** Write \(f=(\theta L'/m)D_{L'}+e\), where \(e\) is the centred noise.
  - \(\sum_{T_\varepsilon}|e|^2\) is a centred Bernoulli quadratic form with the same \(c(d)\) as in (i). Its diagonal is \(\theta(1-\theta)L'|T_\varepsilon|/m^2=(\frac{1-\theta}2+o(1))\sqrt p\), and its off-diagonal part has standard deviation \(O(1/\theta)\).
  - The cross term \(\sum_{T_\varepsilon}D\bar e\) has variance \(\le\theta m^{-2}n\sum_x|D|^2=O(\theta^2\sqrt p)\), so it is \(o(\sqrt p)\).
  - Subtract (ii-1). \(\square\)

**Corollary B (method cap; proved).** No argument that uses (NC) only through \(\mathcal H\) proves (V) or \((\mathrm V_{\rm rel})\) on \(T_\rho\), for either sign. No such argument proves \(\sum g^2\gg\sqrt p\). Adding \(\sum g^2\gg\sqrt p\) to \(\mathcal H\) still does not give (V) (\(D_\theta\) with \(\theta<\frac13\)). This strengthens R190 Cor. 4.1(iii) and turns ASM §5.3 ("Not implied by the sector-free (NC) consequences (evidence)") into a proof.

### 2.4 Proposition C (the uncertainty-principle heuristic; proved on (NC))

Assume (NC) and \((\mathrm V_{\rm rel})\) at level \(a\). Then:
1. \(\sum_{\Lambda_a}g=G_\rho-m_{<a}=(1-o(1))\sqrt p\).
2. \((2-o(1))\sqrt p\le|\Lambda_a|\le(1+o(1))\sqrt p/a\). Hence \(a\le\frac12+o(1)\), as in ASM C5.
3. \((2-o(1))\,n\le|S|\,|\Lambda_a|\le(1+o(1))\,n/a\).

*Proof.* Item 1 is (A3) with \((\mathrm V_{\rm rel})\). The lower bound in item 2 is Cauchy–Schwarz:
\[(\textstyle\sum_{\Lambda_a}g)^2\le|\Lambda_a|\sum_{\Lambda_a}g^2,\qquad \sum_{\Lambda_a}g^2\le\sum g^2\le(\frac12+o(1))\sqrt p\ \text{(A2)}.\]
The upper bound is Chebyshev. Item 3 uses \(|S|\sim m_0=n/\sqrt p\). \(\square\)

**Reading.** The heuristic (AUD191:237) runs: vertex mass on \(\asymp\sqrt p\) points at levels \(\ge a\), with \(\nu\) flat on \(\asymp n/\sqrt p\) points, suggests near-coset structure. That inference would follow from *stability of the uncertainty principle*:
- \(|{\rm supp}\,\nu|\,|{\rm supp}\,\widehat\nu|\ge n\), with \(\ell^2\)-robust form \(|S||\Lambda|\ge n(1-\varepsilon_1-\varepsilon_2)^2\) (Donoho–Stark);
- equality, and stably near-equality, occurs only for cosets.

Proposition C shows that (A2) keeps every \((\mathrm V_{\rm rel})\) configuration at least a factor 2 above that equality case. So the uncertainty principle cannot be the mechanism. Coset structure, if it is forced, must come from the Boolean nature of \(\mathbf 1_S\), that is from an idempotent-type argument (§3). The models confirm the factor: \(|S||\Lambda_{0.2}|/n\approx3.99\) in the two-subgroup family (§5.2).

### 2.5 Lemma J and Proposition D (a sharp family that (A2), (A5) and (A6) do not exclude)

**Lemma J (any prime \(p\equiv1\bmod4\); proved).** Let \(\Gamma\le\mathbb F_p^\times\) be a subgroup and \(\rho=\pm1\). Then
\[\#\{y\in\Gamma\setminus\{1\}:\chi(1-y)=-\rho\}\ \ge\ \tfrac12\big(|\Gamma|-1-\sqrt p\big).\]

*Proof.* Let \(k=(p-1)/|\Gamma|\). Then
\[\sum_{y\in\Gamma}\chi(1-y)=\frac1k\sum_{t\ne0}\chi(1-t^k)=\frac1k\sum_{\psi^k=1}J(\psi,\chi).\]
- The trivial \(\psi\) gives \(-1\).
- \(\psi=\chi\), if \(2\mid k\), gives \(J(\chi,\chi)=-\chi(-1)=-1\).
- Every other \(\psi\) gives \(|J|=\sqrt p\).

So the sum has modulus \(\le(1+(k-1)\sqrt p)/k<\sqrt p\). The term \(y=1\) is \(\chi(0)=0\). Write the sum as \(\rho(|\Gamma|-1)-2\rho\,\#\{\text{bad}\}\). \(\square\)

(Jacobi sums of modulus \(\sqrt p\) are the same input as in R190:112–114. This is the subgroup analogue of the R184 statement (Sub\(_C\)), and it is trivial above order \(\sqrt p\). No geometric progression is involved.)

**Corollary J (on (NC)).** No law on (NC) has \(g\ge\tau\) on all but \(o(\sqrt p)\) points of a subgroup \(\Gamma\le Q\) with \(|\Gamma|\ge(1+\delta)\sqrt p\), for fixed \(\tau,\delta>0\). Indeed \(G_{-\rho}\ge\tau(\delta\sqrt p-1-o(\sqrt p))/2\to\infty\), against (A3).

**Proposition D (the two-subgroup family; exact for each admissible \(p\)).** Let \(h_1\ne h_2\) be divisors of \(n\) with \(d=\gcd(h_1,h_2)\). Let \(H_i\le\mathbb Z/n\) have order \(h_i\), with annihilator \(\Gamma_i=H_i^\perp\le Q\) of order \(n/h_i\). Put
\[\nu=\frac{\mathbf 1_{1+H_1}+\mathbf 1_{2+H_2}}{h_1+h_2},\qquad \beta_i=\frac{h_i}{h_1+h_2},\qquad \Gamma'=\Gamma_1\cap\Gamma_2=(H_1+H_2)^\perp,\quad |\Gamma'|=\frac{n}{{\rm lcm}(h_1,h_2)}.\]
Then:
1. **Levels.** \(f=\beta_1\psi^1\mathbf 1_{\Gamma_1}+\beta_2\psi^2\mathbf 1_{\Gamma_2}\). So \(g=\beta_i^2\) on \(\Gamma_i\setminus\Gamma'\), \(g\le1\) on \(\Gamma'\), and \(g=0\) elsewhere. For every \(a<\min\beta_i^2\), \(m_{<a}\le|\Gamma'|\).
2. **Sector-free properties.** Along any sequence with \(h_1+h_2=(1+o(1))m_0\), \(h_1/h_2\to1\) and \(d=o(m_0)\):
   - \(\nu_0=0\), the cap, flatness, and (NC1);
   - (A2): \(\sum g^2/G\to\beta_1^3+\beta_2^3=\frac14\);
   - (A5): \(q_a=\beta_i+o(1)\to\frac12\) on \(H_i\setminus H_j\), \(H_*=H_1\cap H_2\) of order \(d=o(m_0)\), so the dichotomy holds;
   - (A6): a coset of a subgroup of order \(\le2m_0\) cannot contain \(H_1+H_2\), whose order is \({\rm lcm}\gg m_0\). So it holds \(\le\beta_i+\beta_j/2\to\frac34<(1-\delta/2)^{1/4}\) of the mass, for every \(\delta<350/256\).

   With \(h_i\sim m_0/2\), \(n/{\rm lcm}\to8d\). So for bounded \(d\), (V) holds in **robust form**: \(m_{<a}=O(1)\) for each fixed \(a<\frac14\).
3. **Violations.**
   - (A4) fails: \(B=\Gamma_1\cup\Gamma_2\) is a union of two subgroups of order \(\sim2\sqrt p\), and \(t_B=0\).
   - The sector forms fail: \(g\approx\frac14\) on \(\Gamma_i\setminus\Gamma'\) with \(|\Gamma_i|\sim2\sqrt p\), so Corollary J gives \(G_{-\rho}\ge(\frac18-o(1))\sqrt p\) for both signs.

*Proof.* Item 1: the transform of \(\mathbf 1_{x+H}\) is \(|H|\psi^x\mathbf 1_{H^\perp}\). Item 2: the stated computations (overlaps of the union of two cosets; \(\mathcal E\) from item 1 and Proposition 1.1 of R183). Item 3: Lemma J. \(\square\)

**Existence.** \(\mathcal P\) is the set of primes for which such \(h_1,h_2\) exist. With tolerances \(|h_1+h_2-m_0|\le0.03m_0\), \(h_2/h_1\le1.10\) and \(d\le4\), it contains 2494 primes \(p\equiv1\bmod4\) in \([2\cdot10^4,4\cdot10^6]\) (§5.2). For example \(p=3997297\) with \(h_1=487\), \(h_2=513\), \(d=1\), \(n/{\rm lcm}=8\). I do not prove that \(\mathcal P\) is infinite with tolerances tending to 0; that is a divisor-in-an-interval problem for shifted primes. So Proposition D is exact for each \(p\in\mathcal P\), and its use as a method cap over sequences is conditional on \(\mathcal P\) being infinite along tolerances \(\to0\).

**Reading.** Sharp spectra (in robust \(O(1)\) form) are compatible with flatness, (NC1), the cap and the conclusions of (A2), (A5) and (A6). The auditor's "(A2)/(A6) exclude near-coset structure" is therefore true only for *single* cosets: (A6)(a) together with (A2) and \(C'\ge1\) settle that case. For unions of cosets of different subgroups, (A2) and (A6) do not exclude it. (A4) does, and so does (NC2) via Corollary J.

### 2.6 Proposition F (field-general cap on refuting (V); bookkeeping on R184-SRM Prop. 5)

Let \(q=r^2\) and let \(\nu\) be uniform on \(I\setminus\{0\}\), where \(I\) is the annihilator of \(\mathbb F_r^\times\) (R184-SRM:215–262). Then:
- \(g=1\) on \(\mathbb F_r^\times\), and \(g=\beta=4/(r-1)^2\) elsewhere on \(Q\).
- \(m_{<a}\le\beta\,(|Q|-(r-1))\le2(r+1)/(r-1)\to2\) for every fixed \(a>\beta\). So (V) holds in robust form.
- \(\nu\) satisfies every sector form of §1:
  - \(V_-=0\) and \(G_-\to1\) (R190:123);
  - Lemma 0 and \(d_\rho\to0\), since \(\nu\) is exactly flat with \(\langle e,\rho Ke\rangle=1-(2G_-+1)/G\to1\);
  - \(M_1\sim q\), and \(X\ge(r-2)(r-3)^2\ge2q\).
- \(\nu\) also satisfies (NC1), flatness and the cap.
- It violates (A2), (A4) (R184-SRM Prop. 5(d)), (A5) item 2 (\(H_*\supseteq I\), of order \(\sim m_0\)) and (A6)(a) (\(S\) is a subgroup minus a point, of order \(\sim m_0\)).

**Cap.** A proof that (V) *fails* on (NC) cannot be field-general. It must use (A2), (A4), (A5) item 2, (A6), or a new prime-specific input. With Proposition D, any refutation must use (A4), or a sector form together with one of (A2), (A5) item 2 or (A6). (Square controls test field-general shortcuts only; this is not a statement about primes, WORKFLOW.)

---

## 3. Conditional criterion: the sharp-spectrum statement (SS)

**(SS) (field-free; not proved).** For every \(a\in(0,\frac12]\) there are \(L=L(a)\in\mathbb N\) and \(c=c(a)\in(0,1]\) with the following property. Take finite cyclic groups \(\mathbb Z/N_k\) and sets \(S_k\) with \(|S_k|\to\infty\). Write \(g_k=|\widehat{\mathbf 1_{S_k}}|^2/|S_k|^2\) on the dual and \(M_k=\sum_{\xi\ne0}g_k=N_k/|S_k|-1\). Suppose
\[\sum_{\xi\ne0,\ g_k(\xi)<a}g_k(\xi)=o(M_k).\]
Then there are \(\le L\) subgroups \(\Gamma_{k,i}\) of the dual, of orders in \([c\,N_k/|S_k|,\ N_k/(c|S_k|)]\), with \(\sum_{\xi\notin\cup_i\Gamma_{k,i}}g_k=o(M_k)\).

**(SS\(^*\)) (the weakest form used).** No sequence of sets with \(|S_k|\sim\sqrt{N_k/2}\) has a sharp spectrum at a fixed level \(a\) while satisfying the conclusion of (A4): spectral mass \(\ge c_0\) outside every union of \(\le L\) subgroups of order \(\asymp N_k/|S_k|\). (SS) implies (SS\(^*\)).

**Theorem E (conditional on (SS\(^*\)); proof uses accepted statements only).** On (NC), for every fixed \(a\in(0,1]\),
\[\liminf\ m_{<a}/\sqrt p>0 .\]
Since \(m_{<a}\le G_\rho\le(1+o(1))\sqrt p\), this means \(m_{<a}\asymp\sqrt p\) for every fixed \(a\). In particular (V) and \((\mathrm V_{\rm rel})\) fail.

*Proof.*
1. Suppose \(m_{<a}=o(\sqrt p)\) along a subsequence.
2. Proposition A(3) and (A3) give \(m^Q_{<a}(g)=o(\sqrt p)\).
3. Proposition A(2), with the roles \((g_S,g)\) and levels \(a/2<a\), gives \(m^Q_{<a/2}(g_S)\le m^Q_{<a}(g)+2\Delta=o(\sqrt p)\). So \(S\) has a sharp spectrum at level \(a'=\min(a/2,\frac12)\), with \(N=n\), \(|S|\sim\sqrt{n/2}\) and \(M=n/|S|-1\sim\sqrt p\).
4. (SS\(^*\)) applied to \(S\) gives \(L\) subgroups \(\Gamma_i\le Q\) of order \(\asymp\sqrt p\) with \(\sum_{x\notin B}g_S=o(\sqrt p)\), where \(B=\cup\Gamma_i\).
5. By Proposition A(1), \(\sum_{x\notin B}g\le\sum_{x\notin B}g_S+\Delta=o(\sqrt p)\). So \(t_B=\|\mathbf 1_{Q\setminus B}f\|^2/\|f\|^2\to0\).
6. This contradicts (A4): R151:47 gives a uniformly positive lower bound for \(t_B\) on (NC), for bounded unions of cosets of subgroups of order in \([c_1\sqrt p,c_2\sqrt p]\). \(\square\)

**Remarks.**
- **Only one direction is decided.** (V) on (NC) implies that the near-critical \(S\) has a sharp spectrum and, by (A4), that its spectral mass is not on boundedly many subgroups of order \(\asymp\sqrt p\). So (V) on (NC) implies that (SS\(^*\)) fails for the near-critical supports. A "yes" for (V) therefore requires the near-critical support to be a counterexample to a robust idempotent statement. A "no" follows from (SS\(^*\)).
- **The exact case.** Suppose \(g_S(\xi)\in\{0\}\cup[a,1]\) for every \(\xi\). Then \(\|\mathbf 1_S\|_{A}=N^{-1}\sum_\xi|\widehat{\mathbf 1_S}(\xi)|\le N^{-1}\cdot\frac{N}{a|S|}\cdot|S|=1/a\). The quantitative idempotent theorem of Green and Sanders then writes \(\mathbf 1_S\) as a signed sum of \(\le\exp\exp(O(a^{-4}))\) indicators of cosets. That reference (Ann. of Math. 168 (2008)) is *quoted from memory, not read at source, and used in no proof*. Its spectrum then lies on a bounded union of subgroups. The sizes in (SS), and the **robust** version with error \(o(M)\) at density \(|S|/N\asymp N^{-1/2}\to0\), are not covered: the almost-periodicity arguments I know lose a factor depending on the density.
- **No sector input, no GP input.** Theorem E uses (A4), which R151 proves from Mit'kin's estimate and the cap, and no sector form along geometric progressions. It does not touch `cand:gp-sector-constancy` or `cand:gp-shifted-energy`.
  - A variant could replace (A4) by (A3) and Corollary J. It works only for components of order \(\ge(1+\delta)\sqrt p\). For orders \(\le\sqrt p\) it would need (Sub\(_C\)) (R184-SE:168), which is open.
  - If (SS) failed through progression-shaped spectra (multiplicative Bohr sets in \(Q\)), excluding them by the sector condition would need (GP-Sub), i.e. `cand:gp-sector-constancy`.

---

## 4. The alternative \(\sum g^2\gg\sqrt p\)

- On (NC) it is equivalent to \(\mathcal E(S)\gg|S|^3\) (R183 Prop. 1.4). It is open in \([O(1),(\frac12+o(1))\sqrt p]\) (R183 acc:270), and **unchanged** by this call.
- It is not implied by \(\mathcal H\) (Proposition B(i)). By Lemma S, the sector forms add only the scalar facts (a)–(c) on \(T_\rho\), which have no bearing on energy.
- On sector-free laws, (V) and high energy are independent in both directions:
  - \(D_\theta\): high energy without (V);
  - Proposition D: (V), at energy \(\frac14\).

  Neither direction gives the other, and (SS) says nothing about energy.
- The exact statement that would decide it remains the Round 20 low-energy question: \(\liminf\mathcal E(S)/|S|^3>0\) on (NC).

---

## 5. Evidence (finite, floating point; models, not the near-critical law)

### 5.1 Sector-free families (`paley-192-vertex-models.py A 10009 40009 160001 640009`)

Values are in units of \(\sqrt p\), for both signs. Selected rows:

| law | \(p\) | \(G_{+}\) / \(G_-\) | \(m_{<0.2}(T_\pm)\) | \(m_{<0.05}(T_\pm)\) | \(\sup_{x\ne1}g\) | \(\sum g^2/\sqrt p\) | \(|S||\Lambda_{0.05}|/n\) |
|---|---|---|---|---|---|---|---|
| flat | 160001 | 0.499 / 0.498 | 0.499 / 0.498 | 0.499 / 0.498 | 0.068 | 0.012 | 0.01 |
| flat | 640009 | 0.500 / 0.499 | 0.500 / 0.499 | 0.500 / 0.499 | 0.029 | 0.006 | 0.00 |
| \(D_{0.25}\) | 640009 | 0.517 / 0.482 | 0.388 / 0.390 | 0.385 / 0.383 | 0.9999 | 0.175 | 0.42 |
| \(D_{0.10}\) | 640009 | 0.499 / 0.500 | 0.458 / 0.456 | 0.453 / 0.454 | 0.9995 | 0.071 | 0.21 |

- In the flat law \(\sup g\to0\) and both sectors carry \(\approx\frac12\sqrt p\), all below every level.
- \(D_\theta\) keeps \(\approx(\frac12-\frac\theta2)\sqrt p\) below every fixed level in both sectors. That is above the proved bounds \(\frac12-\theta\) and \(\frac{1-3\theta}2\).
- The uncertainty product is \(<2\) because these laws violate \((\mathrm V_{\rm rel})\), consistent with Proposition C.

### 5.2 Two-subgroup family (`paley-192-vertex-models.py B 20000 4000000`; actual Legendre symbol; about 6 s)

- 2494 primes in \([2\cdot10^4,4\cdot10^6]\) admit \(h_1,h_2\) within the tolerances of §2.5.
- In all eight largest examples:
  - the levels match the closed form to \(\le3\cdot10^{-15}\);
  - \(t_B\le10^{-31}\);
  - \(G/\sqrt p\in[0.984,1.031]\), \(\sum g^2/G\in[0.2515,0.2541]\);
  - dichotomy \(\max(1-q)(2q-1)\le0.021\), \(|H_*|\le4\), \(\max q\) off \(H_*\le0.522\) (equal to \(\beta_{\max}\), tending to \(\frac12\) as \(h_1/h_2\to1\));
  - maximal single-coset mass \(\le0.522\);
  - \(|S||\Lambda_{0.2}|/n\approx3.99\).

  Sector diagnostics, by example:

| \(p\) | \(h_1,h_2\) | \(G_{-\rho}\) (\(\rho=+1\) / \(-1\)) | bad points in \(\Gamma_1,\Gamma_2\) (\(\rho=+1\)) | Lemma J bounds | \(m_{<0.05}(T_\rho)\) (\(+1\) / \(-1\)) |
|---|---|---|---|---|---|
| 3997297 | 487, 513 | 984.8 / 1012.9 | 1978, 1962 | 1051.8, 947.8 | 0.001 / 0.000 |
| 3998809 | 484, 486 | 1033.6 / 1026.6 | 1978, 2160 | 1065.1, 1056.6 | 0.000 / 0.017 |
| 3999001 | 500, 516 | 981.6 / 985.4 | 1994, 1938 | 999.1, 937.1 | 0.046 / 0.006 |

(\(\sqrt p\approx1999\).)
- (V) holds in robust form: \(m_{<a}\) is absolutely bounded, \(\le0.64\) for every \(a\le0.2\) in the eight examples.
- The family is grossly non-sector: \(G_{-\rho}\approx\sqrt p/2\). Bad points number about \(|\Gamma_i|/2\), twice the Lemma J bound.

### 5.3 Sharp-spectrum search, field-free (`paley-192-vertex-sharp-search.py`)

**Part E (exhaustive over all \(S\ni0,1\), \(|S|=m\approx\sqrt{N/2}\), prime \(N\le83\)).**
- \(\min L_{0.2}\in[0.110,0.146]\) for \(N=31,\dots,83\), with no downward trend.
- \(\min L_{0.05}\) reaches 0 at \(N=31,41,61\). This is a finite-size effect: \(a=0.05<1/m^2\), so discreteness alone can empty the band \((0,a)\).
- Composite controls with a subgroup of order \(m\) give \(L_a=0\).
- **Uninformative** about \(a\) fixed with \(m\to\infty\).

**Part S (annealing, 20000 steps per seed, \(a=0.1\); \(N\in\{2003,5003,10007,20011\}\) prime, with controls \(N=2048,5000,10082\)).**

| seed | best \(L_{0.1}\) at prime \(N=2003,\dots,20011\) |
|---|---|
| interval | 0.114 (energy \(\frac23\)) |
| rank-2 Bohr | 0.22–0.26 |
| half-interval | 0.51–0.57 |
| random | 0.55 → 0.98 |

- The annealer did **not** find the exact coset optimum (\(L=0\)) in the composite controls: it reached 0.62–0.94 from random seeds.
- So its failure to find sharp non-coset sets in prime \(N\) is **not** evidence for (SS).
- The only usable content is that the natural non-coset structures keep a fixed fraction of mass at low levels, independent of \(N\). For intervals that is the Fejér tail, \(\approx\sqrt a/\pi\).

### 5.4 Exact arithmetic (`paley-192-vertex-exponents.py`, 48 checks, `ALL OK`)

It checks:
- the bounds \(|\Lambda_a|/\sqrt p\ge2\), \(|S||\Lambda_a|/n\ge2\), and \(a\le\frac12\) as the condition for a nonempty window;
- \(\frac12-\theta\), \(\frac{1-3\theta}{2}\);
- \(\beta_1^3+\beta_2^3=\frac14\), the coset fraction \(\frac34\) and the threshold \(\delta<\frac{350}{256}\), \(n/{\rm lcm}\to8d\), \(|\Gamma_i|\to2\sqrt p\);
- Lemma J's \((1+(k-1)s)/k<s\) and \(G_{-\rho}\ge\sqrt p/8\);
- the square-control bound \(2(r+1)/(r-1)\) and \(G=r+1\);
- the loss exponents of §6;
- primality and divisibility for six listed examples of \(\mathcal P\).

---

## 6. Loss exponents (exact, Fractions)

- **If (V) fails** (Theorem E's conclusion): \(m_{<a}\asymp\sqrt p\). The R160 price \(p\,m_{<a}\) is then \(p^{3/2}\) against the robust \(O(p)\), a loss of **\(1/2\)**. Against \(o(pD)\) the loss is at least \(\frac12-\frac14=\mathbf{1/4}\). This is the worst case of ASM §5.2 / AUD191 (a9).
- **Scale gap.** (V) lives at \(o(D)\le p^{1/4-o(1)}\). Every accepted statement on \(T_\rho\) lives at \(o(p^{1/2})\). The gap exponent is between \(\frac14\) and \(\frac12\) (Proposition A(5), Lemma S).
- **Proposition A.** \(\sum|f-f_S|^2=n\cdot o(1/m_0)=o(p^{1/2})\), and \(\Delta=o(p^{1/4})\cdot O(p^{1/4})=o(p^{1/2})\).

---

## 7. Proved (a) / conditional (b) / evidence (c); remaining gap

**(a) Proved.** Hypotheses: R157:3, R160:3, (NC) as in R183:53, and the accepted statements cited. Items (a1)–(a6) assume (NC) where marked.
- (a1) **Proposition A** ((NC1), (A1), (A3)): \(\sum|g-g_S|=o(\sqrt p)\); level transfer; \(m_{<a}=m^Q_{<a}(g)+O(1)\); \((\mathrm V_{\rm rel})\) is a sharp-spectrum property of \(S\); (V) is not determined by \(S\).
- (a2) **Lemma S** (bookkeeping): the sector forms constrain \(g\) on \(T_\rho\) only through (a)–(c) of §2.2.
- (a3) **Proposition B and Corollary B** (no (NC) assumed; probabilistic constructions):
  - random flat laws and \(D_\theta\) lie in \(\mathcal H\), with \(m_{<a}\ge(\frac12-o(1))\sqrt p\) (flat, both signs) and \(m_{<a}\ge(\frac{1-3\theta}2-o(1))\sqrt p\) (\(D_\theta\), \(\theta<\frac13\), both signs);
  - the second-moment steps (i-3) and (ii-2) are sketched at the level of the variance bounds; item (ii-1) for the heavier sign uses only the accepted Theorem 4 and Parseval;
  - method cap: \(\mathcal H\) implies neither (V) nor \(\sum g^2\gg\sqrt p\), and \(\mathcal H\) with high energy does not imply (V).
- (a4) **Proposition C** ((NC) + \((\mathrm V_{\rm rel})\)): \(|\Lambda_a|\ge(2-o(1))\sqrt p\), \(|S||\Lambda_a|\ge(2-o(1))n\), \(a\le\frac12+o(1)\).
- (a5) **Lemma J** (any \(p\)), **Corollary J** ((NC)), and **Proposition D** (exact for each \(p\in\mathcal P\)).
- (a6) **Proposition F** (exact, bookkeeping on R184-SRM Prop. 5): the field-general cap on refuting (V).

**(b) Conditional.**
- (b1) **Theorem E:** (SS\(^*\)) implies, on (NC), \(m_{<a}\asymp\sqrt p\) for every fixed \(a\). So (V) fails, and (A-vertex) needs a signed estimate.
- (b2) Proposition D as a method cap over sequences, conditional on \(\mathcal P\) being infinite with tolerances \(\to0\).

**(c) Evidence.**
- Models §5.1–§5.2, at \(p\le4\cdot10^6\).
- The field-free search §5.3 (weak).
- The Green–Sanders exact case, quoted from memory and not used.

**Remaining gap (exact).**
1. **(V) on (NC)** is decided negatively by (SS\(^*\)), a field-free robust idempotent statement for sets of density \(\asymp N^{-1/2}\) in cyclic groups. It is not proved, and I found no accepted or quoted source for it.
2. **A positive answer** requires the near-critical support to violate (SS\(^*\)), and requires the absolute-scale upgrade from \(o(\sqrt p)\) to \(o(D)\). No accepted statement acts at that scale on \(T_\rho\).
3. **An explicit (NC) family** cannot be produced with current knowledge, because (NC2) is the theta-type constraint itself (R190:351–354).
4. **\(\sum g^2\gg\sqrt p\):** open, unchanged (R183 acc:270).

**Nothing here proves or refutes the original target.**

---

## 8. For the coordinator

- **What changes.**
  - (A-vertex) is now tied to one field-free statement: (SS\(^*\)) together with the accepted (A4) refutes (V) (Theorem E).
  - The internal lever "(NC) forces (V)" is very unlikely. It would need a counterexample to a robust idempotent theorem.
  - The auditor's heuristic is corrected. The uncertainty principle is excluded by (A2) (Proposition C), and (A2)/(A6) do not exclude sharp families (Proposition D); (A4) and (NC2) do.
  - The sector-free cap is now proved (Proposition B).
- **What does not change.** The ordinary line still rests on `cand:gp-shifted-energy` and `cand:gp-sector-constancy`, both external, plus (A-vertex). The recommendation to hold is unaffected under every outcome.
- **Shared estimates.**
  - `cand:gp-sector-constancy`: **not touched in use.** No sector form is used along geometric progressions. Corollary J concerns subgroups of order \(>\sqrt p\), where Jacobi sums settle it. It would be touched only if a failure of (SS) came from progression-shaped spectra (§3 remark).
  - `cand:gp-shifted-energy`, `cand:slope-row-mass-x`: not touched.
  - **New candidate (proposed, not recorded by me):** `cand:sharp-spectrum-structure` = (SS)/(SS\(^*\)). It is field-free (additive combinatorics in \(\mathbb Z/N\)). It would decide (A-vertex)'s sufficient form (V) negatively. Its exact (\(\varepsilon=0\)) case is the Green–Sanders theorem (to be checked at source).
- **Ranked next tests (only if the coordinator ever reopens the line).**
  1. A literature check, at source, for robust or approximate versions of the idempotent theorem in the sparse regime. That is, sets \(\varepsilon\)-close in \(L^2\) (relative) to a function of algebra norm \(\le M\), at density \(\to0\). If such a version exists, Theorem E becomes unconditional and the verdict becomes "no".
  2. Otherwise record (A-vertex) as needing a signed estimate, with (V) expected false.

---

## 9. Verdict

**Inconclusive** (mission definition). The exact statement that would decide (V) is (SS\(^*\)) of §3:
- if it holds, (V) is refuted on (NC), with \(m_{<a}\asymp\sqrt p\) for every fixed \(a\) (Theorem E);
- (V) on (NC) would make the near-critical support a counterexample to it.

Proved along the way:
- the sector-free (NC) consequences imply neither (V) nor \(\sum g^2\gg\sqrt p\) (Proposition B);
- the uncertainty-principle heuristic fails as a mechanism, because (A2) keeps the configuration a factor 2 from equality (Proposition C);
- its exclusion claim is false for (A2)/(A6) and true for (A4) and (NC2) (Proposition D, Lemma J);
- any refutation must be prime-specific (Proposition F).

Expected answer: "no", conditional on (SS\(^*\)). The decision after this call is **hold** in every case.

---

## Replay

```bash
.venv/bin/python -B research/paley-192-vertex-exponents.py                     # exact; 48 checks, ALL OK (<1 s)
.venv/bin/python -B research/paley-192-vertex-models.py check                  # SELF-CHECK OK (<1 s)
.venv/bin/python -B research/paley-192-vertex-models.py A 10009 40009 160001 640009   # ~1 s
.venv/bin/python -B research/paley-192-vertex-models.py B 20000 4000000        # ~6 s
.venv/bin/python -B research/paley-192-vertex-sharp-search.py E                # ~5 s
.venv/bin/python -B research/paley-192-vertex-sharp-search.py S 20000          # several minutes
```

All model seeds are deterministic (seeded by \(p\) or \(N\)). numpy is from the repository `.venv`.

## Files and hashes

Written by this call only. Nothing was committed, and no coordination, acceptance or other-session file was touched.
- `research/native-claude-ordinary-nc-vertex-tightness-192.md` (this report)

| script | SHA-256 | final replay (2026-11-21) |
|---|---|---|
| `research/paley-192-vertex-exponents.py` | `ce62262687c1c0dd52d6e1e0a393660dc5c05a61304ae9e4281a899088932c0a` | 48 checks, `ALL OK` |
| `research/paley-192-vertex-models.py` | `69560155b8f84eb4b245e35c26d467b1ffe43bf3ddecc9854f486787506584ef` | `SELF-CHECK OK`; Parts A and B as quoted in §5.1–§5.2 |
| `research/paley-192-vertex-sharp-search.py` | `72389a98547ebbd79bd831ae5032f9afae4ddefd230fb1578a4bd943205c01c6` | Parts E and S as quoted in §5.3 |

The self-check verifies four things at small primes: the Legendre and primitive-root tables; \(|T_+|=(p-5)/4\) and \(|T_-|=(p-1)/4\); FFT against direct character sums, with \(G=n\|\nu\|^2\); and Lemma J for every subgroup of \(Q\) and both signs at 13 primes \(\le113\). It also checks the closed-form levels of Proposition D at four small primes.
