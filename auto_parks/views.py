from django.forms import model_to_dict
from django.http import QueryDict
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django.shortcuts import render
from rest_framework.response import Response

from cars.models import CarModel
from cars.serializers import CarSerializer
from .serializers import AutoParkSerializer
from .models import AutoParkModel


# Create your views here.
class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkCrateCar(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        cars = CarModel.objects.filter(auto_park=pk)
        serializer = CarSerializer(instance=cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        self.request.POST._mutable = True
        self.request._mutable = True
        pk = kwargs['pk']
        data = self.request.data
        data.update({'auto_park': pk})
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
