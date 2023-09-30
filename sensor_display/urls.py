from django.urls import path
from . import views

urlpatterns = [
    path('displayed-sensors/', views.displayed_sensors, name='displayed-sensors'),
]