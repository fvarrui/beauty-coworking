---
description: Regenera resumen.md con un resumen alegre y visual para la propietaria del salón de todo lo recopilado en el proyecto
---

Regenera el fichero `resumen.md` en la raíz del repositorio, siguiendo estas reglas:

0. **Añade siempre la fecha y hora de generación al principio del documento**, justo debajo del título, en una línea del estilo: `🕒 *Generado el DD/MM/AAAA a las HH:MM*`. Obtén la fecha/hora real actual (por ejemplo con `date "+%Y-%m-%d %H:%M"` o equivalente) — no la copies de una versión anterior del fichero ni la inventes. Esto permite saber de un vistazo cuándo se generó la versión que está leyendo la propietaria.

1. **Lee primero todo el contenido actual del proyecto**: todos los ficheros de `docs/negocio/` y de `docs/plan-negocio/` (y cualquier otro `.md` relevante que exista bajo `docs/`). No te bases en versiones anteriores del resumen ni en memoria de conversación: el resumen debe reflejar el estado real y actual de esos documentos.

2. **Público objetivo**: el resumen es para **la propietaria** del salón, que **no tiene conocimientos técnicos ni de gestión** y puede no haber seguido el detalle de cada conversación. Debe poder leerlo de un tirón y quedarse con las ideas clave sin esfuerzo. **No uses su nombre real en ningún momento** (el documento se publica en GitHub): dirígete a ella de tú, sin nombrarla.

3. **Tono y formato**:
   - Alegre, cercano, tuteando a la propietaria directamente (sin usar su nombre).
   - Usa emojis con generosidad pero con criterio (títulos, bullets, semáforos 🟢🟡🔴 para indicar viabilidad).
   - Nada de jerga de consultoría ni tecnicismos legales sin explicar — tradúcelo a lenguaje sencillo.
   - Estructura con encabezados claros, listas y alguna tabla corta si ayuda a la lectura.
   - Que dé gusto leerlo: secciones cortas, ritmo ágil, cierre motivador con próximos pasos.

4. **Contenido que debe cubrir** (adaptando según lo que exista en `docs/` en cada momento):
   - Cómo está el negocio hoy (local, equipo, servicios actuales).
   - La idea de diversificación en curso (alquiler de cabinas) y su estado de viabilidad.
   - Ideas de nuevos servicios candidatos, con su semáforo de viabilidad legal/práctica.
   - Otras vías complementarias exploradas (p. ej. alumnado en prácticas).
   - Ayudas o subvenciones públicas relevantes encontradas.
   - Puntos clave a no olvidar si se alquila espacio a terceros (contrato).
   - Lista de preguntas pendientes que solo la propietaria puede responder, en lenguaje llano (no como checklist técnico interno).
   - Próximos pasos concretos y accionables.

5. **No inventes datos.** Si algo sigue sin confirmarse en `docs/negocio/pendientes.md` o en otros documentos, refléjalo como pendiente en el resumen, sin rellenar el hueco con suposiciones.

6. **Cierra el fichero** recordando que el detalle completo está en `docs/` y que este resumen se puede regenerar con `/summary` cuando haya novedades.

Sobrescribe `resumen.md` completo (no lo vayas apilando ni dejes secciones obsoletas) para que siempre refleje el estado más reciente.
