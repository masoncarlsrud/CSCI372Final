import unittest
import tkinter as tk
from GUI_creation import create_gui, display_weather

class TestGUICreation(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.weather_display = tk.Text(self.root)
        self.weather_display.pack()

    def tearDown(self):
        self.root.destroy()

    def test_display_weather(self):
        weather_data = {
            'cod': 200,
            'name': 'London',
            'main': {'temp': 15.0, 'humidity': 80},
            'wind': {'speed': 5.0},
            'sys': {'sunrise': 1600000000, 'sunset': 1600040000},
            'weather': [{'description': 'clear sky', 'icon': '01d'}]
        }
        forecast_data = {
            'list': [
                {'dt_txt': '2024-11-13 12:00:00', 'main': {'temp': 15.0, 'humidity': 80}, 'wind': {'speed': 5.0}, 'weather': [{'description': 'clear sky', 'icon': '01d'}]},
                {'dt_txt': '2024-11-14 12:00:00', 'main': {'temp': 16.0, 'humidity': 75}, 'wind': {'speed': 4.0}, 'weather': [{'description': 'few clouds', 'icon': '02d'}]},
                {'dt_txt': '2024-11-15 12:00:00', 'main': {'temp': 17.0, 'humidity': 70}, 'wind': {'speed': 3.0}, 'weather': [{'description': 'scattered clouds', 'icon': '03d'}]},
                {'dt_txt': '2024-11-16 12:00:00', 'main': {'temp': 18.0, 'humidity': 65}, 'wind': {'speed': 2.0}, 'weather': [{'description': 'broken clouds', 'icon': '04d'}]},
                {'dt_txt': '2024-11-17 12:00:00', 'main': {'temp': 19.0, 'humidity': 60}, 'wind': {'speed': 1.0}, 'weather': [{'description': 'shower rain', 'icon': '09d'}]}
            ]
        }
        display_weather(weather_data, forecast_data, self.weather_display)
        content = self.weather_display.get("1.0", tk.END)
        self.assertIn("Current Weather in London", content)
        self.assertIn("5 Day Forecast", content)
        self.assertIn("Date: Wednesday, November 13, 2024 12:00 PM", content)

if __name__ == '__main__':
    unittest.main()