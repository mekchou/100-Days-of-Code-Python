import requests
from datetime import datetime

API_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 51.507351
MY_LONG = -0.12

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(data)
print(sunrise)
print(sunset)