from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin, \
    ListModelMixin
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer


# Create your views here.
class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):
        auto_park_id = dict(self.request.query_params)['autoParkId'][0]
        if auto_park_id:
            cars = CarModel.objects.filter(auto_park=int(auto_park_id))
            serializer = self.serializer_class(instance=cars, many=True)
            print(serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return self.list(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

# class CarListFromAutoPark(GenericAPIView):
#     def get(self, *args, **kwargs):
#         # get_object_or_404
#         id = self.request.query_params
#         print(id)
