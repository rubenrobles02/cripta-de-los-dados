# Cripta de los Dados

Roguelike de dados en pixel art para móvil (pensado para jugarse en horizontal). Tira, fija y relanza tus dados para bajar diez pisos de cripta y derrotar a Azhrak.

**Jugar:** https://rubenrobles02.github.io/cripta-de-los-dados/

## Estructura

- `index.html`: el juego completo en un solo archivo (HTML, CSS y JS). No lleva `<!doctype>` ni `<head>` porque también se publica como artefacto de claude.ai, que los añade.
- `build.py`: genera `docs/index.html`, la versión completa que sirve GitHub Pages.
- `docs/`: carpeta publicada en GitHub Pages.

## Publicar cambios

```sh
python build.py
git add -A
git commit -m "Describe el cambio"
git push
```

GitHub Pages se actualiza solo a los pocos minutos del `push`.

## App Android

Proyecto Capacitor en `app/`. Para generar el `.aab` (Google Play) y el `.apk` firmados:

```
cd app
npm install
python release.py          # o: python release.py 0.2.0
```

Necesita JDK 21, Android SDK 36 y `app/android/keystore.properties` (ver `keystore.properties.example`). Ficha y gráficos de Play en `app/store/`.
