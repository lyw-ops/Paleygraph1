#!/usr/bin/env python3
"""Record proof-plan changes and export justified research missions."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

import research_index

ROOT = Path(__file__).resolve().parents[1]
EFFECTS = {'removed', 'weakened', 'new_obstruction', 'reformulated', 'evidence_only', 'unchanged'}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(name: str) -> Path:
    if not isinstance(name, str) or not name or Path(name).is_absolute() or '..' in Path(name).parts:
        raise ValueError(f'Expected a repository-relative path: {name!r}')
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f'Reference is outside the repository: {name}')
    return path


def reference(path: Path) -> dict:
    return {'path': path.relative_to(ROOT).as_posix(), 'sha256': digest(path)}


def read_object(path: Path) -> dict:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f'{path}: expected a JSON object')
    return data


def selected_record(number: int | None = None) -> research_index.Record:
    items = research_index.records()
    if number is not None:
        items = [item for item in items if item.round_number == number]
    if not items:
        raise ValueError(f'No acceptance record for round {number}')
    return research_index.latest_record(items)


def review_path(number: int) -> Path:
    return ROOT / 'coordination' / f'round-{number}.json'


def require_text(value, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or re.match(r'^(TODO|TBD|<)', value.strip(), re.I):
        raise ValueError(f'{field}: a concrete assessment is required')
    return value


def checked_reference(value, field: str) -> Path:
    if not isinstance(value, dict):
        raise ValueError(f'{field}: expected a path and SHA-256')
    path = inside(value.get('path'))
    expected = value.get('sha256')
    if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
        raise ValueError(f'{field}: invalid SHA-256')
    if digest(path) != expected:
        raise ValueError(f'{field}: source changed: {value["path"]}')
    return path


def require_list(value, field: str, nonempty: bool = True) -> list:
    if not isinstance(value, list) or (nonempty and not value):
        raise ValueError(f'{field}: expected {"a nonempty" if nonempty else "a"} list')
    return value


def shared_candidates(data: dict) -> list[dict]:
    calls = {call['id'] for call in data['next_calls']}
    entries = require_list(data.get('shared_candidates', []), 'shared_candidates', nonempty=False)
    seen = set()
    for candidate in entries:
        if not isinstance(candidate, dict):
            raise ValueError('shared_candidates: expected candidate objects')
        identifier = require_text(candidate.get('id'), 'candidate.id')
        if not re.fullmatch(r'cand:[a-z0-9][a-z0-9-]*', identifier) or identifier in seen:
            raise ValueError(f'Invalid or duplicate shared candidate: {identifier}')
        seen.add(identifier)
        require_text(candidate.get('statement'), f'{identifier}.statement')
        references = require_list(candidate.get('calls'), f'{identifier}.calls')
        if (any(not isinstance(call, str) or call not in calls for call in references)
                or len(references) < 2 or len(set(references)) != len(references)):
            raise ValueError(f'{identifier}: name at least two different proposed calls')
    return entries


def validate(data: dict, number: int, current_required: bool = False) -> None:
    if data.get('schema_version') != 1 or type(data.get('round')) is not int or data['round'] != number:
        raise ValueError('Wrong schema version or round number')
    if data.get('record_status') != 'ready':
        raise ValueError('Coordinator record is a draft; complete the assessment before preparing a mission')
    require_text(data.get('prepared_by'), 'prepared_by')
    sources = data.get('sources')
    if not isinstance(sources, dict):
        raise ValueError('sources: expected baseline and current acceptance references')
    current_path = checked_reference(sources.get('current'), 'sources.current')
    baseline_path = checked_reference(sources.get('baseline'), 'sources.baseline')
    current = selected_record(number)
    if current_path != current.path.resolve():
        raise ValueError('sources.current does not name the selected acceptance record')
    baseline = read_object(baseline_path)
    baseline_round = baseline.get('round')
    if type(baseline_round) is not int or not 0 < baseline_round < number:
        raise ValueError('Baseline acceptance must name an earlier round')
    if not any(item.path.resolve() == baseline_path and item.round_number == baseline_round
               for item in research_index.records()):
        raise ValueError('Baseline is not an indexed acceptance record')
    if current.data.get('previous'):
        if inside(current.data['previous']) != baseline_path:
            raise ValueError('Baseline differs from the acceptance record previous pointer')
        if current.data.get('previous_sha256') and digest(baseline_path) != current.data['previous_sha256']:
            raise ValueError('Baseline differs from the acceptance record previous hash')
    if current_required and selected_record().round_number != number:
        raise ValueError('A newer acceptance exists; prepare a current coordinator record before dispatch')
    accepted_references = {}
    for source in sources.values():
        accepted_references.setdefault(source['path'], set()).add(source['sha256'])
    for acceptance in [current.data, baseline]:
        for key, values in acceptance.items():
            if key.endswith('_sha256') and isinstance(values, dict):
                for name, sha in values.items():
                    if isinstance(sha, str) and re.fullmatch(r'[0-9a-f]{64}', sha):
                        accepted_references.setdefault(name, set()).add(sha)

    def accepted_reference(evidence, field):
        checked_reference(evidence, field)
        if evidence['sha256'] not in accepted_references.get(evidence['path'], set()):
            raise ValueError(f'{field}: reference is not bound by either acceptance record')

    ids = set()
    for change in require_list(data.get('changes'), 'changes'):
        if not isinstance(change, dict):
            raise ValueError('changes: expected assessment objects')
        identifier = require_text(change.get('id'), 'change.id')
        if identifier in ids:
            raise ValueError(f'Duplicate change id: {identifier}')
        ids.add(identifier)
        if change.get('effect') not in EFFECTS:
            raise ValueError(f'{identifier}: unknown change effect')
        for key in ['route', 'before', 'after', 'remaining']:
            require_text(change.get(key), f'{identifier}.{key}')
        for evidence in require_list(change.get('evidence'), f'{identifier}.evidence'):
            accepted_reference(evidence, f'{identifier}.evidence')
    decision = data.get('decision')
    require_text(data.get('decision_reason'), 'decision_reason')
    calls = require_list(data.get('next_calls'), 'next_calls', nonempty=False)
    if decision not in {'continue', 'hold'} or (decision == 'continue' and not calls) or (decision == 'hold' and calls):
        raise ValueError('Continue needs proposed calls; hold needs an explanation and no calls')
    call_ids, priorities = set(), set()
    for call in calls:
        if not isinstance(call, dict):
            raise ValueError('next_calls: expected mission objects')
        identifier = require_text(call.get('id'), 'call.id')
        priority = call.get('priority')
        if identifier in call_ids or type(priority) is not int or priority < 1 or priority in priorities:
            raise ValueError('Mission ids and positive integer priorities must be unique')
        call_ids.add(identifier)
        priorities.add(priority)
        if call.get('change_id') not in ids:
            raise ValueError(f'{identifier}: unknown change_id')
        for key in ['question', 'why_now', 'scope', 'if_yes', 'if_no', 'if_inconclusive']:
            require_text(call.get(key), f'{identifier}.{key}')
        for evidence in require_list(call.get('inputs'), f'{identifier}.inputs'):
            accepted_reference(evidence, f'{identifier}.inputs')
    shared_candidates(data)


def initialize(number: int | None, baseline_name: str | None) -> Path:
    current = selected_record(number)
    if baseline_name:
        baseline_path = inside(baseline_name)
    elif current.data.get('previous'):
        baseline_path = inside(current.data['previous'])
    else:
        earlier = [item for item in research_index.records() if item.round_number and item.round_number < current.round_number]
        if not earlier:
            raise ValueError('Choose an earlier acceptance record with --baseline')
        baseline_path = research_index.latest_record(earlier).path
    suggestions = current.data.get('main_ranked_closeout', [])
    note_paths = research_index.notes(current)
    evidence = [reference(inside(name)) for name in note_paths]
    data = {
        'schema_version': 1,
        'round': current.round_number,
        'record_status': 'draft',
        'prepared_by': '',
        'sources': {'baseline': reference(baseline_path), 'current': reference(current.path)},
        'changes': [{'id': 'route-1', 'route': '', 'effect': 'unchanged', 'before': '', 'after': '',
                     'remaining': '', 'evidence': evidence}],
        'decision': 'continue',
        'decision_reason': '',
        'next_calls': [{'id': 'next-test', 'priority': 1, 'change_id': 'route-1',
                        'question': suggestions[0] if suggestions else '', 'why_now': '', 'scope': '',
                        'if_yes': '', 'if_no': '', 'if_inconclusive': '', 'inputs': evidence}],
    }
    output = review_path(current.round_number)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x') as stream:
        stream.write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    return output


def show(data: dict) -> str:
    lines = [f'# Round {data["round"]}: coordinator assessment', '',
             f'Record status: {data.get("record_status", "draft")}. This is not mathematical certification.', '']
    for change in data.get('changes', []):
        lines += [f'## {change["id"]}: {change["effect"]}',
                  f'- Before: {change.get("before", "")}', f'- After: {change.get("after", "")}',
                  f'- Remaining: {change.get("remaining", "")}', '']
    lines += [f'Decision: {data.get("decision", "")}. {data.get("decision_reason", "")}', '']
    for call in sorted(data.get('next_calls', []), key=lambda item: item['priority']):
        lines += [f'## Proposed call {call["priority"]}: {call["id"]}', call.get('question', ''),
                  'Why now: ' + call.get('why_now', ''), '']
    return '\n'.join(lines)


def mission(data: dict, identifier: str, path: Path, record_sha256: str) -> str:
    matches = [call for call in data['next_calls'] if call['id'] == identifier]
    if not matches:
        raise ValueError(f'No proposed call named {identifier}')
    call = matches[0]
    change = next(item for item in data['changes'] if item['id'] == call['change_id'])
    lines = [f'# Proposed research mission: {identifier}', '',
             f'Coordinator record: {path.relative_to(ROOT)}', f'Record SHA-256: {record_sha256}',
             'This exports a proposal; it does not launch an agent or record a past dispatch.', '',
             '## Question', call['question'], '', '## Why this call is worth making', call['why_now'], '',
             '## Current proof obligation', change['remaining'], '', '## Scope', call['scope'], '',
             '## How the result changes the next decision',
             '- If supported: ' + call['if_yes'], '- If refuted: ' + call['if_no'],
                  '- If inconclusive: ' + call['if_inconclusive'], '']
    shared = [item for item in shared_candidates(data) if identifier in item['calls']]
    if shared:
        lines.extend(['## Shared proof obligations', ''])
        lines.extend(f'- `{item["id"]}` — {item["statement"]}' for item in shared)
        lines.append('')
    lines.extend(['## Read these sources', ''])
    sources = [*data['sources'].values(), *call['inputs']]
    seen = set()
    for source in sources:
        if source['path'] not in seen:
            lines.append(f'- {source["path"]} (SHA-256 {source["sha256"]})')
            seen.add(source['path'])
    lines += ['', 'Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. '
              'A finite check or a failed sufficient bound does not settle the asymptotic target.', '']
    return '\n'.join(lines)


def checkpoint(data: dict, path: Path) -> str:
    calls = sorted(data['next_calls'], key=lambda item: item['priority'])
    shared = shared_candidates(data)
    lines = ['---', '---', '', f'# Paley synthesis checkpoint after round {data["round"]}', '',
             f'Draft from `{path.relative_to(ROOT)}`. Verify evidence labels and fill any route decisions before handoff.',
             '', '## Question examined', '',
             'What did this round change in the search for the ordinary Lovász theta limit of prime Paley localizations, '
             'and what should a fresh coordinator test next?', '', '## What we learned', '']
    for change in data['changes']:
        lines.append(f'- **{change["route"]}** ({change["effect"]}) — {change["after"]}')
    lines.extend(['', '## What resists', ''])
    for item in shared:
        references = ', '.join(f'`{identifier}`' for identifier in item['calls'])
        lines.append(f'- `{item["id"]}` — {item["statement"]} Shared by {references}.')
    for change in data['changes']:
        lines.append(f'- **{change["route"]}** — {change["remaining"]}')
    lines.extend(['', '## Proposed next step', '', data['decision_reason'], ''])
    if calls:
        first, *queued = calls
        lines.extend([f'**First proposed mission** `{first["id"]}`', '', first['question'], first['why_now'],
                      first['scope'], '', '- If supported — ' + first['if_yes'],
                      '- If refuted — ' + first['if_no'], '- If inconclusive — ' + first['if_inconclusive'], ''])
        for call in queued:
            lines.append(f'- **Queued** `{call["id"]}` — {call["question"]} {call["why_now"]}')
    lines.extend(['', '**Reading path**', '', f'- `{data["sources"]["current"]["path"]}`'])
    if calls:
        for source in calls[0]['inputs']:
            if source['path'] != data['sources']['current']['path']:
                lines.append(f'- `{source["path"]}`')
    return '\n'.join(lines) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ['init', 'show', 'check', 'mission', 'checkpoint']:
        command = commands.add_parser(name)
        command.add_argument('--round', type=int, help='defaults to the latest acceptance round')
        if name == 'init':
            command.add_argument('--baseline', help='repository-relative earlier acceptance record')
        if name == 'check':
            command.add_argument('--current', action='store_true', help='require the latest acceptance round')
        if name == 'mission':
            command.add_argument('--call', required=True, help='proposed call id')
    commands.add_parser('status', help='check coordination readiness for the latest acceptance')
    args = parser.parse_args()
    try:
        if args.command == 'init':
            path = initialize(args.round, args.baseline)
            print(f'Created draft: {path.relative_to(ROOT)}. Fill the assessment; no plan change was inferred.')
            return 0
        selected = selected_record(getattr(args, 'round', None))
        path = review_path(selected.round_number)
        if not path.exists():
            raise ValueError(f'No coordinator record for round {selected.round_number}. Run: '
                             f'python3 scripts/round_review.py init --round {selected.round_number}')
        content = path.read_bytes()
        data = json.loads(content)
        if not isinstance(data, dict):
            raise ValueError(f'{path}: expected a JSON object')
        if args.command == 'show':
            print(show(data))
            return 0
        current_required = args.command in {'mission', 'status'} or getattr(args, 'current', False)
        validate(data, selected.round_number, current_required)
        if args.command == 'mission':
            print(mission(data, args.call, path, hashlib.sha256(content).hexdigest()))
        elif args.command == 'checkpoint':
            print(checkpoint(data, path), end='')
        else:
            print(f'Round {selected.round_number}: coordinator record ready; '
                  f'{len(data["changes"])} assessments, {len(data["next_calls"])} proposed calls. '
                  'Structure and source bytes checked; mathematics not certified and no agent launched.')
        return 0
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    raise SystemExit(main())
