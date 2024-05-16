import requests
import bearer
from flight_data import FlightData

AMADEUS_API_KEY = "HsjAFDneqLqrgeocM2No3jKjLIFI0bal"
AMADEUS_API_SECRET = "W70gnyCsd9XwnbwD"
AMADEUS_API_URL = "https://test.api.amadeus.com"
AMADEUS_CITY_SEARCH = "/v1/reference-data/locations/cities"
AMADEUS_FLIGHT_OFFERS = "/v2/shopping/flight-offers"
AMADEUS_FLIGHT_DATES = "/v1/shopping/flight-dates"
AMADEUS_TOKEN_ENDPOINT = "/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self) -> None:
        self.city = None
        self.access_token = self.get_access_token()
        
        
    # def search_iata(self):
    #     return "testing"

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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        body = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time,
            "returnDate": to_time,
            "nonStop": "true",
            "travelClass": "ECONOMY",
            "adults": 1,
            "currencyCode": "USD",
            "max": 10,
        }
        response = requests.get(url=f"{AMADEUS_API_URL}{AMADEUS_FLIGHT_OFFERS}", auth=bearer.BearerAuth(self.access_token), params= body)
        try:
        # response.raise_for_status()
            data = response.json()
            price = data["data"][0]["price"]["grandTotal"]
        except:
            print("no flight found")
            price = 9999
        # print(data)
        # departure_iata0 = data["data"][1]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        # price = data["data"][1]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        flight_data = FlightData(
            price = price,
            origin_city = origin_city_code,
            origin_airport = origin_city_code,
            destination_city = destination_city_code,
            destination_airport = destination_city_code,
            departure_date = from_time,
            return_date = to_time,
        )
        
        
        
        return flight_data
        # price_1= data["data"][6]["price"]["grandTotal"]
        # print(price_0)
        # print(price_1)