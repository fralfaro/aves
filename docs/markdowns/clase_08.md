# Colores e Ilusiones


A través del curso hemos visto que los colores expresan atributos a través de los canales. En la unidad de codificación visual definimos que el tono, la saturación y la luminosidad de los colores se utilizan para codificar valores cuantitativos o categóricos.

Solemos ser testigues del uso del color como expresión. Sin ir más lejos, la artista chilena [Matilde Pérez](https://es.wikipedia.org/wiki/Matilde_P%C3%A9rez), fallecida el año 2014, destacó por su uso de las formas geométricas y los colores como expresión de movimiento. Muchas de sus obras podrían ser visualizaciones de datos (quizás lo son, pero nunca lo sabremos):

![&ldquo;Sin título&rdquo;, Matilde Pérez.](../../../courses/infovis/09_colores/images/matilde_perez_hu9f4f671e8baaaf7ef0f8b71f746bc15f_2064450_660x0_resize_q75_box.jpg)

Sin título, Matilde Pérez.

La obra de Matilde Pérez que he mostrado _podría_ ser una visualización, una atractiva ciertamente. Si utilizásemos un criterio estético y expresivo (en un sentido artístico) haríamos visualizaciones hermosas, sin embargo corremos el riesgo de no respetar los principios de eficiencia y coherencia. Así, en esta unidad discutiremos brevemente cómo interpretamos la información, principalmente a través del color y de las formas geométricas. También veremos ejemplos de como nuestra mente interpreta fenómenos o cambios en las imágenes que realmente no están allí. El uso de colores y formas geométricas en visualización requiere que pensemos en quién hará uso de nuestras visualizaciones, que, como vimos en la unidad introductoria, es _otra persona_. Quien diseña visualizaciones debe tener en cuenta que al otro lado del medio en el que publicamos las personas pueden ver algo distinto de lo que vemos nosotros.

## Ejemplos de Uso de color 

Hasta ahora hemos utilizado el color de dos maneras: para codificar atributos categóricos y para codificar atributos cuantitativos. Un ejemplo de uso categórico es la siguiente `scatterplot_matrix` donde se utiliza el canal de tono para sobreponer distintas categorías en cada gráfico de la matriz:

![Utilizando colores para diferenciar categorías dentro del mismo gráfico. Fuente: <code>seaborn</code>](../../../courses/infovis/09_colores/images/iris_splom_hubd4b0f0c9cfbea5045000ce02f19d7a7_136885_660x0_resize_box_3.png)

Utilizando colores para diferenciar categorías dentro del mismo gráfico. Fuente: `seaborn`.

Este uso de los tonos es típico y adecuado. Usualmente quien diseña la visualización elige colores cuyos tonos se distingan fácilmente. En otras ocasiones, el color elegido para cada categoría se relaciona con la semántica de lo que es visualizado, como en este ejemplo de la visualización `circle_packing` aplicada a datos de Pokémon:

![Estos son los únicos Pokémon que reconozco, la primera generación. Fuente: @DataToViz](../../../courses/infovis/09_colores/images/pokemon_hu82dc4746ddf20f0bf2e1ab29f43503e7_2571613_660x0_resize_box_3.png)

Estos son los únicos Pokémon que reconozco, la primera generación. Fuente: @DataToViz.

También es posible que los colores estén relacionados con el mensaje que se está entregando. Esta visualización del [New York Times](https://www.nytimes.com/interactive/2020/09/02/upshot/america-political-spectrum.html?action=click&module=Top%20Stories&pgtype=Homepage) muestra el espectro político en Estados Unidos con colores distintos a sus típicos azul y rojo (para representar a demócratas y republicanes):

![Los verdaderos colores políticos de Estados Unidos. Fuente: New York Times.](../../../courses/infovis/09_colores/images/us_real_political_colors_hud75a2140b770b254f90613fcb6875f88_95772_660x0_resize_q75_box.jpg)

Los verdaderos colores políticos de Estados Unidos. Fuente: New York Times.

Este `normalized_stacked_area_chart` utiliza los colores de la superficie asociados a cada candidate presidencial. Gris es asfalto y cemento (ciudad), verde son bosques, azul es agua, etc. Se refiere a la división urbana/rural en las votaciones en Estados Unidos. Un uso novedoso y potente del color, no solo como canal de codificación visual, sino también de expresión de un mensaje.

Respecto al uso cuantitativo del color, de colores secuencial, es decir, aquellos donde la saturación o la luminosidad varían. La siguiente visualización que muestra la [población de una ciudad en 3D](https://pudding.cool/2018/12/3d-cities-story/) utiliza una paleta de colores secuencial para representar la cantidad de población en un espacio de la ciudad, en este caso, Santiago entre los años 1975 y 2015:

![Uso de paleta de colores secuencial para codificar atributos cuantitativos. Fuente: Population Mountains](../../../courses/infovis/09_colores/images/population_mountains_hu4d46243b6191dfc8d3227e36a9e62762_1641433_660x0_resize_box_3.png)

Uso de paleta de colores secuencial para codificar atributos cuantitativos. Fuente: Population Mountains.

Los mapas que hemos observado hasta ahora han sido bidimensionales. Si viésemos este mapa desde arriba, veríamos una grilla de cuadrados coloreados que nos permitirían entender la distribución geográfica de la población. Al ser un mapa tridimensional, donde hay barras con volumen en vez de celdas cuadradas, cuya altura codifica la cantidad de población, el color es un canal redundante puesto que expresa el mismo atributo. Sin embargo, es justamente esta redundancia la que permite entender la visualización, al proveer legibilidad a lo 3D, y, al mismo tiempo, le otorga atractivo estético.

El tono puede variar en una paleta que codifique colores secuenciales. Un ejemplo de uso estas paletas es el `normalized_stacked_area_chart` de [El Lenguaje de la Ciencia](https://www.scientificamerican.com/article/the-language-of-science/), una visualización que muestra la evolución del lenguaje empleado en los artículos de la revista Scientific American. Cada área en el gráfico representa la importancia de una palabra en cada año de publicación de la revista, considerando solamente las 1000 palabras más frecuentes. El orden de las áreas y el color de éstas codifican el año en que la palabra correspondiente tuvo su mayor frecuencia. Se ve así:

![The Language of Science. Fuente: Scientific American.](../../../courses/infovis/09_colores/images/scientific_american_hu88bb1d4af34726a1ef0d0621a2cf17fc_2906288_660x0_resize_q75_box.jpg)

The Language of Science. Fuente: Scientific American.

El ejemplo presenta un buen uso de los cambios de tono. Mi hipótesis sobre el uso de una paleta basada en tonos más que en saturación y luminosidad es que se buscaba mostrar la variación temporal sin implicar que unos años fuesen más importantes que otros, una interpretación común en las paletas de colores secuenciales. Sin embargo, es un desafío usar bien los tonos o matices de esta manera — un buen punto de partida son las paletas de colores _secuenciales y perceptualmente uniformes_, es decir, cuyas variaciones de tono en la paleta son constantes. En contraste, en una paleta de colores categórica se busca que los tonos sean diferentes, pero no tienen por qué ser _igualmente distintos_ entre sí.

Finalmente, recordemos que un atributo cuantitativo también puede ser divergente o bidireccional. En estos casos se suelen utilizar paletas de colores que mezclan dos paletas secuenciales, una para dirección de divergencia, partiendo de un punto central común. Como ejemplo veremos una visualización que ha tenido impacto en los últimos años, llamada [Warming Stripes](https://en.wikipedia.org/wiki/Warming_stripes). Esta visualización muestra la evolución de la temperatura promedio de un lugar (donde lugar puede ser el planeta, un continente, un país, una ciudad, etc.). Cada año se muestra como una marca rectangular (o una barra de tamaño constante), y el canal de color codifica su divergencia desde el promedio de todos los años. Pueden construir esta visualización para cualquier país del mundo en el sitio [#ShowYourStripes](https://showyourstripes.info/). A continuación, el de Chile:

![Evolución de temperatura promedio en Chile. Fuente: ShowYourStripes de Ed Hawkins con datos de Berkeley Earth.](../../../courses/infovis/09_colores/images/_stripes_SOUTH_AMERICA-Chile--1901-2019-BK-withlabels_hu7517afac12c0c214b9373b17ad6ec2ac_67237_660x0_resize_box_3.png)

Evolución de temperatura promedio en Chile. Fuente: ShowYourStripes de Ed Hawkins con datos de Berkeley Earth.

Las dos paletas secuenciales se basan en rojo (valores positivos, sobre el promedio) y azul (valores negativos, bajo el promedio). Un rojo más saturado implica mayor distancia desde el promedio, lo mismo un azul más saturado. El punto central es un gris donde ambos colores presentan ausencia de saturación. Estas visualizaciones tienden a mostrar una agrupación de colores azules a la izquierda y de colores rojos a la derecha, cuya saturación nos comunica la tendencia de aumento de temperaturas en las últimas décadas. Esta visualización ha sido portada de revistas (The Economist, por ej.), ha sido pintada en murales, hay personas que la utilizan de fondo de pantalla o de sus perfiles de redes sociales, o incluso han creado ropa u objetos inspirados en ella. Warming Stripes muestra que una buena visualización responde una pregunta específica y relevante utilizando una codificación visual adecuada para ello. No se necesita complejidad para causar impacto.

## Espacios de Color y Paletas de Colores 

Las definiciones de paletas de colores secuenciales, divergentes y categóricas se basan en como interpretamos la composición de los colores. Eso significa que existe una manera de representar un color que permite comparar y operar con sus componentes, de modo que podamos cuantificar esos tres aspectos. Un espacio de color se define como la manera de formalizar esos conceptos a través de la organización matemática de los colores. Así, podemos **representar** un color de acuerdo a un espacio específico.

Nuestra biología nos da una primera aproximación de lo que es un espacio de color. Nuestros ojos tienen dos tipos de células fotorreceptoras, los bastones y los conos. Estos últimos son los encargados de aportar la información del color, y hay de tres tipos: rojo (`R`), verde (`G`) y azul (`B`). Así, el espacio de color `RGB` define un espacio cúbico en el cual cada color es la suma ponderada de los tres colores primarios.

![Espacio de color RGB. Fuente: Wikipedia.](../../../courses/infovis/09_colores/images/color_rgb_huce01328d0f6f09ceb7884bf00d6c658b_460666_660x0_resize_box_3.png)

Espacio de color RGB. Fuente: Wikipedia.

`RGB` es el modelo de color más usado. Los colores de las páginas web se expresan usualmente en este espacio. En `matplotlib` también se usa `RGB`. Cuando se escoge un color en un programa, usualmente vemos las componentes `RGB` como opción por omisión.

Lamentablemente, a pesar de que nuestra biología funciona en `RGB`, no pensamos en `RGB`. ¿Alguna vez han descrito un color como “una mezcla de azul y verde”?¿O más bien han dicho algo “este morado intenso pero no muy oscuro”? Este tipo de descripciones, que son intuitivas para nosotros, son posibles de expresar en espacios de colores. Uno de ellos es conocido como `HSL`, que proviene de las siglas _hue_ (tono o matiz), _saturation_ (saturación) y _lightness_ (luminosidad). De acuerdo a Wikipedia, “el modelo `HSL` se representa gráficamente como un cono doble. Los dos vértices en el modelo `HSL` se corresponden con el blanco y el negro, el ángulo se corresponde con el matiz, la distancia al eje con la saturación y la distancia al eje blanco-negro se corresponde a la luminancia,” como se ve a continuación:

![Espacio de color <code>HSL</code>. Fuente: Wikipedia.](../../../courses/infovis/09_colores/images/color_hsl_hu464b4907a041bc3a38945618bc744479_1115058_660x0_resize_box_3.png)

Espacio de color `HSL`. Fuente: Wikipedia.

Las componentes de este espacio de color (sus _canales_) se relacionan directamente con los principios de efectividad y coherencia:

*   **¿qué? ¿dónde?** => categorías: matiz o tono (hue).
*   **¿cuánto?¿cómo?** => atributos cuantitativos: luminancia, saturación.

En contraste, los tres canales `RGB` no se relacionan con estos principios.

Teniendo en consideración la especificación colores de acuerdo a su posición en estos espacios, podemos definir lo que es una _paleta de colores_ o `colormap` (de allí los nombres de los parámetros `cmap` y `palette` en los métodos de `matplotlib` y `seaborn`). Hemos usado el término en las unidades anteriores y ésta de manera indiscriminada, con el supuesto de que nos referimos a un conjunto de colores que, a través de los canales de la visualización, utilizamos para expresar atributos en las marcas. Como base, partiendo de un tono específico, podemos definir estos `colormaps` a través de variaciones en cada uno de los canales:

![Paletas de colores donde varía un único canal. Fuente: Visualization Analysis &amp; Design.](../../../courses/infovis/09_colores/images/colormaps_hubb8465cfbc78fa7ebe0d6d276111412b_20116_660x0_resize_box_3.png)

Paletas de colores donde varía un único canal. Fuente: Visualization Analysis & Design.

Existen muchas [estrategias para construir paletas de colores utilizando las variaciones de los canales](http://www.personal.psu.edu/faculty/c/a/cab38/ColorSch/Schemes.html). Eso nos permite construir paletas para atributos binarios, paletas divergentes, paletas bivariable, que permiten expresar relaciones entre dos atributos, incluso considerando atributos cuantitativos y categóricos al mismo tiempo:

![Estrategias de construcción de paletas de colores. Fuente: Visualization Analysis &amp; Design, basado en trabajo de Cynthia Brewer.](../../../courses/infovis/09_colores/images/colormap_divergent_hu6d497c4878f3ee895cd3082a15ab6472_92492_660x0_resize_box_3.png)

Estrategias de construcción de paletas de colores. Fuente: Visualization Analysis & Design, basado en trabajo de Cynthia Brewer.

Ahora bien, al construir estas paletas más complejas debemos tener en cuenta no solo los principios de efectividad y coherencia, sino también la legibilidad y discriminabilidad de los colores. Por ejemplo, ¿Estamos utilizando marcas de tamaño variable? El tamaño de las marcas (por ejemplo, las áreas en un `choropleth_map`) afecta la percepción de color, particularmente la saturación: regiones pequeñas se ven más saturadas, regiones grandes se ven menos saturadas en comparación a sus regiones vecinas. ¿Cuántas categorías podemos mostrar? La discriminabilidad de los colores varía de acuerdo al contexto. En el siguiente gráfico de una publicación científica observamos que la distribución de los colores en el genoma de humanos y ratas no deja claro cuántos genes estamos analizando:

![Discriminabilidad varía de acuerdo al contexto. Fuente: Sinha and Meller, Cinteny: flexible analysis and visualization of synteny and genome rearrangements in multiple organisms.](../../../courses/infovis/09_colores/images/discriminability_hu88d589f998b798349ae59f82abca7636_67108_660x0_resize_box_3.png)

Discriminabilidad varía de acuerdo al contexto. Fuente: Sinha and Meller, Cinteny: flexible analysis and visualization of synteny and genome rearrangements in multiple organisms.

Una cantidad máxima aceptable de categorías cae entre 6 y 12. Más se vuelve imposible de percibir.

Construir paletas de colores categóricas basadas en tonos no es fácil. El investigador [Martin Krzywinski](http://mkweb.bcgsc.ca/brewer/) nos advierte sobre el cuidado que debemos tener a la hora de elegir tonos. Por ejemplo, un azul y un amarillo que tengan los mismos valores de saturación y luminosidad son percibidos de manera distinta:

![Azul y amarillo &mdash; un color predomina más. Fuente: Martin Krzywinski.](../../../courses/infovis/09_colores/images/yellow_brighter_hu9d85b0e49352bb2151ecca39f7400210_74937_660x0_resize_box_3.png)

Azul y amarillo — un color predomina más. Fuente: Martin Krzywinski.

Observamos que el amarillo predomina. Eso significa que, ante la presencia de otros colores, tendemos a darle mayor importancia a las marcas que tienen ese color, como vemos en el siguiente ejemplo, que contiene un gráfico publicado en un paper, y una modificación que busca utilizar colores sin predominancia:

![Propuesta de colores sin predominancia, modificación de un gráfico publicado en un artículo científico. Fuente: Martin Krzywinski.](../../../courses/infovis/09_colores/images/bar_colors_comparison_hu2e1b1969a8411ab183a0e24c8efb622b_870327_660x0_resize_box_3.png)

Propuesta de colores sin predominancia, modificación de un gráfico publicado en un artículo científico. Fuente: Martin Krzywinski.

Afortunadamente existen buenas paletas de colores para estas situaciones, así como herramientas que nos facilitan elegirlas y configurarlas. El sitio [Color Brewer](http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) nos permite explorar paletas de colores para múltiples escenarios, con características óptimas de predominancia y respetando los principios de efectividad y coherencia, más previsualización para saber como luce cada paleta:

![Imagen del sitio Color Brewer.](../../../courses/infovis/09_colores/images/color_brewer_hu7e15c755513ff1aebcd82b491a1be774_951695_660x0_resize_box_3.png)

Imagen del sitio Color Brewer.

Esta herramienta permite construir paletas que también sean compatibles con impresión y ceguera de colores. Este último tema lo veremos más adelante en esta unidad.

## Usando la Transparencia: Value-by-Alpha 

La transparencia es útil para crear capas de elementos y efectos visuales, pero interfiere con la luminosidad y la saturación, así que debe ser usada con cuidado. Una técnica que hace buen uso de ella es `value_by_alpha_map`, una extensión del `choropleth_map` que añade el canal de transparencia a cada área. En este ejemplo, la transparencia codifica la [certidumbre que se tiene sobre la mortalidad del cáncer de cérvix en los Estados Unidos](http://andywoodruff.com/blog/value-by-alpha-maps/):

![Mapa de Coropletas tipo value-by-alpha. Fuente: Andy Woordruff.](../../../courses/infovis/09_colores/images/value_by_alpha_hu00f956f469f6e0116421c52247acd999_437650_660x0_resize_box_3.png)

Mapa de Coropletas tipo value-by-alpha. Fuente: Andy Woordruff.

¿Les parece un mapa fácil de interpretar? En ocasiones puede ser más eficiente tener un color para representar áreas con datos que no son confiables. Eso permitiría poner la atención en las áreas donde los datos sí permiten el análisis.

## Arcoiris 🌈 es una Mala Opción 

La paleta de colores de arcoiris 🌈 tiene múltiples nombres, dependiendo de la plataforma en la que se utilice. Los más comunes son `rainbow` y `jet`. Esta paleta es utilizada frecuentemente para todo tipo de tareas. No se puede negar que evoca familiaridad, sin embargo, presenta muchos problemas de percepción. Veamos el siguiente ejemplo, cortesía de [Google AI](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html):

![Izquierda: mapa de profundidad con una paleta secuencial monocromática. Derecha: mapa de profundidad con paleta conocida como jet o rainbow. Fuente: Google AI](../../../courses/infovis/09_colores/images/google_jet.png)

Izquierda: mapa de profundidad con una paleta secuencial monocromática. Derecha: mapa de profundidad con paleta conocida como jet o rainbow. Fuente: Google AI.

Observamos que los colores no tienen orden en ninguno de los canales (tono o matiz, luminosidad, saturación) y que los cambios de un tono a otro no son lineales. Este mapa de colores puede mostrar una estructura fina en los datos, pero también introduce artefactos que pueden interpretarse como estructurales, cuando solamente son una característica de la paleta elegida. Puede servir para datos categóricos, pero hay mejores, puesto que utiliza colores que tienen predominancia. El siguiente `choropleth_map` ilustra como su uso categórico también puede introducir artefactos estructurales:

![Mapa de coropletas utilizando una escala de colores de arcoiris. Fuente: EagerEyes.](../../../courses/infovis/09_colores/images/rainbow_choropleth_hu4208984f5f1a4726ea503a84e7f26a37_1523547_660x0_resize_box_3.png)

Mapa de coropletas utilizando una escala de colores de arcoiris. Fuente: EagerEyes.

Pareciera que el país se divide en dos, sin embargo, los cambios bruscos de tonalidad no representan lo que realmente sucede: como vemos en la leyenda, hay una transición suave entre los valores de cada categoría.

## ¿Ceguera a los Colores? 

Hasta ahora hemos discutido aspectos técnicos del uso de color. Sin embargo, también hay un aspecto humano que no podemos ignorar: la ceguera a los colores ([_color blindness_](https://en.wikipedia.org/wiki/Color_blindness) en inglés). Esta condición, en la que una persona no percibe todos los colores, es más frecuente y compleja de lo que se puede creer. En términos de frecuencia, el [8% de los hombres y el 0.4% de las mujeres no ve todos los colores que pueden percibir las personas](https://en.wikipedia.org/wiki/Color_blindness#Epidemiology). En términos de complejidad, usualmente se confunde daltonismo con la ceguera a los colores, pero existen más condiciones dentro de esta categoría. Una persona con ceguera a los colores [ve de la siguiente manera](http://mkweb.bcgsc.ca/colorblind/):

![Ejemplos de como distintos tipos de ceguera a los colores afectan la percepción. Fuente: Martin Krzywinski.](../../../courses/infovis/09_colores/images/colorblindness.palettes.v11_9_hu4b9499cab3dd2469224071849d6dcdc4_2044360_660x0_resize_box_3.png)

Ejemplos de como distintos tipos de ceguera a los colores afectan la percepción. Fuente: Martin Krzywinski.

A continuación vemos una animación de algunas de las paletas de colores disponibles en `matplotlib`:

![Animación de mapas de colores en <code>matplotlib</code> de acuerdo a como los ve una persona: sin ceguera a los colores; con ceguera del color verde (deuteranopia); ceguera del color rojo (protanopia); ceguera del color azul (tritanopia); y en blanco y negro.](../../../courses/infovis/09_colores/images/blindness_hu0864d344d79069fedf1b5960754487fb_896042_660x0_resize_box.gif)

Animación de mapas de colores en `matplotlib` de acuerdo a como los ve una persona: sin ceguera a los colores; con ceguera del color verde (deuteranopia); ceguera del color rojo (protanopia); ceguera del color azul (tritanopia); y en blanco y negro.

Si tienes que presentar una visualización a una audiencia es probable que hayan personas con algún grado de ceguera a los colores. Una visualización que utiliza paletas aptas para todes amplía la accesibilidad de tu trabajo y no perjudica la aplicación de los principios de efectividad y coherencia.

## Ilusiones

Incluso si ves todos los colores, puede que las cosas no sean como crees que son. En la siguiente imagen, ¿cuál es el color de las frutillas?

![¿Cuál es el color de las frutillas? Fuente: @AkiyoshiKitaoka.](../../../courses/infovis/09_colores/images/frutillas_hu978ecf8f8db4de694bf4236f5ce8e890_44742_660x0_resize_q75_box.jpg)

¿Cuál es el color de las frutillas? Fuente: @AkiyoshiKitaoka.

Vemos que las frutillas son de un color rojizo. Sin embargo, si utilizamos un programa para ver cuál es el color exacto, veremos que en realidad son grises:

![Las frutillas eran grises (en la imagen). Fuente: @AkiyoshiKitaoka.](../../../courses/infovis/09_colores/images/frutillas_reveal.png)

Las frutillas eran grises (en la imagen). Fuente: @AkiyoshiKitaoka.

¿Cuánto de lo que vemos está influenciado por lo que esperamos ver? Es una pregunta que debemos hacernos a la hora de diseñar una visualización. Hay que tener cuidado con los contextos y con la manera de percibir de nuestra mente. Los contextos son importantes puesto que determinan lo que observamos. La siguiente imagen nos muestra un tablero de ajedrez, en el que nos preguntamos si los colores `A` y `B` son iguales:

![¿Son A y B iguales?. Fuente: Edward H. Adelson.](../../../courses/infovis/09_colores/images/checkerboard_hu81d1bff37900d01b5cd1e8e19e35d1f3_189581_660x0_resize_box_3.png)

¿Son A y B iguales?. Fuente: Edward H. Adelson.

Aunque vemos que la celda `A` es más oscura que `B`, basta trazar una línea gruesa entre ambas celdas para darnos cuenta de nuestro error de percepción:

![A y B son iguales. Fuente: Edward H. Adelson.](../../../courses/infovis/09_colores/images/checkerboard_reveal_huc1762c2ade3e25b388bce7a8c4496aa5_180017_660x0_resize_box_3.png)

A y B son iguales. Fuente: Edward H. Adelson.

Esto se debe a que percibimos en términos relativos al contexto de la imagen.

Para ejemplificar este fenómeno en un escenario cotidiano, hace algunos años se hizo viral el meme del vestido que preguntaba si un vestido en una foto era azul y negro o blanco y amarillo. La gente no parecía ponerse de acuerdo porque cada persona veía el vestido de una manera, pero ambas respuestas eran correctas. A continuación un ejemplo de ese fenómeno:

![¿El vestido es azul y negro o blanco y amarillo? La respuesta: ambas. Fuente: anónima.](../../../courses/infovis/09_colores/images/dress.gif)

¿El vestido es azul y negro o blanco y amarillo? La respuesta: ambas. Fuente: anónima.

El contexto que rodea al vestido, la disposición de receptores en nuestros ojos, las condiciones de iluminación, es decir, **todo el contexto** que rodea a la imagen es el que incide en como lo percibimos.

## Conclusiones 

En esta unidad vimos como los colores pueden ser un medio de expresión que incluye los atributos de nuestros datos, pero que puede incluir otros aspectos relacionados con el mensaje que queremos comunicar. Aprendimos que los colores se pueden posicionar formalmente en un espacio de colores y que se pueden construir paletas o conjuntos de colores en base a estos espacios. No todas las paletas son igual de eficientes y coherentes para lo que visualicemos, pero hay estrategias y herramientas que nos ayudarán a elegir y probar. Ahora bien, el contexto técnico es importante, pero nunca debemos olvidar que nuestra visualización será utilizada por otras personas. Así, si no tenemos en cuenta cómo los demás perciben lo que estamos visualizando, podemos inducir errores en la interpretación de los resultados. Al ser un curso introductorio no profundizamos en cómo percibimos información, pero el siguiente paso en un curso más avanzado sería entender la [percepción visual](https://www.csc2.ncsu.edu/faculty/healey/PP/). Asimismo, existen factores culturales que inciden en la interpretación y percepción del color que tampoco revisamos. Sin embargo, estamos en posición de concluir que quien diseña visualizaciones debe tener en cuenta que las personas pueden ver algo distinto de lo que esperamos que vean, sea por motivos biológicos como la ceguera a los colores o contextuales propios o externos a la visualización.