import pyttsx3

def Say(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 175)
    print(text)
    engine.say(text)
    engine.runAndWait()
# Say("hello, my name is artificial intelligence")