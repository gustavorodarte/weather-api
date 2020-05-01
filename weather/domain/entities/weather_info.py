from pydantic import BaseModel, Field
from .current_weather import CurrentWeather
from .location import Location


class WeatherInfo(BaseModel):
    location: Location
    current_weather: CurrentWeather

    class Config:
        allow_mutation = False
