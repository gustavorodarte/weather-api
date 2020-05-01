from weather.config.environment import get_current_settings
from weather.infra.open_weather_api.open_weather_api_mapper import to_entity
import requests_async as requests
from typing import Tuple, Any


_SETTINGS = get_current_settings()


async def make_request(city_name: str):
    payload = {"q": city_name, "appid": _SETTINGS.OPEN_WEATHER_MAP_API_TOKEN}
    result = await requests.get(
        f"{_SETTINGS.OPEN_WEATHER_MAP_URL}/weather/", params=payload
    )
    return result.json()


async def get_current_weather_by_city(city_name: str) -> Tuple[bool, Any]:
    request_result = await make_request(city_name)
    if request_result["cod"] == 200:
        return False, to_entity(request_result)

    return True, None
