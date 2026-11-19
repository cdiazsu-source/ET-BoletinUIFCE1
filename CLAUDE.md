# Boletín UIFCE

Boletín de la **UIFCE (Unidad de Informática de la Facultad de Ciencias Económicas, UNAL Bogotá)** que da visibilidad a los cursos libres, los apoyos académicos y la virtualización. Se publica por correo (HTML) y como archivo web (Markdown).

## Fuentes (insumos)

| Insumo | Sitio publicado | Repositorio |
|---|---|---|
| Oferta de Cursos Libres | https://cdiazsu-source.github.io/2026-2s-ET-OfertaCursosLibres/ | https://github.com/cdiazsu-source/2026-2s-ET-OfertaCursosLibres |
| Apoyos Académicos | https://cdiazsu-source.github.io/2026-2s-ET-ApoyosAcademicos/ | https://github.com/cdiazsu-source/2026-2s-ET-ApoyosAcademicos |

Dónde está cada dato:
- **Cursos libres:** `index.html` (hub de lanzamientos), `lanzamiento-primer|segundo|especial.html` (cursos, horas y monitores), `curso-*.html` (páginas de detalle). El historial de git (`/commits`) indica cuál es la novedad más reciente. Aplicativo de seguimiento y certificados: https://fce.unal.edu.co/cursos-libres-uifce/
- **Apoyos académicos:** `software.js` (objeto `SW` con nombre, área, descripción, temas, sesiones sugeridas y aporte a las asignaturas de cada software), `catalogo.html` (se filtra por área con `#<Área>` en la URL), `solicitar.html` (proceso).
- Los repos son públicos: se leen con `curl` a `api.github.com` / `raw.githubusercontent.com` (el `gh` local no está autenticado).

## Estructura de cada edición

Formato de **boletín institucional** (cercano al Boletín SIUN de la UNAL, sin calcarlo):
1. **Línea de temas** arriba (como un asunto: "Tema A / Tema B / …") y enlace "📺 Ver en TV".
2. **Encabezado:** logo UIFCE estático en negro sobre blanco a la izquierda, y a la derecha una franja navy con "Boletín UIFCE" y "Edición #NN · Mes AAAA" (sin rutas tipo `uifce://…`). Debajo va la franja de colores del robot.
3. **Saludo de Uifcito** (una línea).
4. **Secciones por servicio**, con una barra gris `#E3E8EC` y el número en monoespaciado (`01 /`): Cursos Libres, Apoyos Académicos y Aulas Virtuales.
5. **Noticias:** cada una con imagen de 200 px (tile con logos o un visual) y texto (etiqueta, titular `#005E6F`, 1 o 2 frases y un enlace "… →"). La imagen se alterna entre izquierda y derecha con `dir="rtl"`, y el fondo entre crema `#FCFAEE` y blanco. En celular las columnas se apilan (`.col`).
   - Cursos Libres: lanzamiento, ruta de área ("Inicia tu ruta de área y complétala toda") y certificado en LinkedIn.
   - Apoyos Académicos: 2 o 3 herramientas presentadas como habilidades.
   - Aulas Virtuales · "Moodle sin enredos" (espacio editable): una notificación de entrada y una lista de **4 ajustes concretos**, cada uno con título, ruta del menú en monoespaciado (`Área personal → Línea de tiempo`) y una línea de beneficio. Al final va la nota "los nombres de los menús pueden variar según la versión".
   - **Radar TI · Noticias del mundo:** de 1 a 3 noticias informáticas recientes (la principal a todo el ancho y las demás con imagen y texto alternados) y verificadas en su fuente original, ojalá conectada con los cursos (p. ej., el índice TIOBE). Cada noticia lleva **una foto real de internet con licencia que permita reutilizarla** (Wikimedia Commons con CC BY / CC BY-SA / dominio público, o kits de prensa oficiales), guardada como JPG de 800×560 en `assets/img/foto-*.jpg`. Debajo va el crédito breve: "Foto: Autor, licencia vía Wikimedia Commons (recortada)", con enlace a la ficha. Si el usuario entrega una foto de prensa, se usa la que él aporte con su crédito ("Foto: Medio/Fotógrafo"); en ese caso, el permiso de uso lo gestiona el usuario. Por iniciativa propia no se copian fotos de periódicos o agencias (AP, Reuters, Getty…). Si no hay foto libre, se hace una gráfica propia con los datos (HTML renderizado con Edge headless, `assets/img/noticia-*.png`), como la del índice TIOBE, cuyo uso se permite citando www.tiobe.com. Con noticias sobre personas se usa un tono neutro: hechos confirmados (de preferencia documentos oficiales, como un 8-K), sin detalles de su vida personal; si se usa su foto, debe tener licencia libre.
6. **Contacto:** "¿Tienes alguna pregunta? Comunícate con nosotros" con Uifcito (✉️ uniic_bog@unal.edu.co · 📞 3165000 Ext. 12301 · 📍 Edificio 310).
7. **Pie navy** con el logo estático en blanco y los enlaces.

Archivos por edición:
- `edicion-NN.html`: correo.
- `edicion-NN.md`: archivo web.
- `edicion-NN-tv.html`: formato TV de 1920×1080 que se escala a la pantalla, con **el mismo formato de boletín del correo**. Tiene encabezado fijo (logo estático negro sobre blanco, franja navy y contador `N / total`), franja del robot y una barra de sección que cambia en cada diapositiva (`01 / Cursos Libres`…, con sus temas a la derecha). Las noticias van con imagen y texto alternados sobre crema y blanco, y abajo un pie navy con el logo en blanco. Son 8 diapositivas que avanzan cada 12 s: sumario con Uifcito, lanzamiento, ruta + LinkedIn, SAP/QGIS/Siigo, Moodle (4 ajustes), Radar TI (TIOBE), Radar TI (otras noticias) y contacto. Teclas: ←/→ para moverse, espacio para pausar y F para pantalla completa. `#s=N` abre en la diapositiva N y `#s=N&pausa` la deja fija. Usa rutas relativas a `assets/`.

Publicación en **GitHub Pages** (rama `main`, raíz), activo desde el 18 nov 2026: `https://cdiazsu-source.github.io/ET-BoletinUIFCE1/`.
- `index.html` es la portada con la lista de ediciones. Con cada edición nueva se agrega su tarjeta, con botones a la web, la TV y el Markdown.
- `.nojekyll` evita que Jekyll convierta `edicion-NN.md` en `edicion-NN.html` y choque con el correo.
- El correo enlaza a la TV en `…/edicion-NN-tv.html`.

## Recursos propios (repo `cdiazsu-source/ET-BoletinUIFCE1`)

- `assets/icons/`: logos de software en SVG (originales de los repos fuente) y PNG de 256 px (generados con Edge headless para el correo). Disponibles: excel, python, r, powerbi, sap, qgis, siigo (solo PNG), moodle, linkedin.
- `assets/img/`: uifcito.png, uifcito-cierre.png y el **logo oficial estático**: `logo-uifce-static-negro.png` (correo y MD) y `logo-uifce-static-blanco.png` (pie del correo y portada de la TV), ambos de 1200×530 con fondo transparente. No se usa logo animado.
- En el correo, las imágenes se cargan desde `https://raw.githubusercontent.com/cdiazsu-source/ET-BoletinUIFCE1/main/assets/...`. En la versión MD y en la TV se usan rutas relativas.

## Lenguaje de interfaz (UI/UX)

Inspirado en [Konsta UI](https://github.com/konstaui/konsta), [Framework7](https://github.com/framework7io/framework7) y [Vaul](https://github.com/emilkowalski/vaul). No se importan las librerías; se replican sus patrones con HTML y CSS:
- **Listas agrupadas iOS** (Konsta/F7): contenedor blanco con radio de 16 px (correo) o 36 px (TV), filas con un *tile* de ícono redondeado y fondo tonal, título, subtítulo, separador fino y `›` o una píldora a la derecha.
- **Control segmentado** para las cifras: fondo `#E3E8EC` y celdas blancas, con la celda destacada en navy y el número en amarillo.
- **Botones píldora** (`border-radius:999px`): el primario es navy con flecha cian, el secundario es cian con texto oscuro y "VER" es tonal, estilo App Store.
- **Notificación iOS** para el Tip: tile de la app, "MOODLE · ahora", título cian y texto. En la TV aparece sobre una pantalla de bloqueo con los ojos de Uifcito.
- **Hojas Vaul:** cada sección es una hoja con tirador (40×5 px en el correo, 110×12 px en la TV). En la TV la hoja sube con `cubic-bezier(0.32, 0.72, 0, 1)` mientras el fondo se reduce a 0,94 y se oscurece.
- **Toque informático:** etiquetas en monoespaciado (`Consolas/SFMono`), como `01 / El Lanzamiento` y `// comentarios`. No usar rutas tipo `uifce://boletin/01`. No usar comandos de terminal tipo `$ ruta --completar` (confunden al lector): los títulos van en lenguaje claro, como "Tu ruta de área".
- **Ruta de área:** stepper de 3 pasos (01 Inicial, 02 Intermedio, 03 Avanzado) por cada ruta del mapa (`mapa-rutas.html`), con la invitación a iniciar la ruta y completarla toda.

## Íconos de software

Los logos son grandes para que llamen la atención. En el correo, los tiles miden 176×130 px (SAP 116 px, QGIS 96 px, Siigo 136 px y LinkedIn 88 px de ancho) y el tile de cuatro logos del lanzamiento usa 76 px por logo. En la TV, ese tile mide 580 px con logos de 220 px, y los tiles de apoyos miden 380×212 px. En el sumario de la TV, el número de sección aparece una sola vez por grupo (`01` y luego una línea cian para las otras noticias del mismo número).

## Propuestas de paleta (solo web)

Arriba del correo (solo en la versión web, porque va oculto y aparece con JavaScript) y en la TV (al mover el mouse) hay botones para cambiar de paleta. También se puede abrir con `#p=a`, `#p=b` o `#p=c` en la URL.
- **Original:** navy `#003241`, cian `#3ED3FF`, amarillo y crema del robot.
- **Propuesta A · Azul cartelera:** `#00005C` + azul Docencia `#17A9EA` + amarillo Gestión `#F6C21D`, con fondos azul claro.
- **Propuesta B · Teal UIFCE:** teal `#005E6F` + amarillo Gestión `#F6C21D` + verde Investigación `#10A35A`, con fondos verde agua.
- **Propuesta C · Manual UIFCE** (manual de identidad, sección 05): azul oscuro `#000066` (base y texto fuerte), azul medio `#1D1DA5` (titulares y enlaces), lila `#6666FF` (acentos sobre blanco), amarillo `#FFFF00` solo como acento sobre azul (nunca texto sobre blanco), lienzo `#F5F5FF`, tinte `#E6E6FF` y texto secundario `#4D4D94`. El azul vibrante `#0000FF` no se usa en la interfaz. En la TV, el encabezado, el pie y el stepper llevan un degradado de `#000066` a `#1D1DA5`.
En el correo, el script cambia los hex de los estilos inline con un mapa de colores; en la TV, cambia las variables CSS con `html[data-p]`. Los ojos del robot siempre son `#3ED3FF`. Cuando se elija una paleta, se aplica directamente en los estilos y se quita el selector.

## Densidad visual

Poco texto y mucha imagen: logos, cifras grandes, etiquetas ("pills") y frases de una línea. Cada tarjeta lleva como máximo un titular, una frase y dos o tres etiquetas.

## Enfoque editorial

- **Mostrar lo que se hizo, no promover inscripciones.** No mencionar estados ("en curso", "finalizado", "inscripciones abiertas/cerradas", "cupos") ni poner botones de inscripción o de formularios de solicitud. Los llamados a la acción llevan a **conocer** (ver el lanzamiento, ver el catálogo, emitir el certificado).

## Guía de estilo y tono

- Tono **cercano**: se tutea y se habla directo a estudiantes y docentes.
- El foco es la **productividad académica y la empleabilidad**: qué puedes hacer con esto, cómo se ve en tu hoja de vida y en tu perfil de LinkedIn.
- Nada de lenguaje administrativo acartonado: evitar "se informa a la comunidad", "en atención a", "de conformidad con", "trámite", "diligenciar" (mejor "llenar").
- Frases cortas, verbos de acción y titulares que dicen el beneficio ("Aprende a…", "Convierte…", "Lleva tus datos a…").
- Usar cifras concretas (horas, sesiones, número de cursos).

## Identidad visual

- **Mascota:** Uifcito, el robot de la UIFCE.
  - Imagen de saludo: `https://cdiazsu-source.github.io/2026-2s-ET-ApoyosAcademicos/assets/uifcito.png` (320×540, se asoma desde la izquierda).
  - Imagen de cierre: `https://cdiazsu-source.github.io/2026-2s-ET-OfertaCursosLibres/assets/uifcito-cierre.png` (298×380).
- **Línea de colores del robot:**
  - Pantalla `#000000`
  - Ojos y franja `#3ED3FF`
  - Cuerpo `#F0EBC8`
  - Sombra del cuerpo `#CFC9A0`
  - Botón `#F5C400`
  - Contorno `#2B2B38`
- **Marca institucional:**
  - Título `#003241`
  - Subtítulo `#005E6F`
  - Texto `#262626`
  - Fondo `#F6F6F6`
  - Tarjeta `#FAFAFA`
  - Azul cartelera `#00005C`
- **Colores por área de Apoyos:**
  - Gestión `#F6C21D`
  - Investigación `#10A35A`
  - Análisis `#F07A3B`
  - Docencia `#17A9EA`
  - Econometría `#E3243F`
- **Logo en blanco:** `https://cdiazsu-source.github.io/2026-2s-ET-ApoyosAcademicos/identidad/logotipo-unidad-informatica-blanco.png`
- **Tipografía:** Ancizar Sans, con respaldo `Arial, Helvetica, sans-serif`.

## Reglas técnicas del HTML de correo

- Una sola columna de 600 px máximo, maquetada con `<table>`, con **todos los estilos inline** (el `<style>` del `<head>` solo sirve como refuerzo responsive).
- Imágenes **solo PNG o JPG** con URL absoluta (Gmail no muestra SVG), con `alt`, `width` y `display:block`.
- Botones hechos con `<a>` dentro de una celda con color de fondo (los "bulletproof buttons").
- Incluir texto de vista previa (preheader) oculto.
