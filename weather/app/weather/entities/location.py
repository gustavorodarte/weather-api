from pydantic import BaseModel


class Location(BaseModel):
    city_name: str
    longitude: int
    latitude: int

    class Config:
        allow_mutation = False
