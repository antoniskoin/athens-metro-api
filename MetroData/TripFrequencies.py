from flask_restful import Resource
from bs4 import BeautifulSoup
import requests


class TripFrequencies(Resource):
    def get(self):
        duration_req = requests.get('http://www.stasy.gr/index.php?id=68&L=1').text
        return [get_frequencies_line1(duration_req), get_frequencies_line2_3(duration_req)]


def get_frequencies_line1(metro):
    soup = BeautifulSoup(metro, "html.parser")
    frequencies_weekdays = dict()
    frequencies_weekend = dict()
    table = soup.find('table', {"class": "ticket_tbl"})
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 1:
            cols = row.find_all('td')
            metro_hours = cols[0].text
            if 1 < i < 8:
                if "MONDAY" in metro_hours:
                    metro_hours = cols[1].text
                    metro_frequency = cols[2].text
                else:
                    metro_hours = cols[0].text
                    metro_frequency = cols[1].text
                frequencies_weekdays[metro_hours] = metro_frequency
            elif i > 8:
                if "SATURDAY" in metro_hours:
                    metro_hours = cols[1].text
                    metro_frequency = cols[2].text
                else:
                    metro_hours = cols[0].text
                    metro_frequency = cols[1].text
                frequencies_weekend[metro_hours] = metro_frequency
        i = i + 1
    return [{'monday_friday_line1': frequencies_weekdays}, {'saturday_sunday_line1': frequencies_weekend}]


def get_frequencies_line2_3(metro):
    soup = BeautifulSoup(metro, "html.parser")
    frequencies_weekdays_2 = dict()
    frequencies_weekend_2 = dict()
    frequencies_weekdays_3 = dict()
    frequencies_weekend_3 = dict()
    table = soup.find_all('table', {"class": "ticket_tbl"})[1]
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 1:
            cols = row.find_all('td')
            metro_hours = cols[0].text
            if 1 < i < 5:
                if "MONDAY" in metro_hours:
                    metro_hours = cols[1].text
                    metro_frequency = cols[2].text
                else:
                    metro_hours = cols[0].text
                    metro_frequency = cols[1].text
                frequencies_weekdays_2[metro_hours] = metro_frequency
                frequencies_weekdays_3[metro_hours] = metro_frequency
            elif i > 5:
                if "SATURDAY" in metro_hours:
                    metro_hours = cols[1].text
                    metro_frequency = cols[2].text
                else:
                    metro_hours = cols[0].text
                    metro_frequency = cols[1].text
                frequencies_weekend_2[metro_hours] = metro_frequency
                frequencies_weekend_3[metro_hours] = metro_frequency
        i = i + 1
    return [{'monday_friday_line2': frequencies_weekdays_2}, {'saturday_sunday_line2': frequencies_weekend_2}], \
           [{'monday_friday_line3': frequencies_weekdays_3}, {'saturday_sunday_line3': frequencies_weekend_3}]
