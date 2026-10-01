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
Bajo el pueblo de Valdecenizas hay una cripta que nadie ha logrado vaciar. Tú tienes tres dados de hueso… y ganas de bajar.

Cripta de los Dados es un roguelike de dados en pixel art:
• Tira tus dados, fija los que te gusten y relanza el resto: espadas, escudos, curas, monedas y Magia.
• Elige puerta en cada piso: combates, élites, tiendas, hogueras, tesoros y eventos.
• Mejora tus dados cara a cara, consigue dados nuevos, bendiciones y reliquias.
• Cuatro mundos con su jefe: la Cripta, la Torre del Archimago, las Forjas Hundidas y el Núcleo del Destino.
• Toca el Núcleo, elige un Pacto que cambia las reglas y vuelve a empezar… más fuerte y más loco.
• Equipo con 25 piezas, 4 calidades y 10 niveles: casco, amuleto, escudo, pechera y botas.
• 8 skins de dados con efectos propios al atacar.
• Música chiptune y partidas que se guardan solas: sigue justo donde lo dejaste.

Sin anuncios. Sin conexión. Solo tú, tus dados y la cripta.

## Gráficos (en esta carpeta)
- Icono 512×512: `icon-512.png`
- Gráfico de funciones 1024×500: `feature-1024x500.png`
- Capturas de teléfono (horizontal, 1688×950): `captura-1-portada.png` … `captura-5-tirada.png` (mínimo 2)

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
4. Crear versión → acepta **Play App Signing** → sube `release/cripta-0.1.0-1.aab` → notas: «Primera beta cerrada».
5. Revisar y publicar en el canal. Google revisa (horas o algunos días). Los testers aceptan desde el enlace de inscripción del canal.

> Cuentas personales nuevas: para pasar a Producción Google exige una prueba cerrada con **al menos 12 testers durante 14 días seguidos**.

## Siguientes versiones
`python release.py` (o `python release.py 0.2.0`) sube el versionCode, compila y deja el .aab en `app/release/`. Súbelo como nueva versión del mismo canal.
