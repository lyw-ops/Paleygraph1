# Propagating hot control on the actual marked curve

Round 37. Finite prime monodromy motivates doing the hot-to-cold
argument on the normalized marked curve. A small hyperbolic distance
on that curve suffices, even if the chosen scalar has no single-valued
branch on a proposed domain of the parameter plane. This gives a
specific metric estimate to investigate for primes.

## The surface and its marked function

Use the saturated physical curve and the generic scalar lift of
[round 36](parallel-cold-complex-36.md). Take the smooth projective
normalization of the irreducible image of the physical curve under
$(\tau,\xi,s)\mapsto(\tau,u_0)$. Denote its finite nonconstant parameter
map by $\tau_Y$ and its meromorphic marked coordinate by $u_0$.
Let $Y$ be the connected component of $\tau_Y^{-1}(\{\Re\tau>0\})$
containing the positive physical real lift. The real positive solutions
are unique and regular on the full stationary curve, so each fixed
real interval $[a,2048]$ lifts continuously to $Y$ on the physical
branch. This lift determines specific points $y_a,y_{2048}$ of $Y$.

On $Y$ set $F=\sqrt{W(\tau_Y)/n}\,u_0$ with the principal square root.
Away from finitely many exceptional scalar points, the lift to the
saturated stationary curve gives the sector inequality

$$
\operatorname{dist}(\arg F,\pi\mathbb Z)
\le \tfrac12|\arg W(\tau_Y)|<\pi/4,
$$

The inequality extends to every nonzero finite value by continuity.
A zero or pole of $F$ on $Y$ would force the argument on a small
coordinate circle to wind a nonzero integer number of times,
contradicting that inequality. Thus $F$ is nonvanishing and holomorphic
on $Y$. Since $Y$ is connected and $F(y_{2048})>0$, the positive sector
holds throughout. Its principal logarithm $m_Y$ obeys
$|\Im m_Y|<\pi/4$ everywhere. These statements include
ramification points of the map $\tau_Y$ in the right half-plane.

The surface $Y$ is hyperbolic. Its universal cover carries the bounded
nonconstant holomorphic map
$((\tau_Y-2048)/(\tau_Y+2048))\circ\mathrm{cover}$ into the disk. The sphere
and the plane cannot carry such a map. By uniformization the cover is
the unit disk.

## Quantitative propagation on the surface

Let $d=d_Y(y_a,y_{2048})$ in the curvature-$-1$ metric.
Choose a disk covering map $h$ with $h(0)=y_{2048}$.
For any lift $\zeta$ of $y_a$, set $r=|\zeta|$. Schwarz's lemma on
$(\tau_Y(h(z))-2048)/(\tau_Y(h(z))+2048)$ implies that the projection of
$|z|\le1/4$ is in the hot parameter disk

$$
\left|\frac{\tau-2048}{\tau+2048}\right|\le\tfrac14.
$$

The physical hot mark on the parameter plane and $m_Y\circ h$
agree near $0$. By the identity theorem they agree throughout
$|z|\le1/4$: the map $\tau_Y\circ h$ stays inside the open hot region
there, with a strict margin for $n>3414$. Thus on that disk
$|\tanh(m_Y\circ h)|\le8/\sqrt n$ by the accepted hot estimate.
On the entire covering disk $|\tanh(m_Y\circ h)|<1$ by the phase
bound. Three-circles gives the same interpolation estimate as in
[the base-domain argument](astra-cold-37.md#4-a-growing-prime-sufficient-condition-with-shrinking-domains).
Take a sequence of lifts approaching the infimum of the disk
distances to $0$. Since $r=\tanh(d_{\mathbb D}(0,\zeta)/2)$, this yields

$$
|\tanh m_q(a)|\le (8/\sqrt n)^{
\min\{1,\,\log\coth(d/2)/\log 4\}}.
$$

In particular $(\log n)e^{-d}\to\infty$ would give vanishing actual
marks at a fixed cold point. Applying this for a sequence of cold
floors tending to zero would imply the original ordinary theta limit.
At a fixed $a\in(0,1)$ the actual square-field lower bound instead
forces $d\ge\log\log n-O_a(1)$, even on the normalized surface.

When a base domain admits a single-valued physical branch, its lifted
section into $Y$ contracts hyperbolic distance. The surface distance
is therefore bounded above by any such base-domain distance. The
surface criterion also applies when no section of a proposed domain
exists, as with the certified prime-173 loop. No useful uniform upper
bound for the surface distance through primes is established here.

## A narrower square-field obstruction

Fix $0<a<1$, let $T=2048$, and fix $\epsilon>0$. For sufficiently large
square orders take

$$
\delta_n=\frac{(2+\epsilon)\log(T/a)}{\log\log n},\qquad
D_n=\bigcup_{a\le x\le T}B(x,x\delta_n).
$$

Eventually $\delta_n<1$, so $D_n$ is in the right half-plane. Each
vertical fiber is an interval containing its real-axis point, and
vertical contraction retracts $D_n$ to a real interval. Thus $D_n$
is simply connected. If the component over $D_n$ containing the real
physical lift had no ramification, its finite proper projection would
be a covering and admit a single-valued section on all of $D_n$.
Every centered disk gives an upper metric density $2/(x\delta_n)$
on the real interval. The section would then give

$$
d_Y(y_a,y_T)\le d_{D_n}(a,T)
\le \frac{2\log(T/a)}{\delta_n}
=\frac{2}{2+\epsilon}\log\log n.
$$

The square lower bound for $d_Y$ contradicts this for all sufficiently
large square orders. Therefore there is an accessible actual marked
ramification point over $D_n$. It is accessible from the real lift
inside that component because deletion of finitely many ramification
and branch preimages leaves a connected surface. In particular these
branch values approach the real interval in the sense that
$a(1-\delta_n)<\Re\tau<T(1+\delta_n)$ and
$|\Im\tau|<T\delta_n=O_a(1/\log\log n)$ for fixed $\epsilon$.
They may be on another locally reached sheet over the real axis.
This is an asymptotic square statement and gives no corresponding
prime concentration of branch values.
