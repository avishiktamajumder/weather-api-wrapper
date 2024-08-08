from flask import Flask, jsonify, request
from weather_api import get_weather

app=Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    city_code=request.args.get('city_code')
    if not city_code:
        return jsonify({"error":"City code parameter is missing"}),400
    
    weather_data=get_weather(city_code)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
