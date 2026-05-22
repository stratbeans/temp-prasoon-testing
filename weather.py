# write a code to fetch temperature of New York City from openweathermap api

import requests
import os
from dotenv import load_dotenv

load_dotenv()

# create a function to fetch temperature of a city
def fetch_temperature(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    response = requests.get(url)
    data = response.json()
    return data['main']['temp']