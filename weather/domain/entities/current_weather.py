from pydantic import BaseModel


class CurrentWeather(BaseModel):
    temp: float
    max_temp: float
    min_temp: float
    weather_description: str
    humidity: int
    pressure: int

    class Config:
        allow_mutation = False
