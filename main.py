# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import json
import datetime as dt
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# data2 = {
#     "city": "UMIT",
#     "code": "ATH",
#     "priceExpected": 60,
#     "id": 11
# }
#
# with open(file="flight.json", mode="r") as file:
#     data_read = json.load(file)
#     updated_data = data_read.append(data2)
#     print(data_read)
#
# with open(file="flight.txt", mode="w") as file:
#     data2 = file.write(data_read)


with open(file="flight.json", mode="r") as file:
    city_list = [(item["code"], item["priceExpected"]) for item in json.load(file)]

print(city_list)
data_flight_search = FlightSearch(city_list)
data = data_flight_search.searched_data

# pprint(data)

flight_data = FlightData(data)
final_data = flight_data.structured_data
pprint(final_data)
notification = NotificationManager(final_data)
#
