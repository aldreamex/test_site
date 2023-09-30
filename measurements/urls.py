from django.urls import path
from .views import SensorListView, SensorDetailView, MeasurementCreateView, MeasurementListView

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/<pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('measurements/all/', MeasurementListView.as_view(), name='measurement-list'),
]