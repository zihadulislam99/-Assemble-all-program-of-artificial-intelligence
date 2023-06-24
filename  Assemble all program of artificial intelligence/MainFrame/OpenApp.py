import os
from Body.Speak import Say

def OpenApps(command):
    apps = [["chrome", "C:\Program Files\Google\Chrome\Application\chrome.exe"],
            ["pycharm", "C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.3\\bin\pycharm64.exe"],
            ["cmd", "C:\Windows\system32\cmd.exe"]
        ]
    for app in apps:
        if f"open {app[0]}" in command:
            Say(f"Opening {app[0]}")
            os.startfile(app[1])
