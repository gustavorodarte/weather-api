from weather.app.weather.entities.weather_info import WeatherInfo
from typing import Dict

def to_entity(data: Dict) -> WeatherInfo:
  weather_info = {
    'city_name': data['name'],
    'temp': data['main']['temp'],
    'temp_min': data['main']['temp_min'],
    'temp_max': data['main']['temp_max'],
    'main': data['weather'][0]['main'],
  }
  return WeatherInfo(**weather_info)