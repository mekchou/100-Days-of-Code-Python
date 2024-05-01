import requests

API_URL = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = "387972c91279254a95ac4d8cbcd7108c"
MY_LAT = 43.653225
MY_LONG = -79.383186


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()
data = response.json()

weather_id_list = [data["list"][n]["weather"][0]["id"] for n in range(4)]
print(weather_id_list)

if any(item < 700 for item in weather_id_list):
    print("Bring Umbrella")
else:
    print("All good")