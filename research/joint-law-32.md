# A common joint law for the first rank-three nested family

Round 32. The [uniform positive phase](astra-prime-phase-32.md) closes
the arithmetic identification for this specific family. Together with
the independent derived-group calculation in
[round 31](astra-nested-moment-31.md), it determines the full joint law
of the three fields

\[
 x=F_Qs/\sqrt n,\qquad y=K(x^2),\qquad z=K(xy),
 \qquad q=2n+1\equiv1\pmod4.                              \tag{1}
\]

This is a common prime/square law for **these fields and continuous
functions of them**. It is not the missing matching theorem for every
later nested word or every fixed nonlinear iterate. No estimate of the
actual stationary tail follows merely from this weak law.

## 1. The connected group and its arithmetic identification

Keep the ordinary/perverse conventions of round 31. The relevant objects
are the Jacobi object \(\mathcal M\), the two rank-three objects
\(\mathcal R,\mathcal R'\), and the two old twisted-Legendre objects
\(\mathcal N,\mathcal N'\). In their Mellin representations, round 31
proved the inclusion of the independent derived factors

\[
 D=SL_3^2\times SL_2^2\subseteq G_{\rm geom}.
\]

The Jacobi projection is onto \(\mathbb G_m\). The exact arithmetic
identities proved in round 32, with \(\chi(-1)=1\), are

\[
 \det\mathcal R=\mathcal M^\vee,\qquad
 \det\mathcal R'=\mathcal M,
\]

while the two rank-two representations have determinant one. Thus both
geometric and arithmetic groups lie in

\[
 H=\{(m,U,V,S,T)\in\mathbb G_m\times GL_3^2\times SL_2^2:
                    \det U=m^{-1},\ \det V=m\}.          \tag{2}
\]

The kernel of \(H\to\mathbb G_m\) is exactly \(D\). Since
\(G_{\rm geom}\) contains that kernel and maps onto the quotient,
it equals \(H\): given any \(h\in H\), choose \(g\in G_{\rm geom}\)
with the same \(m\); then \(hg^{-1}\in D\). Consequently

\[
 \boxed{G_{\rm geom}=G_{\rm arith}=H.}                    \tag{3}
\]

In particular no extra finite component or arithmetic coset remains in
this family. This conclusion uses the newly proved **arithmetic**
determinant; its geometric counterpart alone did not justify (3).
It does not construct the general cross-prime Artin model contemplated
in round 30.

## 2. A concrete compact probability model

Let \(J\) be Haar uniform on the unit circle. Conditional on \(J\),
choose independently

\[
 U\in U(3),\quad\det U=J^{-1},\qquad
 V\in U(3),\quad\det V=J,
\]

with Haar probability on the specified determinant cosets. Independently
choose Haar \(S,T\in SU(2)\). Put

\[
 X=\sqrt2\operatorname{Re}J,\quad
 Y=\frac{\operatorname{Tr}S+\operatorname{Tr}T}{2},\quad
 Z=\frac{\operatorname{Re}\operatorname{Tr}U
              +\operatorname{Re}\operatorname{Tr}V}{\sqrt2}.
                                                               \tag{4}
\]

These are real variables. In particular \(Y\) is independent of
\((X,Z)\). One may generate the conditional cosets by multiplying
independent Haar \(SU(3)\) matrices on the left by
\(\operatorname{diag}(J^{-1},1,1)\) and
\(\operatorname{diag}(J,1,1)\).

The positive sums \(J,A,C\) in round 31 are negatives of their perverse
Mellin traces; the two old twisted-Legendre Mellin traces already have
the \(V\) convention in (5). This does not change the Haar model:
multiplication by

\[
 (-1,-I_3,-I_3,I_2,I_2)\in H
\]

is a central translation preserving Haar measure. It is not asserted
to be a group homomorphism, nor is a constant minus sign silently
identified with a base-change-compatible twist. The determinant
constraints in the positive-trace coordinates are precisely those in
(4).

For clarity the full-character positive sums are

\[
 J_\alpha=q^{-1/2}\sum_a\alpha(a)\ell(a),\quad
 A_\alpha=q^{-3/2}\sum_a\alpha(a)r(a),\quad
 C_\alpha=A_{\alpha\chi}.
\]

Away from the two bad full characters \(1,\chi\),
\(J_{\alpha\chi}=\overline{J_\alpha}\), and the exact aliases give

\[
 \begin{split}
 x&=\frac{\sqrt q}{2\sqrt n}(J_\alpha+\overline{J_\alpha}),\\
 y&=\frac q{4n}(V_\alpha+V_{\alpha\chi})-x/\sqrt n,\\
 z&=\frac{q^{3/2}}{8n^{3/2}}
          (A_\alpha+C_\alpha+\overline A_\alpha+\overline C_\alpha)
                      -y/\sqrt n+x/(2n).                  \tag{5}
 \end{split}
\]

Here the two real \(V\)'s are the old rank-two fields. The good Mellin
Frobenius classes belong to a maximal compact subgroup of (3).
Thus \(|J_\alpha|=1\), \(|A_\alpha|,|C_\alpha|\le3\), and
\(|V_\alpha|,|V_{\alpha\chi}|\le2\). Formula (5) is uniformly within
\(O(q^{-1/2})\) of the compact model's coordinate map. The two full
bad characters map to the single trivial character of \(Q\); discard
that one frequency in the following statements.

Mellin equidistribution for (3), in the uniform fixed-word form already
used in round 31, now implies for every fixed polynomial \(P\)

\[
 \frac1{n-1}\sum_{k\ne0}P(x_k,y_k,z_k)
        =\mathbb E P(X,Y,Z)+O_P(q^{-1/2}).                 \tag{6}
\]

For each fixed continuous test function the analogous error is
\(o(1)\), using polynomial approximation on the common compact bound;
no universal \(O(q^{-1/2})\) rate is claimed for arbitrary continuous
functions. The limit is the same through all primes and through square
orders (indeed all odd prime powers satisfying the congruence).

## 3. Good-frequency maxima and square-root-size top sums

Let \(\mathscr C\) be the compact image of (4). For any fixed real
continuous function \(F\) on a neighborhood of that image,

\[
 \max_{k\ne0}F(x_k,y_k,z_k)
          \longrightarrow\max_{\mathscr C}F.             \tag{7}
\]

The upper bound in (7) uses the **pointwise compact-group membership**
and the uniform aliases (5), not just a weak limit. For the lower bound,
the inverse image of a neighborhood of any maximizing point is a
nonempty open set of the compact group, hence has positive Haar mass.
Equidistribution supplies a positive proportion of good frequencies
in that neighborhood.

For nonnegative \(F\), set \(G_k=F(x_k,y_k,z_k)\) at good frequencies
and set \(G_0=0\). If \(k_q/\sqrt n\to\kappa>0\), the same argument
gives the sharper critical-tail statement

\[
 \operatorname{Top}_{k_q}(G/\sqrt n)
                  \longrightarrow\kappa\max_{\mathscr C}F. \tag{8}
\]

The top sum may use fractional final weight. For each fixed proximity
to the maximum there are \(\gg n\) eligible entries, hence more than
\(k_q=O(\sqrt n)\). Their upper and lower bounds prove (8).
A bounded value assigned at the one bad frequency changes the result
by \(O(n^{-1/2})\); an unbounded assignment is outside this statement.

Thus this particular finite family gives a proved common arithmetic
model and matching good-frequency extrema/tails. It does **not** justify
applying (7) or (8) to a later activated field that is not a continuous
function of the three coordinates in (1). In particular the general
matching premise in [round 30](astra-arithmetic-coset-30.md) remains open.

## 4. Exact mixed-moment rule

Let \(m_3(a,b)=\int_{SU(3)}(\operatorname{Tr}S)^a
\overline{\operatorname{Tr}S}^{,b}\,dS\). Schur--Weyl duality gives

\[
 m_3(a,b)=\sum_{\substack{\lambda\vdash a,\ \mu\vdash b\\
              \ell(\lambda),\ell(\mu)\le3\\
              \lambda-\mu\in\mathbb Z(1,1,1)}}f^\lambda f^\mu,
                                                               \tag{9}
\]

where partitions are padded to length three and \(f^\lambda\) is the
number of standard tableaux, given by the hook-length formula. It
vanishes unless \(a-b\) is divisible by three. Conditional determinant
scaling then gives

\[
 \mathbb E[J^h(\operatorname{Tr}U)^a
      (\overline{\operatorname{Tr}U})^b
      (\operatorname{Tr}V)^c(\overline{\operatorname{Tr}V})^d]
 =\begin{cases}
    m_3(a,b)m_3(c,d),&h-(a-b)/3+(c-d)/3=0,\\
    0,&\text{otherwise}.
   \end{cases}                                             \tag{10}
\]

Each factor must also satisfy its divisibility condition. For example
\(\mathbb E[J(\operatorname{Tr}U)^3]=1\), whereas replacing \(J\)
by \(\overline J\) gives zero. Keeping that orientation is essential.

The independent \(SU(2)\) traces have even moments equal to Catalan
numbers and odd moments zero. Therefore

\[
 \mathbb E Y^t=2^{-t}\sum_{i=0}^t\binom ti
       m_2(i)m_2(t-i),\qquad
 \mathbb E[X^rY^tZ^s]=\mathbb E[X^rZ^s]\,\mathbb E Y^t.    \tag{11}
\]

Expanding (4) in (10) produces exact rational answers, including

| Moment | Exact limit |
|---|---:|
| \(\mathbb E Z^2\) | \(1/2\) |
| \(\mathbb E Z^4\) | \(3/4\) |
| \(\mathbb E XZ^3\) | \(1/8\) |
| \(\mathbb E Z^6\) | \(125/64\) |
| \(\mathbb E XZ^5\) | \(35/64\) |
| \(\mathbb E Z^8\) | \(7525/1024\) |
| \(\mathbb E XZ^7\) | \(1281/512\) |

These are deductions from the joint compact model, not fits to sampled
field moments. High powers can have substantial finite-field errors,
particularly on the smaller square controls; no small effective constant
for (6) is inferred from the displayed table.

## 5. Replay and independent checks

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/joint-law-32.py > research/joint-law-32-check.jsonl
```

The 26 JSONL records comprise one exact, independently formulated Weyl
constant-term audit of all 81 \(SU(3)\) moment pairs \(0\le a,b\le8\),
twenty exact rational compact-moment records, and five floating
prime/square field comparisons through prime order \(1000033\).
Each field row includes twenty mixed moments, five oriented complex
determinant probes, and the exact-alias numerical residual. The independent
Weyl computation uses the squared Vandermonde on the two-dimensional
\(SU(3)\) torus and does not call the tableau formula.

The arithmetic group identification and sign conventions were also
independently reviewed by the Astra conversation in
[its note, §8](astra-prime-phase-32.md). The fixed-field records alone
would not establish (3), (6), or any asymptotic theorem. This work is an
ordinary mathematical argument resting on the cited sheaf inputs;
it is not a Lean kernel verification. The actual Paley source-tail and
growing-depth estimates required for Problem 26 remain unproved.
