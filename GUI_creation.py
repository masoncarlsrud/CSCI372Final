import tkinter as tk
from tkinter import messagebox
from API_integration import get_weather_data, get_forecast_data  # Importing the API integration methods

def create_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")

    # Main frame
    main_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Location input frame
    input_frame = tk.Frame(main_frame, bg="#f0f0f0")
    input_frame.pack(pady=10)

    location_label = tk.Label(input_frame, text="Enter Location:", bg="#f0f0f0", font=("Helvetica", 12))
    location_label.pack(side=tk.LEFT, padx=5)
    location_entry = tk.Entry(input_frame, font=("Helvetica", 12))
    location_entry.pack(side=tk.LEFT, padx=5)

    # Display area frame
    display_frame = tk.Frame(main_frame, bg="#ffffff", bd=2, relief=tk.SUNKEN)
    display_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    weather_display = tk.Text(display_frame, height=10, width=50, bg="#ffffff", font=("Helvetica", 12))
    weather_display.pack(padx=10, pady=10)

    def show_weather():
        location = location_entry.get()
        if location:
            weather_data = get_weather_data(location)
            forecast_data = get_forecast_data(location)
            display_weather(weather_data, forecast_data, weather_display)
        else:
            messagebox.showwarning("Input Error", "Please enter a location")

    # Search button frame
    button_frame = tk.Frame(main_frame, bg="#f0f0f0")
    button_frame.pack(pady=10)

    search_button = tk.Button(button_frame, text="Search", command=show_weather, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
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