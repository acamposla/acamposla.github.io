# Contexto de conversación

Última actualización: 2026-11-09, Alejandro

## Web bilingüe y piezas del portfolio
**Último en tocarlo:** Alejandro, 2026-11-09 · **Estado:** abierto
- Dónde quedó: web ES/EN en marcha con seis piezas publicadas en ambos idiomas
  (detalle técnico en `CLAUDE.md`, sección bilingüe). Portada con destacados por
  `orden`. Hechas unas 30 correcciones de ortografía, inglés y coherencia entre idiomas.
  Último commit: `8d80425`.
- Problemas abiertos: Alejandro debe contestar la lista de afirmaciones a confirmar
  (`revision/afirmaciones-2026-11-09.md` en el repo portfolio). Según responda puede
  haber que tocar piezas, "Sobre mí" ("doce años" contra cuatro más siete) y la marca de Edgewell.
  Orden de destacados sin confirmar.
- Próximo paso: leer sus respuestas a esa lista y aplicar los cambios; luego confirmar el orden de la portada.

## Contexto anterior (2026-09-25, sin clasificar)
**Último en tocarlo:** sesión del 2026-09-25 · **Estado:** parcialmente superado
- El punto 1 de "Lo siguiente" (primera ficha real) ya está hecho: hay seis piezas.
  Los puntos 2 a 4 siguen vigentes salvo que se haya hecho fuera de este repo.

## Donde quedo

Publicado hoy (commit `6233033`, verificado en vivo):

- **Previews del blog.** Cada entrada lleva `image` (PNG 1200x630, og:image) y
  `miniatura` (WebP). Blog y portada las pintan via `_includes/entrada-listado.html`.
  Las dos entradas reales ya tienen la suya.
- **Portfolio** en `/portfolio/` (antes `/proyectos/`, que ahora da 404). Con
  `_proyectos/` vacio muestra "En preparacion" con tres piezas de
  `_data/portfolio_proximamente.yml`.
- **Alineacion con LinkedIn**: tagline, description y `sobre-mi.md` reescritos
  desde el "Acerca de" publicado. Borrador aprobado.
- **Andamiaje borrado**: la entrada y la ficha de ejemplo.
- **Bug de `.prosa`** arreglado: los parrafos de toda la prosa salian pegados.
- `scripts/` fuera del sitio generado.

## Lo siguiente, por orden

1. **Primera ficha real de portfolio.** Al crear el primer `_proyectos/*.md`,
   `/portfolio/` vuelve sola a la rejilla por disciplina; quitar esa pieza de
   `_data/portfolio_proximamente.yml`.
2. **Nombre visible en LinkedIn** ("Alejandro Campos" frente a "Alejandro Campos
   Lamas" en la web): lo cambia Alejandro en LinkedIn. En la web no se toca.
3. **`noindex: true` sigue activo a proposito.** Quitarlo el dia del lanzamiento.
4. **Verificar el dominio en GitHub** (Settings, Pages, Verified domains).

## Trampas que ya costaron tiempo

- **El proxy de Cloudflare.** Dos de los cuatro registros A se quedaron en naranja
  al crearlos a mano. Con el proxy activo GitHub no valida el dominio y no emite
  certificado — y ademas vuelve a fallar en cada renovacion, meses despues.
  Verificar siempre con `dig +short alejandrocamposlamas.com A`: si devuelve algo
  que no sean las cuatro IPs `185.199.10x.153`, hay un proxy encendido.
- **Orden al conectar el dominio.** El fichero `CNAME` se crea DESPUES de que el
  DNS resuelva. Al reves, GitHub redirige el `.github.io` al dominio nuevo y el
  sitio queda caido hasta que propague.
- **Estado del build de Pages:** `gh api repos/acamposla/acamposla.github.io/pages/builds/latest`.
  Local con Ruby 3.1, ver `CLAUDE.md`.
- **Playwright desde `scripts/`:** los `.mjs` son ESM y no respetan `NODE_PATH`.
  Para `render-previews.mjs`, symlink temporal `node_modules` a
  `~/dotfiles/claude/skills/brand-assets/scripts/node_modules`, ejecutar y borrar.

## Fuera de alcance de este repo

Salio en la misma sesion y no pertenece aqui, pero conviene no perderlo:
`trypredictaflow.com` tiene la **auto-renovacion desactivada** y caduca el
2027-05-26. Comprobar si es deliberado por la refundacion a Vertienza.
