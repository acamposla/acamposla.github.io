# Estado de la conversacion

Ultima sesion: 2026-08-03 (madrugada). Estado volatil — el criterio estable vive
en `CLAUDE.md`, no aqui.

## Donde quedo

El sitio esta **en linea y funcionando**: https://alejandrocamposlamas.com

Cadena verificada de punta a punta en una sesion:

| Pieza | Estado |
|---|---|
| Dominio | Registrado en Cloudflare Registrar (a coste, auto-renovacion activa) |
| DNS | 4 A del apex a GitHub Pages + `www` CNAME, los 5 **sin proxy** |
| Repo | `acamposla/acamposla.github.io`, publico, rama `main` |
| Pages | Activo, build `built` sin errores |
| Certificado | Aprobado, *Enforce HTTPS* activado |
| Redirecciones | `http://` → `https://` y `www` → apex, ambas 301 |
| Indexacion | **Bloqueada** por `noindex: true` |

## Lo siguiente, por orden

1. **Contenido real.** Borrar `_posts/2026-08-02-ejemplo-*` y
   `_proyectos/ejemplo-*`, y reescribir `sobre-mi.md` — ese borrador lo redacto
   Claude desde la nota de identidad del vault, la voz tiene que ser de Alejandro.
2. **Quitar `noindex: true`** de `_config.yml` el dia del lanzamiento real. Hasta
   entonces el sitio es visible pero ningun buscador lo toca.
3. **Verificar el dominio en GitHub** (Settings → Pages → Verified domains).
   Devuelve un registro TXT que se puede meter en Cloudflare por API con el token
   `claude` de 1Password. Impide que alguien reclame el dominio si el repo se
   desconfigura.

## Trampas que ya costaron tiempo

- **El proxy de Cloudflare.** Dos de los cuatro registros A se quedaron en naranja
  al crearlos a mano. Con el proxy activo GitHub no valida el dominio y no emite
  certificado — y ademas vuelve a fallar en cada renovacion, meses despues.
  Verificar siempre con `dig +short alejandrocamposlamas.com A`: si devuelve algo
  que no sean las cuatro IPs `185.199.10x.153`, hay un proxy encendido.
- **Orden al conectar el dominio.** El fichero `CNAME` se crea DESPUES de que el
  DNS resuelva. Al reves, GitHub redirige el `.github.io` al dominio nuevo y el
  sitio queda caido hasta que propague.
- **No hay Jekyll en local.** El Ruby del sistema es el 2.6 y no vale para el gem
  `github-pages`; no hay Docker. El build real solo se comprueba al hacer push
  (`gh api repos/acamposla/acamposla.github.io/pages/builds/latest`). Si se quiere
  previsualizar en local, `brew install ruby` — instrucciones en el README.

## Fuera de alcance de este repo

Salio en la misma sesion y no pertenece aqui, pero conviene no perderlo:
`trypredictaflow.com` tiene la **auto-renovacion desactivada** y caduca el
2027-05-26. Comprobar si es deliberado por la refundacion a Vertienza.
