from typing import Optional
from typing import List
from pydantic import BaseModel
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
PyObjectId = Annotated[str, BeforeValidator(str)]
from pydantic import ConfigDict, BaseModel, Field
from bson import ObjectId

# models feitos em aula

class Movie(BaseModel):
    # id: int
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    genres: Optional[list] = None
    original_language: str
    overview: str
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    release_date: str
    vote_count: Optional[int] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class MovieCollection(BaseModel):
    movies: list[Movie]

class MovieResults(BaseModel):
    results: list[Movie]
    page: int
    total_pages: int
    total_results: int

#################################
# models trabalho

class Person(BaseModel):
    id: int
    name: str
    popularity: Optional[float] = None
    known_for_department: Optional[str] = None
    profile_path: Optional[str] = None

class PersonList(BaseModel):
    results: List[Person]
    page: int
    total_pages: int
    total_results: int

class MovieList(BaseModel):
    results: List[Movie]
    page: int
    total_pages: int
    total_results: int