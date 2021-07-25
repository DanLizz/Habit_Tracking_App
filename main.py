import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "xxxxxxxx"
TOKEN = "xxxxxxxxxxxxx"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configs = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "steps",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_configs, headers=headers)
# print(response.text)

today = datetime.now()

pixel_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7"
}
graph_id = "graph1"

response = requests.post(url=f"{graph_endpoint}/{graph_id}", json= pixel_value, headers=headers)
print(response.text)

