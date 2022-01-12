#Python
from typing import Optional, List, Dict
from fastapi.param_functions import Query

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query



app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    e_mail: str
    hair_color: Optional[str]  = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"hello":"world"}

    # Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
    	
 #Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: str = Query(...)
): 
    return {name: age}
#con los 3 puntos lo estamos haciendo obligatorio, 
# lo ideal es que un Query no sea obligatorio, sin embargo,
# es posible, que por alguna razon, nos haga falta hacer 
# esto en algun momento. Lo ideal es que si es obligatorio, 
# no sea un Query Parameter, sino un Path Parameter

