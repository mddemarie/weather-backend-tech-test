"""
Just a fake serializer. No database needed.
"""
import datetime

from .client import TemperatureClient

class TemperatureSerializer(object):

    def get_temperature(self):
        temperature_client = TemperatureClient()
        date = '{}Z'.format(datetime.datetime.now().replace(microsecond=0).isoformat())
        params = {'at': date}
        resp = temperature_client.request('get', params)
        return resp.json()

    @property
    def data(self, context={}): # I will use the context later on to try sth.
        self.get_temperature()
        