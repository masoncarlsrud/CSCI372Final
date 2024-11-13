import requests

# API key for the OpenWeatherMap API
API_KEY = '1cf88f423b39a4468b0d258e1af5a7e7'

# Function to get the weather data from the OpenWeatherMap API
def get_weather_data(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=imperial'
    response = requests.get(url)
    return response.json()

# Function to get the forecast data from the OpenWeatherMap API
def get_forecast_data(location):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=imperial'
    response = requests.get(url)
    return response.json()