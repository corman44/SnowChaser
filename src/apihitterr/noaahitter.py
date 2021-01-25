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
    dataset_endpoint = 'datasets'
    
    #header = {'token': token}
    payload = {'User-Agent': '(myapp.com, foo@foo.com)'}

    def get_48hr_forecast(self , x, y):
        """
        returns 48 hour forecasted data for a region otherwise, returns http response
        """
        result = requests.get(self.url + self.dataset_endpoint, headers=header, params=payload)
        return result.json()

    def get_gridpoints(self, lat, lon):
        #TODO: build out getter for lat lon, return endpoints for different time periods of forecast 
        ret office, gridX, gridY


if __name__ == "__main__":
    lat = 45.330558
    lon = -121.711615
    url = 'https://api.weather.gov/'
    header = {'User-Agent': '(myweatherapp.com, contact@myweatherapp.com)'}
    payload = {'lat':lat, 'lon':lon}
    ret = requests.get(url + 'points/' + str(lat) + ',' + str(lon))
    print(ret.url)
    print(ret.status_code)
    print(ret.content)
    pass
