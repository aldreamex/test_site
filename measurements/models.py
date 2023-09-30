from django.db import models
from datetime import datetime

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
