"""Optimize the endpoint ratio of a translated Fourier repair."""

import argparse
import csv
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy
import sys

import numpy as np

RESEARCH = Path(__file__).resolve().parent
sys.path.insert(0, str(RESEARCH.parent))
from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign


def sort_finish(residue, reverse_kernel, mean, mark, height):
    """Evaluate the ratio at every breakpoint using prefix sums."""
    n = len(residue)
    order = np.argsort(-residue, kind="stable")
    levels = residue[order]
    weights = reverse_kernel[order]
    counts = np.arange(n)
    mass = np.r_[0.0, np.cumsum(levels[:-1])] - counts * levels
    height_gain = np.r_[0.0, np.cumsum(weights[:-1] * levels[:-1])]
    height_gain -= np.r_[0.0, np.cumsum(weights[:-1])] * levels
    means = mean + levels + mass / height
    marks = mark + levels + height_gain
    ratios = np.full(n, -np.inf)
    np.divide(marks, sqrt(n) * means, where=means > 0, out=ratios)
    return float(levels[np.argmax(ratios)])


def finish(raw, affine, floor, kernel, threshold, trim=False):
    n = len(raw)
    residual = floor - affine
    weights = np.maximum(residual - threshold, 0)
    translates = np.fft.irfft(np.fft.rfft(kernel) * np.fft.rfft(weights), n)
    correction = affine + threshold + translates
    row = raw + correction
    ratio = row[0] / (sqrt(n) * row.mean())
    reverse_kernel = np.r_[kernel[0], kernel[:0:-1]]
    height = 1 / kernel.mean()
    root_trim = 0.0
    if trim and ratio >= height / sqrt(n):
        root_trim = min(float(weights[0]), max(0.0, float(correction[0] - floor[0])))
        weights[0] -= root_trim
        correction -= root_trim * kernel
        row = raw + correction
        ratio = row[0] / (sqrt(n) * row.mean())
    weighted_cost = (height - 1) * threshold + (1 - reverse_kernel) @ weights
    identity = raw[0] + affine[0] - height * (raw.mean() + affine.mean()) - weighted_cost
    if abs(identity - (row[0] - height * row.mean())) > 5e-9 * max(1, abs(row[0])):
        raise RuntimeError("weighted repair identity failed")
    if np.min(correction - floor) < -5e-9:
        raise RuntimeError("translated finish failed its pointwise repair")
    return correction, row, float(ratio), root_trim


def normalize_kernel(row):
    recentered = np.roll(row, -int(np.argmax(row)))
    even = (recentered + np.r_[recentered[0], recentered[:0:-1]]) / 2
    even -= min(0, float(even.min()))
    return even / even[0]


def candidates(sign, side, raw, floor, depth, rounds, repair_tools):
    n = len(sign)
    project, kappa, omega, (_, translate), _ = repair_tools["sector_tools"](sign, side)
    affine = np.full(n, .75 * (1 - raw.mean()))
    alpha = min(2, 1 / (kappa + omega))
    for _ in range(depth):
        affine += alpha * project(np.maximum(floor - affine, 0))
    impulse = np.zeros(n)
    impulse[0] = 1
    kernel = normalize_kernel(translate(impulse))
    residue = floor - affine
    height = 1 / kernel.mean()
    baseline_threshold = repair_tools["cap"](residue, height)[1]
    correction, best_row, baseline, root_trim = finish(raw, affine, floor, kernel, baseline_threshold)
    yield 'mass', 0, baseline_threshold, height / sqrt(n), correction, best_row, baseline, residue, root_trim
    best_ratio = baseline
    for iteration in range(1, rounds + 1):
        height = 1 / kernel.mean()
        reverse_kernel = np.r_[kernel[0], kernel[:0:-1]]
        threshold = sort_finish(residue, reverse_kernel, raw.mean() + affine.mean(),
                                raw[0] + affine[0], height)
        correction, row, ratio, root_trim = finish(raw, affine, floor, kernel, threshold, trim=True)
        if iteration == 1 and ratio < baseline - 1e-8:
            raise RuntimeError("ratio finish fell below the candidate threshold")
        yield 'ratio', iteration, threshold, height / sqrt(n), correction, row, ratio, residue, root_trim
        if ratio > best_ratio:
            best_ratio = ratio
            best_row = row
        kernel = normalize_kernel(best_row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes', nargs='*', type=int, default=[401, 9413, 37253, 153649])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[19, 97, 193, 389])
    parser.add_argument('--rounds', type=int, default=3)
    parser.add_argument('--depth', type=int, default=4)
    parser.add_argument('--certify-max-order', type=int, default=0)
    args = parser.parse_args()
    if args.rounds < 1 or args.depth < 0:
        parser.error('require a positive number of finishes and a nonnegative projection depth')
    cases = [(p, p, None, paley_sign) for p in args.primes]
    cases += [(h*h, h, h, square_field_sign) for h in args.square_roots]
    repair_tools = runpy.run_path(str(RESEARCH / 'parallel-repair-17.py'))
    cert_tools = runpy.run_path(str(RESEARCH / 'parallel-defect-16.py')) if args.certify_max_order else None
    writer = None
    for order, characteristic, root, maker in sorted(cases):
        if args.certify_max_order and order > args.certify_max_order:
            continue
        sign = maker(characteristic)
        n = len(sign)
        widths = sorted({1/16, order**(-1/4)}, reverse=True)
        for width, _, plus, minus, residual in damped_trials(sign, widths, 1e-11, 48):
            certify = args.certify_max_order >= order
            balls = cert_tools['reference_balls'](sign, width, plus, minus) if certify else None
            for side, y in ((1, minus), (-1, plus)):
                raw = sqrt(n) * np.fft.ifft((sign != side)*np.fft.fft(y)).real
                for signed in (False, True):
                    floor = -raw.copy() if signed else np.maximum(-raw, 0)
                    floor[0] = 0
                    rows = list(candidates(sign, side, raw, floor, args.depth, args.rounds, repair_tools))
                    best = max(rows, key=lambda trial: trial[6])
                    for trial in rows:
                        method, iteration, threshold, previous_ratio, correction, _, ratio, residue, root_trim = trial
                        record = dict(order=order, square_root=root, side=side, width=width,
                                      signed=signed, method=method, iteration=iteration, threshold=threshold,
                                      kernel_ratio=previous_ratio, correction_mass=float(correction.mean()),
                                      endpoint_ratio=ratio, root_residual=float(residue[0]),
                                      root_trim=root_trim,
                                      bulk_peak_residual=float(residue[1:].max()), reference_residual=residual)
                        if certify and (method == 'mass' or trial is best):
                            enclosure = cert_tools['certify'](sign, side, balls, correction, signed, root)
                            print(json.dumps(record | dict(width_exact=str(Fraction(width))) | enclosure), flush=True)
                        if not args.certify_max_order:
                            if writer is None:
                                writer = csv.DictWriter(sys.stdout, record.keys(), lineterminator='\n')
                                writer.writeheader()
                            writer.writerow(record)
                            sys.stdout.flush()


if __name__ == '__main__':
    main()
