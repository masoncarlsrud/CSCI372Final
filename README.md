# CSCI372Final
CSCI372 Final Project

## Weather App

This project is a weather application that fetches real-time weather data from the OpenWeather API and displays it using a graphical user interface (GUI) built with Tkinter.

### Features
- Display current weather conditions including temperature, humidity, wind speed, sunrise, sunset, and weather description with the appropriate icon.
- Show the weather at noon for the next 5 days with the appropriate icon.
- Search for weather information by entering different city names or ZIP codes.
- User-friendly GUI with a clean and intuitive design.

### Requirements
- Python 3.x
- Tkinter
- Pillow (PIL)
- Requests

### Installation
1. **Clone the repository**:
   - ```sh
   - git clone https://github.com/masoncarlsrud/CSCI372Final.git
   - cd CSCI372Final
2. **Install required Python Packages**
    - pip install requests pillow

### Running Application
- python main.py
- Enter a location or Zip code and click the search button

### Developer Guide
1. **Code Structure**
    - GUI_creation.py: Contains the code for creating the GUI and displaying weather data.
    - main.py: The entry point of the application that initializes and runs the GUI.
    - API_integration.py: Contains functions for fetching weather data from the OpenWeather API.
    - tests/: Contains unit tests and integration tests for the project.
2. **Key Functions**
    - create_gui(): Initializes and runs the Tkinter GUI.
    - show_weather(): Fetches weather data and updates the GUI with the current weather and       forecast.
    - create_image(icon_code, display_area): Fetches and displays weather icons in the GUI.
    - display_weather(weather_data, forecast_data, display_area): Updates the GUI with the current weather and forecast data.
3. **Libraries Used**
    - tkinter: For creating the graphical user interface.
    - requests: For making HTTP requests to fetch data from the OpenWeather API.
    - Pillow (PIL): For handling and displaying images in the GUI.
    - datetime: For handling date and time data.
4. **Running the Tests**
    - To run the tests, navigate to the tests directory and execute the following command:
    python -m unittest discover
