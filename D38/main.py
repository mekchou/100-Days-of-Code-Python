import requests
from datetime import datetime
import bearer
import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 168
AGE = 34

NUTRITION_APP_ID = os.environ.get("ENV_NUTRITION_APP_ID")
NUTRITION_API_KEY = os.environ.get("ENV_NUTRITION_API_KEY")
NUTRITION_HOST_DOMAIN = "https://trackapi.nutritionix.com"
NUTIOTION_ENDPOINT = "/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/f57eb1dd3b398c09d11ae905bda32e17/workoutTracking/workouts"
BEARER_TOKEN = os.environ.get("ENV_SHEETY_BEARER_TOKEN")



def get_exercise_stats():
    headers = {
        "x-app-id": NUTRITION_APP_ID,
        "x-app-key": NUTRITION_API_KEY,
    }
    parameters= {
        "query": input("What's your exercise today?\n"),
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }
    response = requests.post(url=f"{NUTRITION_HOST_DOMAIN}{NUTIOTION_ENDPOINT}", headers=headers, json=parameters)
    response.raise_for_status()
    exercises = response.json()["exercises"][0]["user_input"]
    duration_min = response.json()["exercises"][0]["duration_min"]
    calories = response.json()["exercises"][0]["nf_calories"]
    return (exercises, duration_min, calories)
    
# get_exercise_stats(input("What's your exercise today?\n"))

def add_exercise(exercise, duration, calories):
    parameters = {
        "workout":{
            "date": datetime.now().strftime("%Y/%m/%d"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url = SHEETY_URL, json=parameters, auth=bearer.BearerAuth(BEARER_TOKEN))

def main():
    exercise, duration, calories = get_exercise_stats()
    add_exercise(exercise, duration, calories)
    
if __name__ == "__main__":
    main()
    