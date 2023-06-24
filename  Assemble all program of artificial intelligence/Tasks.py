import pywhatkit
import wikipedia
import datetime
import calendar
from datetime import date



from Body.Speak import Say
from Body.Listening import TakeCommand
from MainFrame.Weather_report_today import weather
from MainFrame.OpenWeb import OpenWebs
from MainFrame.OpenApp import OpenApps
from MainFrame.Files_and_Folder import FilesAndFolders
from MainFrame.Main_computer_task import Main_computer_task
from MainFrame.Create_a_new_project import New_project


# Greeting()

def Aisha_Main():
        command = TakeCommand()

        if command is None or command == "":
                pass

        elif "use your intelligence" in command:
                work = command.replace('use your intelligence ', '')
                Say(f"Use my intelligence {work}")
                pywhatkit.playonyt(work)

        elif 'play music' in command or "play song" in command:
                song = command.replace('play music ', '')
                song = song.replace('play song ', '')
                Say(f"Playing {song} music or song")
                pywhatkit.playonyt(song)

        elif 'youtube search' in command:
                youtube = command.replace('youtube search ', '')
                Say(f"Youtube searching {youtube}")
                pywhatkit.playonyt(youtube)

        elif "search" in command or "tell me about" in command:
                info = command.replace("search ", '')
                info = info.replace("tell me about ", '')
                Say(f'Searching about "{info}" in our Central database.')
                try:
                        info = wikipedia.summary(info, 3)
                        Say(info)
                except wikipedia.exceptions.PageError:
                        Say(f'Sorry, I have no information about "{info}" in our central database.')
                except wikipedia.exceptions.DisambiguationError:
                        Say(f'There are multiple matches for "{info}". Please be more specific.')

        elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                Say(f"Current time is {time}")

        elif 'weather' in command:
                weather()

        elif 'day' in command:
                day = date.today()
                week = calendar.day_name[day.weekday()]
                Say(f"Today is {week}, {day}")

        elif "tik tok download" in command:
                Say("OK, Please enter your preferred Tiktok account username")
                Tiktok_Username = input("Enter tiktok username : ")
                Say("Thanks, I am starting the Process to download Tiktok videos, and please wait")
                # TiktokVideoDownload(Tiktok_Username)
                pass

        elif 'open' in command:
                OpenWebs(command)
                OpenApps(command)
                FilesAndFolders(command)

        elif "create a new project" in command:
                command = command.replace("create a new project ", "")
                Say(command)
                New_project(command)

        elif "computer" in command:
                a = command.replace("the ", "")
                computer_task = a.replace("computer ", "")
                computer_task = computer_task.replace("computer", "")
                Say(f"{computer_task} main system")
                Main_computer_task(computer_task)


        elif any(keyword in command for keyword in ['exit', 'quit', 'bye']):
                Say("Have a good day! See you again. Goodbye.")
                exit()

        else:
                Say("I'm sorry, I don't understand that command.")
                Say(command)


# while True:
#         Aisha_Main()

Aisha_Main()