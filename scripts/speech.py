
def google_speak(text):
    import os
    from gtts import gTTS
    from playsound import playsound
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")


google_speak("Hello, world!")
    

