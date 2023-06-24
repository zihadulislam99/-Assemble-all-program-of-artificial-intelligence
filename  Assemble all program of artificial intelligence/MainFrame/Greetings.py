import calendar
import datetime
import requests
from datetime import date
from Body.Speak import Say

def Greeting():
    Gtime = datetime.datetime.now().hour
    time = datetime.datetime.now().strftime('%I:%M %p')
    day = date.today()
    week = calendar.day_name[day.weekday()]

    API_keys = "8d572482eaf8471d952163558232105"
    City = "Shariatpur,Bangladesh"
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_keys}&q={City}&aqi=no").json()
    Celsius = response["current"]["temp_c"]
    Weather_type = response["current"]["condition"]["text"]
    Humidity = response["current"]["humidity"]
    Weather = (f"Today is {Celsius}° Celsius, or it is {Weather_type} day and humidity is {Humidity}%")

    print(Gtime)
    if Gtime>=4 and Gtime<12:
        Say("Good morning")

    elif Gtime>=12 and Gtime<18:
        Say("Good afternoon")

    elif Gtime>=18 and Gtime<=24:
        Say("Good evening")
    else:
        Say("Good night")



    Say(f"Welcome back, Current time is {time} and Today is {week}, {day}, {Weather}")

Greeting()