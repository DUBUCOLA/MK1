from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    beach_name = request.args.get('beach', '')
    api_key = 'YOUR_API_KEY'
    
    
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={beach_name}')
    weather_data = response.json()
    
    
    
    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
