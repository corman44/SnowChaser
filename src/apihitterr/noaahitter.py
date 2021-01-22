import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

class noaa_hitter(lat=0, lon=0):
    """
    Get weather data from NOAA API
    - Hourly forecast from 2.5km Grid location
    """
    url = 'https://api.weather.gov/'
    token = os.getenv('NOAA_TOKEN')
    dataset_endpoint = 'datasets'
    
    header = {'token': token}
    payload = {'User-Agent': '(myapp.com, foo@foo.com)'}

    def get_48hr_forecast(self , x, y):
        """
        returns 48 hour forecasted data for a region otherwise, returns http response
        """
        result = requests.get(url + dataset_endpoint, headers=header, params=payload)
        return result.json()


if __name__ == "__main__":
    
    pass
