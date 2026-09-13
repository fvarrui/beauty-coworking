---
description: Regenera la presentación web (docs/) a partir de todo lo recopilado en negocio/ y plan-negocio/
---

Regenera por completo el sitio de `docs/` (portada `index.html` + una página por capítulo en `chapters/`), siguiendo estas reglas. Este comando **sustituye** al antiguo `/summary` — ya no se genera `resumen.md`; el entregable para la propietaria es siempre esta presentación web.

## 0. Antes de nada

- **Lee todo `negocio/` y `plan-negocio/` de cero**, fichero a fichero. No te bases en el estado anterior de la presentación ni en memoria de conversación: el sitio debe reflejar exactamente lo que dicen esos documentos ahora mismo, incluyendo qué está resuelto y qué sigue pendiente.
- **No inventes datos.** Si algo sigue sin confirmar en `pendientes.md` o en cualquier otro documento, refléjalo explícitamente como pendiente en la presentación — nunca rellenes el hueco con una suposición.
- **Nunca uses el nombre real de la propietaria** ni de ninguna otra persona del salón — llámalas por su rol ("la propietaria", "la profesional de pedicura", "quien ocupe el Cubículo 2", etc.), nunca por parentesco ni por nombre propio. El sitio se publica en GitHub.

## 1. Formato y sistema visual — mantén el existente, no lo reinventes

El sitio ya tiene un sistema de diseño (estilo Docusaurus: navbar superior, sidebar de capítulos a la izquierda, contenido central, "En esta página" a la derecha, paginación anterior/siguiente, modo claro/oscuro, responsive, con letra legible). Reutiliza:

- `docs/assets/style.css` — hoja de estilos compartida. Amplíala si necesitas una clase nueva para algo que no exista todavía, pero no rehagas la paleta ni la tipografía sin que te lo pidan explícitamente.
- `docs/assets/app.js` — toggle de tema + menú móvil.
- Un icono (emoji) por capítulo, coherente con su contenido, visible en el sidebar, en la tarjeta de portada y en el título de la página.

Si `docs/` no existe todavía o está vacío, créalo siguiendo esta misma estructura desde cero.

## 2. Diagramas — usa Mermaid, limpios y claros

Los diagramas del sitio (planta del local, organigrama de gestión, transición antes/después del modelo, línea de tiempo de próximos pasos, y cualquier otro que ayude a explicar algo estructural) deben construirse con **Mermaid**, no con divs de CSS a medida:

- Carga Mermaid vía CDN (`<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js">` o cdnjs) una vez por página que lo necesite, e inicialízalo con `mermaid.initialize({ startOnLoad: true, theme: ... })`. Ajusta el tema de Mermaid (claro/oscuro) al `data-theme` activo de la página para que combine con el resto del sitio.
- Usa el tipo de diagrama Mermaid que mejor encaje: `flowchart` para el organigrama y la transición antes/después, `timeline` o `flowchart LR` para la línea de tiempo de próximos pasos, `flowchart`/`graph` para la planta del local (representada como cajas conectadas o agrupadas, ya que Mermaid no dibuja planos arquitectónicos reales).
- Prioriza que cada diagrama se entienda de un vistazo: etiquetas cortas y claras, sin abarrotar, con el precio/estado como parte de la etiqueta cuando aporte información (p. ej. "Salón central — 300 €/mes — ocupado").
- Los datos en €/estado que aparezcan en KPIs sueltos (no relacionales) pueden seguir como bloques HTML/CSS normales (`.kpi-row`, tablas, etc.) — Mermaid es para lo que es genuinamente un diagrama (relaciones, flujo, estructura), no para todo.

## 3. Nivel de detalle — denso, no un resumen

A diferencia del antiguo resumen de una página, esta presentación debe **incluir bastantes detalles y explicaciones**, no condensarlo todo a una frase por idea. Para cada apartado:

- Explica el "por qué", no solo el "qué": si algo es viable o no, di la razón legal/práctica concreta, no solo el semáforo.
- Cuando un documento fuente tenga una tabla, una lista de fuentes o una comparación, tradúcela a la presentación con ese mismo nivel de detalle (no la resumas a una línea).
- Cuando haya varias opciones o casos analizados (candidatos de servicio, casos reales, ayudas públicas, canales de captación de inquilinas...), preséntalos todos, no solo los 2-3 más destacados.
- Mantén el estilo claro y bien estructurado (encabezados, listas, tablas, callouts para avisos/riesgos) para que la densidad de información no se sienta como un muro de texto.

## 4. Estructura de contenido sugerida

Adapta esta estructura a lo que exista realmente en `negocio/` y `plan-negocio/` en cada momento (añade, quita o reordena capítulos si el contenido ha cambiado sustancialmente), pero como referencia de partida:

1. El negocio hoy (local, equipo — situación actual real, no el plan futuro — y servicios)
2. El cambio de modelo (la decisión, el plan de transición, organigrama de gestión)
3. Viabilidad (a favor, riesgos, conclusión)
4. Los números (ingresos reales y objetivo, referencia de mercado)
5. Servicios para los cubículos (semáforo de candidatos, fichas legales)
6. Más ideas (otras profesiones, modelo anglosajón)
7. Casos reales de éxito — **centrados en operadores de coworking/salon suites de verdad** (no solo marcas de un único servicio), con su modelo de precios y lecciones aplicables a esta escala
8. Cómo ofertar el coworking — canales para encontrar inquilinas, qué debe incluir una oferta atractiva, cómo validar demanda antes de comprometerse
9. Ayudas públicas
10. El contrato de alquiler
11. Alumnado en prácticas (vía complementaria)
12. Estado del plan de negocio (mapa de secciones estándar de un plan de negocio)
13. DAFO completo
14. Decisiones pendientes (organizadas por bloques, incluyendo siempre el inventario de equipamiento/material del local)
15. Próximos pasos

## 5. Cierre

Cierra la página del último capítulo con una nota de agradecimiento breve, recordando que el detalle completo (fuentes incluidas) está en `negocio/` y `plan-negocio/`, y que la presentación se puede regenerar en cualquier momento con `/presentar`.

Sobrescribe `docs/` por completo (borra páginas de capítulos que ya no correspondan) para que el sitio publicado siempre refleje el estado más reciente de `negocio/` y `plan-negocio/`. `docs/` es exclusivamente la salida generada — no escribas notas ni contenido a mano ahí.
