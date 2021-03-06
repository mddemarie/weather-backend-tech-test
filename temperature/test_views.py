from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from urllib.parse import urlencode

from temperature.data import TemperatureSerializer


class TemperatureTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = '/temperatures'
        cls.start = '2018-08-12T00:00:00Z'
        cls.end = '2018-08-14T00:00:00Z'

        # create a temperature data for GET method
        cls.temperatures = [
            {'temp': 12.037116255932265, 'date': '2018-08-12T00:00:00Z'},
            {'temp': 10.748827693846698, 'date': '2018-08-13T00:00:00Z'},
            {'temp': 9.55776925245165, 'date': '2018-08-14T00:00:00Z'}]

        # create a list of temperature snippets for GET method with fake serializer
        cls.serializer = TemperatureSerializer()
        cls.temperature_list = cls.serializer.all_data(cls.start, cls.end)

        cls.params = urlencode({'start': cls.start, 'end': cls.end})
        cls.temperature_url = '{}?'.format(cls.url, cls.params)


    def test_list_temperatures(self):
        """
        See the list of temperatures.
        """
        client = APIClient()
        response = self.client.get(self.temperature_url, self.temperature_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response)
        self.assertEqual(len(response.data), 1)

    # integration tests for edge cases:
    # def test_list_temperatures_fails_without_start_date(self):
    #     """
    #     Start date cannot be empty.
    #     """
    #     response = self.client.get(self.url, { # fix this
    #         k: v for (k, v) in self.temperatures.items()
    #         if k is not 'date'
    #     })
    #     self.assertEqual(
    #         response.status_code, status.HTTP_400_BAD_REQUEST, response.data
    #     )
    #     self.assertEqual(response.data['start'], ['This field is required.'])

    # def test_list_temperatures_fails_without_end_date(self):
    #     """
    #     Start date field cannot be empty.
    #     """
    #     response = self.client.get(self.url, { # fix this
    #         k: v for (k, v) in self.temperatures.items()
    #         if k is not 'date'
    #     })
    #     self.assertEqual(
    #         response.status_code, status.HTTP_400_BAD_REQUEST, response.data
    #     )
    #     self.assertEqual(
    #         response.data['end'], ['This field is required.']
    #       )