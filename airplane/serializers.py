from rest_framework import serializers

from .models import AirplaneModel


class AirplaneSerializer(serializers.Serializer):
    class Meta:
        model = AirplaneModel
        fields = '__all__'
