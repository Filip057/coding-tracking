import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

MY_TOKEN = "infjfjklecKLJ"
USERNAME = "filipek"
ID = "graph1"

user_param = {
    "token": MY_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_param)

header = {"X-USER-TOKEN": MY_TOKEN}

body = {
    "id": ID,
    "name": "coding minutes",
    "unit": "mins",
    "type": "int",
    "color": "ichou"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_response = requests.post(url=graph_endpoint, headers=header, json=body)

todays_date = datetime.now()

add_pixel_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}"

mins_of_coding = input("How many minutes today?")

add_pixel_body = {
    "date": todays_date.strftime("%Y%m%d"),
    "quantity": mins_of_coding,
}

add_response = requests.post(url=add_pixel_url, json=add_pixel_body, headers=header)
