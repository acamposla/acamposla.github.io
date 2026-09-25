"""Genera _includes/diagrama-encargo-skill.html: el proceso de la entrada
"Antes de la skill, un fichero de trucos" como SVG interactivo.

La topología es la misma que validó archify (proceso-encargo-a-skill.workflow.json),
redibujada a mano para la columna de 40rem del blog y con sus variables de color,
de modo que el modo oscuro funciona solo. Uso: python3 encargo-a-skill.py
"""
from pathlib import Path

W, H = 640, 480
NH = 64  # alto de nodo

# id: (x, y, ancho, carril, título, subtítulo, explicación)
NODOS = {
    "encargo":      (60, 16, 240, "Tú", "Encargo", "dictado + referencias",
                     "Lo dictas por voz, con las fotos de referencia y tus condiciones: qué modelo, borrador barato primero y que explique lo que hace."),
    "plan":         (60, 111, 240, "Claude", "Plan", "qué modelo y por qué",
                     "Claude elige modelo y parámetros. Pedirle que razone la elección le obliga a comparar antes de lanzar."),
    "generar":      (60, 206, 240, "Higgsfield vía MCP", "Generar", "función generate",
                     "Claude rellena los parámetros de la función de Higgsfield a través del MCP. Solo puede usar las funciones que el conector expone."),
    "calidad":      (60, 301, 240, "Claude", "Control de calidad", "¿es el mismo producto?",
                     "Antes de enseñarte nada, Claude revisa el resultado contra tus reglas. Si las dos tomas no muestran el mismo producto, lo vuelve a pedir."),
    "resultado":    (60, 396, 240, "Tú", "Resultado", "borrador y luego alta",
                     "Te llega el borrador en baja calidad. Con tu visto bueno, la versión en alta."),
    "aprendizajes": (390, 396, 220, "Memoria del proyecto", "aprendizajes.md", "qué funcionó y qué no",
                     "Al cerrar la sesión, Claude apunta en un fichero del proyecto qué funcionó y qué no."),
    "skill":        (390, 111, 220, "Memoria del proyecto", "Skill", "reglas que se repiten",
                     "Cuando esas reglas se repiten de un proyecto a otro, se empaquetan en una skill que Claude carga sola si el encargo se parece."),
}

# (desde, hasta, path, punta (x, y, dirección), etiqueta, (x, y, anchor, rotación), tipo)
ARISTAS = [
    ("encargo", "plan", "M180 80 V108", (180, 111, "abajo"), None, None, ""),
    ("plan", "generar", "M180 175 V203", (180, 206, "abajo"), "vía MCP", (190, 195, "start", 0), ""),
    ("generar", "calidad", "M180 270 V298", (180, 301, "abajo"), None, None, ""),
    ("calidad", "generar", "M60 333 H38 V238 H57", (60, 238, "derecha"), "no pasa", (30, 286, "middle", -90), "fallo"),
    ("calidad", "resultado", "M180 365 V393", (180, 396, "abajo"), "pasa", (190, 385, "start", 0), ""),
    ("resultado", "aprendizajes", "M300 428 H387", (390, 428, "derecha"), "al cerrar sesión", (345, 420, "middle", 0), "memoria"),
    ("aprendizajes", "skill", "M500 396 V178", (500, 175, "arriba"), "cuando se repite", (510, 290, "start", 0), "memoria"),
    ("skill", "plan", "M390 143 H303", (300, 143, "izquierda"), "se carga sola", (345, 135, "middle", 0), "memoria"),
]


def punta(x, y, d):
    s = 5
    forma = {
        "abajo": f"{x},{y} {x - s},{y - 8} {x + s},{y - 8}",
        "arriba": f"{x},{y} {x - s},{y + 8} {x + s},{y + 8}",
        "derecha": f"{x},{y} {x - 8},{y - s} {x - 8},{y + s}",
        "izquierda": f"{x},{y} {x + 8},{y - s} {x + 8},{y + s}",
    }[d]
    return f'<polygon points="{forma}"/>'


def svg():
    partes = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="dg-titulo dg-desc">',
              '<title id="dg-titulo">Del encargo a la skill</title>',
              ('<desc id="dg-desc">Tu encargo pasa a un plan de Claude; Claude genera en Higgsfield vía MCP; '
               'un control de calidad devuelve a generar si falla y entrega el resultado si pasa. Al cerrar sesión '
               'lo aprendido va a aprendizajes.md, que cuando se repite se convierte en una skill que Claude carga '
               'en el siguiente plan.</desc>')]
    for desde, hasta, d, (px, py, dir_), etiqueta, pos, tipo in ARISTAS:
        clase = f"dg-arista {tipo}".strip()
        g = [f'<g class="{clase}" data-desde="{desde}" data-hasta="{hasta}">',
             f'<path d="{d}"/>', punta(px, py, dir_)]
        if etiqueta:
            x, y, anchor, rot = pos
            giro = f' transform="rotate({rot} {x} {y})"' if rot else ""
            g.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}"{giro}>{etiqueta}</text>')
        g.append("</g>")
        partes.append("".join(g))
    for id_, (x, y, w, carril, titulo, sub, _) in NODOS.items():
        cx = x + w / 2
        clase = "dg-nodo" + (" control" if id_ == "calidad" else "")
        partes.append(
            f'<g class="{clase}" data-id="{id_}" tabindex="0" role="button" aria-label="{titulo}">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{NH}" rx="8"/>'
            f'<text class="carril" x="{cx}" y="{y + 18}" text-anchor="middle">{carril.upper()}</text>'
            f'<text class="titulo" x="{cx}" y="{y + 38}" text-anchor="middle">{titulo}</text>'
            f'<text class="sub" x="{cx}" y="{y + 54}" text-anchor="middle">{sub}</text></g>')
    partes.append("</svg>")
    return "\n".join(partes)


def script():
    textos = ",\n    ".join(f'{id_}: "{n[6]}"' for id_, n in NODOS.items())
    return f"""<script>
(function () {{
  var fig = document.getElementById('diagrama-encargo');
  if (!fig) return;
  var detalle = fig.querySelector('.dg-detalle');
  var porDefecto = detalle.textContent;
  var textos = {{
    {textos}
  }};
  var nodos = fig.querySelectorAll('.dg-nodo');
  var aristas = fig.querySelectorAll('.dg-arista');
  var fijo = null;
  function activar(id) {{
    fig.classList.toggle('activo', !!id);
    var vecinos = {{}};
    vecinos[id] = true;
    aristas.forEach(function (a) {{
      var on = a.dataset.desde === id || a.dataset.hasta === id;
      a.classList.toggle('on', on);
      if (on) {{ vecinos[a.dataset.desde] = true; vecinos[a.dataset.hasta] = true; }}
    }});
    nodos.forEach(function (n) {{
      n.classList.toggle('on', !!id && vecinos[n.dataset.id]);
      n.classList.toggle('actual', n.dataset.id === id);
    }});
    detalle.textContent = id ? textos[id] : porDefecto;
  }}
  nodos.forEach(function (n) {{
    n.addEventListener('mouseenter', function () {{ if (!fijo) activar(n.dataset.id); }});
    n.addEventListener('mouseleave', function () {{ if (!fijo) activar(null); }});
    n.addEventListener('focus', function () {{ activar(n.dataset.id); }});
    n.addEventListener('click', function () {{
      fijo = fijo === n.dataset.id ? null : n.dataset.id;
      activar(fijo);
    }});
  }});
}})();
</script>"""


html = f"""<!-- Generado por scripts/diagramas/encargo-a-skill.py. No editar a mano. -->
<figure class="diagrama" id="diagrama-encargo">
{svg()}
<p class="dg-detalle" aria-live="polite">Pasa el ratón o toca un paso para ver qué ocurre en él.</p>
</figure>
{script()}
"""

raiz = Path(__file__).resolve().parents[2]
(raiz / "_includes" / "diagrama-encargo-skill.html").write_text(html, encoding="utf-8")
print("ok")
