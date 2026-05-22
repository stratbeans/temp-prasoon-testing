# create a fast api application to fetch temperature of a city

from fastapi import FastAPI
from weather import fetch_temperature

app = FastAPI()

@app.get("/temperature/{city}")
def get_temperature(city: str):
    return {"temperature": fetch_temperature(city)}

