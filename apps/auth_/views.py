from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.user.models import CustomUser
from constants.constants import ResponseConstants
from utils.jwt_utils import JwtUtils

UserModel: CustomUser = get_user_model()


class ActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        JwtUtils.validate_token(token)
        UserModel.objects.activate_user()
        return Response(status=ResponseConstants.ok.status)
