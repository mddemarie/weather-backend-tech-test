from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.generic.base import View
from django.shortcuts import render

from .serializers import TemperatureSerializer


class TemperatureList(View):
    """
    List all temperatures between start_date and end_date.
    """
    def get(self, request, *args, **kwargs):
        # start = self.request.start
        # end = self.request.end
        start = self.kwargs.get('start')
        end = self.kwargs.get('end')

        data = TemperatureSerializer().data(start, end)
        
        # print(serializer.data('2018-08-12T00:00:00Z', '2018-08-14T00:00:00Z'))
        return render(data)