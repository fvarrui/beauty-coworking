# Fuentes de investigación — bitácora

Registro de dónde se ha buscado información para el plan y qué tal ha funcionado cada fuente. No es el contenido de la investigación (eso vive en el documento de `negocio/`/`plan-negocio/` correspondiente) — es el mapa de "cómo lo encontré / por dónde seguir buscando la próxima vez".

## Índice rápido

| Tema | Última actualización | Documento con los hallazgos |
|---|---|---|
| Ayudas y subvenciones públicas | 13/09/2026 | [`ayudas-subvenciones.md`](./ayudas-subvenciones.md) |
| Trámites administrativos (licencia de actividad, IAE, IVA/IRPF, RGPD, sanitario, seguro) | 13/09/2026 | [`tramites-administrativos.md`](./tramites-administrativos.md) |

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

### Trámites administrativos (licencia de actividad, IAE, IVA/IRPF, RGPD, sanitario, seguro)

- **Investigado el**: 13/09/2026
- **Portales/organismos que funcionaron**:
  - **BOE**: [boe.es/buscar/act.php?id=BOE-A-2012-15595](https://www.boe.es/buscar/act.php?id=BOE-A-2012-15595) — texto consolidado de la Ley 12/2012 de liberalización del comercio; el anexo con el listado de grupos/epígrafes (incluye Grupo 972 peluquería/institutos de belleza) se encontró mejor en un PDF de una diputación provincial que en el propio BOE: [dipalme.org — Anexo Ley 12/2012](https://www.dipalme.org/Servicios/Organizacion/servicios.nsf/0/75AE663F349B2256C1258522003D15ED/$FILE/ANEXO%20LEY%2012-2012.pdf).
  - **BOC (Boletín Oficial de Canarias)**: [gobiernodecanarias.org/boc/2012/117/001.html](https://www.gobiernodecanarias.org/boc/2012/117/001.html) — Decreto 52/2012 (nomenclátor de actividades clasificadas de Canarias); confirma que las no listadas son inocuas, pero no se pudo extraer el nomenclátor completo en detalle vía WebFetch/WebSearch (solo referencias indirectas).
  - **arona.org (Portals, documentos oficiales en PDF)**: fuente primaria municipal de más valor de toda la investigación. Dos hallazgos clave:
    - [arona.org/Portals/0/documentos/0_16595_1.pdf](https://www.arona.org/Portals/0/documentos/0_16595_1.pdf) — Ordenanza Fiscal nº 7 de Arona (Tasa por Licencia de Apertura), texto completo y legible. Contiene el art. 8 "Concurrencia de actividades varias" — confirma que el Ayuntamiento sí tiene previsto el caso de varias actividades en un mismo local (tasa al 1/3 para la 2ª y siguientes). **Importante**: `WebFetch` no consigue extraer texto de los PDF de arona.org directamente (da error de "PDF binario codificado"), pero si se usa `WebFetch` igualmente el archivo se descarga en la carpeta de resultados de herramientas de la sesión y se puede releer con la herramienta `Read` (que sí extrae el texto del PDF) — este es el truco que funcionó.
    - [sede.arona.org/Tramites/ctl/Ver/mid/1190?id=45288](https://sede.arona.org/Tramites/ctl/Ver/mid/1190?id=45288) — ficha del trámite "116 - Actividad Clasificada - Comunicación previa de Instalación y/o Inicio" (para actividades clasificadas, no inocuas — sirve de referencia de formato pero no es el trámite exacto que necesita un salón de estética/peluquería inocuo).
  - **Gobierno de Canarias — Sanidad**: [www3.gobiernodecanarias.org/sanidad/scs/RegistroCentros/](https://www3.gobiernodecanarias.org/sanidad/scs/RegistroCentros/) y [contenidoGenerico.jsp?idDocument=8c42fd97...](https://www3.gobiernodecanarias.org/sanidad/scs/contenidoGenerico.jsp?idDocument=8c42fd97-9319-11df-a391-bb32e33a3514&idCarpeta=decccf4f-af33-11dd-a7d2-0594d2361b6c) — confirma que el registro sanitario de centros (Decreto 68/2010) es para centros con actos médicos ("centros de estética con medicina estética"), no para estética general.
  - **Agencia Tributaria (sede electrónica)**: [sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-inmobiliarias/alquilo-local-tengo-que-ingresar-iva.html](https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-inmobiliarias/alquilo-local-tengo-que-ingresar-iva.html) — confirma IVA 21% en alquiler de local de negocio (no exento como la vivienda).
  - **Licencias Tenerife** (gestoría privada especializada en licencias en Tenerife, fuente secundaria pero la más específica encontrada para el caso concreto): [licenciastenerife.es/2017/04/16/se-pueden-desarrollar-varias-actividades-en-el-mismo-local-comercial](https://www.licenciastenerife.es/2017/04/16/se-pueden-desarrollar-varias-actividades-en-el-mismo-local-comercial/) y [licenciastenerife.es/info/es-mi-actividad-inocua-o-clasificada](https://www.licenciastenerife.es/info/es-mi-actividad-inocua-o-clasificada/) — los dos artículos más útiles de toda la búsqueda para la pregunta "licencia por local o por titular", aunque sin valor normativo oficial.
- **Portales/vías que no dieron resultado**:
  - Buscador de trámites de `sede.arona.org/Tramites` — no indexa bien búsquedas por términos como "declaración responsable actividad inocua"; solo se pudo llegar a trámites concretos vía enlaces directos encontrados por `WebSearch`, no navegando el buscador interno de la sede.
  - `WebFetch` directo sobre PDFs de `arona.org` — falla con "contenido PDF codificado/binario" cuando se le pide analizar el contenido en el mismo prompt; **truco que sí funcionó**: el PDF se guarda igualmente en el disco local (ruta que aparece en la respuesta de `WebFetch`) y se puede releer con la herramienta `Read`, que sí extrae el texto correctamente.
  - No se ha localizado el texto completo del nomenclátor del Decreto 52/2012 (solo referencias y resúmenes de terceros) para confirmar 1:1 si "instituto de belleza"/"gabinete de estética" aparece nombrado o solo "peluquería".
  - No se ha localizado ninguna guía oficial de la AEPD específica para "salones de belleza multiprofesional"/coworking — solo guías genéricas de peluquerías con empleados y de pyme en general (Grupo Atico34, Cardeseo, Grupo PIC, todas consultoras privadas).
- **Términos de búsqueda que funcionaron mejor**:
  - `"Ley 12/2012 liberalización comercio declaración responsable salón belleza actividades clasificadas Canarias"`
  - `"licencia de actividad" varios titulares mismo local alquiler cabinas peluquería declaración responsable cada profesional` (llevó directo al artículo clave de Licencias Tenerife)
  - `site:arona.org licencia apertura actividad declaración responsable` (mejor que buscar en el propio buscador de la sede — encontró la ordenanza fiscal y el trámite 116)
  - `Decreto 52/2012 nomenclátor actividades clasificadas Canarias peluquería instituto de belleza inocua`
  - `Ley 12/2012 anexo actividades comercio servicios declaración responsable "peluquería" "institutos de belleza" listado` (dio el Grupo 972 con sus epígrafes exactos)
  - `retención IRPF 19% alquiler local negocio modelo 115 quién retiene arrendatario autónomo obligado`
  - `AEPD registro de actividades de tratamiento pequeña empresa menos de 250 empleados exención obligatorio`
- **Hallazgos volcados en**: [`tramites-administrativos.md`](./tramites-administrativos.md)
