from flask import Flask, render_template, request
from weather_api import get_weather

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    weather_data=None
    if request.method == 'POST':
        city_code = request.form['city_code']
        weather_data=get_weather(city_code)
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)