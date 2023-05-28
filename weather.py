
import tkinter as tk
import os
import requests


os.environ["DISPLAY"] = "0"

# Create the main window.
root = tk.Tk()

# Create a label to display the city name.
city_label = tk.Label(text="City:")

# Create an entry box to enter the city name.
city_entry = tk.Entry()

# Create a button to get the weather.
get_weather_button = tk.Button(text="Get Weather", command=get_weather)

# Layout the widgets.
city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
get_weather_button.grid(row=1, column=0)


# Start the main loop.
root.mainloop()


def get_weather():
    # Get the city name from the entry box.
    city = city_entry.get()
    
    # https://api.openweathermap.org/data/2.5/weather?q=london&appid=c291711997e91ed2b8660eee81fe4382
    # Make an API request to get the weather for the city.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR_API_KEY".format(city)
    response = requests.get(url)

    # Check if the request was successful.
    if response.status_code == 200:
        # Parse the JSON response.
        data = response.json()

        # Get the weather information.
        weather = data["weather"][0]
        temperature = data["main"]["temp"]

        # Display the weather information in a label.
        weather_label = tk.Label(text="Weather: {} {}°C".format(weather["description"], temperature))
        weather_label.grid(row=2, column=0)
    else:
        # Display an error message if the request was not successful.
        error_label = tk.Label(text="Error getting weather information.")
        error_label.grid(row=2, column=0)
