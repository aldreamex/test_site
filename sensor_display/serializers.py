from rest_framework import serializers
from .models import DisplayedSensor

class DisplayedSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayedSensor
        fields = '__all__'
