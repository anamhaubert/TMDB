# feito em aula

import requests
import os
import dotenv
from pycine.models import Movie
from pycine.models import MovieResults
dotenv.load_dotenv(".env")
token = os.environ["API_TOKEN"]
from fastapi import FastAPI

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()

app=FastAPI()

def get_movie(id:int):

    

    url=f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    data=get_json(url)
    movie= Movie.model_validate(data)
    return movie

#########################################

def fetch_movies():

    url=f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "include_adult": False,
        "include_video": False,
        "language": "en_US",
        "page": 1,
        "sort_by":"popularity.desc"
    }
    data=get_json(url, params)
    movies= MovieResults.model_validate(data)
    return movies

##########################################
def top_movies():
    
    url=f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "include_adult": False,
        "include_video": False,
        "language": "en_US",
        "page": 1,
        "sort_by":"vote_average.desc"
    }
    data=get_json(url, params)
    movies= MovieResults.model_validate(data)
    return movies
##########################################
    
# @app.get("/movies")
# def get_movies():
#     """faz requests para a API TMDB e obtem lista de filmes"""

#     #menos populares
#     # url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.asc"
    
#     #mais votados
#     url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_count.desc&primary_release_year=2010"

#     headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer {token}"
#     }
#     data = requests.get(url,headers=headers)
#     data= data.json()

#     results = data['results']

#     # movie = results[0]

#     titles=[]
#     for m in results:
#         titles.append(
#             m['title'] + " " + m['release_date']
#                       )
#     return titles

@app.get("/actors/{nome}")
def get_actors(nome: str):

    url = f"https://api.themoviedb.org/3/search/person?query={nome}"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzhhMzRlMTEzODI4NjdjMDQyNWI3ZmNkNmMzYjk2MSIsIm5iZiI6MTcyOTg5ODE3Mi42NTY0OCwic3ViIjoiNjcxYzE5MjI1YmU5ZTg3NTlkYTc0ODgwIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.BvIWEHaXcSARLK_nSMRF0Jg4O6jupa4KcqMiaKAv4UI"
    }

    data = requests.get(url,headers=headers)
    data= data.json()

    results = data['results']

    return results

@app.get("/movie/{title}")
def get_titles(title : str):
    url = f"https://api.themoviedb.org/3/search/movie?query={title}"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzhhMzRlMTEzODI4NjdjMDQyNWI3ZmNkNmMzYjk2MSIsIm5iZiI6MTcyOTg5ODE3Mi42NTY0OCwic3ViIjoiNjcxYzE5MjI1YmU5ZTg3NTlkYTc0ODgwIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.BvIWEHaXcSARLK_nSMRF0Jg4O6jupa4KcqMiaKAv4UI"
    }

    data = requests.get(url,headers=headers)
    data= data.json()

    results = data['results']

    return results

@app.get("/genre")
def get_genre():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzhhMzRlMTEzODI4NjdjMDQyNWI3ZmNkNmMzYjk2MSIsIm5iZiI6MTcyOTg5ODE3Mi42NTY0OCwic3ViIjoiNjcxYzE5MjI1YmU5ZTg3NTlkYTc0ODgwIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.BvIWEHaXcSARLK_nSMRF0Jg4O6jupa4KcqMiaKAv4UI"
    }
    data = requests.get(url,headers=headers)
    data= data.json()

    genres = data.get('genres', [])

    return genres

#pegar um filme e trazer todos os atores
@app.get("/casting/{movie}")
def get_casting(movie: str):
    url = f"https://api.themoviedb.org/3/search/movie?query=${movie}"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzhhMzRlMTEzODI4NjdjMDQyNWI3ZmNkNmMzYjk2MSIsIm5iZiI6MTcyOTg5ODE3Mi42NTY0OCwic3ViIjoiNjcxYzE5MjI1YmU5ZTg3NTlkYTc0ODgwIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.BvIWEHaXcSARLK_nSMRF0Jg4O6jupa4KcqMiaKAv4UI"
    }
    
    data = requests.get(url,headers=headers)
    data= data.json()
    id = data['results'][0]['id']
    url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"

    datacast = requests.get(url,headers=headers)
    datacast = datacast.json(),
    result = datacast['cast']
    return result