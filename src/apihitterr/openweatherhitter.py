import requests

class open_weather_hitter():
    """
    Get and return weather data from OpenWeather API
    - Current Weather
    - Minute forecast for 1 hour
    - Hourly forecast for 48 hours
    - Daily forecast for 7 days
    - Historical data for 5 previous days
    - 5 day per 3 hour forecast
    - Air Pollution API
    """

    url_base    = 'http://api.openweathermap.org/data/2.5/'
    token       = '1a4d180ffc35d8e5f8cd405d6caf99f1'
    header = {}
    payload = {'appid': token}

    def __init__(self):
        pass

    def get_current_weather_gps(self, lat, lon):
        payload = self._set_payload_gps(lat,lon)
        #get current weather result of lat lon cooridantes
        result = requests.get(self.url_base + 'weather', params=payload, headers=self.header)
        return result.json()
    
    def get_current_weather_city(self, city):
        payload = self._set_payload_city(city)

        #get current weather result of lat lon cooridantes
        result = requests.get(self.url_base + 'city', params=payload, headers=self.header)
        return result.json()

    def get_current_4day_forecast_gps(self, lat,lon):
        payload = self._set_payload_gps(lat,lon)

        #get 4 day forecase by gps
        result = requests.get(self.url_base + 'city', params=payload, headers=self.header)
        return result.json()

    #Private method for creating GPS related payload
    def _set_payload_gps(self, lat,lon):
        payload = self.payload
        payload['lat'] = lat
        payload['lon'] = lon
        return payload

    #Private method for creating City related payload
    def _set_payload_city(self, city):
        payload = self.payload
        payload['city'] = city
        return payload



if __name__ == "__main__":

    #Timberline GPS Coords
    x = open_weather_hitter(45.330558, -121.711615)
    print(x)
    pass