from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from temperature.data import TemperatureSerializer


class TemperatureViewSet(viewsets.ViewSet):
    """
    A view that returns the list of temperatures in JSON.
    """
    def get(self, request, *args, **kwargs):
        start = self.kwargs.get('start')
        end = self.kwargs.get('end')

        data = TemperatureSerializer().all_data(start, end)
        return JSONRenderer().render(data)
