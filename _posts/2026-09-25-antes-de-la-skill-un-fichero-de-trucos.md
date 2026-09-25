---
title: "Antes de la skill, un fichero de trucos"
resumen: "Claude conectado por MCP a Higgsfield, un agregador de modelos de imagen y vídeo. Pides dos packshots del mismo producto y salen dos etiquetas distintas. Cómo meter un control de calidad e iterar hasta tener tu propia skill."
tags: [ia, proceso, skills]
---

Un amigo lleva un par de semanas usando Claude y me pidió una llamada para
"hacerlo ordenado". Quería que Claude, conectado a Higgsfield (un generador de
imágenes), le sacara dos fotos de un producto desde dos ángulos, a partir de
fotos reales. En cada foto salió un producto distinto.

Higgsfield es un agregador: reúne en un solo sitio modelos de imagen y vídeo de
varios fabricantes, y tiene un MCP para que Claude lo maneje. Con eso, Claude
puede elegir el modelo, lanzar la generación y recoger el resultado sin que tú
abras la web. Es una combinación muy útil para un equipo de marketing, y es
también donde más se nota la falta de un control de calidad.

Lo cuento con un encargo de marca, porque el fallo es el mismo y es el que más
veo en equipos de marketing: dos packshots de un producto para una campaña, de
frente y en tres cuartos, a partir de fotos del envase. La marca, Olmo, es
inventada. El proceso es el que le expliqué a él; pasa el ratón o toca cada paso.

{% include diagrama-encargo-skill.html %}

Las imágenes que siguen son recreaciones de la pantalla con ese ejemplo. No hice
capturas durante la llamada.

## Un conector es un diccionario de funciones

Le pedí que abriera Higgsfield a pelo, sin Claude. Un cuadro de texto y una fila
de controles: modelo, proporción, calidad, resolución, cuántas imágenes. Cada
control es un parámetro, y el botón de generar es una función que los recoge. El
primero de la fila es el que más pesa: al ser un agregador, el mismo cuadro de
texto sirve para modelos distintos (en la captura, GPT Image 2, de OpenAI), y
cada uno resuelve el mismo prompt a su manera.

<figure>
  <img src="{{ '/assets/img/encargo-a-skill/higgsfield.webp' | relative_url }}" width="704" height="206" loading="lazy"
       alt="Barra de generación de Higgsfield: cuadro de texto y controles de modelo (GPT Image 2), proporción (Auto), calidad (High), resolución (2K) y número de imágenes (1/4), con el botón Generate">
  <figcaption>Recreación. Higgsfield usado a mano: cada control es un parámetro de la función de generar.</figcaption>
</figure>

Un MCP es un conector que le da a Claude acceso a una herramienta para que haga
cosas en ella, y no solo hable. Por dentro es un fichero que alguien ha escrito
para decirle: existe una función de generar, admite un texto, un modelo, una
calidad, una proporción. Claude lee tu petición y rellena esos campos. Lo vimos
en directo en la ventana de permisos:

<figure>
  <img src="{{ '/assets/img/encargo-a-skill/permiso.webp' | relative_url }}" width="704" height="425" loading="lazy"
       alt="Ventana de Claude pidiendo permiso para usar la herramienta generate_image de Higgsfield, con el prompt del packshot y los parámetros model, aspect_ratio auto, quality low e input_images">
  <figcaption>Recreación. Los mismos controles, rellenados por Claude. El "auto" es el mismo de la web.</figcaption>
</figure>

A mi amigo le habían dicho que "con los conectores pierdes el control". No lo
pierdes: lo delegas. Si no dices qué calidad quieres, Claude elige una. Con
herramientas de cientos de parámetros eso ayuda; otras veces decide algo que tú
no habrías decidido.

Hay un matiz que casi nadie mira: el conector no siempre trae todas las funciones
de la herramienta. Higgsfield tiene un modo de retoque (inpainting) para corregir
solo un trozo de la foto. Si el conector no lo expone, cuando le pides a Claude
que arregle el logo vuelve a tirar la foto entera, y con ella cambian la
etiqueta, el color y la luz. Yo con Higgsfield uso su API, que expone más
funciones que el conector. Lo sé porque le pedí a Claude que comparase la
documentación de la herramienta con las funciones que tenía y me dijera cuáles le
faltaban, y esa pregunta la puede hacer cualquiera sin saber programar.

## Preguntar antes de dejarle hacer

El encargo va dictado por voz, que deja salir más contexto que escribiendo, con
las dos fotos de referencia adjuntas y cuatro condiciones que valen para
cualquier encargo:

<figure>
  <img src="{{ '/assets/img/encargo-a-skill/dictado.webp' | relative_url }}" width="704" height="363" loading="lazy"
       alt="Compositor de Claude en modo Cowork con dos fotos del envase adjuntas y el encargo dictado: dos packshots de la botella para la campaña, decir qué modelo y por qué, borrador en baja calidad, explicar el prompt y las funciones usadas, y avisar si algo del plan no convence">
  <figcaption>Recreación. El encargo, dictado, con las condiciones al final.</figcaption>
</figure>

Pedirle que razone la elección del modelo cambia el resultado más de lo que
parece. Sin esa pregunta tiende a lanzar lo primero que encaja; con ella compara,
y a veces se corrige solo.

## El becario que te trae lo que le dio el proveedor

Los dos borradores llegan en un par de minutos y son bonitos. Cada uno con su
propia etiqueta.

<figure>
  <img src="{{ '/assets/img/encargo-a-skill/borradores.webp' | relative_url }}" width="704" height="354" loading="lazy"
       alt="Respuesta de Claude con los dos borradores de la botella: de frente con etiqueta verde y el logo OLMO bien escrito; en tres cuartos con etiqueta naranja y el logo mal escrito, OMLO">
  <figcaption>Recreación esquemática. Dos ángulos, dos etiquetas: dos productos distintos.</figcaption>
</figure>

El modelo que eligió Claude dentro de Higgsfield genera la imagen siguiendo sus
instrucciones, y es Claude quien te la entrega. Lo que falta es que Claude pase un
control de calidad antes de enseñarte nada. Es como con un becario: si lo mandas a
por algo y el proveedor le da una chapuza, quieres que la revise y la devuelva
antes de traértela.

Con un agregador esto importa más que con una sola herramienta. Cada modelo falla
a su manera (uno escribe mal el texto de la etiqueta, otro cambia los colores,
otro inventa detalles del envase), y quien elige el modelo es Claude. Sin control
de calidad, cada fallo lo descubres tú y lo corriges tú, vuelta a vuelta. Con él,
Claude revisa, vuelve a pedir, y a ti te llega la versión que ya ha pasado.

Aquí la regla cabe en una línea: si se piden varias tomas del mismo producto,
tiene que ser el mismo producto en todas (etiqueta, logo, colores de marca), y si
no lo es, se vuelve a pedir. Tarda un poco más y llega mejor a la primera. Para
una marca hay una segunda regla que conviene apuntar desde el primer día: el logo
no se genera, se compone encima con el archivo real.

## Del fichero a la skill

Mi amigo salió de la llamada queriendo crearse skills (instrucciones empaquetadas
que Claude carga solo cuando la conversación las necesita): una de piel perfecta
para retratos, otra de iluminación de estudio. Le frené un paso. Antes de una
skill va un fichero en la carpeta del proyecto, donde al acabar cada sesión le
pides a Claude que apunte qué ha funcionado y qué no.

<figure>
  <img src="{{ '/assets/img/encargo-a-skill/aprendizajes.webp' | relative_url }}" width="704" height="376" loading="lazy"
       alt="Editor con el fichero aprendizajes.md: reglas sobre tomas del mismo producto, el logo compuesto con el archivo real, retoque en lugar de regenerar, elegir modelo antes de generar y borrador en baja calidad">
  <figcaption>Recreación. Lo que queda apuntado de la sesión.</figcaption>
</figure>

Dentro de tres meses no te vas a acordar de cómo lo resolviste, y Claude tampoco.
El fichero crece por iteración. La primera sesión deja una regla escrita deprisa.
En la segunda y la tercera, esa regla se confirma, se corrige o se afina: qué
modelo funcionó mejor con etiquetas con texto, qué comprobar exactamente, qué
hacer cuando falla. Cuando una regla ha aguantado varios encargos, pasa a la skill
con la redacción exacta que funcionó:

```markdown
---
name: packshots-de-marca
description: Packshots de producto con Higgsfield. Usar cuando se pidan
  fotos de un envase para campaña, web o marketplace.
---
1. Antes de generar, di qué modelo vas a usar y por qué. Para etiquetas
   con texto, empieza por el que mejor resultado dio en aprendizajes.md.
2. Primero un borrador en baja calidad. Alta solo con visto bueno.
3. El logo se compone encima con el archivo real de /marca.
4. Control de calidad antes de entregar: en todas las tomas, misma
   etiqueta, mismo logo, mismos colores de marca. Si una falla, corrige
   la zona con retoque (inpaint) y vuelve a comprobar.
5. Al cerrar, añade a aprendizajes.md lo que funcionó y lo que falló.
```

Normalmente empiezas con una skill grande (Higgsfield, calidad, piel, luz, todo
junto) y un día pesa tanto que hay que partirla.

El fichero, además, no ocupa sitio en la cabeza de la IA. Si le dejas escrito
"antes de generar imágenes, lee este documento", solo lo abre cuando le toca, como
quien va a la estantería a por el manual de After Effects y lo vuelve a dejar.

Por eso me cuesta la memoria automática de ChatGPT, que era lo que le gustaba a su
otro amigo. Yo quiero saber exactamente qué tiene mi IA en memoria y qué va a
consultar, y eso solo lo sé si lo he escrito yo. Por lo mismo casi nunca me bajo
skills de terceros. Una skill es un texto, como una receta: son cuatro huevos y
tú querías dos. Si te bajas una que se llama "piel perfecta" y funciona, bien,
pero ábrela y léela antes de fiarte.

## Qué me llevo

Cuatro preguntas que ahora le haría a cualquier herramienta conectada, antes de
pedirle nada:

1. ¿Qué funciones tienes de esta herramienta y cuáles te faltan?
2. ¿Qué modelo o qué opción vas a usar y por qué?
3. ¿Qué vas a comprobar antes de enseñarme el resultado?
4. Al acabar: ¿qué hemos aprendido hoy que deba quedar apuntado?

La primera te dice qué tendrás que hacer a mano. La cuarta es la que va llenando
el `aprendizajes.md`.
