# boardgame-reviews
Este repositorio contiene la documentación, archivos y scripts utilizados para crear el _dataset_ **Boargame Ranking**.

En la Wiki de este repositorio pueden consultarse las actas de reunión así como instrucciones para configurar anaconda y `python 3.7`. También un breve recopilación de la documentación _online_ conusltada.

El directorio `/doc` contiene una copia del email de confirmación del propietario de la web mishigeek.com en que da su consentimiento para la realización de _web scrapping_. También se encuentra el archivo PNG de la representación gráfica del _dataset_ así como los _markdown_ con los que se han elaborado las respuestas a la PRA1

En el directorio `/py` hemos alojado los scripts y csv utilizados para generar el _dataset_ **Boardgame Ranking**.
* `gen_boardgame_dataset.py`. Genera el dataset a partir de las reseñas, cuyo url identifica `get_reviews_list.py`.
* `get_ratings.py`. Archivo python en que se define la función `get_ratings`, que dada un url de una reseña retorna los campos analizados.
* `get_reviews_list.py`. Script que genera un archivo csv con las urls de las reseñas, así como la categoría de reseña.
* `mishigeek_reviews.csv`. Archivo generado por `get_reviews_list.py` que contiene los urls de las reseñas publicadas en mishigeek.com. Este csv **no es el dataset** obtenido. Dicho dataset no se ha publicado a petición del propietario de los datos.

# Autores
Ignacio Such Ballester (isuch@uoc.edu)

Andrés Fonts Santana (afontss@uoc.edu)

# Dataset License - Simulación
El dataset resultande no puede ser compartido de forma pública a petición del propietario de los datos. Hemos publicado una simulación del dataset original bajo una licencia _CC BY_ en el repositorio Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6447900.svg)](https://doi.org/10.5281/zenodo.6447900)


