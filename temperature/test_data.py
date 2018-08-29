import unittest
import datetime
from tzlocal import get_localzone

from .data import TemperatureSerializer

class TemperatureTestCase(unittest.TestCase):
    """Tests for 'data.py'."""

    def test_get_temperature_from_client(self):
        date = "2018-08-12T00:00:00Z"
        serializer = TemperatureSerializer()
        result = serializer.get_temperature_from_client(date)
        test_result = {
            "temp":10.46941232124016,
            "date":"2018-08-12T00:00:00Z"
            }

        self.assertEqual(result, test_result)

    def test_get_datetime_from_ISO8601(self):
        isoformat = "2018-08-12T00:00:00Z"
        serializer = TemperatureSerializer()
        result =  serializer.get_datetime_from_ISO8601(isoformat)
        test_result = datetime.datetime(2018, 8, 12, 0, 0, tzinfo=get_localzone())

        self.assertEqual(result, test_result)

    def test_get_delta(self):
        start = "2018-08-01T00:00:00Z"
        end = "2018-08-07T00:00:00Z"
        serializer = TemperatureSerializer()
        result = serializer.get_delta(start, end)

        self.assertEqual(result, 6)

    def test_all_data(self):
        start_date = "2018-08-01T00:00:00Z"
        end_date = "2018-08-07T00:00:00Z"
        serializer = TemperatureSerializer()
        result = serializer.all_data(start_date, end_date)
        test_result = [
            {'temp': 12.037116255932265, 'date': '2018-08-01T00:00:00Z'},
            {'temp': 10.748827693846698, 'date': '2018-08-02T00:00:00Z'},
            {'temp': 9.55776925245165, 'date': '2018-08-03T00:00:00Z'},
            {'temp': 12.293283312397936, 'date': '2018-08-04T00:00:00Z'},
            {'temp': 9.061370411273243, 'date': '2018-08-05T00:00:00Z'},
            {'temp': 12.071404446393888, 'date': '2018-08-06T00:00:00Z'},
            {'temp': 10.63004921027248, 'date': '2018-08-07T00:00:00Z'}]

        self.assertEqual(result, test_result)

if __name__ == '__main__':
    unittest.main()