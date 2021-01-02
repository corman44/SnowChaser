import requests

noaa_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
noaa_token = 'LfxZeKJJIQXTfiomXFDkBLrFbiXuARcL'

openweather_url = 'http://api.openweathermap.org/'
openweather_token = '1a4d180ffc35d8e5f8cd405d6caf99f1'


noaa_dataset_endpoint = '/datasets'

header = {'Token': noaa_token}
payload = {}

noaa_result = list(requests.get(noaa_url + noaa_dataset_endpoint, headers=header, params=payload))
print(noaa_result)