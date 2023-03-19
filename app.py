from flask import Flask, render_template, request
from configparser import ConfigParser
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
        if request.method == 'POST':   
              city = request.form.get('city')
              
              result = requests.get(url.format(city, api_key))
              json = result.json()
              city_name = json['name']
              country = json['sys']['country']
              temp = '{:.2f}'.format((json['main']['temp'] - 273.15))
              humidity = json['main']['humidity']
              icon = json['weather'][0]['icon']
              weather = json['weather'][0]['main']
    
              return render_template('index.html', city_name=city_name, country=country, temp=temp, humidity=humidity, icon=icon, weather=weather)
        else:
              city = 'Bangkok'

              result = requests.get(url.format(city, api_key))

              json = result.json()
              city_name = json['name']
              country = json['sys']['country']
              temp = '{:.2f}'.format((json['main']['temp'] - 273.15))
              humidity = json['main']['humidity']
              icon = json['weather'][0]['icon']
              weather = json['weather'][0]['main']

              return render_template('index.html', city_name=city_name, country=country, temp=temp, humidity=humidity, icon=icon, weather=weather)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)