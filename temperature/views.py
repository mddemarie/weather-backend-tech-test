# from django.shortcuts import render
import datetime

from client import TemperatureClient


def get_temperatures():
    temperature_client = TemperatureClient()
    date = '{}Z'.format(datetime.datetime.now().replace(microsecond=0).isoformat())
    url = '?'
    params = {
        'at': date
    }
    resp = temperature_client.request(url, 'get', params)
    return resp.json()

print(get_temperatures())

class TempertureList():
    pass
