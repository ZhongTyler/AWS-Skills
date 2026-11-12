"""Inventory static HTML dependencies and embedded Markdown source references.

This is a read-only audit. It neither runs JavaScript nor fetches/copies resources.
Attachment origins are optional and must be supplied explicitly by the caller.
"""
import argparse
import base64
import hashlib
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, unquote_to_bytes, urlsplit


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def location_kind(value):
    value = value.strip()
    if not value or value.startswith('#'):
        return 'internal'
    if value.lower().startswith('data:'):
        return 'embedded'
    if value.startswith('//'):
        return 'network'
    if re.match(r'^[A-Za-z]:[\\/]', value):
        return 'local'
    scheme = urlsplit(value).scheme.lower()
    if scheme in ('http', 'https'):
        return 'network'
    if scheme in ('', 'file'):
        return 'local'
    return 'other_scheme'


def css_urls(text):
    pattern = r'url\(\s*(?:"([^"]*)"|\x27([^\x27]*)\x27|([^)]*?))\s*\)|@import\s+["\x27]([^"\x27]+)["\x27]'
    return [next((x for x in match.groups() if x is not None), '')
            for match in re.finditer(pattern, text, re.I)]


def srcset_urls(value):
    # A data URI can contain commas. Consume its non-whitespace payload intact.
    return re.findall(r'(?:^|,\s*)(data:[^\s]+|[^,\s]+)', value)


class Inventory(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.runtime = []
        self.links = []
        self.attachments = []
        self.styles = []
        self.scripts = []
        self.active = None
        self.base_hrefs = []
        self.inline_documents = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('style', 'script'):
            self.active = tag
        if tag == 'base' and attrs.get('href'):
            self.base_hrefs.append(attrs['href'])
        if 'srcdoc' in attrs:
            self.inline_documents += 1
        if attrs.get('style'):
            self.styles.append(attrs['style'])
        runtime_attrs = {
            'img': ('src',), 'script': ('src',), 'iframe': ('src',),
            'audio': ('src',), 'video': ('src', 'poster'),
            'source': ('src',), 'track': ('src',), 'object': ('data',),
            'embed': ('src',), 'image': ('href', 'xlink:href'),
            'use': ('href', 'xlink:href'), 'input': ('src',),
        }
        for attr in runtime_attrs.get(tag, ()):
            if attrs.get(attr):
                self.runtime.append((f'{tag}.{attr}', attrs[attr]))
        if tag in ('img', 'source') and attrs.get('srcset'):
            self.runtime.extend((f'{tag}.srcset', url)
                                for url in srcset_urls(attrs['srcset']))
        if tag == 'link' and attrs.get('href'):
            self.runtime.append(('link.href', attrs['href']))
        if tag == 'a' and attrs.get('href'):
            value = attrs['href']
            self.links.append(value)
            if re.match(r'data:(?:text/markdown|text/x-markdown)', value, re.I):
                self.attachments.append((attrs.get('download', ''), value))

    def handle_endtag(self, tag):
        if tag == self.active:
            self.active = None

    def handle_data(self, data):
        if self.active == 'style':
            self.styles.append(data)
        elif self.active == 'script':
            self.scripts.append(data)


def markdown_urls(text):
    # Ignore fenced/inline code. This covers common inline and reference links,
    # plus HTML resources, and leaves exotic Markdown syntax for manual review.
    text = re.sub(r'^\s*(`{3,}|~{3,}).*?^\s*\1\s*$', '', text,
                  flags=re.M | re.S)
    text = re.sub(r'`+[^`\n]*`+', '', text)
    urls = []
    for match in re.finditer(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|(?:[^\s()]|\([^()]*\))+)\s*(?:["\x27][^\n]*?["\x27]\s*)?\)', text):
        urls.append(match[1].strip('<>'))
    urls.extend(match[1].strip('<>') for match in re.finditer(
        r'^\s{0,3}\[[^\]\n]+\]:\s*(<[^>]+>|\S+)', text, re.M))
    markup = Inventory()
    markup.feed(text)
    urls.extend(value for _, value in markup.runtime)
    urls.extend(markup.links)
    return urls


def resolve_local(value, origin, roots):
    parsed = urlsplit(value)
    if parsed.scheme == 'file' and parsed.netloc:
        return {'status': 'remote_file_uri'}
    path_text = unquote(value.split('#', 1)[0].split('?', 1)[0])
    if parsed.scheme == 'file':
        path_text = unquote(parsed.path)
        if re.match(r'^/[A-Za-z]:/', path_text):
            path_text = path_text[1:]
    path = (origin.parent / path_text).resolve()
    result = {'path': str(path)}
    if not any(path.is_relative_to(root) for root in roots):
        return dict(result, status='outside_allowed_roots')
    if path.is_file():
        return dict(result, status='exists')
    return dict(result, status='exists_directory' if path.is_dir() else 'missing')


def audit_html(path, origins=None, roots=None):
    path = Path(path).resolve(strict=True)
    roots = [Path(root).resolve() for root in (roots or [path.parent])]
    origins = origins or []
    by_name = {}
    for item in origins:
        if item['download'] in by_name:
            raise ValueError('Duplicate attachment origin name')
        by_name[item['download']] = item
    raw = path.read_bytes()
    parser = Inventory()
    parser.feed(raw.decode('utf-8-sig'))
    runtime = []
    for style in parser.styles:
        parser.runtime.extend(('css.url', value) for value in css_urls(style))
    for context, value in parser.runtime:
        kind = location_kind(value)
        record = {'context': context, 'kind': kind}
        if kind == 'embedded':
            record['mime'] = value.split(',', 1)[0].split(';', 1)[0][5:]
        else:
            record['value'] = value
        if kind == 'local' and not parser.base_hrefs:
            record.update(resolve_local(value, path, roots))
        runtime.append(record)
    attachments = []
    embedded_origins = set()
    for name, value in parser.attachments:
        header, payload = value.split(',', 1)
        body = base64.b64decode(payload, validate=True) if ';base64' in header.lower() else unquote_to_bytes(payload)
        record = {'download': name, 'bytes': len(body), 'sha256': digest(body),
                  'local_references': []}
        origin_spec = by_name.get(name)
        origin = Path(origin_spec['path']).resolve() if origin_spec else None
        if origin_spec and origin_spec.get('sha256') != record['sha256']:
            raise ValueError(f'Attachment origin hash mismatch: {name}')
        if origin:
            embedded_origins.add(str(origin))
            record['origin'] = str(origin)
        for value in markdown_urls(body.decode('utf-8-sig')):
            if location_kind(value) != 'local':
                continue
            reference = {'value': value, 'status': 'origin_unknown'}
            if origin:
                reference.update(resolve_local(value, origin, roots))
            record['local_references'].append(reference)
        attachments.append(record)
    targets = {}
    for attachment in attachments:
        for reference in attachment['local_references']:
            if 'path' not in reference:
                continue
            key = reference['path']
            reference['embedded_as_markdown'] = key in embedded_origins
            target = targets.setdefault(key, {'path': key, 'status': reference['status'],
                                              'embedded_as_markdown': key in embedded_origins,
                                              'downloads': [], 'occurrences': 0})
            if attachment['download'] not in target['downloads']:
                target['downloads'].append(attachment['download'])
            target['occurrences'] += 1
    warnings = []
    scripts = '\n'.join(parser.scripts)
    for label, pattern in {
        'script_network_or_module_api': r'\b(?:fetch|XMLHttpRequest|WebSocket|Worker|importScripts)\b|\bimport\s*(?:\(|["\x27{*])',
        'script_resource_assignment': r'\.(?:src|href)\s*=|setAttribute\(\s*["\x27](?:src|href)',
    }.items():
        if re.search(pattern, scripts):
            warnings.append(label)
    if parser.base_hrefs:
        warnings.append('base_href_requires_manual_resolution')
    if parser.inline_documents:
        warnings.append('srcdoc_requires_nested_document_review')
    kinds = Counter(item['kind'] for item in runtime)
    summary = {'runtime_resources': len(runtime), 'runtime_kinds': dict(kinds),
               'static_runtime_embedded_or_internal': all(item['kind'] in ('embedded', 'internal') for item in runtime),
               'embedded_markdown_downloads': len(attachments),
               'attachment_local_link_occurrences': sum(len(item['local_references']) for item in attachments),
               'attachment_unique_resolved_targets': len(targets),
               'attachment_targets_embedded_as_markdown': sum(item['embedded_as_markdown'] for item in targets.values()),
               'attachment_target_statuses': dict(Counter(item['status'] for item in targets.values())),
               'ordinary_link_kinds': dict(Counter(location_kind(value) for value in parser.links)),
               'manual_review_flags': warnings}
    return {'schema': 'html-dependency-audit/v1', 'html_sha256': digest(raw),
            'summary': summary, 'runtime': runtime, 'attachments': attachments,
            'attachment_targets': list(targets.values()),
            'scope': 'Static HTML/CSS and common Markdown links. Does not execute scripts, fetch resources, prove browser behavior or measure reader understanding.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html', type=Path)
    parser.add_argument('--attachment-origins', type=Path)
    parser.add_argument('--allow-root', type=Path, action='append')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--check-runtime', action='store_true')
    args = parser.parse_args()
    origins = json.loads(args.attachment_origins.read_text(encoding='utf-8')) if args.attachment_origins else None
    result = audit_html(args.html, origins, args.allow_root)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result['summary'], ensure_ascii=False))
    if args.check_runtime and not result['summary']['static_runtime_embedded_or_internal']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
