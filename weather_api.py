import os
import requests
import redis 
import json

#setting up Redis client
redis_url=os.getenv('REDIS_URL')
redis_client=redis.StrictRedis.from_url(redis_url, ssl=True)

#Function to get weather data
def get_weather(city_code):
    cached = redis_client.get(city_code)
    if cached:
        return cached.decode('utf-8')
    
    print("Fetching data from API...")
    api_key='QT52JP3HDR5FWRK3U5WLM2HZE'
    url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_code}?key={api_key}"

    response=requests.get(url)
    weather_data=response.json()

    #pushing the API response to cache
    redis_client.setex(city_code,43200, weather_data) #set 12 hour TTL for the cached data

    return weather_data
