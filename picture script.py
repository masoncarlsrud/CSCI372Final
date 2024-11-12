import os
import requests

# List of icon codes from OpenWeatherMap
icon_codes = [
    "01d", "01n", "02d", "02n", "03d", "03n", "04d", "04n",
    "09d", "09n", "10d", "10n", "11d", "11n", "13d", "13n", "50d", "50n"
]

# Create the icons directory if it doesn't exist
os.makedirs("icons", exist_ok=True)

# Base URL for OpenWeatherMap icons
base_url = "http://openweathermap.org/img/wn/"

# Download each icon
for icon_code in icon_codes:
    icon_url = f"{base_url}{icon_code}@2x.png"
    response = requests.get(icon_url)
    if response.status_code == 200:
        with open(f"icons/{icon_code}.png", "wb") as file:
            file.write(response.content)
        print(f"Downloaded {icon_code}.png")
    else:
        print(f"Failed to download {icon_code}.png")