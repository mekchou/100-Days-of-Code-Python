import requests
import bearer

AMADEUS_API_KEY = "HsjAFDneqLqrgeocM2No3jKjLIFI0bal"
AMADEUS_API_SECRET = "W70gnyCsd9XwnbwD"
AMADEUS_API_URL = "https://test.api.amadeus.com"
AMADEUS_CITY_SEARCH = "/v1/reference-data/locations/cities"
AMADEUS_TOKEN_ENDPOINT = "/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self) -> None:
        self.city = None
        self.access_token = self.get_access_token()
        
        
    def search_iata(self):
        return "testing"

    def get_access_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_API_SECRET,
        }
        response = requests.post(url=f"{AMADEUS_API_URL}{AMADEUS_TOKEN_ENDPOINT}", headers=headers, data=body)
        token_data = response.json()
        return token_data.get("access_token")

    def search_city(self, keywords):
        body = {
                "keyword": keywords,
                "max": 1
        }
        response = requests.get(url=f"{AMADEUS_API_URL}{AMADEUS_CITY_SEARCH}", auth=bearer.BearerAuth(self.access_token), params= body)
        data = response.json()
        return data