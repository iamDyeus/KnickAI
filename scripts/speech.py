import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
    
    
   #using pyttsx3 with default windows voice for the time being, until i dont find some solution for any other voice.
