---
description: Audita todo el contenido del plan (negocio/, plan-negocio/) en busca de inconsistencias, datos inventados, nombres reales sin anonimizar y pendientes desactualizados
---

Audita el estado real de `negocio/` y `plan-negocio/` (los documentos fuente; `docs/` es la presentación generada, no hace falta auditarla aparte — si el contenido fuente cambia, se regenera con `/presentar`) para detectar problemas que se acumulan con ediciones sucesivas. No es una skill de contenido nuevo, es un control de calidad. Repasa:

## 1. Anonimización

- Busca en todo el repo cualquier nombre propio real (no roles) de la propietaria o de cualquier otra persona del salón. El repo se publica en GitHub — cero tolerancia a esto.
- Verifica que todas las personas se nombran por rol ("la propietaria", "la profesional de pedicura", "quien ocupe el Cubículo X"), nunca por parentesco no verificado ni por nombre.

## 2. Consistencia interna

- Compara cifras que deberían coincidir entre documentos (precios de alquiler, ingresos, nº de puestos, quién ocupa qué espacio hoy) y señala cualquier discrepancia.
- Comprueba que la distinción entre **situación actual** (qué pasa hoy) y **plan/objetivo** (qué se propone) esté clara en cada documento que toque el tema — es el error más fácil de reintroducir al editar solo una parte.
- Revisa que los enlaces internos entre documentos markdown (`[texto](./fichero.md)`) apunten a ficheros que existen de verdad, con el nombre correcto.

## 3. Datos inventados o sin fuente

- Señala cualquier afirmación que suene a dato concreto (precio, porcentaje, cifra legal) sin fuente ni indicación de que es una hipótesis propia — debería estar en `pendientes.md` o marcada explícitamente como suposición, no colada como hecho.

## 4. Estado de `pendientes.md`

- Contrasta `negocio/pendientes.md` contra el resto de `negocio/` y `plan-negocio/`: pendientes que ya se resolvieron en otro documento y no se han tachado/quitado; pendientes reales que han surgido en otros documentos y no están recogidos aquí.

## 5. Lenguaje y referencias

- Señala cualquier pregunta o pendiente formulado como fragmento nominal en vez de pregunta directa y completa (ver `CLAUDE.md`).
- Si al revisar `negocio/` o `plan-negocio/` detectas una afirmación citada en `docs/` (la presentación) sin el enlace correspondiente en su bloque `.sources` o en línea, señálalo también — se corrige regenerando esa sección con `/presentar`, no a mano en `docs/`.

## 6. Salida

No edites nada todavía: primero presenta al usuario una lista corta de lo encontrado, agrupada por las categorías anteriores, con el fichero y la línea o cita concreta. Pregunta o procede a corregir solo lo que sea mecánico y de bajo riesgo (enlaces rotos, "prima"/nombres colados) directamente; para lo que implique una decisión de contenido, déjalo listado para que el usuario decida.
