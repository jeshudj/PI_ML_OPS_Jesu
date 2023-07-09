<p align=center><img src="src\001logohenry.png"><p>

# <h1 align=center> **APLICACIÓN PARA CONSULTAR Y RECIBIR RECOMENDACIONES DE PELÍCULAS** </h1>
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <h1 align=center> **Jesus Marceliano Neira** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
  <img src="src\002MLOpslogo.png" alt="Diagrama de Flujo">
</p>



## ¡Bienvenido a mi aplicación para consultas y recomendacion de películas! Aquí, podrás explorar y descubrir películas de acuerdo a tus gustos. La aplicacion de recomendación utilizará técnicas de ***Machine Learning*** para brindarte sugerencias, basadas en un historial de películas vistas. 

<hr>  

## **Descripción del proyecto**

## Contexto

Como Data Scientist Nuestro objetivo es desarrollar una aplicación de recomendación de películas que permita a los usuarios descubrir nuevos contenidos relevantes y disfrutar de una experiencia de busqueda personalizada.



<p align="center">
  <img src="src\003transformer.png" alt="Diagrama de tranformacion">
</p> 


## Transformaciones

En el archivo ETL.ipynb que se proporciona hay una serie de pasos que se realizó para extraer, transformar y cargar datos en un DataFrame llamado 'movies'. Aquí está la propuesta de trabajo planteada.


## **Propuesta de trabajo planteada**

**`Transformaciones`**:  Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, ***y solo estas***, transformaciones a los datos:


+ Algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder  y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

+ Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
  
+ Los valores nulos del campo **`release date`** deben eliminarse.

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.

+ Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.

+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`poster_path`** y **`homepage`**.


## Análisis exploratorio de los datos EDA

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Las nubes de palabras dan una buena idea de cuáles palabras son más frecuentes en los títulos, se deja capturas obtenidas del DataFrame


<p align="center">
  <img src="src\004Nubepalabras.png" >
</p>

<p align="center">
  <img src="src\005Histogram.png" >
</p>



## API en desarrollo: 6 funciones API con FastAPI

Se Propone disponibilizar los datos usando el framework ***FastAPI***. Las consultas que se propones son las siguientes:

Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).
  
+ def **peliculas_idioma( *`Idioma`: str* )**:
    Se ingresa un idioma. Debe devolver la cantidad de películas producidas en ese idioma.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` cantidad de películas fueron estrenadas en `idioma`*
         

+ def **peliculas_duracion( *`Pelicula`: str* )**:
    Se ingresa una pelicula. Debe devolver la la duracion y el año.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` . Duración: `x`. Año: `xx`*

+ def **franquicia( *`Franquicia`: str* )**:
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La franquicia `X` posee `X` peliculas, una ganancia total de `x` y una ganancia promedio de `xx`*

+ def **peliculas_pais( *`Pais`: str* )**:
    Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *Se produjeron `X` películas en el país `X`*

+ def **productoras_exitosas( *`Productora`: str* )**:
    Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La productora `X` ha tenido un revenue de `x`*

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.






**Este repositorio incluye:**

+ Cuadernos de Jupyter para su visualización<br/>
+ Un proceso ETL paso a paso<br/>
+ Un análisis exploratorio de datos (EDA)<br/>
+ Desarrollo de una API<br/>
+ Implementación<br/>



## Detalles adicionales del proyecto

Aquí encontrarás información adicional y recursos relacionados con nuestro proyecto:

1. `Video explicativo:` Se ha creado un [video explicativo](https://www.youtube.com/watch?v=V7I7m5FmO_A&t=38s)  donde te muestro algunas funciones de mi proyecto con el uso de la API.

2. `Acceso a la API:` En el Siguiente [enlace de la API](https://pi-ml-ops-jesus.onrender.com/docs) podras encontrar las funciones de este proyecto.

3. `Obtención de datos originales:` Si te interesa en obtener acceso a los datos originales utilizados en este proyecto de análisis, puedes ir al siguiente [enlace de descarga](https://drive.google.com/drive/folders/1nvSjC2JWUH48o3pb8xlKofi8SNHuNWeu) para que puedas explorar y analizar los datos por tu cuenta.

4. `Acceso rápido:`
- Visualize ETL [ETL.ipynb](ETL_Jesu.ipynb) notebook.
- Visualize EDA [EDA.ipynb](EDA_Jesu.ipynb) notebook.
- Visualize API  [`MAIN.PY`](main.py)

<br/>

