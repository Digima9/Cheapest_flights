class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.data = data
        self.structured_data = []
        self.structured_data_fun()

    def structured_data_fun(self):
        self.structured_data = []
        for item in self.data:
            if len(item) != 0:
                city_from = item[0]["cityFrom"]
                city_to = item[0]["cityTo"]
                price = item[0]["price"]
                departure = item[0]['local_departure']
                arrival = item[0]['local_arrival']
                airlines = item[0]['airlines']
                flight_no = item[0]["route"][0]["flight_no"]
                stopover = item[0]["pnr_count"]
                if stopover == 1:
                    city_price = {
                        "city_from": city_from,
                        "city to": city_to,
                        "price(eur) ": price,
                        "departure time": departure,
                        "arrival time": arrival,
                        "airlines": [airlines, flight_no],
                        "stopover": "Direct flight"
                    }
                else:
                    city_price = {
                        "city_from": city_from,
                        "city to": city_to,
                        "price(eur) ": price,
                        "departure time": departure,
                        "arrival time": arrival,
                        "airlines": [airlines, flight_no],
                        "stopover": f"Flight has 1 stop"    # through {item[0]["route"][0]["cityTo"]}
                    }
                self.structured_data.append(city_price)





