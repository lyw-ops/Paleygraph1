#!/usr/bin/env python3
"""Browse and run published Paley Python tools without moving their source files."""

from __future__ import annotations

import argparse
import ast
from collections import defaultdict
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'scripts' / 'python-tools.json'
GUIDE = ROOT / 'docs' / 'PYTHON.md'

GROUPS = {
    'theta': ('Theta and witnesses', 'The ordinary theta programs and explicit witness families.'),
    'smoothing': ('Smoothing and signed iterates', 'Fourier smoothing, mixed feedback and signed drift.'),
    'response': ('Stationary response', 'Marked response, resolvents, stationary modes and sitewise changes.'),
    'repairs': ('Witness repair', 'Point, coset and negative-part repairs of proposed witnesses.'),
    'quadratic': ('Quadratic regularization', 'Regularized programs, energy bounds and one-sided penalties.'),
    'endpoints': ('Endpoint geometry', 'Endpoint supports, tangents, extensions and exact finite checks.'),
    'geometry': ('Cosets, ranks and sparse geometry', 'Subgroups, phase profiles, ranks and sparse frequency models.'),
    'rounds': ('Research-round scripts', 'Historical route-specific scripts, grouped by the round in their filename.'),
    'maintenance': ('Repository maintenance', 'Navigation, catalogue generation and maintenance tests.'),
    'other': ('Other published Python files', 'Published files awaiting a more specific functional classification.'),
}

ROOT_GROUPS = {
    'theta': 'theta witnesses',
    'smoothing': 'smoothing square_control feedback log_means signed_drift',
    'response': 'sensitivity response_shift response_windows stationary_modes stationary_attenuation stationary_ordered stationary_secant stationary_defect_tail stationary_mark_constant subgroup_modes coset_activation_probe exterior_focus',
    'repairs': 'iterate_majorants coset_majorants negative_pairing bulk_caps endpoint_mixture',
    'quadratic': 'quadratic_theta quadratic_gap quadratic_fourth quadratic_compression quadratic_angle one_sided_penalty rational_endpoint',
    'endpoints': 'endpoint_norm endpoint_tangent endpoint_tangent_certificate endpoint_extension_certificate square_endpoint_rank parallel_kernel_11 parallel_sampling_12',
    'geometry': 'mobius_probe critical_sets progression_boxes coset_defects coset_bands coset_phase_check coset_phase_certificate face_ranks rank_partitions poisson_weights two_mark_geometry two_mark_frontier parallel_sparse_check neighbor_compression',
}
CLASSIFICATION = {name + '.py': group for group, names in ROOT_GROUPS.items() for name in names.split()}


def git(*args: str, input: bytes | None = None) -> bytes:
    result = subprocess.run(['git', '-C', str(ROOT), *args], input=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError(result.stderr.decode().strip())
    return result.stdout


def published_sources(ref: str) -> tuple[str, dict[str, bytes]]:
    revision = git('rev-parse', '--verify', ref + '^{commit}').decode().strip()
    blobs = []
    for row in git('ls-tree', '-r', '-z', revision).split(b'\0'):
        if not row:
            continue
        metadata, name = row.split(b'\t', 1)
        mode, kind, oid = metadata.split()
        if name.endswith(b'.py') and kind == b'blob' and mode in (b'100644', b'100755'):
            blobs.append((name.decode(), oid))
    raw = git('cat-file', '--batch', input=b''.join(oid + b'\n' for _, oid in blobs)) if blobs else b''
    stream = io.BytesIO(raw)
    sources = {}
    for name, oid in blobs:
        actual_oid, kind, size = stream.readline().split()
        if actual_oid != oid or kind != b'blob':
            raise ValueError(f'Unexpected Git object for {name}')
        content = stream.read(int(size))
        if stream.read(1) != b'\n':
            raise ValueError(f'Truncated Git object for {name}')
        sources[name] = content
    return revision, sources


def build_catalog(ref: str) -> dict:
    revision, sources = published_sources(ref)
    tools = []
    for name, content in sorted(sources.items()):
        tree = ast.parse(content, filename=name)
        description = ast.get_docstring(tree) or ''
        if name.startswith('research/'):
            group = 'rounds'
        elif name.startswith(('scripts/', 'tests/')):
            group = 'maintenance'
        else:
            group = CLASSIFICATION.get(name, 'other')
        match = re.search(r'[-_](\d+)(?=[-_]|\.py$)', Path(name).name)
        imports = set()
        for node in ast.walk(tree):
            modules = []
            if isinstance(node, ast.Import):
                modules = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                modules = [node.module]
            for module in modules:
                relative = module.replace('.', '/') + '.py'
                for candidate in [(Path(name).parent / relative).as_posix(), relative]:
                    if candidate in sources:
                        imports.add(candidate)
                        break
        tools.append({
            'path': name,
            'group': group,
            'round': int(match[1]) if match else None,
            'description': description.splitlines()[0].strip() if description else '',
            'static_imports': sorted(imports),
            'sha256': hashlib.sha256(content).hexdigest(),
        })
    return {'schema_version': 1, 'source_revision': revision, 'tools': tools}


def source_link(path: str, label: str | None = None) -> str:
    return f'[{label or Path(path).name}](../{quote(path, safe="/.-_")})'


def render_guide(catalog: dict) -> str:
    grouped = defaultdict(list)
    for tool in catalog['tools']:
        grouped[tool['group']].append(tool)
    revision = catalog['source_revision']
    lines = [
        '# Python tools', '',
        f'This catalogue covers **{len(catalog["tools"])} Python files** from published snapshot '
        f'[{revision[:7]}](https://github.com/lyw-ops/Paleygraph1/tree/{revision}). '
        'It is built from Git objects, so uncommitted files are excluded.', '',
        '## One entry point', '',
        'Listing and inspecting tools use only the Python standard library. Use the project interpreter '
        'to run mathematical programs after installing [requirements.txt](../requirements.txt).', '',
        '```sh',
        'python3 scripts/paley.py list',
        'python3 scripts/paley.py list --group response',
        'python3 scripts/paley.py list --round 91',
        'python3 scripts/paley.py show theta',
        '.venv/bin/python -B scripts/paley.py run theta --certify 5 13 41',
        '.venv/bin/python -B scripts/paley.py run research/real-two-marks-91-check.py',
        '```', '',
        '`list` shows the shared tools and maintenance utilities by default; `--all` includes the round '
        'archive. Tool selectors accept a catalogue path, or a unique filename or stem. `show` reads '
        'catalogue metadata without importing the selected program.', '',
        '`run` uses the interpreter that invoked this entry point, executes the existing file from the '
        'repository root and adds that root to `PYTHONPATH`. Arguments, stdout, stderr and exit status '
        'belong to the selected program. Relative input/output paths are resolved from the repository '
        'root. A run uses this checkout, including any local modifications; the catalogue is not a '
        'frozen execution environment.', '',
        'Original paths, imports and direct commands remain available. Some round scripts have fixed '
        'parameters and run immediately; use `show` to inspect their description before execution.', '',
        '## Shared tools by function', '',
    ]
    for key, (title, description) in GROUPS.items():
        tools = grouped[key]
        if key == 'rounds' or not tools:
            continue
        lines += [f'### {title}', '', description, '', '| Source | Purpose |', '| --- | --- |']
        for tool in tools:
            purpose = tool['description'].replace('|', '\\|') or 'See the source file.'
            lines.append(f'| {source_link(tool["path"])} | {purpose} |')
        lines += ['']
    lines += [
        '## Research-round archive', '',
        'Round labels below come from filenames. They do not establish acceptance or proof status; '
        'consult the [acceptance-record index](../research/README.md) and the associated notes.', '',
        '| Round | Scripts |', '| --- | --- |',
    ]
    rounds = defaultdict(list)
    for tool in grouped['rounds']:
        rounds[tool['round']].append(tool)
    for number in sorted(rounds, key=lambda value: value if value is not None else -1, reverse=True):
        links = ', '.join(source_link(tool['path']) for tool in rounds[number])
        lines.append(f'| {number if number is not None else "Unspecified"} | {links} |')
    lines += [
        '', '## Updating the catalogue', '',
        'The machine-readable source is [scripts/python-tools.json](../scripts/python-tools.json). '
        'It records source hashes and static imports within the published Python files. '
        'Static imports omit dynamic loads and data dependencies.', '',
        'After the intended research code is published, refresh from its published Git reference:', '',
        '```sh',
        'git fetch origin',
        'python3 scripts/paley.py index --ref origin/main --write',
        'python3 scripts/paley.py index --check',
        '```', '',
        '`index --check` compares the catalogue and this guide with their recorded source revision. '
        'It does not infer a newer published version or certify a mathematical result. Supplying '
        '`--ref` explicitly compares with that revision instead. No source program or acceptance '
        'record is rewritten.', '',
    ]
    return '\n'.join(lines)


def load_catalog() -> dict:
    data = json.loads(CATALOG.read_text())
    if data.get('schema_version') != 1 or not isinstance(data.get('tools'), list):
        raise ValueError('Unsupported Python tool catalogue')
    return data


def resolve_tool(catalog: dict, selector: str) -> dict:
    # A full path wins over basename aliases; ambiguous aliases are never guessed.
    matches = [tool for tool in catalog['tools'] if selector == tool['path']]
    if not matches:
        matches = [tool for tool in catalog['tools'] if selector in (Path(tool['path']).name, Path(tool['path']).stem)]
    if not matches:
        raise ValueError(f'Unknown published tool: {selector}. Use list --all to browse the catalogue.')
    if len(matches) > 1:
        raise ValueError('Ambiguous tool; use a full catalogue path: ' + ', '.join(tool['path'] for tool in matches))
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    listing = commands.add_parser('list', help='browse tools without importing them')
    listing.add_argument('--group', choices=GROUPS)
    listing.add_argument('--round', type=int)
    listing.add_argument('--all', action='store_true', help='include all research-round scripts')
    showing = commands.add_parser('show', help='show purpose, source and static local imports')
    showing.add_argument('tool')
    running = commands.add_parser('run', help='run an existing tool with its original arguments')
    running.add_argument('tool')
    running.add_argument('arguments', nargs=argparse.REMAINDER)
    indexing = commands.add_parser('index', help='refresh or validate the published-code catalogue')
    indexing.add_argument('--ref', help='Git revision to catalogue; required for a fresh catalogue')
    output = indexing.add_mutually_exclusive_group(required=True)
    output.add_argument('--write', action='store_true')
    output.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'index':
            previous = load_catalog() if CATALOG.exists() else None
            ref = args.ref or (previous['source_revision'] if previous else None)
            if not ref:
                raise ValueError('Choose the published source with --ref, for example --ref origin/main')
            catalog = build_catalog(ref)
            serialized = json.dumps(catalog, ensure_ascii=False, indent=2) + '\n'
            guide = render_guide(catalog)
            if args.write:
                CATALOG.write_text(serialized)
                GUIDE.parent.mkdir(parents=True, exist_ok=True)
                GUIDE.write_text(guide)
                print(f'Indexed {len(catalog["tools"])} Python files from {catalog["source_revision"][:7]}.')
            elif not CATALOG.exists() or CATALOG.read_text() != serialized or not GUIDE.exists() or GUIDE.read_text() != guide:
                print('Python catalogue or guide is stale. Refresh with index --ref <published-revision> --write.')
                return 1
            else:
                print(f'Python catalogue and guide match {catalog["source_revision"][:7]} ({len(catalog["tools"])} files).')
            return 0
        catalog = load_catalog()
        if args.command == 'list':
            selected = [tool for tool in catalog['tools']
                        if (not args.group or tool['group'] == args.group)
                        and (args.round is None or tool['round'] == args.round)
                        and (args.all or args.group or args.round is not None or tool['group'] != 'rounds')]
            for group, (title, _) in GROUPS.items():
                tools = [tool for tool in selected if tool['group'] == group]
                if tools:
                    print(f'{title} ({len(tools)})')
                    for tool in tools:
                        print(f'  {tool["path"]:<48} {tool["description"]}')
            return 0
        tool = resolve_tool(catalog, args.tool)
        if args.command == 'show':
            print(tool['description'] or tool['path'])
            print('Source:', tool['path'])
            print('Group:', GROUPS[tool['group']][0])
            print('Catalogue revision:', catalog['source_revision'])
            print('Recorded source SHA-256:', tool['sha256'])
            print('Static local imports:', ', '.join(tool['static_imports']) or '(none recorded)')
            callers = [item['path'] for item in catalog['tools'] if tool['path'] in item['static_imports']]
            print('Statically imported by:', ', '.join(callers) or '(none recorded)')
            return 0
        path = (ROOT / tool['path']).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError(f'Tool source is not available inside this checkout: {tool["path"]}')
        forwarded = args.arguments[1:] if args.arguments[:1] == ['--'] else args.arguments
        env = dict(os.environ)
        env['PYTHONPATH'] = str(ROOT) + (os.pathsep + env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
        os.chdir(ROOT)
        os.execve(sys.executable, [sys.executable, '-B', str(path), *forwarded], env)
    except (OSError, ValueError, SyntaxError, KeyError, TypeError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    raise SystemExit(main())
