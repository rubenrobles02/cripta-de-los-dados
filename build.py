"""Genera docs/index.html (documento completo para GitHub Pages) a partir de index.html.

index.html es la fuente: no lleva <!doctype>, <html> ni <head> porque el visor de
artefactos de claude.ai los añade. Este script los añade para publicarlo como web normal.
Uso: python build.py
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'index.html')
OUT_DIR = os.path.join(ROOT, 'docs')

src = open(SRC, encoding='utf-8').read()
split = src.find('<canvas id="bg">')
if split < 0:
    raise SystemExit('No encuentro <canvas id="bg"> en index.html')
head, body = src[:split], src[split:]
head = head.replace('<meta charset="utf-8">', '').strip()

page = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body.strip()}
</body>
</html>
"""

manifest = {
    'name': 'Cripta de los Dados',
    'short_name': 'Cripta',
    'start_url': './',
    'display': 'fullscreen',
    'orientation': 'landscape',
    'background_color': '#0b0a12',
    'theme_color': '#0b0a12',
}

os.makedirs(OUT_DIR, exist_ok=True)
open(os.path.join(OUT_DIR, 'index.html'), 'w', encoding='utf-8').write(page)
open(os.path.join(OUT_DIR, 'manifest.webmanifest'), 'w', encoding='utf-8').write(json.dumps(manifest, ensure_ascii=False, indent=2))
open(os.path.join(OUT_DIR, '.nojekyll'), 'w').close()
print('docs/index.html generado')
