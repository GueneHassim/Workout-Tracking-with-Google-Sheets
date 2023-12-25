
nutrx_url = "https://www.trackapi.nutritionix.com/v2/natural/exercise?"

import requests
import json
from datetime import datetime
import os

# environment variable
NUTRIXIONIX_ID = os.environ.get("NUTRX_ID")
NUTRIXIONIX_KEY = os.environ.get("NUTRX_KEY")
SHEETY_POST_URL = os.environ.get('SHEETY_URL')
SHEETY_BEAR_AUTH = os.environ.get("SHEETY_AUTH")


GENDER = "male"
WEIGHT_KG = 67
HEIGHT_CM = 176
AGE = 28
# %d day of month 01-31 %m month as a number 01-12 %Y full year version
today_date = datetime.now().strftime("%d/%m/%Y")
#formating the time at the local version
now_time = datetime.now().strftime("%X")



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRIXIONIX_ID,
    "x-app-key": NUTRIXIONIX_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutrixionix_response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = nutrixionix_response.json()
print("")

result_data = result["exercises"]
for exercise in result_data:
    sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
sheety_header = {
    
    #The string 'Bearer ' at the beginning of the authentication code was separated 
    #from the rest of the code with a space. I wanted to go easy, 
    #so I saved the essential part of the code as an environment variable. The first part, 
    #I hardwrote it in the 'Authentication' key value.

    "Authorization": f"Bearer {SHEETY_BEAR_AUTH}"
}
sheet_response = requests.post(url=SHEETY_POST_URL, json=sheet_inputs, headers=sheety_header)

print("DONE")
print(sheet_response.text)

