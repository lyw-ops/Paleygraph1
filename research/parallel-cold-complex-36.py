"""Exact stationary phase identities and Arb square-obstruction constants.

Only stdout is written. Nonreal samples check stationary algebra, not
physical branch tracking. The uniform theorem is proved in the companion
note; the inherited hot estimate is an explicit mathematical dependency.
"""

from dataclasses import dataclass
from fractions import Fraction as F
import json

from flint import arb, ctx


def emit(**row):
    print(json.dumps(row, sort_keys=True), flush=True)


@dataclass(frozen=True)
class G:
    """A Gaussian rational, with no floating-point operations."""

    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def cast(value):
        return value if isinstance(value, G) else G(value)

    def __add__(self, other):
        other = G.cast(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G.cast(other))

    def __rsub__(self, other):
        return G.cast(other) - self

    def __mul__(self, other):
        other = G.cast(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re**2 + self.im**2

    def __truediv__(self, other):
        other = G.cast(other)
        numerator = self * other.conj()
        denominator = other.abs2()
        return G(numerator.re / denominator, numerator.im / denominator)

    def __rtruediv__(self, other):
        return G.cast(other) / self

    def record(self):
        return {"re": str(self.re), "im": str(self.im)}


def dot(xs, ys):
    return sum((x * y for x, y in zip(xs, ys)), G())


def mv(matrix, vector):
    return [dot(row, vector) for row in matrix]


def stationary_samples():
    n, N = 6, 5
    b = [F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2)]
    kernel = [F(x, 6) for x in [-1, 3, -1, -3, -1, 3]]
    plus = [[(F(i == j) - F(1, n) + kernel[(i-j) % n])/2
             for j in range(n)] for i in range(n)]
    minus = [[(F(i == j) - F(1, n) - kernel[(i-j) % n])/2
              for j in range(n)] for i in range(n)]
    samples = [G(0), G(F(1, 2)), G(F(1, 2), F(1, 10)),
               G(F(1, 2), F(-1, 10)), G(F(-1, 4), F(1, 5))]
    for x in samples:
        u = [1 + x * bi for bi in b]
        assert all(ui.abs2() > 0 for ui in u)
        bulk_derivative = sum((bi/ui for bi, ui in zip(b[1:], u[1:])), G())
        tau = -n / (u[0] * bulk_derivative)
        assert tau.re > 0
        c, W = tau/n, 1 + N*tau/n
        w = [G(1)] + [c]*N
        reciprocal = [wi/ui for wi, ui in zip(w, u)]
        opposite = [n * ri/W for ri in reciprocal]
        assert dot(b, reciprocal) == G()
        assert sum(u, G()) == G(n)
        assert sum(opposite, G()) == G(n)
        assert mv(plus, [ui-1 for ui in u]) == [ui-1 for ui in u]
        assert mv(minus, [vi-1 for vi in opposite]) == [vi-1 for vi in opposite]
        assert all(W/n*ui*vi == wi for ui, vi, wi in zip(u, opposite, w))
        ratios = [ui.conj()/ui for ui in u]
        assert all(ri.abs2() == 1 for ri in ratios)
        assert sum(reciprocal, G()) == W
        assert dot(w, ratios) == W
        assert dot([ui.conj() for ui in u], opposite) == G(n)
        slack = N*N*c.abs2() - (W-ratios[0]).abs2()
        sum_bulk = sum(ratios[1:], G())
        assert slack == c.abs2()*(N*N-sum_bulk.abs2())
        phase_margin = (W*ratios[0].conj()).re-W.re
        assert slack == 2*phase_margin and slack >= 0
        real_physical = x.im == 0
        if real_physical:
            assert all(ui.im == 0 and ui.re > 0 for ui in u+opposite)
        emit(kind="exact_actual_p13_stationary_phase_identity",
             x=x.record(), tau=tau.record(), W=W.record(),
             both_sector_constraints=True, both_normalized_means_one=True,
             actual_exceptional_product_weights=True,
             conjugate_stationarity_identity=True,
             squared_phase_disk_slack=str(slack),
             phase_cone_margin=str(phase_margin),
             positive_real_physical_stationary_point=real_physical,
             nonreal_sample_scope="algebraic identity only; no branch tracking")


def square_constants():
    ctx.prec = 192
    T = F(2048)
    Rbig, R, r, r0 = T-F(1, 16), T-F(1, 8), T-F(1, 4), F(1024)
    assert (Rbig+R)/(Rbig-R) == 65533
    assert R/r == F(16383, 16382)
    assert R/r0 == F(16383, 8192)
    assert T-Rbig == F(1, 16) and T-r == F(1, 4)
    omega = (arb(16383)/16382).log()/(arb(16383)/8192).log()
    outer = 4/arb(3072).sqrt()+arb(65533).log()/2
    assert omega > arb(8807)/100000000
    assert outer < arb(5618)/1000 and outer < 7
    logupper = omega*(arb(4).log()-50000)+(1-omega)*arb(7).log()
    loglower = -arb(8).log()
    assert logupper < -arb(24576)/10000
    assert loglower > -arb(20795)/10000
    assert logupper < loglower
    threshold = arb(16).log()-arb(49).log()+2*arb(56).log()/omega
    assert threshold < 100000
    emit(kind="validated_square_nonextension_constants", arb_precision=ctx.prec,
         disk_center=str(T), disk_radius=str(Rbig), outer_radius=str(R),
         cold_radius=str(r), hot_radius=str(r0), omega_interval=str(omega),
         outer_modulus_bound_interval=str(outer), outer_rational_bound="7",
         log_three_circle_upper_at_log_n_100000=str(logupper),
         log_cold_lower_bound=str(loglower), exact_threshold_log_interval=str(threshold),
         explicit_sufficient_condition="n > exp(100000)",
         inherited_input="actual uniform hot theorem and exact square theta value")

    # At h=11, using W < 5/4, the square real lower ratio exceeds 4/3.
    ratio_lower = F(2)*(11-1)/(11+1)/F(5, 4)
    assert ratio_lower == F(4, 3)
    margin = (arb(4)/3).log()/2-arb(1)/8
    assert margin > 0
    emit(kind="exact_and_validated_square_cold_lower_bound", cold_floor="1/4",
         square_root_minimum=11, strict_ratio_lower_bound="4/3",
         strict_marked_log_lower_bound="1/8", positive_margin_interval=str(margin),
         square_theta_plus="h-1", square_theta_minus="(h+1)/2")


if __name__ == "__main__":
    stationary_samples()
    square_constants()
    emit(kind="all_checks_passed", substantive_records=7,
         prime_common_cold_domain_proved=False,
         growth_automatic_given_common_marked_domain=True,
         explicit_large_square_physical_branchpoint_existence=True,
         finite_sample_scope="normalization checks, not an asymptotic numerical proof")
