import requests
import os

class TemperatureClient(object):
    def __init__(self):
        self.endpoint = os.environ.get('TEMPERATURE_ENDPOINT', 'http://localhost:8000/')
        self.session = requests.Session()

        
        # 'https://http://localhost:8000/?at{}'.format(
        #     datetime.datetime.now().replace(microsecond=0).isoformat()))
        # self.session = requests.session() -> we could do the request over here if we want to

    def url(self, _url):
        return '{}{}'.format(self.endpoint, _url)

    def request(self, url, method='get', params={}, data={}):
        f = getattr(self.session, method)
        resp = f(self.url(url), params=params, data=data)
        return resp