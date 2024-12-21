import requests
import os
import dotenv
from pycine.models import Person, PersonList, MovieList
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

# 1. encontra person por id
def get_person(id):
    url = f"https://api.themoviedb.org/3/person/{id}"
    data = get_json(url)
    person = Person.model_validate(data) 
    return person

# 2. encontra person por nome
def search_person(name: str):
    url = "https://api.themoviedb.org/3/search/person"
    params = {"query": name}
    data = get_json(url, params)
    person = PersonList.model_validate(data) 
    return person

# 3. person popular (trending)
def get_popular_person():
    url = "https://api.themoviedb.org/3/person/popular"
    data = get_json(url)
    person = PersonList.model_validate(data) 
    return person

# 4. todos os filmes de um artista
def get_person_movies(id: int):
    url = f"https://api.themoviedb.org/3/person/{id}/movie_credits"
    data = get_json(url)
    movie = {
        'results': data.get("cast"),
        'page': 1,
        'total_pages': 1,
        'total_results': len(data.get("cast"))
    }
    return MovieList.model_validate(movie)

# 5. artista trending da semana
def get_trending_person(time_window: str):
    url = f"https://api.themoviedb.org/3/trending/person/{time_window}"
    data = get_json(url)
    person = PersonList.model_validate(data) 
    return person