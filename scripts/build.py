"""Copy the public site to dist without exposing scripts or private documents."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ('index.html', '404.html', 'robots.txt', 'sitemap.xml', 'CNAME', 'assets', 'learn', 'about')

def build():
    output = ROOT / 'dist'
    output.mkdir(exist_ok=True)
    for name in PUBLIC:
        source = ROOT / name
        target = output / name
        if source.is_dir():
            shutil.copytree(source, target, dirs_exist_ok=True)
        else:
            shutil.copy2(source, target)
    print('Public site copied to dist.')

if __name__ == '__main__':
    build()
