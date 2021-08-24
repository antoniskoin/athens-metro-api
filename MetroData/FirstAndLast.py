from flask_restful import Resource
from bs4 import BeautifulSoup
import requests


class FirstLast(Resource):
    def get(self):
        metro = requests.get('http://www.stasy.gr/index.php?id=67&L=1', verify=False).text
        # metro = metro.encode('windows-1253')
        return [get_line1(metro), get_line2(metro), get_line3(metro)]


def get_line1(metro_data):
    soup = BeautifulSoup(metro_data, "html.parser")
    table_data = dict()
    table = soup.find('table', {"class": "ticket_tbl"})
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 2:
            cols = row.find_all('td')
            metro_from = cols[0].text.strip()
            first = cols[1].text.strip()
            last = cols[2].text.strip()
            first_and_last = [first, last]
            table_data[metro_from] = first_and_last
        i = i + 1

    return {'first_last_metro_line1': table_data}


def get_line2(metro_data):
    soup = BeautifulSoup(metro_data, "html.parser")
    table_data = dict()
    table = soup.find_all('table', {"class": "ticket_tbl"})[1]
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 4:
            cols = row.find_all('td')
            metro_from = cols[0].text.strip()
            first = cols[1].text.strip()
            last = cols[2].text.strip()
            first_and_last = [first, last]
            table_data[metro_from] = first_and_last
        i = i + 1

    return {'first_last_metro_line2': table_data}


def get_line3(metro_data):
    soup = BeautifulSoup(metro_data, "html.parser")
    table_data = dict()
    table = soup.find_all('table', {"class": "ticket_tbl"})[2]
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 4:
            cols = row.find_all('td')
            metro_from = cols[0].text.strip()
            first = cols[1].text.strip()
            last = cols[2].text.strip()
            first_and_last = [first, last]
            table_data[metro_from] = first_and_last
        i = i + 1

    return {'first_last_metro_line2': table_data}
