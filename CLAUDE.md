# Blog y portfolio personal de Alejandro Campos Lamas (Jekyll + GitHub Pages).

Sitio estático servido por GitHub Pages desde la rama `main`. Sin Actions, sin
build local obligatorio: GitHub construye Jekyll en su lado al recibir el push.

Dominio previsto: `alejandrocamposlamas.com` (los dos apellidos a propósito —
`alejandrocampos.dev/.com/.es` están ocupados, y el `.dev` lo tiene un homónimo
developer con portfolio activo).

## Dos tipos de contenido

- `_posts/` → blog, cronológico, `/blog/:year/:title/`.
- `_proyectos/` → colección de portfolio, atemporal, `/proyectos/:name/`, con
  ficha técnica (cliente, rol, stack, resultado) y agrupada por `disciplina`.

El portfolio se ordena por **disciplina en orden narrativo** (Datos → Marca →
Dirección de arte), declarado a mano en `proyectos.html`. No es cosmético: según
la nota de identidad del vault, lo escaso no es cada pieza suelta sino la
secuencia completa creativo premiado → dueño del margen → gobierno del dato.
Romper ese orden rompe el argumento.

## Rol de la IA en este repo

Ayudas con **estructura, diseño y publicación**. NO escribes entradas por tu
cuenta: la voz del blog es la de Alejandro y el contenido lo escribe él. Si te
pide ayuda con una entrada, trabajas sobre su borrador — no lo generas de cero
salvo que lo pida explícitamente.

## Línea editorial (fuente: cerebro-digital)

Narrar **desde el proceso**, no desde la cátedra: "estoy construyendo, esto es
lo que los datos me enseñaron". Es la corrección explícita al patrón de
[[Referentes_Profesionales]] — imitar la voz de autoridad de 25 años de
trayectoria directiva sin ese recorrido suena impostado.

Territorio: el cruce negocio ↔ datos ↔ creatividad. Margen, surtido, sell-in/
sell-out, PIM, SAP, BI, y el criterio que se saca de operarlos. Detalle del
posicionamiento en `cerebro-digital/2_Areas/Negocio/Identidad_Vertice_Conector_Bilingue.md`.

**Este blog NO es el de Vertienza ni el de Sapioverse.** Marca personal, primera
persona. Si una idea es corporativa, va a la web de su vehículo, no aquí.

## Restricciones técnicas

- Solo plugins de la lista blanca de GitHub Pages (`jekyll-feed`,
  `jekyll-seo-tag`, `jekyll-sitemap`). Cualquier otro obliga a migrar a Actions.
- Sin fuentes ni scripts externos: cero peticiones de red desde la página.
- Todo el diseño vive en `assets/css/main.css`. No añadir frameworks CSS.
- Sitio estático: no hay formularios con backend ni base de datos.

## Integración con el sistema

- **Ficha Notion**: —
- **Capa de ejecución**: Ninguna (sin tracking operativo)
- **Routing**: Se toca cuando hay algo que publicar
