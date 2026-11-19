#!/usr/bin/env python3
"""Summarize acceptance records and maintain the research navigation page."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'research' / 'README.md'


@dataclass
class Record:
    path: Path
    data: dict
    round_number: int | None
    inferred_round: bool


def records() -> list[Record]:
    result = []
    for path in sorted((ROOT / 'research').glob('*acceptance*.json')):
        data = json.loads(path.read_text())
        if not isinstance(data, dict):
            raise ValueError(f'{path.name}: expected a JSON object')
        number = data.get('round')
        inferred = number is None
        if inferred:
            match = re.search(r'-(\d+)-acceptance', path.name)
            number = int(match[1]) if match else None
        elif isinstance(number, bool) or not str(number).isdigit():
            raise ValueError(f'{path.name}: invalid round number {number!r}')
        else:
            number = int(number)
        result.append(Record(path, data, number, inferred))
    if not result:
        raise ValueError('No acceptance records found in research/')
    return result


def latest_record(items: list[Record]) -> Record:
    numbered = [item for item in items if item.round_number is not None]
    if not numbered:
        raise ValueError('No numbered acceptance records found')
    return max(numbered, key=lambda item: (
        item.round_number,
        item.path.name == f'round-{item.round_number}-acceptance.json',
        item.path.name,
    ))


def notes(record: Record) -> list[str]:
    return sorted(name for name in record.data.get('proof_and_code_sha256', {})
                  if name.endswith('.md'))


def link(name: str, label: str | None = None) -> str:
    target = Path(name)
    relative = target.relative_to('research').as_posix() if target.parts[0] == 'research' else '../' + name
    return f'[{label or target.name}]({quote(relative, safe="/.-_")})'


def render(items: list[Record], latest: Record) -> str:
    data = latest.data
    lines = [
        '# Research index', '',
        'Generated from the acceptance records present in this working tree. '
        'This index is navigation; the linked records retain their own scope, review history and limitations.', '',
        'Refresh with `python3 scripts/research_index.py --write` from the repository root; '
        'check freshness with `python3 scripts/research_index.py --check`. '
        'Run the script without options for a live summary.', '',
        '## Latest recorded acceptance', '',
        f'- Round: **{latest.round_number}** — {link(latest.path.relative_to(ROOT).as_posix())}.',
        f'- Target status reported by this record: `{data.get("target_status", "not specified")}`.',
        f'- Acceptance timestamp in the record: `{data.get("accepted_at_utc", "not specified")}`.',
        '- Read the [latest ledger entries](ledger.md) alongside the record and its route notes.',
        '- Files from later rounds may be in progress; their presence alone gives them no acceptance status.',
        '- The working tree can contain unpublished records. Use Git status to distinguish local work from a committed snapshot.', '',
    ]
    if notes(latest):
        lines += ['### Route notes named in this record', '']
        lines += [f'- {link(name)}' for name in notes(latest)]
        lines += ['']
    priorities = data.get('main_ranked_closeout', [])
    if priorities:
        lines += ['### Priorities recorded by the research session', '']
        lines += [f'{i}. {text}' for i, text in enumerate(priorities, 1)]
        lines += ['']
    lines += [
        '## Acceptance record archive', '',
        'Rows are ordered by round, not by filename. A record may cover one route or an entire round; '
        'multiple records in one round are listed separately. Earlier work without a separate acceptance '
        'record is introduced in the [background guide](../docs/RESEARCH.md) and the ledger.', '',
        '| Round | Acceptance record |',
        '| --- | --- |',
    ]
    ordered = sorted(items, key=lambda item: (item.round_number or -1, item.path.name), reverse=True)
    for item in ordered:
        number = str(item.round_number) if item.round_number is not None else 'Unspecified'
        if item.inferred_round and item.round_number is not None:
            number += '*'
        lines.append(f'| {number} | {link(item.path.relative_to(ROOT).as_posix())} |')
    lines += [
        '', '* Round inferred from the filename because the record has no `round` field.', '',
        '## Reading and replaying', '',
        '- [Repository overview](../README.md)',
        '- [Research background and early milestones](../docs/RESEARCH.md)',
        '- [Replay guide and historical command catalogue](../docs/REPLAY.md)',
        '- [Continuing the research and preparing a handoff](../docs/WORKFLOW.md)',
        '- [Round-36 handoff](../HANDOFF.md) and [round-36 coordinator prompt](../BRAIN_PROMPT.md): historical snapshots.', '',
        'Proof notes, exact or interval computations, and floating-point diagnostics carry different kinds '
        'of evidence. Indexing a record does not independently validate its mathematics or turn its evidence '
        'into a proof of the target.', '',
    ]
    return '\n'.join(lines)


def verify_latest(record: Record) -> int:
    entries = []
    for key, value in record.data.items():
        if key.endswith('_sha256') and isinstance(value, dict):
            entries.extend(value.items())
    if 'previous_sha256' in record.data:
        if not record.data.get('previous'):
            raise ValueError('previous_sha256 has no previous-record path')
        entries.append((record.data['previous'], record.data['previous_sha256']))
    if not entries:
        raise ValueError('Latest record has no supported explicit file-hash references')
    for name, expected in entries:
        if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-fA-F]{64}', expected):
            raise ValueError(f'{name}: invalid SHA-256 value')
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f'{name}: reference is outside the repository')
        digest = hashlib.sha256()
        with path.open('rb') as source:
            for block in iter(lambda: source.read(1024 * 1024), b''):
                digest.update(block)
        if digest.hexdigest() != expected.lower():
            raise ValueError(f'{name}: SHA-256 mismatch')
    return len(entries)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    output = parser.add_mutually_exclusive_group()
    output.add_argument('--write', action='store_true', help='refresh research/README.md')
    output.add_argument('--check', action='store_true', help='fail if the navigation page is stale')
    parser.add_argument('--verify-latest', action='store_true', help='check explicit file-hash maps and the previous-record hash of the latest acceptance')
    args = parser.parse_args()
    try:
        items = records()
        latest = latest_record(items)
        if args.verify_latest:
            count = verify_latest(latest)
            print(f'Verified {count} recorded file hashes for round {latest.round_number}; no proofs or replays checked.')
        expected = render(items, latest)
        if args.write:
            INDEX.write_text(expected)
            print(f'Wrote research/README.md from {len(items)} acceptance records, through round {latest.round_number}.')
        elif args.check:
            if not INDEX.exists() or INDEX.read_text() != expected:
                print('Research index is stale. Run: python3 scripts/research_index.py --write')
                return 1
            print(f'Research index is current: {len(items)} records, through round {latest.round_number}.')
        else:
            print(f'Latest acceptance record in this checkout: {latest.path.relative_to(ROOT)}')
            print(f'Target status reported by the record: {latest.data.get("target_status", "not specified")}')
            for i, text in enumerate(latest.data.get('main_ranked_closeout', []), 1):
                print(f'{i}. {text}')
        return 0
    except (OSError, ValueError, TypeError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    raise SystemExit(main())
