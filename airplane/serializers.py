from rest_framework import serializers

from .models import AirplaneModel


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneModel
        fields = ['id', 'model', 'brand']
