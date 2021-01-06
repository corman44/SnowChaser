import requests

def open_weather_hitter(lat, lon):
    """
    Get weather data from OpenWeather API
    """
    url_base    = 'http://api.openweathermap.org/data/2.5/'
    token       = '1a4d180ffc35d8e5f8cd405d6caf99f1'

    header = {}
    payload = {'appid': token, 'lat': lat, 'lon': lon}   
    result = requests.get(url_base + 'weather', params=payload, headers=header)
    
    return result.json()

def noaa_hitter(lat=0, lon=0):
    """
    Get weather data from NOAA API
    """
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    token = 'LfxZeKJJIQXTfiomXFDkBLrFbiXuARcL'
    dataset_endpoint = 'datasets'
    
    header = {'token': token}
    payload = {}

    result = requests.get(url + dataset_endpoint, headers=header, params=payload)
    return result.json()

    pass

if __name__ == "__main__":
    x = open_weather_hitter(45.330558, -121.711615)
    print(x)
    y = noaa_hitter()
    print(y)
    pass