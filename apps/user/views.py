from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.profile_.serializers import ProfileAvatarSerializer
from apps.user.models import CustomUser
from apps.user.serializers import UserSerializer, UserUpdateSerializer

UserModel: CustomUser = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserActivateView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_active": True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDeactivateView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_active": False})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDoSuperuserView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_superuser": True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDoUserView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_superuser": False})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserAddAvatarView(GenericAPIView, UpdateModelMixin):
    serializer_class = ProfileAvatarSerializer

    def get_object(self):
        return self.request.user.profile

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)
