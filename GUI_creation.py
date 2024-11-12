import tkinter as tk
from tkinter import messagebox

from API_integration import get_weather_data, get_forecast_data

def create_gui():
    root = tk.Tk()
    root.title("Weather App")

    # Location input
    location_label = tk.Label(root, text="Enter Location:")
    location_label.pack()
    location_entry = tk.Entry(root)
    location_entry.pack()

    # Display area
    weather_display = tk.Text(root, height=10, width=50)
    weather_display.pack()

    def show_weather():
        location = location_entry.get()
        if location:
            weather_data = get_weather_data(location)
            forecast_data = get_forecast_data(location)
            display_weather(weather_data, forecast_data, weather_display)
        else:
            messagebox.showwarning("Input Error", "Please enter a location")

    # Search button
    search_button = tk.Button(root, text="Search", command=show_weather)
    search_button.pack()

    root.mainloop()

def display_weather(weather_data, forecast_data, display_area):
    display_area.delete(1.0, tk.END)
    if weather_data.get('cod') == 200:
        current_weather = f"Current Weather in {weather_data['name']}:\n"
        current_weather += f"Temperature: {weather_data['main']['temp']}°F\n"
        current_weather += f"Humidity: {weather_data['main']['humidity']}%\n"
        current_weather += f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
        current_weather += f"Description: {weather_data['weather'][0]['description']}\n\n"
        display_area.insert(tk.END, current_weather)

        forecast = "5 Day Forecast:\n"
        for item in forecast_data['list'][:5]:
            forecast += f"Date: {item['dt_txt']}\n"
            forecast += f"Temperature: {item['main']['temp']}°F\n"
            forecast += f"Description: {item['weather'][0]['description']}\n\n"
        display_area.insert(tk.END, forecast)
    else:
        display_area.insert(tk.END, "Error fetching weather data")

if __name__ == "__main__":
    create_gui()