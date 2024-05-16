import requests


class DataManager:
    def __init__(self) -> None:
        self.sheet_url = "https://api.sheety.co/f57eb1dd3b398c09d11ae905bda32e17/flightDeals/prices"
        
    def retrieve_rows(self):
        response = requests.get(url = self.sheet_url)
        response.raise_for_status()
        data = response.json()
        return data
    
    def update_data(self, data):
        endpoint = f"{self.sheet_url}/{data["id"]}"
        body = {
            "price": {
                "city": data["city"],
                "iataCode": data["iataCode"],
                "lowestPrice": data["lowestPrice"]
            }
        }
        response = requests.put(url=endpoint, json=body)
        response.raise_for_status()