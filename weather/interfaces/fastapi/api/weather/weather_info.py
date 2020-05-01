from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse  # type: ignore
from weather.app.weather.services.wealther_info_service import get_info
from weather.app.weather.entities.weather_info import WeatherInfo


# Router
router = APIRouter()

@router.get(
    "",
    response_class=JSONResponse,
    response_model=WeatherInfo,
    status_code=200,
    responses={
        200: {"description": "Items found"},
    },
)
# @database.transaction()
async def get_weather_info(city_name: str):
    result = await get_info(city_name)
    return result