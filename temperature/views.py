from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TemperatureSerializer


class TemperatureList(APIView):
    """
    List all temperatures between start_date and end_date.
    """
    def get(self, request, format=None):
        serializer = TemperatureSerializer()
        context = {
            'start': start_date,
            'end': end_date
            }
        return Response().render(data=serializer.data, renderer_context=context)