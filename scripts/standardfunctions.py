import time
import subprocess
import os
import playsound
import speech_recognition as sr
from speech import speak
from console import intro_header

def assistant_introduction():
    print(intro_header)
    playsound._playsoundWin(os.path.join('soundeffects\sfx',"intro.wav"))
    time.sleep(2)


def takeCommand():     
		print("Listening.....")
		r = sr.Recognizer()
		r.dynamic_energy_threshold=False
		r.energy_threshold=4000
		r.pause_threshold = 1
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			said=""
		try:
			print("Recognizing.....")
			said = r.recognize_google(audio,language='en-in')
			print(f"You Said : {said}\n")
		except sr.UnknownValueError :
			print("could not understand audio \n ~Trying Again~")
			return takeCommand()
		except sr.RequestError as e:
			print("Could not request results, check your internet connection; {0}".format(e))
			return "None"

		return said.lower()

def wishMe():
    from datetoday import datetime
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("\n")
        playsound._playsoundWin(os.path.join('soundeffects\sfx',"gm.mp3"))
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        print("\n")
        playsound._playsoundWin(os.path.join('soundeffects\sfx',"ga.mp3"))
        print("Hello,Good Afternoon")
    else:
        print("\n")
        playsound._playsoundWin(os.path.join('soundeffects\sfx',"ge.mp3"))
        print("Hello,Good Evening")


def note(text):
    from datetoday import datetime
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])


def any_random(var):
    import random
    choice=var[random.randint(0,len(var)-1)]
    return choice

''' USAGE : 
salutation=["Hello","Hi","Hey","Howdy","Hola","Bonjour","Greetings","Good Morning","Good Afternoon","Good Evening"]
print(any_random(salutation))
'''
