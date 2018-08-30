"""
Just a fake serializer. No database needed.
"""
from datetime import datetime, timedelta
import dateutil.parser

from temperature.client import TemperatureClient

class TemperatureSerializer(object):

    def get_temperature_from_client(self, date):
        temperature_client = TemperatureClient()
        params = {'at': date}
        resp = temperature_client.request('get', params)
        return resp.json()

    def get_datetime_from_ISO8601(self, string):
        dt_result = dateutil.parser.parse(string)
        return dt_result

    def get_delta(self, start, end):
        first_date = self.get_datetime_from_ISO8601(start)
        second_date = self.get_datetime_from_ISO8601(end)
        delta = second_date - first_date
        diff_in_days = delta.days
        return diff_in_days

    def all_data(self, start_date, end_date):
        delta = self.get_delta(start_date, end_date)
        result_data = []

        for day in range(delta + 1):
            one_snippet = self.get_temperature_from_client(start_date)
            result_data.append(one_snippet)
            start_date = self.get_datetime_from_ISO8601(start_date) + timedelta(days=1)
            start_date = start_date.isoformat()

        return result_data
