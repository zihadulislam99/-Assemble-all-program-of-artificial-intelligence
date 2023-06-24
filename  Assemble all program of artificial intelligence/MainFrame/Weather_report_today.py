import requests
from Body.Speak import Say

def weather():
    API_keys = "8d572482eaf8471d952163558232105"
    City = "Shariatpur,Bangladesh"

    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_keys}&q={City}&aqi=no").json()
    Celsius = response["current"]["temp_c"]
    Fahrenheit = response["current"]["temp_f"]
    Weather_type = response["current"]["condition"]["text"]
    Humidity = response["current"]["humidity"]
    Weather = (f"Today is {Celsius}° Celsius and {Fahrenheit}° Fahrenheit,\nor today is {Weather_type} day and humidity is {Humidity}%")
    Say(Weather)