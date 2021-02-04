import logging
import requests
import os
from dotenv import load_dotenv
from requests.models import parse_url
load_dotenv('.env')

class noaa_hitter():
    """
    Get weather data from NOAA API
    - Hourly forecast from 2.5km Grid location
    """
    url = 'https://api.weather.gov/'
    #token = os.getenv('NOAA_TOKEN')
    points_endpoint = 'points/'
    
    #payload = {'User-Agent': '(myapp.com, foo@foo.com)'}

    def get_48hr_forecast(self , x, y):
        """
        returns 48 hour forecasted data for a region otherwise, returns http response
        """
        pass
        #return result.json()

    def get_gridpoints(self, lat, lon):
        #TODO: build out getter for lat lon, return endpoints for different time periods of forecast 
        
        url = 'https://api.weather.gov/'
        header = {'User-Agent': '(myweatherapp.com, contact@myweatherapp.com)'}
        payload = {'lat':lat, 'lon':lon}

        try:
            result = requests.get(url + 'points/' + str(lat) + ',' + str(lon))
            print(result.url)
            print(result.status_code)
            print(result.content)
        except Exception as e:
            #log exception
            logging.error(traceback.format_exc())

            print("retrying request")
            result = requests.get(url + 'points/' + str(lat) + ',' + str(lon))
        
        pass


if __name__ == "__main__":
    lat = 45.330558
    lon = -121.711615

    x = noaa_hitter()
    x.get_gridpoints(lat,lon)

    pass
