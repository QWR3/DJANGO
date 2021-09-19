from rest_framework import serializers

from apps.profile_.models import ProfileModel


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ['user', ]


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['avatar']
        extra_kwargs = {
            'avatar': {'required': True}
        }
