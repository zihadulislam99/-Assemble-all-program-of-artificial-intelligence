import speech_recognition as sr

def DoWork_or_NoWork():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print("Yes or Not...")
            audio = r.listen(source, 8)
            query = r.recognize_google(audio, language="en")
            query = query.lower()

            query = query.replace("now", "y")
            query = query.replace("yes", "y")
            query = query.replace("yep", "y")
            query = query.replace("yeah", "y")
            query = query.replace("yah", "y")
            query = query.replace("positive", "y")
            query = query.replace("always", "y")

            query = query.replace("no", "n")
            query = query.replace("never", "n")
            query = query.replace("nothing", "n")
            query = query.replace("nthing", "n")
            query = query.replace("negative", "n")

            if "y" in query or "n" in query:
                return query
            else:
                return ""
    except:
        return ""

while True:
    a = DoWork_or_NoWork()
    print(a)