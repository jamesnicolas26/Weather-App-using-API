import requests

API_KEY = 'd19769ea1e6df01a4ed10964f20475ea'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        wind_speed = wind['speed']
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found.")

city = input("Enter city name: ")
get_weather(city)