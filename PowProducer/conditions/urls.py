from django.urls import path
from . import views

urlpatterns = [
    path('openweather', views.openWeather, name="openweather"),
    path('noaa', views.noaa, name="noaa")
]
