# Round 180 candidate: mixed row autocorrelation and the slope-product sum

Author: independent agent run (Claude). This is an agent draft. It is not human acceptance or mathematical certification. No repository file was modified.

Mission: `coordination/missions/round-180/ordinary-prime-mixed-row-slope-product.md` (coordinator record `coordination/round-179.json`).

## Result summary

Counting normalization is used throughout. \(G=\sum g=O(\sqrt p)\) and \(0\le g\le 1\). \(M_1=\sum_r m(r)\le G^2\). "(a)" means proved for all sufficiently large primes \(p\equiv1\pmod 4\). Inherited steps are named where they are used.

1. **Mixed row autocorrelation lemma (a).** Put
\[
C(\lambda)=\sum_r m(r)\,m(\lambda r).
\]
For every \(\lambda\in\mathbb F_p^\times\setminus\{1\}\), uniformly in \(\lambda\),
\[
C(\lambda)\ \ll\ G^{11/4}+G^2+p^{-1/8}G^3=O(p^{11/8}).
\]
The proof uses only \(0\le g\le1\), \(\sum g=G\), the chart and its interior exclusions. The square mask \(b\in Q\) is dropped as a positive upper. The one external input is Stevens–de Zeeuw, Theorem 4, which rests on Rudnev's point-plane theorem.

2. **Multiplicative energy of the row mass (a).**
\[
E^\times(m)=\sum_\xi W_\xi^2=\sum_\lambda C(\lambda)^2=O(p^{27/8}).
\]
The old bound was \(\|m\|_1^2\|m\|_2^2=O(p^{7/2-3/418})\).

3. **Slope-product sum (a).**
\[
\sum_\xi W_\xi^{3/2}\le M_1\,E^\times(m)^{1/2}=O(p^{43/16}).
\]
Round 178 had \(O(p^{11/4-3/836})\). The gain is \(p^{-197/3344}\), since \(11/4-3/836-43/16=197/3344\).

4. **Effect on the right energy and downstream bounds.** These are (a), reusing the accepted Round 178 deductions verbatim with only the sum over \(\xi\) changed.
   - Whole right energy: \(\mathcal E(\mu)=O(p^{43/16})\). The old bound was \(O(p^{11/4-3/836})\). This now matches the accepted bound \(\mathcal E(\mu_*)=O(p^{43/16})\) for the inverted chart.
   - Weighted affine incidence: the second norm of \(H_\alpha\) over \(s\) is \(O(p^{147/128})\), uniformly in \(t\). The old bound was \(O(p^{37/32-3/6688})\).
   - Weighted twisted sum: \(\sum_{s\ne0,1,t}w(t)|H_\alpha(s,t)|^2=O(p^{179/64})\). The old bound was \(O(p^{45/16-3/3344})\).
   - One-match covariance, in the normalization of Round 173: \(O(p^{115/64})\). The old bound was \(O(p^{29/16-3/3344})\), so the gain is \(p^{-197/13376}\). The target is \(O(p^{3/2})=O(p^{96/64})\).
5. **Limit of the route, as a statement about the method.**
   - Inside this route, the one-match output is \(p^{9/8}\mathcal E(\mu)^{1/4}\). This uses Round 178's caps \(G\le p^{1/2}\) and \(M_1\le p\).
   - Every per-\(\xi\) point-plane bound for \(\mathcal E(\mu)\) carries \(\sum_\xi W_\xi^{3/2}\ge M_1^3/\sqrt{p-1}\). This floor is \(p^{5/2}\) when \(M_1\asymp p\), and then the output is at least \(p^{7/4}\).
   - Every bound on \(\mathcal E(\mu)\) satisfies \(\mathcal E(\mu)\ge M_1^4/(p(p-1))\). If \(M_1\gg p^{7/8+\varepsilon}\), the target \(O(p^{3/2})\) is therefore out of reach of the Rudnev–Shkredov second-norm route with any energy, and the output cannot go below \(p^{13/8}\) when \(M_1\asymp p\).
   - This is a conditional observation about the method, not a lower bound for \(H_\alpha\).

6. **By-product (a), given the accepted Round 176 generic maximum.** At every fixed slope \(a\notin\{0,1\}\), the first mass over \(c\) of the full right correlation is
\[
\sum_c\Delta(a,c)=C(a)=O(p^{11/8}).
\]
The old bound was \(O(p^{3/2-3/418})\). The fixed-\(a\) generic squared mass is then \(O(p^{19/8-1/1280-1/840})\).

## Setup recalled

**Chart (Round 171).** Take \(Y,D\in\mathbb F_p\setminus\{0,1\}\) with \(Y\ne D\). Then
\[
r=\frac{Y-D}{1-D},\qquad b=\frac{D(1-Y)}{Y(1-D)} .
\]
The weight is \(\mu(r,b)=g(Y)g(D)\) with the square mask \(b\in Q\) and the interior exclusions. The map \((Y,D)\mapsto(r,b)\) is injective.

**Row masses and slope products.** \(m(r)=\sum_b\mu(r,b)\), \(W_\xi=\sum_r m(r)m(\xi/r)\), \(\sum_\xi W_\xi=M_1^2\).

**Round 178 point-plane step.** For each \(\xi\), the weighted point-plane incidence in the PRRW chart is \(O(W_\xi^2/p+W_\xi^{3/2}+G(1+\log p)W_\xi)\). This is applied to the reduced weight \(\mu\,1_{\mu\ge p^{-2}}\le\mu\). Then \(\mathcal E(\mu)\) is bounded by the sum over \(\xi\) plus \(O(p)\).

**Monotonicity.** \(m\), \(W_\xi\), \(C(\lambda)\), \(E^\times(m)\) and \(\sum W^{3/2}\) are all nondecreasing in the nonnegative weight. Every upper below therefore holds for the actual masked weight and for Round 178's reduced weight.

**Completion used.** Define
\[
m^\sharp(r)=\sum_{\substack{Y,D\notin\{0,1\},\ Y\ne D\\ (Y-D)/(1-D)=r}} g(Y)g(D)\ \ge\ m(r).
\]
This drops only the mask \(b\in Q\). At fixed \(r\), \(D\) determines \(Y=r+(1-r)D\), so \(m^\sharp(r)\le G\).

**Two identities.**
\[
\sum_\lambda C(\lambda)^2=\#_w\{r_1r_2=r_3r_4\}=\sum_\xi W_\xi^2=E^\times(m),
\]
and \(\sum_\lambda C(\lambda)=M_1^2\). Also \(C(1)=\sum m^2\) and \(C(\lambda)=C(1/\lambda)\).

**Why the earlier approach could not gain.** At \(\lambda=1\), or for \(W_\xi\) at any \(\xi\), fixing one pair \((Y,D)\) fixes the partner's \(r\). The partner \((Y',D')\) then lies on a line through \((1,1)\), so the family is a pencil and incidence bounds give nothing. For \(W_\xi\), the other split \((Y_1,Y_2)\) against \((D_1,D_2)\) gives hyperbolas \((Y_1-D_1)(Y_2-D_2)=\xi(1-D_1)(1-D_2)\), not lines. For the autocorrelation at \(\lambda\ne1\), the split \((Y_1,Y_3)\) against \((D_1,D_3)\) gives a genuine two-parameter family of lines. This is the mixed structure exploited below: multiplicative in \(r\), and dilation about 1 in \(1-r\).

## Argument

### Step 1: unfolding \(C(\lambda)\)

By the symmetry \(C(\lambda)=C(1/\lambda)\), write the relation as \(r_1=\lambda r_3\). Then
\[
C^\sharp(\lambda)=\sum_{(Y_1,D_1,Y_3,D_3)\in\Omega_\lambda} g(Y_1)g(D_1)g(Y_3)g(D_3),
\]
where \(\Omega_\lambda\) is the set of tuples satisfying
\[
(Y_1-D_1)(1-D_3)=\lambda\,(Y_3-D_3)(1-D_1)\qquad (\ast)
\]
with all four variables in \(\mathbb F_p\setminus\{0,1\}\) and \(Y_i\ne D_i\).

### Step 2: a genuine line family

Fix \(\lambda\notin\{0,1\}\). For \(D_1,D_3\notin\{0,1\}\), let \(\ell_{D_1,D_3}\) be the set of points \((X,Z)=(Y_1,Y_3)\) with
\[
(1-D_3)(X-D_1)=\lambda(1-D_1)(Z-D_3).
\]
This is a line of slope \((1-D_3)/(\lambda(1-D_1))\). The slope is neither \(0\) nor \(\infty\), so the line is neither horizontal nor vertical.

The map \((D_1,D_3)\mapsto\ell_{D_1,D_3}\) is injective:
- The line passes through \((D_1,D_3)\).
- It meets \(Z=1\) at \(X_0=\lambda+(1-\lambda)D_1\), which determines \(D_1\) because \(\lambda\ne1\).
- Then \(D_3=\ell(D_1)\).

Hence \(C^\sharp(\lambda)\) is a weighted incidence count between the points \((Y_1,Y_3)\) and the distinct lines \(\ell_{D_1,D_3}\).

**Each variable is determined by the other three on \(\Omega_\lambda\).**
- \(Y_1\): its coefficient is \(1-D_3\ne0\).
- \(Y_3\): its coefficient is \(\lambda(1-D_1)\ne0\).
- \(D_1\): its coefficient is \(-(1-D_3)+\lambda(Y_3-D_3)\). If this vanishes, \((\ast)\) reduces to \(Y_1(1-D_3)=1-D_3\), forcing \(Y_1=1\), which is excluded.
- \(D_3\): its coefficient is \(-(Y_1-D_1)+\lambda(1-D_1)\). If this vanishes, the constant term is \((Y_1-D_1)(1-Y_3)\ne0\).

The exact checker verifies these claims for every \(\lambda\) at \(p=13,17,29\).

### Step 3: Stevens–de Zeeuw incidence bound

The input is Stevens–de Zeeuw, "An improved point-line incidence bound over arbitrary fields", Theorem 4 (arXiv:1609.06284; statement read from the PDF). Let \(A,B\subset\mathbb F\) with \(|A|=a\le b=|B|\) and \(ab^2\le n^3\), and let \(L\) be a set of \(n\) lines. In positive characteristic \(p\), assume \(an\ll p^2\). Then
\[
I(A\times B,L)\ll a^{3/4}b^{1/2}n^{3/4}+n .
\]
The proof goes through Rudnev's point-plane bound, their Theorem 6.

Two complements extend it to all the cases needed here:
- **Case \(ab^2>n^3\).** Our lines are nonvertical, so \(I\le an\). Moreover \(n<a^{1/3}b^{2/3}\) gives \(an<a^{3/4}n^{3/4}\,a^{1/3}b^{1/6}\le a^{3/4}b^{1/2}n^{3/4}\). The same bound therefore holds.
- **Case \(|U_1|>|U_3|\).** Swap the coordinates. The lines are also nonhorizontal, so they stay nonvertical after the swap.

With \(\min^{3/4}\max^{1/2}\le(ab)^{5/8}\), we get for all level sets \(U_1,U_3\) (point coordinates) and \(V_1,V_3\) (line parameters), provided \(\max(|U_i|)\cdot|V_1||V_3|\le c_0p^2\):
\[
I\le C_0\Big((|U_1||U_3|)^{5/8}(|V_1||V_3|)^{3/4}+|V_1||V_3|\Big).
\]
Dropping \(Y_i\ne D_i\) in the incidence count only adds nonnegative terms.

### Step 4: heavy and light parts

Take \(\tau=p^{-1/8}\) and split \(g=g1_{g>\tau}+g1_{g\le\tau}\) in each of the four roles.

**Heavy part.** Use the layer cake \(g1_{g>\tau}=\int_0^1 1[g>\max(t,\tau)]\,dt\). The level sets satisfy:
- \(|U(t)|\le G/\tau=O(p^{5/8})\);
- \(\int_0^1|U(t)|\,dt\le G\);
- by Jensen, \(\int_0^1|U|^\theta\le G^\theta\) for \(\theta\le1\).

The hypothesis holds: \(an\le(G/\tau)^3=O(p^{15/8})\le c_0p^2\) for large \(p\). The all-heavy part is therefore at most
\[
C_0\big(G^{5/8}G^{5/8}G^{3/4}G^{3/4}+G^2\big)=C_0\big(G^{11/4}+G^2\big).
\]

**Light part.** Every term with at least one light role is at most \(4\tau G^3\). This uses Step 2: the light variable is determined by the other three. Since \(\tau G^3=O(p^{11/8})\), the lemma follows.

### Step 5: energy

\[
E^\times(m)\le C(1)^2+\sup_{\lambda\ne1}C(\lambda)\cdot M_1^2 .
\]
For the first term, \(C(1)=\sum m^2\le G\,M_1\le G^3=O(p^{3/2})\), so \(C(1)^2=O(p^3)\). Round 177's \(O(p^{3/2-3/418})\) is not needed. The second term is \(O(p^{11/8}p^2)\). Hence \(E^\times(m)=O(p^{27/8})\).

### Step 6: the slope-product sum

By Cauchy–Schwarz,
\[
\sum_\xi W_\xi^{3/2}\le\Big(\sum_\xi W_\xi\Big)^{1/2}\Big(\sum_\xi W_\xi^2\Big)^{1/2}=M_1E^\times(m)^{1/2}=O(p^{43/16}).
\]
The Round 178 term \(\sum_\xi W_\xi^2/p\) also improves, to \(O(p^{19/8})\).

### Step 7: propagation through Round 178

**Right energy.**
\[
\mathcal E(\mu)=O\big(p^{19/8}+p^{43/16}+p^{5/2}\log p+p\big)=O(p^{43/16}).
\]

**Weighted affine incidence (Rudnev–Shkredov).** The second norm of \(H_\alpha\) is
\[
G^{5/8}\cdot p^{43/128}\cdot G+O(p)=O(p^{147/128}),
\]
since \(5/16+43/128+1/2=147/128\).

**Squared and weighted.** \(\sum w(t)\,\|H_\alpha\|^2\le G\,p^{147/64}=O(p^{179/64})\).

**One-match covariance.** Subtracting 1 in the Round 173 normalization gives \(O(p^{115/64})\).

**Not affected:** the zero-match term, and the separate full-diagonal results.

### Corollary at fixed slope

For a fixed slope \(a\), the right correlation's first mass is \(\sum_c\Delta(a,c)=\sum_r m(r)m(ar)=C(a)\), as stated in Round 177. Step 4 gives \(O(p^{11/8})\) for every \(a\ne1\). Multiplying by the Round 176 generic maximum \(O(p^{1-1/1280-1/840})\) bounds the fixed-\(a\) generic squared mass by \(O(p^{19/8-1/1280-1/840})\).

## Proved vs conditional vs evidence

**Proved, label (a), for all sufficiently large \(p\):**
- Lemma \(\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8})\).
- \(E^\times(m)=O(p^{27/8})\).
- \(\sum_\xi W_\xi^{3/2}=O(p^{43/16})\).

These have only the external input Stevens–de Zeeuw Theorem 4. Its hypotheses are checked above: \(p\ne2\), \(an\le c_0p^2\), the orientation \(a\le b\), and the complementary case \(ab^2>n^3\).

**Proved (a), reusing Round 178's accepted deductions unchanged:**
- \(\mathcal E(\mu)=O(p^{43/16})\).
- \(H_\alpha\) second norm \(O(p^{147/128})\).
- \(\sum w|H_\alpha|^2=O(p^{179/64})\).
- One-match covariance \(O(p^{115/64})\).

**Proved (a), also reusing the accepted Round 176 generic maximum:** the fixed-\(a\) first mass and the corresponding squared mass.

**Conditional criterion (b).**
- If \(\sup_{\lambda\ne1}C(\lambda)=O(p^{1+\theta})\) with \(0\le\theta\le3/8\), then \(E^\times(m)=O(p^{3+\theta})\) and \(\sum_\xi W_\xi^{3/2}=O(p^{5/2+\theta/2})\).
- The lowest this sum can go is \(M_1^3/\sqrt{p-1}\).
- The one-match output of this route is \(p^{9/8}\mathcal E^{1/4}\), which is at least \(p^{7/4}\) for every point-plane bound when \(M_1\asymp p\).
- Since \(\mathcal E\ge M_1^4/(p(p-1))\), the route can never reach \(p^{3/2}\) if \(M_1\gg p^{7/8+\varepsilon}\).

**Finite evidence (c).**
- *Exact, at \(p=13,17,29\):* injectivity of the line family for every \(\lambda\notin\{0,1\}\); single-variable determination on random samples of tuples; equality of \(C(\lambda)\) with the incidence count over all tuples; and \(\sum C^2=\sum W^2\). These use exact integer arithmetic, except that the weighted equalities are floating-point.
- *Floating-point FFT, \(p=1009,2017,4001,8009\):* synthetic weights only, namely random \(\sqrt p\)-subsets of \(Q\), the flat weight \(1/\sqrt p\) on \(Q\), the first \(\sqrt p\) squares, and subgroup and shifted-subgroup profiles. These are not the actual \(g\).
  - \(\sup_{\lambda\ne1}C/G^{11/4}\) lies between \(0.005\) and \(0.05\).
  - \(\sum W^{3/2}\) lies within 6% of the floor \(M_1^3/\sqrt p\), except for the shifted-subgroup profile at 3–6 times the floor.
  - In every case it lies below the old bound \(\max W^{1/2}M_1^2\).

**Scripts:**
- `/private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r180/check_r180.py`, output in `check_r180.out`
- `/private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r180/check_r180_shifted.py`, output in `check_r180_shifted.out`

The scripts need Python with numpy, e.g. `/opt/homebrew/opt/python@3.13/bin/python3.13`. The exponent arithmetic is checked with exact fractions.

## Exact remaining gap

**Slope-product sum.** The sum is now \(p^{43/16}\) against the floor \(p^{5/2}\). Closing it needs \(\sup_{\lambda\ne1}C(\lambda)=O(p^{1+o(1)})\), or a summed bound \(\sum_{\lambda\ne1}C(\lambda)^2=O(p^{3+o(1)})\).

**One-match covariance.** It is \(p^{115/64}\) against the target \(p^{3/2}\), a gap of \(p^{19/64}\). The route's floor is \(p^{7/4}\) for point-plane energies and \(p^{13/8}\) for any energy when \(M_1\asymp p\).

In Round 178's layer-cake bookkeeping, the target is equivalent to a level bound
\[
\|F_\mu1_U\|_2\ll M_1(1+|U|/\sqrt p)\cdot(|U|/G)^{\theta}\quad\text{for some }\theta<1 .
\]
That means removing the main term \(|U|^{5/8}\mathcal E^{1/8}M_1^{1/2}\) entirely. Equivalently,
\[
\sum_h\Delta(h)\big(m_U(h)-|U|^2/p\big)=O(p^2)
\]
for level sets \(|U|\le G\), where \(m_U(h)=|U\cap hU|\). The zero-match term and the full diagonal \(O(p^{3/2})\) remain open.

## Two ranked next tests

1. **One-match without the energy route.** Bound \(\sum_h\Delta(h)m_U(h)\) directly by slope fibres \(h=(a,c)\). Use the new fixed-slope first masses \(\sum_c\Delta(a,c)=C(a)=O(p^{11/8})\) for \(a\ne1\), and the translation overlaps \(m_U(a,\cdot)\) together with \(E^+(U,aU)\), keeping the actual \(D\) amplitudes and \(w\). The required size is \(O(p^2)\) after subtracting the mean \(M_1^2|U|^2/p\). Any argument through \(\mathcal E(\mu)\) and Rudnev–Shkredov is capped at \(p^{13/8}\) when \(M_1\asymp p\).
2. **Improve \(\sup_{\lambda\ne1}C(\lambda)\) below \(p^{11/8}\).** Use the actual level-set structure, for example the hereditary quotient/BSG extraction of Rounds 173, 176 and 177: Theorem 4 is weaker on small-quotient grids. Alternatively, bound \(\sum_{\lambda\ne1}C(\lambda)^2\) through rich-\(\lambda\) incidences with multiplicity control. The multiplicity of a line across \(\lambda\) is at most its richness in \(S\times S\). The constraint \(an\ll p^2\) currently limits this to about \(p^{1/2}\) values of \(\lambda\).
