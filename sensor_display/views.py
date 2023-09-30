from django.shortcuts import render
from measurements.models import Sensor
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def generate_temperature_plot(temperatures, sensor_name):
    plt.figure(figsize=(8, 4))
    plt.plot(range(len(temperatures)), temperatures, marker='o', linestyle='-', color='blue', markersize=5, label='Temperature')
    plt.title(f'Temperature Readings for {sensor_name}')
    plt.xlabel('Measurement')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    return f"data:image/png;base64,{image_base64}"


def displayed_sensors(request):
    sensors = Sensor.objects.prefetch_related('measurement_set').all()

    for sensor in sensors:
        temperatures = [measurement.temperature for measurement in sensor.measurement_set.all()]
        sensor.temperature_plot = generate_temperature_plot(temperatures, sensor.name)

    context = {
        'sensors': sensors
    }
    return render(request, 'sensor_display/sensors.html', context)


