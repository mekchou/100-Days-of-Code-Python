import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "mekchou"
TOKEN = "asjghuh34789sadf895"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes", 
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Sex Graph",
    "unit": "Time",
    "type": "int",
    "color": "shibafu",
    
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

body1 = {
    "date": "20240502",
    "quantity": "1",
    "optionalData": "{\"eject\":\"0\"}"
}

graph1_endpoint = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
response = requests.post(url=graph1_endpoint, json = body1, headers=headers)