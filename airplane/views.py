from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AirplaneSerializer, AirplaneListSerializer
from .models import AirplaneModel


# Create your views here.


class Airplane_list_get_create(APIView):
    def get(self, *args, **kwargs):
        airplanes = AirplaneModel.objects.all()
        serializer = AirplaneListSerializer(instance=airplanes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AirplaneListSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class Airplane_read_update_delete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AirplaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(f"sorry, but we did not have any airplane with id {pk}", status.HTTP_404_NOT_FOUND)
        airplane = AirplaneModel.objects.get(pk=pk)
        return Response(model_to_dict(airplane), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AirplaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(f"sorry, but we did not have any airplane with id {pk}", status.HTTP_404_NOT_FOUND)
        data = self.request.data
        airplane = AirplaneModel.objects.get(pk=pk)
        serializer = AirplaneSerializer(instance=airplane, data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AirplaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(f"sorry, but we did not have any airplane with id {pk}", status.HTTP_404_NOT_FOUND)
        airplane = AirplaneModel.objects.get(pk=pk)
        airplane.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
