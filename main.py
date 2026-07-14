import os
import requests
from datetime import datetime

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")
GRAPHID = os.environ.get("GRAPHID")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPHID,
    "name" : "Studying Graph",
    "unit" : "hours",
    "type" : "float",
    "color" : "ajisai",
    "timezone" : "Asia/Kolkata"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

def habittracker():
    operation = input("Welcome to Habit Tracker!!!"
                      "\nEnter {update} to update a day or {delete} to delete a day"
                      "\nHow many hours did you studied today?: ")
    if operation.lower() == "update":
        pixel_date = input("Add date in format (yyyymmdd) : ")
        quantity = input("Enter the number of hours you studied : ")
        update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{pixel_date}"
        update_params = {
            "quantity": quantity
        }
        response = requests.put(url=update_endpoint,json=update_params,headers=headers)
        print(response.text)
    elif operation.lower() == "delete":
        pixel_date = input("Add date in format (yyyymmdd) : ")
        delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{pixel_date}"
        delete_params = {}
        response = requests.delete(url=delete_endpoint,json=delete_params,headers=headers)
        print(response.text)
    else:
        date = datetime.now()
        pixel_date = date.strftime("%Y%m%d")
        pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
        pixel_params = {
            "date": pixel_date,
            "quantity": operation,
            "optionalData": "{\"Note\":\"This is an OptionalData in Json format!\"}"
        }
        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
        print(response.text)

isrunning = True
while isrunning:
    habittracker()
    run = input("Do you want to do something else? (Y/N)")
    if run.upper() != "Y":
        isrunning = False
        print("\nThank you for using Habit Tracker!!! Goodbye!")
