from rest_framework import serializers as s
from .models import CarModel


class CarSerializer(s.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
