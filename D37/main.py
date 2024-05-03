import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "mekchou"
TOKEN = "asjghuh34789sadf895"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

EVENT_YEAR = 2024
EVENT_MONTH = 4
EVENT_DAY = 27
EVENT_QUANTITY = 1
EVENT_orgasm = 1

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes", 
}
def create_user():
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

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
def create_graph():
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)


# today = datetime(year = EVENT_YEAR, month=EVENT_MONTH, day=EVENT_DAY)
# today_date = today.strftime("%Y%m%d")
# print(today_date)

def add_pixel(year,month,day,quantity,orgasm=0):
    date = datetime(year=year,month=month,day=day).strftime("%Y%m%d")
    body = {
        "date": f"{date}",
        "quantity": f"{quantity}",
        "optionalData": f"{{\"orgasm\": \"{orgasm}\"}}"
    }
    graph1_endpoint = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
    response = requests.post(url=graph1_endpoint, json = body, headers=headers)
    print(response)

def modify_pixel(year,month,day,quantity,orgasm=0):
    date = datetime(year=year,month=month,day=day).strftime("%Y%m%d")
    endpoint = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}"
    body = {
        "date": f"{date}",
        "quantity": f"{quantity}",
        "optionalData": f"{{\"orgasm\": \"{orgasm}\"}}"
    }
    response = requests.post(url=endpoint, json = body, headers=headers)


modify_pixel(2024,4,27,1,2)