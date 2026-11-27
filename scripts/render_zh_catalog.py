"""Project the reviewed Chinese reader catalog; never edit Skill originals or IDs."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / 'locales/zh-CN.json'


def outputs():
    locale = json.loads(LOCALE.read_text('utf-8'))
    catalog = json.loads((ROOT / 'catalog.json').read_text('utf-8'))
    current = json.loads((ROOT / 'skills.json').read_text('utf-8'))
    rows = locale['skills']
    by_id = {row['id']: row for row in rows}
    if len(rows) != 42 or len(by_id) != 42 or set(by_id) != set(catalog['components']):
        raise ValueError('Chinese locale must match all 42 selectable IDs exactly')
    if {row['id'] for row in current['skills']} != set(by_id):
        raise ValueError('Reader index and selectable IDs differ')
    for row in rows:
        for key in ('display_name_zh', 'description_zh'):
            if not isinstance(row[key], str) or not any('\u4e00' <= c <= '\u9fff' for c in row[key]):
                raise ValueError('Missing Chinese reader field: ' + row['id'])
        if row['upstream_url'] is not None and not row['provenance_evidence']:
            raise ValueError('External repository needs preserved evidence: ' + row['id'])
        for proof in row['provenance_evidence']:
            path = (ROOT / proof['path']).resolve()
            if not path.is_relative_to(ROOT) or hashlib.sha256(path.read_bytes()).hexdigest() != proof['sha256']:
                raise ValueError('Source evidence changed: ' + row['id'])
    for row in current['skills']:
        text = by_id[row['id']]
        row.update(description=text['description_zh'], display_name_zh=text['display_name_zh'],
                   description_original=text['description_original'], upstream_url=text['upstream_url'],
                   origin_kind=text['origin_kind'])
    current['reader_locale'] = 'locales/zh-CN.json'
    lines = ['# 中文方法目录', '',
             '显示名和简介来自 [统一中文映射](../locales/zh-CN.json)。英文 ID 用于调用、选装与升级；中文名用于阅读。', '',
             '外部方法按包内来源记录列出原仓库。工作区维护表示当前维护归属，不据此宣称原创。上游正文、原始快照、代码和既有许可保持原样。', '',
             '| 中文名称 | 调用 ID | 简介 | 来源 |', '|---|---|---|---|']
    def cell(value):
        return value.replace('|', '\\|').replace('\n', ' ')
    for row in rows:
        source = '[原仓库](' + row['upstream_url'] + ')' if row['upstream_url'] else '工作区维护'
        lines.append('| [' + cell(row['display_name_zh']) + '](../library/' + row['id'] + '/SKILL.md) | ' + row['id'] + ' | ' + cell(row['description_zh']) + ' | ' + source + ' |')
    result = {'skills.json': (json.dumps(current, ensure_ascii=False, indent=2)+'\n').encode(),
              'docs/skills.zh-CN.md': ('\n'.join(lines)+'\n').encode()}
    for row in rows:
        source = ('本方法引入或适配自 [原仓库](' + row['upstream_url'] + ')。上游原件与许可按原记录保留。'
                  if row['upstream_url'] else '本方法由工作区维护；具体依据见方法正文，此分类不作原创性认定。')
        text = '# ' + row['display_name_zh'] + '\n\n' + row['description_zh'] + '\n\n调用 ID：' + row['id']
        text += '\n\n' + source + '\n\n[方法正文](SKILL.md)包含具体做法及检查要求。中文显示名用于阅读，英文调用 ID 和原文保持原样。\n'
        result['library/' + row['id'] + '/README.zh-CN.md'] = text.encode()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    generated = outputs()
    drift = []
    for name, data in generated.items():
        path = ROOT / name
        if not path.is_file() or path.read_bytes() != data:
            drift.append(name)
        if args.apply:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(json.dumps({'skills': 42, 'locale_sha256': hashlib.sha256(LOCALE.read_bytes()).hexdigest(),
                      'applied': args.apply, 'drift': drift}, ensure_ascii=False))
    return 0 if args.apply or not drift else 1


if __name__ == '__main__':
    raise SystemExit(main())
