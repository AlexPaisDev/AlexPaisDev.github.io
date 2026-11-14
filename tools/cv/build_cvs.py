"""
Builds the four CVs from content.py, all with the same look (template.docx).

  python tools/cv/build_cvs.py

Writes:
  cv-source/<name>.docx   editable Word files (local only, not published)
  <name>.pdf              in the site root, the files the website links to
The PDF step uses Microsoft Word (Windows). Without Word you still get the .docx files.
Standard library only.
"""
import html
import pathlib
import re
import subprocess
import sys
import zipfile
from datetime import datetime, timezone

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TEMPLATE = HERE / 'template.docx'
OUT_DOCX = ROOT / 'cv-source'
sys.path.insert(0, str(HERE))
import content  # noqa: E402

T = re.compile(r'<w:t(?: [^>]*)?>[^<]*</w:t>')


# ---------------------------------------------------------------- template pieces
def load_template():
    with zipfile.ZipFile(TEMPLATE) as z:
        files = {n: z.read(n) for n in z.namelist() if not n.endswith('/')}
    doc = files['word/document.xml'].decode('utf8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    sect = doc[doc.index('<w:sectPr'):]
    body = doc[len(head):doc.index('<w:sectPr')]
    items = re.findall(r'<w:p[ >].*?</w:p>|<w:tbl>.*?</w:tbl>', body, re.S)

    def find(test, what):
        for it in items:
            if test(it):
                return it
        raise SystemExit(f'template.docx: no paragraph found for {what}')

    is_list = lambda p: 'ListParagraph' in p
    pieces = {
        'h1': find(lambda p: 'Heading1' in p, 'name (Heading 1)'),
        'h2': find(lambda p: 'Heading2' in p, 'section title (Heading 2)'),
        'h3': find(lambda p: 'Heading3' in p, 'job title (Heading 3)'),
        'contact': find(lambda p: '<w:hyperlink' in p, 'contact line'),
        'bullet': find(lambda p: is_list(p) and len(T.findall(p)) == 1 and '<w:b/>' not in p, 'bullet'),
        'tech': find(lambda p: '<w:i/>' in p, 'technologies line'),
        'labelled': find(lambda p: is_list(p) and '<w:b/>' in p, 'labelled bullet'),
        'edu': find(lambda p: not is_list(p) and '<w:b/>' in p and 'Heading' not in p, 'education line'),
        'table': find(lambda p: p.startswith('<w:tbl>'), 'languages table'),
    }
    # a plain paragraph: no style, no list, no bold/italic, no link (the headline under the name)
    pieces['plain'] = find(lambda p: '<w:pPr>' not in p and '<w:b/>' not in p and '<w:i/>' not in p and '<w:hyperlink' not in p, 'plain paragraph')
    return files, head, sect, pieces


def fill(xml, *texts):
    """Put texts into the template element's text runs, in order (extra runs become empty)."""
    runs = T.findall(xml)
    if len(texts) > len(runs):
        raise SystemExit(f'template element has {len(runs)} text runs, got {len(texts)} texts')
    it = iter(list(texts) + [''] * (len(runs) - len(texts)))
    xml = T.sub(lambda m: f'<w:t xml:space="preserve">{html.escape(next(it), quote=False)}</w:t>', xml)
    # cloned paragraphs must not share Word's internal ids
    return re.sub(r' (?:w14:paraId|w14:textId|w:rsid\w*)="[^"]*"', '', xml)


def keep_with_next(xml):
    """Ask Word to keep this paragraph on the same page as the next one (dates with their bullets…)."""
    if '<w:pPr>' in xml:
        return xml.replace('<w:pPr>', '<w:pPr><w:keepNext/>', 1)
    return re.sub(r'(<w:p\b[^>]*>)', r'\1<w:pPr><w:keepNext/></w:pPr>', xml, count=1)


# ---------------------------------------------------------------- one CV
def build_document(cv, head, sect, P):
    out = [
        fill(P['h1'], content.NAME),
        fill(P['plain'], cv['headline']),
        fill(P['contact'], f"{cv['location']} · {content.EMAIL} · {content.PHONE} · ", content.LINKEDIN),
        fill(P['plain'], cv['open_to']),
    ]
    for kind, title, data in cv['sections']:
        out.append(fill(P['h2'], title))
        if kind == 'summary':
            out.append(fill(P['plain'], data))
        elif kind == 'jobs':
            for job in data:
                out.append(fill(P['h3'], job['title']))
                out.append(keep_with_next(fill(P['plain'], job['dates'])))
                out += [fill(P['bullet'], b) for b in job['bullets']]
                out.append(fill(P['tech'], job['tech']))
        elif kind == 'labelled':
            out += [fill(P['labelled'], label, text) for label, text in data]
        elif kind == 'education':
            for bold, rest, note in data:
                edu = fill(P['edu'], bold, rest)
                out.append(keep_with_next(edu) if note else edu)
                if note:
                    out.append(fill(P['plain'], note))
        elif kind == 'languages':
            cells = [c for row in data for c in row]
            out.append(fill(P['table'], *cells))
        else:
            raise SystemExit(f'unknown section kind: {kind}')
    return head + ''.join(out) + sect


def core_xml(cv):
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lang = 'pt-PT' if cv['lang'] == 'pt' else 'en-GB'
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<dc:title>{html.escape(cv["doc_title"])}</dc:title><dc:creator>{content.NAME}</dc:creator>'
            f'<cp:lastModifiedBy>{content.NAME}</cp:lastModifiedBy><dc:language>{lang}</dc:language>'
            f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
            f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>')


def write_docx(cv, files, document):
    OUT_DOCX.mkdir(exist_ok=True)
    path = OUT_DOCX / f"{cv['pdf']}.docx"
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in files.items():
            if name == 'word/document.xml':
                data = document.encode('utf8')
            elif name == 'docProps/core.xml':
                data = core_xml(cv).encode('utf8')
            z.writestr(name, data)
    return path


# ---------------------------------------------------------------- PDF through Word
def export_pdfs(docx_paths):
    if sys.platform != 'win32':
        print('PDF export needs Microsoft Word on Windows: open the .docx files and "Save as PDF".')
        return
    src = ','.join(f"'{d}'" for d in docx_paths)
    dst = ','.join(f"'{ROOT / (d.stem + '.pdf')}'" for d in docx_paths)
    ps = (
        f"$ErrorActionPreference='Stop'; $src=@({src}); $dst=@({dst});"
        " $w = New-Object -ComObject Word.Application; $w.Visible=$false; $w.DisplayAlerts=0;"
        " try { for ($i = 0; $i -lt $src.Count; $i++) { $d = $w.Documents.Open($src[$i], $false, $true);"
        " $n = $d.ComputeStatistics(2); $d.SaveAs([ref]$dst[$i], [ref]17); $d.Close([ref]0);"
        " Write-Output ('{0}  ({1} pages)' -f (Split-Path $dst[$i] -Leaf), $n) } }"
        " finally { $w.Quit(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($w) }"
    )
    result = subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-Command', ps],
                            capture_output=True, text=True, timeout=300)
    print(result.stdout.strip() or result.stderr.strip())


if __name__ == '__main__':
    files, head, sect, pieces = load_template()
    made = []
    for cv in content.CVS:
        made.append(write_docx(cv, files, build_document(cv, head, sect, pieces)))
        print('built', made[-1].relative_to(ROOT))
    export_pdfs(made)
