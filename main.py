import requests

TOKEN = "zxfzfzx56zxf656fz6f54fz"
USERNAME = "sheida"

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
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)