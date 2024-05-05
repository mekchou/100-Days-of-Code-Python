import requests


class DataManager:
    def __init__(self) -> None:
        self.sheet_url = "https://api.sheety.co/f57eb1dd3b398c09d11ae905bda32e17/flightDeals/prices"
        
    def retrieve_rows(self):
        response = requests.get(url = self.sheet_url)
        response.raise_for_status()
        data = response.json()
        return data