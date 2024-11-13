import unittest
from API_integration import get_weather_data, get_forecast_data

class TestAPIIntegration(unittest.TestCase):

    def test_get_weather_data(self):
        location = "London"
        data = get_weather_data(location)
        self.assertEqual(data['name'], "London")
        self.assertIn('main', data)
        self.assertIn('weather', data)

    def test_get_forecast_data(self):
        location = "London"
        data = get_forecast_data(location)
        self.assertIn('list', data)
        self.assertGreater(len(data['list']), 0)

if __name__ == '__main__':
    unittest.main()
