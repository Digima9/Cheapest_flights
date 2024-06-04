import smtplib
import datetime as dt
import html
import codecs

email = "umitaslan.au@gmail.com"
password = "sfct xapa ccef hglz"
email_to ="aslan_umit@yahoo.com"
email_to2 ="popesculaura3081@yahoo.com"


class NotificationManager:
    def __init__(self, final_data):
    #This class is responsible for sending notifications with the deal flight details.
        self.final_data = final_data
        with smtplib.SMTP("smtp.gmail.com") as self.connection:

            self.connection.starttls()
            self.connection.login(user=email, password=password)
            self.send_email()

    def send_email(self):
        global email
        msg = ''
        for item in self.final_data:
            a = item["stopover"].encode(encoding="utf-8")

            msg += (f'{self.final_data.index(item)+1}-From: {item["city_from"]} To: {item["city to"].encode()} Price: '
                    f'{item["price(eur) "]} Eur\n Departure: {item["departure time"].split("T")}\n '
                    f'Arrival: {item["arrival time"].split("T")}\n Airlines and Flight No:{item["airlines"]}\n'
                    f'Flight Stoppage:{item["stopover"]}\n\n')

        self.connection.sendmail(from_addr=email,
                                 to_addrs=email_to2,
                                 msg=f'Subject:Cheapest Flights between {dt.datetime.today().strftime("%d/%m/%Y")}-'
                                     f'{(dt.datetime.today() + dt.timedelta(10 * 30)).strftime("%d/%m/%Y")}'
                                     f'\n\nHello\n\nFlights found:\n\n{msg}')
