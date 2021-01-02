import requests

url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
token = 'LfxZeKJJIQXTfiomXFDkBLrFbiXuARcL'

endpoint = '/datasets'
header = {'Token': token}
payload = {}

r = list(requests.get(url + endpoint, headers=header, params=payload))
print(r)