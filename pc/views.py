from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

from .models import PC


# Create your views here.

class PC_list_get_create(APIView):
    def get(self, *args, **kwargs):
        computer = PC.objects.all().values()
        return Response(computer, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.query_params.dict()
        computer = PC.objects.create(**data)
        return Response(model_to_dict(computer), status.HTTP_201_CREATED)


class PC_read_update_delete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = PC.objects.filter(pk=pk).exclude()
        if not exclude:
            return Response(f'sorry, but we have not pc with id {pk}', status.HTTP_404_NOT_FOUND)
        computer = PC.objects.get(pk=pk)
        return Response(model_to_dict(computer), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = PC.objects.filter(pk=pk).exclude()
        if not exclude:
            return Response(f'sorry, but we have not pc with id {pk}', status.HTTP_404_NOT_FOUND)
        data = self.request.query_params.dict()
        PC.objects.filter(pk=pk).update(**data)
        computer = PC.objects.get(pk=pk)
        return Response(model_to_dict(computer), status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = PC.objects.filter(pk=pk).exclude()
        if not exclude:
            return Response(f'sorry, but we have not pc with id {pk}', status.HTTP_404_NOT_FOUND)
        computer = PC.objects.get(pk=pk)
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
