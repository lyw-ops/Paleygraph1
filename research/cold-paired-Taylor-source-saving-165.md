# The actual even-word Taylor source with paired Jacobi savings

Keep the original cold square, both lifts, \(t_0=n=(p-1)/2\), and actual increment \(R=V_{601}-V_{600}\). Put \(V=V_{600}\), \(V_s=V+sR\), \(\varepsilon=0.011\), \(M=4.811\), \(N=4(2031/128-2^{-17})\), \(x=M^2/N<1\). Use the genuine representation bounds of [Round 126](cold-actual-first-insertion-126.md). The even Taylor remainder on the bulk is the actual analytic expansion
\[
 r^{\mathrm b}=\sum_{l\ge0}(-1)^l b_l(4t)^{-l-1/2}
                   R^2\int_0^1(1-s)V_s^{2l}\,ds,
 \qquad b_l=(2l+1)\binom{2l}{l}/4^l.
\]

In each word pair the \(2l\) factors from \(V_s\), retaining the two actual \(R\) factors. The same Jacobi seed \(2\sqrt n\,Ke_0\) occurs in every \(V_s\) representation, with squared dimension mass \(s_n^2\ge8\). Its independently expanded lift weights have first absolute moment one and their paired mean absolute sum is one. This is the actual pair saving of [Round 128](cold-actual-quadratic-128.md#first-moment-price-of-the-actual-derivative-difference). The argument uses convolution weight addition and also applies to the even word: punctual terms have zero weight and are killed by the following \(K\). Summing the paired first moments bounds its generic rank by
\[
 \varepsilon^2\big((2l+2)M^{2l}-8l M^{2l-2}\big),
]
where at \(l=0\) the second term is zero. To check monotonicity of the substituted dimension budgets, each paired contribution has form \(2d_1d_2-s_n^2\) with \(d_i\ge s_n\). It is nonnegative and increases in both inputs. The products of dimensions of the other words also increase. This uses a saving in a positive first-moment comparison with a designated actual sign-paired seed.

The post-\(K\) base price is at most twice the generic rank, while integrating \(1-s\) costs one half. The bad base-character and true-mark repairs contribute \(O(n^{-1/2}\varepsilon^2)\) in the same price, by the convergent uncompensated bounds of [Round 162](cold-height-602-frozen-kernel-162.md). Since \(\sum b_l x^l=(1-x)^{-3/2}\) and \(sum l b_l x^l=(3/2)x(1-x)^{-5/2}\), summing gives
\[
 \|Kr\|_{P_{5000}}
 \le \frac{\varepsilon^2}{\sqrt N}(2+x-12/N)(1-x)^{-5/2}
       +O(n^{-1/2})<0.000103
]
eventually on the original square. For the single \(l=1\) term the same argument gives eventual price below \(0.000031\), by comparing \((3/2)\varepsilon^2(4M^2-8)N^{-3/2}\) to that constant. Both comparisons use exact rational squaring. This improves the full source price \(0.000115\) before the outer frozen inverse. It does not give a translated bound after that inverse or a growing-depth continuation.
