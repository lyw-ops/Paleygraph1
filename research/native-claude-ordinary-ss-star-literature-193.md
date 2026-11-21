# Round 193 native Claude literature report: is (SS\*) a published theorem?

- **call_id:** `ordinary-ss-star-literature`
- **Author:** Claude session started by the Round 193 coordinator (generation-2 brain), working alone. This is an agent literature report. It is not an audit, not human acceptance and not a mathematical certification. Nothing was committed.
- **Mission:** `coordination/missions/round-193/ordinary-ss-star-literature.md` (SHA-256 `6b539911…ee063`), exported from `coordination/round-192.json` (SHA-256 `6237ed51…7fcbf`, matches the mission header).
- **Sources checked.** All four SHA-256 values listed in the mission match the files on disk (`shasum -a 256`, start of session):
  - `research/round-191-acceptance.json` (`51b86804…9538`);
  - `research/round-192-acceptance.json` (`25a7b70e…1041`);
  - `research/native-claude-ordinary-nc-vertex-tightness-192.md` (`509e0d40…d98b`): §§0–3 read in full (R192 below);
  - `research/native-claude-audit-192.md` (`455c97ed…d85b`): §2.9 and §§4.2–4.4 read in full (AUD192 below).

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, and the (GP-Sub) statements of `research/native-claude-ordinary-gp-sector-constancy-literature-191.md` (§0 items 1–8) and `research/native-claude-audit-191.md` (g4, g7).
- **Files written:** this report and `research/paley-193-ssstar-checks.py` (floating-point diagnostics on small examples; evidence only). Nothing else.
- **How sources were read.** Every paper cited as "read at source" was downloaded as a PDF from arXiv (or the author's page), converted to text, and the quoted theorem was read in that text, with its hypotheses. Page and theorem numbers below refer to those files. Two sources were *not* retrieved and are marked as such (§2.7).

**Normalisations (used throughout).** \(S\subseteq\mathbb Z/N\), \(\alpha=|S|/N\), \(\widehat{\mathbf 1_S}(\xi)=\sum_{x\in S}e(-x\xi/N)\), \(g(\xi)=|\widehat{\mathbf 1_S}(\xi)|^2/|S|^2\), so \(\sum_\xi g=N/|S|=1/\alpha\) and \(M=N/|S|-1\). The algebra (Wiener, spectral) norm is the one of Green–Sanders, Sanders and Konyagin–Shkredov: \(\|f\|_A=\sum_\xi|N^{-1}\sum_xf(x)e(-x\xi/N)|\). So \(\|\mathbf 1_S\|_A=N^{-1}\sum_\xi|\widehat{\mathbf 1_S}(\xi)|=\alpha\sum_\xi g^{1/2}\). "Sharp at level \(a\)" means \(\sum_{\xi\ne0,\,g(\xi)<a}g(\xi)=o(M)\) along the sequence (R192 §3).

---

## 0. Answer in brief

**Verdict: refuted** in the mission's sense: I found no published theorem that implies (SS\*) or (SS\*\*). (SS\*) stays an internal open problem; Theorem E of Round 192 stays conditional. A literature search cannot prove that no source exists; the verdict rests on reading the natural candidates at source (§2) and on a precise account of which parameter each one fails to reach (§3).

1. **The exact case is a theorem (new bookkeeping, derived in full here).** If \(g(\xi)\in\{0\}\cup[a,1]\) for *every* \(\xi\), then \(\|\mathbf 1_S\|_A\le a^{-1/2}\) (Lemma 2(i)).
   - Composite \(N\): Green–Sanders Theorem 1.3 (arXiv:math/0611286) gives \(\mathbf 1_S=\sum_{j\le L}\pm\mathbf 1_{x_j+H_j}\) with \(L\le\exp\exp(Ca^{-2})\) and at most \(a^{-1/2}+\frac1{100}\) distinct \(H_j\); Sanders (arXiv:1610.07092, Theorem 1.1) improves \(L\) to \(\exp(a^{-2-o(1)})\). The spectrum then lies *exactly* in a bounded union of subgroups. Proposition 3 below turns this into the order window of (SS) in an "\(\varepsilon\)-form": for each \(\varepsilon>0\), at most \(a^{-1/2}+\frac1{100}\) subgroups with orders in \([\eta N/|S|,N/(\eta|S|)]\), \(\eta=\eta(a,\varepsilon)\), carry all but \(\varepsilon N/|S|\) of the mass. The audit's form (fixed \(c\), remainder \(o(M)\)) needs one more step, not supplied here.
   - Prime \(N\): Konyagin–Shkredov Theorem 3 (arXiv:1403.8129) gives \(\|\mathbf 1_S\|_A\gg(\log(N/|S|))^{1/3}(\log\log(N/|S|))^{-1+o(1)}\to\infty\) for \(|S|\sim\sqrt{N/2}\). So for large prime \(N\) no such set has an exactly sharp spectrum, as (SS) predicts.
2. **The robust case is not covered by any source read.** Under sharpness, \(\mathbf 1_S\) is within relative \(L^2\) error \(o(1)\) of \(h=\mathbf 1_S\) projected onto \(\Lambda=\{g\ge a\}\), with \(\|h\|_A\le a^{-1/2}\) (Lemma 2). Equivalently: \(|\mathbf 1_S-h|<\varepsilon\) for every fixed \(\varepsilon\) outside an exceptional set of \(o_\varepsilon(|S|)\) points. The gap to the literature is exactly that exceptional set, at density \(\alpha=N^{-1/2}\):
   - Every approximate idempotent theorem read (Green–Sanders Lemma 3.1; Sanders, arXiv:1804.04050, Theorem 2.5; Cheung–Hatami–Zhao–Zilberstein, arXiv:2409.10634, Theorem 2) assumes an approximation in **sup norm**, i.e. an empty exceptional set. The (SS) hypothesis is invariant under adding \(o(|S|)\) arbitrary points (Lemma 1), so no sup-norm hypothesis can be verified from it without a cleaning step that no source supplies.
   - The one \(L^2\)-robust structure theorem found (Gopalan–O'Donnell–Servedio–Shpilka–Wimmer, SIAM J. Comput. 40 (2011), Theorem 3.4) is for \(\mathbb F_2^n\) only and needs \(L^2\) error \(\mu\le1/(20s^2)\) with \(s\ge(1-o(1))/\alpha\) the sparsity. Translated, that is relative error \(\lesssim\alpha^3/1600=N^{-3/2}/1600\), against the available \(o(1)\).
   - The density-dependent tools (Chang's lemma; Croot–Sisask; Croot–Łaba–Sisask; Sanders Proposition 7.1) all lose a factor \(\log(1/\alpha)\asymp\log N\) in a dimension or an exponent. At \(\alpha=N^{-1/2}\) this makes every guaranteed structure trivial (§3.2, with numbers in the script).
3. **(SS\*\*) does not help.** None of its extra hypotheses (flatness, \(\mathcal E(S)\le(\frac12+o(1))|S|^3\), the (A5) overlap dichotomy, (A6)) is a hypothesis of any source read. The energy lower bound \(\mathcal E(S)\ge(a-o(1))|S|^3\) gives, density-free, structure on a fraction \(c(a)\) of \(S\) (Balog–Szemerédi–Gowers with Sanders' Proposition 8.1). That fails the robustness parameter: it covers a fixed fraction, not \(1-o(1)\), and it gives Bohr systems or coset progressions, not subgroups (§4).
4. **`cand:gp-sector-constancy`.** Yes, a failure of (SS) through progression-shaped spectra would touch it. The dual of \(\mathbb Z/n\) is \(Q\), additive progressions in the dual are geometric progressions in \(Q\), and excluding sharp spectral mass on a geometric progression of length \(c_0\sqrt p\) by the sector condition is (GP-Sub\(_\kappa\)) for that \(c_0\). It is known only for \(c_0>1\) (Vinogradov; R191 GPSUB §3.1) (§5).

**Consequence.** Theorem E stays conditional on (SS\*). The record can add that the exact case of (SS\*) is source-backed (item 1); the robust sparse case is open as far as these sources go. The plan is unchanged: hold.

---

## 1. The statements to be matched

**(SS)** and **(SS\*)** are as in R192 §3 (lines 244–255), with the audit's quantifiers (AUD192 §2.9):

> For every \(a\in(0,\frac12]\) there are \(L\in\mathbb N\) and \(c\in(0,1]\) such that no sequence \(S_k\subseteq\mathbb Z/N_k\) with \(|S_k|\sim\sqrt{N_k/2}\) and \(\sum_{\xi\ne0,\,g_k<a}g_k=o(M_k)\) has
> \(\liminf_k\min_B\sum_{\xi\notin B}g_k/M_k>0\), the minimum over unions \(B\) of at most \(L\) subgroups of the dual of orders in \([cN_k/|S_k|,\,N_k/(c|S_k|)]\).

**(SS\*\*)** (AUD192 §2.9) is (SS\*) with the extra hypotheses: flatness; \((a-o(1))|S|^3\le\mathcal E(S)\le(\frac12+o(1))|S|^3\); the (A5) overlap dichotomy with \(|H_*|=o(m_0)\); (A6).

The parameters that a source must reach:
- **density** \(\alpha=|S|/N\sim(2N)^{-1/2}\to0\);
- **robustness**: the hypothesis is an \(L^2\) statement with relative error \(o(1)\), not an exact or sup-norm statement;
- **number of subgroups** \(L(a)\), bounded in terms of \(a\) only, and their **orders** in the window \([cN/|S|,N/(c|S|)]\).

### Lemma 1 (the (SS) hypothesis tolerates \(o(|S|)\) exceptional points; proved)

Let \(H\le\mathbb Z/N\) have order \(h\), let \(E\subseteq\mathbb Z/N\setminus H\) with \(|E|=r\le\frac{1-\sqrt a}2h\), and let \(S=H\cup E\). Then
\[
\sum_{\xi\ne0,\ g_S(\xi)<a}g_S(\xi)\ \le\ \frac{Nr}{|S|^2}\Big(1+\frac{16a}{(1-\sqrt a)^2}\Big),\qquad \sum_{\xi\notin H^\perp}g_S(\xi)\le\frac{Nr}{|S|^2}.
\]
Hence if \(r=o(|S|)\), \(S\) is sharp at level \(a\), and the single subgroup \(H^\perp\) (of order \(N/h\sim N/|S|\)) carries all but \(o(M)\): \(S\) satisfies the conclusion of (SS) with \(L=1\).

*Proof.* \(\widehat{\mathbf 1_S}=\widehat{\mathbf 1_H}+\widehat{\mathbf 1_E}\), with \(\widehat{\mathbf 1_H}=h\,\mathbf 1_{H^\perp}\), and Parseval gives \(\sum_\xi|\widehat{\mathbf 1_E}|^2=Nr\).
- Off \(H^\perp\), \(\widehat{\mathbf 1_S}=\widehat{\mathbf 1_E}\). So the mass there is at most \(Nr/|S|^2\) in units of \(g\).
- On \(H^\perp\), \(g_S(\xi)<a\) means \(|\widehat{\mathbf 1_S}(\xi)|<\sqrt a(h+r)\). Then \(|\widehat{\mathbf 1_E}(\xi)|>h-\sqrt a(h+r)\ge(1-\sqrt a)h-r\ge\frac{1-\sqrt a}2h\). By Chebyshev there are at most \(4Nr/((1-\sqrt a)^2h^2)\) such \(\xi\). Each has \(g_S<a\), and \(h\ge|S|/2\) because \(r\le h\).
- Adding the two parts gives the bound. Since \(M\sim N/|S|\), the low mass is \(O_a(r/|S|)\cdot M\). \(\square\)

**Reading.** Sharpness and the (SS) conclusion are both stable under adding or removing \(o(|S|)\) arbitrary points. A theorem whose hypothesis concerns \(\mathbf 1_S\) at *every* point therefore cannot be applied to the (SS) hypothesis directly. The script checks two instances (\(N=1800\), \(H\) of order 30, \(r=2,5\)): \(\text{low}/M=0.062,\ 0.141\), with \(\|\mathbf 1_S\|_A=2.23,\ 2.94\) against \(1.00\) for \(H\).

### Lemma 2 (reformulation as an approximate idempotent; proved)

Let \(S\) be sharp at level \(a\) along a sequence, \(\Lambda=\{\xi:g(\xi)\ge a\}\) (so \(0\in\Lambda\), \(\Lambda=-\Lambda\)), and
\[h(x)=N^{-1}\sum_{\xi\in\Lambda}\widehat{\mathbf 1_S}(\xi)\,e(x\xi/N).\]
Then:
1. \(h\) is real, and \(\|h\|_A\le a^{-1/2}\);
2. \(\mathbb E_x|\mathbf 1_S-h|^2=\alpha^2\sum_{\xi\notin\Lambda}g=o(\alpha)\);
3. for every fixed \(\varepsilon>0\), \(\#\{x:|\mathbf 1_S(x)-h(x)|\ge\varepsilon\}=o_\varepsilon(|S|)\);
4. \(|\Lambda|\le1/(a\alpha)\) and \(|\Lambda|\ge\sum_\Lambda g=(1-o(1))/\alpha\).

Conversely, \(h=\mathbf 1_S\) exactly if and only if \(g\in\{0\}\cup[a,1]\) everywhere (the *exact case*).

*Proof.*
1. \(\Lambda\) is symmetric and \(\widehat{\mathbf 1_S}(-\xi)=\overline{\widehat{\mathbf 1_S}(\xi)}\), so \(h\) is real. Also \(\|h\|_A=\alpha\sum_\Lambda g^{1/2}\le\alpha a^{-1/2}\sum_\Lambda g\le\alpha a^{-1/2}\cdot\alpha^{-1}\), since \(g^{1/2}\le g/\sqrt a\) on \(\Lambda\).
2. The normalised Fourier coefficients of \(\mathbf 1_S-h\) are \(N^{-1}\widehat{\mathbf 1_S}(\xi)\mathbf 1_{\xi\notin\Lambda}\). Parseval gives \(N^{-2}\sum_{\xi\notin\Lambda}|\widehat{\mathbf 1_S}|^2=\alpha^2\sum_{\xi\notin\Lambda}g\). The last sum is the low mass \(o(M)=o(1/\alpha)\).
3. Chebyshev: the count is at most \(N\varepsilon^{-2}\,o(\alpha)=o(|S|)\).
4. \(g\ge a\) on \(\Lambda\) and \(\sum g=1/\alpha\); and \(g\le1\).
- The converse: \(h=\mathbf 1_S\) if and only if \(\widehat{\mathbf 1_S}\) vanishes off \(\Lambda\). \(\square\)

So (SS\*) is a statement about **approximate idempotents with an exceptional set**: \(h\) has bounded algebra norm, Fourier support of size \(\asymp1/\alpha\), and agrees with the indicator \(\mathbf 1_S\) to any fixed accuracy outside \(o(|S|)\) points, where \(|S|=\alpha N\) and \(\alpha=N^{-1/2}\). The script checks items 1–3 on five examples.

---

## 2. Sources read at source

### 2.1 Exact quantitative idempotent theorems (composite \(N\))

- **Green–Sanders**, "A quantitative version of the idempotent theorem in harmonic analysis", Ann. of Math. 168 (2008); arXiv:math/0611286v2.
  - **Theorem 1.3 (p. 2):** \(G\) finite abelian, \(f:G\to\mathbb Z\) with \(\|f\|_A\le M\). Then \(f=\sum_{j=1}^L\pm\mathbf 1_{x_j+H_j}\) with \(L\le e^{e^{CM^4}}\), and the number of distinct \(H_j\) is at most \(M+\frac1{100}\).
  - Hypotheses: exactly integer-valued; algebra norm bounded. No density condition.
- **Sanders**, "Bounds in Cohen's idempotent theorem", J. Fourier Anal. Appl. 26 (2020), no. 2, paper 25; arXiv:1610.07092v5.
  - **Theorem 1.1 (p. 2):** \(f:G\to\mathbb Z\), \(\|f\|_A\le M\). Then \(f=\sum_{W}z(W)\mathbf 1_W\) over cosets \(W\), with \(\|z\|_{\ell^1}\le\exp(M^{4+o(1)})\).
  - **Proposition 1.2 (p. 2):** intervals in \(\mathbb Z/N\), \(N\) prime, show that \(\exp(\frac{\pi^2}4M)\) cosets can be needed.
  - §1.5 names the two bottlenecks: Proposition 7.1 (a Green–Konyagin continuity estimate) and Proposition 8.1 (a Freiman-type theorem).
- **Sanders**, "Boolean functions with small spectral norm, revisited", Math. Proc. Cambridge Philos. Soc. (2019); arXiv:1804.04050v3.
  - **Theorem 1.1 (p. 1):** \(\mathbb F_2^n\), integer-valued \(f\), \(\|f\|_A\le M\). Then \(f=\sum_{i\le L}\pm\mathbf 1_{V_i}\) with \(L\le\exp(M^{3+o(1)})\).

**Proposition 3 (exact case, composite \(N\); derived from Green–Sanders Theorem 1.3 and Sanders Theorem 1.1).** Suppose \(g(\xi)\in\{0\}\cup[a,1]\) for every \(\xi\in\mathbb Z/N\). Then:
1. \(\mathbf 1_S=\sum_{j\le L}\pm\mathbf 1_{x_j+H_j}\) with \(L\le\exp(a^{-2-o(1)})\). By Green–Sanders the subgroups can be taken from at most \(m\le a^{-1/2}+\frac1{100}\) distinct ones, with \(L\le e^{e^{Ca^{-2}}}\). The spectrum \(\{g\ne0\}\) is contained in \(\bigcup_jH_j^\perp\).
2. For every \(\eta\in(0,1]\), let \(B_\eta\) be the union of those \(H_j^\perp\) with \(\eta|S|\le|H_j|\le|S|/\eta\), i.e. of dual order in \([\eta N/|S|,N/(\eta|S|)]\). Then
\[\sum_{\xi\notin B_\eta}g(\xi)\ \le\ (m+L^2)\,\eta\,N/|S|.\]

*Proof.*
1. Lemma 2(1) with \(h=\mathbf 1_S\) gives \(\|\mathbf 1_S\|_A\le a^{-1/2}=:M\), and \(\mathbf 1_S\) is integer-valued. Apply Green–Sanders Theorem 1.3 (for \(m\) and the doubly exponential \(L\)) or Sanders Theorem 1.1 (for \(L\le\|z\|_{\ell^1}\le\exp(M^{4+o(1)})\)). Finally, \(\widehat{\mathbf 1_{x+H}}\) is supported on \(H^\perp\).
2. Split the indices into \(J_{\rm small}=\{j:|H_j|<\eta|S|\}\), \(J_{\rm large}=\{j:|H_j|>|S|/\eta\}\) and the rest, \(J_{\rm mid}\). Write \(F_\bullet=\sum_{j\in J_\bullet}\pm\mathbf 1_{x_j+H_j}\).
   - A point \(\xi\notin B_\eta\) that lies in some \(H_j^\perp\), \(j\in J_{\rm large}\): there are fewer than \(m\,\eta N/|S|\) such points (each such \(H_j^\perp\) has order \(N/|H_j|<\eta N/|S|\), and there are at most \(m\) distinct ones), and each has \(g\le1\).
   - Every other \(\xi\notin B_\eta\) has \(\widehat{F_{\rm mid}}(\xi)=\widehat{F_{\rm large}}(\xi)=0\), so \(\widehat{\mathbf 1_S}(\xi)=\widehat{F_{\rm small}}(\xi)\). By Parseval and the triangle inequality in \(\ell^2(\mathbb Z/N)\),
     \[\sum_\xi|\widehat{F_{\rm small}}|^2=N\|F_{\rm small}\|_{\ell^2}^2\le N\Big(\sum_{J_{\rm small}}|H_j|^{1/2}\Big)^2\le NL^2\eta|S|.\]
     Divide by \(|S|^2\).
   - Add the two parts. \(\square\)

**What this gives and what it does not.**
- Given \(\varepsilon>0\), take \(\eta=\varepsilon/(m+L^2)\). At most \(a^{-1/2}+\frac1{100}\) subgroups with orders in \([\eta N/|S|,N/(\eta|S|)]\) carry all but \(\varepsilon(M+1)\). This is the conclusion of (SS) in an \(\varepsilon\)-form with \(c=c(a,\varepsilon)\).
- The audit's form (fixed \(c=c(a)\), remainder \(o(M)\)) would also need that components with \(|H_j|\) of order \(\eta|S|\), or dual subgroups of order \(\le cN/|S|\), carry \(o(M)\) or are absent. I have not proved this; it is not stated in the sources.
- For Theorem E the difference matters only through how the (A4) constant \(c_0(k,c_1,c_2)\) behaves as \(c_1\to0\) (R151). I did not examine that.

### 2.2 The exact case for prime \(N\)

- **Konyagin–Shkredov**, "On Wiener norm of subsets of \(\mathbb Z_p\) of medium size", Fundam. Prikl. Mat. 19 (2014), no. 5, 75–87; J. Math. Sci. 218 (2016), 599–608; arXiv:1403.8129v1.
  - **Theorem 3 (p. 2):** \(p\) prime, \(A\subset\mathbb Z_p\), \(\exp((\log p/\log\log p)^{1/3})\le|A|\le p/3\). Then
    \[\|\chi_A\|_A\gg(\log(p/|A|))^{1/3}(\log\log(p/|A|))^{-1+o(1)}.\]
  - The normalisation (p. 1: \(\hat f(\gamma)=p^{-1}\sum_xf(x)e_p(x\gamma)\), \(\|f\|_A=\sum_\gamma|\hat f(\gamma)|\)) is the one used here.
  - **Theorem 2** (from their earlier paper, arXiv:1401.4429) covers \(2\le|A|\le\exp((\log p/\log\log p)^{1/3})\) with \(\gg\log|A|\).
- **Green–Konyagin**, "On the Littlewood problem modulo a prime", Canad. J. Math. 61 (2009); arXiv:math/0601565v2.
  - **Theorem 1.2:** \(S(p)\gg(\log p/\log\log p)^{1/3}\), but only for \(|A|=\lfloor p/2\rfloor\) (Question 1.1). This is the dense case.

**Corollary 4 (exact case, prime \(N\); derived from Konyagin–Shkredov Theorem 3).** Fix \(a\in(0,1]\). For all sufficiently large primes \(N\), no \(S\subseteq\mathbb Z/N\) with \(|S|\sim\sqrt{N/2}\) has \(g(\xi)\in\{0\}\cup[a,1]\) for every \(\xi\).

*Proof.*
- Such \(S\) would have \(\|\mathbf 1_S\|_A\le a^{-1/2}\) (Lemma 2(1) with \(h=\mathbf 1_S\)).
- \(|S|\sim\sqrt{N/2}\) lies in the range of Theorem 3 for large \(N\). The script prints the lower end of the range: 5.69, 7.59 and 10.99 at \(N=10^6,10^{12},10^{24}\), against \(|S|\approx7\cdot10^2,\ 7\cdot10^5,\ 7\cdot10^{11}\).
- Theorem 3 then gives \(\|\mathbf 1_S\|_A\gg(\frac12\log N)^{1/3-o(1)}\to\infty\). \(\square\)

**Limits.**
- Theorem E uses \(N=n=(p-1)/2\), which is prime only for safe primes. So Corollary 4 is the exact case of (SS\*) for those \(N\) only. Proposition 3 covers every \(N\).
- The Konyagin–Shkredov argument bounds an \(L^1\) norm of the Fourier transform from below, through McGehee–Pigno–Smith's inequality (their (5) and Lemmas 4–7, pp. 3–6). It needs \(\|\mathbf 1_S\|_A\) itself, i.e. the exact case. An \(L^2\)-small change of \(\mathbf 1_S\) (Lemma 1) changes \(\|\mathbf 1_S\|_A\) by an unbounded amount, so the method gives nothing robust.

### 2.3 Approximate (sup-norm) idempotent theorems

- **Green–Sanders**, arXiv:math/0611286, **Lemma 3.1 (Inductive Step, p. 4)**.
  - Hypotheses: \(f:G\to\mathbb R\), \(\|f\|_A\le M\), and \(d(f,\mathbb Z)\le e^{-C_1M^4}\), where \(d(f,\mathbb Z)<\varepsilon\) means \(f\) takes values in \(\mathbb Z+[-\varepsilon,\varepsilon]\) **at every point**.
  - The iteration proving Theorem 1.3 (pp. 4–5) starts from \(d(f,\mathbb Z)=0\) and keeps \(d\le\varepsilon=e^{-C_0M^4}\) throughout.
- **Sanders**, arXiv:1804.04050, **Theorem 2.5 (p. 4)**. \(\mathbb F_2^n\); \(f\) is \(\epsilon\)-almost integer-valued (sup norm), \(\|f\|_A\le M\), \(\epsilon\le\exp(-CM)\). Then \(f_{\mathbb Z}=\sum_{i\le L}\pm\mathbf 1_{V_i}\) with \(L\le\exp(M^{3+o(1)})\).
- **Cheung–Hatami–Zhao–Zilberstein**, "Boolean functions with small approximate spectral norm", Discrete Analysis 2024:6; arXiv:2409.10634v1.
  - Definition (p. 2): \(\|f\|_{A,\varepsilon}=\inf\{\|g\|_A:\|f-g\|_\infty\le\varepsilon\}\).
  - **Theorem 2 (p. 3):** for \(\mathbb F_2^n\), \(\varepsilon\in[0,\frac12)\), \(\|\mathbf 1_A\|_{A,\varepsilon}\le M\), and \(A\), \(A^c\) both \(k\)-affine connected, \(A\) has coset complexity \(\le\ell(k,M,\varepsilon)\), a tower-type bound (Remark 2).
  - The Hamming-ball example (p. 3) shows that a connectivity hypothesis is needed for constant \(\varepsilon\). Extending to all LCA groups is an open question (§4).
  - Their §1 credits Méla (1982) and Sanders [San19, Theorem 2.5] with the sup-norm version under \(M\le c\log\varepsilon^{-1}\).

**Gap (proved by Lemmas 1–2).** All three assume \(\|f-\text{integer}\|_\infty\) small at every point. Lemma 2 supplies smallness only outside \(o(|S|)\) points, and Lemma 1 shows the (SS) hypothesis cannot supply more. So the failing parameter is **robustness**: an empty exceptional set against \(o(|S|)\) exceptional points.

The natural way to remove the exceptional set is to smooth by convolution with a Bohr-set measure. That runs into the density, as §3.2 explains.

### 2.4 The one \(L^2\)-robust structure theorem found

- **Gopalan–O'Donnell–Servedio–Shpilka–Wimmer**, "Testing Fourier dimensionality and sparsity", SIAM J. Comput. 40 (2011); author copy `cs.columbia.edu/~rocco/Public/4-27-2011-gossw.pdf`.
  - **Definition 3.1:** \(f\) is \(\mu\)-close to \(s\)-sparse in \(\ell_2\) if the Fourier mass outside the \(s\) largest coefficients is \(\le\mu^2\).
  - **Theorem 3.3 (granularity):** under this hypothesis, each of the \(s\) largest coefficients is \(\mu\sqrt s\)-close to \(\lceil\log s\rceil\)-granular.
  - **Theorem 3.4 (p. 8):** \(f:\mathbb F_2^n\to\{-1,1\}\), \(\mu\)-close to \(s\)-sparse, \(\mu\le1/(20s^2)\). Then \(f\) is within Hamming distance \(\mu^2/2\) of an \(s\)-sparse Boolean function.

**Translation (derived in full).** Put \(f=1-2\cdot\mathbf 1_S\) on \(\mathbb F_2^n\), \(N=2^n\).
- For \(\xi\ne0\): \(\hat f(\xi)=-2N^{-1}\widehat{\mathbf 1_S}(\xi)\), so \(\hat f(\xi)^2=4\alpha^2g(\xi)\).
- The \(s\) largest coefficients are those in \(\Lambda\) when \(s=|\Lambda|\). Hence
  \[\mu^2=4\alpha^2\sum_{\xi\notin\Lambda}g=4\alpha^2\cdot o(M)=o(\alpha).\]
- By Lemma 2(4), \(s\ge(1-o(1))/\alpha\). So the hypothesis \(\mu\le1/(20s^2)\) requires \(\mu^2\le(1+o(1))\alpha^4/400\), i.e. low mass \(\le(1+o(1))\alpha^2/1600\). In relative terms, \(\text{low}/M\lesssim\alpha^3/1600\).
- At \(\alpha\asymp N^{-1/2}\) that is relative error \(N^{-3/2}\), against the available \(o(1)\). The script shows the two sides on examples, e.g. \(\mu^2=4.3\cdot10^{-3}\) against the required \(\le1.9\cdot10^{-10}\).

**Gap.** The group is wrong: the proof of Theorem 3.3 uses random permuted coset structures of \(\mathbb F_2^n\), with no \(\mathbb Z/N\) analogue in the paper. Robustness is short by a factor \(\asymp\alpha^3\). And the conclusion is \(s\)-sparsity with \(s\asymp1/\alpha\) unbounded, not a bounded number of cosets.

### 2.5 Spectral-structure theorems

- **Chang's lemma**, as stated and proved in Green, "Spectral structure of sets of integers" (survey; `people.maths.ox.ac.uk/greenbj/papers/spectral-structure-sets-of-integers.pdf`), **Theorem 1 (p. 1)**: for \(|A|=\alpha N\), \(R=\{r:|\hat A(r)|\ge\rho|A|\}\subseteq\mathrm{Span}(E)\) with \(|E|\ll\rho^{-2}\log(1/\alpha)\).
  - With \(\rho^2=a\) and \(\alpha=N^{-1/2}\): \(|E|\ll a^{-1}\cdot\frac12\log N\). This is unbounded, and no better than the trivial bound \(\log_2N\) once \(a\) is small.
  - Hosseini–Lovett (below, p. 2) make the same point for \(|A|=|G|^\alpha\): Chang's and Bloom's bounds "become trivial".
  - **Theorem 3** there (Chang is sharp; from Green, CPC 2003; not re-read at source) needs \(\rho^{-2}\log(1/\alpha)\le\log N/\log\log N\). That fails at \(\alpha=N^{-1/2}\), so Green's sharpness construction does not live in the (SS\*) regime either.
  - **Theorem 5** (Nazarov; dense sets, \([0,1]\)-valued functions) does not concern our regime.
- **Shkredov**, "On sets of large exponential sums, I", arXiv:math/0605689; and "Some examples of sets of large exponential sums", arXiv:math/0610554 (Mat. Sb. 198 (2007)).
  - **Theorem 1.3** of the second paper: for \(B\subseteq R_\alpha\setminus\{0\}\), \(T_k(B)\ge\delta\alpha^{2k}|B|^{2k}/(2^{4k}\delta^{2k})\), with \(\delta\) the density.
  - **Theorem 1.4**: Chang with \(\log^{13/7}\) refinements.
  - These are additive-energy lower bounds for the spectrum, with the density \(\delta\) as a factor. They contain no coset or idempotent conclusion and no robustness statement.
- **Hosseini–Lovett**, "On the structure of the spectrum of small sets", arXiv:1504.01059v1.
  - Regime \(|A|=|G|^\alpha\), \(\alpha<\frac12\); the (SS\*) size \(|S|\sim\sqrt{N/2}\) is at the boundary \(\alpha\uparrow\frac12\).
  - **Example 1.1 (p. 3):** \(A=(\mathbb Z_2^n\times0)\cup(0\times\mathbb Z_2^n)\), \(|A|=2|G|^{1/2}-1\), \(\mathrm{Spec}_{1/2}(A)=A\). This is the \(\mathbb F_2\) analogue of R192 Proposition D: a sharp set that is a union of two subgroups, consistent with (SS).
  - **Theorems 1.2–1.3 (pp. 3–4):** a subset \(A'\subseteq A\) with \(|A'|\ge|A|/C\), \(C\le\exp((1/\varepsilon)^{O(1/\delta)})\) (Thm 1.2), whose spectrum has \(|\mathrm{Spec}_\varepsilon(A')+\mathrm{Spec}_\varepsilon(A')|\le C|G|^{1-\alpha+\delta}\). Conjecture 1.4 (bounded doubling of the spectrum of a large subset) is open.
  - **Gap:** robustness (only a fraction \(1/C\) of \(A\)), losses of \(|G|^\delta\), and no conclusion about sharpness or subgroups.
- **Carenini–Franchi**, "A strengthening of Chang's lemma", arXiv:2605.07916 (abstract and §1 read). Same \(2\varepsilon^{-2}\log(1/\alpha)\) dimension, with a cosetwise \(\ell^1\) refinement. Same density loss.

### 2.6 Almost-periodicity with explicit density dependence

- **Croot–Sisask**, "A probabilistic technique for finding almost-periods of convolutions", GAFA 20 (2010) 1367–1396; arXiv:1003.2978.
  - **Corollary 1.2 (p. 3):** \(B\) of density \(\beta\). There is \(T\) with \(|T|\ge(\beta/2)^{9/\epsilon^2}|G|\) such that \(\|\mathbf 1_A*\mathbf 1_B(x+t)-\mathbf 1_A*\mathbf 1_B(x)\|_2^2\le\epsilon^2|A||B|^2\) for \(t\in T-T\).
  - At \(\beta=N^{-1/2}\), \(\log|T|\ge\log N-\frac9{\epsilon^2}(\frac12\log N+\log2)<0\) for every \(\epsilon<1\). The guarantee is empty (script: \(\log|T|\ge-70.6\) at \(N=10^6\), \(\epsilon=0.9\)).
  - **Proposition 1.1** (local version) replaces \(\beta\) by \(1/K\), where \(|B\cdot S'|\le K|B|\) for some auxiliary set \(S'\) and \(T\subseteq S'\). Applied with \(B=S\), it needs a set \(S'\) of size \(\gg|S|\) with \(|S+S'|\le K|S|\), \(K\) bounded. That is a bounded-doubling container for all of \(S\), which the (SS) hypothesis does not supply. Energy gives one only for a subset of \(S\) (§4).
- **Croot–Łaba–Sisask**, "Arithmetic progressions in sumsets and \(L^p\)-almost-periodicity", CPC (2013); arXiv:1103.6000v2.
  - **Theorem 1.2 (p. 2):** for any \(f\) there is a Bohr set of rank \(\le Cp/\epsilon^2\) and radius \(c\epsilon\) of \(L^p\)-almost-periods with error \(\epsilon\|\hat f\|_{\ell^1}\).
- **Sanders**, arXiv:1610.07092, **Proposition 7.1 (p. 22):** a Bohr system \(B'\le B\) with \(\dim B'\le d+O(p\delta^{-2}\log^22\delta^{-1})\) and measures \(\mu,\nu\) with \(\sup_x\|f-f*\mu\|_{L^p(\tau_x(\nu))}\le\delta\|f\|_A\). This is the density-free continuity estimate in the idempotent proofs.

How these fail at \(\alpha=N^{-1/2}\) is quantified in §3.2.

### 2.7 Not retrieved

- J.-F. Méla, "Mesures \(\varepsilon\)-idempotentes de norme bornée", Studia Math. 72 (1982); and Host–Méla–Parreau, *Analyse harmonique des mesures*, Astérisque 135–136 (1986). Only CHZZ's description was read (p. 2): a sup-norm \(\varepsilon\)-approximation with \(M\le c\log\varepsilon^{-1}\), for LCA groups. As described, they are sup-norm statements and fall under §2.3. Not read at source.
- Green, "Some constructions in the inverse spectral theory of cyclic groups" (CPC 2003): only through the survey's Theorem 3 (§2.5).
- Bloom's large-subset Chang bound: only through Hosseini–Lovett p. 2.
- Searches for a robust, \(L^2\), sparse or relative-density idempotent theorem in \(\mathbb Z/N\) (queries in the hand-over note) found nothing beyond the above.

---

## 3. The gap, parameter by parameter

### 3.1 Table

| source (theorem) | group | hypothesis type | density | conclusion | fails at |
|---|---|---|---|---|---|
| Green–Sanders Thm 1.3 | any finite abelian | \(f\) integer-valued, \(\|f\|_A\le M\) | free | \(\le e^{e^{CM^4}}\) cosets, \(\le M+\frac1{100}\) subgroups | robustness: exact only (gives the exact case, Prop. 3) |
| Sanders 2020 Thm 1.1 | any finite abelian | same | free | \(\|z\|_1\le e^{M^{4+o(1)}}\) | robustness: exact only |
| Konyagin–Shkredov Thm 3 | \(\mathbb Z_p\) | \(\exp((\log p/\log\log p)^{1/3})\le|A|\le p/3\) | covers \(N^{-1/2}\) | \(\|\chi_A\|_A\to\infty\) | robustness: exact only (gives Cor. 4); \(L^1\) method |
| GS Lemma 3.1; Sanders 2019 Thm 2.5; CHZZ Thm 2 | any / \(\mathbb F_2^n\) / \(\mathbb F_2^n\) | sup-norm almost integer-valued | free | coset structure | robustness: needs empty exceptional set; (SS) gives \(o(|S|)\) points (Lemmas 1–2) |
| GOSSW Thm 3.4 | \(\mathbb F_2^n\) | \(L^2\): \(\mu\le1/(20s^2)\) | implicit through \(s\asymp1/\alpha\) | \(s\)-sparse Boolean | group; robustness short by \(\asymp\alpha^3\); \(s\) unbounded |
| Chang (Green survey Thm 1); Carenini–Franchi | any | none beyond density | loss \(\log(1/\alpha)\) | span of \(\ll a^{-1}\log(1/\alpha)\) elements | number of generators \(\asymp\log N\) |
| Shkredov Thms 1.3–1.4 | \(\mathbb Z_N\) | none | factor \(\delta\) | energy of spectrum | no coset conclusion |
| Hosseini–Lovett Thms 1.2–1.3 | any | \(|A|\ge|G|^\alpha\) | covers \(\alpha\uparrow\frac12\) | subset \(|A|/C\) with structured spectrum | robustness (fraction \(1/C\)); \(|G|^\delta\) losses |
| Croot–Sisask Cor. 1.2; CŁS Thm 1.2; Sanders Prop. 7.1 | any | none / \(\|f\|_A\) | base \(\beta\), or \(p\gtrsim\log(1/\alpha)\) | almost periods / continuity | density: guaranteed structure trivial at \(\alpha=N^{-1/2}\) |

No row reaches all three parameters at once (density \(N^{-1/2}\), \(L^2\) relative robustness, bounded number of subgroups in the order window). The two exact rows reach density and the number of subgroups, and fail only robustness.

### 3.2 Why the continuity tools lose the density (derivation; agent analysis)

The idempotent proofs smooth \(h\) (Lemma 2) by a Bohr-set measure, using \(\|h-h*\mu\|_{L^p(\tau_x\nu)}\le\delta\|h\|_A\) (Sanders Prop. 7.1; CŁS Thm 1.2 with \(\epsilon=\delta\)). For this to say anything about \(S\), the right side must be smaller than what the indicator contributes on a typical translate:
- Since \(h\approx\mathbf 1_S\) and \(h*\mu\) is an average over a set much larger than \(S\), on a translate \(\tau_x\nu\) one has \(\|h-h*\mu\|_{L^p(\tau_x\nu)}\approx\nu(S-x)^{1/p}\).
- Averaged over \(x\), \(\nu(S-x)=\alpha\).
- So the estimate is informative only if \(\delta<\alpha^{1/p}\), i.e. \(p\gtrsim\log(1/\alpha)/\log(1/\delta)\).
- Then \(\dim B'\gtrsim p\delta^{-2}\gtrsim\log(1/\alpha)=\frac12\log N\), up to factors depending on \(\delta\). A Bohr set of dimension \(d\) and radius \(\kappa\) is guaranteed only \(\kappa^{O(d)}N\) points; at \(d\asymp\log N\) this is \(N^{1-O(\log(1/\kappa))}\), below \(|S|=N^{1/2}\) once \(\log(1/\kappa)\) exceeds an absolute constant.

The same \(\log(1/\alpha)\) appears as the exponent in Croot–Sisask (\(\beta^{9/\epsilon^2}\)) and in Chang's dimension.

At bounded density this loss is a constant and harmless. At \(\alpha=N^{-1/2}\) it is \(\asymp\log N\), which is the whole group's dimension. This is the precise sense of R192's remark (line 263) that "the almost-periodicity arguments … lose a factor depending on the density".

This paragraph explains why the read sources fail. It does not prove that no method works.

---

## 4. (SS\*\*): do the extra hypotheses bring a source into reach?

- **Flatness** and **(A6)** (no single coset of order \(\le(2-\delta)m_0\) carries nearly all of \(S\)) are not hypotheses of any source read. (A6) excludes the single-coset case, which Lemma 1 shows is the easiest sharp example. It does not exclude two-coset unions (R192 Prop. D; Hosseini–Lovett Ex. 1.1).
- **(A5)** (the overlap dichotomy \((1-q_a)(2q_a-1)\le o(1)\), \(|H_*|=o(m_0)\)) is a statement about \(r_S(a)=|S\cap(S+a)|/|S|\). No source has such a hypothesis.
- **Energy.** Sharpness gives \(\mathcal E(S)/|S|^3=\sum_\xi g^2\cdot\alpha\ge a\alpha\sum_\Lambda g\ge a-o(1)\). This is the only hypothesis of (SS\*\*) that feeds a published tool density-free:
  - Balog–Szemerédi–Gowers (as used in CHZZ Lemma 5; there [TV10, Thm 2.31], not re-read) gives \(S'\subseteq S\) with \(|S'|\ge a^{O(1)}|S|\) and \(|S'+S'|\le a^{-O(1)}|S'|\).
  - Sanders 2020 Prop. 8.1 (p. 27) then gives a Bohr system \(B\) with \(C_\Delta(S';B')=\exp(O(\log^3(2K)\cdots))\) and \(\dim B=O(\log^32K\cdots)\), \(K=a^{-O(1)}\). For \(\mathbb F_2^n\), CHZZ Lemma 5 gives a coset \(V+a\) with \(|V+a|\ge2^{-O(\log^{3+o(1)}\varepsilon^{-1})}|A|\) and density \(2^{-O(\log^{1+o(1)}\varepsilon^{-1})}\) of \(A\) in it.
  - **Gap:** robustness. This structures a fraction \(a^{O(1)}\) of \(S\), not all but \(o(|S|)\). In \(\mathbb Z/N\) it yields Bohr systems or coset progressions, not subgroups. For prime \(N\) there are no subgroups at all, so the structure is progression-like, and that is exactly the case (SS\*) must exclude.
  - The energy upper bound \(\le\frac12+o(1)\) has no counterpart in any source.

So (SS\*\*) is not covered either. Its extra hypotheses are tailored to (NC) and appear in no source.

---

## 5. Progression-shaped spectra and `cand:gp-sector-constancy`

- The near-critical support lives in \(\mathbb Z/n\), \(n=(p-1)/2\). Its dual is identified with \(Q\) through \(x\mapsto(j\mapsto\psi^j(x))\) (R192 §1).
- So subgroups of the dual are subgroups of \(Q\). Additive progressions \(\{k\xi_0:|k|\le K\}\) in the dual are geometric progressions \(\{\zeta^k:|k|\le K\}\subseteq Q\), and rank-one Bohr sets in the dual are multiplicative Bohr sets.
- Suppose (SS) failed because some sharp sets carry their spectral mass on progression-shaped sets rather than on subgroups. (No such set is known. Intervals have Fejér tails and are not sharp: script, \(\text{low}/M=0.159\) at \(a=\frac14\), \(N=1800\). Corollary 4 excludes exactly sharp sets for prime \(N\), but says nothing robust.)
- Then Theorem E's use of (A4), which concerns cosets of subgroups only (R151), would no longer apply, and the near-critical support would be a candidate counterexample of that shape.
- To exclude it on (NC) through the sector forms:
  - R190 Theorem 1(4) puts every level \(\ge\tau\) in \(T_\rho\cup\{1\}\).
  - So a geometric progression of length \(\asymp c_0\sqrt p\) carrying levels \(\ge a\) would need \(\chi(1-\zeta^k)=\rho\) for all but a small fraction of \(k\).
  - Excluding this is (GP-Sub\(_\kappa\)) at that \(c_0\), in the "for every \(c_0>0\)" form of AUD191 (g7).
  - Published results give it only for \(c_0>1\): the Vinogradov consequence \(E_\rho\ge(M-\sqrt p)/2\) (R191 GPSUB §3.1, re-derived in AUD191 (g4)). Shorter progressions need the open part of `cand:gp-sector-constancy`.
- The subgroup analogue is unconditional for orders \(\ge(1+\delta)\sqrt p\) (R192 Corollary J).
- **Answer: yes.** A failure of (SS) through progression-shaped spectra would touch `cand:gp-sector-constancy` (as (GP-Sub\(_\kappa\)), lengths below \(\sqrt p\)). A sector-free alternative would need a progression analogue of (A4) (R151 coset mass for geometric progressions), which is not among the accepted statements. A failure through subgroup-shaped spectra cannot occur, since that is (SS)'s conclusion.
- None of the sources read decides whether progression-shaped sharp spectra exist in the robust sense.

---

## 6. For the coordinator

- **Before:** (SS\*) unproved, "no source known", exact case attributed to Green–Sanders "quoted from memory" (R192 §3, AUD192 §2.9).
- **After:**
  - (i) The exact case of (SS\*) is source-backed, read at source:
    - composite \(N\): Green–Sanders Thm 1.3 / Sanders Thm 1.1 via Proposition 3, in an \(\varepsilon\)-form of the order window;
    - prime \(N\): Konyagin–Shkredov Thm 3 via Corollary 4, no exactly sharp set exists.

    Also, \(\|\mathbf 1_S\|_A\le a^{-1/2}\), sharper than R192's \(1/a\).
  - (ii) No source covers the robust sparse case. The precise gap: every approximate idempotent theorem needs a sup-norm approximation (empty exceptional set), while (SS) supplies agreement outside \(o(|S|)\) points (Lemmas 1–2). The only \(L^2\)-robust theorem (GOSSW 3.4, \(\mathbb F_2^n\)) needs relative error \(\lesssim\alpha^3\). The density-dependent tools lose \(\log(1/\alpha)\asymp\log N\).
  - (iii) (SS\*\*)'s extra hypotheses match no source.
  - (iv) Progression-shaped failures of (SS) would route through `cand:gp-sector-constancy`.
- **Unchanged:** Theorem E conditional; (A-vertex) and (A-slope) as recorded; plan on hold. Per AUD192 §4.4, the decision after this call is hold in every case.
- **Wording for the record (suggested):** "(SS\*): open (literature check R193). Exact case known (GS08 Thm 1.3 / San20 Thm 1.1 for composite \(N\), \(\varepsilon\)-form of the order window; KS14 Thm 3 for prime \(N\)). The robust sparse case (relative \(L^2\) error \(o(1)\), equivalently \(o(|S|)\) exceptional points, at density \(N^{-1/2}\)) is not covered by any source read."
- **Open quantifier point (not settled here):** whether the exact case gives the audit's fixed-\(c\) form, or whether Theorem E can use the \(\varepsilon\)-form, which depends on the \(c_1\)-dependence of (A4)'s \(c_0\).

---

## Verdict

**Refuted** (mission sense: no published theorem found that implies (SS\*) or (SS\*\*); (SS\*) stays an internal open problem; Theorem E stays conditional).

- **Strongest published statements, read at source:**
  - Exact case:
    - Green–Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, Ann. of Math. 168 (2008), arXiv:math/0611286, Theorem 1.3 and Lemma 3.1;
    - Sanders, *Bounds in Cohen's idempotent theorem*, J. Fourier Anal. Appl. 26 (2020) paper 25, arXiv:1610.07092, Theorem 1.1 (and Propositions 7.1, 8.1);
    - Konyagin–Shkredov, *On Wiener norm of subsets of \(\mathbb Z_p\) of medium size*, J. Math. Sci. 218 (2016), arXiv:1403.8129, Theorem 3.
  - Sup-norm approximate:
    - Sanders, *Boolean functions with small spectral norm, revisited*, Math. Proc. Cambridge Philos. Soc. (2019), arXiv:1804.04050, Theorem 2.5;
    - Cheung–Hatami–Zhao–Zilberstein, *Boolean functions with small approximate spectral norm*, Discrete Analysis 2024:6, arXiv:2409.10634, Theorem 2.
  - \(L^2\)-robust (\(\mathbb F_2^n\)): Gopalan–O'Donnell–Servedio–Shpilka–Wimmer, *Testing Fourier dimensionality and sparsity*, SIAM J. Comput. 40 (2011), Theorems 3.3–3.4.
  - Spectral structure and almost periodicity:
    - Chang's lemma as in Green, *Spectral structure of sets of integers*, Theorem 1;
    - Shkredov, arXiv:math/0605689 and arXiv:math/0610554 (Theorems 1.3–1.4);
    - Hosseini–Lovett, *On the structure of the spectrum of small sets*, arXiv:1504.01059, Theorems 1.2–1.3, Example 1.1;
    - Croot–Sisask, GAFA 20 (2010), arXiv:1003.2978, Corollary 1.2;
    - Croot–Łaba–Sisask, arXiv:1103.6000, Theorem 1.2;
    - Carenini–Franchi, arXiv:2605.07916;
    - Green–Konyagin, Canad. J. Math. 61 (2009), arXiv:math/0601565, Theorem 1.2 (dense only).
- **Failing parameter:**
  - **Robustness**, for every exact or sup-norm theorem: an empty exceptional set against \(o(|S|)\) exceptional points.
  - **Density**, for every \(L^2\) or almost-periodicity tool: a loss of \(\log(1/\alpha)\asymp\log N\), or relative error \(\alpha^3\) in GOSSW.
  - The **number of subgroups** is bounded only in the exact theorems, by \(a^{-1/2}+\frac1{100}\) (Green–Sanders).
- **Not retrieved:** Méla (Studia Math. 72, 1982); Host–Méla–Parreau (Astérisque 135–136, 1986). Both are sup-norm statements according to CHZZ's description.
- **`cand:gp-sector-constancy`:** touched only if (SS) fails through progression-shaped spectra (§5).

## Replay

```sh
python3 -B research/paley-193-ssstar-checks.py
```

Pure Python (no numpy), about 0.1 s. It prints a table and `ALL OK`.

## Files and hashes

| file | SHA-256 | output |
|---|---|---|
| `research/paley-193-ssstar-checks.py` | `ac4d042abed532f530aa30fb94e2c07c50d4c8fe244c8ab9060a1882314facc3` | `ALL OK`; stdout SHA-256 `e1c399fed427d518d7cf7b3b70ad77a9bd2ca1cf2ef575abc4673a024487ac2d` |

Script output (floating point; evidence only):

| example | \(N\) | \(|S|\) | \(a\) | low/\(M\) | \(\|\mathbf 1_S\|_A\) | \(\|h\|_A\) (\(\le a^{-1/2}\)) | exceptional count (\(\le16N\,\mathbb E|\mathbf 1_S-h|^2\)) | GOSSW \(\mu^2\) / required |
|---|---|---|---|---|---|---|---|---|
| subgroup of order 30 | 1800 | 30 | 1/4 | 0.000 | 1.000 | 1.000 (2) | 0 (0.00) | \(\approx0\) / \(1.9\cdot10^{-10}\) |
| subgroup + 2 points | 1800 | 32 | 1/4 | 0.062 | 2.231 | 1.000 (2) | 2 (30.9) | \(4.3\cdot10^{-3}\) / \(1.9\cdot10^{-10}\) |
| subgroup + 5 points | 1800 | 35 | 1/4 | 0.141 | 2.942 | 1.001 (2) | 5 (77.3) | \(1.1\cdot10^{-2}\) / \(1.9\cdot10^{-10}\) |
| \(1+H_{15}\cup2+H_{16}\) | 1920 | 31 | 1/16 | 0.000 | 1.953 | 1.952 (4) | 0 (0.01) | \(1.1\cdot10^{-6}\) / \(7.7\cdot10^{-13}\) |
| interval \(\{0,\dots,29\}\) | 1800 | 30 | 1/4 | 0.159 | 2.368 | 0.995 (2) | 22 (75.0) | \(1.0\cdot10^{-2}\) / \(8.8\cdot10^{-11}\) |

Parameter lines (floating point):
- Croot–Sisask \(\log|T|\) lower bound at \(\beta=N^{-1/2}\): \(-70.6\) to \(-964.4\) for \(N=10^6\)–\(10^{24}\), \(\epsilon\in\{0.5,0.9\}\). Always negative, i.e. empty.
- Chang bound \(/\log N\) at \(a=\frac14\) (constant 1): \(2.00\).
- Konyagin–Shkredov range contains \(|S|=\sqrt{N/2}\) at all three \(N\).
