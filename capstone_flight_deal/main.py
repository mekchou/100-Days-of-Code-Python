#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()
# print(flight_search.search_iata())
flight_deals_data = data_manager.retrieve_rows()["prices"]

for row in range(len(flight_deals_data)):
    # print(rows)
    # print(flight_deals_data[row])
    city = flight_deals_data[row]["city"]
    city_data = flight_search.search_city(city)
    iata = city_data["data"][0]["iataCode"]
    flight_deals_data[row]["iataCode"] = iata
    data_manager.update_data(data=flight_deals_data[row])
    
    # print(rows)
pprint(flight_deals_data)