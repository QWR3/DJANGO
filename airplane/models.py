from django.db import models
from django.core import validators as v


# Create your models here.

class AirplaneModel(models.Model):
    class Meta:
        db_table = 'airplanes'
    brand = models.CharField(max_length=255, validators=[v.MinLengthValidator(3)])
    model = models.CharField(max_length=255, validators=[v.MinLengthValidator(3)])
    speed = models.IntegerField(validators=[v.MinValueValidator(250), v.MaxValueValidator(2000)])
    length = models.IntegerField(validators=[v.MinValueValidator(10), v.MaxValueValidator(100)])
    number_of_passengers = models.IntegerField(validators=[v.MinValueValidator(10), v.MaxValueValidator(100)])
    max_range_of_flight = models.IntegerField(validators=[v.MinValueValidator(500), v.MaxValueValidator(50000)])
