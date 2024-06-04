from keys import os
import datetime as dt
import os
from dotenv import load_dotenv
import pprint

load_dotenv()
pprint.pprint(dict(os.environ))
kiwi_key = os.environ.get("KIWI_API_KEY")
print(kiwi_key)

data = ""
class FlightSearch:
    import requests

    #   This class is responsible for talking to the Flight Search API.

    def __init__(self, city_list):

        self.city_list = city_list
        self.searched_data = []
        self.search()

    def search(self):
        global data
        self.searched_data = []
        #date = input("enter return date: ")
        for item in self.city_list:
            url = "https://api.tequila.kiwi.com/v2/search"
            params = {
                "fly_from": "OTP",
                "fly_to": f"{item[0]}",
                "date_from": dt.datetime.today().strftime("%d/%m/%Y"),
                # "date_from": "16/04/2024",
                "date_to": (dt.datetime.today() + dt.timedelta(10*30)).strftime("%d/%m/%Y"),
                "max_stopovers": 0,
                #"one_for_city": 1,
                "price_from": 20,
                "price_to": item[1],
                # "price_to": 100

            }
            header = {
                "apikey": kiwi_key,
            }
            response = self.requests.get(url=url, params=params, headers=header)
            try:
                data = response.json()["data"]
            except IndexError:
                print(f"{item} data couldn't find!")
            except KeyError:
                print(f"{item} data couldn't find!")
            else:
                self.searched_data.append(data)


