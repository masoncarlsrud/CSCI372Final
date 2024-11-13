# Test Cases

This directory contains test cases for the Weather App project. The tests are divided into unit tests and integration tests to verify the functionality and reliability of the application.

## Unit Tests

### `test_API_integration.py`

- **test_get_weather_data**: Tests the `get_weather_data` function to ensure it returns valid weather data for a given location.
- **test_get_forecast_data**: Tests the `get_forecast_data` function to ensure it returns valid forecast data for a given location.

## Integration Tests

### `test_GUI_creation.py`

- **test_display_weather**: Tests the `display_weather` function to ensure it correctly updates the `Text` widget with current weather and forecast data.

## Running the Tests

To run the tests, navigate to the `tests` directory and execute the following command:

```sh
python -m unittest discover