import requests
import logging
import traceback
from requests import exceptions
from requests.api import request

class open_weather_hitter():
    """
    Get and return weather data from OpenWeather API
    - Current Weather
    - Minute forecast for 1 hour
    - Hourly forecast for 48 hours
    - Daily forecast for 7 days
    - Historical data for 5 previous days
    - 5 day per 3 hour forecast
    - Air Pollution API
    """

    url_base    = 'http://api.openweathermap.org/data/2.5/'
    token       = '1a4d180ffc35d8e5f8cd405d6caf99f1'
    header = {}
    payload = {'appid': token}

    def __init__(self):
        pass

    #Return current weather based on a GPS location
    def get_current_weather_gps(self, lat, lon):
        payload = self._set_payload_gps(lat,lon)
        
        #get current weather result of lat lon cooridantes
        try:
            result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
        except Exception as e:
            #log exception
            logging.error(traceback.format_exc())

            print("retrying request")
            result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)

        if result.status_code == requests.codes.ok:
            return result.json()
        else:
            return result.status_code
    
    #Return Current Weather based on a city name
    def get_current_weather_city(self, city):
        payload = self._set_payload_city(city)

        #get current weather result of lat lon cooridantes
        result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
        print(result.request.url)

        if result.status_code == requests.codes.ok:
            return result.json()
        else:
            return result.status_code

    #Private method for creating GPS related payload
    def _set_payload_gps(self, lat,lon):
        payload = {}
        payload.update(self.payload)
        payload['lat'] = lat
        payload['lon'] = lon
        return payload

    #Private method for creating City related payload
    def _set_payload_city(self, city):
        payload = {}
        payload['q'] = city
        payload.update(self.payload)
        return payload



if __name__ == "__main__":

    #Timberline GPS Coords
    x = open_weather_hitter()
    print(x.get_current_weather_gps(45.330558,-121.711615))
    print("")
    print(x.get_current_weather_city('Government Camp, US'))
    pass