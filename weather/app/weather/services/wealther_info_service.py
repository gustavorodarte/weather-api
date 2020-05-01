
from weather.infra.open_weather_api.open_weather_api_service import get_current_weather_by_city

async def get_info(city_name: str):
  result = await get_current_weather_by_city(city_name)
  return result