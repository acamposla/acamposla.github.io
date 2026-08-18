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

## Compilar una entrada desde `analitica-comercial`

La mayor parte del blog sale del proyecto privado
`~/Proyectos/personal/analitica-comercial`. El procedimiento es fijo y **se
ejecuta desde una sesión abierta en ESTE repo**, leyendo el otro como fuente de
solo lectura. Nunca al revés: allí suele haber otra sesión trabajando.

### El ciclo

1. **La cantera manda.** Los candidatos viven en
   `analitica-comercial/docs/cantera-blog.md`, con estado `LISTA` / `ESPERA` /
   `PENDIENTE` y la fuente anotada. No se empieza una entrada que no esté ahí:
   si no está anotada, es que no dolió, y si no dolió no hay post.
2. **Leer el material real**, no reescribirlo de memoria. Está en `docs/` de ese
   repo, casi nunca en el notebook.
3. **Regenerar, no recortar.** El análisis se reproduce sobre datos sintéticos
   con semilla fija, no se recortan celdas del notebook real. Elimina el riesgo
   de fuga en origen y hace la entrada reproducible por el lector — que es el
   criterio de `Fuentes_Abiertas_Para_Portfolio_Publico` del vault: *un análisis
   que el lector no puede reproducir no demuestra competencia, demuestra acceso*.
4. **Verificar el código antes de escribirlo en el post.** `conda activate
   env_datos`. Las salidas que aparecen en la entrada son las que dio la máquina.
5. **Pasar el gate** de `analitica-comercial/docs/gate-publicacion.md` y dejar
   el resultado apuntado en el comentario de cabecera del borrador, nivel por
   nivel. El gate vive en el repo privado a propósito: para explicar qué no se
   publica hay que nombrar lo que no se publica.
6. **Dejar el borrador en `_drafts/`**, que está en `.gitignore`, con la
   estructura de cinco bloques y los huecos marcados `[ESCRIBE TÚ]`.

### La estructura de cinco bloques

1. Lo que esperaba · 2. Lo que me encontré (dato + gráfico) · 3. Cómo lo comprobé
(código reproducible) · 4. **Qué decidí y qué me costó** · 5. Qué me llevo (el
método, transferible).

El bloque 4 **siempre lo escribe Alejandro**. Los otros cuatro los puede montar
cualquiera con el material delante; el 4 es la entrada entera. En el borrador se
deja vacío con la materia prima ya decidida anotada dentro, para que no parta de
cero — pero no se redacta.

### Regla que no se negocia

El andamiaje es de la IA; **la voz es suya**. Si un párrafo suena a asistente,
está mal aunque sea correcto.

## Este repo es PÚBLICO

No es un detalle de configuración: condiciona qué fichero puede existir aquí.
`_drafts/` no lo construye Jekyll, pero eso solo lo oculta del sitio web — en
GitHub lo lee cualquiera. Un fichero no publicado no es un fichero privado.

Por eso `_drafts/` está en `.gitignore` y el gate de publicación vive en el repo
privado. Lo único que sube de una entrada es el `.md` final en `_posts/`, ya sin
comentarios de andamiaje, sin nombres de terceros y sin notas de criterio.

**Antes de commitear cualquier fichero nuevo, la pregunta es la misma que para un
post: ¿esto lo puede leer cualquiera?**

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
