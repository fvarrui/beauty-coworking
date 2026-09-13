---
description: Investiga en profundidad una pregunta concreta del plan de negocio (mercado, competencia, normativa, casos reales...) y vuelca el resultado, con fuentes, en docs/
---

Investiga a fondo la pregunta o el tema que te indique el usuario (por ejemplo: un servicio candidato, un requisito legal, un canal de captación, un competidor, una ayuda pública) y deja el resultado documentado en `docs/negocio/` o `docs/plan-negocio/`, según corresponda. Sigue el mismo estándar ya aplicado en `casos-reales-coworking.md` y `propuesta-oferta-coworking.md`:

## 1. Antes de investigar

- Lee primero lo que ya existe en `docs/` sobre el tema, para no duplicar trabajo ni contradecir datos ya confirmados. Si la pregunta amplía o corrige un documento existente, actualiza ese documento en vez de crear uno nuevo redundante.
- Si la investigación es amplia (varios casos, varias fuentes), lánzala como un `Agent` en segundo plano (`subagent_type: general-purpose`, `run_in_background: true`) para no bloquear la conversación, y verifica el resultado leyéndolo antes de darlo por bueno.

## 2. Reglas de la investigación

- **Prioriza casos y datos reales, con nombre propio y fuente verificable**, frente a generalidades de sector. Un caso real con enlace vale más que un párrafo de sentido común sin referencia.
- **Prioriza lo aplicable a la escala real de este negocio** (un local, 3 puestos, zona no metropolitana) sobre ejemplos de operadores gigantes — cita estos últimos solo como contexto de mercado, dejándolo explícito.
- **Distingue siempre** lo confirmado con fuente, lo que es una hipótesis propia razonable (márcalo como tal), y lo que sigue siendo un hueco de información.
- **No inventes ni redondees datos para que "cuadren"**. Si una cifra no se encuentra, dilo — no la sustituyas por una estimación sin avisar de que lo es.
- **Nunca copies el nombre real de nadie del salón** en el documento resultante; usa siempre el rol ("la propietaria", "la profesional de pedicura", etc.).
- Cita fuentes con enlace siempre que exista una consultable online.

## 3. Formato del documento resultante

- Estructura en secciones claras con encabezados, tablas para comparaciones (precios, requisitos, canales...) y un aviso (`⚠️`) allí donde haya un hueco de información relevante.
- Cierra con una sección `## Huecos de información` o `## Resumen de huecos` que liste, sin adornos, todo lo que quedó sin confirmar.
- Si el nuevo documento debería enlazarse desde otro ya existente (p. ej. desde `diversificacion.md`, `situacion-actual.md` o `pendientes.md`), añade ese enlace.

## 4. Al terminar

Dile al usuario, en el chat, qué se ha confirmado (lo más relevante, con la fuente), qué sigue siendo un hueco, y si el hallazgo debería reflejarse también en la presentación (`/presentar`) o en `pendientes.md`.
