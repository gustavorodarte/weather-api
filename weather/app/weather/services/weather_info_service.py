async def get_info(fetch_weather_info, city_name):
    result = await fetch_weather_info(city_name)
    return result
