import requests
from datetime import datetime
import os

APP_ID = os.environ['NUT_APP_ID']
API_KEY = os.environ['NUT_API_KEY']
GENDER = "male"
WEIGHT_KG = "KG as int"
HEIGHT_CM = "Height as int"
AGE = "Age as int"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ['SHEET_ENDPOINT']

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_post_request = {
    "query": input("Which exercise did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(nutritionix_endpoint, json=nutritionix_post_request, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=(os.environ['SHEET_USER'],
                                                                             os.environ['SHEET_PW']))
    print(sheet_response.text)
