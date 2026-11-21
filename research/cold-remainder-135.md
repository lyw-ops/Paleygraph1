# The first two unsigned remainder orders and a certified tail

Use the actual predictors \(V_h\), \(h=601,602\), the Jacobi seed \(S\), the full pure-seed derivative \(D^{\mathrm J}\), and the translated physical price \(P_{5000}\) of [Round 134](cold-pure-seed-134.md). Write \(C_h=V_h-S\) and \(E_h=D_h-D^{\mathrm J}\). The goal of the shared cold candidate is to establish the actual step price \(\|K E_h\|_{P_{5000}}<0.472\) with a uniform strict gap for these two rows on the original square.

## A specific unsigned comparison already exceeds the budget

At the real center \(a=2031/128\), use the **positive envelope of the actual height-601 predictor** from [Round 130](cold-combined-height-130.md). Let \(\sigma\) be the seed's symmetric weight envelope and \(\beta\) the positive envelope for \(C_{601}\), consisting of the other eight-center weights and the retained residual and zero mass of the replay. Charge the linear and cubic orders separately by their absolute binomial coefficients. Since the pure seed has been removed, the comparison for those two orders is
\[
 \frac{\beta}{\sqrt{4a}}+
 \frac{(\sigma+\beta)^{*3}-\sigma^{*3}}{2(4a)^{3/2}} .
\]
The cubic difference expands into nonnegative terms with at least one factor \(\beta\). Other orders, omitted weights and repairs only increase this comparison. Its base-column charge in the affine limit is mass plus \(\pi\)-moment divided by the final slope of \(\pi\). The [outward replay](cold-remainder-135-check.py) gives a strict lower bound \(0.6404\) for this limit from those two retained orders alone. Thus this construction cannot certify \(0.472\) in the fixed physical price, whatever unsigned tail is added. It is a lower bound on a **specified comparison**. It gives no signed lower bound on \(K E_{601}\).

The exact linearization in \(C_h\) is \(d_t'(S)C_h\) with \(d_t'(S)=4t/(4t+S^2)^{3/2}\). Across different orders of the rank-one seed, a fixed Laurent exponent times the same actual nonseed field can be collected before absolute value. Coincidence of numerical boundary weights alone does not identify two Mellin objects and does not justify such cancellation.

## A quantitative tail and counting comparison for the actual remainder

Set \(A=4\inf_Q\Re t\), \(m=4.8\), and \(\rho=m^2/A\). The first absolute weight moment per unit mass of the product of \(k\) negative factors is at most \(k\), by the [weight addition rule](cold-actual-first-insertion-126.md#uniform-word-cost-and-the-two-translated-columns). Because a single atom of weight \(w\) costs at most \(2(1+|w|)\) per unit translated price, the geometric translated cost of an unpriced order \(k=2\ell+1\) is at most \(4(\ell+1)\sqrt{\rho}\rho^\ell\). This upper applies to \(E_h\) after subtracting all pure seed words. The nonnegative mixed binomial masses are bounded by the full dimension budget of the actual \(V_h\). Summing the displayed bound from \(\ell=14\) gives
\[
 4\sqrt{\rho}\,\rho^{14}\left(\frac{15}{1-\rho}+
                         \frac{\rho}{(1-\rho)^2}\right)<0.0000407.
\]
The uniform bad lifts and actual marked corrections still cost \(O_{5000}(n^{-1/2})\) relative to the input price. The tails' scalar dimension sums converge for these corrections as well. This is an explicit price available for the omitted analytic orders once an actual signed retained expansion is supplied.

Separately the seed-centered disks from [Round 133](cold-seed-packet-133.md) give \(|C_h|<1.971573\). At \(z\) on the segment from \(S_i\) to \(V_{h,i}\),
\[
 |d_{t_i}'(z)|\le
 \frac{4|t_i|}{(4\Re t_i-(1.971573)^2)^{3/2}}.
\]
On the bulk the right side is below \(0.139\) across the entire square. At the mark it is still smaller eventually because \(t_0=n\). Thus \(\|K E_h\|_{2\to2}<0.275\). The Jacobi seed is real and bounded by \(2.828428\), so \(\|KD^{\mathrm J}\|_{2\to2}<0.335\) from the real-part radicand bound. With \(\|KD_{601}\|_{2\to2}<0.5145\), the exact splitting of the two-step remainder into \(K E_{602}K D_{601}+K D^{\mathrm J}K E_{601}\) gives counting rate below \(0.234\). These counting bounds do not price a physical packet.

The saved [comparison records](cold-remainder-135-checks.jsonl) use outward Arb for the inherited positive envelope and exact rational checks for the counting and tail bounds. The remaining test is a signed physical comparison. A direct aggregation of the terms linear in the actual nonseed row against the analytic seed is a narrower next calculation than repeating an unsigned cubic charge.
