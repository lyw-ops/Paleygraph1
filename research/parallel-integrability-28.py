"""Evaluate the explicit uniformly integrable residual-pairing example."""

import json
from math import sqrt


def clipped_pairing(n, depth):
    cutoff = n**(-2/3)
    interval = 1/depth
    source_mean = 4-3*n**(-1/6)
    initial_integral = (
        sqrt(n)*interval if interval <= cutoff
        else 4*interval**.25-3*n**(-1/6)
    )
    return depth**.25*(initial_integral/source_mean-interval)


def main():
    for n in (64, 4096, 262144, 16777216):
        mean = 4-3*n**(-1/6)
        second = (3*n**(1/3)-2)/mean**2
        print(json.dumps(dict(
            kind="clipped_source", n=n, source_mean=1.,
            source_coordinate_cap=sqrt(n)/mean,
            source_second_moment=second,
            tail_bound="E[G 1_{G>R}] <= 4 R^(-1/3)",
        )))
        for depth in (4,16,64,256):
            print(json.dumps(dict(
                kind="pairing", n=n, depth=depth,
                test_l2=depth**(-.25)*sqrt(1-1/depth),
                test_supremum=depth**.25*(1-1/depth),
                source_test_pairing=clipped_pairing(n,depth),
                field_limit_pairing=1-depth**(-.75),
            )))


if __name__ == "__main__":
    main()
