from django.db import models


# Create your models here.
class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    city = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name
