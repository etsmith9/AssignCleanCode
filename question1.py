#question1.py

#Task 1: Identifying and Creating Classes Analyze the provided script and 
# identify distinct functionalities that can be encapsulated into classes. 
# Create classes that represent different aspects of the weather forecast 
# application, such as fetching data, parsing data, and user interaction.

#Problem Statement: The existing script for the weather forecast application 
# is written in a procedural style and lacks organization.

# Weather Forecast Application Script

def fetch_weather_data(city):
    weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    normalized_city = city.strip().lower()
    for city_name in weather_data.keys():
        if city_name.lower() == normalized_city:
            return weather_data[city_name]
    return None

def format_detailed_weather_report(city, data):
    if not data:
        return f"Weather data not available for {city}"
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def format_basic_weather_report(city, data):
    if not data:
        return f"Weather data not available for {city}"
    temperature = data["temperature"]
    return f"Weather in {city}: {temperature} degrees"

def get_detailed_weather_forecast(city):
    weather_data = fetch_weather_data(city)
    return format_detailed_weather_report(city, weather_data)

def get_basic_weather_forecast(city):
    weather_data = fetch_weather_data(city)
    return format_basic_weather_report(city, weather_data)

def request_weather_details():
    city = input("\nEnter the city to get weather details or 'exit' to quit  ").lower()
    if city.lower() == 'exit':
        return None, None
    forecast_type = input("Do you want a detailed forecast? (yes/no):  ").lower()
    return city, forecast_type == 'yes'

def main():
    while True:
        city, detailed = request_weather_details()

        if city is None:
            print("Exiting the application.")
            break

        if detailed:
            print(get_detailed_weather_forecast(city))
        else:
            print(get_basic_weather_forecast(city))

if __name__ == "__main__":
    main()