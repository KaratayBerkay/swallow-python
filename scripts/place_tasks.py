"""Place existing checkpoints in their lesson's reading flow."""

import json
import os
from pathlib import Path

from validate_tasks import ROOT, SECTION_MENU, clean_source, embedded_text, number


def relative(source, target):
    return Path(os.path.relpath(target, source.parent)).as_posix()


def place(root):
    manifest = json.loads((root / 'tasks/manifest.json').read_text())
    rows = {row['id']: row for row in manifest['sections']}
    milestones = {row['section']: row for row in manifest['milestones']}
    events = []

    def walk(sid):
        row = rows[sid]
        if row['status'] == 'task':
            events.append((sid, row['task'], row['source']))
        children = [other for other in rows
                    if Path(rows[other]['source']).parent.parent == Path(row['source']).parent]
        for child in sorted(children, key=number):
            walk(child)
        if sid in milestones:
            events.append(('milestone:' + sid, milestones[sid]['task'], row['source']))

    walk('t:root')
    walk('r:root')
    walk('b:root')
    following = {event[0]: events[i + 1] if i + 1 < len(events) else None
                 for i, event in enumerate(events)}

    def block(kind, event_id, checkpoint_path, source, base):
        checkpoint = (root / checkpoint_path).read_text()
        text = embedded_text(checkpoint, base)
        label = 'bölüm görevi' if kind == 'task' else 'klasör milestone görevi'
        text += f'\nAyrı dosya: [{label}]({Path(checkpoint_path).name}).\n'
        next_event = following[event_id]
        if next_event:
            next_id, _, next_source = next_event
            link = relative(source, Path(next_source))
            if next_id.startswith('milestone:'):
                link += '#klasör-milestone-görevi'
                action = 'Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.'
            else:
                action = 'Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.'
            text += f'\n**Sonraki adım:** [{action}]({link})\n'
        else:
            text += '\nBu öğrenme rotasındaki son kontrol.\n'
        return f'\n<!-- learning-{kind}:start -->\n{text}<!-- learning-{kind}:end -->\n'

    for sid, row in rows.items():
        if row['status'] != 'task' and sid not in milestones:
            continue
        source = Path(row['source'])
        base = clean_source((root / source).read_text())
        menu = SECTION_MENU.search(base)
        insertion = menu.start() if menu else len(base)
        rendered = base
        if row['status'] == 'task':
            rendered = (base[:insertion] + block('task', sid, row['task'], source, base)
                        + base[insertion:])
        if sid in milestones:
            rendered += block('milestone', 'milestone:' + sid,
                              milestones[sid]['task'], source, base)
        assert clean_source(rendered) == base, f'Lesson text changed: {source}'
        (root / source).write_text(rendered)

    index_path = root / 'TASKS.md'
    index = index_path.read_text()
    for _, checkpoint, source in events:
        link = source
        if checkpoint.endswith('/MILESTONE.md'):
            link += '#klasör-milestone-görevi'
        index = index.replace('](' + checkpoint + ')', '](' + link + ')')
    index_path.write_text(index)
    print(f'Placed {sum(r["status"] == "task" for r in rows.values())} tasks '
          f'and {len(milestones)} milestone checkpoints inline.')


if __name__ == '__main__':
    place(ROOT)
