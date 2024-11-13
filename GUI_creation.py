import tkinter as tk
from tkinter import messagebox
from API_integration import get_weather_data, get_forecast_data  # Importing the API integration methods
from datetime import datetime  # Importing the datetime module
from PIL import Image, ImageTk  # Importing the Pillow library
import requests
from io import BytesIO

def create_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("600x600")
    root.configure(bg="gray")  # Change background color to gray

    # General font
    general_font = ("Times New Roman", 14)

    # Title label
    title_label = tk.Label(root, text="Weather App", bg="gray", font=("Times New Roman", 24, "bold"))
    title_label.pack(pady=10)

    # Main background
    main_frame = tk.Frame(root, bg="gray", padx=10, pady=10)
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Location input
    input_frame = tk.Frame(main_frame, bg="gray")
    input_frame.pack(pady=10)

    location_label = tk.Label(input_frame, text="Enter Location:", bg="gray", font=general_font)
    location_label.pack(side=tk.LEFT, padx=5)
    location_entry = tk.Entry(input_frame, font=general_font)
    location_entry.pack(side=tk.LEFT, padx=5)

    # Display area frame
    display_frame = tk.Frame(main_frame, bg="gray", bd=2, relief=tk.SUNKEN)
    display_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Adding a scrollbar
    scrollbar = tk.Scrollbar(display_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    weather_display = tk.Text(display_frame, height=15, width=60, bg="gray", font=general_font, yscrollcommand=scrollbar.set)
    weather_display.pack(padx=10, pady=10)

    scrollbar.config(command=weather_display.yview)

    # Store image references in the Text widget
    weather_display.image_references = []

    def show_weather():
        location = location_entry.get()
        if location:
            weather_data = get_weather_data(location)
            forecast_data = get_forecast_data(location)
            display_weather(weather_data, forecast_data, weather_display)
        else:
            messagebox.showwarning("Input Error", "Please enter a location")

    # Search button frame
    button_frame = tk.Frame(main_frame, bg="gray")
    button_frame.pack(pady=10)

    search_button = tk.Button(button_frame, text="Search", command=show_weather, font=general_font, bg="#00796b", fg="#ffffff")
    search_button.pack()

    root.mainloop()

def create_image(icon_code, display_area):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    try:
        response = requests.get(icon_url)
        icon_image = Image.open(BytesIO(response.content))
        icon_image = icon_image.resize((50, 50), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
        icon_photo = ImageTk.PhotoImage(icon_image)
        display_area.image_references.append(icon_photo)  # Keep a reference to avoid garbage collection
        display_area.image_create(tk.END, image=icon_photo)
    except Exception as e:
        display_area.insert(tk.END, f"Error loading icon: {e}\n\n")

def display_weather(weather_data, forecast_data, display_area):
    display_area.delete(1.0, tk.END)
    if weather_data.get('cod') == 200:
        current_weather = (
            f"Current Weather in {weather_data['name']}:\n"
            f"Temperature: {weather_data['main']['temp']}°F\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} mph\n"
            # Convert sunrise and sunset timestamps to human-readable format
            f"Sunrise: {datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%I:%M %p')}\n"
            f"Sunset: {datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%I:%M %p')}\n"
            f"Description: {weather_data['weather'][0]['description']}\n\n"
        )
        
        # Fetch and add weather icon for current weather
        icon_code = weather_data['weather'][0]['icon']
        display_area.insert(tk.END, current_weather)
        create_image(icon_code, display_area) #actually creating the image to input into the GUI
        display_area.insert(tk.END, "\n\n")

        forecast = "5 Day Forecast:\n"
        display_area.insert(tk.END, forecast)
        noon_forecasts = [item for item in forecast_data['list'] if '12:00:00' in item['dt_txt']]
        for item in noon_forecasts[:5]:
            date_time_obj = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
            formatted_date = date_time_obj.strftime('%A, %B %d, %Y %I:%M %p')
            
            entry = (
                f"Date: {formatted_date}\n"
                f"Temperature: {item['main']['temp']}°F\n"
                f"Humidity: {item['main']['humidity']}%\n"
                f"Wind Speed: {item['wind']['speed']} mph\n"
                f"Description: {item['weather'][0]['description']}\n"
            )
            
            display_area.insert(tk.END, entry)
            icon_code = item['weather'][0]['icon']
            create_image(icon_code, display_area)
            display_area.insert(tk.END, "\n\n")
    else:
        display_area.insert(tk.END, "Error fetching weather data")