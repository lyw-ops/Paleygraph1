# A marked sector theorem: complex growth is automatic, continuation is not

Round 36. **The all-prime ordinary-theta target remains open.** There is,
however, a positive structural improvement to the complex route:

> On any connected right-half-plane domain where the actual marked germ
> has a single-valued holomorphic continuation, its unwrapped phase is
> bounded by `pi/4`. A common cold–hot domain therefore automatically
> supplies the required uniform complex-growth bound. No separate prime
> growth conjecture is needed on such a domain.

This is a theorem for the **actual** stationary curve, with its strong
marked weight, not a claim about arbitrary real analytic functions. It
uses a conjugate pairing with the opposite sector. It also applies when
only the marked scalar continues: a generic algebraic lift suffices;
single-valued continuation of the entire spectrum is unnecessary.

For squares this resolves the old extension-versus-large-phase
disjunction in favor of failed extension. In particular, for every square
field `q=2n+1` with `n>exp(100000)`, the physical marked algebraic branch
has a genuine accessible branch point in

\[
                 \Re\tau>1/16,\qquad |\tau|\le1024.             \tag{1}
\]

The threshold is deliberately very large. This is an existence theorem
about the actual branch, not a numerical location, a discriminant test,
or a counterexample at a specified manageable field order.

Inputs: [round 35 structural theorem](parallel-complex-structure-35.md),
[its independent acceptance, Section 7](parallel-audit-35.md),
[round 33](complex-floor-33.md), and
[round-35 acceptance](averaged-complex-35-acceptance.json).
The hot estimate and the
[exact square theta value](square-order-control.md) are inherited inputs.
The mixed Mellin/sheaf proof behind the hot estimate is not reaudited here.

## 1. The exceptional coordinate forces a complex sector

Let `n=(q-1)/2`, `c=tau/n`, `N=n-1`, and

\[
             w_0=1,\quad w_i=c\ (i\ne0),\quad W=1+Nc.          \tag{2}
\]

Work in either of the actual real even Paley tangent spaces, with a
real full-column-rank basis matrix `B`. A normalized row is
`u=1+B xi`. A complex stationary point away from coordinate zeros obeys

\[
              B^T(w/u)=0.                                    \tag{3}
\]

Division and all products of rows in this note are coordinatewise.
Since both `u-1` and `conj(u)-1` belong to the complexification of the
same **real** tangent space, (3) gives the two exact identities

\[
 \sum_i\frac{w_i}{u_i}=W,
 \qquad \sum_i w_i\frac{\overline{u_i}}{u_i}=W.                 \tag{4}
\]

For the first one, pair (3) with `xi`; for the second, pair it with
`conj(xi)` and then use the first. Set `r_i=conj(u_i)/u_i`;
each `|r_i|=1`. The second identity implies

\[
 |W-r_0|=|c|\left|\sum_{i\ne0}r_i\right|\le N|c|.
\]

Expanding the squares and using `W=1+Nc` yields

\[
                    \Re(W\overline{r_0})\ge\Re W.              \tag{5}
\]

On `Re tau>0` fix the square root `mu=sqrt(W/n)` positive on the
positive axis. The actual scaling is `A=mu u`. Since

\[
 W\overline{r_0}=|W|\frac{A_0}{\overline{A_0}},
\]

we obtain the **marked sector inequality**

\[
 \boxed{\quad
 \Re\frac{A_0}{\overline{A_0}}
       \ge\frac{\Re W}{|W|},\qquad
 \operatorname{dist}(\arg A_0,\pi\mathbb Z)
       \le\frac12|\arg W|<\frac\pi4.
 \quad}                                                       \tag{6}
\]

It holds for every complex stationary solution with nonzero
coordinates, including nonphysical chambers. Their marked signs can
differ. A continuation of the positive physical marked value stays in
the positive component of these two separated sectors.

### Opposite-sector and normalization check

Define `Bopp_i=w_i/A_i` (this `Bopp` is a row, not the basis matrix).
Equation (3) puts `Bopp` in the opposite sector plus constants.
The first identity in (4) gives `mean(Bopp)=mu`, exactly as for `A`.
Consequently the complementary-sector orthogonality can alternatively
be written

\[
 \sum_i\overline{A_i}\,Bopp_i=n|\mu|^2=|W|.
\]

The marked term of that displayed sum is `conj(A_0)/A_0`, so
`| |W|-conj(A_0)/A_0| <= N|c|`, which again gives (6).
Thus the argument preserves the actual reciprocal relation
`A_i Bopp_i=w_i`, both sector constraints, and both means.

The weight `w_0=1` is essential: replacing it by the bulk weight would
change (5). There is exactly one marked exceptional coordinate;
self-inverse Fourier positions remain bulk coordinates of weight `c`.
No exceptional multiplier is deleted and no full-Hessian norm estimate
is used. The argument works for either sector and does not assume a
Pick/Stieltjes representation.

## 2. Why scalar continuation alone is enough

Here are the algebraic details needed to avoid silently strengthening
the continuation hypothesis. Fix a positive real base point. Introduce
`u=1+B xi` and an extra variable `s`, clear (3)'s denominators, and add

\[
                         s\prod_i u_i=1.                       \tag{7}
\]

This gives a polynomial stationary variety and excludes every
coordinate-zero component. At the physical base point the derivative
in `xi` is the negative definite real matrix

\[
                    -B^T\operatorname{diag}(w/u^2)B.
\]

Thus the variety is smooth of local dimension one there, with `tau`
a local parameter, and has a unique irreducible curve component `C`
through that point. It is the physical stationary algebraic curve.
The closure of its image under `(tau,xi,s) -> (tau,u_0)` is an
irreducible curve `C0`, possibly simply `u_0=constant`.

The dominant map `C -> C0` has finite generic fibers: its function
fields have transcendence degree one and the extension is algebraic
and finite. After removing finitely many points of `C0`, every point
has a lift to the affine curve `C` satisfying (7). One elementary
way to see the finite exclusion is to take a primitive element of
the function-field extension, express the coordinates rationally in
it, and exclude poles, leading-coefficient zeros, and the finitely
many specialization exceptions. Each remaining fiber has a root over
the algebraically closed field `C`. The excluded points have only
finitely many `tau` coordinates.

Now suppose the actual germ `m=log A_0` has a single-valued holomorphic
extension to a connected domain `D` in `Re tau>0`. Put

\[
                  f=e^m,\qquad z=f/\sqrt{W/n}.
\]

The defining polynomial of `C0` vanishes at `(tau,z(tau))` near the
base point, hence everywhere on `D` by the identity theorem.
Outside the finite exceptional set just described it has a lift to
`C`. Apply (6) to that lift. Continuity extends the inequality to
every point of `D`. Since `f` is nonzero and initially positive,
connectedness selects the positive sector throughout:

\[
       \Re f>0,\qquad |\operatorname{Arg}f|
                 \le\tfrac12|\arg W|<\pi/4.                   \tag{8}
\]

The analytic logarithm of a positive-real-part function has principal
imaginary part in `(-pi/2,pi/2)`. It agrees with the actual real
normalization at the base point. Its difference from `m` is a constant
integer multiple of `2pi i`, equal to zero there. Therefore

\[
 \boxed{\qquad |\Im m(\tau)|\le\tfrac12|\arg W(\tau)|<\pi/4
                  \quad(\tau\in D).\qquad}                    \tag{9}
\]

This bounds the **unwrapped analytic phase**, not just a principal
argument chosen independently at each point. Generic lifts may be
multivalued, and may leave the positive real chamber. Neither affects
the stationary identity (4) or the marked component selection.

The same proof works if the assumed scalar continuation is a
holomorphic `A_0` rather than `m`. Away from its isolated zeros it
has the sector property. Continuity gives `Re A_0>=0` everywhere;
the minimum principle, using the positive base value, makes this
strict. Its canonical logarithm then supplies `m` on all of `D`.

## 3. Uniform growth on a common domain, with explicit constants

Let `D` be a simply connected right-half-plane domain containing
`[a,T+1]`, with `T>1024`. Let `phi:D -> unit disk` be a conformal
map with `phi(T)=0`. Suppose the actual marked germs for a family of
field orders extend holomorphically to `D`. For large enough `n`, the
inherited hot theorem gives `|m_q(T)|<=4/sqrt(n)`.

By (9), the function

\[
                   g_q=\tanh(m_q-m_q(T))
\]

maps `D` into the unit disk and vanishes at `T`. Schwarz's lemma
after the conformal change gives `|g_q(z)|<=|phi(z)|`. The inverse
`arctanh` on the unit disk is the inverse of `tanh` on the strip
`|Im z|<pi/4`; its power series has positive absolute coefficients.
Consequently

\[
 \boxed{\quad |m_q(z)|\le\frac4{\sqrt n}
                     +\operatorname{arctanh}|\phi(z)|.\quad}   \tag{10}
\]

On each fixed compact subdomain `D0` this is an `O_{D,D0}(1)` bound,
independent of the field. In a disk of radius `Rbig` centered at `T`,
the explicit bound on the concentric disk of radius `R<Rbig` is

\[
 \frac4{\sqrt n}+\frac12\log\frac{Rbig+R}{Rbig-R}.               \tag{11}
\]

For a general connected common domain containing the real interval,
choose a smaller simply connected tube around that interval, compactly
contained in the original domain; the same conclusion applies there.

In particular the round-33 slit two-constants argument now needs only
the **common marked continuation domain** through primes. If `omega`
is the fixed positive harmonic measure in a compact inner domain,

\[
                         |m_p(a)|=O_D(p^{-\omega/2}).            \tag{12}
\]

The former subpolynomial-growth or phase assumption is discharged by
(9)–(10), with a bounded-growth result. A domain reaching each member
of a sequence `a_j downarrow 0` would prove the target, taking the
prime limit first as before. **No such prime common cold domain has
been proved here.** Real derivative bounds or finite-field checks are
not being substituted for it.

## 4. An actual square branch obstruction, not an eliminant zero

Already (10) and the round-33 square lower bound imply the following:
for any fixed common right-half-plane domain containing a cold point
`0<a<1` and a hot interval, all sufficiently large square marked germs
fail to extend single-valuedly and holomorphically over that domain.
There is no remaining large-unwrapped-phase alternative.

Here is one completely explicit, though inefficient, version. Set

\[
 T=2048,\quad a=1/4,\quad
 Rbig=2048-1/16,\quad R=2048-1/8,\quad r=2048-1/4,\quad r_0=1024.
                                                                    \tag{13}
\]

Suppose the actual square marked logarithm extends to
`D={|tau-T|<Rbig}`. Its real parts exceed `1/16`. For `n>3072`,
the hot theorem bounds `|m|<=4/sqrt(n)` on the inner circle of
radius `r0`. At its one boundary point `tau=1024`, take the limit
from the hot region, using the assumed holomorphy on `D`.
Equation (11) bounds the modulus on the radius-`R` circle by

\[
        4/\sqrt n+\tfrac12\log65533<7.                         \tag{14}
\]

Hadamard's three-circles theorem, at radius `r`, now yields

\[
 |m(a)|\le(4/\sqrt n)^\omega 7^{1-\omega},\qquad
 \omega=\frac{\log(16383/16382)}{\log(16383/8192)}
                  >0.00008807.                               \tag{15}
\]

For `q=h^2`, the exact values are `theta_-=(h+1)/2` and
`theta_+=h-1`. The subfield clique and the constant opposite-sector
witness proving this in [square-order control](square-order-control.md)
also work for any odd prime-power `h`: only the subfield inclusion
and the finite-field Jacobi bound `|lambda_k|<=h` are used.
The actual real stationary bracket therefore gives

\[
 m_q(1/4)\ge\tfrac12\log
     \frac{2(h-1)}{(h+1)[1+(1-1/n)/4]}.
\]

For `h>=11` the expression inside the log is strictly larger than
`4/3`. Since `log(4/3)>1/4`, this proves `m_q(1/4)>1/8`.
But at `log n=100000` the logarithm of the right side of (15) is
less than `-2.4576`, whereas `log(1/8)>-2.0795`. It decreases with
`n`. Thus

\[
 \boxed{\ n>e^{100000},\ q\text{ a square}
       \quad\Longrightarrow\quad m_q\text{ does not extend to }D.\ }\tag{16}
\]

All inequalities involving the numerical constants are enclosed by
Arb in the checker. The exact three-circle threshold has logarithm
approximately `91410.4614`; `100000` leaves a comfortable margin.

### Why this forces a physical marked branch point in (1)

The germ `A_0=exp(m)` is algebraic by Section 2. Start with its actual
hot germ at `T`. If the Taylor series of `m` there had radius at least
`Rbig`, it would define the forbidden extension to `D`. Its radius
`Rstar` is therefore strictly smaller, and some point on that circle
is a singularity of this **actual scalar germ**. It is not selected
from a discriminant of other components or sheets.

This point has `Re tau>1/16`. It cannot have `|tau|>1024`: the
intersection of the centered Taylor disk with
`{Re tau>0, |tau|>1024}` is connected (rotate each point about the
positive real center toward the rightmost radius; its modulus about
zero increases). The Taylor function thus agrees there with the
accepted actual hot branch by the identity theorem. As `n>e^100000`,
the whole relevant disk also has `|tau|<n`. The hot branch would
extend the purported singularity. Hence `|tau|<=1024`.

Finally this is a genuine ramification point of the marked algebraic
function, not a logarithm singularity above an ordinary zero or pole.
To check this, take the normalization of the physical marked curve
and a local parameter `t` at any accessible point over the right
half-plane. If

\[
 \tau=\tau_*+t^k,\qquad A_0=t^j h(t),\qquad h(0)\ne0,
\]

then analytic continuation around a small full `t` circle continues
the marked value through the accessible sheets. At every generic
point (6) holds, and continuity keeps the value in the positive
sector; a finite number of generic-lift exceptions is harmless.
Its winding about zero is consequently zero. The displayed local
factorization has winding `j`, so `j=0`. Thus the marked value is
finite and nonzero at every such point. If it were unramified as a
marked function, its logarithm would extend locally. A singularity
of the actual logarithm in this half-plane must therefore be genuine
marked ramification, with a finite nonzero limiting marked value.

This argument tracks the physical germ analytically from `T` and
uses the saturated stationary component throughout. It requires no
floating branch tracking and no claim that every discriminant zero
belongs to that germ. It does not give an individual numerical
coordinate of the branch point or a practical smallest square order.

## 5. Exact replay and remaining work

Run from the repository root:

```sh
.venv/bin/python -B research/parallel-cold-complex-36.py \
  > research/parallel-cold-complex-36-certified.jsonl
```

The checker uses exact Gaussian rationals on the accepted actual
prime-13 stationary curve to check both sector constraints, means,
the exceptional product weights, (4), and the phase-disk inequality.
The nonreal samples are algebraic stationary-point checks; they are
not used as physical branch-tracking certificates. A positive real
base sample is checked as the actual physical stationary row by
strict positivity and concavity. Further Arb records verify the
explicit square-obstruction constants. The uniform assertions are
proved above; finite samples are only normalization checks. These
are ordinary mathematical proofs and interval checks, not Lean proofs.

The strongest new prime conclusion is a reduction: a common scalar
cold–hot domain in the right half-plane suffices **on its own**.
Direction-sensitive continuation still has to distinguish primes from
squares. A field-general common-domain argument is now rigorously
excluded for all sufficiently large squares, even if it attempts to
allow arbitrarily large marked growth. No prime common cold domain,
prime branch-point exclusion, or ordinary-theta asymptotic is claimed.

Only `research/parallel-cold-complex-36*` is written. No README,
ledger, other prefix, commit, push, or external communication is part
of this research line.
