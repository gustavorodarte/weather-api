from functools import partial
from typing import Any, Dict
import pytest
from pydantic import ValidationError
from tests.utils.asserts import assert_validation_error
from weather.domain.entities.weather_info import Location

# Types
DataType = Dict[str, Any]


# Fixtures
@pytest.fixture(name="valid_data")
def valid_data_fixture() -> DataType:
    return {
        "city_name": "Shuzenji",
        "longitude": 139,
        "latitude": 35,
    }


@pytest.fixture(name="invalid_data")
def invalid_data_fixture() -> DataType:
    return {
        "city_name": "some string",
        "longitude": "some  int",
        "latitude": "some int",
    }


@pytest.mark.unit
class TestLocation:
    class TestModel:
        def test_validation(self, valid_data):
            assert Location(**valid_data)

        def test_invalidation(self, invalid_data):
            with pytest.raises(ValidationError):
                Location(**invalid_data)

        def test_immutability(self, valid_data):
            tdi = Location(**valid_data)
            for key in tdi.dict().keys():
                with pytest.raises(TypeError):
                    setattr(tdi, key, "some value")

    class TestCityName:
        assert_validation_error = partial(assert_validation_error, 1, "city_name")

        def test_must_be_str(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"city_name": [1]})
                Location(**valid_data)

            self.assert_validation_error("type_error.str", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("city_name")
                Location(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestLongitude:
        assert_validation_error = partial(assert_validation_error, 1, "longitude")

        def test_must_be_int(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"longitude": "some longitude"})
                Location(**valid_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("longitude")
                Location(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestLatitude:
        assert_validation_error = partial(assert_validation_error, 1, "latitude")

        def test_must_be_int(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.update({"latitude": "some latitude"})
                Location(**valid_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_is_required(self, valid_data):
            with pytest.raises(ValidationError) as excinfo:
                valid_data.pop("latitude")
                Location(**valid_data)

            self.assert_validation_error("value_error.missing", excinfo)
