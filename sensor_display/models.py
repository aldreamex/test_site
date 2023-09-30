from django.db import models

class DisplayedSensor(models.Model):
    sensor = models.ForeignKey('measurements.Sensor', on_delete=models.CASCADE)
