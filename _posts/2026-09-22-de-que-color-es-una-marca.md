---
title: "De qué color es una marca, según su propia web"
resumen: "Tenía que rehacer un deck de 34 slides respetando la marca de un cliente. En vez de sacar los colores a ojo del manual, abrí su web con un navegador automatizado y conté lo que pinta de verdad. Aparecieron valores que nadie había decidido."
tags: [marca, proceso, playwright]
---

Tenía que rehacer un deck de 34 slides para una marca de gran consumo. Los
mismos mensajes, toda la dirección visual nueva. El encargo venía con lo
habitual: el PowerPoint viejo, un manual de marca en PDF y una muestra de seis
slides de cómo querían que quedara.

Lo normal a partir de ahí es abrir PowerPoint, poner la web del cliente al lado
y sacar los colores a ojo con el cuentagotas. Lo he hecho muchas veces. Funciona
hasta la tercera ronda de correcciones, que es cuando alguien pregunta de dónde
ha salido ese azul y nadie se acuerda.

## Lo que esperaba

Que el manual de marca me diera los valores y el trabajo fuera de maquetación.

Un manual de marca describe la marca quieta: el logo, la paleta, la tipografía,
los márgenes de respeto. Está bien hecho y normalmente está desactualizado, no
porque el diseñador se equivocara, sino porque se escribió una vez y la empresa
siguió publicando cosas después.

Así que antes de abrir PowerPoint fui a mirar qué estaba publicando la web.

## Lo que me encontré

Abrí las 14 páginas del sitio con un navegador automatizado y, en vez de leer el
código fuente, le pregunté al navegador por los valores **ya calculados**: de qué
color está pintando cada texto y cada fondo en el momento en que la página se ve
en pantalla.

Esa distinción es la que hace que esto funcione, y merece dos frases para quien
no venga de programar. El código de una web no dice de qué color es un titular:
dice qué reglas se le aplican. Esas reglas se pisan unas a otras, vienen de
varios ficheros, algunas dependen del tamaño de la pantalla y otras las añade un
plugin al vuelo. El color final es el resultado de todo eso junto, y solo existe
cuando la página está pintada. Preguntárselo al navegador es preguntar por el
resultado, no por la receta.

Lo interesante no fue la lista de colores. Fue **cuántas veces** aparece cada uno.

Un color que sale una vez en todo el sitio y un color que estructura la mitad de
las páginas no son lo mismo, y en una paleta de manual ocupan el mismo espacio.
Contar frecuencias separa "esto lo usan" de "esto lo decidieron alguna vez". En
el proyecto del cliente esa cuenta dio el argumento entero de la conversación
posterior.

Como no puedo enseñar sus números, lo he corrido contra mi propio sitio, este
mismo. Cuatro colores, y el orden importa:

```
  20 rgb(22, 22, 26)
  18 rgb(85, 85, 95)
   4 rgb(0, 0, 0)
   1 rgb(251, 251, 249)
```

Tres de esos cuatro están declarados en mi hoja de estilos: mi tinta (`#16161a`,
los 20 usos), mi tinta suave (`#55555f`) y mi fondo (`#fbfbf9`). El que falta es
el negro puro, que no aparece en ningún sitio de mi CSS y aun así mi web lo pinta
cuatro veces. Lo pone el navegador por su cuenta, en los elementos que mis reglas
no llegan a cubrir.

Nadie decidió ese negro. Está ahí porque es el valor por defecto de la
herramienta, que es como acaban dentro de una marca la mayoría de las cosas que
nadie eligió.

## El proceso entero, de un vistazo

Antes de bajar al detalle, el mapa. Cuatro carriles: lo que aporta el cliente, lo
que mide la máquina, lo que se decide a mano y lo que se produce.

<figure>
  <img src="{{ '/assets/img/pipeline-marca-deck.png' | relative_url }}"
       alt="Esquema del proceso en cuatro carriles: material de partida, medición y sistema de marca, control, y producción del deck">
  <figcaption>El único paso que no automatiza nada es el de "decisión humana", y es
  el que sostiene los demás.</figcaption>
</figure>

## Cómo lo comprobé

El script entero son treinta líneas. Corre sobre cualquier URL pública, así que
puedes pasarlo por tu propia web mientras lees.

```js
import { chromium } from 'playwright';

const url = process.argv[2];
const navegador = await chromium.launch();
const pagina = await navegador.newPage();
await pagina.goto(url, { waitUntil: 'networkidle' });

const uso = await pagina.evaluate(() => {
  const cuenta = {};
  const apunta = (valor) => {
    if (!valor || valor === 'rgba(0, 0, 0, 0)') return;
    cuenta[valor] = (cuenta[valor] || 0) + 1;
  };
  for (const el of document.querySelectorAll('*')) {
    const estilo = getComputedStyle(el);
    if (el.textContent.trim()) apunta(estilo.color);
    apunta(estilo.backgroundColor);
  }
  return cuenta;
});

const orden = Object.entries(uso).sort((a, b) => b[1] - a[1]);
for (const [color, veces] of orden.slice(0, 8)) {
  console.log(String(veces).padStart(4), color);
}
await navegador.close();
```

La pieza importante es `getComputedStyle`: la función del navegador que devuelve
el valor final de una propiedad después de aplicar todas las reglas. Y
`rgba(0, 0, 0, 0)` se descarta porque significa transparente, no negro.

Con la medición hecha, el resultado no fue una paleta. Fue una tabla con 60
valores donde **cada uno lleva anotado de dónde viene**. Cuatro orígenes
posibles:

| Origen | Qué significa |
|---|---|
| `medido` | Está en la web y el sitio lo usa |
| `enviado` | Lo mandó el cliente en su muestra |
| `calculado` | Lo he calculado yo para que el texto se lea sobre ese fondo (contraste AA) |
| `provisional` | Me lo he inventado porque hacía falta y nadie lo había decidido |

Esa última columna es la que se salta todo el mundo, y es la que evita la
discusión de la ronda tres. Un valor sin origen no se puede defender ni corregir:
cuando el canónico dice 24 píxeles y el código hace 16, sin esa columna nadie
sabe si es un fallo o una decisión.

Con la tabla montada, las slides las genera un programa que la lee. Cambias un
valor y las 34 se rehacen. Y antes de entregar pasa un corrector automático que
comprueba que no se haya colado un color o una palabra que la marca tenga
prohibidos, porque los fallos de marca no viven donde uno mira: viven en el
metadato de la página, en el `<title>`, en un carácter tipográfico.

## La prueba: la misma slide, dos marcas

Hasta aquí suena a teoría, así que lo he montado con mis dos marcas, que son las
únicas cuyos valores puedo enseñar enteros. Vertienza es un estudio de branded
content. Sapioverse es un producto de software. Nada que ver una con otra.

Las dos slides que siguen salen del **mismo fichero de código**, con el mismo
texto y la misma composición. Lo único que cambia entre una y otra es qué ficha
de valores se le pasa por línea de comandos.

<figure>
  <img src="{{ '/assets/img/slide-vertienza.png' | relative_url }}"
       alt="Slide con fondo crema, titular en serif verde oscuro y etiqueta en cobre">
  <figcaption>Vertienza: crema, serif, cobre. Todo sale de su ficha.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/slide-sapioverse.png' | relative_url }}"
       alt="La misma slide con fondo blanco azulado, titular en grotesca y acentos en azul">
  <figcaption>Sapioverse: el mismo código, otra ficha. No se tocó una línea de HTML.</figcaption>
</figure>

Lo que el programa imprime al generarlas:

```
Vertienza:  fondo #F4F0E9 · tinta #152420 · acento #C07B5B · "Century Schoolbook"
Sapioverse: fondo #F8FAFC · tinta #0F172A · acento #2563EB · "Inter"
```

Un apunte de honestidad sobre esa segunda captura: la ficha de Sapioverse pide
Inter y yo no la tengo instalada en este portátil, así que lo que se ve es la
grotesca de sistema, el primer recambio que declara la propia ficha. Es
exactamente lo que le pasaría al cliente que abre el PowerPoint sin las fuentes
instaladas, y por eso los recambios se declaran en la ficha en vez de dejárselos
al azar.

Aquí está la parte que sí requiere criterio, y que conviene no esconder: **el
mapeo de papeles**. Una ficha de marca no viene con una etiqueta que diga "este
es el color de fondo de una slide". Viene con nombres propios de esa marca.
Alguien tiene que decidir qué token hace de qué en este formato concreto:

```js
const papeles = {
  vertienza:  { fondo: 'color.neutral.cream', acento: 'color.accent.copper',
                display: 'typography.fontFamily.display' },
  sapioverse: { fondo: 'color.paper.base',    acento: 'color.brand.600',
                display: 'typography.fontFamily.sans' },
};
```

Son seis líneas y son el trabajo entero. El resto (leer el JSON, resolver las
referencias entre tokens, pintar el HTML, exportar el PNG) es mecánica que se
escribe una vez.

Fíjate en una cosa de las dos capturas: no hay ningún valor hexadecimal escrito a
mano en la plantilla. Si mañana Vertienza cambia su cobre, cambia en el JSON y
las slides salen con el cobre nuevo sin que nadie abra el HTML.

## Qué me llevo

Tres cosas que me valen para el próximo proyecto, tenga deck o no.

**Contar, no listar.** Una paleta enumera los colores que existen sin decir cuáles
sostienen el sitio. La cuenta de usos sí: en mi web, mi tinta aparece 20 veces y
el negro que nadie decidió, 4. Con esos números la conversación deja de ser sobre
gustos. En una marca más grande que la mía, con un sitio de cientos de páginas,
esa proporción puede darse la vuelta, y ahí es donde el dato vale dinero.

**Anotar el origen de cada valor.** Cuesta diez minutos mientras montas la tabla
y ahorra la conversación entera de la tercera ronda.

**Distinguir un retrato de un canónico.** Esto es lo que más me costó entender.
Lo que sale de medir la web de alguien es un retrato: una foto de lo que hace
hoy, tomada desde fuera. No es su sistema de marca, porque nadie de esa casa lo
ha decidido ni aprobado. En pantalla los dos documentos se parecen muchísimo, y
por eso hay que escribir cuál es cuál en la primera línea: un retrato sirve para
trabajar y para argumentar, pero no puede citarse como si fuera la marca.

Lo que no resuelve nada de esto: medir no elige. Cuando dos fuentes se
contradicen, la decisión es de quien manda en la marca, y si hay dos dueños, de
los dos.
