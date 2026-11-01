"""Apply the Pages project prefix after building; custom domains use an empty prefix."""
from pathlib import Path
import os,re
root=Path(__file__).resolve().parents[1]/'dist'
base=os.environ.get('PAGES_BASE_PATH','').rstrip('/')
if base:
    for path in root.rglob('*.html'):
        text=path.read_text()
        text=re.sub(r'((?:href|src)=[\"\'])/(?!/)',lambda m:m[1]+base+'/',text)
        text=text.replace('content="0;url=/','content="0;url='+base+'/')
        path.write_text(text)
print('Pages base path:',base or '/')
