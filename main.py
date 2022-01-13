#Python
import email
from typing import Optional
from fastapi.param_functions import Query
from enum import Enum

#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path




app = FastAPI()

# Models
class HairColor(Enum):
    white= "white"
    brown="brown"
    black= "black"
    blonde= "blonde"
    red= "red"
    gray= "gray"

    
class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    email: EmailStr = Field(
        ..., 
        title="Personal E-mail",
        description="This is the personal e-mail"
    )

    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor]  = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


class Location(BaseModel):
    city: str
    state: str
    country: str
    


@app.get("/")
def home():
    return {"hello":"world"}

    # Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
    	
 #Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
    ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the Person Age. It's required"
    )
): 
    return {name: age}
"""
con los 3 puntos lo estamos haciendo obligatorio, 
lo ideal es que un Query no sea obligatorio, sin embargo,
es posible, que por alguna razon, nos haga falta hacer 
esto en algun momento. Lo ideal es que si es obligatorio, 
no sea un Query Parameter, sino un Path Parameter
"""

# Validaciones: Path parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the Person ID"
    )
):
    return{person_id:"It exists"}

#Validaciones : Request Body

@app.put("/person/{person_id}")
def update_person(
        person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...),
   ):
    results = person.dict()
    results.update(location.dict())
    return results
