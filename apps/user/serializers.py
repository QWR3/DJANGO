from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import CustomUser
from ..profile_.models import ProfileModel
from ..profile_.serializers import ProfileSerializers

UserModel: CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'email': {'required': False},
            'password': {'required': False},
            'profile': {'required': False},
        }
