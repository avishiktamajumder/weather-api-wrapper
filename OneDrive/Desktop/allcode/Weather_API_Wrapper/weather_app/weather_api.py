import os
import requests
import redis

redis_url=os.getenv('REDIS_URL','redis://localhost:6379/0')
redis_client=redis.StrictRedis.from_url(redis_url, decode_responses=True)

API_KEY = 'QT52JP3HDR5FWRK3U5WLM2HZE'
BASE_URL='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

def get_weather(city_code):
    cached_data=redis_client.get(city_code)
    if cached_data:
        return cached_data
    url = f'{BASE_URL}{city_code}?unitGroup=metric&key={API_KEY}&contentType=json'
    response=requests.get(url)
    if response.status_code==200:
        weather_data=response.json()
        redis_client.setex(city_code,43200,str(weather_data))
        return weather_data
    else:
        return None