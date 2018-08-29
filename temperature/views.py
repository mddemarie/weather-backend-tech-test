from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .data import TemperatureSerializer

# For testing:
# result = TemperatureSerializer()
# print(result.data('2018-08-12T00:00:00Z', '2018-08-14T00:00:00Z'))

class TemperaturesList(APIView):
    """
    A view that returns the list of temperatures in JSON.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, *args, **kwargs):
        start = self.kwargs.get('start')
        end = self.kwargs.get('end')

        data = TemperatureSerializer().all_data(start, end)
        return Response(data)
