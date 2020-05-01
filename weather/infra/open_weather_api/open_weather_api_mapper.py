from weather.app.weather.entities.weather_info import WeatherInfo, Location, CurrentWeather
from typing import Dict

def to_entity(data: Dict) -> WeatherInfo:

  location = {
    'city_name': data['name'],
    'longitude': data['coord']['lon'],
    'latitude': data['coord']['lat'],
  }

  current_weather = {
    'temp': data['main']['temp'],
    'min_temp': data['main']['temp_min'],
    'max_temp': data['main']['temp_max'],
    'weather_description': data['weather'][0]['description'],
    'humidity': data['main']['humidity'],
    'pressure': data['main']['pressure'],
    }

  weather_info = {
    'location': Location(**location),
    'current_weather': CurrentWeather(**current_weather),
  }
  return WeatherInfo(**weather_info)



  