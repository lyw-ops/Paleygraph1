#!/usr/bin/env python3
"""Capture launch evidence and summarize prospective shared-obligation reviews."""

import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
from tempfile import NamedTemporaryFile

from round_review import ROOT, inside, read_object, reference, shared_candidates


RECORDS = ROOT / 'coordination' / 'shared-obligations'
CLASSIFICATIONS = {'recognized', 'missed', 'unknown'}
EFFECTS = {'change', 'same', 'unknown'}


def utc(value):
    timestamp = datetime.fromisoformat(value)
    if timestamp.utcoffset() != timedelta(0):
        raise ValueError('capture and launch times must be UTC')
    return timestamp


def nonempty(data, field):
    value = data[field]
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{field} must be nonempty text')
    return value


def batch_paths(batch):
    if not re.fullmatch(r'round-[1-9]\d*(?:-b[1-9]\d*)?', batch):
        raise ValueError('use a batch name such as round-134 or round-134-b2')
    return (RECORDS / f'{batch}-before.json', RECORDS / f'{batch}-after.json',
            ROOT / 'coordination' / f'{batch}-inflight.json')


def save_once(path, record, ignore_on_retry=()):
    with NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent) as stream:
        stream.write(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        stream.flush()
        try:
            os.link(stream.name, path)
        except FileExistsError:
            existing = read_object(path)
            expected = {**record, **{key: existing.get(key) for key in ignore_on_retry}}
            if existing != expected:
                raise ValueError(f'{path.name} already exists with different contents') from None
    return reference(path)


def capture(batch, coordinator_path, call_ids, assessment):
    before, _, dispatch = batch_paths(batch)
    coordinator = inside(coordinator_path)
    content = coordinator.read_bytes()
    plan = json.loads(content)
    dispatch_round = int(batch.split('-')[1])
    if (not isinstance(plan, dict) or plan.get('round') != dispatch_round - 1 or plan.get('record_status') != 'ready'
            or plan.get('decision') != 'continue'):
        raise ValueError('capture needs the ready coordinator plan for the previous round')
    calls = {call['id']: call for call in plan['next_calls']}
    changes = {change['id']: change for change in plan['changes']}
    if len(set(call_ids)) != len(call_ids) or set(call_ids) - calls.keys():
        raise ValueError('call IDs must be unique and named in the coordinator plan')
    routes = dict(assessment.get('active_routes', {}) if assessment is not None else {})
    for identifier in call_ids:
        call = calls[identifier]
        route = f'r{dispatch_round}/{identifier}'
        if route in routes:
            raise ValueError(f'{route} appears twice in the snapshot')
        routes[route] = {'question': call['question'], 'scope': call['scope'],
                         'remaining': changes[call['change_id']]['remaining']}
    if dispatch.exists() and not before.exists():
        raise ValueError('dispatch manifest already exists; the batch cannot get a new before snapshot')
    declared = shared_candidates(plan)
    candidate_ids = {identifier: [item['id'] for item in declared if identifier in item['calls']]
                     for identifier in call_ids}
    known_shared = [
        {'id': item['id'], 'statement': item['statement'],
         'routes': [f'r{dispatch_round}/{identifier}' for identifier in call_ids if identifier in item['calls']]}
        for item in declared if len(set(call_ids) & set(item['calls'])) >= 2
    ]
    by_id = {item['id']: item for item in known_shared}
    for item in assessment.get('known_shared', []) if assessment is not None else []:
        existing = by_id.get(item['id'])
        if existing is None:
            by_id[item['id']] = item
            known_shared.append(item)
        elif (set(existing['routes']) != set(item['routes'])
              or item.get('statement', existing.get('statement')) != existing.get('statement')):
            raise ValueError(f'{item["id"]} differs from its recorded routes or statement')
    comparison = (nonempty(assessment, 'comparison') if assessment is not None
                  else 'Route questions and scope captured automatically. The dependency comparison is unassessed.')
    record = {
        'captured_at_utc': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'prepared_by': nonempty(assessment, 'prepared_by') if assessment is not None else 'Automatic dispatch capture',
        'coordinator': f'{coordinator_path}#next_calls',
        'coordinator_sha256': hashlib.sha256(content).hexdigest(),
        'call_ids': call_ids,
        'routes': routes,
        'candidate_ids_by_call': candidate_ids,
        'known_shared': known_shared,
        'comparison_status': 'assessed' if assessment is not None else 'unassessed',
        'comparison': comparison,
    }
    return save_once(before, record, ignore_on_retry=('captured_at_utc',))


def validate_groups(groups, has_comparison, seen, known_shared=()):
    if not isinstance(groups, list):
        raise ValueError('groups must be a list')
    for group in groups:
        identifier = nonempty(group, 'id')
        if not re.fullmatch(r'cand:[a-z0-9][a-z0-9-]*', identifier):
            raise ValueError(f'invalid candidate ID {identifier}')
        if identifier in seen:
            raise ValueError(f'{identifier} is already counted in another group')
        routes = group['routes']
        if not isinstance(routes, list) or len(routes) < 2 or any(
            not isinstance(route, str) or not route.strip() for route in routes
        ) or len(set(routes)) != len(routes):
            raise ValueError(f'{identifier} needs at least two distinct route IDs')
        status = group['classification']
        if status not in CLASSIFICATIONS or group['dispatch_effect'] not in EFFECTS:
            raise ValueError(f'{identifier} has an invalid classification or dispatch effect')
        declared = any(item['id'] == identifier and set(routes) <= set(item['routes']) for item in known_shared)
        if status == 'missed' and declared:
            raise ValueError(f'{identifier} was already shared at dispatch')
        if status != 'unknown' and not has_comparison and not (status == 'recognized' and declared):
            raise ValueError(f'{identifier} has no attributable pre-dispatch comparison')
        for field in ('math_evidence', 'prior_evidence', 'effect_reason'):
            nonempty(group, field)
        seen.add(identifier)


def closeout(batch, assessment):
    before, after, dispatch_path = batch_paths(batch)
    nonempty(assessment, 'reviewed_by')
    nonempty(assessment, 'comparison')
    dispatch = read_object(dispatch_path)
    lanes = dispatch.get('lanes') or [dispatch]
    launched = [lane for lane in lanes if lane.get('started_utc_epoch') is not None]
    if not launched:
        raise ValueError('dispatch manifest has no recorded launches')
    ids = [nonempty(lane, 'call_id') for lane in launched]
    launch_time = datetime.fromtimestamp(min(lane['started_utc_epoch'] for lane in launched), timezone.utc)
    before_hash = None
    has_comparison = False
    known_shared = []
    bound = dispatch.get('shared_obligations_before')
    if bound is not None:
        if reference(before) != bound:
            raise ValueError('dispatch manifest and before snapshot differ')
        snapshot = read_object(before)
        if utc(snapshot['captured_at_utc']) >= launch_time:
            raise ValueError('pre-dispatch snapshot must precede the first launch')
        if 'call_ids' in snapshot and set(ids) - set(snapshot['call_ids']):
            raise ValueError('dispatch includes calls outside the snapshot')
        if snapshot['coordinator_sha256'] != dispatch['coordinator']['sha256']:
            raise ValueError('the snapshot and dispatch cite different coordinator bytes')
        before_hash = bound['sha256']
        has_comparison = snapshot.get('comparison_status') != 'unassessed'
        known_shared = snapshot.get('known_shared', [])
    validate_groups(assessment['groups'], has_comparison, set(), known_shared)
    if before_hash is not None and 'candidate_ids_by_call' in snapshot:
        for group in assessment['groups']:
            if group['classification'] == 'recognized' and not any(
                group['id'] == item['id'] and set(group['routes']) <= set(item['routes']) for item in known_shared
            ):
                raise ValueError(f'{group["id"]}: recognized groups must reuse their pre-dispatch candidate ID')
    record = {**assessment, 'dispatch': dispatch_path.relative_to(ROOT).as_posix(),
              'launched_at_utc': launch_time.isoformat().replace('+00:00', 'Z'),
              'launched_calls': ids, 'before_sha256': before_hash}
    return save_once(after, record)


def summarize(directory):
    counts = Counter()
    seen = set()
    after_files = sorted(directory.glob('round-*-after.json'))
    before_only = set(directory.glob('round-*-before.json'))
    for path in after_files:
        before_path = path.with_name(path.name.removesuffix('-after.json') + '-before.json')
        before_only.discard(before_path)
        try:
            data = json.loads(path.read_bytes())
            nonempty(data, 'reviewed_by')
            nonempty(data, 'dispatch')
            launched = utc(data['launched_at_utc'])
            before_hash = data['before_sha256']
            has_comparison = False
            known_shared = []
            if before_hash is not None:
                content = before_path.read_bytes()
                if hashlib.sha256(content).hexdigest() != before_hash:
                    raise ValueError('pre-dispatch snapshot hash mismatch')
                before = json.loads(content)
                if utc(before['captured_at_utc']) >= launched:
                    raise ValueError('pre-dispatch snapshot must precede the first launch')
                has_comparison = before.get('comparison_status') != 'unassessed'
                known_shared = before.get('known_shared', [])
            validate_groups(data['groups'], has_comparison, seen, known_shared)
            for group in data['groups']:
                status = group['classification']
                counts[status] += 1
                if status == 'missed':
                    counts[f'missed_dispatch_{group["dispatch_effect"]}'] += 1
        except (KeyError, OSError, TypeError, ValueError) as error:
            raise ValueError(f'{path.name}: {error}') from error
    return len(after_files), len(before_only), counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command')
    before = commands.add_parser('capture', help='save a snapshot immediately before launch')
    before.add_argument('--batch', required=True)
    before.add_argument('--coordinator', required=True)
    before.add_argument('--call', required=True, action='append')
    before.add_argument('--assessment', type=Path, help='optional dependency comparison JSON')
    after = commands.add_parser('closeout', help='bind a review to the actual dispatch manifest')
    after.add_argument('--batch', required=True)
    after.add_argument('--assessment', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'capture':
            assessment = read_object(args.assessment) if args.assessment else None
            print(json.dumps(capture(args.batch, args.coordinator, args.call, assessment)))
            return
        if args.command == 'closeout':
            print(json.dumps(closeout(args.batch, read_object(args.assessment))))
            return
        batches, pending, counts = summarize(RECORDS)
    except (KeyError, OSError, TypeError, ValueError) as error:
        raise SystemExit(f'Error: {error}') from error
    known = counts['missed'] + counts['recognized']
    rate = f"{counts['missed']}/{known} ({counts['missed'] / known:.1%})" if known else 'unavailable (0 classifiable groups)'
    print(f'Reviewed batches: {batches}; snapshots without closeout: {pending}')
    print(f"Recognized: {counts['recognized']}; missed: {counts['missed']}; unknown: {counts['unknown']}")
    print(f'Missed overlap rate: {rate}')
    print(f"Confirmed misses that would change dispatch: {counts['missed_dispatch_change']}; "
          f"uncertain dispatch effect: {counts['missed_dispatch_unknown']}")


if __name__ == '__main__':
    main()
