from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)
def temp(x):
    return ('%.2f' % (x-273.15))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city_name']
        API_KEY = '1c5516e7f948519fb10e58e1f0d65a8c'
        API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
        response = requests.get(API_URL)
        weather_data = response.json()
        if response.status_code == 200:
            weather = {
                'city_name': city_name,
                'temperature': temp(weather_data['main']['temp']),
                'humidity': weather_data['main']['humidity'],
                'pressure': weather_data['main']['pressure'],
                'wind_speed': weather_data['wind']['speed'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            }
            return render_template('weather.html', weather=weather)
        else:
            return render_template('weather.html', error='City not found')
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)
