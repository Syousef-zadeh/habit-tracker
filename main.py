import requests

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

pixel_data = {
    "date": "20211221",
    "quantity": "9.74",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response.text)