from django.contrib.auth import get_user_model
from django.forms import model_to_dict

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from user.models import CustomUser
from user.serializers import UserSerializer

UserModel: CustomUser = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserActivateView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        UserModel.objects.filter(pk=pk).update(is_active=True)
        user = UserModel.objects.get(pk=pk)
        return Response(model_to_dict(user), status.HTTP_201_CREATED)


class UserDeactivateView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        UserModel.objects.filter(pk=pk).update(is_active=False)
        user = UserModel.objects.get(pk=pk)
        return Response(model_to_dict(user), status.HTTP_201_CREATED)


class UserDoSuperuserView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        UserModel.objects.filter(pk=pk).update(is_superuser=True)
        user = UserModel.objects.get(pk=pk)
        return Response(model_to_dict(user), status.HTTP_201_CREATED)


class UserDoUserView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        UserModel.objects.filter(pk=pk).update(is_superuser=False)
        user = UserModel.objects.get(pk=pk)
        return Response(model_to_dict(user), status.HTTP_201_CREATED)
