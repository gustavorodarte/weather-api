from fastapi.routing import APIRouter

from . import weather_info


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(weather_info.router, prefix="/info", tags=["Weather Info"])
    return rt


router = _build_router()
