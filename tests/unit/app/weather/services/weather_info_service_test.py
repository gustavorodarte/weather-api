import pytest

from weather.app.weather.services.weather_info_service import get_info
from weather.domain.entities.weather_info import WeatherInfo, Location, CurrentWeather

@pytest.fixture(name="city_name")
def city_name():
    return "London"

@pytest.fixture(name="weather_info")
def weather_info(city_name):
    location = {
      'city_name': city_name,
      'longitude': 139,
      'latitude': 35,
    }

    current_weather = {
      'temp': 281.52,
      'max_temp': 283.71,
      'min_temp': 280.15,
      'weather_description': 'clear sky',
      'humidity': 93,
      'pressure': 1016,
    }

    weather_info = {
        "location": Location(**location),
        "current_weather": CurrentWeather(**current_weather),
     }
 
    return WeatherInfo(**weather_info)

@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_info(city_name, weather_info):
    async def fetch_weather_info_fn(_):
      return weather_info
      
    result = await get_info(fetch_weather_info_fn, city_name)
    assert result == weather_info