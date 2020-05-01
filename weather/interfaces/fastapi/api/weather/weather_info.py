from fastapi.routing import APIRouter
from fastapi import FastAPI, HTTPException
from weather.app.weather.services.weather_info_service import get_info
from weather.app.weather.entities.weather_info import WeatherInfo
from weather.infra.open_weather_api.open_weather_api_service import get_current_weather_by_city


# Router
router = APIRouter()

@router.get(
    "",
    response_model=WeatherInfo,
    status_code=200,
)
async def get_weather_info(city_name: str):
    result = await get_info(get_current_weather_by_city, city_name)
    if result['err']:
        raise HTTPException(status_code=503, detail="Weather Info can not be fetched")
    return result
