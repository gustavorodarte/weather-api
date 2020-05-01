from typing import Awaitable, Callable, Iterable, Optional, Tuple, TypeVar

from weather.app.weather.entities.weather_info import WeatherInfo

FetchWeatherFnType = Callable[[str], Awaitable[WeatherInfo]]


async def get_info(fetch_weather_info: FetchWeatherFnType, city_name: str) -> WeatherInfo:
    result = await fetch_weather_info(city_name)
    return result
