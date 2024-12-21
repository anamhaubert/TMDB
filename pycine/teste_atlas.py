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

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(db_url,server_api=ServerApi('1'))

client.admin.command('ping')
print(client.list_database_names())
print('pong')

movie = {
    'id': 218,
    'title': 'Terminator',
    'genres': ['Action', 'Sci-fi'],
    'original_language': 'ingles',
    'overview': 'info do filme',
    'release_date': '1991-10-10'
}
# define a base de dados
db = client.get_database('pycinedb')

#obtem a collection (tabela) movies
movies_collection = db.get_collection('movies')

#crud

#read
from pprint import pprint
pprint(movies_collection.find_one({'id':218}))

#drop
movies_collection.delete_many({'id':218})

#insert
movies_collection.insert_one(movie)