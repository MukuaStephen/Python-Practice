import requests

def get_weather(city):
    # Replace with your actual API key
    API_KEY = 'c4c49c5ca683eef5722b63cb52ff6d59'
    
    # Step 1: Get latitude and longitude for the city
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geocode_response = requests.get(geocoding_url)
    
    if geocode_response.status_code == 200 and geocode_response.json():
        location = geocode_response.json()[0]
        lat, lon = location['lat'], location['lon']
        
        # Step 2: Get weather data based on latitude and longitude
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
        response = requests.get(weather_url)
        
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            description = data['weather'][0]['description']

            print(f"Temperature in {city}: {temperature:.2f}°C")
            print(f"Weather description: {description}")
        else:
            print("Error fetching weather data.")
    else:
        print("Error fetching location data for the city.")

# Example usage
city = input("Enter the city name: ")
get_weather(city)




