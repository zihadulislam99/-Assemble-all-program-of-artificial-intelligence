import speech_recognition as sr

def TakeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en")
            print("=======================Test_the_setting=======================")
            print(query)
            query = query.lower()
            query = query.replace("ayesha", "aisha")
            query = query.replace("asha", "aisha")
            query = query.replace("aisa", "aisha")
            print(query)
            if "aisha" in query or "artificial intelligence" in query:
                query = query.replace("aisha ", "")
                query = query.lower()
                print(query)
                print("==============================================================")
                return
            # print("==============================================================")
            # return query
    except:
        pass
