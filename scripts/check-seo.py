"""Validate published metadata, local links, structured data and output parity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import struct
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'dist'
BASE = 'https://embroidhub.com'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.ids = set()
        self.json = []
        self.current = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        if 'id' in a:
            assert a['id'] not in self.ids, 'Duplicate HTML id'
            self.ids.add(a['id'])
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.current = ''

    def handle_data(self, value):
        if self.current is not None:
            self.current += value

    def handle_endtag(self, tag):
        if tag == 'script' and self.current is not None:
            self.json.append(json.loads(self.current))
            self.current = None

pages = {p: Page(p.read_text(encoding='utf-8')) for p in SITE.rglob('*.html')}
canonical_urls = set()
titles = set()
for path, page in pages.items():
    assert (ROOT / path.relative_to(SITE)).read_bytes() == path.read_bytes(), f'Stale output: {path}'
    assert sum(tag == 'h1' for tag, a in page.tags) == 1, path
    assert sum(tag == 'title' for tag, a in page.tags) == 1, path
    assert any(tag == 'html' and a.get('lang') == 'en' for tag, a in page.tags)
    meta = {a.get('name', a.get('property')): a.get('content') for tag, a in page.tags if tag == 'meta'}
    if path.name == '404.html':
        assert 'noindex' in meta['robots']
    else:
        canonicals = [a['href'] for tag, a in page.tags if tag == 'link' and a.get('rel') == 'canonical']
        assert len(canonicals) == 1
        expected_path = '/' + path.parent.relative_to(SITE).as_posix().strip('.')
        expected_path = expected_path.rstrip('/') + '/'
        assert canonicals[0] == BASE + expected_path, path
        assert canonicals[0] not in canonical_urls
        canonical_urls.add(canonicals[0])
        assert meta['description'] and 'max-image-preview:large' in meta['robots']
        assert 'noindex' not in meta['robots']
        assert meta['og:url'] == canonicals[0]
        assert meta['twitter:card'] == 'summary_large_image'
        assert meta['og:title'] not in titles
        titles.add(meta['og:title'])
        assert page.json
        image_path = SITE / urlsplit(meta['og:image']).path.lstrip('/')
        width, height = struct.unpack('>II', image_path.read_bytes()[16:24])
        assert width >= 1200 and width * height > 300000
        assert int(meta['og:image:width']) == width and int(meta['og:image:height']) == height
    for tag, a in page.tags:
        if tag == 'img':
            assert a.get('alt') and a.get('width') and a.get('height'), path
        if a.get('href', '').startswith('https://go.hotmart.com/'):
            assert a['href'] == 'https://go.hotmart.com/N101596432X'
            assert 'sponsored' in a.get('rel', '')
        for key in ('href', 'src'):
            url = urlsplit(a.get(key, ''))
            if key not in a or url.scheme or url.netloc:
                continue
            target = (SITE / url.path.lstrip('/')) if url.path.startswith('/') else path.parent / url.path
            if not url.path:
                target = path
            elif target.is_dir():
                target = target / 'index.html'
            assert target.exists(), f'Broken local link: {path} -> {a[key]}'
            if url.fragment and target.suffix == '.html':
                assert unquote(url.fragment) in pages[target].ids, f'Broken fragment: {a[key]}'

ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap = ET.parse(SITE / 'sitemap.xml')
assert {e.text for e in sitemap.findall('s:url/s:loc', ns)} == canonical_urls
assert f'Sitemap: {BASE}/sitemap.xml' in (SITE / 'robots.txt').read_text()
for asset in (SITE / 'assets').iterdir():
    assert asset.read_bytes() == (ROOT / 'assets' / asset.name).read_bytes()
assert not list(SITE.rglob('*.pdf')), 'Paid PDF must stay private'
print(f'PASS: {len(pages)} HTML pages; {len(canonical_urls)} indexable URLs; sitemap, images, metadata, JSON-LD, internal links and output parity.')
