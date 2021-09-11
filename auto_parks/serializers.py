from rest_framework import serializers as s

from auto_parks.models import AutoParkModel
from cars.serializers import CarSerializer


class AutoParkSerializer(s.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ['id', 'name', 'city', 'street', 'cars']
