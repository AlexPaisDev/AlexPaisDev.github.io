"""
Quick health check to run after editing the site by hand.

  python tools/check_site.py

For every page it reports:
  * texts marked with data-i18n (or data-i18n-attr) that have no Portuguese version,
  * links and files (href / src) that point to something missing in the repo,
  * id="…" values used more than once.
Exit code 0 = all good, 1 = something to fix. Uses only the Python standard library.
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'data/index.html', 'software/index.html', 'download.html', '404.html']
KEY = re.compile(r"^\s*'([^']+)'\s*:", re.M)


def pt_keys(page_path, html):
    """Portuguese keys available to a page: its i18n scripts plus any inline I18N_PT block."""
    keys = set()
    for src in re.findall(r'<script src="([^"]*i18n/[^"]+)"', html):
        keys |= set(KEY.findall((page_path.parent / src).resolve().read_text(encoding='utf8')))
    for block in re.findall(r'window\.I18N_PT\s*=\s*\{(.*?)\};', html, re.S):
        keys |= set(KEY.findall(block))
    return keys


def main():
    problems = 0
    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            continue
        html = path.read_text(encoding='utf8')
        used = set(re.findall(r'data-i18n="([^"]+)"', html))
        for attr in re.findall(r'data-i18n-attr="([^"]+)"', html):
            used |= {pair.split(':')[1] for pair in attr.split(';') if ':' in pair}
        missing = sorted(used - pt_keys(path, html))
        for key in missing:
            print(f'{name}: no Portuguese text for "{key}"')
        for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
            if re.match(r'^(https?:|mailto:|tel:|#|data:)', ref):
                continue
            clean = ref.split('#')[0].split('?')[0]
            target = (ROOT / clean.lstrip('/')) if clean.startswith('/') else (path.parent / clean).resolve()
            if target.is_dir():
                target = target / 'index.html'
            if not target.exists():
                print(f'{name}: broken link "{ref}"')
                problems += 1
        dupes = [i for i, n in collections.Counter(re.findall(r'\sid="([^"]+)"', html)).items() if n > 1]
        for i in dupes:
            print(f'{name}: id "{i}" is used more than once')
        problems += len(missing) + len(dupes)
    print('All good.' if not problems else f'{problems} problem(s) found.')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
