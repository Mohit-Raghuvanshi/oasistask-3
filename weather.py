import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if not data:
        print("Could not fetch weather data. Please check the city name or try again later.")
        return

    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    
    print(f"\nWeather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc.capitalize()}")

def main():
    print("Welcome to the Weather App")
    api_key = "9bfffaf6b5b0b9e6a0145ad5b578fe72"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ").strip()
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
