### IMPORTAMOS LIBRERIAS

import pandas as pd
import numpy  as np
from fastapi import FastAPI
import uvicorn
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.neighbors               import NearestNeighbors

app = FastAPI()

# Creaoms una consulta como presentacion con nuestro nombre
@app.get('/')
def presentacion():
    return 'Jesus Marceliano'

# IMPORTAMOS LOS DATOS
data = pd.read_csv("data/clean_movies.csv", sep=';', encoding='utf-8')


# CONSULTA 1:
# Ingresas el idioma, retornando la cantidad de peliculas producidas en el mismo
@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma(idioma:str):
    idioma_filtro = data[data['language'] == idioma]
    cantida_pelis =  idioma_filtro['language'].shape[0]
    return {'Idioma:':idioma, 'cantidad de peliculas:':cantida_pelis}

# CONSULTA 2:
# Ingresas la pelicula, retornando la duracion y el año
@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion(pelicula:str):
    peli_filtro = data[data['title'] == pelicula]
    duracion =  peli_filtro['runtime']
    año = peli_filtro['release_year']
    return {'Pelicula:':pelicula, 'duracion en minutos:':duracion, 'año de estreno:':año }


# CONSULTA 3:
# Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
@app.get("/franquicia/{franquicia}")
def franquicia(franquicia:str):
    franquicia_filtro = data[data['collection'] == franquicia]
    cantidad_pelis = data['title'].shape[0]
    ganancia = data['revenue'].sum()
    promedio = data['revenue'].mean()
    return {'franquicia:':franquicia_filtro, 'Cantidad de Peliculas:':cantidad_pelis,'ganancias totales generadas:':ganancia, 'ganancia promedio:':promedio}


# CONSULTA 4:
# Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais:str):
    pais_filtro = data[data['country'] == pais]
    cantidad = pais_filtro['country'].shape[0]
    return{'Pais:':pais, 'cantidad de peliculas creadas:':cantidad}


# CONSULTA 5:
# Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo
@app.get("/productoras_exitosas/{productora}")
def productora_exitosa(productora:str):
    productora_filtro = data[data['company'] == productora]
    cantidad = productora_filtro['revenue'].sum()
    cantidad_peliculas = productora_filtro['company'].shape[0]
    return{'Productora:':productora, 'ganancias totales:':cantidad, 'cantidad de peliculas generadas:':cantidad_peliculas}


# CONSULTA 6:
# e ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
# Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista
@app.get("/get_director/{director}")
def get_director(director:str):
   director_data = data[data['director'].apply(lambda x: director in x if isinstance(x, (list, str)) else False)].head(5)
   ganancias_totales = director_data['revenue'].sum()
   peliculas = []
   for _, row in director_data.iterrows():
        titulo = row['title']
        fecha_estreno = row['release_date']
        retorno = row['return']
        costo = row['budget']
        ganancia = row['revenue']
        peliculas.append({'titulo': titulo, 'fecha_estreno': fecha_estreno, 'retorno':retorno, 'ganancia generada:':ganancia, 'coste de la pelicula:': costo})
    
   return {'nombre del director': director, 'retorno total': ganancias_totales, 'peliculas': peliculas}


@app.get("/recomendacion/{recomendacion}")
def movie_recomendacion(movie_title):
    # Cargar el archivo CSV con los datos
    movie_data = pd.read_csv("data/recomendacion_movies.csv")

    # Buscar la película por título en la columna 'title'
    movie = movie_data[movie_data['title'] == movie_title]

    if len(movie) == 0:
        return "La película no se encuentra en la base de datos."

    # Obtener el género y la popularidad de la película
    movie_genre = movie['genre'].values[0]
    movie_popularity = movie['popularity'].values[0]

    # Crear una matriz de características para el modelo de vecinos más cercanos
    features = movie_data[['popularity']]
    genres = movie_data['genre'].str.get_dummies(sep=' ')
    features = pd.concat([features, genres], axis=1)

    # Manejar valores faltantes (NaN) reemplazándolos por ceros
    features = features.fillna(0)

    # Crear el modelo de vecinos más cercanos
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] * len(genres.columns)], n_neighbors=6)

    # Obtener los títulos de las películas recomendadas
    recomendacion = movie_data.iloc[indices[0][1:]]['title']

    return recomendacion
