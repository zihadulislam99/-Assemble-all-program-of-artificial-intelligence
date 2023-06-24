# from gtts import gTTS
# import os
#
# def SpeakBangla(text):
#     tts = gTTS(text=text, lang='bn')
#     tts.save("speech.mp3")
#     os.system("speech.mp3")
#
# def SpeakEnglish(text):
#     tts = gTTS(text=text, lang='en')
#     tts.save("speech.mp3")
#     os.system("speech.mp3")
#
#
# SpeakEnglish("text")

from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')