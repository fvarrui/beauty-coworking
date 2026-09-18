---
description: Regenera la presentación web (docs/) a partir de todo lo recopilado en negocio/ y plan-negocio/
---

Regenera por completo el sitio de `docs/` (portada `index.html` + una página por sección en `sections/`), siguiendo estas reglas. Este comando **sustituye** al antiguo `/summary` — ya no se genera `resumen.md`; el entregable para la propietaria es siempre esta presentación web.

Las unidades de contenido se llaman **secciones**, no "capítulos" — etiquétalas siempre como "Sección 01", "Sección 02"... (breadcrumb, tarjetas de portada, sidebar), y la carpeta técnica que las contiene se llama `sections/`.

## 0. Antes de nada

- **Lee todo `negocio/` y `plan-negocio/` de cero**, fichero a fichero. No te bases en el estado anterior de la presentación ni en memoria de conversación: el sitio debe reflejar exactamente lo que dicen esos documentos ahora mismo, incluyendo qué está resuelto y qué sigue pendiente.
- **No inventes datos.** Si algo sigue sin confirmar en `pendientes.md` o en cualquier otro documento, refléjalo explícitamente como pendiente en la presentación — nunca rellenes el hueco con una suposición.
- **Nunca uses el nombre real de la propietaria** ni de ninguna otra persona del salón — llámalas por su rol ("la propietaria", "la profesional de pedicura", "quien ocupe el Cubículo 2", etc.), nunca por parentesco ni por nombre propio. El sitio se publica en GitHub.

## 1. Formato y sistema visual — mantén el existente, no lo reinventes

El sitio ya tiene un sistema de diseño (estilo Docusaurus: navbar superior, sidebar de secciones a la izquierda, contenido central, "En esta página" a la derecha, paginación anterior/siguiente, modo claro/oscuro, responsive, con letra legible). Reutiliza:

- `docs/assets/style.css` — hoja de estilos compartida. Amplíala si necesitas una clase nueva para algo que no exista todavía, pero no rehagas la paleta ni la tipografía sin que te lo pidan explícitamente.
- `docs/assets/app.js` — toggle de tema + menú móvil.
- Un icono (emoji) por sección, coherente con su contenido, visible en el sidebar, en la tarjeta de portada y en el título de la página.

Si `docs/` no existe todavía o está vacío, créalo siguiendo esta misma estructura desde cero.

### El sitio no se escribe a mano: se genera con `docs-src/gen.py`

**No edites los ficheros de `docs/` directamente** — son salida generada y cualquier cambio a mano se pierde en la siguiente regeneración. El flujo es:

1. **Escribe el contenido** de cada sección en `docs-src/bodies/NN.html` (`00.html` es la portada). Esos ficheros llevan **solo el cuerpo**: nada de `<html>`, `<head>`, navbar, sidebar, paginación ni `<h1>` — de eso se encarga la plantilla.
2. **Ajusta los metadatos** en la lista `SECTIONS` de `docs-src/gen.py` si cambian el número, el orden, el icono, el título, la entradilla, el texto de la tarjeta de portada o los ficheros fuente que se citan al final de cada sección.
3. **Ejecuta `python docs-src/gen.py`**, que reescribe `docs/` por completo y borra las páginas de secciones que ya no correspondan.

Esto te ahorra repetir catorce veces el armazón del sitio y garantiza que el pie, la paginación y el sidebar sean idénticos en todas las páginas. El índice lateral de cada sección **se construye solo** con los `<h2 id="...">` del cuerpo: pon un `id` a cada `<h2>` y aparecerá en él.

Detalle completo del reparto de responsabilidades, y los detalles de Mermaid que conviene no romper, en [`docs-src/README.md`](../../docs-src/README.md).

### Pie de página con la marca de generación — obligatorio en todas las páginas

**Todas** las páginas del portal —la portada `index.html` y cada página de `sections/`, sin excepción— terminan con un pie que dice cuándo se generó lo que se está leyendo:

```html
      <footer class="site-footer">
        Generado el <time datetime="AAAA-MM-DDTHH:MM:SS+01:00">D de MES de AAAA a las HH:MM</time> (hora de Canarias)
      </footer>
```

**De esto se encarga la plantilla de `docs-src/gen.py`, no tú**: no escribas el pie en ningún `bodies/NN.html`, porque saldría duplicado. Lo que sí debes respetar si algún día tocas la plantilla:

- La fecha y la hora son las del **momento real de la ejecución** del generador, nunca copiadas de la versión anterior ni deducidas de memoria. Todas las páginas de una misma regeneración llevan exactamente la misma marca.
- El texto visible va en español natural ("18 de septiembre de 2026 a las 17:47"). El atributo `datetime` va en ISO 8601 con el desfase escrito con dos puntos (`+01:00`), que es lo que exige HTML — `+0100` no es válido.
- La zona horaria es la de Canarias: **UTC+1 en horario de verano** (finales de marzo a finales de octubre) y **UTC+0 en invierno**. El generador ya lo ajusta según el mes.
- El estilo `.site-footer` ya existe en `docs/assets/style.css` — reutilízalo, no crees otra clase para lo mismo.
- Si añades una página nueva al portal, lleva su pie igual que las demás: el pie no es decoración de la portada, es la marca de cuándo se generó lo que se está leyendo.

## 2. Diagramas — solo si aportan, y en Mermaid

**No añadas un diagrama porque "queda bien" o porque la sección lo admite.** Antes de meter uno, pregúntate si una tabla, una lista o un párrafo ya cuentan lo mismo igual de claro — si es así, no hace falta diagrama. Un diagrama se justifica cuando muestra una **relación, un flujo o una estructura** que en prosa cuesta seguir (quién depende de quién, un proceso con pasos, un antes/después, una distribución de partes sobre un total). Ejemplos que sí aportan: organigrama de gestión (sección 2), transición antes/después del modelo (sección 2), reparto de ingresos por espacio (sección 4). Ejemplo que **no** aporta y no debe repetirse: un diagrama de "planta del local" a base de cajas conectadas — no representa la disposición real del espacio (Mermaid no dibuja planos) y la tabla de "quién ocupa qué espacio hoy" ya da esa misma información mejor. Tampoco fuerces un diagrama para una simple línea temporal de pasos si un `.step-row`/`.badge-step` numerado con enlaces a cada sección relevante queda más claro (ver "Próximos pasos").

Cuando un diagrama sí esté justificado, constrúyelo con **Mermaid**, no con divs de CSS a medida:

- Carga Mermaid vía CDN (`<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js">` o cdnjs) una vez por página que lo necesite, e inicialízalo con `mermaid.initialize({ startOnLoad: true, theme: ... })`. Ajusta el tema de Mermaid (claro/oscuro) al `data-theme` activo de la página para que combine con el resto del sitio. No incluyas el script de Mermaid en páginas sin ningún diagrama.
- Prioriza que cada diagrama se entienda de un vistazo: etiquetas cortas y claras, sin abarrotar, con el precio/estado como parte de la etiqueta cuando aporte información (p. ej. "Salón central — 300 €/mes — ocupado").
- Los datos en €/estado que aparezcan en KPIs sueltos (no relacionales) van como bloques HTML/CSS normales (`.kpi-row`, tablas, etc.), nunca como diagrama.
- **Gráficos de tipo `pie`**: la directiva `title` de Mermaid se corta por la izquierda en este layout (el título se centra sobre el círculo, no sobre el ancho total con leyenda, y el contenedor lo recorta) — no la uses; pon el título como texto HTML normal (`<p class="mermaid-caption">...</p>`) justo antes del `.mermaid-wrap`. Define también los colores de las porciones en `themeVariables` (`pie1`, `pie2`, `pie3`..., más `pieStrokeColor`, `pieSectionTextColor`, `pieLegendTextColor`) para que combinen con la paleta del sitio en vez de usar los grises por defecto de Mermaid — usa una rampa de 2-3 tonos de `--primary`/`--primary-dark`. ⚠️ Mermaid ordena las porciones **alfabéticamente por etiqueta**, no por el orden en que las declaras en el código ni por su valor — no cuentes con `pie1`/`pie2`/`pie3` para dar significado a una porción en concreto (p. ej. "la real" vs "las objetivo"), porque qué etiqueta cae en cada color depende del texto exacto y puede cambiar si renombras algo.

## 3. Nivel de detalle — denso, no un resumen

A diferencia del antiguo resumen de una página, esta presentación debe **incluir bastantes detalles y explicaciones**, no condensarlo todo a una frase por idea. Para cada apartado:

- Explica el "por qué", no solo el "qué": si algo es viable o no, di la razón legal/práctica concreta, no solo el semáforo.
- Cuando un documento fuente tenga una tabla, una lista de fuentes o una comparación, tradúcela a la presentación con ese mismo nivel de detalle (no la resumas a una línea).
- Cuando haya varias opciones o casos analizados (candidatos de servicio, casos reales, ayudas públicas, canales de captación de inquilinas...), preséntalos todos, no solo los 2-3 más destacados.
- Mantén el estilo claro y bien estructurado (encabezados, listas, tablas, callouts para avisos/riesgos) para que la densidad de información no se sienta como un muro de texto.

## 4. Lenguaje claro y directo

Especialmente en las "Decisiones pendientes" y en cualquier lista de preguntas para la propietaria: formula cada punto como una **pregunta directa y completa**, no como un fragmento nominal ("Superficie, planos y equipamiento de cada espacio" no es una pregunta). Una propietaria sin formación técnica ni de gestión debe poder leer la pregunta y saber exactamente qué se le está pidiendo, sin tener que interpretarla. Este mismo criterio (claro, directo, sin jerga sin explicar) aplica a toda la presentación, no solo a esa sección.

## 5. Referencias — todo debe poder contrastarse

Cada sección debe permitir comprobar de dónde sale la información, con enlaces reales (nunca inventados):

- **Al final de cada sección** (o de cada bloque `<h2>` cuando el contenido de la sección mezcla temas distintos, como en "Decisiones pendientes"), añade un bloque `<div class="sources">` con enlaces a los ficheros fuente en GitHub: `https://github.com/fvarrui/beauty-coworking/blob/main/negocio/<fichero>.md` (o `plan-negocio/<fichero>.md`). Usa un `<span class="sep">·</span>` entre enlaces cuando haya varios.
- **Enlaza en línea** los nombres de operadores, anuncios, estudios o fuentes externas citadas (p. ej. "Alzentro", "Sola Salon Studios", "foro de BeautyMarket") directamente a su URL real, tal como aparece citada en el `.md` de origen (`casos-reales-coworking.md` y `propuesta-oferta-coworking.md` llevan las URLs primarias). No cites una fuente sin enlazarla si el `.md` de origen ya tiene el enlace.
- Nunca inventes una URL ni una cifra de fuente para "completar" una referencia — si el dato no tiene fuente en `negocio/`, dilo como hueco de información en vez de fabricar una.

## 6. Nivel de confianza — no publiques más seguridad de la que hay

Las referencias (sección 5) dicen **de dónde** sale un dato. Esta sección va de **cuánto te puedes fiar de él**, que es una cosa distinta y la que más fácilmente se pierde al pasar de los `.md` a la web.

- **Conserva las marcas de incertidumbre del documento de origen.** Si un `.md` de `negocio/` o `plan-negocio/` marca una afirmación como "fuente única", "sin segunda fuente", "no verificado", "pendiente de confirmar" o con ⚠️, la presentación debe llevar esa misma marca, pegada a la afirmación y no escondida en un bloque de fuentes al final. Usa `<span class="tag">` o un `<div class="callout warn">` para que se vea.
- **Nunca conviertas en afirmación cerrada algo que el origen da por provisional.** Publicar "la jurisprudencia trata la depilación láser como acto médico" cuando el `.md` dice "fuente única, no localizada en CENDOJ" no es simplificar: es dar por cierto algo que no lo está, y quien lea la web decidirá creyendo que hay una certeza que nadie ha comprobado.
- **Si el matiz no cabe, quita la afirmación, no el matiz.** Es preferible omitir un dato que publicarlo con más autoridad de la que tiene.
- **Distingue lo investigado de lo propuesto.** Las recomendaciones propias del asesor (modelo de precio, umbrales del piloto, secuencia de entrada) van marcadas como tales — "recomendación propia, no un hallazgo documentado" — igual que ya lo hacen los `.md` de origen.

**Comprobación antes de dar por terminada la regeneración**: cuenta las marcas de incertidumbre en los `.md` que has usado como fuente y en el HTML que has generado. Si la web tiene bastantes menos, has perdido matices por el camino y hay que revisarlo. En la revisión externa de septiembre de 2026 la proporción era de 70 marcas en las fuentes frente a 5 en la web publicada, y así fue como se coló el error del láser.

## 7. Estructura de contenido sugerida

Adapta esta estructura a lo que exista realmente en `negocio/` y `plan-negocio/` en cada momento (añade, quita o reordena secciones si el contenido ha cambiado sustancialmente), pero como referencia de partida:

1. El negocio hoy (local, equipo — situación actual real, no el plan futuro — y servicios)
2. El cambio de modelo (la decisión, el plan de transición, organigrama de gestión)
3. Viabilidad (a favor, riesgos, conclusión)
4. Los números (ingresos reales y objetivo, referencia de mercado)
5. Servicios para los cubículos (semáforo de candidatos, fichas legales)
6. Más ideas (otras profesiones, modelo anglosajón, y alumnado en prácticas como vía complementaria para cubrir un cubículo)
7. Casos reales de éxito — **centrados en operadores de coworking/salon suites de verdad** (no solo marcas de un único servicio), con su modelo de precios y lecciones aplicables a esta escala. Es el sitio **canónico** para casos como Phenix Salon Suites — en otras secciones que lo mencionen, enlaza aquí en vez de repetir el relato completo.
8. Cómo ofertar y gestionar el coworking — buenas prácticas de creación (antes de abrir) y gestión (una vez alquilado), más canales para encontrar inquilinas, qué debe incluir una oferta atractiva, ejemplos reales de anuncios, cómo validar demanda antes de comprometerse y perfil de profesional. Es el sitio **canónico** para el aviso del foro BeautyMarket sobre "cartera propia" — enlaza aquí en vez de repetirlo entero.
9. Ayudas públicas (municipal, insular, nacional, europeo)
10. Trámites administrativos y contrato — licencia de actividad, IAE, naturaleza jurídica del contrato, checklist de cláusulas, IVA/IRPF, registro sanitario, RGPD, seguro, reparto de responsabilidades
11. Estado del plan y DAFO — mapa de secciones del plan de negocio y radiografía DAFO completa
12. Decisiones pendientes (organizadas por bloques, incluyendo siempre el inventario de equipamiento/material del local)
13. Próximos pasos

**Evita repetir el mismo caso/dato citado con detalle en más de un sitio.** Si un hallazgo (un caso real, un aviso de foro, una cifra) ya tiene su sección natural, en el resto de secciones referencia esa sección en vez de recontar la historia — un enlace corto ("ver sección N") es preferible a duplicar dos o tres frases del mismo hallazgo.

## 8. Cierre

**No cierres la última sección con una nota de agradecimiento ni ningún mensaje meta sobre la presentación.** "Próximos pasos" debe terminar en una lista de acciones concretas, cada una enlazando a la sección donde se explica en detalle (p. ej. "Decidir precio y qué incluye el alquiler — ver Decisiones pendientes"), no en un párrafo de cierre. Esto no afecta al pie de generación descrito en la sección 1: ese pie va en todas las páginas, incluida la última, y no cuenta como mensaje meta de cierre.

Sobrescribe `docs/` por completo (borra páginas de secciones que ya no correspondan) para que el sitio publicado siempre refleje el estado más reciente de `negocio/` y `plan-negocio/`. `docs/` es exclusivamente la salida generada — no escribas notas ni contenido a mano ahí.
