# Fuentes de investigación — bitácora

Registro de dónde se ha buscado información para el plan y qué tal ha funcionado cada fuente. No es el contenido de la investigación (eso vive en el documento de `negocio/`/`plan-negocio/` correspondiente) — es el mapa de "cómo lo encontré / por dónde seguir buscando la próxima vez".

## Índice rápido

| Tema | Última actualización | Documento con los hallazgos |
|---|---|---|
| Ayudas y subvenciones públicas | 13/09/2026 | [`ayudas-subvenciones.md`](./ayudas-subvenciones.md) |

## Entradas

### Ayudas y subvenciones públicas

- **Investigado el**: 13/09/2026
- **Portales/organismos que funcionaron**:
  - **Ayuntamiento de Arona — sede/área de Promoción Económica**: [arona.org/Areas-Municipales/Promocion-Economica-y-Empleo/Ayudas-y-subvenciones](https://www.arona.org/Areas-Municipales/Promocion-Economica-y-Empleo/Ayudas-y-subvenciones) — listado de convocatorias municipales vigentes/recientes (Bono Comercio 2026, dinamización de zonas comerciales abiertas). El detalle de cada convocatoria concreta sí carga bien vía `WebFetch` en las URLs con `ctl/Ver/mid/...?id=...` (a diferencia de la sede.arona.org, ver más abajo).
  - **Centro Empresarial de Arona**: [arona.org/emprende/CentroEmpresarial](https://www.arona.org/emprende/CentroEmpresarial) — confirma que es solo servicio de asesoramiento/tramitación, sin línea de subvención propia.
  - **Portal Comercio de Tenerife (Cabildo)**: [tenerifecomercio.com/index.php/subvenciones?view=subvenciones](https://www.tenerifecomercio.com/index.php/subvenciones?view=subvenciones) — el mejor punto de entrada para ver de un vistazo TODAS las convocatorias de comercio del Cabildo vigentes con sus plazos exactos (funcionó mucho mejor que buscar cada convocatoria por separado). Enlaza a las fichas de `sede.tenerife.es`.
  - **Sede electrónica del Cabildo de Tenerife**: [sede.tenerife.es](https://sede.tenerife.es/) — tiene las fichas oficiales de cada trámite/subvención (URLs tipo `sede.tenerife.es/es/tramites/NNNNNNN-Nombre-tramite`), pero son páginas cargadas por JavaScript: `WebFetch` solo devuelve el título "Sede Electrónica del Cabildo de Tenerife", sin contenido. Para esta sede, mejor apoyarse en `tenerifecomercio.com` o en `WebSearch` (que sí indexa el contenido) y contrastar con prensa/BOP.
  - **Diario de Avisos** (prensa especializada, ya usado en la investigación anterior): [diariodeavisos.elespanol.com](https://diariodeavisos.elespanol.com/2026/05/ayudas-comercio-tenerife-2026-reforma-locales/) — buen resumen de la ayuda de reforma/equipamiento del Cabildo, aunque no daba el plazo exacto (eso se confirmó en tenerifecomercio.com).
  - **sede.red.gob.es** (Kit Digital): [sede.red.gob.es/es/procedimientos/convocatoria-de-ayudas-destinadas-la-digitalizacion-de-empresas-del-segmento-iii](https://sede.red.gob.es/es/procedimientos/convocatoria-de-ayudas-destinadas-la-digitalizacion-de-empresas-del-segmento-iii) — sí carga bien vía `WebFetch` y confirma el estado "PLAZO FINALIZADO" del Segmento III.
  - **Seguridad Social / Importass**: [seg-social.es — nuevo sistema de cotización para autónomos](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24) — confirma la tarifa plana de 80 €/mes con fuente oficial.
  - **SEPE**: [sepe.es/HomeSepe/autonomos/prestaciones-para-emprendedores-y-autonomos/capitaliza-tu-prestacion.html](https://www.sepe.es/HomeSepe/autonomos/prestaciones-para-emprendedores-y-autonomos/capitaliza-tu-prestacion.html) — página oficial correcta para capitalización del paro (¡ojo! la URL corta `sepe.es/HomeSepe/autonomos/pago-unico.html` da 404, no usarla).
  - **Sede electrónica del Gobierno de Canarias**: [sede.gobiernodecanarias.org/sede/tramites/3885](https://sede.gobiernodecanarias.org/sede/tramites/3885) — Subvención Promoción del Empleo Autónomo, ya usada en la investigación anterior, confirmada con fechas actualizadas de la convocatoria 2026 vía `WebSearch`.
  - **ICO**: [ico.es/web/ico/prestamos-ico](https://www.ico.es/web/ico/prestamos-ico) — portal general válido como fuente oficial de referencia, pero no tiene una ficha fija con condiciones de la Línea Empresas y Emprendedores (usa un buscador de productos dinámico); para condiciones concretas hubo que apoyarse en agregadores (buscaayudas.es) sin verificación 1:1 oficial — dejarlo como hueco.
- **Portales/vías que no dieron resultado**:
  - `sede.tenerife.es` vía `WebFetch` directo — la página es una SPA de JavaScript, solo devuelve el título. Usar `WebSearch` o `tenerifecomercio.com` en su lugar para el Cabildo.
  - `sepe.es/HomeSepe/autonomos/pago-unico.html` — 404. La ruta correcta es la de "capitaliza-tu-prestacion.html" (ver arriba).
  - Búsqueda de Innova Tenerife como fuente de ayudas de digitalización/equipamiento accesibles a microempresas — solo aparecen programas de I+D+i (doctorados industriales, Activa Startups) que no encajan con el tamaño del negocio; no hay una línea "pyme pequeña" propia distinta de Pyme Digital (gestionada por la Cámara de Comercio, no por Innova Tenerife directamente).
  - No se ha encontrado ninguna línea municipal (Arona) de subvención económica directa a comercio/autónomos individuales (solo incentivos al consumo tipo Bono Comercio, y ayudas a asociaciones de comerciantes, no a negocios individuales).
- **Términos de búsqueda que funcionaron mejor**:
  - `"Ayuntamiento de Arona ayudas subvenciones comercio autónomos 2026"`
  - `"Ayudas Comercio Tenerife 2026 Cabildo bases reguladoras plazo solicitud"`
  - `"Subvención Apertura Nueva Empresa" Tenerife 2026 BOP Cabildo bases site:tenerife.es OR site:sede.tenerife.es OR site:tenerifecomercio.com` (la búsqueda con `site:` acotada a varios dominios a la vez dio muy buen resultado para encontrar la ficha oficial exacta)
  - `Kit Digital segmento III 2026 nueva convocatoria reapertura fondos remanentes`
  - `capitalización prestación desempleo pago único autónomo SEPE 2026`
- **Hallazgos volcados en**: [`ayudas-subvenciones.md`](./ayudas-subvenciones.md)
