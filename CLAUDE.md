# Cripta de los Dados — guía para Claude

Roguelike de dados en pixel art para móvil, **pensado para jugarse en horizontal**. Todo el juego vive en un solo archivo, `index.html` (unas 3.200 líneas de HTML, CSS y JS sin dependencias, salvo Google Fonts). El usuario habla en español: la interfaz y los textos del juego van en español.

## Cómo trabajar en este repo (ahorro de tokens)

- **No leer `index.html` entero, nunca.** Localiza con `grep -n "<ancla>" index.html` y lee solo el tramo con `Read` usando `offset`/`limit` (30–80 líneas).
- Los cambios grandes se aplican con un script de Python en el scratchpad que hace `rep(viejo, nuevo)` comprobando que el texto aparece **exactamente una vez** (si no, aborta sin escribir). Los cambios pequeños, con `Edit`.
- Tras cada cambio: `node --check` sobre el `<script>` extraído:
  `node -e "const s=require('fs').readFileSync('index.html','utf8');require('fs').writeFileSync(process.env.TEMP+'/c.js',s.match(/<script>([\s\S]*)<\/script>/)[1])" && node --check "$TEMP/c.js"`
- Para verificar en el navegador, **pocas capturas y pequeñas** (scale ≤ 0.6 o zoom a una región). Prefiere comprobaciones con `javascript_tool` que devuelvan texto (existe el elemento, `scrollHeight` vs `clientHeight`…) y simulaciones con Node para la lógica. Las capturas llegaron a gastar el 75% del contexto.

## Publicar

1. `python build.py` → genera `docs/` y `app/www/` (documento completo con `<!doctype>`, viewport y manifiesto) a partir de `index.html`.
2. `git add -A && git commit -m "..." && git push` (rama `main`). Termina los commits con `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
3. Republicar el artefacto con la herramienta Artifact usando `file_path` = `cripta-dados/index.html` y `url` = https://claude.ai/artifact/3dqqA3TPukSjQvm3AgHxK9 (mismo enlace).

- GitHub: https://github.com/rubenrobles02/cripta-de-los-dados (público). Pages: https://rubenrobles02.github.io/cripta-de-los-dados/ desde `main` → `/docs`.
- `index.html` **no lleva** `<!doctype>`, `<html>` ni `<head>` porque el visor de artefactos los añade. No se los pongas.
- Prueba local: `python -m http.server 18931 --bind 127.0.0.1` en segundo plano (el puerto 8765 lo usa otra app del usuario). Un `_test.html` temporal con un `<iframe>` de 844×390 sirve para simular el móvil en horizontal; **bórralo antes de hacer commit**.
- La pestaña de pruebas de Chrome suele estar en segundo plano: `requestAnimationFrame` y las animaciones CSS se congelan y los timers van a 1/s. Para ver el canvas, carga el juego con `srcdoc` e inyecta delante `window.requestAnimationFrame=cb=>{__raf.push(cb)}`, luego avanza a mano con `__raf.splice(0).forEach(cb=>cb(T))`.

## App Android (Google Play)

- Capacitor 8 en `app/` (`appId` **`io.github.rubenrobles02.cripta`**, permanente). `app/www/` y `app/android/app/src/main/assets/public` se generan: no se editan a mano.
- Fuentes locales en `fonts/` (descargadas con `python fonts.py`); `build.py` cambia Google Fonts por `fonts/fonts.css` en `docs/` y `app/www/`, así el juego funciona sin conexión.
- Nativo: `MainActivity.java` (pantalla completa inmersiva + margen para el notch), manifiesto `sensorLandscape`, splash oscuro (`styles.xml`), `SystemBars.insetsHandling=disable`.
- En el juego, `onBack()` (al final del script) gestiona el botón atrás de Android vía `Capacitor.Plugins.App`: cierra capa → pausa → minimiza en la portada.
- **Nueva versión:** `cd app && python release.py [versionName]` → sube `versionCode`, compila y deja `.aab` y `.apk` firmados en `app/release/` (ignorado en git). Si cambias solo el juego, basta con esto.
- Herramientas: JDK 21 y Android SDK 36 en `C:/Users/Gabriel/android-tools` (sin emulador). `android/local.properties` apunta al SDK.
- **Clave de subida:** `C:/Users/Gabriel/cripta-keys/cripta-upload.jks` + `keystore.properties` (copiado a `app/android/`, ignorado en git). Nunca subirla al repo.
- Icono: `python app/icon.py` (pixel art generado). Ficha de Play, gráficos y pasos de la beta: `app/store/` (capturas con `node app/capturas.mjs`). En tablets en horizontal, un script del `<head>` (en `build.py`) fija el viewport a 480px de alto para que se use el diseño horizontal compacto escalado; `MainActivity` activa `setUseWideViewPort` para que el WebView lo respete. Privacidad: `docs/privacidad.html`. Página para reclutar testers: `docs/beta/index.html` (https://rubenrobles02.github.io/cripta-de-los-dados/beta/), enlaza al Google Group https://groups.google.com/g/sumitesters → invitación de prueba de Play → ficha de Play.

## Mapa de `index.html` (busca estas cabeceras con grep)

CSS (arriba, dentro de `<style>`): `pixel frames` (clases `.pf` panel y `.pb` botón con marco pixel), `hud`, `title`, `map`, `combat`, `cards`, `forge`, `overlays`, `dice skins`, `merchant`, `orientation` (reglas de horizontal), `armory / equipment`, `loot modal`, `reward cards`, `title: name and dice…`, `intro story`. Luego hay bloques sueltos (legibilidad, `.wtrack`, `.modes`, `.pacts`, `.lockall`, `.cmp`, `#tip`…). Los estilos nuevos se insertan justo antes de `@media (prefers-reduced-motion: reduce){`.

JS (dentro de `<script>`, en este orden):
- `palette` → `P`, `RAMP` (rampas de 4 colores por tipo) y `RC`.
- `pixel icons` → `ICD` (iconos definidos como trazos SVG que se pasan a píxeles), `icon(nombre, rampa, escala)`.
- `pixel dice` → `SKINS`, `SWORD_PAL`, `swordSprite`, `orbSprite`, `dieGen` y `dieImg(face, cls, skin)`.
- `pixel sprites` → `SPR` (sprites de 16×16 en texto), `PAL_ALT` (cambios de paleta por enemigo) y `procSprite` (escala con EPX a 32 px, añade contorno y sombreado).
- `pixel doors` → `doorURL(tipo, abierta)`, con un diseño propio por tipo de puerta.
- `data` → `TYPES` (caras), `RELICS`, `ENEMIES`, `DOORS`.
- `worlds` → `WORLD_LEN=25`, `WORLDS` (cripta, torre, forja, núcleo) y `worldOf(f)` → `{idx, w, cycle, local}`.
- `storage` → `META` (persistente: `bank` o Tesoro, `skins`, `gear`, `best`, `wins`, `introSeen`) y `saveRun`.
- `equipment` → `GEAR` (25 piezas, `st:L=>stats`), `QUAL` (common, rare, epic, legend), niveles 1–10, `gearTotal()`, modal de la caja (`openLootModal`), `showGear` (arrastrar y soltar), `compareHTML`.
- `sound` / `music` → `SFX` y `TRACKS` (dungeon, tower, forge, core, boss, camp), `setMusic`, `trackFor`.
- `scene engine` → canvas de fondo a baja resolución con luz por dithering, `SCN.{title,hall,crypt,tower,forge,core,shop,rest,treasure,event}`, `drawFoe`, partículas y `goblinPeek` (el goblin de la portada).
- `combat` → `startCombat`, `calc` (suma las caras, rachas, multiplicador de Magia), `roll`, `resolve`, `throwSwords` y `applyPerk` (efecto de las espadas según la skin), `enemyTurn`, `winCombat` (genera la recompensa), `lose`.
- `intro story` → `playStory(paneles, alTerminar, opts)`, `INTRO`, `worldStory()`, `CYCLE_TALES`, `chooseMode`.
- `screens` → `renderTitle`, `renderMap`, `renderReward` (3 cartas que se reparten, reroll de un solo uso), `renderForge` y `renderForgePick`, `renderShop`, `renderRest`, `renderTreasure`, `renderEvent`, `renderEnd`.
- `upgrade cards` → `UPG` (11 mejoras), `genOpts` (mezcla las 3 opciones), `applyUpg`, `dieOp`.
- `hud` → `updateTop` (reliquias, bendiciones y la gema del pacto), `sceneFor`, `render`.

## Estado de la partida `G` (se guarda en `localStorage` como `cripta-run`)

`{mode, screen, hp, maxHp, gold, floor (global, 1..∞), relics[], dice[{faces[{t,v,rar}]}], doors[], combat, reward, shop, event, pending, buffs{}, pact, seen{} (enfriamiento de salas), gearHp, stats}`.
Tipos de cara: `atk`, `def`, `heal`, `crit` (se muestra como «Magia»: lanza un orbe y duplica el ataque), `coin`, `blank`.

## Sistemas clave

- **Mundos:** 25 pisos cada uno. Cripta (Azhrak) → Torre (Malakar) → Forjas Hundidas (Brokk) → Núcleo del Destino (El Tahúr). Al vencer al Tahúr hay historia y se eligen 1 de 3 **pactos** (`PACTS`: blood, gold, fury, luck, iron, echo), que cambian las reglas de todo el ciclo. Luego se vuelve a la Cripta con el ciclo +1.
- **Puertas:** `genDoors` con enfriamiento por tipo (`COOL`). El último piso de cada mundo es el jefe; el penúltimo, hoguera y tienda.
- **Recompensas:** caja de equipo (`BOX_CHANCE=1`, provisional para pruebas) y después 3 cartas: caras, dado nuevo, bendición (`BLESS`/`BUFFK`, duran la siguiente pelea) o mejora (`UPG`).
- **Skins:** 8, compradas con el Tesoro. Cada una cambia el aspecto de los dados, las partículas y el efecto de las espadas al atacar.
- **Economía:** al morir, `bankRun` ingresa en el Tesoro el oro restante + 15 por piso + 8 por enemigo. La Armería tiene un botón «+1000 (pruebas)».

## Preferencias del usuario

- **Horizontal primero.** Comprueba los diseños a 844×390 antes que en vertical.
- Que quepa en pantalla si se puede, pero **legible antes que diminuto**: mejor scroll que letra pequeña.
- Estética pixel coherente en todo (marcos `.pf`/`.pb`, sin degradados genéricos de IA). La fuente gótica (Jacquarda) solo para títulos grandes. Las cifras usan Silkscreen (cargada solo con dígitos) para que no se confundan.
- Los avisos (`toast`) salen arriba y no bloquean toques.

## Pendiente / ideas acordadas

- Modo **Campaña** (en el menú como «Próximamente»): por capítulos, con mecánicas distintas.
- Sistema de **niveles/experiencia** (el desmantelado de equipo debería dar también experiencia).
- Bajar `BOX_CHANCE` cuando termine la fase de pruebas.
- Equilibrar la dificultad de los mundos 3–4 y de las piezas legendarias con partidas reales.
