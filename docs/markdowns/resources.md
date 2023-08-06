# Recursos

En esta página recopilo enlaces a distintos tipos de datos que pueden utilizar en sus proyectos.

## Datasets relacionados con Chile

*   [Portal de Datos Abiertos del Gobierno de Chile](http://datos.gob.cl/): incluye muchos datasets interesantes como la [Encuesta Origen-Destino de Viajes en Santiago 2012](http://datos.gob.cl/dataset/31682).
*   [Encuestas de Movilidad en varias ciudades de Chile](http://www.sectra.gob.cl/encuestas_movilidad/encuestas_movilidad.htm): Arica, Iquique-Alto Hospicio, Antofagasta, Copiapó, Coquimbo-La Serena, Gran Valparaíso, Gran Santiago, Temuco-Padre de las Casas, Valdivia, Osorno, Puerto Montt. Sin embargo, no están en formatos abiertos :(
*   [Delitos de mayor connotación social en Chile](http://www.seguridadpublica.gov.cl/estadisticas/tasa-de-denuncias-y-detenciones/): estadísticas de delitos agregadas por comunas, desde 2001 hasta 2017.
*   [Estadísticas migratorias en Chile, 2000–2016](http://www.extranjeria.gob.cl/estadisticas-migratorias/)
*   [Datos COVID-19 del Ministerio de Ciencia de Chile](https://github.com/MinCiencia/Datos-COVID19): repositorio con todos los datos recolectados y disponibilizados por el Ministerio de Ciencia. Incluye datos de movilidad, series temporales, y más.
*   [Guaguas](https://github.com/rivaquiroga/guaguas/): “nombres de guaguas (bebés) registrados en Chile entre 1920 y 2019, según el Servicio de Registro Civil e Identificación. Incluye todos los nombres con al menos 15 ocurrencias.”
*   [Cartografía del Censo 2017 de Chile](http://www.censo2017.cl/resultados-precenso-2016/#1483043043443-4db741fa-4733): links a los mapas del Censo 2017 (áreas urbanas, comunas, provincias, distritos, calles, etc.).
*   [Mapas vectoriales de Chile](https://www.bcn.cl/siit/mapas_vectoriales/index_html): archivos en formato _shapefile_ que incluyen redes viales del país, bordes administrativos de regiones, comunas y provincias, entre otras, provistos por la Biblioteca del Congreso Nacional. Estos mapas se pueden cargar con el módulo [GeoPandas](http://geopandas.org/). Están desactualizados.
*   [Microdatos del Censo 2017](https://drive.google.com/drive/u/1/folders/12qIuycAHmXPDwqmtz4PB_ozfj1Wd9Zjn): archivos con los datos individuales del Censo 2017 de Chile. Nota: no es la fuente oficial (para ello deben ir al INE y solicitar un `CD-ROM` con los datos).
*   [OpenStreetMap Data Extracts](http://download.geofabrik.de/): dumps de la información contenida en OpenStreetMap, separadas por continente y país, incluyendo [Chile](http://download.geofabrik.de/south-america/chile.html). Está en formato `pbf` que puede ser leído utilizando [esta versión de `imposm.parser`](https://github.com/mtskelton/imposm-parser). Otra alternativa es usar [`pyrosm`](https://pyrosm.readthedocs.io/en/latest/).
*   [Asesorías de la Cámara de Diputados/as 2018–2022](https://github.com/rivaquiroga/asesorias-externas-camara).

## Datasets en general 

Podrían contener información relevante de/sobre/en Chile.

*   [DBpedia](https://wiki.dbpedia.org/develop/datasets/latest-core-dataset-releases): el contenido de Wikipedia en todos los lenguajes disponibles de la enciclopedia, de manera estructurada.
*   [Recomendaciones de series de Animé](https://www.kaggle.com/CooperUnion/anime-recommendations-database): dataset con las series de animé recomendadas por cada usuario de MyAnimeList.net.
*   [Reproducciones de música en last.fm](http://ocelma.net/MusicRecommendationDataset/index.html): los artistas top para 360 mil usuarios, o todas las canciones escuchadas por 1000 usuarios, de acuerdo a su actividad en last.fm.
*   [Resultados de enfrentamientos en el juego DOTA2](https://www.kaggle.com/devinanzelmo/dota-2-matches)
*   [Datos de Telefonía Móvil de Milán](https://www.kaggle.com/marcodena/mobile-phone-activity)
*   [Medallas y Resultados de los Juegos de Rio 2016](https://www.kaggle.com/rio2016/olympic-games)
*   [Jugadores de FIFA 2017](https://www.kaggle.com/artimous/complete-fifa-2017-player-dataset-global)
*   [La red social de personajes de Marvel Comics](https://www.kaggle.com/csanhueza/the-marvel-universe-social-network)
*   [Datos de redes en la Uni. Koblenz](http://konect.uni-koblenz.de/): conjunto de datasets con redes de distinto tipo, incluyendo redes dirigidas, no dirigidas, bipartitas, con/sin pesos, con signos y con ratings, en áreas como redes sociales, redes de enlaces, redes de autoría, redes físicas, redes de interacción y redes de comunicaciones.
*   [Gender Equity Index](http://www.socialwatch.org/node/14367): mediciones del año 2012 de igualdad de género en el mundo, por país.
*   [The World Bank Data Catalog](http://data.worldbank.org/data-catalog): datos del Banco Mundial que incluyen series temporales de desarrollo, educación, GDP, GINI, etc.
*   [Wikipedia Pageviews](https://dumps.wikimedia.org/other/pageviews/): cantidad de visitas que recibe cada artículo de Wikipedia.
*   [Wikipedia Clickstream](https://dumps.wikimedia.org/other/clickstream/): red de artículos de Wikipedia basada en como las personas hacen clic entre ellos (por ej., si alguien lee el artículo `A` y hace un clic hace el artículo `B`, la red contiene el link `A -> B`).
*   [Foursquare Datasets](https://sites.google.com/site/yangdingqi/home/foursquare-dataset): millones de _check-ins_ de Foursquare entre el año 2012 y 2014.
*   [Pingüinos de Palmer](https://github.com/allisonhorst/palmerpenguins/): repositorio que contiene un dataset con datos de seguimiento (GPS) y características de pingüinos en la antártica.
*   [Características de Canciones de Spotify](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks): propiedades de más de 160 mil canciones.

## Repositorios de Datasets


*   [Kaggle](https://www.kaggle.com/datasets): más de 50 mil datasets, algunos utilizados para competencias. Hay mucho por explorar (algunos de los datasets vinculados arriba están en Kaggle).

## Sitios para buscar inspiración

*   [Kantar Information is Beautiful Awards](https://www.informationisbeautifulawards.com/showcase?page=1&type=awards)
*   [Nightingale](https://medium.com/nightingale) (visítenlo en una ventana anónima del navegador, para poder leer los artículos).
*   [Flowing Data](https://flowingdata.com/)
*   [Observable HQ](https://observablehq.com/explore)
*   [Malofiej](https://www.malofiejgraphics.com/)