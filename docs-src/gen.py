# -*- coding: utf-8 -*-
"""Genera docs/ (portada + secciones) para el portal del plan de negocio.

Uso:  python docs-src/gen.py

Reparto de responsabilidades:
  - bodies/NN.html  contiene SOLO el cuerpo de cada seccion (lo que se
    reescribe al regenerar el contenido con /presentar).
  - este fichero    contiene los metadatos de cada seccion y la plantilla
    comun: navbar, sidebar, breadcrumbs, paginacion, indice lateral, pie
    con la marca de generacion y la configuracion de Mermaid.

Regenera docs/ por completo: borra las paginas de secciones que ya no
correspondan y reescribe la portada. No edites docs/ a mano.
"""
import os
import re
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
BODIES = os.path.join(HERE, "bodies")
# docs/ es hermana de docs-src/ dentro del repositorio
OUT = os.path.normpath(os.path.join(HERE, os.pardir, "docs"))

MESES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

SITE = "Coworking de Belleza"
HOME_TITLE = "Coworking de belleza en Las Galletas"
HOME_LEAD = ("C&oacute;mo convertir el sal&oacute;n en un espacio gestionado, sin reformas, "
             "alquilando puestos a profesionales del sector.")

SECTIONS = [
    dict(num="01", slug="el-negocio-hoy", icon="\U0001F3E0",
         title="El negocio hoy",
         lead="Local, equipo y servicios tal y como est&aacute;n ahora mismo, antes del cambio de modelo.",
         card="Local, equipo y servicios tal y como est&aacute;n ahora mismo, antes del cambio de modelo.",
         sources=["negocio/situacion-actual.md", "negocio/local.md", "negocio/equipo.md",
                  "negocio/servicios.md", "negocio/precios-servicios.md"]),
    dict(num="02", slug="el-cambio-de-modelo", icon="\U0001F504",
         title="El cambio de modelo",
         lead="El plan: de sal&oacute;n tradicional a espacio de coworking de belleza, y en qu&eacute; orden conviene darlo.",
         card="El plan: de sal&oacute;n tradicional a espacio de coworking de belleza.",
         mermaid=True,
         sources=["negocio/diversificacion.md", "negocio/equipo.md",
                  "negocio/propuesta-oferta-coworking.md", "plan-negocio/validacion.md"]),
    dict(num="03", slug="viabilidad", icon="\U0001F4CA",
         title="Viabilidad",
         lead="Valoraci&oacute;n preliminar: qu&eacute; juega a favor, qu&eacute; riesgos hay y qu&eacute; falta por validar.",
         card="Valoraci&oacute;n preliminar: qu&eacute; juega a favor y qu&eacute; falta por validar.",
         sources=["negocio/diversificacion.md", "negocio/casos-reales-coworking.md",
                  "plan-negocio/validacion.md", "plan-negocio/financiero.md"]),
    dict(num="04", slug="los-numeros", icon="\U0001F4B6",
         title="Los n&uacute;meros",
         lead="Lo que ya genera el modelo, lo que podr&iacute;a generar, y el dato que falta para saber si el plan compensa.",
         card="Lo que ya genera el modelo y lo que podr&iacute;a generar a pleno rendimiento.",
         mermaid=True,
         sources=["plan-negocio/financiero.md", "negocio/precios-servicios.md",
                  "negocio/tramites-administrativos.md"]),
    dict(num="05", slug="servicios-para-los-cubiculos", icon="\U0001F485",
         title="Servicios para los cub&iacute;culos",
         lead="Qu&eacute; especialidades podr&iacute;an ocuparlos, con su viabilidad legal servicio por servicio.",
         card="Qu&eacute; especialidades podr&iacute;an ocuparlos, con su viabilidad legal.",
         sources=["negocio/diversificacion.md", "negocio/servicio-trenzas.md",
                  "negocio/servicio-masajes.md", "negocio/servicio-piercing-micropigmentacion.md",
                  "negocio/servicio-laser.md"]),
    dict(num="06", slug="mas-ideas", icon="\U0001F4A1",
         title="M&aacute;s ideas",
         lead="Fuera del sal&oacute;n de belleza cl&aacute;sico: otras profesiones, aprendizajes anglosajones y alumnado en pr&aacute;cticas.",
         card="Otras profesiones, aprendizajes anglosajones y alumnado en pr&aacute;cticas como v&iacute;a complementaria.",
         sources=["negocio/ideas-servicios-adicionales.md", "negocio/opcion-alumnado-fp-dual.md"]),
    dict(num="07", slug="casos-reales-de-exito", icon="\U0001F30D",
         title="Casos reales de &eacute;xito",
         lead="Operadores que viven de alquilar el espacio &mdash; lo mismo que se plantea aqu&iacute; &mdash; con sus precios y sus fracasos.",
         card="Operadores reales de coworking de belleza, con su modelo de precios y sus casos de fracaso.",
         sources=["negocio/casos-reales-coworking.md", "negocio/ideas-servicios-adicionales.md"]),
    dict(num="08", slug="como-ofertar-y-gestionar-el-coworking", icon="\U0001F9F0",
         title="C&oacute;mo ofertar y gestionar el coworking",
         lead="C&oacute;mo encontrar inquilinas, qu&eacute; ofrecerles y qu&eacute; vigilar en el d&iacute;a a d&iacute;a del espacio.",
         card="C&oacute;mo encontrar inquilinas, qu&eacute; incluir en la oferta y c&oacute;mo gestionar el espacio.",
         sources=["negocio/propuesta-oferta-coworking.md", "negocio/buenas-practicas-coworking.md",
                  "negocio/contrato-alquiler-cabina.md"]),
    dict(num="09", slug="ayudas-publicas", icon="\U0001F3DB️",
         title="Ayudas p&uacute;blicas",
         lead="Qu&eacute; ayudas existen en cada nivel administrativo &mdash; municipal, insular, nacional y europeo.",
         card="Qu&eacute; ayudas existen en cada nivel administrativo, y cu&aacute;les sirven de argumento de venta.",
         sources=["negocio/ayudas-subvenciones.md"]),
    dict(num="10", slug="tramites-administrativos-y-contrato", icon="\U0001F4DC",
         title="Tr&aacute;mites administrativos y contrato",
         lead="Qu&eacute; gestiones hay que hacer ante la administraci&oacute;n y qu&eacute; debe decir el contrato con cada inquilina.",
         card="Licencia, impuestos, seguros, RGPD y el checklist de cl&aacute;usulas del contrato.",
         sources=["negocio/tramites-administrativos.md", "negocio/contrato-alquiler-cabina.md"]),
    dict(num="11", slug="estado-del-plan-y-dafo", icon="\U0001F9ED",
         title="Estado del plan y DAFO",
         lead="Qu&eacute; secciones del plan de negocio ya se pueden redactar, cu&aacute;les siguen bloqueadas, y la radiograf&iacute;a DAFO.",
         card="Mapa de secciones del plan de negocio y radiograf&iacute;a DAFO completa.",
         sources=["plan-negocio/estructura.md", "plan-negocio/financiero.md"]),
    dict(num="12", slug="decisiones-pendientes", icon="❓",
         title="Decisiones pendientes",
         lead="Todo lo que solo puede responder la propietaria, agrupado por bloques.",
         card="Todo lo que solo puede responder la propietaria.",
         sources=[]),
    dict(num="13", slug="proximos-pasos", icon="\U0001F680",
         title="Pr&oacute;ximos pasos",
         lead="Por d&oacute;nde seguir a partir de aqu&iacute;, en orden.",
         card="Por d&oacute;nde seguir a partir de aqu&iacute;.",
         sources=["plan-negocio/validacion.md", "negocio/pendientes.md",
                  "negocio/tramites-administrativos.md"]),
]

GH = "https://github.com/fvarrui/beauty-coworking/blob/main/"


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def sources_block(files):
    if not files:
        return ""
    links = []
    for f in files:
        links.append('<a href="%s%s" target="_blank" rel="noopener">%s</a>' % (GH, f, f))
    return ('\n      <div class="sources"><span class="sources-label">Fuentes</span>'
            + '<span class="sep">&middot;</span>'.join(links) + "</div>\n")


def sidebar(current_slug):
    rows = []
    home = "index.html" if current_slug is None else "../index.html"
    cls = ' class="current"' if current_slug is None else ""
    rows.append('      <li><a href="%s"%s>Inicio</a></li>' % (home, cls))
    items = []
    for s in SECTIONS:
        href = ("sections/%s-%s.html" % (s["num"], s["slug"])) if current_slug is None \
            else ("%s-%s.html" % (s["num"], s["slug"]))
        cls = ' class="current"' if s["slug"] == current_slug else ""
        items.append('      <li><a href="%s"%s><span class="icon">%s</span>%s</a></li>'
                     % (href, cls, s["icon"], s["title"]))
    return ("""      <ul>
%s
      </ul>
      <div class="sidebar-group-label">Secciones</div>
      <ul>
%s
      </ul>""" % ("\n".join(rows), "\n".join(items)))


MERMAID_LIGHT = {
    "primaryColor": "#fce4ec", "primaryTextColor": "#1c1e21", "primaryBorderColor": "#c2185b",
    "lineColor": "#99123f", "secondaryColor": "#f6f7f9", "tertiaryColor": "#ffffff",
    "background": "#ffffff", "mainBkg": "#fce4ec", "nodeBorder": "#c2185b",
    "clusterBkg": "#f6f7f9", "clusterBorder": "#e3e5e8", "fontSize": "15px",
    "pie1": "#c2185b", "pie2": "#d9558a", "pie3": "#eda0bf",
    "pieStrokeColor": "#ffffff", "pieSectionTextColor": "#ffffff", "pieLegendTextColor": "#1c1e21",
    "pieTitleTextColor": "#1c1e21", "pieOuterStrokeColor": "#e3e5e8",
}
MERMAID_DARK = {
    "primaryColor": "#3a2430", "primaryTextColor": "#e6e6e6", "primaryBorderColor": "#f48fb1",
    "lineColor": "#f8bbd0", "secondaryColor": "#242526", "tertiaryColor": "#1b1b1d",
    "background": "#1b1b1d", "mainBkg": "#3a2430", "nodeBorder": "#f48fb1",
    "clusterBkg": "#242526", "clusterBorder": "#3b3d40", "fontSize": "15px",
    "pie1": "#f48fb1", "pie2": "#c76e8c", "pie3": "#8d4f66",
    "pieStrokeColor": "#1b1b1d", "pieSectionTextColor": "#1b1b1d", "pieLegendTextColor": "#e6e6e6",
    "pieTitleTextColor": "#e6e6e6", "pieOuterStrokeColor": "#3b3d40",
}


def mermaid_script():
    import json
    return """<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>
(function(){
  if (typeof mermaid === "undefined") return;
  var LIGHT = %s;
  var DARK  = %s;
  function currentTheme(){
    var a = document.documentElement.getAttribute("data-theme");
    if (a) return a;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  var nodes = [];
  function render(){
    var dark = currentTheme() === "dark";
    mermaid.initialize({ startOnLoad:false, theme:"base", securityLevel:"strict",
                         themeVariables: dark ? DARK : LIGHT,
                         flowchart: { htmlLabels:false, useMaxWidth:true,
                                      nodeSpacing:45, rankSpacing:70, padding:12 } });
    nodes.forEach(function(n){
      n.removeAttribute("data-processed");
      n.innerHTML = n.getAttribute("data-src");
    });
    try { mermaid.run({ nodes: nodes }); } catch(e) {}
  }
  document.addEventListener("DOMContentLoaded", function(){
    nodes = Array.prototype.slice.call(document.querySelectorAll(".mermaid"));
    nodes.forEach(function(n){ n.setAttribute("data-src", n.textContent); });
    render();
    var t = document.getElementById("theme-toggle");
    if (t) t.addEventListener("click", function(){ setTimeout(render, 30); });
  });
})();
</script>""" % (json.dumps(MERMAID_LIGHT), json.dumps(MERMAID_DARK))


def page(title, description, body, current_slug, stamp, depth, toc=None,
         breadcrumbs="", pagination="", mermaid=False):
    up = "../" if depth else ""
    toc_html = ""
    if toc:
        lis = "\n".join('      <li><a href="#%s">%s</a></li>' % (i, t) for i, t in toc)
        toc_html = """  <aside class="toc">
      <div class="toc-title">En esta secci&oacute;n</div>
      <ul>
%s
      </ul>
    </aside>
""" % lis
    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light dark">
<title>%(title)s &mdash; %(site)s</title>
<meta name="description" content="%(description)s">
<link rel="stylesheet" href="%(up)sassets/style.css">
<script>
(function(){try{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();
</script>
</head>
<body>
<header class="navbar">
  <div class="navbar-left">
    <button class="menu-toggle" id="menu-toggle" aria-label="Abrir navegaci&oacute;n">&#9776;</button>
    <a class="navbar-brand" href="%(up)sindex.html">
      <span class="logo">&#128135;</span>
      <span>%(site)s</span>
    </a>
  </div>
  <div class="navbar-right">
    <button class="theme-toggle" id="theme-toggle" aria-label="Cambiar tema">&#127769;</button>
  </div>
</header>
<div class="layout">
  <div class="sidebar-overlay" id="sidebar-overlay"></div>
  <aside class="sidebar" id="sidebar">
    <nav>
%(sidebar)s
    </nav>
  </aside>
  <main class="doc-main">
    <div class="doc-content">
%(breadcrumbs)s%(body)s
%(pagination)s
      <footer class="site-footer">
        Generado el <time datetime="%(iso)s">%(human)s</time> (hora de Canarias)
      </footer>

    </div>
  </main>
%(toc)s</div>
<script src="%(up)sassets/app.js"></script>
%(mermaid)s
</body>
</html>
""" % dict(title=title, site=SITE, description=description, up=up,
           sidebar=sidebar(current_slug), breadcrumbs=breadcrumbs, body=body,
           pagination=pagination, toc=toc_html, iso=stamp[0], human=stamp[1],
           mermaid=mermaid_script() if mermaid else "")


def pagination(idx):
    prev_html = "<span></span>"
    next_html = "<span></span>"
    if idx == 0:
        prev_html = '<a class="pag-link prev" href="../index.html"><span class="pag-dir">&larr; Anterior</span><span class="pag-title">Inicio</span></a>'
    else:
        p = SECTIONS[idx - 1]
        prev_html = ('<a class="pag-link prev" href="%s-%s.html"><span class="pag-dir">&larr; Anterior</span>'
                     '<span class="pag-title">%s</span></a>' % (p["num"], p["slug"], p["title"]))
    if idx < len(SECTIONS) - 1:
        n = SECTIONS[idx + 1]
        next_html = ('<a class="pag-link next" href="%s-%s.html"><span class="pag-dir">Siguiente &rarr;</span>'
                     '<span class="pag-title">%s</span></a>' % (n["num"], n["slug"], n["title"]))
    return '      <nav class="pagination">\n%s\n%s\n</nav>\n' % (prev_html, next_html)


def main():
    now = datetime.datetime.now()
    offset = "+01:00" if 3 < now.month < 11 else "+00:00"
    stamp = (now.strftime("%Y-%m-%dT%H:%M:%S") + offset,
             "%d de %s de %d a las %s" % (now.day, MESES[now.month], now.year, now.strftime("%H:%M")))

    os.makedirs(os.path.join(OUT, "sections"), exist_ok=True)
    # Limpia paginas de secciones antiguas
    for f in os.listdir(os.path.join(OUT, "sections")):
        if f.endswith(".html"):
            os.remove(os.path.join(OUT, "sections", f))

    # --- Portada ---
    cards = []
    for s in SECTIONS:
        cards.append('<a class="chapter-card" href="sections/%s-%s.html"><span class="card-icon">%s</span>'
                     '<span class="num">Secci&oacute;n %s</span><h3>%s</h3><p>%s</p></a>'
                     % (s["num"], s["slug"], s["icon"], s["num"], s["title"], s["card"]))
    home_body = open(os.path.join(BODIES, "00.html"), encoding="utf-8").read()
    home_body = home_body.replace("{{CARDS}}", "\n      ".join(cards))
    first = SECTIONS[0]
    home_pag = ('      <nav class="pagination">\n<span></span>\n'
                '<a class="pag-link next" href="sections/%s-%s.html"><span class="pag-dir">Siguiente &rarr;</span>'
                '<span class="pag-title">%s</span></a>\n</nav>\n' % (first["num"], first["slug"], first["title"]))
    html = page(HOME_TITLE, "Plan de negocio: coworking de belleza en Las Galletas (Arona, Tenerife).",
                home_body, None, stamp, 0, pagination=home_pag)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n").write(html)

    # --- Secciones ---
    for i, s in enumerate(SECTIONS):
        body = open(os.path.join(BODIES, s["num"] + ".html"), encoding="utf-8").read()
        toc = [(m.group(1), strip_tags(m.group(2)).strip())
               for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)]
        head = ('      <h1><span class="icon-lg">%s</span>%s</h1>\n'
                '      <p class="lead">%s</p>\n' % (s["icon"], s["title"], s["lead"]))
        crumbs = ('      <div class="breadcrumbs"><a href="../index.html">Inicio</a>'
                  '<span class="sep">&rsaquo;</span><span>Secci&oacute;n %s</span></div>\n' % s["num"])
        full = head + body + sources_block(s.get("sources"))
        html = page(s["title"], strip_tags(s["lead"]), full, s["slug"], stamp, 1,
                    toc=toc, breadcrumbs=crumbs, pagination=pagination(i),
                    mermaid=s.get("mermaid", False))
        open(os.path.join(OUT, "sections", "%s-%s.html" % (s["num"], s["slug"])),
             "w", encoding="utf-8", newline="\n").write(html)

    print("Generadas %d paginas en %s" % (len(SECTIONS) + 1, OUT))
    print("Marca de generacion: %s | %s" % (stamp[1], stamp[0]))


if __name__ == "__main__":
    main()
