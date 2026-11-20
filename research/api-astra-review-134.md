# Review of the round-134 gateway drafts

The two [gateway receipts](api-astra-134-receipt.json) were collected from the existing launches. No round-134 call was repeated.

The [real draft](api-astra-overflow-134.txt) correctly applies odd trace cancellation to a fixed even polynomial in bounded negative fields. The seed bound is \(2\sqrt{p/n}=2\sqrt2+O(p^{-1})\). Fixed-window approximation of the actual ordinary activation and its large-value tail are distinct obligations. Even when absolute tails vanish, bounded-window parity may still fail. The positive auxiliary profile in the [window note](ordinary-seed-window-134.md) gives a direct check. A continuous clipped window and a signed tail retain that distinction.

The [cold draft](api-astra-cold-134.txt) correctly separates the linear seed block and its remaining terms. Its rank-one example has counting norm \((n-1)/\sqrt n\), rather than a counting contraction. The two-basis flatness control in the [pure seed note](cold-pure-seed-134.md) supplies a valid example on the actual seed direction, as an auxiliary operator only. The verified translated rate below \(1.048\) is for heights 600 and 601. At height 602 the existing bound below \(0.516074\) is in counting norm. A low-arity remainder test must include the linear term \((V_h-S)/(2\sqrt{t_i})\), in addition to the higher odd terms.

The new outward replay collects every retained pure seed power at each Laurent exponent before taking absolute values. Including the infinite tail and both marked corrections gives a stronger eventual step bound \(0.528\) and two-step bound \(0.279\) on the original closed square. The nonlinear remainder and the invariant-ball margin remain open.

The new [closeout hook](../coordination/shared-obligations/round-134-after.json) checked the old batch's bound snapshot and launch chronology. The two routes had different objects, floors and estimates. There was no shared candidate to merge.
