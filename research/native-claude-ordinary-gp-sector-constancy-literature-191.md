# Round 191 literature call: sector constancy along geometric progressions (cand:gp-sector-constancy)

- **call_id:** `ordinary-gp-sector-constancy-literature`
- **Author:** Claude subagent started by the Round 191 coordinator (session/r191-gpsub-literature). This is an agent literature report. It is not an audit, not human acceptance and not a mathematical certification.
- **Mission:** `coordination/missions/round-191/ordinary-gp-sector-constancy-literature.md`, exported from `coordination/round-190.json` (SHA-256 `b8f6e40f…4c05cc`, matches).
- **Inputs read.** All five SHA-256 values listed in the mission match (checked with `shasum -a 256` at the start of this session):
  - `research/round-189-acceptance.json` (`ad4e0b5a…6176506`): `proof_scope` (the Round 189 method cap);
  - `research/round-190-acceptance.json` (`11c42c0a…cf83409b`): the `proof_scope` and `failed_paths_and_open_bounds` entries on (GP-Sub);
  - `research/native-claude-audit-190.md` (`6237bffb…c97b80`): every passage on (GP-Sub) (overlap table; §4.3; §5 items 5–6; proposed call 3; outlook);
  - `research/native-claude-ordinary-nc-excludes-sector-laws-190.md` (`5081b11a…817`): in full (§5 defines (GP-Sub));
  - `research/native-claude-ordinary-gp-shifted-energy-literature-190.md` (`557777a4…53dd0`): in full.

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-190.md`.
- **Files written:** this report and `research/paley-191-gpsub-checks.py` (finite sanity checks, evidence only). **Nothing was committed.**

## Result summary

**Verdict: refuted** in the mission's sense: (GP-Sub) is open in the needed range. I found no published result that gives (GP-Sub\(_c\)) for any \(c\le1/\sqrt2\), or (GP-Sub\(_\kappa\)) for progressions of length \(c_0\sqrt p\) with \(c_0\le1\). A literature search cannot prove that a statement is open. The verdict rests on (i) no hit in a broad search (§6) and (ii) explicit statements, at source and as late as October 2026, that the neighbouring and stronger problems are open.

1. **Best known, (GP-Sub\(_c\)): \(c>1/\sqrt2\).**
   - Source: Hanson–Petridis Corollary 1.5 (arXiv:1905.09134v3). A sector-constant run of length \(R\) is a Paley clique (or co-clique) of size \(R+1\) (Round 190 Lemma 2), so \((R+1)R\le(p-1)/2\).
   - The 2026 refinement of Cochrane–Yip–Yoo (arXiv:2608.02568v3, Corollary 4.6) gives \(\omega(P_p)\le(1+\sqrt{2p-17})/2\) for \(p>41\). The leading constant is unchanged.
   - No published argument uses the progression structure to do better.
2. **Best known, (GP-Sub\(_\kappa\)): only for \(c_0>1\).** Vinogradov's bilinear estimate (quoted at source in HP and Gong) gives a direct consequence (§3.1):
   \[
   \#\{0<|h|\le M:\chi(1-\zeta^h)=\varepsilon\}\ \ge\ (M-\sqrt p)/2\qquad(\varepsilon=\pm1,\ 2M<\operatorname{ord}\zeta).
   \]
   - This is (GP-Sub\(_\kappa\)) for every \(\kappa<1/2\) when \(c_0>1\).
   - The Round 190 wording ("there are \(\kappa>0\) and \(c_0>0\)") is therefore already satisfied, trivially, with \(c_0>1\).
   - Criterion 5.2 needs it at \(c_0\approx\theta/2<1/4\), and nothing is known there. The candidate's wording should say "for every \(c_0>0\)" (§5).
3. **Character sums \(\sum_{k\le M}\chi(\zeta^k+a)\).** The best bound valid for every base \(\zeta\) and every shift is the completion bound \(<\sqrt p\,(\tfrac2\pi\log p+\tfrac75)\) (Yu 2001). It is trivial at \(M\asymp\sqrt p\).
   - Shteinikov (2017, Theorem 2) gives \(\ll\sqrt p(\log(K/\sqrt p)+1)\) for \(K\ge\sqrt p\). This is still \(\asymp\sqrt p\) at \(K\asymp\sqrt p\).
   - Shparlinski's 2016 problem list (Problem 1) asks for any nontrivial bound for \(\sum_{x\le N}\chi(g^x+a)\) with \(N\) small relative to \(p\).
   - Bourgain's problem for complete sums over subgroups of size \(\sim\sqrt p\) was still described as open in 2017 (Chang–Shparlinski 2014; Shteinikov 2017).
   - Nontrivial results below \(\sqrt p\) exist only for sums with an extra variable (Chang–Shparlinski 2014: an interval of shifts or a second subgroup variable), or for additive characters (Kerr 2013: \(N>p^{12/25}\)). Neither transfers to a fixed shift (§2.7–2.8).
4. **Paley cliques with multiplicative structure.** I found no bound specific to cliques that are geometric progressions or multiplicative Bohr sets. Every structured improvement of Vinogradov's bilinear bound found (Chang 2008; Shkredov–Volostnov 2017; Hanson's Bohr sets 2015) needs **additive** structure.
   - Geometric progressions have **multiplicative** structure.
   - Those theorems need \(|A+A|\le K|A|\) with \(K\) bounded. A progression has \(|AA|<2|A|\), and by the sum–product phenomenon it cannot also have small additive doubling. (I did not re-read a sum–product statement at source for this; nothing in the hypotheses of those theorems is available for progressions.)
   - The structural sum–product statements (Kim–Yip–Yoo 2023/25 Theorem 1.1; Yip 2023/25 Theorem 1.2) apply to the progression clique. They give \(c>\sqrt2\) and \(c>1/\sqrt2\) respectively, so they are no better than Hanson–Petridis.
5. **Stepanov / Hanson–Petridis adapted to progressions.** None found.
   - Every Stepanov-type result read (HP 2019/21; Kim–Yip–Yoo; Cochrane–Yip–Yoo 2026; Rudnev–Tyrrell 2026; the subgroup-shift lineage) uses only the containment of a sumset or difference set in a subgroup plus \(\{0\}\). The run structure is invisible to these arguments.
   - The closest progression analogue is for **arithmetic** progressions: a \(\sqrt{p/k}\)-type bound on the least \(k\)-th power non-residue in an AP (Forbes–Kayal–Mittal–Saha 2011).
6. **Longest constant run of \(\chi(1-\zeta^k)\).** No literature bound found below the clique bound. The Round 190 computations (runs \(\le1.69\log_2p\)) remain finite evidence only.
7. **Primality is necessary.** In \(\mathbb F_{r^2}\), a generator \(\zeta\) of \(\mathbb F_r^*\) has \(\chi(1-\zeta^k)=+1\) for all \(1\le k\le r-2=\sqrt q-2\), so (GP-Sub\(_c\)) is false there for every \(c<1\) (checked for \(r\le43\) by the script).
   - Every known positive result for \(c<1\) uses primality: HP "only works in prime fields" (their words).
   - Vinogradov's bound (\(c_0>1\)) holds in every finite field and is consistent with the \(\mathbb F_{r^2}\) run of length \(\sqrt q-2\).
8. **Statements that would imply (GP-Sub) for all \(c\)** (all open, as read at source):
   - the Paley graph conjecture (Chang survey Problem 4.3; CYY 2026: "the range δ < 1/2 remains widely open");
   - \(\omega(G_p)=o(\sqrt p)\) (Kunisky 2023: only conjecturally reachable; Randomstrasse101, Dec 2025: HP is the best bound);
   - Shparlinski's Problem 1, uniform in a base of large order.

   (GP-Sub) is a special case of Chang's Problem 3 (\(A=I\), \(B=-I\), \(|A|,|B|\sim\sqrt p\)), weakened from "nontrivial bound" to "not identically \(\pm1\)". I found no paper that states it separately.

**Effect on the project.**
- Criterion 5.1 and Criterion 5.2 of Round 190 stay **conditional**. Their hypotheses are an external open problem of Paley-clique type.
- Following the mission's mapping, the (NC) sector lever below 45/26 should be retired. A route that needs the sector condition must assume (GP-Sub) as an external input.
- No bound on \(T_0\), \(X\), \(\Gamma_{\rm tot}\) or \(\mathcal M_w\) changes. The original theta-limit target is untouched.

## 1. The statements tested (Round 190 §5, audit §5 item 5)

Notation: \(p\equiv1\pmod4\) prime, \(Q\) the nonzero squares, \(\chi\) the Legendre symbol, and \(R(\zeta)=\max\{R:\chi(1-\zeta^k)=\chi(1-\zeta)\ (1\le k\le R)\}\).

- **(GP-Sub\(_c\)).** For all large \(p\), every \(\zeta\in Q\) with \(\operatorname{ord}\zeta>c\sqrt p\) has \(R(\zeta)<c\sqrt p\).
- **(GP-Sub\(_\kappa\)).** There are \(\kappa>0\) and \(c_0>0\) such that, for all large \(p\), every symmetric \(P=\{\zeta^k:|k|\le M\}\subset Q\) with \(c_0\sqrt p\le M<\operatorname{ord}\zeta/2\) has at least \(p^\kappa\) points \(y\) with \(\chi(1-y)=\varepsilon\), for each \(\varepsilon=\pm1\).
- **Needed range.** The Round 190 Theorem 4 laws \(D_\theta\) (\(0<\theta<\tfrac12\)) need \(c\approx\theta/2<1/4\) (Round 190 §5, Criterion 5.1 status). For Criterion 5.2 to remove the \(D_\theta\) obstruction, (GP-Sub\(_\kappa\)) must hold with \(c_0\le\theta/2\), i.e. for arbitrarily small \(c_0\).
- **Translation used throughout** (Round 190 Lemma 2, accepted).
  - \(\{\zeta^k:0\le k\le R\}\) is a Paley \(\rho\)-clique iff \(\chi(1-\zeta^k)=\rho\) for \(1\le k\le R\).
  - For \(\zeta\in Q\), \(\chi(1-\zeta^{-h})=\chi(1-\zeta^h)\), since \(-1,\zeta\in Q\).
  - Hence \(\sum_{x,x'\in I}\chi(x-x')=\sum_{0<|h|\le M}(M+1-|h|)\chi(1-\zeta^h)\) for \(I=\{\zeta^j:0\le j\le M\}\). Character sums over **sets** \(A=I\), \(B=-I\) are therefore Fejér-weighted single sums over the progression.

## 2. Results read at source

### Method

- **arXiv and open-access PDFs.** Downloaded with `curl` into the session scratchpad (outside the repository) and converted to text locally with PyMuPDF. Quotes are copied from that text, with PDF ligatures normalised and mathematical symbols retyped where the extraction garbled them. The version is the one printed in the arXiv margin stamp.
- **zbMATH Open reviews.** Read through the public API (`https://api.zbmath.org/v1/document/_search`). Where zbMATH withholds the text for licence reasons, I say so.
- **Searches.** arXiv through `https://export.arxiv.org/api/query`; citing papers through the Semantic Scholar graph API; general web search.
- **Not from memory.** Nothing below is reported from memory. Items marked *not read at source* are metadata only.

### 2.1 Hanson–Petridis (the clique bound; Stepanov method)

B. Hanson, G. Petridis, *Refined estimates concerning sumsets contained in the roots of unity*, arXiv:1905.09134v3 (stamp "6 May 2020"); Proc. LMS 122 (2021) 353–358. https://arxiv.org/abs/1905.09134

> Theorem 1.2. Let p be a prime and suppose A, B ⊆ F_p satisfy A + B ⊆ Z_d ∪ {0} for some d properly dividing p − 1. Then |A||B| ≤ d + |B ∩ (−A)|.

> Corollary 1.5. Let p be a prime, d properly dividing p − 1 and suppose A ⊆ F_p is such that A − A ⊆ Z_d ∪ {0}. Then |A|(|A| − 1) ≤ d. In particular, for p ≡ 1 (mod 4), we have ω(G_p) ≤ (√(2p − 1) + 1)/2.

Also from the introduction (p. 2): Vinogradov's estimate \(|S_\chi(A,B)|\le\sqrt{p|A||B|}\), with the remark "while it is totally elementary to prove, it is still the best known estimate for S_χ(A, B)". From p. 5: "The method developed to prove Theorem 1.2 only works in prime fields."

- **Hypotheses at \(M=c\sqrt p\).** Apply it to \(A=\{\zeta^k:0\le k\le R\}\) (distinct when \(\operatorname{ord}\zeta>R\)) with \(d=(p-1)/2\). For \(\rho=-1\), apply it to \(\nu A\) with \(\nu\) a nonsquare (Round 190 audit §4.3). The hypotheses hold for every \(R\).
- **Primality.** Used ("only works in prime fields").
- **Gives:** (GP-Sub\(_c\)) for every \(c>1/\sqrt2\). Nothing for \(c\le1/\sqrt2\).
- **Gives for (GP-Sub\(_\kappa\)):** nothing. The method excludes only zero-exception configurations, and I found no robust "almost clique" version.

### 2.2 Cochrane–Yip–Yoo (2026): the current constant-term refinement

A. Cochrane, C. H. Yip, S. Yoo, *Additive decompositions of multiplicative subgroups via differential identities*, arXiv:2608.02568v3 (stamp "6 Oct 2026"). https://arxiv.org/abs/2608.02568

> Corollary 4.6. If p > 41 is prime and p ≡ 1 (mod 4), then ω(P_p) ≤ (1 + √(2p − 17))/2.

From §4.2: "Little progress beyond the trivial upper bound √p was known, until Hanson and Petridis [8] famously proved the sharper bound (√(2p−1)+1)/2." From the introduction, on the Paley graph conjecture (for \(|A|,|B|>p^\delta\), \(|\sum_{a\in A,b\in B}\chi(a+b)|\le p^{-\theta}|A||B|\)): "Standard Fourier-analytic estimates give the conjectured cancellation when δ > 1/2, while the range δ < 1/2 remains widely open".

- **Hypotheses.** Any clique, \(p>41\).
- **Primality.** Used (Stepanov / Kalmynin classification in prime fields).
- **Gives:** (GP-Sub\(_c\)) for \(c>1/\sqrt2\) with a slightly better additive constant. Same threshold. Nothing for (GP-Sub\(_\kappa\)).

### 2.3 Yip (2023/2025): clique bound through the ratio set of the connection set

C. H. Yip, *Exact values and improved bounds on the clique number of cyclotomic graphs*, arXiv:2304.13213v5 (stamp "15 Aug 2025"); Des. Codes Cryptogr. 93 (2025) 5131–5142.

> Theorem 1.2. Let q be an odd power of a prime p. Let S ⊆ F*_q with S = −S such that S/S ≠ F*_q. Then ω(Cay(F+_q; S)) < √|S/S| + 1 if q = p and ω(Cay(F+_q; S)) < √|S/S| + √(q/p) − 1 if q ≠ p.

- **Hypotheses at \(c\sqrt p\).**
  - With \(S=Q\): \(S/S=Q\), which recovers HP's \(\sqrt{p/2}\) scale.
  - A progression clique \(C\) is also a clique of \(\mathrm{Cay}(\mathbb F_p;S_C)\), \(S_C=(C-C)\setminus\{0\}\subseteq Q\). Theorem 1.2 would give \(|C|<\sqrt{|S_C/S_C|}+1\).
  - Going below \(1/\sqrt2\) would need \(|S_C/S_C|\le c^2p\) with \(c<1/\sqrt2\): an **upper** bound on the ratio set of a shifted progression. Known sum–product bounds go the other way (lower bounds on ratio sets). So the theorem gives nothing new here.
  - *(Agent hypothesis check, not a theorem.)*
- **Primality.** The \(q=p\) case is stated separately.
- **Gives:** (GP-Sub\(_c\)) for \(c>1/\sqrt2\) only.

### 2.4 Kim–Yip–Yoo: product sets inside shifted subgroups (multiplicative HP analogue)

S. Kim, C. H. Yip, S. Yoo, *Multiplicative structure of shifted multiplicative subgroups and its applications to Diophantine tuples*, arXiv:2309.09124v4 (stamp "12 Feb 2025"); Canad. J. Math. 78 (2026) 1861–1901.

> Theorem 1.1. Let d | (q − 1) with d ≥ 2. Let S_d = {x^d : x ∈ F*_q}. Let A, B ⊂ F*_q and λ ∈ F*_q with |A|, |B| ≥ 2. Assume further that binom(|A|−1+(q−1)/d, |A|) ≢ 0 (mod p) if q ≠ p. If AB + λ ⊂ S_d ∪ {0}, then |A||B| ≤ |S_d| + |B ∩ (−λA^{−1})| + |A| − 1. Moreover, when λ ∈ S_d, we have a stronger upper bound: |A||B| ≤ |S_d| + |B ∩ (−λA^{−1})| − 1.

- **Hypotheses.** A \(\rho=+1\) run of length \(R\) gives \(AB+1\subseteq Q\cup\{0\}\) with \(A=\{-\zeta^a:1\le a\le s\}\), \(B=\{\zeta^b:0\le b\le R-s\}\), \(\lambda=1\in Q\). The intersection term vanishes when \(\operatorname{ord}\zeta>R\). This gives \(s(R-s+1)\le(p-1)/2-1\), hence \(R\lesssim\sqrt{2p}\).
- **Primality.** The theorem covers all finite fields (with a binomial condition). Its use of a product decomposition of the run loses a factor 2.
- **Gives:** (GP-Sub\(_c\)) for \(c>\sqrt2\) only. This is weaker than HP and nothing new. The arithmetic is checked in the script, Part X.

### 2.5 Vinogradov's bilinear estimate (the elementary barrier)

As quoted in HP v3 p. 2:

> Theorem (Vinogradov). For any subsets A and B of F_p and any non-trivial multiplicative character χ, we have the estimate |S_χ(A, B)| ≤ √(p|A||B|).

Gong (arXiv:1401.4618v1, Lemma 3) gives the weighted version, \(\sum_{x,y}\xi(x)\eta(y)\chi(xy+a)\) bounded by \(\sqrt{pXY}\).

- **Hypotheses.** None beyond finite field and nontrivial \(\chi\).
- **Primality.** Not used.
- **Gives:**
  - (GP-Sub\(_c\)) for \(c>1\) (Round 190 Lemma 2).
  - (GP-Sub\(_\kappa\)) for \(c_0>1\), \(\kappa<1/2\) (§3.1).
  - Nothing at \(c,c_0\le1\).

### 2.6 Single sums along progressions: \(\sum_{x\le N}\chi(g^x+a)\) and subgroup sums

**(a) Yu (completion bound).** H. Yu, *Estimates of character sums with exponential function*, Acta Arith. 97 (2001) 211–218, zbMATH 1002.11067. The review by J. Hinz is quoted through the zbMATH API. The same theorem is restated as Theorem 1 by Shteinikov in (b).

> Let n ≥ 2 and λ be integers satisfying (n, λ) = 1 and λ belonging to the exponent d modulo n. Given a primitive Dirichlet character χ mod n the author proves the estimate |Σ_{x=1}^X χ(aλ^x + b)| < √n ((2/π) log n + 7/5). Here a, b and X are integers satisfying (ab, n) = 1 and 1 ≤ X ≤ d. In certain cases this inequality is essentially best possible.

- **Hypotheses at \(X=c\sqrt p\).** All satisfied, uniformly in the base and shift.
- **Gives:** a bound \(\gg X\). Trivial for (GP-Sub\(_c\)) and (GP-Sub\(_\kappa\)) whenever \(X\lesssim\sqrt p\log p\).

**(b) Shteinikov.** Yu. N. Shteinikov, *Character sums over shifted powers*, Chebyshevskii Sb. 18:2 (2017) 267–274, http://www.chebsbornik.ru/jour/article/viewFile/337/302. The abstract (English version printed in the paper):

> The case when the cardinality of subgroup is less than √p, it is a question of non-trivial upper bounds for such sums that remains open and is unsolved today. It was proposed by J. Burgain and M.Ch. Chang in the review of 2010.

From §1:

> Problem (J. Bourgain) Let G - subgroup, G ⊂ Z*_p, |G| ∼ p^{1/2}, p → ∞, χ – nontrivial character modulo p, gcd(a, p) = 1. Obtain nontrivial upper estimate in the following form |S(χ, a, G)| = o(|G|), p → ∞.

> Theorem 2. Let K ≥ p^{1/2}, χ – is a multiplicative character modulo p. Than the following estimate holds |S(χ, a, l, K)| ≪ √p (log(K/√p) + 1).

Here \(S(\chi,a,l,K)=\sum_{1\le k\le K}\chi(a+l^k)\).

- **Hypotheses.** \(K\ge\sqrt p\), so the theorem does not apply below \(\sqrt p\).
- **At \(K=c\sqrt p\), \(c\ge1\).** The bound is \(O(\sqrt p)\), with an absolute but unspecified constant, so it is not \(o(K)\).
- **Gives:** nothing for (GP-Sub) at \(c\le1\).
- **Relation to Bourgain's problem.** Bourgain's problem is about complete subgroups. The part of (GP-Sub\(_c\)) where the run covers all of \(\langle\zeta\rangle\) is "no subgroup Paley (co-)clique of order \(>c\sqrt p+1\)". That is \(\sum_{h\in H}\chi(1-h)\ne\pm(|H|-1)\), the non-constancy special case of Bourgain's problem with \(a=-1\). It too is open below \(1/\sqrt2\) (Round 184 (Sub\(_C\))).

**(c) Gong.** K. Gong, *An elementary approach to character sums over multiplicative subgroups*, arXiv:1401.4618v1 (18 Jan 2014).

> Problem 1 (J. Bourgain). Obtain nontrivial bound on Σ_{x∈H} χ(x + a) for H < F*_p, |H| ∼ √p, and a ∈ F*_p.

> Theorem 2. For any H < F*_p, we have max_{a∈F*_p} |Σ_{x∈H} χ(x + a)| < p^{1/2}.

- **Gives:** the trivial bound at \(|H|\sim\sqrt p\).

**(d) Chang's survey.** M.-C. Chang, *Character sums in finite fields*, Contemp. Math. 518 (2010) 83–98 (citation as given in Gong's bibliography), PDF https://math.ucr.edu/~mcc/paper/DubProc.pdf.

> Problem 4.3. Let χ be the quadratic character mod p (or any non-trivial character). Prove that for some γ = γ(δ) > 0 |Σ_{x∈A, y∈B} χ(x + y)| < p^{−γ}|A| |B| holds, for arbitrary subsets A, B ⊂ F_p of size |A| > p^δ, |B| > p^δ and p large enough.

> Problem 3. Obtain a nontrivial estimate on Σ_{x∈A,y∈B} χ(x + y) for A, B ⊂ F_p arbitrary, and |A|, |B| ∼ √p. Problem 4. (Sarnak) In Problem (3), consider A = B = H < F*_p with |H| ∼ √p. Problem 5. (Bourgain) Obtain nontrivial bound on Σ_{x∈H} χ(a + x) for H < F*_p, |H| ∼ √p, and a ∈ F*_p.

The survey also says (§4): "For q = p prime, it is conjectured that the clique number is ∼ log p."

- **Relation.**
  - Problem 3 with \(A=I\), \(B=-I\), \(I\) a progression of length \(\sim\sqrt p\), is the bilinear form of (GP-Sub) (§1, translation). (GP-Sub\(_c\)) asks only for "not \(\pm\)maximal".
  - Problem 4.3 (the Paley graph conjecture) implies (GP-Sub\(_c\)) for all \(c\) and (GP-Sub\(_\kappa\)) for all \(c_0\) with every \(\kappa<1/2\), by the computation of §3.1 with \(p^{-\gamma}|A||B|\) in place of \(\sqrt{p|A||B|}\). *(One-line consequence; agent check.)*

**(e) Shparlinski's problem list.** I. E. Shparlinski, *Open Problems on Exponential and Character Sums*, version "May 4, 2016", https://web.maths.unsw.edu.au/~igorshparlinski/CharSumProjects.pdf, §3.1:

> Problem 1. Obtain analogues of the results of J. Bourgain, A. A. Glibichuk and S. V. Konyagin [35] for multiplicative character sums Σ_{x1,...,xk∈X} χ(x1 . . . xk + a) and Σ_{x=1}^{N} χ(g^x + a) with very small values of N relative to p, where X ⊆ Z_p, gcd(g, p) = 1 and χ is a nonprincipal multiplicative character modulo p

**(f) Chang–Shparlinski, §1.1.** M.-C. Chang, I. E. Shparlinski, *Double character sums over subgroups and intervals*, arXiv:1401.6611v2 (stamp "15 Feb 2014"); Bull. Aust. Math. Soc. 2014.

> the multiplicative analogues of the sums (1), that is, the sums Σ_{λ∈G} χ(a + λ), a ∈ F*_p, with a nonprincipal multiplicative character χ of F_p have been resisting all attempts to improve the classical bound (2) |Σ_{λ∈G} χ(a + λ)| ≤ √p.

**Primality, items (a)–(f).** Yu's bound holds for any modulus (completion plus Gauss sums). Problems 3–5 and 4.3 are posed for prime \(p\).

### 2.7 Double sums with an extra averaging variable (nontrivial below \(\sqrt p\), but not for a fixed shift)

Chang–Shparlinski (arXiv:1401.6611v2), with \(S_\chi(a,I,G)=\sum_{x\in I}\sum_{\lambda\in G}\chi(x+a\lambda)\), \(I=\{1,\dots,H\}\):

> Theorem 1. For every fixed real ε > 0 there are some δ > 0 and η > 0 such that if H > p^ε and T > p^{1/2−δ} then for the interval I = {1, . . . , H} and the multiplicative subgroup G ⊆ F*_p of order T, we have S_χ(a, I, G) = O(HTp^{−η}) uniformly over a ∈ F*_p and nonprincipal multiplicative characters χ of F_p.

> Theorem 4. Let T ≤ p^{2/3}. Then for the multiplicative subgroup G ⊆ F*_p of order T, we have |T_χ(a, G)| ≤ T^{19/26} p^{1/2+o(1)}, if T ≤ p^{1/2}, [...] uniformly over a ∈ F*_p and nonprincipal multiplicative characters χ of F_p.

(The second and third ranges of Theorem 4 are omitted here; \(T_\chi(a,G)=\sum_{\lambda,\mu\in G}\chi(a+\lambda+\mu)\). The text adds that it is nontrivial for \(T\ge p^{13/33+\varepsilon}\).)

- **Hypotheses at our scale.**
  - Theorem 1 averages over \(H>p^\varepsilon\) additive shifts \(x\) and needs a full subgroup of order \(>p^{1/2-\delta}\).
  - Theorem 4 has a three-term argument \(a+\lambda+\mu\) with \(a\ne0\). Our sum \(\sum_{\lambda,\mu\in I}\chi(\lambda-\mu)\) has \(a=0\) and is over a progression, not a subgroup.
  - An average over shifts does not control the single shift \(a=-1\), and a progression segment is not a subgroup.
- **Primality.** Used (sum–product in \(\mathbb F_p\)).
- **Gives:** nothing for (GP-Sub).

Related, **not read at source:** Shparlinski–Yau, *Bounds of double multiplicative character sums and gaps between residues of exponential functions*, J. Number Theory 167 (2016) 304–316 (Crossref metadata only; the ScienceDirect page returned 403 and zbMATH withholds the review). Web-search snippets describe double sums of the same "interval × powers" type. The same fixed-shift gap would apply, but I did not verify its statements.

### 2.8 Structured bilinear sums and the additive-character analogue

These results are nontrivial below \(\sqrt p\), but only under **additive** structure or for **additive** characters.

**(a) Additive structure.**
- **Chang 2008.** M.-C. Chang, Duke Math. J. 145 (2008) 409–442, zbMATH 1241.11137 (review by O. Ninnemann, via the API). For \(|A|,|B|>p^{4/9+\varepsilon}\) and \(|B+B|<k|B|\): \(|\sum_{x\in A,y\in B}\chi(x+y)|<p^{-\tau}|A||B|\).
- **Shkredov–Volostnov 2017.** Proc. Steklov Inst. 296, arXiv:1606.00358, zbMATH 1371.11127 (review by J. H. Loxton). The same with \(|A|,|B|>p^{12/31+\delta}\), \(|A+A|<K|A|\), \(|B+B|<L|B|\).
- **Hanson 2015** (Bohr sets). arXiv:1409.7924, Canad. Math. Bull. 58 (2015), zbMATH 1334.11064 (review by J. H. Loxton). Pólya–Vinogradov and Burgess analogues for **additive** Bohr sets \(B(\Gamma,\varepsilon)=\{x:\|xr/p\|\le\varepsilon\ \forall r\in\Gamma\}\).
- **Why none applies.** A geometric progression \(I\) of length \(\asymp\sqrt p\) has \(|II|<2|I|\), but nothing gives \(|I+I|\le K|I|\) with \(K\) bounded. Sum–product heuristics say the opposite; no source was re-read for this. The small-additive-doubling hypotheses are not available.
  - HP v3 p. 3 lists the structured improvements as: "In the case that A or B is highly structured, Vinogradov's estimate can be improved. Theorems of this sort can be found in [Bu1], [Bu2], [FI], [Ch], [SS], [SV] and [Vol]".
  - The ones I could check (Chang [Ch], Shkredov–Volostnov [SV], Volostnov [Vol], arXiv:1712.09355 abstract: "sets, having small additive doubling") are additive.
  - I found no analogue for small **multiplicative** doubling.

**(b) Additive characters along progressions.** B. Kerr, *Incomplete exponential sums over exponential functions*, arXiv:1302.4170v1 (stamp "18 Feb 2013"), with \(S_{g,p}(\lambda,N)=\sum_{n\le N}e_p(\lambda g^n)\):

> Theorem 2. For g ∈ F*_p of order t and integer N ≤ t, we have max_{gcd(λ,p)=1} |S_{g,p}(λ, N)| ≤ p^{1/8} N^{71/96+o(1)} for N ≤ t^{1/2}, [...]

Nontrivial for \(N>p^{12/25+\varepsilon}\), below \(\sqrt p\) (Part X).

- **Why it does not transfer.** Writing \(\chi(1-y)=\tau(\bar\chi)^{-1}\sum_t\bar\chi(t)e_p(t(1-y))\) gives
  \[
  \Bigl|\sum_{k\le N}\chi(1-\zeta^k)\Bigr|\le p^{-1/2}\sum_{t\ne0}|S_{\zeta,p}(-t,N)|,
  \]
  Since \(\sum_{t\ne0}|S_{\zeta,p}(t,N)|^2=pN-N^2\) and \(|S|\le N\), the right side is at least \(p^{-1/2}(p-N)\). That is \(\ge N\), hence trivial, whenever \(N\le\sqrt p\), whatever bound on the individual additive sums is used. Kerr's fourth-moment Theorem 1 gives \(\sqrt p\,N^{71/96+o(1)}\) on this route, which is worse than trivial.
  - *(Agent remark explaining why the additive results are not usable; not a theorem.)*
- **Gives:** nothing for (GP-Sub).

### 2.9 State of the art on Paley cliques (corroboration)

- **Kunisky 2023.** D. Kunisky, arXiv:2303.16475v1 (29 Mar 2023), abstract (arXiv API text):

  > once a ≥ 3, this (conjectural) convergence of the minimum eigenvalue would imply bounds on the clique number of the Paley graph improving on the current state of the art due to Hanson and Petridis (2021), and that this convergence for all a ≥ 1 would imply that the clique number is o(√p).

- **Randomstrasse101 2025.** *On the clique number of the Paley Graph (problems 25–29)*, posted Dec 15, 2025, updated Dec 18, 2025, https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/ (read through WebFetch; quote as returned by that tool):

  > ω(G_p) ≤ (1 + o(1))√(p/2)

  The post attributes this to Hanson–Petridis as the current bound. It poses Conjecture 25, \(\omega(G_p)=O(\mathrm{polylog}(p))\). (Its Conjecture 26 concerns the theta number of the 1-localization, which is the project's own target; I note this only for the coordinator.)
- **Bachoc–Matolcsi–Ruzsa 2013.** arXiv:1305.0577v1, abstract: \(|B|\le\sqrt p-1\) for about three quarters of primes \(p=4k+1\). Superseded.
- **arXiv listing.** The arXiv listing of Paley clique / independence papers sorted by date (through 2026-11-18) and the Semantic Scholar list of papers citing HP show no prime-field improvement of the \(1/\sqrt2\) constant.

### 2.10 Runs (item d) and Stepanov for progressions (item c)

- **Arithmetic progressions.** M. Forbes, N. Kayal, R. Mittal, C. Saha, arXiv:1104.4557v1, abstract: "the value of the least k-th power non-residue in an arithmetic progression {bn+c}, over a prime field F_p, is bounded by 7/√5 · b · √(p/k) + 4b + c", by a Stepanov-type auxiliary polynomial. This handles arithmetic progressions only. For intervals the classical run bounds (Burgess) are far below \(\sqrt p\). For geometric progressions there is no analogue.
- **Subgroup and decomposition Stepanov arguments.**
  - Read at source (§2.1–2.4): HP, Kim–Yip–Yoo, Cochrane–Yip–Yoo, Yip.
  - Abstracts read: Rudnev–Tyrrell, arXiv:2607.24270v2 ("Multiplicative Subgroups of Prime Fields Are Not Sumsets"); Yoo, arXiv:2607.24370v1; A. Cochrane, arXiv:2602.04111v2.
  - Their inputs are containments \(A+B\subseteq H\cup\{0\}\) or \(AB+\lambda\subseteq S_d\cup\{0\}\), or equalities. None uses or recovers the run structure \(\{\zeta^k\}_{k\le R}\) beyond the clique property.
- **Runs.** I found no paper bounding \(R(\zeta)\), or the longest run of residues or non-residues in \(\{\zeta^k+a\}\), below the clique bound.
- **Konyagin–Shparlinski book.** S. V. Konyagin, I. E. Shparlinski, *Character Sums with Exponential Functions and Their Applications*, Cambridge Tracts 136 (1999). It has a chapter "Bounds of Short Character Sums" (pp. 26–30) and "Distribution of Powers of Primitive Roots" (pp. 131–140), per the Cambridge table of contents. It was **not read at source**: no access. Shparlinski's 2016 Problem 1 (§2.6(e)) and Chang–Shparlinski 2014 (§2.6(f)) postdate it and treat the short multiplicative case as open.

## 3. Hypothesis checks that use only quoted statements

### 3.1 What Vinogradov's estimate gives for (GP-Sub\(_\kappa\))

Let \(\zeta\in Q\), \(2M<\operatorname{ord}\zeta\), \(I=\{\zeta^j:0\le j\le M\}\), \(\rho\in\{\pm1\}\), and \(E_\rho=\#\{0<|h|\le M:\chi(1-\zeta^h)=-\rho\}\).
- By §1, \(\rho\sum_{x,x'\in I}\chi(x-x')=\sum_{0<|h|\le M}(M+1-|h|)\rho\chi(1-\zeta^h)\ge M(M+1)-2E_\rho M\).
- By Vinogradov with \(A=I\), \(B=-I\), the left side is at most \(\sqrt p(M+1)\).
- Hence \(E_\rho\ge(M-\sqrt p)/2\). This is an elementary consequence of the quoted theorem, in the same way as Round 190 Lemma 2. The script (Part V) checks the inequality exhaustively for \(p\le1000\): 3,431,852 cases, no violation.
- **Consequence.**
  - (GP-Sub\(_\kappa\)) with \(c_0>1\) holds for every \(\kappa<1/2\) (\(\ge(c_0-1)\sqrt p/2\) points of each sign).
  - At \(c_0\le1\) the bound is vacuous.
  - Under the Paley graph conjecture, \(\sqrt p(M+1)\) is replaced by \(p^{-\gamma}(M+1)^2\), and the same lines give \(E_\rho\ge(1-o(1))M/2\) for every \(c_0>0\).

### 3.2 Primality is necessary for any \(c<1\)

- In \(\mathbb F_{r^2}\), \(\mathbb F_r\subset\) squares, so \(\{1,\zeta,\dots,\zeta^{r-2}\}=\mathbb F_r^*\) is a clique when \(\zeta\) generates \(\mathbb F_r^*\). Then \(R(\zeta)=r-2=\sqrt q-2\) with \(\operatorname{ord}\zeta=\sqrt q-1\). This is the \(\mathbb F_{r^2}\) control of Rounds 184/190, now read as a (GP-Sub) counterexample. The script, Part F, checks it for \(r\in\{7,11,19,23,31,43\}\).
- So no field-general argument can give (GP-Sub\(_c\)) for \(c<1\).
- **Consistency.** HP and CYY use primality explicitly. Vinogradov's \(c>1\) and \(c_0>1\) statements are field-general and consistent with this example.

### 3.3 Summary table

| result (source, version) | form | hypotheses at \(M\asymp c\sqrt p\), \(\operatorname{ord}\zeta>4M\) | primality | (GP-Sub\(_c\)) | (GP-Sub\(_\kappa\)) |
|---|---|---|---|---|---|
| Vinogradov (as in HP v3 p. 2; Gong Lemma 3) | \(\lvert S_\chi(A,B)\rvert\le\sqrt{p\lvert A\rvert\lvert B\rvert}\) | hold | no | \(c>1\) | \(c_0>1\), \(\kappa<1/2\) (§3.1) |
| Hanson–Petridis 1905.09134v3 Cor. 1.5 | \(\lvert A\rvert(\lvert A\rvert-1)\le d\) if \(A-A\subseteq Z_d\cup\{0\}\) | hold | yes | **\(c>1/\sqrt2\)** (best) | none |
| Cochrane–Yip–Yoo 2608.02568v3 Cor. 4.6 | \(\omega\le(1+\sqrt{2p-17})/2\), \(p>41\) | hold | yes | \(c>1/\sqrt2\) (constant term only) | none |
| Yip 2304.13213v5 Thm 1.2 | \(\omega<\sqrt{\lvert S/S\rvert}+1\) | hold; useful only if \(\lvert S_C/S_C\rvert\le c^2p\) (not available) | \(q=p\) case | \(c>1/\sqrt2\) | none |
| Kim–Yip–Yoo 2309.09124v4 Thm 1.1 | \(\lvert A\rvert\lvert B\rvert\le\lvert S_d\rvert+\dots\) if \(AB+\lambda\subseteq S_d\cup\{0\}\) | hold (run = product of two halves) | no | \(c>\sqrt2\) | none |
| Yu 2001 (zbMATH 1002.11067) | \(\lvert\sum_{x\le X}\chi(a\lambda^x+b)\rvert<\sqrt n(\frac2\pi\log n+\frac75)\) | hold | no | trivial | trivial |
| Shteinikov 2017 Thm 2 | \(\ll\sqrt p(\log(K/\sqrt p)+1)\), \(K\ge\sqrt p\) | fail below \(\sqrt p\) | yes | none | none |
| Gong 1401.4618v1 Thm 2 | subgroup sum \(<\sqrt p\) | subgroups only | no | none | none |
| Chang–Shparlinski 1401.6611v2 Thms 1, 4 | double sums, interval or second subgroup variable | fail (fixed shift; segment is not a subgroup) | yes | none | none |
| Chang 2008; Shkredov–Volostnov 2017; Hanson 2015 | bilinear or Bohr bounds under additive structure | fail (no additive structure) | yes | none | none |
| Kerr 1302.4170v1 Thm 2 | additive \(e_p(\lambda g^n)\), \(N>p^{12/25}\) | additive character only; no transfer (§2.8) | yes | none | none |
| Forbes–Kayal–Mittal–Saha 1104.4557v1 | AP non-residue, \(\sqrt{p/k}\) | arithmetic, not geometric, progressions | yes | none | none |

## 4. Best known range and exact gaps

- **(GP-Sub\(_c\)).**
  - Known: every \(c>1/\sqrt2\), for all large \(p\). Source: HP Cor. 1.5 (arXiv:1905.09134v3), with the constant-term refinement CYY Cor. 4.6 (arXiv:2608.02568v3). Precisely, \(R(\zeta)+1\le(1+\sqrt{2p-17})/2\) for \(p>41\).
  - Needed: \(c\approx\theta/2<1/4\) for every \(\theta\in(0,\tfrac12)\), i.e. all \(c>0\) in practice.
  - **Gap:** \(c\in(0,1/\sqrt2]\). No partial result inside the gap (for example \(c>1/\sqrt2-\eta\)) was found.
- **(GP-Sub\(_\kappa\)).**
  - Known: \(c_0>1\), any \(\kappa<1/2\) (§3.1, from Vinogradov).
  - Needed (for Criterion 5.2 to touch \(D_\theta\)): \(c_0\le\theta/2<1/4\), with \(5\kappa>\delta\) for the targeted \(\delta\) (Round 190 Criterion 5.2 with the audit's \(p^{16/13}\) threshold).
  - **Gap:** \(c_0\in(0,1]\). Zero-exception results (HP) do not even give \(\kappa>0\) at \(c_0\in(1/\sqrt2,1]\). Excluding a single all-one-sign run is weaker than having \(p^\kappa\) points of each sign.
- **Character sums.** Every bound valid for each base \(\zeta\) and the fixed shift \(-1\) is \(\gg\sqrt p\) at \(M\lesssim\sqrt p\). Nontrivial bounds below \(\sqrt p\) exist only with an extra averaging variable or for additive characters.
- **What would close the gap (all open):**
  - the Paley graph conjecture (Chang Problem 4.3; CYY 2026 "widely open" for \(\delta<1/2\));
  - \(\omega(G_p)=o(\sqrt p)\) (Kunisky 2023; Randomstrasse101 2025);
  - Shparlinski 2016 Problem 1 uniformly in bases of order \(\ge\sqrt p\).

  For (GP-Sub\(_c\)) restricted to subgroups, the "non-constancy" case of Bourgain's problem would also do (Chang Problem 5; Gong 2014; Shteinikov 2017).

## 5. What this changes for the project (agent assessment; for the coordinator)

- **`cand:gp-sector-constancy`.**
  - Proposed record: "open below \(c=1/\sqrt2\) (Hanson–Petridis Cor. 1.5; CYY 2026 Cor. 4.6 refines only the constant term); quantitative form known only for \(c_0>1\) (Vinogradov); false in \(\mathbb F_{r^2}\) for \(c<1\), so primality is necessary".
  - **Wording correction.** The quantitative form should read "for every \(c_0>0\) there is \(\kappa>0\)…", or name \(c_0\le1/4\) explicitly. As recorded ("there are \(\kappa>0\) and \(c_0>0\)"), it is true with \(c_0>1\) by Vinogradov and does not reach \(D_\theta\). This corrects a statement; it does not change any accepted mathematics.
- **Round 190 Criteria 5.1 and 5.2** stay conditional. Their conditions are now documented as an external open problem of Paley-clique type. It is a special case of Chang's Problem 3, but I found no source that treats the special case.
- **Mission outcome mapping ("If refuted").** Record (GP-Sub) as an external open problem and retire the (NC) sector lever below 45/26. Any ordinary route below 45/26 then needs:
  - (GP) below \(|I|^{32/13}\) (`cand:gp-shifted-energy`, Round 190); or
  - (GP-Sub) as an assumption; or
  - an argument that uses neither.

  This report supplies no such argument.
- **Unchanged.** \(T_0\), \(X\), \(\Gamma_{\rm tot}\), \(\mathcal M_w\), the one-match exponent 43/24, the (A) and (F) obligations, and the original target.
- **Finite evidence.** Round 190 §7.2 found maximal runs \(\le1.69\log_2p\) up to \(2\cdot10^5\) and 25 at \(p=3\cdot10^7\). This matches the folklore expectation \(\omega(G_p)=O(\mathrm{polylog}\,p)\) (Randomstrasse101 Conjecture 25; Chang: "conjectured that the clique number is ∼ log p"). It remains finite evidence.

## 6. Search coverage and what was not read

- **Searched.**
  - General web search, several phrasings: \(\chi(g^x+a)\) short sums, Paley cliques as geometric progressions, multiplicative Bohr sets, Stepanov for progressions, least non-residue of \(g^n+a\), Bourgain's subgroup problem 2020–2026, Paley clique improvements 2025–2026.
  - The arXiv API: Paley clique or independence papers by date; Hanson–Petridis follow-ups; Stepanov with subgroups; shifted subgroups; Shparlinski, Kerr, Garaev, Shkredov, Cilleruelo–Garaev listings.
  - zbMATH Open API reviews for: Friedlander–Hansen–Shparlinski 2000, Konyagin–Shparlinski 1999, Yu 2001, Shteinikov 2017, Winterhof 2001, Hanson 2015/2017, Chang 2008, Shkredov–Volostnov 2017, Shkredov–Shparlinski 2018, Garaev 2006, Hanson–Petridis.
  - Semantic Scholar citations of HP (about 70 papers screened by title) and of Gong 2014.
- **Read at source (PDF text).** HP 1905.09134v3; Chang–Shparlinski 1401.6611v2; Gong 1401.4618v1; Shteinikov 2017; Chang survey (DubProc.pdf); Shparlinski 2016 problem list; Yip 2304.13213v5; Kim–Yip–Yoo 2309.09124v4; CYY 2608.02568v3; Kerr 1302.4170v1. Also scanned: Ostafe–Shparlinski–Voloch 2110.10941v1, Shkredov 2307.03156v1, Bourgain–Garaev–Konyagin–Shparlinski 1110.0812 (open questions section).
- **Abstracts only.** Kunisky 2303.16475; Rudnev–Tyrrell 2607.24270; Yoo 2607.24370; A. Cochrane 2602.04111; Zhelezov 1507.05548; Cilleruelo–Garaev 1404.5070; Garaev 1810.06341; Volostnov 1712.09355; Bachoc–Matolcsi–Ruzsa 1305.0577; Forbes et al. 1104.4557; Hanson 1409.7924 (and zbMATH review).
- **Not read** (no access, or the review was withheld):
  - the Konyagin–Shparlinski book (1999);
  - Friedlander–Hansen–Shparlinski, Mathematika 47 (2000) (the zbMATH review describes additive sums with \(\vartheta^{x^n}\), \(\vartheta^{e^x}\));
  - Shparlinski–Yau JNT 2016;
  - Shkredov–Shparlinski Mathematika 2017;
  - Garaev's 2010 survey;
  - journal versions of the arXiv papers.

  A result in these that solves (GP-Sub) for \(c\le1/\sqrt2\) would contradict the 2014–2017 open-problem statements and the 2026 CYY remark quoted above. I therefore consider such a result unlikely, but I have not verified its absence.

## Replay

```bash
python3 -B research/paley-191-gpsub-checks.py              # Part V (p <= 400), Part F, Part X: ALL OK (< 1 s)
python3 -B research/paley-191-gpsub-checks.py --pmax 1000  # Part V exhaustive to p <= 1000 (~3 s)
```

Output of the final run, 2026-11-21:
- Part V held in all 3,431,852 cases for \(p\le1000\). The smallest margin is 1.062 (\(p=17\), \(\zeta=8\), \(M=2\)).
- Part F gave \(R(\zeta)=r-2\) for \(r=7,11,19,23,31,43\).
- Part X: `ALL OK`.

Evidence label: finite exact checks of an elementary consequence of a quoted theorem and of the \(\mathbb F_{r^2}\) control; not certificates. Literature quotations: at source unless marked otherwise. The proofs of the quoted theorems were not re-verified.

| script | SHA-256 |
|---|---|
| `research/paley-191-gpsub-checks.py` | `91a88be66d03f7d3e231a47b666ecfa02fba2449acceb0a954a52f8b51291a58` |

## Verdict

**Refuted** (mission definition: "(GP-Sub) is open"). It is open as far as this search reaches, and corroborated by explicit open-problem statements up to 2026.
- **Best known:**
  - (GP-Sub\(_c\)) for \(c>1/\sqrt2\): Hanson–Petridis Cor. 1.5; Cochrane–Yip–Yoo Cor. 4.6 refines the constant term.
  - (GP-Sub\(_\kappa\)) for \(c_0>1\), \(\kappa<1/2\): Vinogradov.
- **Needed:** \(c,c_0\approx\theta/2<1/4\).
- **Gaps:** \(c\in(0,1/\sqrt2]\) and \(c_0\in(0,1]\).
- **No relevant transfer.** No character-sum bound for \(\sum_{k\le M}\chi(\zeta^k+a)\) at \(M\lesssim\sqrt p\) beats the completion bound. No clique bound uses the progression structure. No Stepanov argument for progressions exists in the literature read.
- **Primality is necessary** for any \(c<1\) (the \(\mathbb F_{r^2}\) example).
- **Recorded wording.** The recorded quantitative form should be re-quantified "for every \(c_0>0\)".
