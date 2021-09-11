from datetime import datetime

from django.db import models
from django.core import validators as v

# Create your models here.
from auto_parks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=255, validators=[v.MinLengthValidator(3)])
    model = models.CharField(max_length=255, validators=[v.MinLengthValidator(3)])
    year = models.IntegerField(validators=[v.MinValueValidator(1970), v.MaxValueValidator(datetime.now().year)])
    cost = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.model