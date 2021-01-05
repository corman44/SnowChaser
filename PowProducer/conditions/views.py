import requests
from django.shortcuts import render
from django.http import HttpResponse

tLineLodgelat = 45.330558
tLineLodgelng = -121.711615

def open_weather_hitter(lat, lon):
    """
    Get weather data from OpenWeather API
    """
    url_base    = 'http://api.openweathermap.org/data/2.5/'
    token       = '1a4d180ffc35d8e5f8cd405d6caf99f1'

    header = {}
    payload = {'appid': token, 'lat': lat, 'lon': lon}   
    result = requests.get(url_base + 'weather', params=payload, headers=header)
    
    return result.content

def noaa_hitter(lat, lon):
    """
    Get weather data from NOAA API (not defined)
    """
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    token = 'LfxZeKJJIQXTfiomXFDkBLrFbiXuARcL'
    dataset_endpoint = '/datasets'
    
    return "foobar"

# Create your views here.
def openWeather(request):
    weatherData = open_weather_hitter(tLineLodgelat, tLineLodgelng)
    return HttpResponse(weatherData)

def noaa(request):
    weatherData = noaa_hitter(tLineLodgelat, tLineLodgelng)
    return HttpResponse(weatherData)
