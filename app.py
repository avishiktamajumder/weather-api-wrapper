from flask import Flask, jsonify, request, send_from_directory
from weather_api import get_weather

app=Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    city_code=request.args.get('city_code')
    if not city_code:
        return jsonify({"error":"City code parameter is missing"}),400
    
    weather_data=get_weather(city_code)
    return jsonify(weather_data)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True, host='0.0.0.0', port=port)
