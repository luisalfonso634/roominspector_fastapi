#Python
from typing import Optional, List, Dict

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body



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
    	