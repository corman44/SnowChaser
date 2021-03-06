import requests
import os
from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client

tLineLodgelat = 45.330558
tLineLodgelng = -121.711615

def open_weather_hitter(lat, lon):
    """
    Get weather data from OpenWeather API
    """
    url_base    = 'http://api.openweathermap.org/data/2.5/'
    token       = os.getenv('OPEN_WEATHER_TOKEN')

    header = {}
    payload = {'appid': token, 'lat': lat, 'lon': lon}   
    result = requests.get(url_base + 'weather', params=payload, headers=header)
    
    return result.content

def noaa_hitter(lat, lon):
    """
    Get weather data from NOAA API (not defined)
    """
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    token = os.getenv('NOAA_TOKEN')
    dataset_endpoint = '/datasets'
    
    return "foobar"

# Create your views here.
def openWeather(request):
    weatherData = open_weather_hitter(tLineLodgelat, tLineLodgelng)
    return HttpResponse(weatherData)

def noaa(request):
    weatherData = noaa_hitter(tLineLodgelat, tLineLodgelng)
    return HttpResponse(weatherData)

def twilioMessage(request):
    account_sid = os.getenv('TWILIO_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    phone_number = os.getenv('TWILIO_PHONE_NUMBER')
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Gumby",
                     from_=phone_number,
                     to='wouldn\'t you like to know'
                 )
    return HttpResponse(message)
