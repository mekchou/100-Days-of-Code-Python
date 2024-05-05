import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 168
AGE = 34



NUTRITION_APP_ID = "63a7ba28"
NUTRITION_API_KEY = "5222cdd05b53a0e6c04289ab5d5eea03"
NUTRITION_HOST_DOMAIN = "https://trackapi.nutritionix.com"
NUTIOTION_ENDPOINT = "/v2/natural/exercise"

def get_exercise_stats(prompt):
    headers = {
        "x-app-id": NUTRITION_APP_ID,
        "x-app-key": NUTRITION_API_KEY,
    }
    parameters= {
        "query": prompt,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }
    response = requests.post(url=f"{NUTRITION_HOST_DOMAIN}{NUTIOTION_ENDPOINT}", headers=headers, json=parameters)
    print(response.raise_for_status())
    print(response.json())
    
# get_exercise_stats(input("prompt: "))

# def _add_exercise():