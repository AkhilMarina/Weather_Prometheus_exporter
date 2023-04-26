
# Weather Metrics Exporter

This is a simple Python script that fetches weather data from the OpenWeatherMap API and exports the temperature and humidity as Prometheus metrics.

Taking advantage of client libraries Python provides, I am using a Python script to push the data points for prometheus to scrape via API.

## Features

- Fetches weather data for a specified city
- Exports temperature in Celsius and humidity in percentage as Prometheus metrics
- Configurable interval for fetching weather data

## Requirements

- Python 3
- `requests` library
- `prometheus_client` library

## Setup

1. Install required Python libraries:

```bash
pip install requests prometheus_client
```

2. Replace the placeholder `API_KEY` with your OpenWeatherMap API key:

```python
API_KEY = 'your_api_key_here'
```

  You can obtain an API key by signing up at [OpenWeatherMap](https://openweathermap.org/).

3. Replace the `CITY` variable with the desired city and its corresponding city ID:

```python
CITY = 'City_name,City_ID'
```

  You can find the city ID in the [OpenWeatherMap city list](http://bulk.openweathermap.org/sample/).

4. (Optional) Adjust the `INTERVAL` variable to control the frequency of data fetching (in seconds):

```python
INTERVAL = 60
```

## Running the script

To run the script, simply execute the following command:

```bash
python weather_metrics_exporter.py
```

By default, the script will start an HTTP server on port 8000, serving the metrics at the `/metrics` endpoint. You can then configure Prometheus to scrape the metrics from this endpoint.

## Metrics

The following metrics are exported:

- `weather_temperature_celsius`: Temperature in Celsius, labeled by the city
- `weather_humidity_percent`: Humidity in percentage, labeled by the city

Example of metrics output:

```
weather_temperature_celsius{location="London,2643743"} 12.34
weather_humidity_percent{location="London,2643743"} 67.0
```

Now you can easily monitor the weather data of your desired city using this script and visualize the metrics using Prometheus and Grafana, or any other visualization tool that supports Prometheus.
## Authors

- [@AkhilMarina](https://github.com/AkhilMarina)

