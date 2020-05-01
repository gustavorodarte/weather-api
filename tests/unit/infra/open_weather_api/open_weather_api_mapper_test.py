import pytest
from weather.app.weather.entities.weather_info import WeatherInfo, Location, CurrentWeather
from weather.infra.open_weather_api.open_weather_api_mapper import to_entity

# Types
DataType = Dict[str, Any]


# Fixtures
@pytest.fixture(name="api_payload")
def api_payload_fixture() -> DataType:
    return {
      "coord": { "lon": 139,"lat": 35},
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "base": "stations",
      "main": {
        "temp": 281.52,
        "feels_like": 278.99,
        "temp_min": 280.15,
        "temp_max": 283.71,
        "pressure": 1016,
        "humidity": 93
      },
      "wind": {
        "speed": 0.47,
        "deg": 107.538
      },
      "clouds": {
        "all": 2
      },
      "dt": 1560350192,
      "sys": {
        "type": 3,
        "id": 2019346,
        "message": 0.0065,
        "country": "JP",
        "sunrise": 1560281377,
        "sunset": 1560333478
      },
      "timezone": 32400,
      "id": 1851632,
      "name": "Shuzenji",
      "cod": 200
    }


@pytest.fixture(name="valid_entity")
def valid_entity_fixture() -> DataType:

    location = {
      'city_name': 'Shuzenji',
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
class TestOpenWeatherApiMapper:
    class TestToEntity:
        def test_mapper(self, api_payload, valid_entity):
            assert to_entity(api_payload) == valid_entity
            