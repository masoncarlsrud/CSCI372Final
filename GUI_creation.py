import tkinter as tk
from tkinter import messagebox
from API_integration import get_weather_data, get_forecast_data  # Importing the API integration methods
from datetime import datetime  # Importing the datetime module

def create_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("600x600")
    root.configure(bg="#e0f7fa")

    # General font
    general_font = ("Times New Roman", 14)

    # Title label
    title_label = tk.Label(root, text="Weather App", bg="#e0f7fa", font=("Times New Roman", 24, "bold"))
    title_label.pack(pady=10)

    # Main background
    main_frame = tk.Frame(root, bg="#e0f7fa", padx=10, pady=10)
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Location input
    input_frame = tk.Frame(main_frame, bg="#e0f7fa")
    input_frame.pack(pady=10)

    location_label = tk.Label(input_frame, text="Enter Location:", bg="#e0f7fa", font=general_font)
    location_label.pack(side=tk.LEFT, padx=5)
    location_entry = tk.Entry(input_frame, font=general_font)
    location_entry.pack(side=tk.LEFT, padx=5)

    # Display area frame
    display_frame = tk.Frame(main_frame, bg="#ffffff", bd=2, relief=tk.SUNKEN)
    display_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Adding a scrollbar
    scrollbar = tk.Scrollbar(display_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    weather_display = tk.Text(display_frame, height=15, width=60, bg="#ffffff", font=general_font, yscrollcommand=scrollbar.set)
    weather_display.pack(padx=10, pady=10)

    scrollbar.config(command=weather_display.yview)

    def show_weather():
        location = location_entry.get()
        if location:
            weather_data = get_weather_data(location)
            forecast_data = get_forecast_data(location)
            display_weather(weather_data, forecast_data, weather_display)
        else:
            messagebox.showwarning("Input Error", "Please enter a location")

    # Search button frame
    button_frame = tk.Frame(main_frame, bg="#e0f7fa")
    button_frame.pack(pady=10)

    search_button = tk.Button(button_frame, text="Search", command=show_weather, font=general_font, bg="#00796b", fg="#ffffff")
    search_button.pack()

    root.mainloop()

def display_weather(weather_data, forecast_data, display_area):
    display_area.delete(1.0, tk.END)
    if weather_data.get('cod') == 200:
        current_weather = f"Current Weather in {weather_data['name']}:\n"
        current_weather += f"Temperature: {weather_data['main']['temp']}°F\n"
        current_weather += f"Humidity: {weather_data['main']['humidity']}%\n"
        current_weather += f"Wind Speed: {weather_data['wind']['speed']} mph\n"
        current_weather += f"Description: {weather_data['weather'][0]['description']}\n\n"
        display_area.insert(tk.END, current_weather)

        forecast = "5 Day Forecast:\n"
        x = 4
        for item in forecast_data['list'][:40]:
            if x % 8 == 0:
                date_time_obj = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
                formatted_date = date_time_obj.strftime('%A, %B %d, %Y %I:%M %p')
                forecast += f"Date: {formatted_date}\n"
                forecast += f"Temperature: {item['main']['temp']}°F\n"
                forecast += f"Description: {item['weather'][0]['description']}\n\n"
            x += 1
        display_area.insert(tk.END, forecast)
    else:
        display_area.insert(tk.END, "Error fetching weather data")