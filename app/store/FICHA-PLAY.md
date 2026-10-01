# Ficha de Google Play — Cripta de los Dados

## Datos básicos
- **Nombre de la app:** Cripta de los Dados
- **ID del paquete:** `io.github.rubenrobles02.cripta` (permanente)
- **Categoría:** Juegos → Rol (o Estrategia)
- **Idioma predeterminado:** Español (España) – es-ES
- **Gratis**, sin anuncios, sin compras en la app
- **Política de privacidad:** https://rubenrobles02.github.io/cripta-de-los-dados/privacidad.html

## Descripción breve (máx. 80)
Tira los dados, cruza puertas y baja hasta el fondo de una cripta sin fin.

## Descripción completa
Bajo el pueblo de Valdeceniza hay una cripta que nadie ha logrado vaciar. Tú tienes tres dados de hueso… y ganas de bajar.

Cripta de los Dados es un roguelike de dados en pixel art:
• Tira tus dados, fija los que te gusten y relanza el resto: espadas, escudos, curas, monedas y Magia.
• Elige puerta en cada piso: combates, élites, tiendas, hogueras, tesoros y eventos.
• Mejora tus dados cara a cara, consigue dados nuevos, bendiciones y reliquias.
• Cuatro mundos con su jefe: la Cripta, la Torre del Archimago, las Forjas Hundidas y el Núcleo del Destino.
• Toca el Núcleo, elige un Pacto que cambia las reglas y vuelve a empezar… más fuerte y más loco.
• Equipo con 25 piezas, 4 calidades y 10 niveles: casco, amuleto, escudo, pechera y botas.
• 6 héroes con habilidades propias y más de 30 enemigos, cada mundo con los suyos.
• 8 skins de dados con efectos propios al atacar.
• Disponible en español e inglés.
• Música chiptune y partidas que se guardan solas: sigue justo donde lo dejaste.

Sin anuncios. Sin conexión. Solo tú, tus dados y la cripta.

## Ficha en inglés (en-US) — añadir en «Traducciones»
**Nombre:** Crypt of the Dice

**Descripción breve (máx. 80):**
Roll the dice, pick your door and descend into an endless crypt.

**Descripción completa:**
Beneath the village of Ashvale lies a crypt no one has ever cleared. You have three bone dice… and a sister to bring back.

Crypt of the Dice is a pixel-art dice roguelike:
• Roll your dice, hold the ones you like and reroll the rest: swords, shields, heals, coins and Magic.
• Choose a door on every floor: fights, elites, shops, campfires, treasure and mysteries.
• Upgrade your dice face by face, and find new dice, blessings and relics.
• Four worlds, each with its boss: the Crypt, the Archmage's Tower, the Sunken Forges and the Core of Fate.
• Touch the Core, choose a Pact that changes the rules, and start again… stronger and wilder.
• Gear with 25 pieces, 4 qualities and 10 levels: helm, amulet, shield, chest and boots.
• 6 heroes with their own abilities and 30+ enemies, each world with its own.
• 8 dice skins with unique attack effects.
• Chiptune music and runs that save themselves: pick up right where you left off.
• Available in English and Spanish.

No ads. No connection needed. Just you, your dice and the crypt.

## Gráficos (en esta carpeta)
- **Icono** 512×512: `icon-512.png`
- **Gráfico de funciones** (el banner de la ficha) 1024×500: `banner-1024x500.png`
- **Capturas de teléfono** (1688×950, 16:9): carpeta `telefono/` (6 capturas)
- **Capturas de tablet de 7"** (1440×900): carpeta `tablet-7/` (6 capturas)
- **Capturas de tablet de 10"** (2560×1600): carpeta `tablet-10/` (6 capturas)
- Para regenerarlas: `node app/capturas.mjs` con el servidor local en marcha (ver cabecera del script).

## Seguridad de los datos (cuestionario)
- ¿Recoge o comparte datos de usuario? **No**
- ¿Los datos se cifran en tránsito? No aplica (no se envía nada)
- ¿Se puede pedir que se eliminen? No aplica (todo es local; desinstalar borra el progreso)

## Clasificación de contenido (IARC)
- Categoría: Juego
- Violencia: fantástica, no realista y sin sangre (monstruos pixel art). Sin contenido sexual, lenguaje soez, drogas, juego con dinero real ni interacción entre usuarios.
- Resultado esperado: PEGI 7 / Para todos 10+ aprox.

## Público objetivo
- Recomendado: 13 años o más (evita los requisitos extra de apps para niños).
- ¿Atrae a niños? No especialmente.

## Otras declaraciones
- Anuncios: **No**
- Acceso a la app: todas las funciones disponibles sin restricciones (no hay inicio de sesión)
- App de noticias / gubernamental / financiera / salud: No
- Identificador de publicidad (Android 13+): **No** se usa

## Beta cerrada (Pruebas → Prueba cerrada)
1. Crea la app en Play Console con el nombre y el idioma de arriba (App · Gratis).
2. Completa en «Panel» → «Configura tu app»: acceso, anuncios, clasificación, público, seguridad de datos, política de privacidad, categoría y ficha (textos + gráficos).
3. Pruebas → Prueba cerrada → Crear canal (o usar «Alpha») → Testers: crea una lista con los correos de tus testers (cuentas Google).
4. Crear versión → acepta **Play App Signing** → sube el `.aab` más reciente de `app/release/` → notas: «Primera beta cerrada».
5. Revisar y publicar en el canal. Google revisa (horas o algunos días). Los testers aceptan desde el enlace de inscripción del canal.

> Cuentas personales nuevas: para pasar a Producción Google exige una prueba cerrada con **al menos 12 testers durante 14 días seguidos**.

## Reclutar testers
- Página: https://rubenrobles02.github.io/cripta-de-los-dados/beta/ (comparte este enlace)
- En Play Console → Prueba cerrada → Testers, elige **Grupos de Google** y pon `sumitesters@googlegroups.com`.
- En el grupo, ajustes → «Quién puede unirse»: **Cualquier usuario de la Web puede unirse**.

## Siguientes versiones
`python release.py` (o `python release.py 0.2.0`) sube el versionCode, compila y deja el .aab en `app/release/`. Súbelo como nueva versión del mismo canal.
