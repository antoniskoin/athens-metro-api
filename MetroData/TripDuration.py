from flask_restful import Resource
from bs4 import BeautifulSoup
import requests


class TripDuration(Resource):
    def get(self):
        duration_req = requests.get('http://www.stasy.gr/index.php?id=68&L=1').text
        return [get_duration_line1(duration_req), get_duration_line2(duration_req), get_duration_line3(duration_req)]


def get_duration_line1(duration_data):
    soup = BeautifulSoup(duration_data, "html.parser")
    go_data = dict()
    return_data = dict()
    table = soup.find('table', {"class": "ticket_tbl"})
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 1:
            cols = row.find_all('td')
            metro_from = cols[0].text.strip()
            metro_duration = cols[1].text.strip()
            metro_back = cols[2].text.strip()
            metro_duration_back = cols[3].text.strip()
            go_metro = [metro_from, metro_duration]
            return_metro = [metro_back, metro_duration_back]
            go_data[metro_from] = go_metro
            return_data[metro_back] = return_metro
        i = i + 1

    return [{'go_data_line1': go_data}, {'return_data_line1': return_data}]


def get_duration_line2(duration_data):
    soup = BeautifulSoup(duration_data, "html.parser")
    go_data = dict()
    return_data = dict()
    table = soup.find_all('table', {"class": "ticket_tbl"})[1]
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 1:
            cols = row.find_all('td')
            metro_from = cols[0].text.strip()
            metro_duration = cols[1].text.strip()
            metro_back = cols[2].text.strip()
            metro_duration_back = cols[3].text.strip()
            go_metro = [metro_from, metro_duration]
            return_metro = [metro_back, metro_duration_back]
            go_data[metro_from] = go_metro
            return_data[metro_back] = return_metro
        i = i + 1

    return [{'go_data_line2': go_data}, {'return_data_line2': return_data}]


def get_duration_line3(duration_data):
    soup = BeautifulSoup(duration_data, "html.parser")
    go_data = dict()
    return_data = dict()
    table = soup.find_all('table', {"class": "ticket_tbl"})[2]
    rows = table.find_all('tr')
    i = 0
    for row in rows:
        if i > 1:
            cols = row.find_all('td')
            metro_from = cols[0].text.strip()
            metro_duration = cols[1].text.strip()
            metro_back = cols[2].text.strip()
            metro_duration_back = cols[3].text.strip()
            go_metro = [metro_from, metro_duration]
            return_metro = [metro_back, metro_duration_back]
            go_data[metro_from] = go_metro
            return_data[metro_back] = return_metro
        i = i + 1

    return [{'go_data_line3': go_data}, {'return_data_line3': return_data}]
