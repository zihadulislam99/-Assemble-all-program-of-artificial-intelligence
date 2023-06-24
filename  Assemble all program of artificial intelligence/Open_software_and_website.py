import os
import keyboard
import pyautogui
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

pyautogui.press('win')