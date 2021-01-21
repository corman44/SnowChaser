import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

def noaa_hitter(lat=0, lon=0):
    """
    Get weather data from NOAA API
    """
    url = 'https://api.weather.gov/'
    token = os.getenv('NOAA_TOKEN')
    dataset_endpoint = 'datasets'
    
    header = {'token': token}
    payload = {}

    result = requests.get(url + dataset_endpoint, headers=header, params=payload)
    return result.json()