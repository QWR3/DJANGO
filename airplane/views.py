from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AirplaneSerializer
from .models import AirplaneModel


# Create your views here.


class Airplane_list_get_create(APIView):
    def get(self, *args, **kwargs):
        airplanes = AirplaneModel.objects.all()
        serializer = AirplaneSerializer(instance=airplanes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AirplaneSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class Airplane_read_update_delete(APIView):
    def get(self, *):