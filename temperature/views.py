# from django.shortcuts import render
import datetime

from client import TemperatureClient


def get_temperature():
    temperature_client = TemperatureClient()
    date = '{}Z'.format(datetime.datetime.now().replace(microsecond=0).isoformat())
    params = {
        'at': date
    }
    resp = temperature_client.request('get', params)
    return resp.json()


class TempertureList():
    pass
