"""Descarga las fuentes de Google Fonts a fonts/ para que la app Android funcione sin conexión.

Solo hace falta ejecutarlo si cambian las fuentes del <head> de index.html.
Uso: python fonts.py
"""
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'fonts')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
SUBSETS = ('latin', 'latin-ext')

src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
urls = [u.replace('&amp;', '&') for u in re.findall(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)"', src)]


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA})).read()


os.makedirs(OUT, exist_ok=True)
css_out, files = [], {}
for url in urls:
    css = get(url).decode('utf-8')
    for comment, block in re.findall(r'(?:/\* ([\w-]+) \*/\s*)?(@font-face\s*\{[^}]*\})', css):
        if comment and comment not in SUBSETS:
            continue
        family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
        furl = re.search(r'url\(([^)]+)\)', block).group(1)
        if furl not in files:
            name = re.sub(r'\W+', '-', family).lower() + f'-{len(files)}.woff2'
            open(os.path.join(OUT, name), 'wb').write(get(furl))
            files[furl] = name
        css_out.append(block.replace(furl, files[furl]))

open(os.path.join(OUT, 'fonts.css'), 'w', encoding='utf-8').write('\n'.join(css_out) + '\n')
print(f'{len(files)} fuentes en fonts/, {len(css_out)} reglas @font-face')
