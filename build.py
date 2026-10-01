"""Genera las versiones publicables a partir de index.html.

index.html es la fuente: no lleva <!doctype>, <html> ni <head> porque el visor de
artefactos de claude.ai los añade. Este script los añade y cambia Google Fonts por
las fuentes locales de fonts/ (descargadas con fonts.py) para que funcione sin conexión.

  docs/      -> GitHub Pages
  app/www/   -> la app Android (Capacitor). Después: cd app && npx cap sync android

Uso: python build.py
"""
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'index.html')
FONTS = os.path.join(ROOT, 'fonts')

src = open(SRC, encoding='utf-8').read()
split = src.find('<canvas id="bg">')
if split < 0:
    raise SystemExit('No encuentro <canvas id="bg"> en index.html')
head, body = src[:split], src[split:]
head = head.replace('<meta charset="utf-8">', '')
head = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', head)
head, n = re.subn(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]+">\s*', '', head)
if not n:
    raise SystemExit('No encuentro los <link> de Google Fonts en index.html')
head = '<link rel="stylesheet" href="fonts/fonts.css">\n' + head.strip()


def page(extra_head):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">
{extra_head}
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}[hidden]{{display:none!important}}html,body{{overscroll-behavior:none;-webkit-tap-highlight-color:transparent;-webkit-user-select:none;user-select:none}}</style>
{head}
</head>
<body>
{body.strip()}
</body>
</html>
"""


def write(out_dir, html):
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(html)
    shutil.copytree(FONTS, os.path.join(out_dir, 'fonts'), dirs_exist_ok=True)


web_head = """<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">"""
docs = os.path.join(ROOT, 'docs')
write(docs, page(web_head))
manifest = {
    'name': 'Cripta de los Dados',
    'short_name': 'Cripta',
    'start_url': './',
    'display': 'fullscreen',
    'orientation': 'landscape',
    'background_color': '#0b0a12',
    'theme_color': '#0b0a12',
}
open(os.path.join(docs, 'manifest.webmanifest'), 'w', encoding='utf-8').write(json.dumps(manifest, ensure_ascii=False, indent=2))
open(os.path.join(docs, '.nojekyll'), 'w').close()

write(os.path.join(ROOT, 'app', 'www'), page(''))
print('docs/ y app/www/ generados')
