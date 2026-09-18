# `docs-src/` — generador del portal

Esta carpeta es la **fuente** del portal publicado en [`docs/`](../docs/). `docs/` es salida generada: **no se edita a mano**, se regenera desde aquí.

## Cómo regenerar el portal

```bash
python docs-src/gen.py
```

No necesita instalar nada: solo Python 3 de la biblioteca estándar. Reescribe `docs/index.html` y todas las páginas de `docs/sections/`, y borra las páginas de secciones que ya no correspondan.

## Qué hay en cada sitio

| Fichero | Qué contiene | Cuándo se toca |
|---|---|---|
| `gen.py` → lista `SECTIONS` | Metadatos de cada sección: número, icono, título, entradilla, texto de la tarjeta de portada y los ficheros de `negocio/` y `plan-negocio/` que se citan como fuentes | Al añadir, quitar o reordenar secciones |
| `gen.py` → resto | Plantilla común: navbar, sidebar, breadcrumbs, paginación, índice lateral, pie con la marca de generación y configuración de Mermaid | Al cambiar el armazón del sitio |
| `bodies/NN.html` | **Solo el cuerpo** de cada sección, sin `<h1>` ni entradilla (esos salen de los metadatos). `bodies/00.html` es la portada | Al reescribir el contenido, que es lo habitual |
| [`docs/assets/style.css`](../docs/assets/style.css) | Hoja de estilos compartida | Al necesitar una clase nueva |

El índice lateral («En esta sección») **se construye solo** a partir de los `<h2 id="...">` del cuerpo: basta con poner un `id` a cada `<h2>` y aparecerá en el índice, en orden.

## Detalles que conviene no romper

- **El pie de generación** lo pone la plantilla en todas las páginas, con la hora real del momento de ejecución y el desfase de Canarias (`+01:00` en horario de verano, `+00:00` en invierno). No se escribe a mano en ningún cuerpo.
- **Mermaid** solo se carga en las secciones marcadas con `mermaid=True`. Los diagramas se redibujan al cambiar de tema claro/oscuro.
- **Las etiquetas de los diagramas van en una sola línea**: el modo seguro de Mermaid descarta los `<br/>`, y el texto sale pegado sin avisar.
- **En los gráficos de tipo `pie` no se usa la directiva `title`** de Mermaid, porque este diseño la recorta. El título va como `<p class="mermaid-caption">` justo antes del `.mermaid-wrap`.
- **Mermaid ordena las porciones del `pie` alfabéticamente** por etiqueta, no por el orden en que se declaran: no se puede dar significado a un color concreto.

## Relación con `/presentar`

El comando [`/presentar`](../.claude/commands/presentar.md) es el que decide **qué se cuenta** en el portal: lee de cero `negocio/` y `plan-negocio/` y reescribe los cuerpos de `bodies/`. Este generador decide **cómo se ve**. Las reglas de contenido —referencias con fuente, conservar las marcas de incertidumbre, lenguaje directo— viven en `/presentar`, no aquí.
