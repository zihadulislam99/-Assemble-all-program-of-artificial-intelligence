import os

def Main_computer_task(a):
    a = a.strip()
    print(a)
    if a == "shutdown":
        os.system("shutdown /s /t 1")
    elif a == "restart":
        os.system("shutdown /r /t 1")
    elif a in ["log out", "lockout", "logout"]:
        os.system("shutdown -l")
    else:
        print("Unrecognized command. Please try again.")

    print(a)
