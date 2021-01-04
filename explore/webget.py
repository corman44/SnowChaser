import requests

#NOAA Consts
noaa_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
noaa_token = 'LfxZeKJJIQXTfiomXFDkBLrFbiXuARcL'
noaa_dataset_endpoint = '/datasets'

#Open Weather Consts
openweather_url = 'http://api.openweathermap.org/data/2.5/'
openweather_token = '1a4d180ffc35d8e5f8cd405d6caf99f1'
openweather_weather = 'weather'

#noaa_result = list(requests.get(noaa_url + noaa_dataset_endpoint, headers=header, params=payload))
#print(noaa_result)

header = {}

#payload = {'appid': openweather_token, 'q': 'Portland'}
#r = requests.get(openweather_url + openweather_weather, headers=header, params=payload)

payload = {'appid': openweather_token, 'lat': '45.330558', 'lon': '-121.711615'}
r = requests.get(openweather_url + openweather_weather, headers=header, params=payload)
print(r.json())