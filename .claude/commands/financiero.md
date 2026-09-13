---
description: Construye o actualiza la sección económico-financiera del plan de negocio (docs/plan-negocio/) a partir de los datos ya confirmados en docs/negocio/
---

Construye o actualiza el bloque económico-financiero del plan (`docs/plan-negocio/`, p. ej. `financiero.md`): ingresos, costes, punto de equilibrio y proyección a 12 meses. Es la sección que hoy está más bloqueada (ver `estado-del-plan-de-negocio` / capítulo 12 de la presentación), así que trátala con más cuidado que las demás:

## 1. Reúne los datos ya confirmados

Lee `docs/negocio/` entero antes de escribir una sola cifra: rentas (300 €/mes en marcha, ~400 €/mes objetivo por cubículo), cualquier precio de servicio ya registrado, y cualquier coste mencionado (ayudas, cuotas de autónomo citadas en las fichas de servicios). No mezcles cifras de referencia de mercado (de otras ciudades u operadores) con cifras propias del negocio sin dejar clarísimo cuál es cuál.

## 2. No inventes ni un coste fijo

Gastos fijos habituales de un local de este tipo (suministros, seguro, gestoría, IBI, comunidad si aplica) casi seguro **no están documentados todavía**. No los estimes para poder cerrar una tabla bonita: lístalos como fila con la cifra en blanco y una nota "⚠️ pendiente de confirmar con la propietaria", y añádelos también a `docs/negocio/pendientes.md` si no están ya.

## 3. Qué construir

- **Ingresos**: tabla mes a mes/objetivo con lo ya real (salón central) separado de lo objetivo (cubículos 1 y 2), igual que ya se hace en la presentación.
- **Costes**: fijos conocidos vs. pendientes de confirmar, separados con claridad.
- **Punto de equilibrio**: solo lo calcules si hay datos suficientes para que el cálculo sea real, no ilustrativo — si faltan costes clave, dilo en vez de dar un número que parezca más sólido de lo que es.
- **Escenarios**: como mucho un escenario "solo salón central" (ingreso ya real) vs. "a pleno rendimiento" (los 3 puestos alquilados) — evita escenarios optimista/pesimista inventados sin base.

## 4. Al terminar

Señala explícitamente qué inputs harían que este documento deje de ser provisional (qué preguntarle a la propietaria), y si procede, recuérdale al usuario regenerar la presentación con `/presentar` para que el capítulo "Los números" quede sincronizado.
