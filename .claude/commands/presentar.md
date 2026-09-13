---
description: Regenera la presentación web (docs/) a partir de todo lo recopilado en negocio/ y plan-negocio/
---

Regenera por completo el sitio de `docs/` (portada `index.html` + una página por sección en `chapters/`), siguiendo estas reglas. Este comando **sustituye** al antiguo `/summary` — ya no se genera `resumen.md`; el entregable para la propietaria es siempre esta presentación web.

Las unidades de contenido se llaman **secciones**, no "capítulos" — etiquétalas siempre como "Sección 01", "Sección 02"... (breadcrumb, tarjetas de portada, sidebar) aunque la carpeta técnica siga llamándose `chapters/`.

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

## 2. Diagramas — solo si aportan, y en Mermaid

**No añadas un diagrama porque "queda bien" o porque la sección lo admite.** Antes de meter uno, pregúntate si una tabla, una lista o un párrafo ya cuentan lo mismo igual de claro — si es así, no hace falta diagrama. Un diagrama se justifica cuando muestra una **relación, un flujo o una estructura** que en prosa cuesta seguir (quién depende de quién, un proceso con pasos, un antes/después, una línea temporal). Ejemplos que sí aportan: organigrama de gestión (sección 2), transición antes/después del modelo (sección 2), línea de tiempo de próximos pasos (sección 15). Ejemplo que **no** aporta y no debe repetirse: un diagrama de "planta del local" a base de cajas conectadas — no representa la disposición real del espacio (Mermaid no dibuja planos) y la tabla de "quién ocupa qué espacio hoy" ya da esa misma información mejor.

Cuando un diagrama sí esté justificado, constrúyelo con **Mermaid**, no con divs de CSS a medida:

- Carga Mermaid vía CDN (`<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js">` o cdnjs) una vez por página que lo necesite, e inicialízalo con `mermaid.initialize({ startOnLoad: true, theme: ... })`. Ajusta el tema de Mermaid (claro/oscuro) al `data-theme` activo de la página para que combine con el resto del sitio. No incluyas el script de Mermaid en páginas sin ningún diagrama.
- Prioriza que cada diagrama se entienda de un vistazo: etiquetas cortas y claras, sin abarrotar, con el precio/estado como parte de la etiqueta cuando aporte información (p. ej. "Salón central — 300 €/mes — ocupado").
- Los datos en €/estado que aparezcan en KPIs sueltos (no relacionales) van como bloques HTML/CSS normales (`.kpi-row`, tablas, etc.), nunca como diagrama.

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

## 6. Estructura de contenido sugerida

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

## 7. Cierre

Cierra la página de la última sección con una nota de agradecimiento breve, recordando que el detalle completo (fuentes incluidas) está en `negocio/` y `plan-negocio/`, y que la presentación se puede regenerar en cualquier momento con `/presentar`.

Sobrescribe `docs/` por completo (borra páginas de secciones que ya no correspondan) para que el sitio publicado siempre refleje el estado más reciente de `negocio/` y `plan-negocio/`. `docs/` es exclusivamente la salida generada — no escribas notas ni contenido a mano ahí.
