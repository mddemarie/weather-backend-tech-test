import unittest

from .client import TemperatureClient


class TemperatureTestCase(unittest.TestCase):
    """Tests for 'client.py'."""

    def test_request(self):
        date = "2018-08-12T00:00:00Z"
        client = TemperatureClient()
        result = client.request(method='get', params={'at': date})
        result = result.json()
        test_result = {
            "temp":10.46941232124016,
            "date":"2018-08-12T00:00:00Z"
            }

        self.assertEqual(result, test_result)

if __name__ == '__main__':
    unittest.main()
