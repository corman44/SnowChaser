import requests
import os

def noaa_hitter(lat=0, lon=0):
    """
    Get weather data from NOAA API
    """
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    token = os.getenv('NOAA_TOKEN')
    dataset_endpoint = 'datasets'
    
    header = {'token': token}
    payload = {}

    result = requests.get(url + dataset_endpoint, headers=header, params=payload)
    return result.json()