---
title: "Ejemplo: automatización del catálogo SAP → PIM"
resumen: "Ficha de andamiaje. Muestra todos los campos disponibles en un proyecto. Bórrala o reescríbela antes de publicar."
disciplina: Datos
anyo: 2025
cliente: "Distribución FMCG"
rol: "Diseño del flujo y desarrollo"
stack: [Oracle, PL/SQL, Python, Sales Layer]
resultado: "~9.300 materiales gobernados desde una única fuente"
destacado: true
# portada: /assets/img/proyecto-catalogos.jpg
# portada_alt: "Descripción de la imagen para lectores de pantalla"
# enlace: https://ejemplo.com
# enlace_texto: "Ver el repositorio"
---

{% comment %}
Esta ficha existe para ver la plantilla con contenido real. Bórrala antes de publicar.
Campos: title, resumen, disciplina, anyo, cliente, rol, stack, resultado, destacado,
portada, portada_alt, enlace, enlace_texto. Todos opcionales salvo title y disciplina.

`disciplina` tiene que coincidir con una de las declaradas en proyectos.html
(Datos / Marca / Dirección de arte) o el proyecto no aparecerá en el listado.
`destacado: true` lo saca en la portada.
{% endcomment %}

## El problema

Una línea por proyecto explicando qué estaba roto antes. Concreto, con el número
si lo hay. No "mejorar la eficiencia" sino "el catálogo se montaba a mano y el
PIM iba tres semanas por detrás de SAP".

## Qué hice

El mecanismo, no el adjetivo. Aquí es donde un portfolio de datos se diferencia
de uno de diseño: se puede enseñar la arquitectura.

```sql
-- Un fragmento representativo vale más que un párrafo describiéndolo.
create materialized view mv_golden_table as
select ...
```

## El resultado

Qué cambió y cómo se mide. Si no hay número, di por qué no lo hay — es más
creíble que inventarlo.

## Lo que aprendí

La parte que un cliente no puede copiar: el criterio. Por ejemplo, que el estado
de vida se evalúa a nivel EAN y no a nivel de material SAP, porque un EAN tiene
sustitutivos. Eso no está escrito en ninguna documentación.
