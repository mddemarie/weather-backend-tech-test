import requests
import os

class Client(object):
    def __init__(self):
        self.endpoint = os.environ.get('TEMPERATURE_ENDPOINT', 'https://http://localhost:8000/')
        
        # 'https://http://localhost:8000/?at{}'.format(
        #     datetime.datetime.now().replace(microsecond=0).isoformat()))
        # self.session = requests.session() -> we could do the request over here if we want to

    def url(self, _url):
        return '{}{}'.format(self.endpoint, _url)