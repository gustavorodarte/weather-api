from pydantic import BaseModel, Field

class WeatherInfo(BaseModel):
    city_name: str
    temp: float
    temp_min: float
    temp_max: float 
    main: str

    class Config:
        allow_mutation = False