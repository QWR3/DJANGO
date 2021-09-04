from django.db import models


# Create your models here.

class PC(models.Model):
    class Meta:
        db_table = 'my_pc'
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    RAM = models.IntegerField()
    CPU_frequency = models.IntegerField()
    monitor = models.IntegerField()
