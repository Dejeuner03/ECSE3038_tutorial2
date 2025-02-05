from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    occupation: str
    address: str
    

app = FastAPI()

list_of_persons = [
        {
    "name": "John Doe",
    "occupation": "Software Engineer",
    "address": "123 Main St"
    },
    {
    "name": "Jane Smith",
    "occupation": "Data Scientist",
    "address": "456 Elm St"
    },
    {
    "name": "Michael Johnson",
    "occupation": "Web Developer",
    "address": "789 Oak St"
    },
    {
    "name": "Emily Brown",
    "occupation": "UX Designer",
    "address": "101 Maple Ave"
    },
    {
    "name": "David Lee",
    "occupation": "Product Manager",
    "address": "202 Pine St"
    },
    {        
    "name": "Sarah Taylor",
    "occupation": "Marketing Specialist",
    "address": "303 Cedar St"
    },
    {
    "name": "Chris Evans",
    "occupation": "Graphic Designer",
    "address": "404 Walnut St"
    },
    {
    "name": "Jessica White",
    "occupation": "Financial Analyst",
    "address": "505 Birch St"
    },
    {
    "name": "Matthew Miller",
    "occupation": "Systems Administrator",
    "address": "606 Spruce St"
    },
    {
    "name": "Amanda Martinez",
    "occupation": "HR Coordinator",
    "address": "707 Chestnut St"
    }
]

@app.get("/person")
async def get_all_person():
    return list_of_persons

@app.get("/name")
async def get_names_of_persons():
    list_of_names =[]
    count = 0 
    for x in list_of_persons:
        list_of_names.append(list_of_persons[count]["name"])
        count = count + 1
        return {"name: list_of_names"}
    
    
@app.get("/address")
async def get_address_of_persons():
    list_of_address =[]
    count = 0 
    for x in list_of_persons:
        list_of_address.append(list_of_persons[count]["address"])
        count = count + 1
        return {"name: list_of_address"}
    
    
@app.get("/occupation")
async def get_occupation_of_persons():
    list_of_occupation=[]
    count = 0 
    for x in list_of_persons:
        list_of_occupation.append(list_of_persons[count]["occupation"])
        count = count + 1
        
        return {"name: list_of_occupation"}
    