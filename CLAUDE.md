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

1. **Encabezado:** logo UIFCE en blanco sobre azul institucional, número y fecha de la edición, franja de colores del robot.
2. **Bloque 1 · El Lanzamiento:** el último lanzamiento o novedad de Cursos Libres, con un titular centrado en el beneficio, cifras (cursos, horas, sesiones, áreas), los cursos con sus monitores y un enlace para ver el lanzamiento.
3. **Bloque 2 · Caja de Herramientas:** 2 o 3 apoyos académicos presentados como **habilidades** (qué aprendes, para qué te sirve, temas, formato) y enlazados a su área en el catálogo.
4. **Bloque 3 · Tip de Virtualización:** un consejo breve sobre las aulas virtuales (Moodle). Es un espacio editable.
5. **Cierre:** "¿Tienes alguna pregunta? Comunícate con nosotros", con Uifcito, contacto (✉️ uniic_bog@unal.edu.co · 📞 3165000 Ext. 12301 · 📍 Edificio 310) y pie institucional.

Archivos por edición:
- `edicion-NN.html`: correo.
- `edicion-NN.md`: archivo web.
- `edicion-NN-tv.html`: formato TV, con 6 diapositivas 16:9 de 1920×1080 (portada, lanzamiento, ruta, herramientas, tip y contacto) que se escalan a la pantalla y avanzan cada 12 s. Teclas: ←/→ para moverse, espacio para pausar y F para pantalla completa. Usa rutas relativas a `assets/`.

El correo enlaza a la versión TV en `https://cdiazsu-source.github.io/ET-BoletinUIFCE1/edicion-NN-tv.html`, que requiere GitHub Pages activo.

## Recursos propios (repo `cdiazsu-source/ET-BoletinUIFCE1`)

- `assets/icons/`: logos de software en SVG (originales de los repos fuente) y PNG de 256 px (generados con Edge headless para el correo). Disponibles: excel, python, r, powerbi, sap, qgis, siigo (solo PNG), moodle, linkedin.
- `assets/img/`: uifcito.png, uifcito-cierre.png y logo-uifce-blanco.png.
- **Logo animado en 3D** (sale de la grabación de Blender "LOGO UIFCE BLENDER.mp4", recortada a 1200×600 desde x=190, y=220):
  - `logo-uifce-3d.gif`: 400 px, 8 fps, 32 colores, ~1,5 MB. Va en el encabezado del correo a 280 px.
  - `logo-uifce-3d.mp4`: 960 px, sin audio. Lo usa la portada de la TV.
  - `logo-uifce-3d-poster.jpg`: primer cuadro, se muestra mientras carga el video.
- En el correo, las imágenes se cargan desde `https://raw.githubusercontent.com/cdiazsu-source/ET-BoletinUIFCE1/main/assets/...`. En la versión MD y en la TV se usan rutas relativas.

## Lenguaje de interfaz (UI/UX)

Inspirado en [Konsta UI](https://github.com/konstaui/konsta), [Framework7](https://github.com/framework7io/framework7) y [Vaul](https://github.com/emilkowalski/vaul). No se importan las librerías; se replican sus patrones con HTML y CSS:
- **Listas agrupadas iOS** (Konsta/F7): contenedor blanco con radio de 16 px (correo) o 36 px (TV), filas con un *tile* de ícono redondeado y fondo tonal, título, subtítulo, separador fino y `›` o una píldora a la derecha.
- **Control segmentado** para las cifras: fondo `#E3E8EC` y celdas blancas, con la celda destacada en navy y el número en amarillo.
- **Botones píldora** (`border-radius:999px`): el primario es navy con flecha cian, el secundario es cian con texto oscuro y "VER" es tonal, estilo App Store.
- **Notificación iOS** para el Tip: tile de la app, "MOODLE · ahora", título cian y texto. En la TV aparece sobre una pantalla de bloqueo con los ojos de Uifcito.
- **Hojas Vaul:** cada sección es una hoja con tirador (40×5 px en el correo, 110×12 px en la TV). En la TV la hoja sube con `cubic-bezier(0.32, 0.72, 0, 1)` mientras el fondo se reduce a 0,94 y se oscurece.
- **Toque informático:** etiquetas en monoespaciado (`Consolas/SFMono`), como `uifce://boletin/01`, `01 / El Lanzamiento` o `$ ruta --iniciar --completar` con cursor parpadeante, y `// comentarios`.
- **Ruta de área:** stepper de 3 pasos (01 Inicial, 02 Intermedio, 03 Avanzado) por cada ruta del mapa (`mapa-rutas.html`), con la invitación a iniciar la ruta y completarla toda.

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
