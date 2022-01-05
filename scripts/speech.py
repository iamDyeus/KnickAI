from gtts import gTTS
def speak(text):                #https://pypi.org/project/gtts/
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    import os
    import playsound
    playsound.playsound("speech.mp3", True)
    os.remove("speech.mp3")


'''
import pyttsx3                  #https://pypi.org/project/pyttsx3/
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
'''

#pyttsx3 was showing an error, so I switched to gTTS
#but still i have not found any better alternative than pyttsx3 and gTTS
#so i will keep them both for now, You decide which one you want to use.