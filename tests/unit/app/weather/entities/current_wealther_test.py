from functools import partial
from typing import Any, Dict
import pytest
from pydantic import ValidationError
from tests.utils.asserts import assert_validation_error
from weather.app.weather.entities.weather_info import CurrentWeather

# Types
DataType = Dict[str, Any]


# Fixtures
@pytest.fixture(name="valid_data")
def valid_data_fixture() -> DataType:
    return {
      'temp': 281.52,
      'max_temp': 283.71,
      'min_temp': 280.15,
      'weather_description': 'clear sky',
      'humidity': 1016,
      'pressure': 93,
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture() -> DataType:
    return {
      'temp': 'some temp',
      'max_temp': 'some max_temp',
      'min_temp': 'some min temp',
      'weather_description': ['some string'],
      'humidity': 'some string',
      'pressure': '93',
    }


@pytest.mark.unit
class TestLocation:
    class TestModel:
        def test_validation(self, valid_data):
            assert CurrentWeather(**valid_data)

        def test_invalidation(self, invalid_data):
            with pytest.raises(ValidationError):
                CurrentWeather(**invalid_data)

        def test_immutability(self, valid_data):
            tdi = CurrentWeather(**valid_data)
            for key in tdi.dict().keys():
                with pytest.raises(TypeError):
                    setattr(tdi, key, "some value")

    class TestTemp:
        assert_validation_error = partial(assert_validation_error, 1, "temp")

        def test_must_be_float(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"temp": [1]})
                CurrentWeather(**valid_data)

            self.assert_validation_error("type_error.float", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("temp")
                CurrentWeather(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)
   
    class TestMaxTemp:
        assert_validation_error = partial(assert_validation_error, 1, "max_temp")

        def test_must_be_float(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"max_temp": [1]})
                CurrentWeather(**valid_data)

            self.assert_validation_error("type_error.float", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("max_temp")
                CurrentWeather(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)
    
    class TestMinTemp:
        assert_validation_error = partial(assert_validation_error, 1, "min_temp")

        def test_must_be_float(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"min_temp": [1]})
                CurrentWeather(**valid_data)

            self.assert_validation_error("type_error.float", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("min_temp")
                CurrentWeather(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

    
    class TestWeatherDescription:
        assert_validation_error = partial(assert_validation_error, 1, "weather_description")

        def test_must_be_float(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"weather_description": ['some string']})
                CurrentWeather(**valid_data)

            self.assert_validation_error("type_error.str", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("weather_description")
                CurrentWeather(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

    
    class TestHumidity:
        assert_validation_error = partial(assert_validation_error, 1, "humidity")

        def test_must_be_float(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"humidity": 'some string'})
                CurrentWeather(**valid_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("humidity")
                CurrentWeather(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

      
    class TestPressure:
        assert_validation_error = partial(assert_validation_error, 1, "pressure")

        def test_must_be_float(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"pressure": 'some string'})
                CurrentWeather(**valid_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("pressure")
                CurrentWeather(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

