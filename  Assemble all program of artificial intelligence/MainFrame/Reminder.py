import datetime
import time

def addZero(number):
    if number < 10:
        a = (f"0{number}")
        return a
    else:
        return number

def set_reminder(reminder_text, reminder_time):

    while True:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        if current_time == reminder_time:
            return reminder_text
        else:
            time.sleep(60)

reminder_text = input("Enter your reminder message: ")

R_hour = addZero(int(input("Enter the hour for your reminder: ")))
R_minute = addZero(int(input("Enter the minute for your reminder: ")))
R_AmPm = input("Enter the AM/PM for your reminder: ").upper()
reminder_time = (f"{R_hour}:{R_minute} {R_AmPm}")

print(set_reminder(reminder_text, reminder_time))