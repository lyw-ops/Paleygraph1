# Off-diagonal support of the two-mark bodies

Let $C_+$ and $C_-$ be the antipolar [normalized two-mark bodies](sparse-mark-geometry.md#two-mark-diagonal-geometry) for a displacement $h\ne0$. Both are downward convex polygons in $[0,1]^2$ containing the two unit axis points. Write $r_C(t)$ for the dimension of the face selected by the maximization of $t\log z_1+(1-t)\log z_2$, and put $R(C)=\int_0^1 r_C(t)\,dt$. The conditional rank term is $D(h)=[R(C_+)-R(C_-)]/2=R(C_+)-1/2$.

## Integration over support normals

For any such polygon $C$, let $U_C(x)=\log h_C(e^x,1)$ and let $T_C(x)=U_C'(x)$ where the derivative exists. On an interval exposing a single vertex $(a,b)$, we have

$$T_C(x)=\frac{e^x a}{e^x a+b},\qquad T_C'(x)=T_C(x)(1-T_C(x)).$$

At a positive-normal supporting edge, the jump of $T_C$ is the length of the interval of weights $t$ that select an interior point of that edge. Indeed, for an interior optimizer $z$ the gradient $(t/z_1,(1-t)/z_2)$ is proportional to the normal $(e^x,1)$, so $t=e^xz_1/(e^xz_1+z_2)$. The endpoints give the one-sided derivatives. The total increase of $T_C$ is one because the polygon has unit axis maxima. Thus

$$R(C)=1-\int_{\mathbb R}T_C(x)(1-T_C(x))\,dx.$$

For $B>0$ the combined tails outside $[-B,B]$ are at most $2 e^{-B}$, using $T_C(x)\le e^x$ for $x<0$ and $1-T_C(x)\le e^{-x}$ for $x>0$. These follow from $h_C(e^x,1)\ge\max(1,e^x)$ and $a,b\le1$.

For a second polygon $E$ with the same axis maxima, $U_C-U_E$ vanishes at both infinities. Subtracting the two rank formulas and integrating by parts gives

$$R(C)-R(E)=-\int_{\mathbb R}(U_C-U_E)\,d(T_C+T_E).$$

The measure on the right is positive and has total mass two. In particular a pair with its two normalized support functions close in every positive direction satisfies the deterministic bound

$$|D(h)|\le \sup_{s>0}\left|\log\frac{h_{C_+}(s,1)}{h_{C_-}(s,1)}\right|.$$

The integral also localizes the effect of differences in directional support to the slope measure $d(T_{C_+}+T_{C_-})$. In the square and simplex cases the respective rank integrals are zero and one. They agree with the exact subgroup displacements.

## Enclosing the contribution of a shift by linear LPs

For a grid of weights $t$, [the probe](../two_mark_frontier.py) maximizes $tP_0+(1-t)P_h$ over plus spectra. The full real Fourier basis has nonconstant sine and cosine terms with coefficients bounded in absolute value by two, since $P\ge0$ and $\overline P=1$. Write the spectral constraints as $A x\le\mathbf1$ and the variable part of the cost as $c^\mathsf T x$. Every nonnegative dual multiplier $y$ gives the exact upper bound $\sum_i y_i+2\|c-A^\mathsf T y\|_1$. Adding a constant to the computed primal spectrum and renormalizing gives a feasible point in exact arithmetic. Both are divided by the plus one-mark maximum, after adding the constant cost term one on the upper side.

The coordinate axes, the downclosed hull of the primal points and their reflections give an inner polygon. The grid of dual inequalities clips the unit square to give an outer polygon. For any of these polygons, the unit axis maxima and integration by parts in the log value $L_C(t)$ yield $R(C)=-2\int_0^1 L_C(t)\,dt$. Thus the outer polygon gives the lower bound on $D(h)$ and the inner polygon gives the upper bound. The code computes the integral by summing the lengths of the weight intervals at the exposed edges. Its stored results use floating-point bases, LPs and hulls.

Complete vertex enumeration on eight orders at most 41 gave an independent comparison at all 76 nonzero shifts. The maximum deviation outside a computed interval was $1.9\times10^{-11}$. Integrating the support-slope identity separately for both signs at those shifts agreed with the directly enumerated rank integral within $1.4\times10^{-12}$.

## Prime and square comparisons

The [118 recorded rows](../data/two-mark-frontier.csv) use a mesh of step $1/16$ in the normalized linear cost. The largest directional gap between the repaired primal and dual support bounds was $6.9\times10^{-8}$. Each row below averages the two bounding methods over the same 12 random displacements, leaving out the extra exact subgroup tests. The last column gives the sample standard error of the new interval midpoint.

| Field order | Diagonal-only interval | Off-diagonal interval | Sample standard error |
|---:|---:|---:|---:|
| $401$ | $[-0.11719,0.04992]$ | $[-0.03555,-0.03242]$ | $0.02510$ |
| $31^2$ | $[0.36009,0.38598]$ | $[0.37498,0.38555]$ | $0.08112$ |
| $1009$ | $[-0.09170,0.07739]$ | $[-0.01125,-0.00799]$ | $0.02084$ |
| $43^2$ | $[0.41592,0.45361]$ | $[0.43982,0.45327]$ | $0.01716$ |
| $1997$ | $[-0.09991,0.06908]$ | $[-0.02020,-0.01716]$ | $0.01908$ |

The intervals concern the sampled means. For the prime rows shown, the sampling error exceeds the numerical uncertainty from the mesh. The five plus-subfield controls give $D=-1/2$, and the norm-one control at $5^2$ gives $D=1/2$, to numerical precision. The leading sparse contribution still requires an asymptotic argument for typical prime-field shifts, and even direct control of this contribution leaves the $k\ge3$ terms of the rank expansion.
