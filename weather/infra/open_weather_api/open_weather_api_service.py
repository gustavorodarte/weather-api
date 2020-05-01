from weather.config.environment import get_current_settings
from weather.infra.open_weather_api.open_weather_api_mapper import to_entity
from weather.app.weather.entities.weather_info import WeatherInfo
import requests_async as requests

_SETTINGS = get_current_settings()


async def make_request(city_name: str):
    payload = {"q": city_name, "appid": _SETTINGS.OPEN_WEATHER_MAP_API_TOKEN}
    result = await requests.get(
        f"http://{_SETTINGS.OPEN_WEATHER_MAP_URL}/weather/", params=payload
    )
    return result.json()


async def get_current_weather_by_city(city_name: str) -> WeatherInfo:
    result = await make_request(city_name)
    return to_entity(result)
