# acamposla.github.io

Blog y portfolio de Alejandro Campos Lamas. Jekyll servido por GitHub Pages.

Dos tipos de contenido distintos, cada uno con su plantilla:

- **Entradas** (`_posts/`) — cronológicas, con fecha en la URL. Van a `/blog/`.
- **Proyectos** (`_proyectos/`) — colección atemporal con ficha técnica
  (cliente, rol, herramientas, resultado). Van a `/portfolio/`.

## Publicar un proyecto

Crea `_proyectos/slug-del-proyecto.md` (sin fecha en el nombre):

```yaml
---
title: "Nombre del proyecto"
resumen: "Una frase para la tarjeta del listado."
disciplina: Datos          # Datos | Marca | Dirección de arte
anyo: 2025
cliente: "Quién"
rol: "Qué hiciste tú"
stack: [Oracle, Python]
resultado: "El número, si lo hay"
destacado: true            # lo saca en la portada
portada: /assets/img/slug.jpg
portada_alt: "Descripción para lectores de pantalla"
---
```

`disciplina` debe coincidir con una de las declaradas en `portfolio.html`, o el
proyecto no aparece en el listado. El orden de las disciplinas se declara ahí a
mano: manda la narrativa, no el alfabeto.

Mientras `_proyectos/` no tenga ninguna ficha, `/portfolio/` muestra el estado
"en preparación": la entradilla y las piezas de `_data/portfolio_proximamente.yml`.
Con la primera ficha vuelve sola a la rejilla por disciplina.

## Publicar una entrada

1. Crea `_posts/AAAA-MM-DD-slug.md` (el nombre del fichero fija fecha y URL).
2. Front matter mínimo:
   ```yaml
   ---
   title: "Titular"
   resumen: "Una frase para el listado y la entradilla."
   tags: [datos, margen]
   image:                    # preview: og:image al compartir (LinkedIn) y miniatura
     path: /assets/img/previews/slug.png   # PNG o JPG 1200x630, LinkedIn no lee bien WebP
     width: 1200
     height: 630
     alt: "Qué se ve en la imagen"
   miniatura: /assets/img/previews/slug.webp  # opcional, versión ligera para el listado
   ---
   ```
   Sin `image` ni `miniatura` la entrada se lista solo con texto. Las previews
   se generan con `scripts/previews/render-previews.mjs` (lienzos en
   `scripts/previews/previews.html`).
3. `git add . && git commit -m "post: titular" && git push`

GitHub construye el sitio solo. Sin Actions, sin build local, sin dependencias.
Tarda entre 30 segundos y 2 minutos.

Borradores: `_drafts/nombre-sin-fecha.md`. No se publican.

## Estructura

```
_config.yml     Configuración del sitio (título, URL, colecciones, plugins)
_layouts/       default (esqueleto) · post · proyecto · page
_includes/      fecha.html (fechas en español) · entrada-listado.html (entrada con miniatura)
_data/          portfolio_proximamente.yml (piezas en preparación)
_posts/         Entradas publicadas
_drafts/        Entradas sin publicar
_proyectos/     Fichas de portfolio
assets/css/     main.css — todo el diseño, un solo fichero
assets/img/     Imágenes de proyectos
index.html      Portada: bio + trabajo destacado + últimas entradas
portfolio.html  Portfolio: en preparación o agrupado por disciplina
blog.html       Archivo del blog agrupado por año
sobre-mi.md     Página de perfil
```

## Imágenes

El repo tiene un límite de 1 GB y Pages ~100 GB/mes de tráfico. Un portfolio con
imágenes sin optimizar se los come. Antes de subir: exporta a **WebP**, ancho
máximo 1600 px, y comprueba que cada fichero baje de ~200 KB.

```bash
# macOS trae sips; para WebP conviene cwebp (brew install webp)
cwebp -q 82 -resize 1600 0 original.jpg -o assets/img/slug.webp
```

## Previsualizar en local (opcional)

No hace falta para publicar. El Ruby del sistema (2.6) es demasiado viejo para
el gem `github-pages`; requiere Ruby 3.x:

```bash
brew install ruby
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle install
bundle exec jekyll serve --livereload   # http://localhost:4000
```

## Dominio propio: alejandrocamposlamas.com

Orden obligatorio. Si se crea el fichero `CNAME` antes de que el DNS resuelva,
GitHub redirige `acamposla.github.io` al dominio nuevo y el sitio queda caído
hasta que propague.

1. **Registrar** `alejandrocamposlamas.com`.
2. **DNS** — apex `@` → 4 registros A, con el **proxy desactivado** (nube gris
   en Cloudflare); con el proxy activo GitHub no puede emitir el certificado:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
   Y `www` → CNAME → `acamposla.github.io`.
3. **Comprobar** que resuelve antes de seguir:
   ```bash
   dig +short alejandrocamposlamas.com A
   ```
4. **Repo**: crear `CNAME` en la raíz con una sola línea —
   `alejandrocamposlamas.com` — y cambiar `url:` en `_config.yml` a
   `https://alejandrocamposlamas.com`. Push.
5. **Settings → Pages**: marcar *Enforce HTTPS* cuando el certificado esté listo
   (tarda entre minutos y una hora).
6. Opcional pero recomendado: **Settings → Pages → Verified domains** en el
   perfil de GitHub, para que nadie pueda reclamar el dominio si algún día se
   desconfigura el repo.
