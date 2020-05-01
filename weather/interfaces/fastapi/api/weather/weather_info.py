from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRouter
from weather.app.weather.services.weather_info_service import get_info
from weather.domain.entities.weather_info import WeatherInfo
from weather.infra.open_weather_api.open_weather_api_service import get_current_weather_by_city


# Router
router = APIRouter()

@router.get(
    "",
    response_model=WeatherInfo,
    status_code=200,
)
async def get_weather_info(city_name: str):
    has_error, result = await get_info(get_current_weather_by_city, city_name)
    if has_error:
        raise HTTPException(status_code=503, detail="Weather Info can not be fetched")
    return result
