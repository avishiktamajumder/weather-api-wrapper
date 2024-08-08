import requests
import redis 
import json

#setting up Redis client
redis_client=redis.StrictRedis(host='localhost', port=6379, db=0)

#Function to get weather data
def get_weather(city_code):
    cached = redis_client.get(city_code)
    if cached:
        print("Fetching data from cache...")
        return json.loads(cached)
    
    print("Fetching data from API...")
    api_key='QT52JP3HDR5FWRK3U5WLM2HZE'
    url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_code}?key={api_key}"

    response=requests.get(url)
    weather_data=response.json()

    #pushing the API response to cache
    redis_client.setex(city_code,43200, json.dumps(weather_data)) #set 12 hour TTL for the cached data

    return weather_data
