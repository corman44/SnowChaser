import requests
import logging
import traceback
import os
from requests import exceptions
from requests.api import request
from dotenv import load_dotenv
load_dotenv()

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
    token       = os.getenv('OPEN_WEATHER_TOKEN')
    header = {}
    payload = {'appid': token}

    def __init__(self) -> None:
        super().__init__()

    def get_current_weather_gps(self, lat, lon):
        """
        returns JSON of current weather given lat and lon
        returns error code if failure occur
        """

        payload = self._set_payload_gps(lat,lon)
        
        #get current weather result of lat lon cooridantes
        try:
            result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
            pass
        except Exception as e:
            #log exception
            logging.error(traceback.format_exc())

            print("retrying request")
            result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
            pass

        if result.status_code == requests.codes.ok:
            return result.json()
        else:
            return result.status_code
    
    def get_current_weather_city(self, city):
        """
        returns JSON of current weather given city name
        returns error code if failure occur
        """
        payload = self._set_payload_city(city)

        #get current weather result of lat lon cooridantes
        try:
            result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
            pass
        except Exception as e:
            #log exception
            logging.error(traceback.format_exc())

            print('retrying request')
            result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
            pass

        if result.status_code == requests.codes.ok:
            return result.json()
        else:
            return result.status_code

    def get_48hour_forecast_gps(self, lat, lon):
        """
        return 48 Hour Hourly forecast based on GPS location
        returns error code if failure
        """
        exclude=b"current,minutely,daily,alerts"
        payload = self._set_payload_gps(lat,lon,exclude)
        
        #get current weather result of lat lon cooridantes
        try:
            result = requests.get(self.url_base + 'onecall', params=payload, headers=self.header)
            pass
        except Exception as e:
            #log exception
            logging.error(traceback.format_exc())

            print("retrying request")
            result = requests.get(self.url_base + 'onecall', params=payload, headers=self.header)
            pass

        print(result.url)
        if result.status_code == requests.codes.ok:
            return result.json()
        else:
            return result.status_code



    #Private method for creating GPS related payload
    def _set_payload_gps(self, lat,lon,exclude=''):
        payload = {}
        payload.update(self.payload)
        payload['lat'] = lat
        payload['lon'] = lon

        #check if including exclude parameter
        if len(exclude) > 0:
            payload['exclude'] = exclude
        
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
    #print(x.get_current_weather_gps(45.330558,-121.711615))
    #print("")
    #print(x.get_current_weather_city('Government Camp, US'))
    #print('')
    print(x.get_48hour_forecast_gps(45.330558,-121.711615))
    pass