---
title: "Ejemplo: cómo se escribe una entrada"
resumen: "Entrada de andamiaje. Muestra el front matter disponible y cómo se ve cada elemento tipográfico. Bórrala antes de publicar el sitio."
tags: [meta]
---

Esta entrada existe solo para ver el diseño con contenido real. **Bórrala o
reescríbela antes de publicar.** El fichero vive en
`_posts/2026-08-02-ejemplo-como-se-escribe-una-entrada.md`.

El nombre del fichero manda: `AAAA-MM-DD-slug-en-minusculas.md`. La fecha sale
de ahí y el slug se convierte en la URL. Si el nombre no cumple ese patrón,
Jekyll ignora el fichero en silencio.

## El front matter

Es el bloque entre `---` al principio del fichero. Campos que entiende este sitio:

| Campo | Obligatorio | Qué hace |
|---|---|---|
| `title` | sí | Titular de la entrada y `<title>` de la página |
| `resumen` | no | Entradilla bajo el titular y texto del listado |
| `tags` | no | Etiquetas bajo la fecha |
| `layout` | no | Ya viene puesto por defecto en `_config.yml` |

Si no pones `resumen`, el listado usa el primer párrafo.

## Elementos

> Una cita se marca con `>` al principio de la línea. Sirve para el dato ajeno
> o la frase que sostiene el argumento.

Listas para lo enumerable:

- Un elemento
- Otro elemento
- Un tercero

Y código cuando toca enseñar el mecanismo, no describirlo:

```sql
select ean, count(*) as repeticiones
from reporting.materiales
group by ean
having count(*) > 1;
```

Términos sueltos en `código en línea`, enlaces [así](https://github.com/acamposla),
y `---` en una línea sola para separar bloques.

---

## Publicar

Guardas, `git add`, `git commit`, `git push`. GitHub construye el sitio y en un
par de minutos está en línea. No hay más pasos.

Para que una entrada no se publique todavía, muévela a `_drafts/` y quítale la
fecha del nombre: los borradores no se construyen.
