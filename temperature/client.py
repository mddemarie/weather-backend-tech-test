import requests
import os

class TemperatureClient(object):
    def __init__(self):
        self.endpoint = os.environ.get('TEMPERATURE_ENDPOINT', 'http://temperature:8000/?')
        self.session = requests.Session()

    def request(self, method='get', params={}, data={}):
        f = getattr(self.session, method)
        resp = f(self.endpoint, params=params, data=data)
        return resp
