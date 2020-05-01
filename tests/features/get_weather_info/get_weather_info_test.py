import pytest
from fastapi.testclient import TestClient
from weather.config.environment import get_current_settings
from weather.app.weather.entities.weather_info import WeatherInfo, Location, CurrentWeather
from weather.interfaces.fastapi.app import init_app

_SETTINGS = get_current_settings()

_SETTINGS.ENV = "testing"

@pytest.fixture(name="test_client")
def test_client_fixture():
  return TestClient(init_app(_SETTINGS))

@pytest.fixture(name="r_mock")
def requests_mock_fixture():
  return requests_mock.Mocker(real_http=False)

    
@pytest.fixture(name="valid_response")
def valid_response_fixture():
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
 
    return WeatherInfo(**weather_info).dict()


@pytest.mark.integration
class TestGetWeatherInfo:
    def test_success(self, test_client, valid_response):
        with test_client:
            response = test_client.get(f"weather/info?city_name=New%20York")
            data, status_code = response.json(), response.status_code
            assert status_code == 200
            assert data == valid_response

    def test_service_unavailable(self, test_client):
        with test_client:
            response = test_client.get(f"weather/info?city_name=New%20York")
            data, status_code = response.json(), response.status_code
            assert status_code == 503
            assert data['detail'] == "Weather Info can not be fetched"