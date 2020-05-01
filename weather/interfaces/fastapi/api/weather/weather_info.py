from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse  # type: ignore
from weather.app.weather.services.weather_info_service import get_info
from weather.app.weather.entities.weather_info import WeatherInfo
from weather.infra.open_weather_api.open_weather_api_service import (
    get_current_weather_by_city,
)

# Router
router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=WeatherInfo,
    status_code=200,
    responses={200: {"description": "Items found"},},
)
async def get_weather_info(city_name: str):
    result = await get_info(city_name, get_current_weather_by_city)
    return result
