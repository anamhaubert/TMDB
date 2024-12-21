from fastapi import FastAPI

from pycine import tmdb
from pycine import entrega
from fastapi.middleware.cors import CORSMiddleware

import pymongo
import os
import dotenv
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
import motor.motor_asyncio
from pymongo import ReturnDocument

dotenv.load_dotenv(".env")
db_url = os.environ["MONGODB_URL"]

app = FastAPI()

origins = [
"http://localhost",
"http://localhost:*",
"http://localhost:5173",
]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# feito em aula

@app.get("/")
def hello():
    return{"status":"pycine is running"}

# @app.get("/movie/{id}")
# def get_movie(id:int):
#     return tmdb.get_movie(id)

# @app.get("/movies")
# def fetch_movies():
#     return tmdb.fetch_movies()

#########################
# atividade

@app.get("/person/{id}") #OK
def get_person(id: int):
    return entrega.get_person(id)

@app.get("/person/search/{name}") #OK
def search_person(name: str):
    return entrega.search_person(name)

@app.get("/popular/person") #OK
def get_popular_person():
    return entrega.get_popular_person()

@app.get("/person/movies/{id}") #OK
def get_person_movies(id: int):
    return entrega.get_person_movies(id)

@app.get("/trending/person/{time_window}") #OK
def get_trending_person(time_window: str):
    if time_window not in ["day", "week"]:
        return {"erro": "o parâmetro deve ser 'day' ou 'week'"}
    return entrega.get_trending_person(time_window)

############################
#22/11/2024

# results = tmdb.search_movies(params)
# return results

@app.get("/movies/top")
def search_movies():
    results = tmdb.fetch_movies()
    return results

############
#       MONGO       #

client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
db = client.pycinedb
movies_collection = db.get_collection("movies")
# representa id gerado no atlas
PyObjectId = Annotated[str, BeforeValidator(str)]

from pycine import models
@app.get(
   "/find/",
    response_description="List all movies",
    response_model=models.MovieCollection,
    response_model_by_alias=False,
)
async def list_movies():
    return models.MovieCollection(movies=await movies_collection.find().to_list(20))
