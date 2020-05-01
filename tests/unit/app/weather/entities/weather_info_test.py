from functools import partial
from typing import Any, Dict
import pytest
from pydantic import ValidationError
from tests.utils.asserts import assert_validation_error
from weather.domain.entities.weather_info import WeatherInfo, Location, CurrentWeather

# Types
DataType = Dict[str, Any]


# Fixtures
@pytest.fixture(name="valid_data")
def valid_data_fixture() -> DataType:

    location = {
        "city_name": "Shuzenji",
        "longitude": 139,
        "latitude": 35,
    }

    current_weather = {
        "temp": 281.52,
        "max_temp": 283.71,
        "min_temp": 280.15,
        "weather_description": "clear sky",
        "humidity": 1016,
        "pressure": 93,
    }

    return {
        "location": Location(**location),
        "current_weather": CurrentWeather(**current_weather),
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture() -> DataType:
    return {"location": "some location", "current_weather": ["some string"]}


@pytest.mark.unit
class TestWeatherInfo:
    class TestModel:
        def test_validation(self, valid_data):
            assert WeatherInfo(**valid_data)

        def test_invalidation(self, invalid_data):
            with pytest.raises(ValidationError):
                WeatherInfo(**invalid_data)

        def test_immutability(self, valid_data):
            tdi = WeatherInfo(**valid_data)
            for key in tdi.dict().keys():
                with pytest.raises(TypeError):
                    setattr(tdi, key, "some value")

    class TestCurrentWeather:
        assert_validation_error = partial(assert_validation_error, 1, "current_weather")

        def test_must_be_dict(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"current_weather": "some current_weather"})
                WeatherInfo(**valid_data)

            self.assert_validation_error("type_error.dict", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("current_weather")
                WeatherInfo(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestLocation:
        assert_validation_error = partial(assert_validation_error, 1, "location")

        def test_must_be_dict(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"location": "some location"})
                WeatherInfo(**valid_data)

            self.assert_validation_error("type_error.dict", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("location")
                WeatherInfo(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)
