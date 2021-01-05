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

def noaa_hitter(lat, lon):
    """
    Get weather data from NOAA API (not defined)
    """
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
    token = 'LfxZeKJJIQXTfiomXFDkBLrFbiXuARcL'
    dataset_endpoint = '/datasets'
    
    pass

if __name__ == "__main__":
    x = open_weather_hitter(45.330558, -121.711615)
    print(x)
    pass