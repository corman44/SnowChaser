import requests
import os

class noaa_hitter(lat=0, lon=0):
    """
    Get weather data from NOAA API
    - Hourly forecast from 2.5km Grid location
    """
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    
    #TODO: Update TOKEN to use request api instead of the weather station data
    token = os.getenv('NOAA_TOKEN')
    dataset_endpoint = 'datasets'
    
    header = {'token': token}
    payload = {}

    def __init__(self) -> None:
        super().__init__()

    def (self, parameter_list):
        """
        docstring
        """
        result = requests.get(url + dataset_endpoint, headers=header, params=payload)
        return result.json()