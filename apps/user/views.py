from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from apps.profile_.serializers import ProfileAvatarSerializer
from apps.user.models import CustomUser
from apps.user.serializers import UserSerializer, UserUpdateSerializer
from constants.constants import ResponseConstants
from paginations.my_pagination import MyPagination
from permissions.is_superuser import IsSuperuser

UserModel: CustomUser = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['email', 'profile.born']

    def get_serializer_context(self):
        return {"request": self.request}


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserActivateView(GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_active": True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, ResponseConstants.created.status)


class UserDeactivateView(GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_active": False})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, ResponseConstants.created.status)


class UserDoSuperuserView(GenericAPIView):
    permission_classes = [IsSuperuser]

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_superuser": True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, ResponseConstants.created.status)


class UserDoUserView(GenericAPIView):
    permission_classes = [IsSuperuser]

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_object_or_404(UserModel, pk=pk)
        user = UserModel.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data={"is_superuser": False})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, ResponseConstants.created.status)


class UserAddAvatarView(GenericAPIView, UpdateModelMixin):
    serializer_class = ProfileAvatarSerializer

    def get_object(self):
        return self.request.user.profile

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)
