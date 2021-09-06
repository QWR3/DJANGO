from rest_framework import serializers

from .models import AirplaneModel


class AirplaneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneModel
        fields = ['id', 'model', 'brand']


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneModel
        fields = "__all__"
