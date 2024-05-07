from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()



def main():
    flight_deals_data = data_manager.retrieve_rows()["prices"]

    for row in range(len(flight_deals_data)):
        city = flight_deals_data[row]["city"]
        city_data = flight_search.search_city(city)
        iata = city_data["data"][0]["iataCode"]
        flight_deals_data[row]["iataCode"] = iata
        data_manager.update_data(data=flight_deals_data[row])

        flight_data = flight_search.check_flights("YYZ",iata,"2024-05-08","2024-05-20")

        if float(flight_data.price) <= flight_deals_data[row]["lowestPrice"]:
            price = f"Price: {flight_data.price}\n"
            departure_city_name = "Departure City Name: Toronto\n"
            departure_airport_iata_code = "Departure Airport IATA Code: YYZ\n"
            arrival_city_name = f"Arrival City Name: {flight_deals_data[row]['city']}\n"
            arrival_airport_iata_code = f"Arrival Airport IAIA Code: {flight_data.destination_airport}\n"
            outbound_date = f"Outbound Date: {flight_data.departure_date}\n"
            inbound_date = f"Inbound Date: {flight_data.return_date}\n"

            content = price + departure_city_name + departure_airport_iata_code + arrival_city_name + arrival_airport_iata_code + outbound_date + inbound_date

            notification_manager.send_email(content)

        # else:
            # print("No notification")

        # print(f"{iata}: {flight_data.price}")

    # pprint(flight_deals_data)
    # print(flight_search.access_token)

if __name__ == "__main__":
    main()