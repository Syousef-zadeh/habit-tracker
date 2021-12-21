import requests
from datetime import datetime

TOKEN = "zxfzfzx56zxf656fz6f54fz"
USERNAME = "sheida"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


# create new username(account) on the pixela website
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}
# CREATE THE GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=12, day=20)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "19.74",
}
# CREATE A NEW ACTIVITY IN A SPECIFIC DATE IN THE GRAPH
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "5.5"
}
# UPDATE THE GRAPH
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(response.text)

