#question1.py

#Task 1: Identifying and Creating Classes Analyze the provided script and 
# identify distinct functionalities that can be encapsulated into classes. 
# Create classes that represent different aspects of the weather forecast 
# application, such as fetching data, parsing data, and user interaction.

#Problem Statement: The existing script for the weather forecast application 
# is written in a procedural style and lacks organization.

# Weather Forecast Application Script

class WeatherData:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

    def fetch(self, city_name):
        city_name_normalized = self.normalize_city_name(city_name)
        return self.weather_data.get(city_name_normalized)

    def normalize_city_name(self, city_name):
        return city_name.strip().title()


class WeatherReport:
    def format_basic(self, city_name, data):
        if not data:
            return f"Weather data not available for {city_name}."
        temperature = data["temperature"]
        return f"Weather in {city_name}: {temperature}°C"

    def format_detailed(self, city_name, data):
        if not data:
            return f"Weather data not available for {city_name}."
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city_name}: {temperature}°C, {condition}, Humidity: {humidity}%"


class WeatherApp:
    def __init__(self):
        self.weather_data = WeatherData()
        self.weather_report = WeatherReport()

    def run(self):
        while True:
            city_name, detailed = self.user_input()

            if city_name == "exit":
                print("Exiting the application.")
                break

            weather_data = self.weather_data.fetch(city_name)
            report = self.generate_report(city_name, weather_data, detailed)
            print(report)

    def user_input(self):
        city_name = input("\nEnter the city to get weather details or 'exit' to quit: ").strip().lower()
        if city_name == "exit":
            return city_name, None

        forecast_type = input("Do you want a detailed forecast? (yes/no): ").lower()
        return city_name, forecast_type == "yes"

    def generate_report(self, city_name, weather_data, detailed):
        if detailed:
            return self.weather_report.format_detailed(city_name, weather_data)
        return self.weather_report.format_basic(city_name, weather_data)


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
