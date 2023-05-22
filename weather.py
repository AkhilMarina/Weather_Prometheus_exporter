import time
import requests
from prometheus_client import start_http_server, Gauge

# Replace with your OpenWeatherMap API key
API_KEY = 'your_api_key'

# Replace with the city and country code you want to fetch the weather data for
CITY = 'London,2643743'

# Set the interval at which the script fetches the weather data (in seconds)
INTERVAL = 60

# Define Prometheus Gauges
TEMPERATURE = Gauge('weather_temperature_celsius', 'Temperature in Celsius', ['location'])
HUMIDITY = Gauge('weather_humidity_percent', 'Humidity in percentage', ['location'])

def fetch_weather_data():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return temperature, humidity
    else:
        print(f'Error fetching weather data: {response.status_code}')
        return None, None

def main():
    start_http_server(8000)

    while True:
        temperature, humidity = fetch_weather_data()

        if temperature is not None and humidity is not None:
            TEMPERATURE.labels(location=CITY).set(temperature)
            HUMIDITY.labels(location=CITY).set(humidity)

        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
