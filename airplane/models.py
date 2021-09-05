from datetime import datetime

from django.db import models
from django.core import validators as v


# Create your models here.


class AirplaneModel(models.Model):
    class Meta:
        db_table = 'airplanes'
    brand = models.CharField(max_length=255, validators=[v.MinLengthValidator(2)])
    model = models.CharField(max_length=255, validators=[v.MinLengthValidator(2)])
    speed = models.IntegerField(validators=[v.MinValueValidator(250), v.MaxValueValidator(2000)])
    year = models.IntegerField(validators=[v.MinValueValidator(2000), v.MaxValueValidator(datetime.now().year)])
    number_of_passengers = models.IntegerField(validators=[v.MinValueValidator(10), v.MaxValueValidator(100)])
    max_range_of_flight = models.IntegerField(validators=[v.MinValueValidator(500), v.MaxValueValidator(50000)])
