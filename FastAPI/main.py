from fastapi import FastAPI
from models import *

app=FastAPI()

@app.get("/hellopage")
async def hello_page():
    print("received a call from API")
    return "Hey There"

@app.post("/person_details")
async def hello_page(person_obj:Person_class):
    print("received a call from API")
    return person_obj
